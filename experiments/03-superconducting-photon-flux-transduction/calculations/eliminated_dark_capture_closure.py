#!/usr/bin/env python3
"""Experiment 03: eliminated dark-count / capture-time closure.

This script reproduces the conditional Huang-calibrated dwell table recorded in
HUANG_THERMAL_DWELL_CALIBRATION_2026-08-15.md and checks the algebraic
elimination

    L C_min,Q = tau_Q^2

for the current retuned family.

IMPORTANT
---------
The 75-ns Huang value is used only through the explicit conditional mapping

    tau_ep^loc(T0=20 mK) = 75 ns

inside the clean graphene Ce~T, Pe-ph~T^4 model. This is not a claim that the
published device has a directly measured local hot-state lifetime equal to the
values calculated here.

The C_min,Q values are inherited from the provisional cubic-MQT diagnostic, not
an exact dissipative rf-SQUID dark-count model.
"""

from __future__ import annotations

import math

T0 = 0.020          # K
TAU0 = 75.0e-9      # s, conditional coefficient identification at T0
G_PHASE = 5.0

# r_Delta, Tf [K], barrier/kB [K], Cmin [F], L [H], lambda thermal max [um]
ROWS = [
    (1.0, 0.905, 9.10, 161e-15, 87.8e-12, 11.83),
    (0.8, 0.813, 8.12, 181e-15, 96.8e-12, 14.66),
    (0.6, 0.695, 6.87, 215e-15, 111.5e-12, 20.07),
    (0.5, 0.623, 6.10, 244e-15, 123.1e-12, 24.98),
    (0.4, 0.540, 5.22, 287e-15, 140.3e-12, 33.27),
]


def tmax_clean(Tf: float) -> float:
    """Infinite-photon-energy dwell ceiling in the retained T^4 cooling law."""
    return TAU0 * math.log((Tf * Tf + T0 * T0) / (Tf * Tf - T0 * T0))


def tau_local(T: float) -> float:
    """Conditional local clean-graphene relaxation scale."""
    return TAU0 * (T0 / T) ** 2


def main() -> None:
    print("Experiment 03 eliminated dark/capture closure")
    print(f"conditional tau_ep^loc({T0*1e3:.0f} mK) = {TAU0*1e9:.1f} ns")
    print(f"g = {G_PHASE:g}\n")

    header = (
        "rDel  Tf[K]  barrier[K]  L[pH]  Cmin[fF]  "
        "tauQ[ps]  tphi[ps]  tmax[ps]  Mphi  Rcrit[ohm]  lamMax[um]"
    )
    print(header)

    for rdel, Tf, barrier_K, Cmin, L, lam in ROWS:
        tau_q = math.sqrt(L * Cmin)
        t_phi = G_PHASE * tau_q
        t_max = tmax_clean(Tf)
        m_phase = t_max / t_phi
        r_crit = t_max / (2.0 * Cmin)

        # Regression of the asymptotic interpretation tmax ~ 2 tau_local(Tf).
        asymptotic_ratio = t_max / (2.0 * tau_local(Tf))
        if abs(asymptotic_ratio - 1.0) > 0.01:
            raise RuntimeError("T0<<Tf asymptotic regression unexpectedly poor")

        print(
            f"{rdel:4.1f}  {Tf:5.3f}   {barrier_K:6.2f}    "
            f"{L*1e12:6.1f}   {Cmin*1e15:7.0f}    "
            f"{tau_q*1e12:7.2f}   {t_phi*1e12:7.2f}   "
            f"{t_max*1e12:7.2f}   {m_phase:5.2f}    "
            f"{r_crit:8.1f}      {lam:6.2f}"
        )

    print("\nInterpretation:")
    print("  phase-only margin survives across the retained family for g=5")
    print("  damping requires R_hot <~ 0.23-0.36 kOhm at C=Cmin,Q")
    print("  R_hot is an effective dynamical damping resistance, not automatically dc R_n")


if __name__ == "__main__":
    main()
