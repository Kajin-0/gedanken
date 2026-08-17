#!/usr/bin/env python3
"""Matched coarse-grid direct-TEMPO memory-scaling matrix for dim=2.

All cases hold

    dt=.4, tend=64, epsrel=1e-10

fixed and vary only the memory cutoff:

    tcut=8, 12, 20.

This is an exploratory memory-scaling diagnostic.  It cannot satisfy the frozen
TEMPO timestep acceptance criterion.  Its purpose is to test whether enlarging
the memory window moves the late state toward the independently converged HEOM
stationary reference on a computationally cheaper common time grid.
"""
from __future__ import annotations

import argparse
import tempo_vs_heom_dim2_refine as refine

CASES={
    'c8': dict(dt=.4,tcut=8.0,tend=64.0,eps=1e-10),
    'c12':dict(dt=.4,tcut=12.0,tend=64.0,eps=1e-10),
    'c20':dict(dt=.4,tcut=20.0,tend=64.0,eps=1e-10),
}

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--case',choices=sorted(CASES),required=True)
    args=ap.parse_args()
    refine.CASES[args.case]=CASES[args.case]
    refine.main(args.case)
