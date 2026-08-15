#!/usr/bin/env python3
"""Nonlinear stationary-bath TWA/GLE scan in causal R and cutoff alpha.

The strongest current energy-density lobe is the 8-um equivalent at the
historical delta=.05.  Previous nonlinear screens fixed R=250 ohm, inherited
from the scalar-R probability study.  In the causal environment R simultaneously
sets low-frequency damping and bath spectral density, so the old optimum need
not survive.

This script scans R and alpha at fixed rDelta=.6, delta=.05, C=215 fF, 8-um
equivalent thermal trajectory.  Results are semiclassical TWA/GLE screening
fractions, not exact quantum efficiencies.  Dissipative MQT is not recomputed;
write optimization must later be intersected with dark stability under the same
Y(omega).
"""

from __future__ import annotations

import argparse

from full_dynamic_rfsquid import DynamicForce
from nonlinear_fdt_twa_screen import run_case
from nonlinear_fdt_twa_convergence import wilson


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument('--R',type=float,required=True)
    ap.add_argument('--ntraj',type=int,default=512)
    ap.add_argument('--dt-ps',type=float,default=0.5)
    ap.add_argument('--seed',type=int,default=86420)
    args=ap.parse_args()

    print('Experiment 03 nonlinear causal R-alpha scan')
    print(f'R={args.R:g} ohm, rDelta=.6, delta=.05, C=215 fF, 8-um equivalent')
    model=DynamicForce(0.6,quick=False,Tmax=0.95)
    for alpha in (0.35,0.45,0.50,0.55,0.60,0.65,0.70,0.80,1.00):
        o=run_case(model,8.0,alpha=alpha,R=args.R,ntraj=args.ntraj,
                   dt_ps=args.dt_ps,seed=args.seed)
        n=int(o['ntraj']); k=int(o['n_right_final'])
        lo,hi=wilson(k,n)
        msg=(
            f'R={args.R:g}, alpha={alpha:.2f}: '
            f'coldReg=({o["cold_reg_x"]:.4f},{o["cold_reg_u"]:.4f}), '
            f'P_reform={o["P_xright_reform"]:.5f}, '
            f'P_final={o["P_right_final"]:.5f} CI95=[{lo:.5f},{hi:.5f}], '
            f'xR={o["mean_x_reform"]:+.4f}+-{o["sigma_x_reform"]:.4f}, '
            f'uR={o["mean_u_reform"]:+.4f}+-{o["sigma_u_reform"]:.4f}, '
            f'rho={o["rho_xu_reform"]:+.3f}, tauCold={o["tau_cold_ns"]:.3f} ns'
        )
        print(msg)
        print(f'::notice title=Experiment 03 nonlinear R-alpha::{msg}')
    print('PASS')


if __name__=='__main__':
    main()
