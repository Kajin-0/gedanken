#!/usr/bin/env python3
"""Nested x-grid convergence for Experiment 03 quantum basin probability.

The geometry-aware velocity integration in quantum_basin_integral.py removes the
main discontinuous-u quadrature problem. This script removes the remaining
Gauss-Hermite sensitivity in x by evaluating

    P_R = integral phi(z) P_R(u | x_c + sigma_x z) dz,

on nested uniform z grids and using composite Simpson integration. The omitted
|z|>zmax contribution is reported as a rigorous probability-mass bound rather
than guessed.

This is still initial-state quantum/thermal averaging only. Pulse/environment
noise and dissipative quantum dynamics are absent.
"""

from __future__ import annotations

import argparse
import math

import numpy as np
from scipy.integrate import simpson
from scipy.special import ndtr

from full_dynamic_rfsquid import DynamicForce
from quantum_basin_integral import conditional_right_probability
from quantum_initial_capture import quantum_covariance

SQRT2PI = math.sqrt(2.0 * math.pi)


def normal_pdf(z: np.ndarray) -> np.ndarray:
    return np.exp(-0.5 * z * z) / SQRT2PI


def integrate_case(
    model: DynamicForce,
    r_delta: float,
    R: float,
    rise_ps: float,
    *,
    nxs: list[int],
    zmax_x: float,
    zmax_u: float,
    nscan_u: int,
    lambda_um: float = 14.0,
) -> tuple[list[tuple[int, float]], dict[str, float], float]:
    cov = quantum_covariance(model, r_delta)
    sigma = cov["sigma_x"]
    sigma_u = cov["sigma_v"] / cov["omega_c"]

    nmax = max(nxs)
    if nmax % 2 == 0:
        raise ValueError("maximum nx must be odd")

    zfine = np.linspace(-zmax_x, zmax_x, nmax)
    pcond = np.empty(nmax, dtype=float)
    edge_counts = np.empty(nmax, dtype=int)

    for i, z in enumerate(zfine):
        x0 = cov["x_c"] + sigma * float(z)
        p_u, edges = conditional_right_probability(
            model,
            r_delta,
            R,
            x0,
            sigma_u,
            cov["omega_c"],
            rise_ps=rise_ps,
            lambda_um=lambda_um,
            zmax=zmax_u,
            nscan=nscan_u,
        )
        pcond[i] = p_u
        edge_counts[i] = len(edges)

    results: list[tuple[int, float]] = []
    for nx in nxs:
        if nx < 3 or nx % 2 == 0:
            raise ValueError("all nx values must be odd >=3")
        # Nested grids require (nmax-1) divisible by (nx-1).
        if (nmax - 1) % (nx - 1) != 0:
            raise ValueError(f"nx={nx} is not nested in nmax={nmax}")
        step = (nmax - 1) // (nx - 1)
        z = zfine[::step]
        y = pcond[::step] * normal_pdf(z)
        central = float(simpson(y, x=z))
        results.append((nx, central))

    tail_mass = 2.0 * (1.0 - float(ndtr(zmax_x)))
    stats = {
        "sigma": sigma,
        "min_edges": float(np.min(edge_counts)),
        "max_edges": float(np.max(edge_counts)),
        "max_dp_neighbor": float(np.max(np.abs(np.diff(pcond)))) if nmax > 1 else 0.0,
    }
    return results, stats, tail_mass


def report_case(
    model: DynamicForce,
    r_delta: float,
    rise_ps: float,
    R: float,
    *,
    nxs: list[int],
    zmax_x: float,
    zmax_u: float,
    nscan_u: int,
) -> None:
    results, stats, tail = integrate_case(
        model,
        r_delta,
        R,
        rise_ps,
        nxs=nxs,
        zmax_x=zmax_x,
        zmax_u=zmax_u,
        nscan_u=nscan_u,
    )
    summary = ", ".join(f"nx={n}:Pcentral={p:.6f}" for n, p in results)
    pfin = results[-1][1]
    msg = (
        f"rDelta={r_delta:.1f}, rise={rise_ps:g} ps, R={R:g} ohm; "
        f"{summary}; final rigorous interval=[{pfin:.6f},{min(1.0,pfin+tail):.6f}]; "
        f"tail_mass<={tail:.3e}; sigma={stats['sigma']:.6f}; "
        f"edge_count={int(stats['min_edges'])}..{int(stats['max_edges'])}; "
        f"max_neighbor_dP={stats['max_dp_neighbor']:.3f}"
    )
    print(msg)
    safe = msg.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
    print(f"::notice title=Experiment 03 x-grid Wigner convergence::{safe}")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--nmax", type=int, default=33)
    p.add_argument("--zmax-x", type=float, default=4.5)
    p.add_argument("--zmax-u", type=float, default=5.5)
    p.add_argument("--nscan-u", type=int, default=65)
    args = p.parse_args()

    nmax = int(args.nmax)
    if nmax not in (17, 33, 65):
        raise ValueError("supported nested nmax values are 17, 33, 65")
    nxs = [n for n in (9, 17, 33, 65) if n <= nmax]

    print("Experiment 03 nested x-grid Wigner convergence")
    print(
        f"nx={nxs}; zmax_x={args.zmax_x:g}; "
        f"zmax_u={args.zmax_u:g}; nscan_u={args.nscan_u}\n"
    )

    m08 = DynamicForce(0.8, quick=False)
    m06 = DynamicForce(0.6, quick=False)

    for R in (185.0, 300.0):
        report_case(
            m08, 0.8, 5.0, R,
            nxs=nxs,
            zmax_x=args.zmax_x,
            zmax_u=args.zmax_u,
            nscan_u=args.nscan_u,
        )
    for R in (75.0, 120.0):
        report_case(
            m06, 0.6, 20.0, R,
            nxs=nxs,
            zmax_x=args.zmax_x,
            zmax_u=args.zmax_u,
            nscan_u=args.nscan_u,
        )

    print("PASS")


if __name__ == "__main__":
    main()
