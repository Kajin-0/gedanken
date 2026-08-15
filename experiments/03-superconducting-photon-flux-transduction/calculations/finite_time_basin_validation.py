#!/usr/bin/env python3
"""Full-resolution finite-time basin-section diagnostic.

Evaluate the pulled-back basin boundary at the physical cold coordinate x=x_c
on both sides of two already-established scalar-R capture boundaries.

This diagnostic intentionally reports the nearest velocity-space basin edge
rather than assuming its orientation in advance.  The finite-pulse flow can
produce multiple phase-space basin strips in underdamped regions, so the first
validation task is to inspect the actual local section and only then promote a
signed-margin convention.

The script uses the full CPR grid and emits GitHub Actions notice annotations so
results remain visible through the Checks API.
"""

from __future__ import annotations

import math
import traceback

from finite_time_basin_slice import (
    cold_phase_scale,
    edge_velocity,
    physical_basin,
)
from full_dynamic_rfsquid import DynamicForce


def robust_edge(model: DynamicForce, r_delta: float, R: float, x_c: float,
                rise_ps: float) -> tuple[float, str, str, float]:
    """Expand the velocity search window until a local basin edge is found."""
    last_exc: Exception | None = None
    for vmax in (4.0, 8.0, 16.0):
        try:
            v_edge, lab_lo, lab_hi = edge_velocity(
                model,
                r_delta,
                R,
                x_c,
                lambda_um=14.0,
                rise_ps=rise_ps,
                nscan=41,
                iterations=15,
                vmax_norm=vmax,
            )
            return v_edge, lab_lo, lab_hi, vmax
        except RuntimeError as exc:
            last_exc = exc
    assert last_exc is not None
    raise last_exc


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
        v_edge, lab_lo, lab_hi, vmax = robust_edge(
            model, r_delta, R, x_c, rise_ps
        )
        rows.append(
            (R, basin, v_edge / omega_c, v_edge, lab_lo, lab_hi, vmax)
        )

        msg = (
            f"rDelta={r_delta:.1f}, rise={rise_ps:g} ps, R={R:g} ohm; "
            f"physical={basin}; nearest edge v/omega_c={v_edge/omega_c:.6f}; "
            f"edge orientation={lab_lo}->{lab_hi}; search |v|<{vmax:g} omega_c; "
            f"omega_c/2pi={omega_c/(2*math.pi)*1e-9:.3f} GHz"
        )
        print(msg)
        safe = msg.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
        print(f"::notice title=Experiment 03 finite-time basin section::{safe}")

    # The only scientific assertion made before inspecting edge orientation is
    # the already-established physical v=0 basin change across these brackets.
    assert rows[0][1] == "left", rows
    assert rows[1][1] == "right", rows

    # Report (but do not yet enforce) whether the same nearest edge changes sign.
    v0 = rows[0][2]
    v1 = rows[1][2]
    if v0 * v1 < 0.0:
        R_zero = R_fail + (R_capture - R_fail) * v0 / (v0 - v1)
        summary = (
            f"rDelta={r_delta:.1f}, rise={rise_ps:g} ps: nearest v-edge changes "
            f"sign across physical capture bracket; linear zero~{R_zero:.2f} ohm"
        )
    else:
        summary = (
            f"rDelta={r_delta:.1f}, rise={rise_ps:g} ps: physical basin changes "
            f"but nearest v-edge does NOT change sign (v0={v0:.6f}, v1={v1:.6f}); "
            f"local section has nontrivial/multiple basin geometry"
        )
    print(summary)
    safe = summary.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
    print(f"::notice title=Experiment 03 finite-time basin summary::{safe}")


if __name__ == "__main__":
    try:
        print("Experiment 03 full-resolution finite-time basin diagnostic")
        check_pair(0.8, rise_ps=5.0, R_fail=150.0, R_capture=185.0)
        check_pair(0.6, rise_ps=20.0, R_fail=55.0, R_capture=75.0)
        print("PASS")
    except Exception as exc:
        message = f"{type(exc).__name__}: {exc}".replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
        print(f"::error title=Experiment 03 finite-time basin failure::{message}")
        traceback.print_exc()
        raise
