#!/usr/bin/env python3
"""Final strong-damping scan for Experiment 03.

The causal stationary-bath TWA/GLE optimization remained near-perfect down to
R=20 ohm provided the dissipative cutoff alpha=omega_D/omega_c was raised into
the appropriate band.  This final write-side scan pushes to 5--20 ohm to locate
the actual overdamped/noise turnover.  If no useful improvement appears below
20 ohm, further write-only R scanning should stop and the theory should move to
same-Y dark tunneling/open-system quantum validation.

Results are semiclassical screening fractions only.
"""
from __future__ import annotations
import argparse
from full_dynamic_rfsquid import DynamicForce
from nonlinear_fdt_twa_screen import run_case
from nonlinear_fdt_twa_convergence import wilson


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--R',type=float,required=True)
    p.add_argument('--ntraj',type=int,default=512)
    p.add_argument('--dt-ps',type=float,default=0.5)
    p.add_argument('--seed',type=int,default=717171)
    a=p.parse_args()
    print(f'Experiment 03 extreme-R scan: R={a.R:g} ohm')
    model=DynamicForce(0.6,quick=False,Tmax=0.95)
    for alpha in (0.70,0.80,0.90,1.00,1.20,1.40,1.60,2.00,2.50):
        o=run_case(model,8.0,R=a.R,alpha=alpha,ntraj=a.ntraj,
                   dt_ps=a.dt_ps,seed=a.seed)
        n=int(o['ntraj']); k=int(o['n_right_final'])
        lo,hi=wilson(k,n)
        msg=(f'R={a.R:g}, alpha={alpha:.2f}: '
             f'coldReg=({o["cold_reg_x"]:.4f},{o["cold_reg_u"]:.4f}), '
             f'P_reform={o["P_xright_reform"]:.6f}, '
             f'P_final={o["P_right_final"]:.6f} CI95=[{lo:.6f},{hi:.6f}], '
             f'fail={n-k}, tauCold={o["tau_cold_ns"]:.5f} ns, '
             f'xR={o["mean_x_reform"]:+.4f}+-{o["sigma_x_reform"]:.4f}, '
             f'uR={o["mean_u_reform"]:+.4f}+-{o["sigma_u_reform"]:.4f}')
        print(msg)
        print(f'::notice title=Experiment 03 extreme low-R::{msg}')
    print('PASS')

if __name__=='__main__':
    main()
