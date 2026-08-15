#!/usr/bin/env python3
"""Full-resolution finite-time basin-section validation.

Evaluate the pulled-back basin boundary at the physical cold coordinate x=x_c
on both sides of two already-established scalar-R capture boundaries.

For a right-going target basin the expected local orientation is:

    physical failure (v=0 left basin)  -> nearest edge requires +v kick
    physical capture (v=0 right basin) -> nearest edge lies at -v

Therefore v_edge must change sign across the known R_min.  This validates that
the shooting section is tracking the same finite-time basin boundary that the
full physical v=0 solver detects.

The script uses the full CPR grid, not quick mode.  It emits GitHub Actions
notice annotations so numerical results remain visible through the Checks API.
"""

from __future__ import annotations

import math

from finite_time_basin_slice import (
    cold_phase_scale,
    edge_velocity,
    physical_basin,
)
from full_dynamic_rfsquid import DynamicForce


def check_pair(r_delta: float, rise_ps: float, R_fail: float, R_capture: float) -> None:
    model = DynamicForce(r_delta, quick=False)
    x_c, kappa_c, omega_c = cold_phase_scale(model, r_delta)

    rows = []
    for R in (R_fail, R_capture):
        basin = physical_basin(
            model,
            r_delta,
            R,
            lambda_um=14.0,
            rise_ps=rise_ps,
        )
        v_edge, lab_lo, lab_hi = edge_velocity(
            model,
            r_delta,
            R,
            x_c,
            lambda_um=14.0,
            rise_ps=rise_ps,
            nscan=31,
            iterations=14,
            vmax_norm=4.0,
        )
        rows.append((R, basin, v_edge / omega_c, v_edge, lab_lo, lab_hi))

    R0, basin0, vedge0_n, vedge0, _, _ = rows[0]
    R1, basin1, vedge1_n, vedge1, _, _ = rows[1]

    assert basin0 == "left", rows
    assert basin1 == "right", rows
    assert vedge0_n > 0.0, rows
    assert vedge1_n < 0.0, rows

    # Linear interpolation of this local section gives a diagnostic estimate of
    # where v_edge=0.  Do not confuse it with a replacement for the direct
    # full-solver R_min bisection.
    R_edge_linear = R0 + (R1 - R0) * vedge0_n / (vedge0_n - vedge1_n)

    message = (
        f"rDelta={r_delta:.1f}, rise={rise_ps:g} ps; "
        f"R={R0:g} ohm left: v_edge/omega_c={vedge0_n:.6f}; "
        f"R={R1:g} ohm right: v_edge/omega_c={vedge1_n:.6f}; "
        f"linear zero~{R_edge_linear:.2f} ohm; "
        f"omega_c/2pi={omega_c/(2*math.pi)*1e-9:.3f} GHz"
    )
    print(message)
    safe = message.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
    print(f"::notice title=Experiment 03 finite-time basin section::{safe}")


if __name__ == "__main__":
    print("Experiment 03 full-resolution finite-time basin validation")
    check_pair(0.8, rise_ps=5.0, R_fail=150.0, R_capture=185.0)
    check_pair(0.6, rise_ps=20.0, R_fail=55.0, R_capture=75.0)
    print("PASS")
