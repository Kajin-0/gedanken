#!/usr/bin/env python3
"""Convergence driver for the nonlinear causal-FDT TWA/GLE screen.

Focus on the two most discriminating energy-density points:
- 8 um equivalent: strongest current candidate;
- 14 um: original marginal operating point.

The driver reports cold-covariance regression and Wilson 95% intervals for the
semiclassical final-basin fraction.  These intervals quantify Monte Carlo error
only.  They do not include TWA/open-system quantum model error, which is known
from the closed-system benchmark to be percent-level in some regimes.
"""

from __future__ import annotations

import argparse
import math

from full_dynamic_rfsquid import DynamicForce
from nonlinear_fdt_twa_screen import run_case


def wilson(k: int,n: int,z: float=1.959963984540054) -> tuple[float,float]:
    if n<=0:
        return math.nan,math.nan
    p=k/n
    z2=z*z
    den=1.0+z2/n
    center=(p+z2/(2*n))/den
    half=z*math.sqrt(p*(1-p)/n+z2/(4*n*n))/den
    return center-half,center+half


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument('--ntraj',type=int,default=1024)
    ap.add_argument('--dt-ps',type=float,default=0.5)
    ap.add_argument('--seed',type=int,default=12345)
    args=ap.parse_args()

    print('Experiment 03 nonlinear FDT TWA convergence')
    print(f'N={args.ntraj}, dt={args.dt_ps} ps, seed={args.seed}; paired histories')
    model=DynamicForce(0.6,quick=False,Tmax=0.95)
    for lam in (8.0,14.0):
        o=run_case(model,lam,ntraj=args.ntraj,dt_ps=args.dt_ps,seed=args.seed)
        n=int(o['ntraj'])
        kr=int(o['n_right_reform']); kf=int(o['n_right_final'])
        lr,ur=wilson(kr,n); lf,uf=wilson(kf,n)
        msg=(
            f'lambda={lam:.1f} um: coldReg(x,u)=({o["cold_reg_x"]:.5f},{o["cold_reg_u"]:.5f}), '
            f'P_reform={o["P_xright_reform"]:.6f} CI95=[{lr:.6f},{ur:.6f}], '
            f'P_final={o["P_right_final"]:.6f} CI95=[{lf:.6f},{uf:.6f}], '
            f'x_reform={o["mean_x_reform"]:+.5f}+-{o["sigma_x_reform"]:.5f}, '
            f'u_reform={o["mean_u_reform"]:+.5f}+-{o["sigma_u_reform"]:.5f}, '
            f'rho={o["rho_xu_reform"]:+.4f}'
        )
        print(msg)
        print(f'::notice title=Experiment 03 nonlinear-TWA convergence::{msg}')
    print('PASS')

if __name__=='__main__':
    main()
