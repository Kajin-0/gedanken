#!/usr/bin/env python3
"""Persist the current R=80 ohm, alpha=.90 14-um candidate validation.

This is an auditability wrapper around the established nonlinear stationary-bath
TWA/GLE solver.  It writes one repository markdown snapshot containing:

- high-statistics 8-um/A100 reference;
- exact reduced-model 14-um/A57.142857 similarity point;
- 14-um rise-time robustness.

The numbers remain semiclassical TWA/GLE screening fractions, not exact quantum
capture efficiencies.
"""
from __future__ import annotations
from pathlib import Path
from full_dynamic_rfsquid import DynamicForce
from nonlinear_fdt_twa_screen import run_case
from nonlinear_fdt_twa_convergence import wilson

OUT=Path('../RESULTS_R80_14UM_CANDIDATE_2026-08-15.md')
A_EQ=100.0*8.0/14.0


def row(label,o):
    n=int(o['ntraj']); k=int(o['n_right_final'])
    lo,hi=wilson(k,n)
    return (
        f'{label}: N={n}; coldReg=({o["cold_reg_x"]:.6f},{o["cold_reg_u"]:.6f}); '
        f'P_reform={o["P_xright_reform"]:.8f}; '
        f'P_final={o["P_right_final"]:.8f}; CI95=[{lo:.8f},{hi:.8f}]; '
        f'fail={n-k}; reform={o["reform_ps"]:.4f} ps; '
        f'xR={o["mean_x_reform"]:+.6f}+-{o["sigma_x_reform"]:.6f}; '
        f'uR={o["mean_u_reform"]:+.6f}+-{o["sigma_u_reform"]:.6f}; '
        f'rho={o["rho_xu_reform"]:+.6f}; tauCold={o["tau_cold_ns"]:.6f} ns'
    )


def main():
    model=DynamicForce(.6,quick=False,Tmax=.95)
    R=80.0; alpha=.90; dt=.25; seed=606060
    ref=run_case(model,8.0,R=R,alpha=alpha,ntraj=4096,dt_ps=dt,seed=seed,
                 area_um2=100.0,rise_ps=20.0)
    eq=run_case(model,14.0,R=R,alpha=alpha,ntraj=4096,dt_ps=dt,seed=seed,
                area_um2=A_EQ,rise_ps=20.0)
    lines=[
        '# Experiment 03 — R80 / alpha=.90 14-um Candidate — 2026-08-15','',
        'Stationary external-bath symmetrized-FDT TWA/GLE screen. **Not exact quantum efficiency.**','',
        '```text',
        row('8um A100 rise20 reference',ref),
        row(f'14um A{A_EQ:.8f} rise20 similarity',eq),
        f'similarity deltaP={eq["P_right_final"]-ref["P_right_final"]:+.12e}; '
        f'delta_xR={eq["mean_x_reform"]-ref["mean_x_reform"]:+.12e}; '
        f'delta_uR={eq["mean_u_reform"]-ref["mean_u_reform"]:+.12e}',
    ]
    for rise in (15.,18.,20.,21.,22.,24.,26.,28.,30.):
        o=run_case(model,14.0,R=R,alpha=alpha,ntraj=2048,dt_ps=dt,seed=seed,
                   area_um2=A_EQ,rise_ps=rise)
        lines.append(row(f'14um A{A_EQ:.8f} rise{rise:g}',o))
    lines += ['```','',
              'Thermal area/wavelength similarity is exact only inside the retained reduced calorimetric model.',
              'Rise-time robustness remains lumped; spatial heat transport is not solved here.']
    OUT.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(f'wrote {OUT}')

if __name__=='__main__':
    main()
