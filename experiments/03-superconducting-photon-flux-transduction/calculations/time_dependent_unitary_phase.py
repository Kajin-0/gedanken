#!/usr/bin/env python3
"""Finite-rise/cooling unitary phase benchmark at the safe Experiment-03 design.

This is the controlled next step after the phase-DVR basis convergence check.
It evolves the retained *one-dimensional phase Hamiltonian* under the actual
20-ps optical deposition and conditional cooling law used by the reduced model:

    H_x(t) = -hbar^2/(2 C Phi_bar^2) d^2/dx^2 + U[x,T_e(t)].

No dissipative bath is included in this script.  Therefore its late-time basin
occupation is NOT detector capture efficiency.  The purpose is to determine how
the exact unitary nonlinear phase dynamics behaves under the real time-dependent
pulse before attaching the already-validated reaction-coordinate environment.

Initial state
-------------
The physically consistent cold local-equilibrium approximation is a mixed state
in the metastable left well,

    rho_L = sum_n p_n |n_L><n_L|,
    p_n proportional exp[-(E_n-E_0)/(k_B T0)],

using the converged hard-wall left-well DVR eigenstates.  This is preferable to
the historical quench script's pure Gaussian with a finite-T coth-broadened
position variance: a finite-temperature harmonic state is mixed, not one such
pure Gaussian.  We also propagate the DVR ground state, a pure harmonic ground
Gaussian, and the historical broadened Gaussian as diagnostics.

The hard wall is an initialization device only; all states are embedded onto a
large full phase grid before time evolution, so the wall is removed at t=0.
"""
from __future__ import annotations

import argparse, math
import numpy as np
from scipy.integrate import cumulative_trapezoid, solve_ivp

import full_dynamic_rfsquid as fd
from quantum_initial_capture import HBAR, KB, PHI_BAR
from phase_dvr_basis_convergence import spectrum

L0=111.5e-12; C0=215e-15
ROOTS={.21200:10.6229699624,.21250:10.885578211,.21300:11.2051409652}


def thermal_history(lambda_um: float, area_um2: float, rise_ps: float, tmax_ps: float):
    u0=fd.T0**2
    Tad=fd.adiabatic_photon_temperature(lambda_um,area_um2)
    du=Tad*Tad-u0
    tau_r=rise_ps*1e-12
    cool=1/(2*fd.TAU0_CONDITIONAL*u0)
    def rhs(t,y):
        u=max(float(y[0]),u0)
        src=du/tau_r*math.exp(-t/tau_r)
        return [src-cool*(u*u-u0*u0)]
    tf=tmax_ps*1e-12
    sol=solve_ivp(rhs,(0,tf),[u0],method='DOP853',rtol=2e-11,atol=1e-14,
                  max_step=max(.2e-12,tau_r/20),dense_output=True)
    if not sol.success: raise RuntimeError(sol.message)
    def Tof(t):
        u=np.maximum(sol.sol(np.asarray(t,float))[0],u0)
        return np.sqrt(u)
    ts=np.linspace(0,tf,20001); TT=Tof(ts)
    return Tof,Tad,ts,TT


def crossings(ts,ys,level):
    z=ys-level; out=[]
    for i in range(len(z)-1):
        if z[i]==0 or z[i]*z[i+1]<0:
            # linear interpolation is ample on the dense diagnostic grid
            f=abs(z[i])/(abs(z[i])+abs(z[i+1])) if z[i+1]!=z[i] else 0.0
            out.append(float(ts[i]+f*(ts[i+1]-ts[i])))
    return out


def potential_table(model,x,Tmax,nT,L):
    Tgrid=np.linspace(fd.T0,Tmax,nT)
    F=np.asarray(model.spline(Tgrid,x,grid=True),float)
    U=cumulative_trapezoid(F,x,axis=1,initial=0.0)*(PHI_BAR**2/L)
    # Remove one arbitrary T-dependent scalar; dynamics are unchanged.
    U-=np.min(U,axis=1)[:,None]
    return Tgrid,U


def interp_potential(T,Tgrid,Utab):
    if T<=Tgrid[0]: return Utab[0]
    if T>=Tgrid[-1]: return Utab[-1]
    q=(T-Tgrid[0])/(Tgrid[-1]-Tgrid[0])*(len(Tgrid)-1)
    i=min(len(Tgrid)-2,max(0,int(q))); f=q-i
    return (1-f)*Utab[i]+f*Utab[i+1]


def embed_state(xsrc,psi,x):
    y=np.interp(x,xsrc,np.real(psi),left=0.0,right=0.0)+1j*np.interp(x,xsrc,np.imag(psi),left=0.0,right=0.0)
    dx=x[1]-x[0]; n=math.sqrt(float(np.sum(np.abs(y)**2)*dx))
    if n==0: raise RuntimeError('embedded state vanished')
    return y/n


def run_one(delta,area,nx,dt_ps,tmax_ps,nT):
    r=ROOTS[delta]; C=C0*r*r
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT; original=fd.CASES[.6]
    try:
        fd.BETA_COLD=.80; fd.DELTA_TILT=delta; fd.CASES[.6]=(L0,C,original[2])
        model=fd.DynamicForce(.6,quick=False,Tmax=1.02)
        roots=model.roots(fd.T0)
        mins=[(q,k) for q,k in roots if k>0]; saddles=[(q,k) for q,k in roots if k<0]
        xm=max(q for q,k in mins if q<0); xr=min(q for q,k in mins if q>0)
        xs=min(saddles,key=lambda z:abs(z[0]))[0]
        km=float(np.asarray(model.spline.ev(fd.T0,xm,dx=0,dy=1)).reshape(-1)[0])
        wm=math.sqrt(km/(L0*C)); Tf=model.fold_temperature(hi=.98)

        Tof,Tad,tcheck,Tcheck=thermal_history(14.,area,20.,tmax_ps)
        Tpeak=float(Tcheck.max()); ipeak=int(np.argmax(Tcheck)); tpeak=tcheck[ipeak]
        cf=crossings(tcheck,Tcheck,Tf)
        tfold_up=cf[0] if cf else float('nan'); tfold_down=cf[-1] if len(cf)>=2 else float('nan')

        xmax=4.2; x=np.linspace(-xmax,xmax,nx,endpoint=False); dx=x[1]-x[0]
        Tgrid,Utab=potential_table(model,x,max(Tpeak,fd.T0)+.003,nT,L0)

        # Converged local left-well basis used for conditional metastable preparation.
        xl,Ul,el,vl,res=spectrum(model,fd.T0,C,-3.8,xs,2200,6)
        dE=el-el[0]; boltz=np.exp(-dE/(KB*fd.T0)); boltz/=boltz.sum()
        states=[embed_state(xl,vl[:,j],x) for j in range(6)]

        # Pure harmonic ground Gaussian and historical finite-T broadened Gaussian.
        sigma0=math.sqrt(HBAR/(2*C*PHI_BAR**2*wm))
        q=HBAR*wm/(2*KB*fd.T0); coth=1/math.tanh(q); sigmaT=sigma0*math.sqrt(coth)
        def gauss(sig):
            y=np.exp(-((x-xm)**2)/(4*sig*sig)).astype(complex)
            return y/math.sqrt(float(np.sum(np.abs(y)**2)*dx))
        states += [gauss(sigma0),gauss(sigmaT)]
        psi=np.stack(states,axis=0)

        k=2*np.pi*np.fft.fftfreq(nx,d=dx); p=HBAR*k; m=C*PHI_BAR**2
        dt=dt_ps*1e-12; K=np.exp(-1j*(p*p/(2*m))*dt/HBAR)
        nsteps=int(round(tmax_ps/dt_ps))
        # sample densely enough to expose coherent recrossing around reformation.
        base=[0.,20.,50.,100.,200.,300.,400.,500.,600.,800.,1000.]
        extra=[]
        for tc in (tfold_up,tfold_down,tpeak):
            if np.isfinite(tc):
                ps=tc*1e12
                extra += [max(0.,ps-25),ps,max(0.,ps+25),max(0.,ps+100)]
        sample_ps=sorted(set(round(t,6) for t in base+extra if 0<=t<=tmax_ps))
        step_to_t={max(0,min(nsteps,int(round(t/dt_ps)))):t for t in sample_ps}

        weights=boltz
        records=[]
        def observe(tps):
            prob=np.sum(np.abs(psi[:,x>xs])**2,axis=1)*dx
            edge=np.sum(np.abs(psi[:,np.abs(x)>.90*xmax])**2,axis=1)*dx
            norms=np.sum(np.abs(psi)**2,axis=1)*dx
            mix=float(np.dot(weights,prob[:6]))
            return dict(t=tps,T=float(Tof(tps*1e-12)),mix=mix,ground=float(prob[0]),
                        hground=float(prob[6]),legacy=float(prob[7]),
                        edge=float(np.max(edge)),normerr=float(np.max(np.abs(norms-1))))
        if 0 in step_to_t: records.append(observe(step_to_t[0]))

        for step in range(1,nsteps+1):
            tm=(step-.5)*dt; Tm=float(Tof(tm)); U=interp_potential(Tm,Tgrid,Utab)
            Vh=np.exp(-.5j*U*dt/HBAR)
            psi*=Vh[None,:]
            psi=np.fft.ifft(np.fft.fft(psi,axis=1)*K[None,:],axis=1)
            psi*=Vh[None,:]
            if step in step_to_t: records.append(observe(step_to_t[step]))

        print(f'delta={delta:.5f} r={r:.10f} C={C*1e12:.6f}pF area={area:g}um2 '
              f'nx={nx} dt={dt_ps:g}ps tmax={tmax_ps:g}ps xm={xm:+.7f} xs={xs:+.7f} xr={xr:+.7f} '
              f'fm={wm/(2*math.pi)*1e-9:.7f}GHz Tf={Tf:.8f}K Tad_no_cool={Tad:.8f}K '
              f'Tpeak={Tpeak:.8f}K tpeak={tpeak*1e12:.3f}ps fold_up={tfold_up*1e12:.3f}ps fold_down={tfold_down*1e12:.3f}ps')
        print('left thermal weights=' + ','.join(f'{w:.9e}' for w in weights) +
              f' ; DVRmaxResidual={float(res.max()):.3e}K sigma0={sigma0:.7f} sigmaLegacyT={sigmaT:.7f}')
        for z in records:
            print(f't={z["t"]:.3f}ps T={z["T"]:.7f}K P_R_mix={z["mix"]:.8f} '
                  f'P_R_DVR0={z["ground"]:.8f} P_R_harm0={z["hground"]:.8f} '
                  f'P_R_legacyPureT={z["legacy"]:.8f} edge={z["edge"]:.3e} normerr={z["normerr"]:.3e}')

        max_init_mix_ground=max(abs(z['mix']-z['ground']) for z in records)
        max_dvr_harm=max(abs(z['ground']-z['hground']) for z in records)
        max_legacy=max(abs(z['ground']-z['legacy']) for z in records)
        max_edge=max(z['edge'] for z in records); max_norm=max(z['normerr'] for z in records)
        # Oscillation range after fold reformation is the key warning against calling
        # this bath-free number a capture probability.
        post=[z['mix'] for z in records if np.isfinite(tfold_down) and z['t']>=tfold_down*1e12]
        post_span=max(post)-min(post) if len(post)>=2 else float('nan')
        msg=(f'delta={delta:.5f} area={area:g}: p0={weights[0]:.8f} p1={weights[1]:.8f} '
             f'max|thermalMix-ground|={max_init_mix_ground:.5f} max|DVR0-harm0|={max_dvr_harm:.5f} '
             f'max|DVR0-legacyPureT|={max_legacy:.5f} postReformSpan={post_span:.5f} '
             f'maxEdge={max_edge:.3e} maxNormErr={max_norm:.3e} foldDown={tfold_down*1e12:.2f}ps')
        print(msg); print(f'::notice title=Experiment 03 finite-pulse unitary phase::{msg}')
        if max_edge>2e-7: raise RuntimeError('FFT box edge occupation too large')
        if max_norm>2e-9: raise RuntimeError('unitary norm drift too large')
        if not np.isfinite(tfold_down): raise RuntimeError('thermal history did not reform left well in benchmark horizon')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot; fd.CASES[.6]=original


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--delta',type=float,default=.212)
    ap.add_argument('--area',type=float,default=490.)
    ap.add_argument('--nx',type=int,default=2048)
    ap.add_argument('--dt-ps',type=float,default=.05)
    ap.add_argument('--tmax-ps',type=float,default=1000.)
    ap.add_argument('--ntemp',type=int,default=241)
    a=ap.parse_args(); d=round(a.delta,5)
    if d not in ROOTS: raise SystemExit(f'supported deltas: {tuple(ROOTS)}')
    run_one(d,float(a.area),int(a.nx),float(a.dt_ps),float(a.tmax_ps),int(a.ntemp))

if __name__=='__main__': main()
