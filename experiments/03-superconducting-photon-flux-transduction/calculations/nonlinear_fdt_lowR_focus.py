#!/usr/bin/env python3
"""Focused nonlinear stationary-bath scan below R=150 ohm.

The coarse causal R-alpha screen found near-unity TWA/GLE capture at R=150 ohm
and alpha~0.7--0.8.  This script determines whether the optimum extends to
still stronger damping or turns over as launch becomes overdamped/noise grows.

Results are semiclassical stationary-bath TWA/GLE screening fractions only.
"""

from __future__ import annotations

import argparse

from full_dynamic_rfsquid import DynamicForce
from nonlinear_fdt_twa_screen import run_case
from nonlinear_fdt_twa_convergence import wilson


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument('--R',type=float,required=True)
    ap.add_argument('--ntraj',type=int,default=1024)
    ap.add_argument('--dt-ps',type=float,default=0.5)
    ap.add_argument('--seed',type=int,default=515151)
    args=ap.parse_args()

    print('Experiment 03 focused low-R nonlinear FDT scan')
    print(f'R={args.R:g} ohm, 8-um equivalent, delta=.05, C=215 fF')
    model=DynamicForce(0.6,quick=False,Tmax=0.95)
    for alpha in (0.50,0.60,0.65,0.70,0.75,0.80,0.90,1.00):
        o=run_case(model,8.0,R=args.R,alpha=alpha,ntraj=args.ntraj,
                   dt_ps=args.dt_ps,seed=args.seed)
        n=int(o['ntraj']); k=int(o['n_right_final'])
        lo,hi=wilson(k,n)
        msg=(
            f'R={args.R:g}, alpha={alpha:.2f}: '
            f'coldReg=({o["cold_reg_x"]:.4f},{o["cold_reg_u"]:.4f}), '
            f'P_reform={o["P_xright_reform"]:.6f}, '
            f'P_final={o["P_right_final"]:.6f} CI95=[{lo:.6f},{hi:.6f}], '
            f'fail={n-k}, tauCold={o["tau_cold_ns"]:.4f} ns, '
            f'xR={o["mean_x_reform"]:+.4f}+-{o["sigma_x_reform"]:.4f}, '
            f'uR={o["mean_u_reform"]:+.4f}+-{o["sigma_u_reform"]:.4f}'
        )
        print(msg)
        print(f'::notice title=Experiment 03 focused low-R::{msg}')
    print('PASS')


if __name__=='__main__':
    main()
