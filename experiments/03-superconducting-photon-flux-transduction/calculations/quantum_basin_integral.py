#!/usr/bin/env python3
"""Geometry-aware initial Wigner capture integral for Experiment 03.

The first quantum_initial_capture.py used tensor Gauss-Hermite quadrature on a
discontinuous two-dimensional basin indicator. That is inefficient for folded
finite-time basins and showed material order dependence.

This script conditions on x. At each x quadrature node it:

1. scans normalized velocity u=v/omega_c over a finite many-sigma interval,
2. locates every left/right basin transition,
3. integrates the Gaussian velocity probability analytically between those
   transition points,
4. integrates the resulting conditional P(right|x) over the Gaussian x
   distribution by Gauss-Hermite quadrature.

The velocity tails outside +/- zmax sigma_u are included using the basin labels
at the scan endpoints; the omitted probability from an undetected extra strip
outside that interval is bounded by the Gaussian tail and should be checked by
zmax convergence.

This includes only the cold harmonic Wigner initial-state distribution. Pulse
noise, dissipative-MQT fluctuations, thermal-transport stochasticity and readout
backaction remain absent.
"""

from __future__ import annotations

import argparse
import math

import numpy as np
from numpy.polynomial.hermite import hermgauss
from scipy.special import ndtr

from finite_time_basin_slice import simulate_from_state
from full_dynamic_rfsquid import DynamicForce
from quantum_initial_capture import quantum_covariance


def basin_label(
    model: DynamicForce,
    r_delta: float,
    R: float,
    x0: float,
    u0: float,
    omega_c: float,
    *,
    rise_ps: float,
    lambda_um: float,
    tend_ns: float,
) -> str:
    return str(
        simulate_from_state(
            model,
            r_delta,
            R,
            x0,
            u0 * omega_c,
            lambda_um=lambda_um,
            rise_ps=rise_ps,
            tend_ns=tend_ns,
        )["basin"]
    )


def conditional_right_probability(
    model: DynamicForce,
    r_delta: float,
    R: float,
    x0: float,
    sigma_u: float,
    omega_c: float,
    *,
    rise_ps: float,
    lambda_um: float = 14.0,
    tend_ns: float = 0.6,
    zmax: float = 5.5,
    nscan: int = 65,
    bisect_iter: int = 12,
) -> tuple[float, list[tuple[float, str, str]]]:
    """Integrate P(right|x0) by resolving all velocity-basin strips."""
    umax = zmax * sigma_u
    grid = np.linspace(-umax, umax, nscan)
    labels = [
        basin_label(
            model, r_delta, R, x0, float(u), omega_c,
            rise_ps=rise_ps, lambda_um=lambda_um, tend_ns=tend_ns,
        )
        for u in grid
    ]

    edges: list[tuple[float, str, str]] = []
    for ua, ub, la, lb in zip(grid[:-1], grid[1:], labels[:-1], labels[1:]):
        if la == lb:
            continue
        lo = float(ua)
        hi = float(ub)
        left_label = la
        for _ in range(bisect_iter):
            mid = 0.5 * (lo + hi)
            lm = basin_label(
                model, r_delta, R, x0, mid, omega_c,
                rise_ps=rise_ps, lambda_um=lambda_um, tend_ns=tend_ns,
            )
            if lm == left_label:
                lo = mid
            else:
                hi = mid
        edges.append((0.5 * (lo + hi), la, lb))

    # Build intervals from -infinity to +infinity. The label outside the scan is
    # taken from the corresponding endpoint. With zmax>=5 this affects only a
    # sub-ppm Gaussian tail unless a remote basin strip folds back into the tail.
    bounds = [-math.inf] + [e[0] for e in edges] + [math.inf]
    interval_labels = [labels[0]]
    for _, _la, lb in edges:
        interval_labels.append(lb)

    p_right = 0.0
    for lo, hi, lab in zip(bounds[:-1], bounds[1:], interval_labels):
        if lab != "right":
            continue
        zlo = -math.inf if math.isinf(lo) and lo < 0 else lo / sigma_u
        zhi = math.inf if math.isinf(hi) and hi > 0 else hi / sigma_u
        plo = 0.0 if zlo == -math.inf else float(ndtr(zlo))
        phi = 1.0 if zhi == math.inf else float(ndtr(zhi))
        p_right += phi - plo

    return float(p_right), edges


def integrated_probability(
    model: DynamicForce,
    r_delta: float,
    R: float,
    rise_ps: float,
    *,
    order_x: int,
    lambda_um: float = 14.0,
    zmax: float = 5.5,
    nscan: int = 65,
) -> tuple[float, dict[str, float], list[tuple[float, float, int]]]:
    cov = quantum_covariance(model, r_delta)
    sigma_x = cov["sigma_x"]
    sigma_u = cov["sigma_v"] / cov["omega_c"]
    nodes, weights = hermgauss(order_x)

    total = 0.0
    details: list[tuple[float, float, int]] = []
    for node, weight in zip(nodes, weights):
        x0 = cov["x_c"] + math.sqrt(2.0) * sigma_x * float(node)
        p_u, edges = conditional_right_probability(
            model,
            r_delta,
            R,
            x0,
            sigma_u,
            cov["omega_c"],
            rise_ps=rise_ps,
            lambda_um=lambda_um,
            zmax=zmax,
            nscan=nscan,
        )
        w = float(weight) / math.sqrt(math.pi)
        total += w * p_u
        details.append((x0, p_u, len(edges)))

    return float(total), cov, details


def report_case(
    model: DynamicForce,
    r_delta: float,
    rise_ps: float,
    R: float,
    orders_x: list[int],
    *,
    zmax: float,
    nscan: int,
) -> None:
    results = []
    last_cov = None
    last_details = None
    for n in orders_x:
        p, cov, details = integrated_probability(
            model,
            r_delta,
            R,
            rise_ps,
            order_x=n,
            zmax=zmax,
            nscan=nscan,
        )
        results.append((n, p))
        last_cov = cov
        last_details = details

    assert last_cov is not None and last_details is not None
    edge_counts = [d[2] for d in last_details]
    summary = ", ".join(f"nx={n}:P_R={p:.6f}" for n, p in results)
    msg = (
        f"rDelta={r_delta:.1f}, rise={rise_ps:g} ps, R={R:g} ohm; "
        f"{summary}; sigma={last_cov['sigma_x']:.6f}; "
        f"edge_count_range={min(edge_counts)}..{max(edge_counts)}; "
        f"zmax={zmax:g}; nscan={nscan}"
    )
    print(msg)
    safe = msg.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
    print(f"::notice title=Experiment 03 geometry-aware Wigner integral::{safe}")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--max-order-x", type=int, default=7)
    p.add_argument("--zmax", type=float, default=5.5)
    p.add_argument("--nscan", type=int, default=65)
    args = p.parse_args()

    nmax = int(args.max_order_x)
    if nmax < 3:
        raise ValueError("max-order-x must be >=3")
    if nmax % 2 == 0:
        nmax += 1
    orders = [n for n in range(3, nmax + 1, 2)]

    print("Experiment 03 geometry-aware initial-Wigner capture integral")
    print(f"x orders={orders}, zmax={args.zmax:g}, nscan={args.nscan}\n")

    m08 = DynamicForce(0.8, quick=False)
    m06 = DynamicForce(0.6, quick=False)

    # Representative transition/interior points. The most folded family is .8.
    for R in (185.0, 300.0):
        report_case(
            m08, 0.8, 5.0, R, orders,
            zmax=args.zmax, nscan=args.nscan,
        )

    for R in (75.0, 120.0):
        report_case(
            m06, 0.6, 20.0, R, orders,
            zmax=args.zmax, nscan=args.nscan,
        )

    print("\nInterpretation:")
    print("  x-order convergence is now the main quadrature diagnostic because")
    print("  the discontinuous velocity indicator is integrated through explicit")
    print("  basin-strip boundaries rather than sampled by tensor quadrature.")


if __name__ == "__main__":
    main()
