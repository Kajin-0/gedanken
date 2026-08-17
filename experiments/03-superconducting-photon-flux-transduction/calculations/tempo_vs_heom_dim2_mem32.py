#!/usr/bin/env python3
"""Memory-only direct-TEMPO control for the dim=2 mapping problem.

Compares directly to the completed `tol32` case by changing only
`tcut: 8 -> 12` while keeping

    dt=.2, tend=32, epsrel=1e-10.

This isolates finite-memory bias from extra equilibration time.  The underlying
finite system, bath correlation, counterterm and HEOM comparison state are
unchanged.
"""
import tempo_vs_heom_dim2_refine as refine

refine.CASES['mem32']=dict(dt=.2,tcut=12.0,tend=32.0,eps=1e-10)

if __name__=='__main__':
    refine.main('mem32')
