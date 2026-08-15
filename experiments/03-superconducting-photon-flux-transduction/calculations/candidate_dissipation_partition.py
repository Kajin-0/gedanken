#!/usr/bin/env python3
"""Partition causal-environment dissipation across write stages.

The passive two-pole environment has exact resistor loss

    Q_R = int V_C^2/R dt
        = E_L (L/R) int w^2 dt,

where w=V_C/Phi_bar.  This script asks whether the low-R high-fidelity branch
resolves the launch/capture damping conflict by dissipating comparatively little
before the first favored-side crossing and more after the useful trajectory has
crossed.

For selected R,alpha points on the strongest 8-um-equivalent energy-density
lobe, compute deterministic times and partition Q_R into

    0 -> first x=0 crossing
    crossing -> cooling-side reformation
    reformation -> energetic lock
    lock -> 0.5 ns.

The result is deterministic energy accounting, not a stochastic efficiency or
a novelty claim.
"""
from __future__ import annotations
import math
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

from causal_two_pole_environment import filter_components
from causal_energetic_lock import trace_lock
from finite_time_basin_slice import cold_phase_scale
from full_dynamic_rfsquid import CASES, DynamicForce, T0, TAU0_CONDITIONAL, adiabatic_photon_temperature
from quantum_initial_capture import KB, PHI_BAR


def trajectory(model,R,alpha,*,lambda_um=8.0,rise_ps=20.0,tend_ns=.5):
    L,C,_=CASES[.6]
    x_c,_,wc=cold_phase_scale(model,.6)
    wd=alpha*wc; Lf,Cf=filter_components(R,wd)
    Tad=adiabatic_photon_temperature(lambda_um,100.0)
    u0=T0*T0; du=Tad*Tad-u0
    cool=1/(2*TAU0_CONDITIONAL*u0); tr=rise_ps*1e-12
    def src(t): return du/tr*math.exp(-t/tr)
    def rhs(t,y):
        x,v,u,d,w=y; u=max(float(u),u0); T=math.sqrt(u)
        F=model.force(T,x)
        return np.array([v,-(d+F)/(L*C),src(t)-cool*(u*u-u0*u0),
                         (L/Lf)*(v-w),d/(L*Cf)-w/(R*Cf)])
    sol=solve_ivp(rhs,(0,tend_ns*1e-9),np.array([x_c,0,u0,0,0],float),
                  method='DOP853',rtol=2e-9,
                  atol=np.array([1e-11,1e2,1e-14,1e-11,1e2]),
                  max_step=.03e-12,dense_output=True)
    return sol,wc


def first_cross(sol,tend):
    ts=np.linspace(0,tend,12001); x=sol.sol(ts)[0]
    ids=np.where(x[:-1]*x[1:]<0)[0]
    if not len(ids): return math.nan
    i=int(ids[0]); return brentq(lambda t: float(sol.sol(t)[0]),ts[i],ts[i+1])


def integrate_q(sol,R,ta,tb,n=5001):
    if not (math.isfinite(ta) and math.isfinite(tb)) or tb<=ta: return math.nan
    t=np.linspace(ta,tb,n); w=sol.sol(t)[4]
    return PHI_BAR**2/R*float(np.trapezoid(w*w,t))


def main():
    print('Experiment 03 deterministic dissipation partition')
    print('rDelta=.6, delta=.05, C=215 fF, 8-um/A100-equivalent energy density')
    model=DynamicForce(.6,quick=False,Tmax=.95)
    for R,alpha in [
        (150.,.70),(150.,.80),(100.,.80),(80.,.70),(80.,.90),(80.,1.00),
        (40.,.90),(30.,1.00),(20.,.90),(20.,1.00),
    ]:
        sol,wc=trajectory(model,R,alpha)
        tc=first_cross(sol,.5e-9)
        lock=trace_lock(model,R,alpha,lambda_um=8.0,rise_ps=20.0,tend_ns=.5)
        trf=lock['t_reform']; tl=lock['t_lock']; tf=.5e-9
        qs=[integrate_q(sol,R,a,b) for a,b in [(0,tc),(tc,trf),(trf,tl),(tl,tf)]]
        qt=sum(q for q in qs if math.isfinite(q))
        mev=1.602176634e-22  # joule per meV
        labels=[q/mev for q in qs]
        frac=[q/qt if qt>0 else math.nan for q in qs]
        msg=(
            f'R={R:g} alpha={alpha:.2f}: tcross={tc*1e12:.3f} ps, '
            f'treform={trf*1e12:.3f} ps, tlock={tl*1e12:.3f} ps; '
            f'Q_meV=[preCross {labels[0]:.5f}, crossToReform {labels[1]:.5f}, '
            f'reformToLock {labels[2]:.5f}, postLock {labels[3]:.5f}], '
            f'fractions=[{frac[0]:.4f},{frac[1]:.4f},{frac[2]:.4f},{frac[3]:.4f}], '
            f'Qtotal={qt/mev:.5f} meV'
        )
        print(msg)
        print(f'::notice title=Experiment 03 dissipation partition::{msg}')
    print('PASS')

if __name__=='__main__':
    main()
