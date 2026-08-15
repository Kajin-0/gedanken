#!/usr/bin/env python3
"""Initial quantum-Wigner capture probability for Experiment 03.

This is the first probability calculation built on the exact finite-time basin
picture.  Noise during the optical pulse is still absent; only the cold phase
mode's harmonic quantum/thermal initial-state distribution is included.

For each selected deterministic pulse point, we integrate the full nonlinear
RCSJ trajectory over a tensor Gauss-Hermite quadrature of the cold harmonic
Wigner distribution in (x,v):

    P_R^(init) = integral_{Omega_R^0} rho_W(x,v) dx dv.

The harmonic oscillator Wigner function is an ordinary positive Gaussian with

    sigma_x^2 = hbar/(2 C Phi_bar^2 omega_c) coth(hbar omega_c/2kT)
    sigma_v^2 = hbar omega_c/(2 C Phi_bar^2) coth(...)

and zero x-v covariance.

IMPORTANT
---------
- This is NOT final detector efficiency.
- Pulse/environment noise, dissipative MQT, spatial thermal stochasticity and
  readout backaction are absent.
- C is still inherited from the provisional MQT-optimal C_min,Q family.
- The rDelta=0.8 pulled-back basin is multistrip; quadrature-order convergence
  is therefore scientifically important, not merely numerical housekeeping.
"""

from __future__ import annotations

import argparse
import math

import numpy as np
from numpy.polynomial.hermite import hermgauss

from finite_time_basin_slice import cold_phase_scale, simulate_from_state
from full_dynamic_rfsquid import CASES, DynamicForce

HBAR = 1.054571817e-34
KB = 1.380649e-23
H = 6.62607015e-34
E_CHARGE = 1.602176634e-19
PHI0 = H / (2.0 * E_CHARGE)
PHI_BAR = PHI0 / (2.0 * math.pi)
T0 = 0.020


def quantum_covariance(model: DynamicForce, r_delta: float) -> dict[str, float]:
    L, C, _ = CASES[r_delta]
    x_c, kappa_c, omega_c = cold_phase_scale(model, r_delta)
    q = HBAR * omega_c / (2.0 * KB * T0)
    coth = 1.0 / math.tanh(q)
    sigma_x2 = HBAR / (2.0 * C * PHI_BAR**2 * omega_c) * coth
    sigma_v2 = HBAR * omega_c / (2.0 * C * PHI_BAR**2) * coth
    return {
        "x_c": x_c,
        "kappa_c": kappa_c,
        "omega_c": omega_c,
        "sigma_x": math.sqrt(sigma_x2),
        "sigma_v": math.sqrt(sigma_v2),
        "q": q,
    }


def capture_probability(
    model: DynamicForce,
    r_delta: float,
    R: float,
    rise_ps: float,
    *,
    order: int,
    lambda_um: float = 14.0,
    tend_ns: float = 0.6,
) -> tuple[float, dict[str, float], float]:
    """Tensor Gauss-Hermite integral of the initial harmonic Wigner Gaussian."""
    cov = quantum_covariance(model, r_delta)
    nodes, weights = hermgauss(order)
    norm = math.pi

    right_weight = 0.0
    total_weight = 0.0
    weighted_x = 0.0

    # Standard normal variable z = sqrt(2) * Hermite node.
    for i, xi in enumerate(nodes):
        x0 = cov["x_c"] + math.sqrt(2.0) * cov["sigma_x"] * float(xi)
        for j, vj in enumerate(nodes):
            v0 = math.sqrt(2.0) * cov["sigma_v"] * float(vj)
            w = float(weights[i] * weights[j]) / norm
            out = simulate_from_state(
                model,
                r_delta,
                R,
                x0,
                v0,
                lambda_um=lambda_um,
                rise_ps=rise_ps,
                tend_ns=tend_ns,
            )
            total_weight += w
            weighted_x += w * x0
            if out["basin"] == "right":
                right_weight += w

    return right_weight / total_weight, cov, total_weight


def report_case(
    model: DynamicForce,
    r_delta: float,
    rise_ps: float,
    R: float,
    orders: list[int],
) -> None:
    # Physical deterministic center label.
    cov = quantum_covariance(model, r_delta)
    center = simulate_from_state(
        model,
        r_delta,
        R,
        cov["x_c"],
        0.0,
        lambda_um=14.0,
        rise_ps=rise_ps,
        tend_ns=0.6,
    )["basin"]

    results: list[tuple[int, float]] = []
    for order in orders:
        P, cov, wsum = capture_probability(
            model,
            r_delta,
            R,
            rise_ps,
            order=order,
        )
        results.append((order, P))

    summary = ", ".join(f"n={n}:P_R={P:.6f}" for n, P in results)
    msg = (
        f"rDelta={r_delta:.1f}, rise={rise_ps:g} ps, R={R:g} ohm; "
        f"center={center}; {summary}; "
        f"sigma_x={cov['sigma_x']:.6f} rad; "
        f"sigma_v/omega_c={cov['sigma_v']/cov['omega_c']:.6f}; "
        f"hbaromega/(kBT)={2*cov['q']:.2f}"
    )
    print(msg)
    safe = msg.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
    print(f"::notice title=Experiment 03 quantum initial capture::{safe}")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--order", type=int, default=5,
                   help="highest Gauss-Hermite order; lower odd order also reported")
    args = p.parse_args()
    n_hi = int(args.order)
    if n_hi < 3:
        raise ValueError("order must be >=3")
    n_lo = max(3, n_hi - 2)
    if n_lo % 2 == 0:
        n_lo -= 1
    if n_hi % 2 == 0:
        n_hi += 1
    orders = sorted(set([n_lo, n_hi]))

    print("Experiment 03 harmonic-Wigner initial-state capture probability")
    print(f"Gauss-Hermite orders: {orders}\n")

    m08 = DynamicForce(0.8, quick=False)
    m06 = DynamicForce(0.6, quick=False)

    # Below / near / above the deterministic center-state boundaries.
    # r=.8 is intentionally the folded/multistrip family.
    for R in (150.0, 185.0, 300.0):
        report_case(m08, 0.8, rise_ps=5.0, R=R, orders=orders)

    # r=.6 is the locally simpler broad-strip family.
    for R in (55.0, 75.0, 120.0):
        report_case(m06, 0.6, rise_ps=20.0, R=R, orders=orders)

    print("\nInterpretation:")
    print("  These probabilities include only the initial harmonic Wigner spread.")
    print("  Significant order dependence, especially for rDelta=.8, indicates that")
    print("  folded pulled-back basin strips are not yet resolved by the chosen")
    print("  quadrature and require higher/adaptive integration.")


if __name__ == "__main__":
    main()
