#!/usr/bin/env python3
"""Four-dimensional initial-state capture scout for the passive two-pole bath.

This is the first Experiment-03 capture calculation that samples the *joint*
linearized quantum-FDT covariance of

    [dx, u, d, s]

with

    u = xdot/omega_c,
    d = L I_env/Phi_bar,
    s = V_C/(Phi_bar omega_c).

The covariance comes from two_pole_joint_covariance.py and therefore includes
system-filter correlations required by the same passive Y(omega) used in the
deterministic dynamics.

The joint Gaussian is integrated with low-order tensor Gauss-Hermite quadrature.
Because the final-basin indicator is discontinuous and the basin is folded,
this is explicitly a scouting calculation.  Order convergence must be checked
at any apparently favorable point before using the number quantitatively.

Still absent:
- resistor/FDT noise injected *during* the optical pulse;
- exact nonlinear open-system quantum dynamics;
- dissipative MQT with the same spectral density;
- spatial thermal stochasticity.
"""

from __future__ import annotations

import itertools
import math

import numpy as np
from numpy.polynomial.hermite import hermgauss

from causal_two_pole_environment import simulate_filtered
from finite_time_basin_slice import cold_phase_scale
from full_dynamic_rfsquid import DynamicForce
from two_pole_joint_covariance import covariance_matrix


def joint_capture_probability(
    model: DynamicForce,
    R: float,
    alpha: float,
    *,
    order: int,
    r_delta: float = 0.6,
    rise_ps: float = 20.0,
    lambda_um: float = 14.0,
    tend_ns: float = 0.6,
) -> tuple[float, dict[str, float]]:
    M = covariance_matrix(model, r_delta, R, alpha)
    # Numerical PSD guard.
    evals, evecs = np.linalg.eigh(M)
    if float(np.min(evals)) < -1.0e-10:
        raise RuntimeError(f"covariance not PSD: min eigenvalue={np.min(evals)}")
    evals = np.maximum(evals, 0.0)
    A = evecs @ np.diag(np.sqrt(evals))

    nodes, weights = hermgauss(order)
    x_c, _, omega_c = cold_phase_scale(model, r_delta)
    norm = math.pi ** 2  # (sqrt(pi))^4

    p = 0.0
    total = 0.0
    right_count = 0
    ntraj = 0

    for inds in itertools.product(range(order), repeat=4):
        z = math.sqrt(2.0) * np.array([nodes[i] for i in inds], dtype=float)
        state = A @ z
        dx, u, d, s = [float(v) for v in state]
        wgt = float(np.prod([weights[i] for i in inds])) / norm

        out = simulate_filtered(
            model,
            r_delta,
            R,
            alpha,
            x0=x_c + dx,
            v0=u * omega_c,
            d0=d,
            w0=s * omega_c,
            lambda_um=lambda_um,
            rise_ps=rise_ps,
            tend_ns=tend_ns,
        )
        total += wgt
        ntraj += 1
        if out["basin"] == "right":
            p += wgt
            right_count += 1

    stats = {
        "total_weight": total,
        "ntraj": float(ntraj),
        "right_node_fraction": right_count / ntraj,
        "eigmin": float(np.min(evals)),
        "eigmax": float(np.max(evals)),
    }
    return p / total, stats


def main() -> None:
    print("Experiment 03 4D joint system-filter initial capture scout")
    print("quick CPR grid; tensor GH order=3; no pulse-time bath noise")
    model = DynamicForce(0.6, quick=True)

    cases = [
        (120.0, 0.20), (120.0, 0.35), (120.0, 0.50),
        (160.0, 0.20), (160.0, 0.35), (160.0, 0.50),
        (250.0, 0.20), (250.0, 0.35), (250.0, 0.50), (250.0, 0.75),
        (400.0, 0.20), (400.0, 0.35), (400.0, 0.50),
    ]
    for R, alpha in cases:
        p, st = joint_capture_probability(model, R, alpha, order=3)
        msg = (
            f"R={R:g} ohm, alpha={alpha:.2f}: P_R_GH3={p:.6f}, "
            f"node_right={st['right_node_fraction']:.3f}, ntraj={int(st['ntraj'])}"
        )
        print(msg)
        print(f"::notice title=Experiment 03 joint-capture scout::{msg}")

    print("PASS")


if __name__ == "__main__":
    main()
