#!/usr/bin/env python3
"""Independent holdout test of the provisional three-gate capture corridor.

Training-set observation (DO NOT treat as theorem): on the 21 valid-stage points
of Actions run 31918267102, all and only the sym-TWA screening points with
P>=.99 obeyed approximately

    chi_E >= 1.65
    Lambda_C >= 0.85
    0.7 <= Lambda_L <= 3.0.

This script freezes those thresholds *before* evaluating a disjoint parameter
grid:

    R      = 60, 110, 200 ohm
    alpha  = .75, 1.05, 1.35
    A      = 83, 89 um^2 at 14 um.

It computes the deterministic controls and an N=1024 symmetrized-FDT TWA screen
for each holdout point, then reports confusion statistics for P>=.99.

This is a falsification test of an empirical organizing hypothesis.  It is not
an exact quantum-efficiency model and must not be converted into a paper claim
without broader validation and theory.
"""
from __future__ import annotations

import math
import numpy as np

from full_dynamic_rfsquid import CASES, DynamicForce, T0
from finite_time_basin_slice import cold_phase_scale
from nonlinear_fdt_twa_screen import run_case
from stage_selectivity_stress import deterministic_features

CHI_MIN=1.65
LC_MIN=.85
LL_MIN=.70
LL_MAX=3.00


def predict(chi,lc,ll,valid):
    return bool(valid and chi>=CHI_MIN and lc>=LC_MIN and LL_MIN<=ll<=LL_MAX)


def main():
    model=DynamicForce(.6,quick=False,Tmax=.95)
    _,C,_=CASES[.6]; _,_,wc=cold_phase_scale(model,.6)
    grid=[(R,a,A) for R in (60.,110.,200.) for a in (.75,1.05,1.35) for A in (83.,89.)]
    rec=[]
    print('Experiment 03 three-gate capture-corridor HOLDOUT')
    print(f'frozen rule: chi>={CHI_MIN:g}, LambdaC>={LC_MIN:g}, {LL_MIN:g}<=LambdaL<={LL_MAX:g}')
    for R,alpha,A in grid:
        d=deterministic_features(model,R,alpha,A)
        chi=(d['Tad']**2-T0**2)/(d['Tf']**2-T0**2)
        g=1/(R*C*wc)
        if d['valid']:
            dsC=2*math.pi*d['cyclesC']; dsL=2*math.pi*d['cyclesL']
            LC=g*d['hC']*dsC; LL=g*d['hL']*dsL
        else:
            LC=LL=math.nan
        pred=predict(chi,LC,LL,d['valid'])
        o=run_case(model,14.,R=R,alpha=alpha,ntraj=1024,dt_ps=.25,seed=939393,
                   area_um2=A,rise_ps=20.)
        P=float(o['P_right_final']); actual=P>=.99
        rec.append((pred,actual,P,R,alpha,A,chi,LC,LL,d['valid'],d.get('reason','')))
        msg=(f'R={R:g} alpha={alpha:.2f} A={A:g}: P={P:.6f} actual99={actual} pred99={pred}; '
             f'chi={chi:.5f} LambdaC={LC:.5f} LambdaL={LL:.5f} '
             f'stage={"valid" if d["valid"] else d["reason"]}')
        print(msg); print(f'::notice title=Experiment 03 corridor holdout::{msg}')

    tp=sum(p and a for p,a,*_ in rec); tn=sum((not p) and (not a) for p,a,*_ in rec)
    fp=sum(p and (not a) for p,a,*_ in rec); fn=sum((not p) and a for p,a,*_ in rec)
    print(f'\nconfusion P>=.99: TP={tp} TN={tn} FP={fp} FN={fn} accuracy={(tp+tn)/len(rec):.4f}')
    if fp:
        print('false positives:')
        for r in rec:
            if r[0] and not r[1]: print(r)
    if fn:
        print('false negatives:')
        for r in rec:
            if (not r[0]) and r[1]: print(r)
    print('PASS')

if __name__=='__main__': main()
