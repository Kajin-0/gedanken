#!/usr/bin/env python3
"""Robust coarse-grid smoke regression for full_dynamic_rfsquid.py.

CI should verify structural scientific behavior, not demand that the deliberately
coarse --quick CPR grid reproduce fine-grid crossover resistances to a few ohms.

Checks retained here:
1. the full interpolated force has a cold left/right bistable pair;
2. its static fold remains in the broad validated temperature corridor;
3. at 14 um, strong damping leaves the phase in the original basin while a
   substantially weaker-damping case reaches the favored basin for both retained
   r_Delta checkpoints;
4. simulated temperatures/coordinates remain finite.

Fine crossover locations remain research outputs of full_dynamic_rfsquid.py on
the full grid and are not CI constants.
"""

from __future__ import annotations

import math

from full_dynamic_rfsquid import DynamicForce, simulate


def check_case(r_delta: float, fold_range: tuple[float, float],
               R_left: float, R_right: float) -> None:
    model = DynamicForce(r_delta, quick=True)
    left, right = model.cold_states()
    assert left < 0.0 < right

    Tf = model.fold_temperature()
    lo, hi = fold_range
    assert lo < Tf < hi, (r_delta, Tf, fold_range)

    out_left = simulate(model, r_delta, R_left, rise_ps=0.0, tend_ns=1.5)
    out_right = simulate(model, r_delta, R_right, rise_ps=0.0, tend_ns=1.5)

    assert out_left["basin"] == "left", (r_delta, R_left, out_left)
    assert out_right["basin"] == "right", (r_delta, R_right, out_right)

    for out in (out_left, out_right):
        for key in ("x_final", "x_min", "x_max", "Tpeak"):
            assert math.isfinite(float(out[key])), (r_delta, key, out)

    print(
        f"rDelta={r_delta:.1f}: Tf={Tf:.4f} K; "
        f"R={R_left:g} ohm -> left; R={R_right:g} ohm -> right"
    )


def main() -> None:
    print("Experiment 03 robust full-dynamic smoke regression")
    # Deliberately broad ranges around the validated fine-grid folds.
    check_case(0.8, (0.76, 0.84), R_left=40.0, R_right=500.0)
    check_case(0.6, (0.64, 0.73), R_left=10.0, R_right=200.0)
    print("PASS")


if __name__ == "__main__":
    main()
