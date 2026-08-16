#!/usr/bin/env python3
"""Regression-style falsification of proposed reduced capture controls.

This script uses the frozen sym-FDT/TWA screening fractions from workflow
`Experiment 03 stage-selectivity stress` (run 31918267102) and recomputes the
deterministic dimensionless controls for exactly the same 27 points.

The goal is NOT to fit an empirical device model from 27 correlated samples.
The goal is to falsify overly simple proposed organizing variables and identify
which variables deserve a larger independent scan.

Candidate controls:

    chi_E      = (Tad^2-T0^2)/(Tf^2-T0^2)
    Delta_s_C  = omega_c (t_reform-t_cross)
    A_select   = H_eff,L^2/H_eff,C^2
    Lambda_C   = g H_eff,C^2 Delta_s_C
    g          = 1/(R C omega_c)

Only points with deterministic crossing before reformation have these stage
variables.  Points with cross_after_reform/no_cross are retained as explicit
mechanism failures but excluded from rank correlations involving undefined
stage variables.

All P values are symmetrized-FDT TWA screening fractions, not exact quantum
efficiencies.  Nominal p-values are descriptive only because the grid shares
noise seeds and is not an independent random sample from a population.
"""
from __future__ import annotations

import math
import numpy as np
from scipy.stats import spearmanr

from full_dynamic_rfsquid import CASES, DynamicForce, T0
from finite_time_basin_slice import cold_phase_scale
from stage_selectivity_stress import deterministic_features

# Frozen results from GitHub Actions run 31918267102.
P_TABLE = {
(40,.6,80):.970703,(40,.6,86):.914062,(40,.6,92):.821289,
(40,.9,80):.980469,(40,.9,86):.921875,(40,.9,92):.829102,
(40,1.2,80):.976562,(40,1.2,86):.940430,(40,1.2,92):.853516,
(80,.6,80):1.000000,(80,.6,86):.994141,(80,.6,92):.961914,
(80,.9,80):.999023,(80,.9,86):.991211,(80,.9,92):.965820,
(80,1.2,80):.999023,(80,1.2,86):.991211,(80,1.2,92):.967773,
(150,.6,80):.967773,(150,.6,86):.969727,(150,.6,92):.964844,
(150,.9,80):.986328,(150,.9,86):.986328,(150,.9,92):.979492,
(150,1.2,80):.992188,(150,1.2,86):.993164,(150,1.2,92):.985352,
}


def main():
    model=DynamicForce(.6,quick=False,Tmax=.95)
    _,C,_=CASES[.6]
    _,_,wc=cold_phase_scale(model,.6)
    rows=[]
    invalid=[]
    print('Experiment 03 dimensionless capture-control regression')
    for (R,alpha,A),P in P_TABLE.items():
        d=deterministic_features(model,float(R),float(alpha),float(A))
        chi=(d['Tad']**2-T0**2)/(d['Tf']**2-T0**2)
        g=1/(R*C*wc)
        if not d['valid']:
            invalid.append((R,alpha,A,P,d['reason'],chi,g))
            print(f'INVALID R={R} alpha={alpha:.2f} A={A}: P={P:.6f} reason={d["reason"]} chiE={chi:.5f} g={g:.5f}')
            continue
        ds=2*math.pi*d['cyclesC']
        lamC=g*d['hC']*ds
        lamL=g*d['hL']*(2*math.pi*d['cyclesL'])
        rows.append({
            'R':R,'alpha':alpha,'A':A,'P':P,'fail':1-P,'chi':chi,'g':g,
            'dsC':ds,'cyclesC':d['cyclesC'],'Aselect':d['Aselect'],
            'LambdaC':lamC,'LambdaL':lamL,'fpre':d['fpre'],
            'ratioLambda':lamL/lamC if lamC>0 else math.nan,
        })
        print(f'VALID R={R} alpha={alpha:.2f} A={A}: P={P:.6f} chiE={chi:.5f} g={g:.5f} '
              f'cyclesC={d["cyclesC"]:.5f} Aselect={d["Aselect"]:.5f} '
              f'LambdaC={lamC:.5f} LambdaL={lamL:.5f}')

    names=['chi','g','cyclesC','Aselect','LambdaC','LambdaL','ratioLambda','fpre']
    print('\nRank correlations with failure on valid-stage points:')
    for name in names:
        x=np.array([r[name] for r in rows]); y=np.array([r['fail'] for r in rows])
        rho,p=spearmanr(x,y)
        print(f'{name:>12s}: rho={rho:+.5f}, nominal_p={p:.4g}')

    # Adversarial threshold checks.  These test whether simple one-variable rules
    # can separate high-P and low-P points on this grid.
    print('\nCounterexamples to simple proposed rules:')
    for rule, pred in [
        ('Aselect<1', lambda r:r['Aselect']<1),
        ('LambdaC>1',lambda r:r['LambdaC']>1),
        ('chiE>1.65',lambda r:r['chi']>1.65),
        ('LambdaC>1 and Aselect<1',lambda r:r['LambdaC']>1 and r['Aselect']<1),
    ]:
        yes=[r for r in rows if pred(r)]
        if yes:
            worst=min(yes,key=lambda r:r['P'])
            print(f'{rule}: n={len(yes)}, worst P={worst["P"]:.6f} at R={worst["R"]},alpha={worst["alpha"]},A={worst["A"]}')
        else:
            print(f'{rule}: no points')

    # Pareto-like high-fidelity envelope: report all valid points P>=.99 and their
    # control ranges rather than forcing a fitted boundary.
    hi=[r for r in rows if r['P']>=.99]
    print(f'\nvalid P>=.99 points: {len(hi)}/{len(rows)}')
    if hi:
        for name in ['chi','g','cyclesC','Aselect','LambdaC']:
            vals=[r[name] for r in hi]
            print(f'  {name}: [{min(vals):.5f}, {max(vals):.5f}]')
    print(f'invalid-stage points: {len(invalid)}')
    print('PASS')

if __name__=='__main__': main()
