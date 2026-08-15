#!/usr/bin/env python3
"""Directional barrier and recovery-lock diagnostic for Experiment 03.

The cold barrier quoted throughout the early analysis is the metastable
left-to-saddle barrier.  After a photon-triggered transition into the favored
right well, the relevant return error is instead controlled by the
right-to-saddle barrier.  This script computes both directional barriers versus
temperature and follows their reappearance during the finite photon pulse.

It also reports the first/last x=0 crossing of deterministic causal-filter
trajectories and the right-return barrier at the instant the left well/saddle
reform during cooling.
"""

from __future__ import annotations

import math

import numpy as np
from scipy.integrate import quad, solve_ivp

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


def directional_barriers(model: DynamicForce, T: float) -> dict[str, float]:
    roots = model.roots(T)
    stables = sorted([x for x, k in roots if k > 0.0])
    saddles = sorted([x for x, k in roots if k < 0.0])
    if len(stables) < 2 or not saddles:
        raise ValueError("double-well not present")
    left = stables[-2] if len(stables) > 2 else stables[0]
    right = stables[-1]
    between = [s for s in saddles if left < s < right]
    if not between:
        raise ValueError("no saddle between target wells")
    saddle = between[-1]

    b_left_dimless = quad(lambda x: model.force(T, x), left, saddle,
                          epsabs=1e-11, epsrel=1e-9)[0]
    b_right_dimless = -quad(lambda x: model.force(T, x), saddle, right,
                           epsabs=1e-11, epsrel=1e-9)[0]
    return {
        "left": left,
        "saddle": saddle,
        "right": right,
        "b_left": float(b_left_dimless),
        "b_right": float(b_right_dimless),
    }


def kelvin_scale(r_delta: float) -> float:
    """E_L/kB for the current physical loop inductance."""
    H = 6.62607015e-34
    E = 1.602176634e-19
    PHI0 = H / (2.0 * E)
    PHIB = PHI0 / (2.0 * math.pi)
    L, _, _ = CASES[r_delta]
    return PHIB * PHIB / (L * KB)


def pulse_trace(
    model: DynamicForce,
    R: float,
    alpha: float,
    *,
    r_delta: float = 0.6,
    rise_ps: float = 20.0,
    lambda_um: float = 14.0,
    tend_ns: float = 5.0,
) -> dict[str, object]:
    L, C, _ = CASES[r_delta]
    x_c, _, omega_c = cold_phase_scale(model, r_delta)
    omega_d = alpha * omega_c
    Lf, Cf = filter_components(R, omega_d)

    Tad = adiabatic_photon_temperature(lambda_um, 100.0)
    u0 = T0*T0
    du_total = Tad*Tad-u0
    cool_coeff = 1.0/(2.0*TAU0_CONDITIONAL*u0)
    tau_r = rise_ps*1e-12

    def source(t: float) -> float:
        return du_total/tau_r*math.exp(-t/tau_r)

    def rhs(t: float, y: np.ndarray) -> np.ndarray:
        x,v,u,d,w = y
        u = max(float(u),u0)
        T = math.sqrt(u)
        F = model.force(T,x)
        du = source(t)-cool_coeff*(u*u-u0*u0)
        dv = -(d+F)/(L*C)
        dd = (L/Lf)*(v-w)
        dw = d/(L*Cf)-w/(R*Cf)
        return np.array([v,dv,du,dd,dw])

    # Dense early grid, sufficient to resolve crossing/reformation timing.
    dt = 0.25e-12
    n = int(tend_ns*1e-9/dt)+1
    t = np.linspace(0.0,tend_ns*1e-9,n)
    sol = solve_ivp(rhs,(0.0,t[-1]),np.array([x_c,0.0,u0,0.0,0.0]),
                    t_eval=t,method='DOP853',rtol=4e-8,
                    atol=np.array([1e-10,2e2,1e-13,1e-10,2e2]),
                    max_step=min(dt,0.12/max(omega_c,omega_d)))
    x=sol.y[0]
    T=np.sqrt(np.maximum(sol.y[2],u0))

    signs=np.signbit(x)
    changes=np.where(signs[1:] != signs[:-1])[0]
    crossings=[float(0.5*(t[i]+t[i+1])) for i in changes]

    Tf=model.fold_temperature()
    imax=int(np.argmax(T))
    # first cooling-side index back below fold after the temperature maximum
    inds=np.where(T[imax:] < Tf)[0]
    iref=imax+int(inds[0]) if len(inds) else None

    out: dict[str, object]={
        'Tpeak':float(np.max(T)),
        'Tf':Tf,
        'crossings':crossings,
        'first_cross':crossings[0] if crossings else math.nan,
        'last_cross':crossings[-1] if crossings else math.nan,
        't_reform':float(t[iref]) if iref is not None else math.nan,
        'T_reform':float(T[iref]) if iref is not None else math.nan,
        'x_reform':float(x[iref]) if iref is not None else math.nan,
    }
    if iref is not None:
        # Evaluate a hair below fold if numerical root finder is exactly on edge.
        Teval=min(float(T[iref]),Tf-2e-5)
        try:
            b=directional_barriers(model,Teval)
            out['b_left_reform']=b['b_left']
            out['b_right_reform']=b['b_right']
            out['saddle_reform']=b['saddle']
        except ValueError:
            pass
    return out


def main() -> None:
    print('Experiment 03 directional recovery barriers')
    r=0.6
    model=DynamicForce(r,quick=False)
    Tf=model.fold_temperature()
    EK=kelvin_scale(r)
    print(f'rDelta={r}, E_L/kB={EK:.6f} K, Tf={Tf:.6f} K')

    print('\nDirectional static barrier table:')
    for frac in (0.0,0.25,0.50,0.75,0.90,0.97,0.99):
        T=T0+frac*(Tf-T0)
        b=directional_barriers(model,T)
        print(
            f'T={T:.6f} K ({frac:.2f} fold span): '
            f'B_L/kB={b["b_left"]*EK:.6f} K, '
            f'B_R/kB={b["b_right"]*EK:.6f} K, '
            f'ratio={b["b_right"]/b["b_left"]:.3f}, saddle={b["saddle"]:+.5f}'
        )

    print('\nCausal-filter pulse timing:')
    for R,alpha in [(250.0,0.20),(250.0,0.35),(250.0,0.50)]:
        o=pulse_trace(model,R,alpha)
        br=float(o.get('b_right_reform',math.nan))*EK
        bl=float(o.get('b_left_reform',math.nan))*EK
        msg=(
            f'R={R:g} alpha={alpha:.2f}: Tpeak={float(o["Tpeak"]):.5f} K, '
            f'first_x0={float(o["first_cross"])*1e12:.3f} ps, '
            f'last_x0={float(o["last_cross"])*1e12:.3f} ps, '
            f't_reform={float(o["t_reform"])*1e12:.3f} ps, '
            f'x_reform={float(o["x_reform"]):+.5f}, '
            f'B_L,reform/kB={bl:.5f} K, B_R,reform/kB={br:.5f} K, '
            f'ncross={len(o["crossings"])}'
        )
        print(msg)
        print(f'::notice title=Experiment 03 directional recovery::{msg}')
    print('PASS')

if __name__=='__main__':
    main()
