#!/usr/bin/env python3
"""Map the near-critical 14-um rise-time / scalar-R capture boundary.

This is a research calculation, not part of the fast CI workflow.  It imports
the full deterministic Experiment-03 solver and finds the first left->right
capture transition as R is increased, then fits

    R_min = K / (tau_c - tau_r)^p

to the near-critical points recorded in
RATE_DAMPING_CRITICAL_SCALING_2026-08-15.md.

The fit is descriptive of the current scalar-R model.  The p~1 scaling is
expected for a regular boundary in (tau_r, 1/R); the detector-specific outputs
are tau_c and K.
"""

from __future__ import annotations

import math
import numpy as np
from scipy.optimize import curve_fit

from full_dynamic_rfsquid import DynamicForce, simulate


def boundary(model: DynamicForce, r_delta: float, rise_ps: float,
             *, lam_um: float = 14.0,
             R_lo: float = 1.0, R_hi: float = 2.0e4) -> float:
    """First left->right transition as R is increased, geometric bisection."""
    scan = np.logspace(np.log10(R_lo), np.log10(R_hi), 45)
    prev_R = float(scan[0])
    prev_b = simulate(model, r_delta, prev_R, lambda_um=lam_um,
                      rise_ps=rise_ps, tend_ns=0.6)["basin"]

    for R0 in scan[1:]:
        R = float(R0)
        b = simulate(model, r_delta, R, lambda_um=lam_um,
                     rise_ps=rise_ps, tend_ns=0.6)["basin"]
        if prev_b == "left" and b == "right":
            lo, hi = prev_R, R
            for _ in range(13):
                mid = math.sqrt(lo * hi)
                bm = simulate(model, r_delta, mid, lambda_um=lam_um,
                              rise_ps=rise_ps, tend_ns=0.6)["basin"]
                if bm == "right":
                    hi = mid
                else:
                    lo = mid
            return math.sqrt(lo * hi)
        prev_R, prev_b = R, b

    return math.nan


def divergence(t: np.ndarray, K: float, tc: float, p: float) -> np.ndarray:
    return K / (tc - t) ** p


def fit_boundary(rows: list[tuple[float, float]], cutoff: float,
                 tc_guess: float) -> tuple[np.ndarray, np.ndarray]:
    arr = np.asarray([(t, R) for t, R in rows
                      if np.isfinite(R) and t >= cutoff], dtype=float)
    lower = [0.0, float(np.max(arr[:, 0]) + 1.0e-4), 0.1]
    upper = [1.0e7, float(np.max(arr[:, 0]) + 5.0), 5.0]
    popt, pcov = curve_fit(
        divergence,
        arr[:, 0], arr[:, 1],
        p0=[700.0, tc_guess, 1.0],
        bounds=(lower, upper),
        maxfev=100000,
    )
    return popt, np.sqrt(np.diag(pcov))


def run_family(r_delta: float, rises: list[float], cutoff: float,
               tc_guess: float) -> None:
    print(f"\nrDelta={r_delta:.1f}")
    model = DynamicForce(r_delta, quick=False)
    rows: list[tuple[float, float]] = []
    for rise in rises:
        R = boundary(model, r_delta, rise)
        rows.append((rise, R))
        print(f"  rise={rise:6.2f} ps  R_min={R:10.3f} ohm")

    popt, perr = fit_boundary(rows, cutoff, tc_guess)
    K, tc, p = popt
    print("fit R_min = K/(tau_c-tau_r)^p")
    print(f"  K     = {K:.4f} +/- {perr[0]:.4f} ohm ps^p")
    print(f"  tau_c = {tc:.6f} +/- {perr[1]:.6f} ps")
    print(f"  p     = {p:.6f} +/- {perr[2]:.6f}")


if __name__ == "__main__":
    print("Experiment 03 near-critical rise/damping boundary")
    print("WARNING: full-grid research calculation; can take several minutes.")
    run_family(
        0.8,
        [3.0, 5.0, 7.0, 8.0, 8.5, 9.0, 9.25, 9.5],
        cutoff=7.0,
        tc_guess=9.7,
    )
    run_family(
        0.6,
        [10.0, 20.0, 25.0, 28.0, 30.0, 30.5, 31.0],
        cutoff=25.0,
        tc_guess=31.3,
    )
