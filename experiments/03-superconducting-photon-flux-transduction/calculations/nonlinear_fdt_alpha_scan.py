#!/usr/bin/env python3
"""Nonlinear causal-FDT TWA screen versus environment cutoff alpha.

The deterministic/tangent scan shows broad favorable energy-density regions for
alpha=omega_D/omega_c roughly 0.5--0.8.  This script performs the stronger
nonlinear stationary-bath TWA/GLE screen across that range.

All wavelength-equivalent cases at a given alpha use the same bath-history seed.
Results are semiclassical screening fractions only; exact open-system quantum
corrections remain outside this model.
"""

from __future__ import annotations

import argparse
import math

from full_dynamic_rfsquid import DynamicForce
from nonlinear_fdt_twa_screen import run_case
from nonlinear_fdt_twa_convergence import wilson


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument('--alpha',type=float,required=True)
    ap.add_argument('--ntraj',type=int,default=512)
    ap.add_argument('--dt-ps',type=float,default=0.5)
    ap.add_argument('--seed',type=int,default=24680)
    args=ap.parse_args()

    print('Experiment 03 nonlinear FDT alpha optimization scan')
    print(f'alpha={args.alpha:.3f}, N={args.ntraj}, dt={args.dt_ps} ps')
    model=DynamicForce(0.6,quick=False,Tmax=0.95)
    for lam in (8.0,9.0,10.0,11.0,12.0,14.0):
        o=run_case(model,lam,alpha=args.alpha,ntraj=args.ntraj,
                   dt_ps=args.dt_ps,seed=args.seed)
        n=int(o['ntraj']); k=int(o['n_right_final'])
        lo,hi=wilson(k,n)
        msg=(
            f'alpha={args.alpha:.3f}, lambda={lam:.1f} um: '
            f'coldReg=({o["cold_reg_x"]:.4f},{o["cold_reg_u"]:.4f}), '
            f'P_reform={o["P_xright_reform"]:.5f}, '
            f'P_final={o["P_right_final"]:.5f} CI95=[{lo:.5f},{hi:.5f}], '
            f'xR={o["mean_x_reform"]:+.4f}+-{o["sigma_x_reform"]:.4f}, '
            f'uR={o["mean_u_reform"]:+.4f}+-{o["sigma_u_reform"]:.4f}, '
            f'rho={o["rho_xu_reform"]:+.3f}'
        )
        print(msg)
        print(f'::notice title=Experiment 03 nonlinear alpha scan::{msg}')
    print('PASS')

if __name__=='__main__':
    main()
