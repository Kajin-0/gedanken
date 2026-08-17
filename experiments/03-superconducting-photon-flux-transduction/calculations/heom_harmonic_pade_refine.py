#!/usr/bin/env python3
"""Refinement probes for the Experiment-03 harmonic HEOM Gate B.

The first deep Padé sweep drove the finite-tier reduced-state negativity from
~1e-4 at depth 3 to ~7e-7 at depth 5 while preserving ~1e-5 exact-FDT width
accuracy.  At that scale three independent numerical limits must be separated:

1. hierarchy depth,
2. oscillator Hilbert dimension,
3. ODE integration tolerance.

This wrapper changes one axis at a time while reusing the independently
validated direct-port Padé bath and harmonic model in
`heom_harmonic_pade_depth.py`.
"""
from __future__ import annotations

import argparse
import heom_harmonic_pade_depth as base


CASES = {
    # Continue hierarchy depth with Npade=4; 6 exponents -> 1716 ADOs at d7.
    "p4d7": dict(dim=8, npade=4, depth=7),
    # Independent higher Padé order at one deeper tier; also 1716 ADOs.
    "p5d6": dict(dim=8, npade=5, depth=6),
    # Hilbert-basis convergence at the depth-5 physicality frontier.
    "p5d5_dim10": dict(dim=10, npade=5, depth=5),
    # Same physical point as p5d5 but with 100x tighter ODE tolerances.
    "p5d5_tight": dict(dim=8, npade=5, depth=5),
}


_BaseSolver = base.HEOMSolver


class TightHEOMSolver(_BaseSolver):
    def __init__(self, *args, **kwargs):
        opts = dict(kwargs.get("options") or {})
        opts["rtol"] = 2e-9
        opts["atol"] = 2e-11
        opts["nsteps"] = 500000
        kwargs["options"] = opts
        super().__init__(*args, **kwargs)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--case", choices=sorted(CASES), required=True)
    args = ap.parse_args()
    base.CASES[args.case] = CASES[args.case]
    if args.case.endswith("_tight"):
        base.HEOMSolver = TightHEOMSolver
    base.run_case(args.case)


if __name__ == "__main__":
    main()
