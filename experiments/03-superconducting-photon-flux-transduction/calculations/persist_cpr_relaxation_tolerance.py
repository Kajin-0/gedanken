#!/usr/bin/env python3
"""Persist the finite-CPR-response tolerance curve for Experiment 03.

Uses the current external candidate R=80 ohm, alpha=.90, delta=.05, C=215 fF,
8-um/A100-equivalent thermal trajectory.  The phenomenological first-order CPR
lag remains a sensitivity model, not microscopic ABS kinetics.
"""
from __future__ import annotations
from pathlib import Path
from full_dynamic_rfsquid import DynamicForce
from cpr_relaxation_tolerance import run
from nonlinear_fdt_twa_convergence import wilson

OUT=Path('../RESULTS_CPR_RELAXATION_TOLERANCE_2026-08-15.md')


def main():
    model=DynamicForce(.6,quick=False,Tmax=.95)
    lines=[
        '# Experiment 03 — Finite CPR-Response Tolerance — 2026-08-15','',
        'R=80 ohm, alpha=.90, delta=.05, C=215 fF; stationary external-bath TWA/GLE.','',
        'The delayed-CPR law is phenomenological and omits the additional causal/FDT fluctuations a real delayed susceptibility may require.','',
        '```text'
    ]
    for tau in (0.,.5,1.,2.,3.,5.,7.5,10.,15.,20.,30.,40.,50.,75.,100.,150.):
        o=run(model,tau,ntraj=2048,dt_ps=.25,seed=454545)
        lo,hi=wilson(o['kf'],o['n'])
        lines.append(
            f'tauCPR={tau:g} ps; coldReg=({o["crx"]:.6f},{o["cru"]:.6f}); '
            f'P_reform={o["Pr"]:.8f}; P_final={o["Pf"]:.8f}; '
            f'CI95=[{lo:.8f},{hi:.8f}]; fail={o["n"]-o["kf"]}; '
            f'xR={o["mx"]:+.6f}+-{o["sx"]:.6f}; '
            f'uR={o["mu"]:+.6f}+-{o["su"]:.6f}; rho={o["rho"]:+.6f}'
        )
    lines += ['```','',
              'Failure at small tauCPR is a strong feasibility warning. Survival does not prove microscopic occupation kinetics because the lag model itself adds no internal FDT bath.']
    OUT.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(f'wrote {OUT}')

if __name__=='__main__':
    main()
