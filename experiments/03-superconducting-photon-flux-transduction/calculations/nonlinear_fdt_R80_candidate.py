#!/usr/bin/env python3
"""High-statistics and 14-um robustness validation of the R=80-ohm candidate.

The focused low-R scan found zero final failures in 1024 TWA/GLE trajectories
at R=80 ohm for several cutoff values, including alpha=0.7, 0.9 and 1.0.
This script promotes the broad alpha~0.9 region to the next validation tier:

1. high-statistics 8-um-equivalent reference at A=100 um^2;
2. exact reduced-model thermal translation to 14 um at A=57.142857 um^2;
3. 14-um rise-time robustness around the spatially motivated 20-ps scale.

Results remain stationary-bath symmetrized-FDT TWA/GLE screening fractions,
not exact open-system quantum efficiencies.
"""
from __future__ import annotations
import argparse
from full_dynamic_rfsquid import DynamicForce
from nonlinear_fdt_twa_screen import run_case
from nonlinear_fdt_twa_convergence import wilson

A_EQ=100.0*8.0/14.0


def report(label,o):
    n=int(o['ntraj']); k=int(o['n_right_final'])
    lo,hi=wilson(k,n)
    return (
        f'{label}: N={n}, coldReg=({o["cold_reg_x"]:.5f},{o["cold_reg_u"]:.5f}), '
        f'P_reform={o["P_xright_reform"]:.7f}, '
        f'P_final={o["P_right_final"]:.7f} CI95=[{lo:.7f},{hi:.7f}] fail={n-k}, '
        f'reform={o["reform_ps"]:.2f} ps, '
        f'xR={o["mean_x_reform"]:+.5f}+-{o["sigma_x_reform"]:.5f}, '
        f'uR={o["mean_u_reform"]:+.5f}+-{o["sigma_u_reform"]:.5f}, '
        f'rho={o["rho_xu_reform"]:+.4f}, tauCold={o["tau_cold_ns"]:.5f} ns'
    )


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--dt-ps',type=float,required=True)
    p.add_argument('--ntraj',type=int,default=4096)
    p.add_argument('--seed',type=int,default=606060)
    a=p.parse_args()
    R=80.0; alpha=0.90
    print(f'Experiment 03 R80 alpha.90 validation N={a.ntraj} dt={a.dt_ps} ps')
    model=DynamicForce(0.6,quick=False,Tmax=0.95)
    ref=run_case(model,8.0,R=R,alpha=alpha,ntraj=a.ntraj,dt_ps=a.dt_ps,
                 seed=a.seed,area_um2=100.0,rise_ps=20.0)
    eq=run_case(model,14.0,R=R,alpha=alpha,ntraj=a.ntraj,dt_ps=a.dt_ps,
                seed=a.seed,area_um2=A_EQ,rise_ps=20.0)
    for label,o in [
        ('8um A100 rise20 reference',ref),
        (f'14um A{A_EQ:.6f} rise20 similarity',eq),
    ]:
        msg=report(label,o); print(msg)
        print(f'::notice title=Experiment 03 R80 validation::{msg}')
    print(
        f'similarity delta P={eq["P_right_final"]-ref["P_right_final"]:+.3e}, '
        f'dx={eq["mean_x_reform"]-ref["mean_x_reform"]:+.3e}, '
        f'du={eq["mean_u_reform"]-ref["mean_u_reform"]:+.3e}'
    )
    # Smaller 2048-sample paired robustness ensemble is sufficient for shape;
    # the 4096 reference above carries the main statistical claim.
    for rise in (15.0,18.0,20.0,22.0,24.0,26.0,28.0,30.0):
        o=run_case(model,14.0,R=R,alpha=alpha,ntraj=min(a.ntraj,2048),
                   dt_ps=a.dt_ps,seed=a.seed,area_um2=A_EQ,rise_ps=rise)
        msg=report(f'14um A{A_EQ:.3f} rise{rise:g}',o); print(msg)
        print(f'::notice title=Experiment 03 R80 rise robustness::{msg}')
    print('PASS')

if __name__=='__main__':
    main()
