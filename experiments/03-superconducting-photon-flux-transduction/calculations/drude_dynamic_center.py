#!/usr/bin/env python3
"""Deterministic full-nonlinear pulse dynamics with a causal Drude bath.

The scalar shunt term (1/R) xdot is replaced by an auxiliary bath current j:

    L C xddot + L j + F(x,T) = 0
    tau_D jdot + j = G0 xdot

where Y(omega)=G0/(1-i omega tau_D).  This is the smallest causal colored
admittance that regularizes the ultraviolet quantum bath while remaining close
to scalar-R dynamics when omega_D >> omega_phase.

This script only follows the deterministic cold-well center.  It is a
regression/architecture screen, not a capture probability calculation.
"""
from __future__ import annotations
import math
import numpy as np
from scipy.integrate import solve_ivp

from full_dynamic_rfsquid import (
    CASES, DynamicForce, T0, TAU0_CONDITIONAL,
    adiabatic_photon_temperature,
)
from finite_time_basin_slice import cold_phase_scale


def simulate(model: DynamicForce,r_delta: float,R0: float,d: float,
             rise_ps: float=20.0,lambda_um: float=14.0,tend_ns: float=0.8):
    L,C,_=CASES[r_delta]
    left,right=model.cold_states()
    _,_,omega0=cold_phase_scale(model,r_delta)
    omegaD=d*omega0
    tauD=1.0/omegaD
    G0=1.0/R0
    Tad=adiabatic_photon_temperature(lambda_um,100.0)
    u0=T0*T0
    du=Tad*Tad-u0
    tau_r=rise_ps*1e-12
    cool_coeff=1.0/(2.0*TAU0_CONDITIONAL*u0)

    def source(t): return du/tau_r*math.exp(-t/tau_r)
    def rhs(t,y):
        x,v,j,u=y
        u=max(float(u),u0)
        T=math.sqrt(u)
        F=model.force(T,x)
        du_dt=source(t)-cool_coeff*(u*u-u0*u0)
        dv=-(L*j+F)/(L*C)
        dj=(G0*v-j)/tauD
        return np.array([v,dv,dj,du_dt])

    sol=solve_ivp(rhs,(0,tend_ns*1e-9),np.array([left,0.0,0.0,u0]),
                  rtol=2e-8,atol=(1e-10,1e-2,1e-8,1e-10),max_step=0.25e-12)
    x=float(sol.y[0,-1]); v=float(sol.y[1,-1]); j=float(sol.y[2,-1])
    basin='right' if abs(x-right)<abs(x-left) else 'left'
    return basin,x,v,j,tauD,omega0


def main():
    model=DynamicForce(0.6,quick=False)
    for R0 in (160.0,200.0,250.0,300.0,400.0):
        for d in (2.0,5.0,10.0,20.0):
            basin,x,v,j,tauD,w0=simulate(model,0.6,R0,d)
            re_ratio=1.0/(1.0+(1.0/d)**2)
            msg=(f"rDelta=0.6 rise=20ps R0={R0:g}ohm d={d:g}: basin={basin}, "
                 f"x_final={x:.6f}, v_final={v:.3e}, j_final={j:.3e}, "
                 f"ReY(w0)/G0={re_ratio:.5f}, tauD_ps={tauD*1e12:.3f}")
            print(msg)
            print(f"::notice title=Experiment 03 Drude center dynamics::{msg}")
    print('PASS')

if __name__=='__main__': main()
