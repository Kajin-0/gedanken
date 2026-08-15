#!/usr/bin/env python3
"""Experiment 03 sudden-quench energy threshold.

For a rapid potential quench, the phase initially remains at the cold metastable
minimum x_c.  This script evaluates

    B_q(T) = U(x_s(T),T) - U(x_c,T)
           = integral_{x_c}^{x_s(T)} F(x,T) dx

using the same full nonlinear force construction as full_dynamic_rfsquid.py.
The zero B_q(T_q)=0 defines the conservative held-hot quench-energy threshold.

This threshold is not a universal detector cutoff.  It organizes the
nonadiabatic sub-fold regime and provides a regression for the values recorded
in SUDDEN_QUENCH_BOUND_2026-08-15.md.
"""

from __future__ import annotations

import argparse
from scipy.integrate import quad
from scipy.optimize import brentq

from full_dynamic_rfsquid import DynamicForce, T0


def quench_barrier(model: DynamicForce, T: float) -> float:
    left_cold, _ = model.cold_states()
    roots = model.roots(T)
    saddles = [x for x, curvature in roots if curvature < 0.0]
    if not saddles:
        raise ValueError("No finite saddle: temperature is at/above static fold")
    saddle = min(saddles, key=abs)
    return float(quad(lambda x: model.force(T, x), left_cold, saddle,
                      epsabs=1.0e-10)[0])


def quench_temperature(model: DynamicForce) -> tuple[float, float]:
    Tf = model.fold_temperature()
    prev_T = T0
    prev = quench_barrier(model, prev_T)
    for i in range(1, 100):
        T = T0 + (Tf - T0 - 2.0e-4) * i / 100.0
        val = quench_barrier(model, T)
        if prev * val <= 0.0:
            Tq = brentq(lambda temp: quench_barrier(model, temp), prev_T, T,
                         xtol=1.0e-8)
            return Tq, Tf
        prev_T, prev = T, val
    raise RuntimeError("No quench-energy zero found below fold")


def wavelength_from_temperature(T: float) -> float:
    return 1.55 * (2.5**2 - T0**2) / (T**2 - T0**2)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--quick", action="store_true")
    args = p.parse_args()

    print("Experiment 03 sudden-quench energy threshold")
    print("100 um^2 Huang-ratio energy calibration\n")
    for r in (0.8, 0.6):
        model = DynamicForce(r, quick=args.quick)
        Tq, Tf = quench_temperature(model)
        print(
            f"rDelta={r:.1f}: Tq={Tq:.4f} K, Tf={Tf:.4f} K, "
            f"lambda_q={wavelength_from_temperature(Tq):.2f} um, "
            f"lambda_fold={wavelength_from_temperature(Tf):.2f} um"
        )

    print("\nInterpretation:")
    print("  lambda_fold < lambda_q creates a nonadiabatic sub-fold regime.")
    print("  lambda_q is a conservative held-hot quench-energy threshold, not a")
    print("  universal time-dependent detector cutoff.")


if __name__ == "__main__":
    main()
