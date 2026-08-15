#!/usr/bin/env python3
"""Causal-environment separatrix-energy and energetic-lock diagnostic.

After the metastable left well/saddle reform, position on the favored side is
not by itself a sufficient deterministic trapping criterion if phase kinetic
energy or reactive filter energy can drive a return crossing.

For the passive two-pole environment define the dimensionless total energy
(relative to E_L=Phi_bar^2/L)

  e = 1/2 L C v^2 + U(x,T)
      + 1/2 (L_f/L) d^2 + 1/2 L C_f w^2.

While the separating saddle x_s(T) exists, define

  e_s = e - U[x_s(T),T].

Because F=U_x and F(x_s,T)=0,

  d e_s/dt = [U_T(x,T)-U_T(x_s,T)] Tdot - (L/R) w^2.

This script follows e_s along the deterministic causal-filter trajectory and
reports the final downward zero crossing after which e_s stays negative over
the simulated recovery interval.  That is called the *energetic lock time* in
this checkpoint.  It is a deterministic sufficient-energy diagnostic, not a
stochastic or quantum capture theorem.
"""

from __future__ import annotations

import math

import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq

from causal_two_pole_environment import filter_components
from finite_time_basin_slice import cold_phase_scale
from full_dynamic_rfsquid import (
    CASES,
    DynamicForce,
    T0,
    TAU0_CONDITIONAL,
    adiabatic_photon_temperature,
)
from quantum_initial_capture import KB
from directional_recovery_barriers import kelvin_scale


def phase_potential_difference(model: DynamicForce, T: float, xa: float, xb: float) -> float:
    """U(xb,T)-U(xa,T) in dimensionless E_L units."""
    return float(quad(lambda xx: model.force(T, xx), xa, xb,
                      epsabs=2e-10, epsrel=2e-8, limit=100)[0])


def separating_saddle(model: DynamicForce, T: float) -> float | None:
    roots=model.roots(T)
    stables=sorted([x for x,k in roots if k>0])
    saddles=sorted([x for x,k in roots if k<0])
    if len(stables)<2 or not saddles:
        return None
    left,right=stables[-2],stables[-1]
    between=[s for s in saddles if left<s<right]
    return between[-1] if between else None


def trace_lock(model: DynamicForce,R: float,alpha: float,*,r_delta: float=0.6,
               rise_ps: float=20.0,lambda_um: float=14.0,tend_ns: float=5.0):
    L,C,_=CASES[r_delta]
    x_c,_,omega_c=cold_phase_scale(model,r_delta)
    omega_d=alpha*omega_c
    Lf,Cf=filter_components(R,omega_d)
    Tf=model.fold_temperature()

    Tad=adiabatic_photon_temperature(lambda_um,100.0)
    u0=T0*T0
    du_total=Tad*Tad-u0
    cool_coeff=1.0/(2.0*TAU0_CONDITIONAL*u0)
    tau_r=rise_ps*1e-12
    def source(t): return du_total/tau_r*math.exp(-t/tau_r)
    def rhs(t,y):
        x,v,u,d,w=y
        u=max(float(u),u0); T=math.sqrt(u)
        F=model.force(T,x)
        return np.array([
            v,
            -(d+F)/(L*C),
            source(t)-cool_coeff*(u*u-u0*u0),
            (L/Lf)*(v-w),
            d/(L*Cf)-w/(R*Cf),
        ])

    sol=solve_ivp(rhs,(0.0,tend_ns*1e-9),np.array([x_c,0.0,u0,0.0,0.0]),
                  method='DOP853',rtol=3e-8,
                  atol=np.array([1e-10,2e2,1e-13,1e-10,2e2]),
                  max_step=0.15e-12,dense_output=True)

    # Resolve the important first 500 ps densely; a coarser tail is enough to
    # verify that no later positive excursion reappears.
    t1=np.linspace(0,min(0.5e-9,tend_ns*1e-9),2501)
    if tend_ns>0.5:
        t2=np.linspace(0.5e-9,tend_ns*1e-9,1501)[1:]
        ts=np.concatenate([t1,t2])
    else:
        ts=t1
    ys=sol.sol(ts)
    temps=np.sqrt(np.maximum(ys[2],u0))

    erel=np.full_like(ts,np.nan,dtype=float)
    saddles=np.full_like(ts,np.nan,dtype=float)
    for i,(t,T) in enumerate(zip(ts,temps)):
        xs=separating_saddle(model,float(T))
        if xs is None:
            continue
        x,v,_,d,w=[float(q) for q in ys[:,i]]
        dU=phase_potential_difference(model,float(T),xs,x)
        erel[i]=(0.5*L*C*v*v+dU
                 +0.5*(Lf/L)*d*d+0.5*L*Cf*w*w)
        saddles[i]=xs

    valid=np.where(np.isfinite(erel))[0]
    if not len(valid): raise RuntimeError('saddle never reforms')
    ireform=int(valid[0])

    # Find the final positive->negative sign transition, and verify all later
    # sampled values stay <=0. If already negative at reformation, lock=reform.
    if erel[ireform] <= 0 and np.nanmax(erel[ireform:]) <= 0:
        ilock=ireform
    else:
        ilock=None
        for i in range(ireform+1,len(ts)):
            if np.isfinite(erel[i-1]) and np.isfinite(erel[i]) and erel[i-1]>0>=erel[i]:
                if np.nanmax(erel[i:]) <= 1e-8:
                    ilock=i
                    break
    tlock=float(ts[ilock]) if ilock is not None else math.nan

    EK=kelvin_scale(r_delta)
    out={
        't_reform':float(ts[ireform]),
        'x_reform':float(ys[0,ireform]),
        'u_reform':float(ys[1,ireform]/omega_c),
        'e_reform_K':float(erel[ireform]*EK),
        't_lock':tlock,
        'x_lock':float(sol.sol(tlock)[0]) if math.isfinite(tlock) else math.nan,
        'e_min_after_K':float(np.nanmin(erel[ireform:])*EK),
        'e_max_after_K':float(np.nanmax(erel[ireform:])*EK),
        'e_final_K':float(erel[valid[-1]]*EK),
        'omega_c':omega_c,
    }
    return out


def main():
    print('Experiment 03 causal separatrix energetic lock')
    model=DynamicForce(0.6,quick=False)
    for R,alpha in [(250.0,0.20),(250.0,0.35),(250.0,0.50)]:
        o=trace_lock(model,R,alpha)
        msg=(
            f'R={R:g} alpha={alpha:.2f}: '
            f't_reform={o["t_reform"]*1e12:.3f} ps, '
            f'x_reform={o["x_reform"]:+.5f}, u_reform={o["u_reform"]:+.5f}, '
            f'Esep_reform/kB={o["e_reform_K"]:.5f} K, '
            f't_lock={o["t_lock"]*1e12:.3f} ps, x_lock={o["x_lock"]:+.5f}, '
            f'Esep_max_after/kB={o["e_max_after_K"]:.5f} K, '
            f'Esep_final/kB={o["e_final_K"]:.5f} K'
        )
        print(msg)
        print(f'::notice title=Experiment 03 energetic lock::{msg}')
    print('PASS')

if __name__=='__main__':
    main()
