#!/usr/bin/env python3
"""Fast exploratory direct-TEMPO memory discriminator for dim=2.

This deliberately loosens only tensor tolerance relative to the strict matrix:

    dt=.4, tend=64, epsrel=1e-8

and compares tcut=8 versus tcut=20.  It cannot pass the frozen TEMPO gate.
The completed epsrel study at dt=.2/tcut=8 showed that loosening epsrel from
1e-10 to 1e-8 changes the mapped state far less than the current ~1e-3 memory
bias, so this pair is only used to test whether long memory produces the
predicted order-of-magnitude movement toward the converged HEOM reference.
"""
from __future__ import annotations

import argparse
import tempo_vs_heom_dim2_refine as refine

CASES={
    'f8': dict(dt=.4,tcut=8.0,tend=64.0,eps=1e-8),
    'f20':dict(dt=.4,tcut=20.0,tend=64.0,eps=1e-8),
}

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--case',choices=sorted(CASES),required=True)
    args=ap.parse_args(); refine.CASES[args.case]=CASES[args.case]; refine.main(args.case)
