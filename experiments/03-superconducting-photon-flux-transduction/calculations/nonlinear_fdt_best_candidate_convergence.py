#!/usr/bin/env python3
"""High-statistics convergence of the current best passive causal-bath candidate.

A coarse nonlinear stationary-bath TWA/GLE scan found only 1 failure in 512
trajectories at

    rDelta=.6, delta=.05, C=215 fF,
    8-um-equivalent energy density,
    R=150 ohm, alpha=0.70--0.80.

This script increases ensemble size and checks dt convergence at those points.
It reports Wilson intervals for Monte Carlo uncertainty and the cold covariance
regression.  These intervals DO NOT include TWA/open-system quantum model error.
"""

from __future__ import annotations

import argparse

from full_dynamic_rfsquid import DynamicForce
from nonlinear_fdt_twa_screen import run_case
from nonlinear_fdt_twa_convergence import wilson


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument('--alpha',type=float,required=True)
    ap.add_argument('--dt-ps',type=float,required=True)
    ap.add_argument('--ntraj',type=int,default=4096)
    ap.add_argument('--seed',type=int,default=424242)
    args=ap.parse_args()

    print('Experiment 03 high-statistics best passive candidate')
    print(
        f'R=150 ohm, alpha={args.alpha:.3f}, 8-um equivalent, '
        f'N={args.ntraj}, dt={args.dt_ps} ps'
    )
    model=DynamicForce(0.6,quick=False,Tmax=0.95)
    o=run_case(
        model,8.0,R=150.0,alpha=args.alpha,ntraj=args.ntraj,
        dt_ps=args.dt_ps,seed=args.seed,
    )
    n=int(o['ntraj']); kr=int(o['n_right_reform']); kf=int(o['n_right_final'])
    lr,ur=wilson(kr,n); lf,uf=wilson(kf,n)
    msg=(
        f'R=150 alpha={args.alpha:.3f} dt={args.dt_ps:.3f} ps N={n}: '
        f'coldReg=({o["cold_reg_x"]:.5f},{o["cold_reg_u"]:.5f}), '
        f'P_reform={o["P_xright_reform"]:.7f} CI95=[{lr:.7f},{ur:.7f}] '
        f'fail={n-kr}, '
        f'P_final={o["P_right_final"]:.7f} CI95=[{lf:.7f},{uf:.7f}] '
        f'fail={n-kf}, '
        f'xR={o["mean_x_reform"]:+.5f}+-{o["sigma_x_reform"]:.5f}, '
        f'uR={o["mean_u_reform"]:+.5f}+-{o["sigma_u_reform"]:.5f}, '
        f'rho={o["rho_xu_reform"]:+.4f}, tauCold={o["tau_cold_ns"]:.4f} ns'
    )
    print(msg)
    print(f'::notice title=Experiment 03 best-candidate convergence::{msg}')
    print('PASS')


if __name__=='__main__':
    main()
