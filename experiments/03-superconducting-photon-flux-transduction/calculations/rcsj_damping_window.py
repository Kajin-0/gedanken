#!/usr/bin/env python3
"""Exact linear RCSJ damping window for Experiment 03.

Starting from

    L C y'' + (L/R) y' + kappa y = 0,

this script reconstructs kappa from the retained provisional MQT/Cmin
checkpoints and evaluates the exact scalar-Ohmic resistance interval that
settles the linearized recovered-basin mode within the conditionally calibrated
maximum thermal dwell.

The physical environment of a real GJJ is frequency dependent. These values are
therefore model diagnostics, not a device-level shunt recommendation.
"""

from __future__ import annotations

import math
from scipy.special import lambertw

HBAR = 1.054571817e-34
KB = 1.380649e-23
ALPHA_Q = 7.2
D_TARGET = 1.0e-6
T0 = 0.020
TAU0 = 75e-9

# r_Delta, Tf[K], barrier/kB[K], Cmin[F], L[H]
ROWS = [
    (1.0, 0.905, 9.10, 161e-15, 87.8e-12),
    (0.8, 0.813, 8.12, 181e-15, 96.8e-12),
    (0.6, 0.695, 6.87, 215e-15, 111.5e-12),
    (0.5, 0.623, 6.10, 244e-15, 123.1e-12),
    (0.4, 0.540, 5.22, 287e-15, 140.3e-12),
]


def tmax_clean(Tf: float) -> float:
    return TAU0 * math.log((Tf * Tf + T0 * T0) / (Tf * Tf - T0 * T0))


def infer_kappa(barrier_K: float, Cmin: float, L: float) -> float:
    """Invert the retained provisional MQT Cmin expression for kappa."""
    barrier = barrier_K * KB
    W = float(lambertw(ALPHA_Q * barrier / (2.0 * math.pi * HBAR * D_TARGET)).real)
    return (
        Cmin * ALPHA_Q**2 * barrier**2 * L
        / (HBAR**2 * W**2)
    )


def slow_time(R: float, L: float, C: float, kappa: float) -> float:
    """Slowest linearized e-fold time for positive scalar Ohmic R."""
    omega0 = math.sqrt(kappa / (L * C))
    Rstar = 0.5 * math.sqrt(L / (C * kappa))
    r = R / Rstar
    if r >= 1.0:  # underdamped, envelope
        return r / omega0
    q = 1.0 / r   # overdamped
    return (q + math.sqrt(q * q - 1.0)) / omega0


def main() -> None:
    print("Experiment 03 exact linear RCSJ damping window")
    print("conditional Huang coefficient mapping retained for tmax\n")
    print(
        "rDel  kappa  tauQ[ps]  tmax[ps]  a  "
        "R-[ohm]  R*[ohm]  R+[ohm]  checks"
    )

    for rdel, Tf, barrier_K, Cmin, L in ROWS:
        kappa = infer_kappa(barrier_K, Cmin, L)
        tau_q = math.sqrt(L * Cmin)
        tmax = tmax_clean(Tf)
        omega0 = math.sqrt(kappa) / tau_q
        a = omega0 * tmax
        if a < 1.0:
            raise RuntimeError("No scalar-R settling window exists")

        Rstar = L / (2.0 * tau_q * math.sqrt(kappa))
        Rlo = Rstar * (2.0 * a / (a * a + 1.0))
        Rhi = Rstar * a

        # Exact identities / boundary regressions.
        assert math.isclose(Rhi, tmax / (2.0 * Cmin), rel_tol=2e-12)
        assert math.isclose(slow_time(Rstar, L, Cmin, kappa), 1.0 / omega0, rel_tol=2e-12)
        assert math.isclose(slow_time(Rlo, L, Cmin, kappa), tmax, rel_tol=2e-10)
        assert math.isclose(slow_time(Rhi, L, Cmin, kappa), tmax, rel_tol=2e-10)

        print(
            f"{rdel:4.1f}  {kappa:5.3f}   {tau_q*1e12:7.3f}   "
            f"{tmax*1e12:8.3f}  {a:5.2f}  "
            f"{Rlo:7.3f}   {Rstar:7.3f}   {Rhi:8.3f}  PASS"
        )

    print("\nInterpretation:")
    print("  R+ reproduces the old tmax/(2 Cmin) underdamped upper edge.")
    print("  R- is the missing overdamped lower edge.")
    print("  fastest linear settling occurs at R=R* (critical damping).")


if __name__ == "__main__":
    main()
