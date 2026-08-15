#!/usr/bin/env python3
"""Empirical CPR-shape nonideality envelope for Experiment 03.

This is deliberately NOT a microscopic interface model. It asks a narrower
falsification question: if the ideal arbitrary-length graphene CPR is too
forward-skewed compared with realistic-interface graphene JJs, does reducing
only the CPR shape skewness destroy the rf-SQUID fold corridor?

The cold ideal shape at ell=1.1, mu/Delta0=20 is mixed with a sinusoid:

    f_lambda(phi,T) = normalize[(1-lambda) sin(phi) + lambda f_ideal(phi,T)]

while retaining the ideal model's Ic(T) amplitude ratio. lambda is selected to
approximately reproduce low-T skewness targets motivated by Nanda et al.
(arXiv:1612.06895): S~0.27 (hard-gap nn'n calculation), ~0.22 (soft-gap nn'n),
and ~0.19 (soft-gap npn / experiment scale).

Because Ic(T), induced gap, contact doping and transparency will also change in
a real junction, this is a shape-only sensitivity envelope, not a device model.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import quad
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq
from scipy.special import lambertw

from arbitrary_length_graphene_cpr import (
    HBAR,
    KB,
    PHI0,
    T0,
    GrapheneCPRModel,
)

ELL = 1.1
MU_R = 20.0
DELTA_TILT = 0.05
BETA_COLD = 0.8
IC_PHYS = 3.0e-6
D_TARGET = 1.0e-6
ALPHA_Q = 7.2

# lambda values chosen on a fine grid to reproduce the target cold skewness.
CASES = [
    ("ideal", 1.000, 0.548),
    ("realistic-hard-gap-scale", 0.590, 0.270),
    ("realistic-soft-nn-scale", 0.515, 0.220),
    ("realistic-soft-npn-scale", 0.468, 0.190),
]

BASE = GrapheneCPRModel(ELL, MU_R, delta=DELTA_TILT)
PHIS = BASE.phis
IC0, _ = BASE.cpr(T0)


def mixed_cpr(T: float, lam: float):
    Ic, spline = BASE.cpr(T)
    ideal = spline(PHIS)
    vals = (1.0 - lam) * np.sin(PHIS) + lam * ideal
    vals /= np.max(vals)
    return Ic, CubicSpline(PHIS, vals)


def shifted_shape(x: float, spline: CubicSpline) -> float:
    if x == 0.0:
        return 0.0
    phi = np.pi - abs(x)
    return float(np.sign(x) * spline(phi))


def shifted_slope(x: float, spline: CubicSpline) -> float:
    phi = np.pi - abs(x)
    return -float(spline(phi, 1))


def skewness(lam: float) -> float:
    _, sp = mixed_cpr(T0, lam)
    vals = sp(PHIS)
    phi_max = float(PHIS[int(np.argmax(vals))])
    return 2.0 * phi_max / np.pi - 1.0


def normalized_fold(T: float, lam: float):
    _, sp = mixed_cpr(T, lam)

    def equation(x: float) -> float:
        f = shifted_shape(x, sp)
        fp = shifted_slope(x, sp)
        return x - f / fp - DELTA_TILT

    grid = np.linspace(-1.5, -1.0e-4, 1200)
    candidates = []
    xa, ya = grid[0], equation(grid[0])
    for xb in grid[1:]:
        yb = equation(xb)
        if np.isfinite(ya) and np.isfinite(yb) and ya * yb < 0.0:
            root = brentq(equation, xa, xb)
            beta_fold = 1.0 / shifted_slope(root, sp)
            if beta_fold > 0.0:
                if all(abs(root - old[0]) > 1.0e-5 for old in candidates):
                    candidates.append((root, beta_fold))
        xa, ya = xb, yb
    if not candidates:
        raise RuntimeError("No selected fold")
    return min(candidates, key=lambda pair: abs(pair[0]))


def beta_required(T: float, lam: float) -> float:
    Ic, _ = mixed_cpr(T, lam)
    _, beta_fold = normalized_fold(T, lam)
    return beta_fold / (Ic / IC0)


def fold_temperature(lam: float) -> float:
    prev_T = T0
    prev = beta_required(prev_T, lam) - BETA_COLD
    for T in np.linspace(0.03, 4.0, 40):
        val = beta_required(float(T), lam) - BETA_COLD
        if prev * val <= 0.0:
            return float(brentq(
                lambda temp: beta_required(temp, lam) - BETA_COLD,
                prev_T, float(T), xtol=3.0e-4,
            ))
        prev_T, prev = float(T), val
    return float("nan")


def cold_metrics(lam: float):
    _, sp = mixed_cpr(T0, lam)

    def force(x: float) -> float:
        return x - DELTA_TILT - BETA_COLD * shifted_shape(x, sp)

    def curvature(x: float) -> float:
        return 1.0 - BETA_COLD * shifted_slope(x, sp)

    grid = np.linspace(-np.pi + 0.005, np.pi - 0.005, 6000)
    roots = []
    xa, ya = grid[0], force(grid[0])
    for xb in grid[1:]:
        yb = force(xb)
        if ya * yb < 0.0:
            root = brentq(force, xa, xb)
            if all(abs(root - old) > 1.0e-6 for old in roots):
                roots.append(root)
        xa, ya = xb, yb

    left = max(r for r in roots if r < 0.0 and curvature(r) > 0.0)
    right = min(r for r in roots if r > 0.0 and curvature(r) > 0.0)
    saddle = min((r for r in roots if curvature(r) < 0.0), key=abs)

    barrier_dimless = quad(force, left, saddle, epsabs=1.0e-10)[0]
    kappa = curvature(left)
    L = BETA_COLD * PHI0 / (2.0 * np.pi * IC_PHYS)
    E_L = (PHI0 / (2.0 * np.pi)) ** 2 / L
    barrier = barrier_dimless * E_L

    z = ALPHA_Q * barrier / (2.0 * np.pi * HBAR * D_TARGET)
    W = float(lambertw(z).real)
    Cmin = (
        HBAR * np.sqrt(kappa / L) * W / (ALPHA_Q * barrier)
    ) ** 2

    return {
        "barrier_K": barrier / KB,
        "curvature": kappa,
        "state_sep_phi0": (right - left) / (2.0 * np.pi),
        "Cmin_fF": Cmin * 1.0e15,
    }


def main() -> None:
    print("Experiment 03 realistic-skewness shape sensitivity")
    print("shape-only envelope: not a microscopic interface model\n")
    print("case lambda S beta_fold T_fold[K] barrier[K] sep[Phi0] Cmin[fF]")
    for name, lam, _ in CASES:
        S = skewness(lam)
        _, bfold = normalized_fold(T0, lam)
        Tfold = fold_temperature(lam)
        m = cold_metrics(lam)
        print(
            f"{name:26s} {lam:5.3f} {S:6.3f} {bfold:8.4f} "
            f"{Tfold:8.3f} {m['barrier_K']:10.3f} "
            f"{m['state_sep_phi0']:9.4f} {m['Cmin_fF']:9.1f}"
        )


if __name__ == "__main__":
    main()
