#!/usr/bin/env python3
"""Full-history direct-TEMPO transient control to tau=16 for dim=2.

This changes only the memory window relative to the existing `tol32` mapping:

    dt=.2, epsrel=1e-10, tend=16, tcut=16.

Because tcut=tend, no bath influence coefficient inside the simulated interval
is discarded by a finite-memory cutoff.  The endpoint can therefore be compared
to the already logged tcut=8 state at tau=16 to measure finite-memory
transient distortion directly.  It is not an equilibrium or Gate-C test.
"""
import tempo_vs_heom_dim2_refine as refine

refine.CASES['full16']=dict(dt=.2,tcut=16.0,tend=16.0,eps=1e-10)

if __name__=='__main__':
    refine.main('full16')
