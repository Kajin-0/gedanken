#!/usr/bin/env python3
"""Experiment 03 local saddle-node dynamic stress.

This reproduces the conditional 14-um table in
DYNAMIC_FOLD_GHOST_2026-08-15.md.

Model layers:
- current retuned realistic-skewness fold family;
- provisional cubic-MQT Cmin values;
- local saddle-node normal form inferred from cold curvature;
- constant-peak ghost-passage estimate plus underdamped recovered-basin envelope;
- conditional Huang clean-graphene thermal mapping.

This is a falsification diagnostic, not a full time-dependent CPR/RCSJ solver.
"""

from __future__ import annotations

import math
from scipy.special import lambertw

HBAR = 1.054571817e-34
KB = 1.380649e-23
ALPHA_Q = 7.2
D_TARGET = 1.0e-6
T0 = 0.020
TAU0 = 75.0e-9
LAMBDA_REF_UM = 1.55
TREF = 2.5
A_REF = 100.0
A = 100.0
LAMBDA_UM = 14.0

# rDelta, Tf[K], barrier/kB[K], Cmin[F], L[H]
ROWS = [
    (1.0, 0.905, 9.10, 161e-15, 87.8e-12),
    (0.8, 0.813, 8.12, 181e-15, 96.8e-12),
    (0.6, 0.695, 6.87, 215e-15, 111.5e-12),
    (0.5, 0.623, 6.10, 244e-15, 123.1e-12),
    (0.4, 0.540, 5.22, 287e-15, 140.3e-12),
]


def infer_kappa(barrier_K: float, Cmin: float, L: float) -> float:
    barrier = barrier_K * KB
    W = float(lambertw(ALPHA_Q * barrier / (2.0 * math.pi * HBAR * D_TARGET)).real)
    return Cmin * ALPHA_Q**2 * barrier**2 * L / (HBAR**2 * W**2)


def tpk_from_lambda(lambda_um: float) -> float:
    return math.sqrt(
        T0**2
        + (LAMBDA_REF_UM / lambda_um)
        * (A_REF / A)
        * (TREF**2 - T0**2)
    )


def dwell(Tpk: float, Tf: float) -> float:
    """Conditional clean-T^4 time above Tf."""
    if Tpk <= Tf:
        return 0.0
    return TAU0 * math.log(
        ((Tpk**2 - T0**2) * (Tf**2 + T0**2))
        / ((Tpk**2 + T0**2) * (Tf**2 - T0**2))
    )


def optimized_dynamic_time(Tpk: float, Tf: float, kappa: float,
                           C: float, L: float) -> tuple[float, float]:
    """Return (optimistic min-max dynamic time, equalizing Ropt).

    Uses the full-ghost local normal-form prefactor and balances it against
    the underdamped recovered-basin envelope 2RC.
    """
    theta = Tpk - Tf
    if theta <= 0.0:
        return math.inf, math.nan
    mu = Tf - T0

    # t_ghost = Atilde/R, where
    # Atilde = 2 pi L/kappa * sqrt(mu/theta).
    Atilde = 2.0 * math.pi * L / kappa * math.sqrt(mu / theta)
    Ropt = math.sqrt(Atilde / (2.0 * C))
    tdyn = math.sqrt(2.0 * C * Atilde)
    return tdyn, Ropt


def main() -> None:
    Tpk = tpk_from_lambda(LAMBDA_UM)
    print("Experiment 03 dynamic saddle-node stress")
    print(f"A={A:g} um^2, lambda={LAMBDA_UM:g} um -> Tpk={Tpk:.6f} K")
    print("conditional Huang clean-T^4 mapping retained\n")
    print("rDel  Tf[K]  theta[K]  kappa  dwell[ps]  tdyn[ps]  margin  Ropt[ohm]")

    for rdel, Tf, barrier_K, Cmin, L in ROWS:
        kappa = infer_kappa(barrier_K, Cmin, L)
        if Tpk <= Tf:
            print(f"{rdel:4.1f}  {Tf:5.3f}   --       {kappa:5.3f}    no static fold")
            continue
        t_above = dwell(Tpk, Tf)
        t_dyn, Ropt = optimized_dynamic_time(Tpk, Tf, kappa, Cmin, L)
        print(
            f"{rdel:4.1f}  {Tf:5.3f}  {Tpk-Tf:8.5f}  {kappa:5.3f}  "
            f"{t_above*1e12:9.3f}  {t_dyn*1e12:8.3f}  "
            f"{t_above/t_dyn:6.3f}  {Ropt:9.2f}"
        )

    print("\nInterpretation:")
    print("  static fold crossing is insufficient near a saddle-node.")
    print("  rDelta=0.8 is extremely vulnerable at 14 um in this conditional stress.")
    print("  rDelta=0.6 is the first retained coarse point with margin >1.")
    print("  full CPR + time-dependent RCSJ integration is required before promotion.")


if __name__ == "__main__":
    main()
