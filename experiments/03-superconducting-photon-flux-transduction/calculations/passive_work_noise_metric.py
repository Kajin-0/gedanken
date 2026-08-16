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

import full_dynamic_rfsquid as fd
import nonlinear_fdt_twa_screen as nf
import R80_area_energetic_margin as em
from quantum_initial_capture import HBAR, KB, PHI_BAR
import safe_tilt_optimum_worker as sw

C0=215e-15; R0=80.; L0=111.5e-12; ALPHA=.90
ROOTS={
    .21250:10.885578211,
    .21300:11.2051409652,
}


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
    # Two-sided discrete integral. rfft stores positive frequencies once.
    weight=np.ones_like(omega)
    if n%2==0:
        if len(weight)>2: weight[1:-1]=2
    else:
        if len(weight)>1: weight[1:]=2
    domega=2*math.pi/(n*dt)
    measure=weight*domega/(2*math.pi)*reY*np.abs(Vf)**2
    Ed=float(np.sum(measure))
    Var=float(np.sum(eps*measure))
    # Dissipation-weighted mean absolute frequency is useful in the T->0 limit.
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
        wc=math.sqrt(float(model.spline.ev(fd.T0,model.cold_states()[0],dx=0,dy=1).reshape(-1)[0])/(L0*C))
        wd=ALPHA*wc
        # 4 ns lets the filter/ringdown energy decay well beyond the 2-ns basin
        # classification horizon. A second 6-ns run checks residual tail bias.
        results=[]
        for tend in (4.0,6.0):
            out=em.run_area(model,area,R=R,alpha=ALPHA,lambda_um=14.,rise_ps=20.,tend_ns=tend)
            t=np.asarray(out['t']); v=np.asarray(out['v']); w=np.asarray(out['w'])
            Ed,Var,epsEff,wbar=spectral_metric(t,v,R,wd)
            ER=float(np.trapezoid((PHI_BAR*w)**2/R,t))
            results.append((tend,Ed,ER,Var,epsEff,wbar,out))
            print(f'delta={d:.5f} A={area:g} tend={tend:g}ns: '
                  f'Ed_spec/kB={Ed/KB:.9e}K ER_time/kB={ER/KB:.9e}K '
                  f'relEnergyMismatch={(Ed-ER)/ER:+.4e} VarW/kB2={Var/(KB*KB):.9e}K2 '
                  f'epsEff/kB={epsEff/KB:.9e}K epsEff/(2kBT)={epsEff/(2*KB*fd.T0):.6f} '
                  f'fbar={wbar/(2*math.pi)*1e-9:.6f}GHz sigmaW/kB={math.sqrt(Var)/KB:.6e}K '
                  f'Ed/sigmaW={Ed/math.sqrt(Var):.6f}')
        a4,a6=results
        tail=abs(a6[1]-a4[1])/a6[1]
        mismatch=abs(a6[1]-a6[2])/a6[2]
        msg=(f'delta={d:.5f} A={area:g}: epsEff/kB={a6[4]/KB:.7f}K '
             f'epsEff_classical_floor_ratio={a6[4]/(2*KB*fd.T0):.5f} '
             f'diss_weighted_f={a6[5]/(2*math.pi)*1e-9:.5f}GHz '
             f'Ediss/kB={a6[1]/KB:.7f}K sigmaW/kB={math.sqrt(a6[3])/KB:.7f}K '
             f'4to6ns_Etail={tail:.3e} spectral_vs_resistor={mismatch:.3e}')
        print(msg); print(f'::notice title=Experiment 03 passive work-noise metric::{msg}')
        if tail>.02: raise RuntimeError('dissipated-energy integral has >2% 4->6 ns tail')
        if mismatch>.04: raise RuntimeError('spectral and resistor dissipated energies disagree by >4%')
        if a6[4] < 2*KB*fd.T0*(1-2e-4): raise RuntimeError('FDT work bound violated numerically')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot; fd.CASES[.6]=original; nf.CASES[.6]=original

if __name__=='__main__': main()
