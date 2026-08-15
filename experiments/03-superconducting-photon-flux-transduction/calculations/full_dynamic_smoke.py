#!/usr/bin/env python3
"""Coarse-grid numerical smoke regression for full_dynamic_rfsquid.py.

The deliberate `quick=True` CPR grid is not sufficiently accurate to guard
fine static folds or deterministic capture boundaries. Those scientific values
are kept in full-resolution checkpoints and separate analytical regressions.

This smoke test instead guards the numerical plumbing that CI can test robustly:

1. both retained models build a finite full CPR/phase-force table;
2. each cold potential contains distinct left/right stable states;
3. direct nonlinear RCSJ integration completes with finite coordinates and
   temperature for representative photon pulses;
4. returned basin labels are valid.

Failure therefore indicates an implementation/numerical regression rather than
ordinary coarse-grid movement of a bifurcation boundary.
"""

from __future__ import annotations

import math
import numpy as np

from full_dynamic_rfsquid import DynamicForce, simulate


def check_case(r_delta: float, R_test: float, rise_ps: float) -> None:
    model = DynamicForce(r_delta, quick=True)

    assert np.all(np.isfinite(model.Ftab))
    left, right = model.cold_states()
    assert math.isfinite(left) and math.isfinite(right)
    assert left < 0.0 < right
    assert right - left > 0.1

    out = simulate(
        model,
        r_delta,
        R_test,
        lambda_um=14.0,
        rise_ps=rise_ps,
        tend_ns=0.75,
    )

    assert out["basin"] in {"left", "right"}
    for key in ("x_final", "x_min", "x_max", "Tpeak"):
        assert math.isfinite(float(out[key])), (r_delta, key, out)
    assert float(out["Tpeak"]) >= 0.020

    print(
        f"rDelta={r_delta:.1f}: cold states=({left:.3f},{right:.3f}); "
        f"R={R_test:g} ohm; rise={rise_ps:g} ps; "
        f"basin={out['basin']}; Tpeak={float(out['Tpeak']):.4f} K"
    )


def main() -> None:
    print("Experiment 03 full-dynamic numerical smoke regression")
    check_case(0.8, R_test=200.0, rise_ps=5.0)
    check_case(0.6, R_test=100.0, rise_ps=20.0)
    print("PASS")


if __name__ == "__main__":
    main()
