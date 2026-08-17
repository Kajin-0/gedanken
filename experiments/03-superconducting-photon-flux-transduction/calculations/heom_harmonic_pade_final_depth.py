#!/usr/bin/env python3
"""Final brute-force hierarchy sign-convergence probes for Gate B.

The deep Padé HEOM sequence has reduced the harmonic reduced-state negativity
from O(1e-4) at depth 3 to O(1e-7) at depth 7 while exact-FDT second moments
converge to sub-ppm accuracy.  This script runs the last predeclared brute-force
hierarchy matrix:

* Npade=4, depth 8 and 9: continuation of the economical six-exponential bath;
* Npade=5, depth 7: independent thermal-pole-order control at the same depth.

No depth >9 is authorized by this script.  If these points do not establish a
controlled sign/zero trend, Gate B remains open and the next method must be an
independent physical embedding/closure rather than further raw hierarchy depth.
"""
from __future__ import annotations

import argparse
import heom_harmonic_pade_depth as base

CASES = {
    "p4d8": dict(dim=8, npade=4, depth=8),
    "p4d9": dict(dim=8, npade=4, depth=9),
    "p5d7": dict(dim=8, npade=5, depth=7),
}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--case',choices=sorted(CASES),required=True)
    args=ap.parse_args()
    base.CASES[args.case]=CASES[args.case]
    base.run_case(args.case)

if __name__=='__main__':
    main()
