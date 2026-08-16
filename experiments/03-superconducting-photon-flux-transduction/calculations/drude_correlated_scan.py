#!/usr/bin/env python3
"""Coarse causal-environment scan using the correlated cold Drude state.

This is a scouting optimization only.  It searches (R0, omega_D/omega_c) after
both causal propagation and the correlated cold (x,xdot,j) Gaussian are included.
Pulse-time bath noise remains absent.
"""
from __future__ import annotations
import numpy as np

from full_dynamic_rfsquid import DynamicForce
from drude_correlated_capture import (
    initial_samples, propagate_vectorized, cold_energy_classifier,
)


def main():
    model=DynamicForce(0.6,quick=False)
    Rs=(140.,180.,220.,260.,300.,360.,440.,550.)
    ds=(3.,4.,5.,7.,10.)
    m=10  # 1024 Sobol states per point
    seed=37
    rows=[]
    for d in ds:
        for R in Rs:
            x,v,j,_=initial_samples(model,R,d,m,seed)
            xf,vf,jf,Tf=propagate_vectorized(
                model,x,v,j,R0=R,d=d,dt_ps=0.2,tend_ns=0.8,
            )
            trapped,right,E=cold_energy_classifier(model,R,d,xf,vf,jf)
            p=float(np.mean(trapped)); pr=float(np.mean(right))
            rows.append((p,R,d,pr))
            msg=(f'R0={R:g}ohm d={d:g}: N={2**m} Ptrap={p:.6f} '
                 f'Pright={pr:.6f} Tfinal={Tf:.5f}K')
            print(msg)
            print(f'::notice title=Experiment 03 correlated Drude scan::{msg}')
    rows.sort(reverse=True)
    print('\nTop causal-environment scouting points:')
    for p,R,d,pr in rows[:10]:
        print(f'Ptrap={p:.6f} R0={R:g}ohm d={d:g} Pright={pr:.6f}')
    print('PASS')

if __name__=='__main__': main()
