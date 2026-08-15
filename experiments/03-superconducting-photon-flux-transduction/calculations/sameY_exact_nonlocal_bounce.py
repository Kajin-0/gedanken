#!/usr/bin/env python3
"""Stationary nonlocal Euclidean bounce for the Experiment-03 causal bath.

This is the stronger dark-tunneling calculation after
`sameY_dissipative_bounce_screen.py`.

At cold temperature T_b the phase coordinate x obeys the Euclidean stationary
condition

  -L C x''(tau) + F[x(tau),T_b]
  + L K_Y[x](tau) = 0,

where, in Matsubara/Fourier space,

  K_Y(omega_n) = |omega_n| Y_E(|omega_n|),

and the SAME passive two-pole environment used in real-time write dynamics has

  Y_E(s) = (1/R) [1+s/(sqrt(2) omega_D)]
                  /[1+sqrt(2)s/omega_D+(s/omega_D)^2].

The imaginary-time period is beta*hbar.  At 20 mK the current cold phase mode
has beta*hbar*omega_c >> 1, so the periodic solution is close to the zero-T
bounce but still uses the physical finite-temperature period.

Numerics
--------
- Use an even periodic grid with the bounce center fixed at tau=0.  Evenness
  removes the translational zero mode.
- Solve the stationary equation directly with scipy's Krylov root method; do
  NOT minimize the Euclidean action, because the bounce is a saddle.
- Begin at zero environmental coupling from a sech^2 guess, then continue the
  bath strength lambda_Y from 0 to 1.  This tracks the nontrivial stationary
  branch and makes collapse to the trivial metastable solution easy to detect.
- Report spectral residuals, center amplitude and action decomposition.

The resulting exponent is much stronger than the historical cubic formula and
stronger than the fixed-shape variational environment correction.  It is still
a 1D phase-only dissipative instanton: spatial/material escape channels and
rate prefactors remain outside the calculation.
"""
from __future__ import annotations

import copy
import math
from pathlib import Path

import numpy as np
from scipy.interpolate import CubicSpline, RectBivariateSpline
from scipy.optimize import root

from full_dynamic_rfsquid import CASES, DELTA_TILT, DynamicForce, T0
from directional_recovery_barriers import directional_barriers
from finite_time_basin_slice import cold_phase_scale
from quantum_initial_capture import HBAR, KB, PHI_BAR
from sameY_dissipative_bounce_screen import potential_data

SQRT2 = math.sqrt(2.0)
OUT = Path('../RESULTS_EXACT_SAMEY_BOUNCE_2026-08-15.md')


def with_tilt(base: DynamicForce, delta: float) -> DynamicForce:
    m = copy.copy(base)
    m.Ftab = np.asarray(base.Ftab, dtype=float) - (float(delta) - DELTA_TILT)
    m.spline = RectBivariateSpline(m.Tgrid, m.xgrid, m.Ftab, kx=3, ky=3)
    return m


def y_euclid(s: np.ndarray, R: float, omega_d: float) -> np.ndarray:
    z = s / omega_d
    return (1.0 / R) * (1.0 + z / SQRT2) / (1.0 + SQRT2*z + z*z)


def mirror_half(h: np.ndarray) -> np.ndarray:
    # N is even; h contains j=0..N/2 inclusive.
    return np.concatenate([h, h[-2:0:-1]])


def half_from_full(x: np.ndarray) -> np.ndarray:
    return np.asarray(x[: len(x)//2 + 1], dtype=float)


def build_potential_spline(model: DynamicForce, xm: float,
                           xmin: float, xmax: float, nx: int = 50001):
    xx = np.linspace(xmin, xmax, nx)
    TT = np.full_like(xx, T0)
    ff = np.asarray(model.spline.ev(TT, xx)).reshape(-1)
    # U(x)-U(xm) by cumulative integration, with xm inserted via a global
    # primitive spline.
    from scipy.integrate import cumulative_trapezoid
    prim = np.concatenate([[0.0], cumulative_trapezoid(ff, xx)])
    ps = CubicSpline(xx, prim)
    u0 = float(ps(xm))
    return CubicSpline(xx, prim-u0)


def solve_case(model: DynamicForce, R: float, alpha: float,
               *, N: int = 1024, continuation=(0.0,0.1,0.25,0.5,0.75,1.0)):
    L, C, _ = CASES[0.6]
    xm, xs, xr, xt, xpot, upot, uspl_turn, raw = potential_data(model, nx=40001)
    _, kappa, omega_c = cold_phase_scale(model, 0.6)
    omega_d = alpha * omega_c
    period = HBAR/(KB*T0)
    dt = period/N
    j = np.arange(N)
    # Periodic distance from center tau=0.
    tau = np.minimum(j, N-j) * dt

    # Initial nontrivial even bounce.  eta~1 is close enough for undamped
    # continuation; amplitude uses the exact undamped turning point.
    eta = 1.0
    a = 0.5*eta*omega_c
    x0 = xm + (xt-xm)/np.cosh(np.minimum(a*tau, 30.0))**2
    h = half_from_full(x0)

    freq = np.fft.fftfreq(N, dt)
    om = 2.0*math.pi*np.abs(freq)
    YE = y_euclid(om, R, omega_d)
    # Physical potential spline needs enough range for modest dissipative
    # deformation around the undamped turning point.
    ups = build_potential_spline(model, xm,
                                 max(float(model.xgrid[0]), xm-0.5),
                                 min(float(model.xgrid[-1]), xr+0.5))

    def Fvec(x):
        return np.asarray(model.spline.ev(np.full_like(x,T0),x)).reshape(-1)

    records=[]
    for lam in continuation:
        coeff = L*C*om*om + lam*L*om*YE
        def resid(hh):
            x = mirror_half(np.asarray(hh,dtype=float))
            dx = x-xm
            X = np.fft.fft(dx)
            lin = np.fft.ifft(coeff*X).real
            rr = lin + Fvec(x)
            return half_from_full(rr)

        sol = root(resid, h, method='krylov',
                   options={'fatol':2e-10, 'xatol':2e-10, 'maxiter':250})
        h = np.asarray(sol.x,dtype=float)
        rr = resid(h)
        amp = float(h[0]-xm)
        records.append((lam,bool(sol.success),float(np.max(np.abs(rr))),amp,
                        int(getattr(sol,'nit',-1))))
        if amp < 0.05*(xt-xm):
            raise RuntimeError(f'continuation collapsed to trivial state at lambda={lam}: amp={amp}')
        if np.max(np.abs(rr)) > 2e-6:
            raise RuntimeError(f'nonlocal bounce residual too large at lambda={lam}: {np.max(np.abs(rr))}')

    x = mirror_half(h)
    dx = x-xm
    X = np.fft.fft(dx)
    xn = X/N
    # Spectral derivative.
    xdot = np.fft.ifft(1j*2.0*math.pi*freq*X).real
    u = np.asarray(ups(x),dtype=float)
    S_kin = PHI_BAR**2 * 0.5*C*float(np.sum(xdot*xdot))*dt
    S_pot = PHI_BAR**2/L * float(np.sum(u))*dt
    S_env = 0.5*PHI_BAR**2*period*float(np.sum(om*YE*np.abs(xn)**2))
    S_total = S_kin+S_pot+S_env

    # Undamped exact WKB action from actual potential for regression.
    integ = float(np.trapezoid(np.sqrt(np.maximum(upot,0.0)),xpot))
    S0 = (PHI_BAR**2/L) * 2.0*math.sqrt(2.0*L*C)*integ

    return {
        'R':R,'alpha':alpha,'N':N,'period_ps':period*1e12,
        'omega_c_GHz':omega_c/(2*math.pi)*1e-9,
        'xm':xm,'xs':xs,'xt_undamped':xt,'xcenter':float(x[0]),
        'amp':float(x[0]-xm),
        'B0_exact':S0/HBAR,
        'Bkin':S_kin/HBAR,'Bpot':S_pot/HBAR,'Benv':S_env/HBAR,
        'Btotal':S_total/HBAR,
        'env_log10_supp':S_env/(HBAR*math.log(10.0)),
        'continuation':records,
    }


def main():
    print('Experiment 03 exact stationary same-Y nonlocal bounce')
    base = DynamicForce(0.6, quick=False, Tmax=0.95)
    model = with_tilt(base, 0.05)
    rows=[]
    for R,alpha in [
        (150.0,0.70),(150.0,0.80),
        (100.0,0.80),(80.0,0.90),(80.0,1.00),
        (20.0,0.90),(20.0,1.00),
    ]:
        out=solve_case(model,R,alpha,N=1024)
        rows.append(out)
        msg=(
            f'R={R:g} alpha={alpha:.2f}: B0_exact={out["B0_exact"]:.6f}, '
            f'Bkin={out["Bkin"]:.6f}, Bpot={out["Bpot"]:.6f}, '
            f'Benv={out["Benv"]:.6f}, Btotal={out["Btotal"]:.6f}, '
            f'env_log10_supp={out["env_log10_supp"]:.3f}, '
            f'xcenter={out["xcenter"]:+.6f}, amp={out["amp"]:.6f}'
        )
        print(msg)
        print(f'::notice title=Experiment 03 exact same-Y bounce::{msg}')

    lines=[
        '# Experiment 03 — Exact Same-Y Nonlocal Bounce Results — 2026-08-15','',
        'Stationary even periodic Euclidean bounce at 20 mK in the actual cold full-CPR potential.',
        'The same passive two-pole Y used in real-time capture enters the Matsubara influence kernel.','',
        '```text'
    ]
    for o in rows:
        lines.append(
            f'R={o["R"]:g} ohm alpha={o["alpha"]:.2f}: '
            f'B0_exact={o["B0_exact"]:.8f}; Bkin={o["Bkin"]:.8f}; '
            f'Bpot={o["Bpot"]:.8f}; Benv={o["Benv"]:.8f}; '
            f'Btotal={o["Btotal"]:.8f}; env_log10_supp={o["env_log10_supp"]:.5f}; '
            f'xcenter={o["xcenter"]:+.7f}; amp={o["amp"]:.7f}'
        )
        lines.append('  continuation: '+repr(o['continuation']))
    lines += ['```','',
              '`B0_exact` is the zero-temperature undamped 1D WKB/full-potential exponent regression.',
              '`Btotal` is the stationary finite-20-mK nonlocal dissipative action exponent from the spectral root.','',
              'Rate prefactors and non-phase dark channels remain outside this calculation.']
    OUT.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(f'wrote {OUT}')
    print('PASS')

if __name__=='__main__':
    main()
