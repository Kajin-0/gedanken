#!/usr/bin/env python3
"""Coarse same-memory-window control for the direct-port harmonic TEMPO pilot.

This is deliberately not an acceptance calculation.  It reuses the exact same
physics/mapping as `tempo_harmonic_direct_port_pilot.py` but coarsens only the
time grid:

    dt   = 0.40 tau
    tcut = 8.0 tau
    tend = 24.0 tau
    epsrel = 1e-7

The purpose is to obtain an early gross mapping/relaxation sanity check while
the finer dt=0.20 tensor contraction runs.  No Gate-C.1 promotion may be based
on this control.
"""
import tempo_harmonic_direct_port_pilot as pilot

pilot.DT = 0.40
pilot.TCUT = 8.0
pilot.TEND = 24.0
pilot.EPSREL = 1e-7

if __name__ == '__main__':
    pilot.main()
