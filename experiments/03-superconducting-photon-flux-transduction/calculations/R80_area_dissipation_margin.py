#!/usr/bin/env python3
"""Deterministic stage-selective dissipation across the R80 14-um area threshold.

This complements the stochastic sym-FDT/TWA area scan.  At fixed
R=80 ohm, alpha=.90, lambda=14 um, rise=20 ps, vary absorber area and compute

- first favored-side x=0 crossing;
- cooling-side fold reformation;
- resistor loss before crossing and crossing->reformation;
- stage filter attenuation H_eff^2 = int w^2 dt / int v^2 dt;
- the ratio A_sel=H_eff,L^2/H_eff,C^2.

The purpose is to test whether the sharp stochastic capture loss at increasing
heat capacity is accompanied by loss of stage-selective damping, or whether it
is primarily a thermal-drive/basin-margin effect.
"""
from __future__ import annotations
import math
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

from causal_two_pole_environment import filter_components
from finite_time_basin_slice import cold_phase_scale
from full_dynamic_rfsquid import CASES, DynamicForce, T0, TAU0_CONDITIONAL, adiabatic_photon_temperature
from quantum_initial_capture import PHI_BAR


def trajectory(model,A,tend_ns=.35):
    R=80.; alpha=.90; lam=14.; rise_ps=20.
    L,C,_=CASES[.6]; xc,_,wc=cold_phase_scale(model,.6)
    wd=alpha*wc; Lf,Cf=filter_components(R,wd)
    Tad=adiabatic_photon_temperature(lam,A)
    u0=T0*T0; du=Tad*Tad-u0; cool=1/(2*TAU0_CONDITIONAL*u0); tr=rise_ps*1e-12
    def src(t): return du/tr*math.exp(-t/tr)
    def rhs(t,y):
        x,v,u,d,w=y; u=max(float(u),u0); T=math.sqrt(u)
        F=model.force(T,x)
        return np.array([v,-(d+F)/(L*C),src(t)-cool*(u*u-u0*u0),
                         (L/Lf)*(v-w),d/(L*Cf)-w/(R*Cf)])
    sol=solve_ivp(rhs,(0,tend_ns*1e-9),np.array([xc,0,u0,0,0],float),
                  method='DOP853',rtol=2e-9,
                  atol=np.array([1e-11,1e2,1e-14,1e-11,1e2]),
                  max_step=.03e-12,dense_output=True)
    return sol,wc,Tad


def first_cross(sol,tend):
    ts=np.linspace(0,tend,12001); x=sol.sol(ts)[0]
    ids=np.where(x[:-1]*x[1:]<0)[0]
    if not len(ids): return math.nan
    i=int(ids[0]); return brentq(lambda t: float(sol.sol(t)[0]),ts[i],ts[i+1])


def reformation(sol,model,tend):
    Tf=model.fold_temperature()
    ts=np.linspace(0,tend,20001); T=np.sqrt(np.maximum(sol.sol(ts)[2],T0*T0))
    ip=int(np.argmax(T))
    ids=np.where(T[ip:]<Tf)[0]
    return float(ts[ip+int(ids[0])]) if len(ids) else math.nan


def integ(sol,ta,tb):
    if not (math.isfinite(ta) and math.isfinite(tb) and tb>ta): return (math.nan,)*4
    t=np.linspace(ta,tb,6001); y=sol.sol(t); v=y[1]; w=y[4]
    iv=float(np.trapezoid(v*v,t)); iw=float(np.trapezoid(w*w,t))
    return iv,iw,iw/iv if iv>0 else math.nan,float(tb-ta)


def qloss(sol,R,ta,tb):
    if not (math.isfinite(ta) and math.isfinite(tb) and tb>ta): return math.nan
    t=np.linspace(ta,tb,6001); w=sol.sol(t)[4]
    return PHI_BAR**2/R*float(np.trapezoid(w*w,t))


def main():
    model=DynamicForce(.6,quick=False,Tmax=.95); R=80.; tf=.35e-9
    print('Experiment 03 R80 area stage-selective dissipation margin')
    for A in (57.142857,72.,80.,82.,84.,86.,88.,90.,100.):
        sol,wc,Tad=trajectory(model,A,tend_ns=.35)
        tc=first_cross(sol,tf); trf=reformation(sol,model,tf)
        _,_,hL,dtL=integ(sol,0,tc); _,_,hC,dtC=integ(sol,tc,trf)
        qL=qloss(sol,R,0,tc); qC=qloss(sol,R,tc,trf)
        sel=hL/hC if hC>0 else math.nan
        fracL=qL/(qL+qC) if (qL+qC)>0 else math.nan
        xrf=float(sol.sol(trf)[0]) if math.isfinite(trf) else math.nan
        urf=float(sol.sol(trf)[1]/wc) if math.isfinite(trf) else math.nan
        msg=(f'A={A:g}um2 lambdaA={14*A:.1f} Tadiab={Tad:.4f}K: '
             f'tcross={tc*1e12:.2f}ps treform={trf*1e12:.2f}ps '
             f'x_reform={xrf:+.4f} u_reform={urf:+.4f}; '
             f'HeffL2={hL:.5f} HeffC2={hC:.5f} Aselect={sel:.5f}; '
             f'Qpre/(Qpre+Qcap)={fracL:.5f} '
             f'dtL/dtC={dtL/dtC if dtC>0 else math.nan:.4f}')
        print(msg); print(f'::notice title=Experiment 03 R80 area dissipation::{msg}')
    print('PASS')

if __name__=='__main__': main()
