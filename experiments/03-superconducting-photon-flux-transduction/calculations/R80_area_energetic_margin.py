#!/usr/bin/env python3
"""Exact deterministic separatrix-energy margin across the R80 14-um area scan.

For the passive two-pole environment, after the competing well/saddle reforms,
define the extended-system energy relative to the instantaneous separating saddle

    e_s = 1/2 L C v^2 + [U(x,T)-U(x_s,T)]
          + 1/2 (Lf/L) d^2 + 1/2 L Cf w^2.

Negative e_s on the favored side is an energetic trapping certificate at that
instant.  This script computes e_s at first numerically resolved reformation and
the later energetic-lock time as absorber area is varied through the sharp
14-um stochastic capture transition.

The calculation is deterministic and uses the exact passive-network energy.  It
is not a stochastic/quantum efficiency model.
"""
from __future__ import annotations

import math
import numpy as np
from scipy.integrate import quad, solve_ivp

from causal_two_pole_environment import filter_components
from causal_energetic_lock import separating_saddle
from directional_recovery_barriers import kelvin_scale
from finite_time_basin_slice import cold_phase_scale
from full_dynamic_rfsquid import CASES, DynamicForce, T0, TAU0_CONDITIONAL, adiabatic_photon_temperature


def dU_from_saddle(model,T,xs,x):
    return float(quad(lambda xx:model.force(T,xx),xs,x,epsabs=1e-10,epsrel=2e-8,limit=120)[0])


def run_area(model,A,R=80.,alpha=.90,lam=14.,rise_ps=20.,tend_ns=.5):
    L,C,_=CASES[.6]; xc,_,wc=cold_phase_scale(model,.6); Tf=model.fold_temperature()
    wd=alpha*wc; Lf,Cf=filter_components(R,wd)
    Tad=adiabatic_photon_temperature(lam,A)
    u0=T0*T0; du=Tad*Tad-u0; cool=1/(2*TAU0_CONDITIONAL*u0); tr=rise_ps*1e-12
    def src(t): return du/tr*math.exp(-t/tr)
    def rhs(t,y):
        x,v,u,d,w=y; u=max(float(u),u0); T=math.sqrt(u)
        return np.array([v,-(d+model.force(T,x))/(L*C),src(t)-cool*(u*u-u0*u0),
                         (L/Lf)*(v-w),d/(L*Cf)-w/(R*Cf)])
    tf=tend_ns*1e-9
    sol=solve_ivp(rhs,(0,tf),np.array([xc,0,u0,0,0],float),method='DOP853',rtol=2e-9,
                  atol=np.array([1e-11,1e2,1e-14,1e-11,1e2]),max_step=.03e-12,dense_output=True)

    # Resolve cooling-side reformation, then move infinitesimally below Tf until
    # a numerical saddle is present.  This avoids assigning a separatrix to the
    # exact saddle-node degeneracy itself.
    ts=np.linspace(0,tf,30001); ys=sol.sol(ts); temps=np.sqrt(np.maximum(ys[2],u0))
    ip=int(np.argmax(temps)); cand=np.where(temps[ip:]<Tf)[0]
    if not len(cand): raise RuntimeError('no reformation')
    i0=ip+int(cand[0])
    ireform=None
    for i in range(i0,min(i0+1000,len(ts))):
        if separating_saddle(model,float(temps[i])) is not None:
            ireform=i; break
    if ireform is None: raise RuntimeError('no resolved post-fold saddle')

    EK=kelvin_scale(.6)
    erel=np.full(len(ts),np.nan)
    side=np.zeros(len(ts),dtype=bool)
    for i in range(ireform,len(ts)):
        T=float(temps[i]); xs=separating_saddle(model,T)
        if xs is None: continue
        x,v,_,d,w=[float(q) for q in ys[:,i]]
        erel[i]=(0.5*L*C*v*v+dU_from_saddle(model,T,xs,x)
                 +0.5*(Lf/L)*d*d+0.5*L*Cf*w*w)
        side[i]=x>xs

    # First time after reformation that trajectory is on target side, below
    # separatrix energy, and remains negative for the remainder of this trace.
    ilock=None
    for i in range(ireform,len(ts)):
        if side[i] and np.isfinite(erel[i]) and erel[i]<0:
            tail=erel[i:]
            if np.nanmax(tail)<=1e-8:
                ilock=i; break

    xR=float(ys[0,ireform]); uR=float(ys[1,ireform]/wc)
    return {
        'Tad':Tad,'Tf':Tf,'tR':float(ts[ireform]),'xR':xR,'uR':uR,
        'eR_K':float(erel[ireform]*EK),'targetSideR':bool(side[ireform]),
        'tlock':float(ts[ilock]) if ilock is not None else math.nan,
        'lockDelay':float(ts[ilock]-ts[ireform]) if ilock is not None else math.nan,
        'eMin_K':float(np.nanmin(erel[ireform:])*EK),
        'eMax_K':float(np.nanmax(erel[ireform:])*EK),
        'eFinal_K':float(erel[np.where(np.isfinite(erel))[0][-1]]*EK),
    }


def main():
    model=DynamicForce(.6,quick=False,Tmax=.95)
    print('Experiment 03 R80 exact reformation energetic margin')
    for A in (57.142857,72.,80.,82.,84.,85.,86.,87.,88.,90.,100.):
        o=run_area(model,A)
        msg=(f'A={A:g}um2 Tadiab={o["Tad"]:.5f}K: tR={o["tR"]*1e12:.3f}ps '
             f'xR={o["xR"]:+.5f} uR={o["uR"]:+.5f} sideR={o["targetSideR"]} '
             f'Esep_R/kB={o["eR_K"]:+.6f}K; '
             f'tlock={o["tlock"]*1e12 if math.isfinite(o["tlock"]) else math.nan:.3f}ps '
             f'lockDelay={o["lockDelay"]*1e12 if math.isfinite(o["lockDelay"]) else math.nan:.3f}ps '
             f'Emax_after/kB={o["eMax_K"]:+.6f}K Efinal/kB={o["eFinal_K"]:+.6f}K')
        print(msg); print(f'::notice title=Experiment 03 R80 energetic margin::{msg}')
    print('PASS')
if __name__=='__main__': main()
