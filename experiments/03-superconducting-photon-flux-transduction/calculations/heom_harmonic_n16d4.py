#!/usr/bin/env python3
"""N_Mats=16, depth=4 convergence gate for Experiment 03 harmonic HEOM.

Gate B has established sub-1e-4 observable covariance agreement at N16,d3,
but the reduced state retains a ~1.1e-4 negative eigenvalue.  This calculation
raises hierarchy depth one step without changing the validated direct-port bath
mapping or counterterm.  Two Hilbert dimensions are run independently in CI to
distinguish hierarchy convergence from system-basis effects.
"""
from __future__ import annotations

import argparse
import heom_harmonic_port_probe as probe


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dim", type=int, choices=(8, 10), required=True)
    args = ap.parse_args()
    name = f"dim{args.dim}_n16d4"
    probe.CASES[name] = dict(dim=args.dim, nmats=16, depth=4, counterterm=True)
    probe.run_case(name)


if __name__ == "__main__":
    main()
