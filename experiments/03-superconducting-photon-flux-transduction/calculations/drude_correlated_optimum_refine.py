#!/usr/bin/env python3
"""Refine the causal Drude capture optimum near R0~360 ohm, d~3-4.

Stage 1: local 20-point scan with one scrambled Sobol set, N=2048.
Stage 2: take the best two points and evaluate four independent scrambles at
N=4096 for dt=0.2 ps and dt=0.1 ps.

Pulse-time FDT noise remains absent.  This only refines the correlated cold-state
+ causal-propagator optimum.
"""
from __future__ import annotations
import numpy as np

from full_dynamic_rfsquid import DynamicForce
from drude_correlated_capture import initial_samples, propagate_vectorized, cold_energy_classifier


def pcase(model,R,d,m,seed,dt):
    x,v,j,_=initial_samples(model,R,d,m,seed)
    xf,vf,jf,_=propagate_vectorized(model,x,v,j,R0=R,d=d,dt_ps=dt,tend_ns=0.8)
    trapped,_,_=cold_energy_classifier(model,R,d,xf,vf,jf)
    return float(np.mean(trapped))


def main():
    model=DynamicForce(0.6,quick=False)
    rows=[]
    for d in (2.5,3.0,3.5,4.0):
        for R in (320.,340.,360.,380.,400.):
            p=pcase(model,R,d,11,37,0.2)
            rows.append((p,R,d))
            msg=f'local N=2048 R0={R:g}ohm d={d:g}: Ptrap={p:.6f}'
            print(msg); print(f'::notice title=Experiment 03 Drude local refine::{msg}')
    rows.sort(reverse=True)
    print('\nLocal top points:')
    for row in rows[:8]: print(row)

    # Avoid refining two numerically adjacent points that are effectively the
    # same grid location in d; simply take the top two distinct tuples.
    tops=rows[:2]
    seeds=(7,23,61,101)
    for _,R,d in tops:
        for dt in (0.2,0.1):
            vals=[]
            for seed in seeds:
                p=pcase(model,R,d,12,seed,dt)
                vals.append(p)
                msg=f'R0={R:g}ohm d={d:g} dt={dt:g}ps seed={seed} N=4096 Ptrap={p:.6f}'
                print(msg); print(f'::notice title=Experiment 03 Drude optimum::{msg}')
            a=np.asarray(vals)
            summary=(f'R0={R:g}ohm d={d:g} dt={dt:g}ps: '
                     f'mean={a.mean():.6f} std={a.std(ddof=1):.6f} '
                     f'min={a.min():.6f} max={a.max():.6f}')
            print(summary); print(f'::notice title=Experiment 03 Drude optimum summary::{summary}')
    print('PASS')

if __name__=='__main__': main()
