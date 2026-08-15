#!/usr/bin/env python3
"""Trace all local basin edges on the x=x_c finite-time section.

The first finite_time_basin_validation run showed that the nearest velocity edge
can change branch and therefore does not necessarily track the physical v=0
capture boundary.  This script resolves the full ordered sequence of left/right
basin strips in initial velocity at fixed x=x_c.

It focuses on the r_Delta=0.8, 14-um, 5-ps-rise case where the nearest-edge
linear interpolation disagreed with the direct physical R_min boundary.
"""

from __future__ import annotations

import math

import numpy as np

from finite_time_basin_slice import cold_phase_scale, simulate_from_state
from full_dynamic_rfsquid import DynamicForce


def label(model: DynamicForce, r_delta: float, R: float, x_c: float,
          vn: float, omega_c: float, rise_ps: float) -> str:
    return str(
        simulate_from_state(
            model,
            r_delta,
            R,
            x_c,
            vn * omega_c,
            lambda_um=14.0,
            rise_ps=rise_ps,
            tend_ns=1.5,
        )["basin"]
    )


def all_edges(model: DynamicForce, r_delta: float, R: float,
              rise_ps: float, *, vmax: float = 3.0,
              nscan: int = 121, iterations: int = 16):
    x_c, kappa_c, omega_c = cold_phase_scale(model, r_delta)
    grid = np.linspace(-vmax, vmax, nscan)
    labs = [label(model, r_delta, R, x_c, float(v), omega_c, rise_ps)
            for v in grid]

    edges: list[tuple[float, str, str]] = []
    for lo0, hi0, lab_lo, lab_hi in zip(grid[:-1], grid[1:], labs[:-1], labs[1:]):
        if lab_lo == lab_hi:
            continue
        lo = float(lo0)
        hi = float(hi0)
        left_label = lab_lo
        for _ in range(iterations):
            mid = 0.5 * (lo + hi)
            lm = label(model, r_delta, R, x_c, mid, omega_c, rise_ps)
            if lm == left_label:
                lo = mid
            else:
                hi = mid
        edges.append((0.5 * (lo + hi), lab_lo, lab_hi))

    physical = label(model, r_delta, R, x_c, 0.0, omega_c, rise_ps)
    return x_c, kappa_c, omega_c, physical, edges


def edge_string(edges: list[tuple[float, str, str]]) -> str:
    if not edges:
        return "none"
    return "; ".join(
        f"{v:+.6f}:{a}->{b}" for v, a, b in edges
    )


def run_family(r_delta: float, rise_ps: float, Rs: list[float]) -> None:
    model = DynamicForce(r_delta, quick=False)
    for R in Rs:
        x_c, kappa_c, omega_c, physical, edges = all_edges(
            model, r_delta, R, rise_ps
        )
        msg = (
            f"rDelta={r_delta:.1f}, rise={rise_ps:g} ps, R={R:g} ohm; "
            f"physical(v=0)={physical}; edges v/omega_c=[{edge_string(edges)}]; "
            f"omega_c/2pi={omega_c/(2*math.pi)*1e-9:.3f} GHz"
        )
        print(msg)
        safe = msg.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
        print(f"::notice title=Experiment 03 basin-section topology::{safe}")


if __name__ == "__main__":
    print("Experiment 03 full finite-time basin-section topology")
    run_family(0.8, rise_ps=5.0, Rs=[150.0, 160.0, 166.0, 170.0, 185.0])
    # One control family where the first shooting validation looked simpler.
    run_family(0.6, rise_ps=20.0, Rs=[55.0, 64.0, 66.0, 75.0])
    print("PASS")
