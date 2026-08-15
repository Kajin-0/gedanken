#!/usr/bin/env python3
"""Push the nonlinear stationary-bath TWA/GLE resistance scan below 80 ohm.

The focused low-R scan found essentially perfect 1024-trajectory capture at
R=80--100 ohm over broad alpha ranges for the favorable 8-um-equivalent
energy-density lobe.  This script continues downward until stronger damping/noise
or overdamped launch causes a clear turnover.

Results are semiclassical TWA/GLE screening fractions, not exact quantum
efficiencies.  The same causal Y(omega) must later be used in dissipative dark
escape.
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
    ap.add_argument('--seed',type=int,default=919191)
    args=ap.parse_args()

    print('Experiment 03 ultralow-R nonlinear stationary-bath scan')
    print(f'R={args.R:g} ohm, rDelta=.6, delta=.05, C=215 fF, 8-um equivalent')
    model=DynamicForce(0.6,quick=False,Tmax=0.95)
    for alpha in (0.40,0.50,0.60,0.70,0.80,0.90,1.00,1.20,1.50):
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
        print(f'::notice title=Experiment 03 ultralow-R::{msg}')
    print('PASS')


if __name__=='__main__':
    main()
