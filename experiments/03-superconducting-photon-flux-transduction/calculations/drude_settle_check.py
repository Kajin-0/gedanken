#!/usr/bin/env python3
"""Longer-time Drude-bath persistence diagnostic for Experiment 03.

Nearest-well classification at a single observation time can mislabel a highly
oscillatory trajectory.  This script follows selected causal-Drude points to
multiple late times and reports a cold-separatrix energy margin including the
series-inductor energy of the Drude branch.

For Y=1/(R0-i omega Lb), Lb=R0/omegaD. In the normalized phase-energy units
used by LC*xddot + L*j + F=0, the late-time total energy relative to the cold
central saddle is

  Erel = 0.5*L*C*v^2 + integral(xs->x) F(x,T0) dx + 0.5*L*Lb*j^2.

If x is on the right side and Erel<0 after the thermal pulse has substantially
recovered, the state is energetically trapped below the cold separatrix in this
deterministic extended-system model.  This is still not a stochastic claim.
"""
from __future__ import annotations
import math
import numpy as np
from scipy.integrate import quad, solve_ivp

from full_dynamic_rfsquid import CASES, DynamicForce, T0, TAU0_CONDITIONAL, adiabatic_photon_temperature
from finite_time_basin_slice import cold_phase_scale


def run(model,R0,d,tends_ns):
    r=0.6; rise_ps=20.0; L,C,_=CASES[r]
    left,right=model.cold_states()
    roots=model.roots(T0)
    saddles=[x for x,k in roots if k<0 and left<x<right]
    xs=saddles[0]
    _,_,omega0=cold_phase_scale(model,r)
    omegaD=d*omega0; tauD=1/omegaD; Lb=R0/omegaD; G0=1/R0
    Tad=adiabatic_photon_temperature(14.0,100.0)
    u0=T0*T0; du=Tad*Tad-u0; tau_r=rise_ps*1e-12
    cool=1/(2*TAU0_CONDITIONAL*u0)
    def rhs(t,y):
        x,v,j,u=y; u=max(float(u),u0); T=math.sqrt(u)
        src=du/tau_r*math.exp(-t/tau_r)
        return np.array([v,-(L*j+model.force(T,x))/(L*C),(G0*v-j)/tauD,
                         src-cool*(u*u-u0*u0)])
    tmax=max(tends_ns)*1e-9
    sol=solve_ivp(rhs,(0,tmax),np.array([left,0.0,0.0,u0]),method='DOP853',
                  rtol=5e-8,atol=np.array([2e-10,1e2,1e-7,1e-12]),max_step=2e-12,
                  dense_output=True)
    for tn in tends_ns:
        x,v,j,u=[float(z) for z in sol.sol(tn*1e-9)]
        T=math.sqrt(max(u,u0))
        Urel=quad(lambda xx:model.force(T0,xx),xs,x,epsabs=1e-10)[0]
        Ekin=0.5*L*C*v*v
        Eb=0.5*L*Lb*j*j
        Erel=Ekin+Urel+Eb
        side='right' if x>xs else 'left'
        trapped=(side=='right' and Erel<0)
        msg=(f"R0={R0:g}ohm d={d:g} t={tn:g}ns: T={T:.5f}K x={x:.6f} "
             f"v={v:.3e} j={j:.3e} Erel_cold={Erel:+.6e} "
             f"side={side} trapped_below_cold_sep={trapped}")
        print(msg)
        print(f"::notice title=Experiment 03 Drude settle::{msg}")


def main():
    m=DynamicForce(0.6,quick=False)
    for R0,d in ((160,5),(160,10),(250,5),(250,10),(400,5),(400,10)):
        run(m,float(R0),float(d),(0.8,2.0,5.0,10.0))
    print('PASS')

if __name__=='__main__': main()
