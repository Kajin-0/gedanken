#!/usr/bin/env python3
"""Nonlinear stationary-bath TWA robustness of the 14-um area-translated lobe.

Inside the retained lumped thermal model, 8 um at A=100 um^2 is thermally
identical to 14 um at

    A = 100*(8/14) = 57.142857... um^2

when the deposition rise time is the same.  This script first checks that
similarity numerically in the full nonlinear TWA/GLE solver, then varies the
14-um rise time around the nominal 20 ps value.

This is important because the crude retained diffusion orientation scale gives
~20.2 ps from the center to the edge of a square A~57.1 um^2 active region.
A viable theoretical design should not rely on an infinitely sharp 20-ps rise.

Results remain semiclassical TWA/GLE screening fractions, not exact quantum
efficiencies.  Spatial heat transport itself is not solved here; rise time is
still a lumped control parameter.
"""

from __future__ import annotations

import argparse

from full_dynamic_rfsquid import DynamicForce
from nonlinear_fdt_twa_screen import run_case
from nonlinear_fdt_twa_convergence import wilson

A_EQ=100.0*8.0/14.0


def print_case(label,o):
    n=int(o['ntraj']); k=int(o['n_right_final'])
    lo,hi=wilson(k,n)
    msg=(
        f'{label}: coldReg=({o["cold_reg_x"]:.4f},{o["cold_reg_u"]:.4f}), '
        f'P_reform={o["P_xright_reform"]:.5f}, '
        f'P_final={o["P_right_final"]:.5f} CI95=[{lo:.5f},{hi:.5f}], '
        f'reform={o["reform_ps"]:.2f} ps, '
        f'xR={o["mean_x_reform"]:+.4f}+-{o["sigma_x_reform"]:.4f}, '
        f'uR={o["mean_u_reform"]:+.4f}+-{o["sigma_u_reform"]:.4f}, '
        f'rho={o["rho_xu_reform"]:+.3f}'
    )
    print(msg)
    print(f'::notice title=Experiment 03 14um area-rise robustness::{msg}')


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument('--ntraj',type=int,default=512)
    ap.add_argument('--dt-ps',type=float,default=0.5)
    ap.add_argument('--seed',type=int,default=112233)
    args=ap.parse_args()

    print('Experiment 03 nonlinear FDT 14-um area/rise robustness')
    print(f'alpha=.60, R=250 ohm, delta=.05, C=215 fF, Aeq={A_EQ:.6f} um^2')
    model=DynamicForce(0.6,quick=False,Tmax=0.95)

    # Exact thermal-similarity regression: same seed/bath history.
    ref=run_case(model,8.0,alpha=.60,R=250.0,ntraj=args.ntraj,
                 dt_ps=args.dt_ps,seed=args.seed,area_um2=100.0,rise_ps=20.0)
    eq=run_case(model,14.0,alpha=.60,R=250.0,ntraj=args.ntraj,
                dt_ps=args.dt_ps,seed=args.seed,area_um2=A_EQ,rise_ps=20.0)
    print_case('8um A100 rise20 reference',ref)
    print_case(f'14um A{A_EQ:.3f} rise20 similarity',eq)
    print(
        'similarity deltas: '
        f'dP={eq["P_right_final"]-ref["P_right_final"]:+.6e}, '
        f'dxR={eq["mean_x_reform"]-ref["mean_x_reform"]:+.6e}, '
        f'duR={eq["mean_u_reform"]-ref["mean_u_reform"]:+.6e}'
    )

    for rise in (15.0,18.0,20.0,21.0,22.0,24.0,26.0,28.0,30.0):
        o=run_case(model,14.0,alpha=.60,R=250.0,ntraj=args.ntraj,
                   dt_ps=args.dt_ps,seed=args.seed,area_um2=A_EQ,rise_ps=rise)
        print_case(f'14um A{A_EQ:.3f} rise{rise:g}',o)

    print('PASS')


if __name__=='__main__':
    main()
