#!/usr/bin/env python3
"""Persist hot intrinsic-admittance tolerance for the R80 candidate.

This wraps `hot_intrinsic_admittance_tolerance.py` at dt=.25 ps and N=2048 and
writes the peak-conductance tolerance table into repository history.
"""
from __future__ import annotations
import math
from pathlib import Path
from full_dynamic_rfsquid import DynamicForce
from hot_intrinsic_admittance_tolerance import run_case
from nonlinear_fdt_twa_convergence import wilson

OUT=Path('../RESULTS_HOT_INTRINSIC_ADMITTANCE_TOLERANCE_2026-08-15.md')


def main():
    model=DynamicForce(.6,quick=False,Tmax=.95)
    lines=[
        '# Experiment 03 — Hot Intrinsic-Admittance Tolerance — 2026-08-15','',
        'Rext=80 ohm, alpha=.90, delta=.05, C=215 fF, 8-um/A100-equivalent thermal trajectory.',
        'Pulse-activated intrinsic conductance uses thermal-only classical FDT noise; this is a lower-bound/sensitivity screen, not microscopic Y_JJ.','',
        '```text'
    ]
    for Rhot in (math.inf,50000.,20000.,10000.,5000.,3000.,2000.,1500.,1000.,750.,500.,350.,250.,150.,100.):
        Gpk=0.0 if math.isinf(Rhot) else 1.0/Rhot
        o=run_case(model,Gpk,ntraj=2048,dt_ps=.25,seed=777777)
        lo,hi=wilson(o['kf'],o['n'])
        label='inf' if math.isinf(Rhot) else f'{Rhot:g}'
        lines.append(
            f'Rhot_peak={label} ohm; Gpk={Gpk*1e6:.6f} uS; '
            f'coldReg=({o["cold_reg_x"]:.6f},{o["cold_reg_u"]:.6f}); '
            f'P_reform={o["P_reform"]:.8f}; P_final={o["P_final"]:.8f}; '
            f'CI95=[{lo:.8f},{hi:.8f}]; fail={o["n"]-o["kf"]}; '
            f'xR={o["mean_xr"]:+.6f}+-{o["sig_xr"]:.6f}; '
            f'uR={o["mean_ur"]:+.6f}+-{o["sig_ur"]:.6f}; rho={o["rho"]:+.6f}'
        )
    lines += ['```','',
              'Any microscopic promotion must include frequency-, phase- and temperature-dependent Y_JJ and its quantum FDT spectrum.']
    OUT.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(f'wrote {OUT}')

if __name__=='__main__':
    main()
