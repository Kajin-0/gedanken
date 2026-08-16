#!/usr/bin/env python3
"""Resolve the remaining Experiment-03 harmonic HEOM Gate-B truncation issue.

The dim=8->10->12 sweep at N_Mats=8, depth=3 did not remove the small
negative reduced-density eigenvalue; dim=12 instead exposed an unstable
high-energy sector.  This script therefore holds a well-converged dim=10
system basis fixed and increases the two HEOM/bath truncations independently.

Cases:
  n8d4   : hierarchy-depth test relative to the accepted n8d3 observable result
  n16d2  : Matsubara-tail test at shallow hierarchy
  n16d3  : combined higher-Matsubara test at the working hierarchy

No detector efficiency is computed here.
"""
from __future__ import annotations

import argparse
import heom_harmonic_port_probe as probe

CASES = {
    "n8d4":  dict(dim=10, nmats=8,  depth=4, counterterm=True),
    "n16d2": dict(dim=10, nmats=16, depth=2, counterterm=True),
    "n16d3": dict(dim=10, nmats=16, depth=3, counterterm=True),
}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--case", choices=sorted(CASES), required=True)
    args = ap.parse_args()
    name = args.case
    probe.CASES[name] = CASES[name]
    probe.run_case(name)


if __name__ == "__main__":
    main()
