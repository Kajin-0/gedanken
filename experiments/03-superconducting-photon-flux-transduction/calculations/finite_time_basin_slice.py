#!/usr/bin/env python3
"""Finite-time pulled-back basin boundary: shooting section at x=x_c.

Experiment 03 has moved beyond instantaneous-saddle capture criteria.  For a
prescribed thermal pulse, the exact deterministic initial-time basin boundary is

    B_0 = Phi_{tf,0}^{-1}(W_f^s),

where W_f^s is the stable manifold separating the recovered cold flux basins.

This script computes a robust one-dimensional section of B_0 without explicitly
integrating a stable-manifold curve backward.  At fixed initial phase coordinate
x0, it shoots in initial phase velocity v0 and finds the nearest left/right basin
transition.  At the physical cold coordinate x_c,

    v_edge = 0

is exactly the deterministic pulse-parameter capture boundary.

The calculation uses the same full CPR, conditional thermal pulse and scalar-R
model as full_dynamic_rfsquid.py.  It is still a model diagnostic rather than a
fabricated-device prediction.
"""

from __future__ import annotations

import argparse
import math

import numpy as np
from scipy.integrate import solve_ivp

from full_dynamic_rfsquid import (
    CASES,
    DynamicForce,
    T0,
    TAU0_CONDITIONAL,
    adiabatic_photon_temperature,
)


def simulate_from_state(
    model: DynamicForce,
    r_delta: float,
    R: float,
    x0: float,
    v0: float,
    *,
    lambda_um: float = 14.0,
    area_um2: float = 100.0,
    rise_ps: float = 0.0,
    tend_ns: float = 1.5,
) -> dict[str, float | str]:
    """Integrate the full deterministic pulse from arbitrary (x0,v0)."""
    L, C, _ = CASES[r_delta]
    left, right = model.cold_states()
    Tad = adiabatic_photon_temperature(lambda_um, area_um2)
    u0 = T0 * T0
    du_total = Tad * Tad - u0
    cool_coeff = 1.0 / (2.0 * TAU0_CONDITIONAL * u0)

    if rise_ps <= 0.0:
        y0 = np.array([x0, v0, Tad * Tad], dtype=float)

        def source(_t: float) -> float:
            return 0.0
    else:
        tau_r = rise_ps * 1.0e-12
        y0 = np.array([x0, v0, u0], dtype=float)

        def source(t: float) -> float:
            return du_total / tau_r * math.exp(-t / tau_r)

    def rhs(t: float, y: np.ndarray) -> np.ndarray:
        x, v, u = y
        u = max(float(u), u0)
        T = math.sqrt(u)
        F = model.force(T, x)
        du = source(t) - cool_coeff * (u * u - u0 * u0)
        return np.array([v, -((L / R) * v + F) / (L * C), du])

    sol = solve_ivp(
        rhs,
        (0.0, tend_ns * 1.0e-9),
        y0,
        method="DOP853",
        rtol=5.0e-7,
        atol=np.array([2.0e-9, 1.0e3, 1.0e-12]),
        max_step=5.0e-12,
    )

    xf = float(sol.y[0, -1])
    basin = "right" if abs(xf - right) < abs(xf - left) else "left"
    return {
        "basin": basin,
        "x_final": xf,
        "v_final": float(sol.y[1, -1]),
        "Tpeak": float(np.sqrt(np.max(sol.y[2]))),
    }


def cold_phase_scale(model: DynamicForce, r_delta: float) -> tuple[float, float, float]:
    """Return (x_c, kappa_c, omega_c) for the cold left well."""
    L, C, _ = CASES[r_delta]
    roots = model.roots(T0)
    left_candidates = [(x, k) for x, k in roots if x < 0.0 and k > 0.0]
    if not left_candidates:
        raise RuntimeError("No cold left stable state")
    x_c, kappa_c = max(left_candidates, key=lambda pair: pair[0])
    omega_c = math.sqrt(kappa_c / (L * C))
    return float(x_c), float(kappa_c), float(omega_c)


def edge_velocity(
    model: DynamicForce,
    r_delta: float,
    R: float,
    x0: float,
    *,
    lambda_um: float,
    rise_ps: float,
    vmax_norm: float = 5.0,
    nscan: int = 51,
    iterations: int = 22,
) -> tuple[float, str, str]:
    """Find the basin transition nearest v=0 on a fixed-x initial section.

    Velocity is internally normalized by the cold small-oscillation frequency.
    The returned v_edge is dimensional [rad/s].
    """
    _, _, omega_c = cold_phase_scale(model, r_delta)
    vs_norm = np.linspace(-vmax_norm, vmax_norm, nscan)
    labels: list[str] = []

    for vn in vs_norm:
        labels.append(
            str(
                simulate_from_state(
                    model,
                    r_delta,
                    R,
                    x0,
                    float(vn) * omega_c,
                    lambda_um=lambda_um,
                    rise_ps=rise_ps,
                    tend_ns=1.5,
                )["basin"]
            )
        )

    brackets: list[tuple[float, float, str, str]] = []
    for a, b, la, lb in zip(vs_norm[:-1], vs_norm[1:], labels[:-1], labels[1:]):
        if la != lb:
            brackets.append((float(a), float(b), la, lb))

    if not brackets:
        raise RuntimeError(
            f"No basin edge found within |v|<{vmax_norm} omega_c at x0={x0:.6g}"
        )

    # Select the transition closest to the physical v=0 initial state.
    lo, hi, lab_lo, lab_hi = min(
        brackets, key=lambda item: min(abs(item[0]), abs(item[1]))
    )

    for _ in range(iterations):
        mid = 0.5 * (lo + hi)
        lab_mid = str(
            simulate_from_state(
                model,
                r_delta,
                R,
                x0,
                mid * omega_c,
                lambda_um=lambda_um,
                rise_ps=rise_ps,
                tend_ns=1.5,
            )["basin"]
        )
        if lab_mid == lab_lo:
            lo = mid
        else:
            hi = mid

    edge_norm = 0.5 * (lo + hi)
    return edge_norm * omega_c, lab_lo, lab_hi


def physical_basin(
    model: DynamicForce,
    r_delta: float,
    R: float,
    *,
    lambda_um: float,
    rise_ps: float,
) -> str:
    x_c, _, _ = cold_phase_scale(model, r_delta)
    return str(
        simulate_from_state(
            model,
            r_delta,
            R,
            x_c,
            0.0,
            lambda_um=lambda_um,
            rise_ps=rise_ps,
        )["basin"]
    )


def report_case(
    model: DynamicForce,
    r_delta: float,
    rise_ps: float,
    Rs: list[float],
    *,
    lambda_um: float = 14.0,
) -> None:
    x_c, kappa_c, omega_c = cold_phase_scale(model, r_delta)
    print(
        f"\nrDelta={r_delta:.1f}, rise={rise_ps:g} ps, lambda={lambda_um:g} um\n"
        f"  x_c={x_c:.6f}, kappa_c={kappa_c:.6f}, "
        f"omega_c/2pi={omega_c/(2*math.pi)*1e-9:.3f} GHz"
    )
    print("  R[ohm]  physical  v_edge/omega_c   v_edge[1e9 rad/s]")
    for R in Rs:
        v_edge, _, _ = edge_velocity(
            model,
            r_delta,
            R,
            x_c,
            lambda_um=lambda_um,
            rise_ps=rise_ps,
        )
        basin = physical_basin(
            model, r_delta, R, lambda_um=lambda_um, rise_ps=rise_ps
        )
        print(
            f"  {R:7.2f}  {basin:8s}  {v_edge/omega_c:14.6f}  "
            f"{v_edge/1e9:17.6f}"
        )


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--quick", action="store_true")
    args = p.parse_args()

    print("Experiment 03 finite-time basin-boundary shooting section")
    print("v_edge=0 should coincide with the physical deterministic capture boundary.")

    m08 = DynamicForce(0.8, quick=args.quick)
    m06 = DynamicForce(0.6, quick=args.quick)

    # Bracket the already-known full-resolution lower-capture boundaries.
    report_case(m08, 0.8, 5.0, [150.0, 166.0, 185.0])
    report_case(m06, 0.6, 20.0, [55.0, 64.0, 75.0])

    print("\nInterpretation:")
    print("  failure side should require a positive initial-velocity kick to capture;")
    print("  capture side should have the physical v=0 point on the target side,")
    print("  so the nearest edge moves through zero as R crosses R_min.")


if __name__ == "__main__":
    main()
