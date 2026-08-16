#!/usr/bin/env python3
"""Retry the N_Mats=16, depth=4 harmonic HEOM gate with a larger ODE step budget.

The first dim=8 depth-4 run failed only because QuTiP/ZVODE exhausted its
internal default nsteps allowance after constructing the 7315-ADO hierarchy.
This wrapper changes no physics and no convergence parameters; it only raises
`nsteps` in the same BDF integrator, exactly as requested by the integrator
exception.
"""
from __future__ import annotations

import argparse
import heom_harmonic_port_probe as probe

_Base = probe.HEOMSolver

class HEOMSolverMoreSteps(_Base):
    def __init__(self, *args, **kwargs):
        opts = dict(kwargs.get('options') or {})
        opts['nsteps'] = 200000
        kwargs['options'] = opts
        super().__init__(*args, **kwargs)

probe.HEOMSolver = HEOMSolverMoreSteps


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--dim',type=int,choices=(8,10),required=True)
    args=ap.parse_args()
    name=f'dim{args.dim}_n16d4_retry'
    probe.CASES[name]=dict(dim=args.dim,nmats=16,depth=4,counterterm=True)
    probe.run_case(name)

if __name__=='__main__': main()
