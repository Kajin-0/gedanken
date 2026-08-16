#!/usr/bin/env python3
"""Evaluate the exact passive damping / FDT fluctuation-work metric on capture trajectories.

For the deterministic phase-node voltage V=Phi_bar*x_dot,

    E_diss = int dω/(2π) ReY(ω) |V(ω)|^2

and, using the project's symmetrized FDT convention,

    Var_sym(W_n)
      = int dω/(2π) eps_T(ω) ReY(ω) |V(ω)|^2,

    eps_T = hbar|ω| coth[hbar|ω|/(2kBT)].

Define

    eps_eff = Var_sym(W_n) / E_diss.

The explicit two-pole state-space model also gives the physical resistor Joule
loss

    E_R = int dt (Phi_bar*w)^2/R,

where w is the internal filter-node flux velocity in the dimensionless model.
The spectral and time-domain dissipated energies must agree when the trajectory
is propagated long enough for the filter energy to settle.

This is a prescribed-trajectory linear-bath metric, not an exact nonlinear
capture-error probability.
"""
from __future__ import annotations

import argparse, math
import numpy as np
from scipy.integrate import solve_ivp

import full_dynamic_rfsquid as fd
import nonlinear_fdt_twa_screen as nf
from causal_two_pole_environment import filter_components
from quantum_initial_capture import HBAR, KB, PHI_BAR
import safe_tilt_optimum_worker as sw

C0=215e-15; R0=80.; L0=111.5e-12; ALPHA=.90
ROOTS={
    .21250:10.885578211,
    .21300:11.2051409652,
}


def deterministic_trace(model,area,R,C,wc,wd,tend_ns,lam=14.,rise_ps=20.,sample_ps=.25):
    """Propagate the exact deterministic four-state passive network + thermal pulse.

    This intentionally reproduces the equations used by the energetic-margin
    calculation instead of depending on that helper's reduced return dictionary.
    Uniform dense-output samples provide a transparent FFT trajectory.
    """
    L=L0; Lf,Cf=filter_components(R,wd)
    xc=model.cold_states()[0]
    Tad=fd.adiabatic_photon_temperature(lam,area)
    u0=fd.T0*fd.T0; du=Tad*Tad-u0
    cool=1/(2*fd.TAU0_CONDITIONAL*u0); tr=rise_ps*1e-12
    def src(t): return du/tr*math.exp(-t/tr)
    def rhs(t,y):
        x,v,u,d,w=y; u=max(float(u),u0); T=math.sqrt(u)
        return np.array([
            v,
            -(d+model.force(T,x))/(L*C),
            src(t)-cool*(u*u-u0*u0),
            (L/Lf)*(v-w),
            d/(L*Cf)-w/(R*Cf),
        ])
    tf=tend_ns*1e-9
    sol=solve_ivp(rhs,(0,tf),np.array([xc,0.,u0,0.,0.]),method='DOP853',
                  rtol=2e-10,atol=np.array([1e-12,1e1,1e-15,1e-12,1e1]),
                  max_step=.12e-12,dense_output=True)
    if not sol.success: raise RuntimeError(sol.message)
    dt=sample_ps*1e-12; n=int(round(tf/dt))+1
    t=np.linspace(0,tf,n); y=sol.sol(t)
    return dict(t=t,x=y[0],v=y[1],u=y[2],d=y[3],w=y[4],Tad=Tad,Lf=Lf,Cf=Cf,
                final_filter_K=(0.5*(Lf/L0)*y[3,-1]**2+0.5*L0*Cf*y[4,-1]**2)
                               *(PHI_BAR**2/L0)/KB)


def spectral_metric(t,v,R,wd):
    dt=float(t[1]-t[0]); n=len(t)
    V=PHI_BAR*np.asarray(v,float)
    Vf=dt*np.fft.rfft(V)
    omega=2*math.pi*np.fft.rfftfreq(n,dt)
    reY=(1/R)/(1+(omega/wd)**4)
    z=HBAR*omega/(2*KB*fd.T0)
    eps=np.empty_like(omega)
    small=z<1e-6; large=z>30; mid=~(small|large)
    eps[small]=2*KB*fd.T0
    eps[large]=HBAR*omega[large]
    eps[mid]=HBAR*omega[mid]/np.tanh(z[mid])
    # Two-sided discrete Parseval integral. rfft stores positive frequencies once.
    weight=np.ones_like(omega)
    if n%2==0:
        if len(weight)>2: weight[1:-1]=2
    else:
        if len(weight)>1: weight[1:]=2
    domega=2*math.pi/(n*dt)
    measure=weight*domega/(2*math.pi)*reY*np.abs(Vf)**2
    Ed=float(np.sum(measure))
    Var=float(np.sum(eps*measure))
    wbar=float(np.sum(omega*measure)/Ed)
    return Ed,Var,Var/Ed,wbar


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--delta',type=float,required=True); ap.add_argument('--area',type=float,default=500.); a=ap.parse_args()
    d=round(a.delta,5); area=float(a.area)
    if d not in (.21200,.21250,.21300): raise SystemExit('supported: .212,.2125,.213')
    r=ROOTS.get(d)
    if r is None:
        r,_,_,_=sw.solve_root(d)
    C=C0*r*r; R=R0/r
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT; original=fd.CASES[.6]
    try:
        fd.BETA_COLD=.80; fd.DELTA_TILT=d; fd.CASES[.6]=(L0,C,original[2]); nf.CASES[.6]=fd.CASES[.6]
        model=fd.DynamicForce(.6,quick=False,Tmax=1.02)
        xcold=model.cold_states()[0]
        kcold=float(np.asarray(model.spline.ev(fd.T0,xcold,dx=0,dy=1)).reshape(-1)[0])
        wc=math.sqrt(kcold/(L0*C)); wd=ALPHA*wc
        # 4 ns is well beyond the current 2-ns basin-classification horizon; a
        # 6-ns rerun tests residual stored/filter energy and Fourier truncation.
        results=[]
        for tend in (4.0,6.0):
            out=deterministic_trace(model,area,R,C,wc,wd,tend)
            t=np.asarray(out['t']); v=np.asarray(out['v']); w=np.asarray(out['w'])
            Ed,Var,epsEff,wbar=spectral_metric(t,v,R,wd)
            ER=float(np.trapezoid((PHI_BAR*w)**2/R,t))
            results.append((tend,Ed,ER,Var,epsEff,wbar,out))
            print(f'delta={d:.5f} A={area:g} tend={tend:g}ns Tad={out["Tad"]:.6f}K: '
                  f'Ed_spec/kB={Ed/KB:.9e}K ER_time/kB={ER/KB:.9e}K '
                  f'relEnergyMismatch={(Ed-ER)/ER:+.4e} VarW/kB2={Var/(KB*KB):.9e}K2 '
                  f'epsEff/kB={epsEff/KB:.9e}K epsEff/(2kBT)={epsEff/(2*KB*fd.T0):.6f} '
                  f'fbar={wbar/(2*math.pi)*1e-9:.6f}GHz sigmaW/kB={math.sqrt(Var)/KB:.6e}K '
                  f'Ed/sigmaW={Ed/math.sqrt(Var):.6f} finalFilterEnergy/kB={out["final_filter_K"]:.3e}K')
        a4,a6=results
        tail=abs(a6[1]-a4[1])/a6[1]
        mismatch=abs(a6[1]-a6[2])/a6[2]
        msg=(f'delta={d:.5f} A={area:g}: epsEff/kB={a6[4]/KB:.7f}K '
             f'epsEff_classical_floor_ratio={a6[4]/(2*KB*fd.T0):.5f} '
             f'diss_weighted_f={a6[5]/(2*math.pi)*1e-9:.5f}GHz '
             f'Ediss/kB={a6[1]/KB:.7f}K sigmaW/kB={math.sqrt(a6[3])/KB:.7f}K '
             f'4to6ns_Etail={tail:.3e} spectral_vs_resistor={mismatch:.3e} '
             f'finalFilterEnergy/kB={a6[6]["final_filter_K"]:.3e}K')
        print(msg); print(f'::notice title=Experiment 03 passive work-noise metric::{msg}')
        if tail>.02: raise RuntimeError('dissipated-energy integral has >2% 4->6 ns tail')
        if mismatch>.04: raise RuntimeError('spectral and resistor dissipated energies disagree by >4%')
        if a6[4] < 2*KB*fd.T0*(1-2e-4): raise RuntimeError('FDT work bound violated numerically')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot; fd.CASES[.6]=original; nf.CASES[.6]=original

if __name__=='__main__': main()
