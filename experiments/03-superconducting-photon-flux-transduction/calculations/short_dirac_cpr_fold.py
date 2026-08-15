#!/usr/bin/env python3
"""Short-junction ballistic graphene CPR sensitivity for Experiment 03.

Purpose
-------
Test how a forward-skewed microscopic graphene CPR changes the rf-SQUID fold
relative to the sinusoidal benchmark.  This is intentionally a *model-failure /
sensitivity* calculation: the 2026 MoRe/graphene photon-detector junction has
L_JJ ~ 0.6 um and hbar v_F/Delta ~ 0.5 um, so it is not safely in the short
junction limit.

For a wide ballistic graphene junction at the Dirac point, use transmission
eigenvalues tau=sech^2(u) and the short-junction finite-temperature current
shape

 I(phi,T) ∝ Delta(T) ∫du [tau sin(phi)/sqrt(1-tau sin^2(phi/2))]
                     tanh[Delta(T)sqrt(1-tau sin^2(phi/2))/(2 k_B T)].

A BCS interpolation is used for Delta(T).  The physical CPR is converted to
the x=phi-pi rf-SQUID sign convention, then the general fold equations are
solved.  Results are not a prediction for the intermediate-length MoRe device.
"""

import math
import numpy as np
from scipy.integrate import quad
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq

KB_EV = 8.617333262e-5
DELTA0_EV = 1.3e-3
TC = DELTA0_EV / (1.764 * KB_EV)
T0 = 0.020
DELTA_FLUX = 0.05
PHIS = np.linspace(1e-5, math.pi - 1e-5, 1800)


def gap_bcs(T):
    if T >= TC:
        return 0.0
    return DELTA0_EV * math.tanh(1.74 * math.sqrt(TC / T - 1.0))


def current_raw(phi, T):
    Delta = gap_bcs(T)
    if Delta <= 0.0:
        return 0.0
    y = Delta / (2.0 * KB_EV * T)
    s2 = math.sin(phi / 2.0) ** 2

    def integrand(u):
        tau = 1.0 / math.cosh(u) ** 2
        den = math.sqrt(max(1e-18, 1.0 - tau * s2))
        return tau * math.sin(phi) / den * math.tanh(y * den)

    return Delta * quad(integrand, 0.0, 12.0, epsabs=1e-9,
                        epsrel=1e-8, limit=100)[0]


_cache = {}


def cpr(T):
    key = round(T, 8)
    if key not in _cache:
        vals = np.array([current_raw(phi, T) for phi in PHIS])
        Ic = float(vals.max())
        _cache[key] = (Ic, CubicSpline(PHIS, vals / Ic))
    return _cache[key]


IC0, _ = cpr(T0)


def f_shift(x, T):
    """Normalized rf-SQUID current shape in x=phi-pi convention."""
    _, spline = cpr(T)
    ax = abs(x)
    phi = math.pi - ax
    g = float(spline(phi))
    return g if x > 0 else (-g if x < 0 else 0.0)


def fp_shift(x, T):
    _, spline = cpr(T)
    phi = math.pi - abs(x)
    # derivative is even in x
    return -float(spline(phi, 1))


def normalized_fold(T, delta=DELTA_FLUX):
    def equation(x):
        return x - f_shift(x, T) / fp_shift(x, T) - delta

    grid = np.linspace(-1.5, -1e-4, 1200)
    candidates = []
    for x0, x1 in zip(grid[:-1], grid[1:]):
        y0, y1 = equation(x0), equation(x1)
        if np.isfinite(y0) and np.isfinite(y1) and y0 * y1 < 0:
            root = brentq(equation, x0, x1)
            beta_fold = 1.0 / fp_shift(root, T)
            if beta_fold > 0 and all(abs(root-r) > 1e-6 for r, _ in candidates):
                candidates.append((root, beta_fold))
    if not candidates:
        raise RuntimeError("No selected-branch fold found")
    return min(candidates, key=lambda pair: abs(pair[0] + 0.2))


def fold_margin(T, beta_cold):
    Ic, _ = cpr(T)
    beta_amp = beta_cold * Ic / IC0
    _, beta_fold = normalized_fold(T)
    return beta_amp - beta_fold


def critical_temperature(beta_cold):
    if fold_margin(T0, beta_cold) <= 0:
        return None
    grid = np.linspace(0.03, TC - 0.05, 120)
    pT, pm = T0, fold_margin(T0, beta_cold)
    for T in grid:
        m = fold_margin(float(T), beta_cold)
        if pm * m < 0:
            return brentq(lambda temp: fold_margin(temp, beta_cold), pT, float(T))
        pT, pm = float(T), m
    return None


def main():
    xi_um = 6.582119569e-16 * 1e6 / DELTA0_EV * 1e6  # hbar[eV s] vF / Delta
    print("Short ballistic graphene CPR sensitivity")
    print(f"BCS Tc from Delta0=1.3 meV     = {TC:.3f} K")
    print(f"xi=hbar vF/Delta (vF=1e6 m/s) = {xi_um:.3f} um")
    print(f"0.6-um junction L/xi           = {0.6/xi_um:.3f}")
    print("\nTemperature-dependent normalized fold:")
    for T in [0.02, 1.2, 2.5, 4.2]:
        Ic, _ = cpr(T)
        xc, bf = normalized_fold(T)
        print(f"T={T:4.2f} K: Ic/Ic0={Ic/IC0:.6f}, xc={xc:.6f}, beta_fold={bf:.6f}")

    print("\nFold temperature versus cold beta:")
    for beta in [0.60, 0.70, 0.80, 0.90, 1.00, 1.20, 1.50]:
        Tc_fold = critical_temperature(beta)
        print(f"beta_cold={beta:4.2f}: T_fold={Tc_fold if Tc_fold else float('nan'):.4f} K")

    print("\nInterpretation:")
    print("The forward-skewed short-junction CPR has a much lower cold fold")
    print("threshold than a sinusoidal CPR.  A beta_cold=1.5 design is therefore")
    print("unnecessarily deep in the bistable regime for this idealized CPR and")
    print("would require ~5 K to unfold.  Re-optimizing beta_cold near the actual")
    print("cold fold can reduce T_fold below the 2.5-K photon-heating benchmark.")
    print("Because L_JJ/xi is order unity for the 2026 MoRe device, these numbers")
    print("are sensitivity results only; arbitrary-length CPR physics is required.")


if __name__ == "__main__":
    main()
