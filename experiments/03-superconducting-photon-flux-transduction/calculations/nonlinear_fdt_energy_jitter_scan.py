#!/usr/bin/env python3
"""Nonlinear stationary-bath robustness to deposited-energy-density variation.

The favorable write mechanism is phase-matched and therefore potentially
sensitive to stochastic electronic energy partition/cooling.  This script tests
whether the current R=80-ohm, alpha=.90 candidate is a broad energy-density
plateau or a narrow lobe.

At fixed 8-um photon wavelength, vary deposited energy density by factor s via

    A_eff = 100 um^2 / s,

which is exactly equivalent inside the retained lumped thermal model to scaling
fast deposited energy by s at fixed area.

Use the same external bath histories for every s to reduce Monte Carlo noise in
the differences.  Results remain symmetrized-FDT TWA/GLE screening fractions,
not exact quantum efficiencies.  This is a deterministic-thermal sensitivity
scan: stochastic electron-phonon/partition dynamics are not yet generated
explicitly.
"""
from __future__ import annotations
import argparse
from full_dynamic_rfsquid import DynamicForce
from nonlinear_fdt_twa_screen import run_case
from nonlinear_fdt_twa_convergence import wilson


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--ntraj',type=int,default=1024)
    p.add_argument('--dt-ps',type=float,default=.5)
    p.add_argument('--seed',type=int,default=313131)
    a=p.parse_args()
    print('Experiment 03 deposited-energy-density robustness')
    print('R=80 ohm, alpha=.90, delta=.05, C=215 fF, rise=20 ps')
    model=DynamicForce(.6,quick=False,Tmax=1.05)
    for s in (.75,.80,.85,.90,.95,1.00,1.05,1.10,1.15,1.20,1.25):
        area=100.0/s
        o=run_case(model,8.0,R=80.0,alpha=.90,ntraj=a.ntraj,
                   dt_ps=a.dt_ps,seed=a.seed,area_um2=area,rise_ps=20.0)
        n=int(o['ntraj']); k=int(o['n_right_final']); lo,hi=wilson(k,n)
        msg=(
            f'energyScale={s:.3f} (Aeff={area:.4f} um2): '
            f'coldReg=({o["cold_reg_x"]:.4f},{o["cold_reg_u"]:.4f}), '
            f'P_reform={o["P_xright_reform"]:.6f}, '
            f'P_final={o["P_right_final"]:.6f} CI95=[{lo:.6f},{hi:.6f}] fail={n-k}, '
            f'reform={o["reform_ps"]:.3f} ps, '
            f'xR={o["mean_x_reform"]:+.4f}+-{o["sigma_x_reform"]:.4f}, '
            f'uR={o["mean_u_reform"]:+.4f}+-{o["sigma_u_reform"]:.4f}'
        )
        print(msg)
        print(f'::notice title=Experiment 03 energy-density robustness::{msg}')
    print('PASS')

if __name__=='__main__':
    main()
