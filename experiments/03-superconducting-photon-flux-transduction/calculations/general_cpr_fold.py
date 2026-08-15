#!/usr/bin/env python3
"""General current-phase-relation fold conditions for Experiment 03.

Use the dimensionless phase-force convention

    F(x,T) = x - delta - i(x,T),

where i = I_s / I_* and I_* = Phi0/(2 pi L).  A static fold obeys

    F = 0,
    dF/dx = 0,

or equivalently

    i(xc,Tc) = xc - delta,
    di/dx(xc,Tc) = 1.

For a separable CPR i(x,T)=beta(T) f(x),

    beta_c = 1/f'(xc),
    delta  = xc - f(xc)/f'(xc).

The script verifies the sinusoidal result and explores a normalized
second-harmonic family f=(sin x + r sin 2x)/max_x(sin x+r sin2x) to show how
CPR shape changes the required beta suppression.  This is a sensitivity study,
not a model of a specific graphene junction.
"""

import numpy as np
from scipy.optimize import brentq


def normalization(r):
    x = np.linspace(-np.pi, np.pi, 400001)
    return np.max(np.sin(x) + r * np.sin(2.0 * x))


def fold_for_second_harmonic(delta, r):
    norm = normalization(r)

    def f(x):
        return (np.sin(x) + r * np.sin(2.0 * x)) / norm

    def fp(x):
        return (np.cos(x) + 2.0 * r * np.cos(2.0 * x)) / norm

    def fold_eq(x):
        return x - f(x) / fp(x) - delta

    # Find candidate negative-phase folds and retain positive beta_c.
    grid = np.linspace(-1.55, -1e-7, 100000)
    roots = []
    g0 = fold_eq(grid[0])
    x0 = grid[0]
    for x1 in grid[1:]:
        g1 = fold_eq(x1)
        if np.isfinite(g0) and np.isfinite(g1) and g0 * g1 < 0:
            root = brentq(fold_eq, x0, x1)
            beta_c = 1.0 / fp(root)
            if beta_c > 0 and (not roots or abs(root - roots[-1][0]) > 1e-7):
                roots.append((root, beta_c))
        x0, g0 = x1, g1

    if not roots:
        return None

    # Select the fold closest to the sinusoidal operating branch near -0.5 rad.
    return min(roots, key=lambda item: abs(item[0] + 0.5))


def main():
    delta = 0.05
    beta_cold = 1.5

    a = brentq(lambda z: np.tan(z) - z - delta, 1e-12, np.pi / 2 - 1e-10)
    beta_sine = 1.0 / np.cos(a)
    print("General-CPR fold benchmark")
    print(f"sinusoidal analytic xc      = {-a:.9f}")
    print(f"sinusoidal analytic beta_c  = {beta_sine:.9f}")

    print("\nNormalized second-harmonic sensitivity")
    print("r        xc(rad)       beta_c       q_req at beta_cold=1.5")
    for r in [-0.10, 0.0, 0.10, 0.20, 0.30]:
        result = fold_for_second_harmonic(delta, r)
        if result is None:
            print(f"{r:+.2f}     no fold on selected branch")
            continue
        xc, beta_c = result
        qreq = 1.0 - beta_c / beta_cold
        if qreq < 0:
            qtext = "cold beta below fold"
        else:
            qtext = f"{100*qreq:8.3f}%"
        print(f"{r:+.2f}   {xc: .9f}   {beta_c: .9f}   {qtext}")

    print("\nInterpretation: changing CPR shape can materially shift the bifurcation")
    print("threshold.  A realistic device must use a measured or microscopic CPR;")
    print("the sinusoidal threshold is a benchmark, not a universal number.")


if __name__ == "__main__":
    main()
