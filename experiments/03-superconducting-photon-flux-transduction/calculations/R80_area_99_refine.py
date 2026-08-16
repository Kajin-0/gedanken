#!/usr/bin/env python3
"""High-statistics refinement of the R80 14-um sym-TWA P=0.99 area crossing.

This is a screening threshold only, not exact physical quantum efficiency.
"""
from __future__ import annotations
from full_dynamic_rfsquid import DynamicForce
from nonlinear_fdt_twa_screen import run_case
from nonlinear_fdt_twa_convergence import wilson


def main():
    model=DynamicForce(.6,quick=False,Tmax=.95)
    R=80.; alpha=.90; lam=14.; rise=20.; dt=.125; N=8192; seed=626262
    print('Experiment 03 R80 high-statistics area-99 refinement')
    for A in (84.0,84.5,85.0,85.5,86.0):
        o=run_case(model,lam,R=R,alpha=alpha,ntraj=N,dt_ps=dt,seed=seed,
                   area_um2=A,rise_ps=rise)
        k=int(o['n_right_final']); lo,hi=wilson(k,N)
        msg=(f'A={A:.1f} um2 lambdaA={lam*A:.1f}: P_final={o["P_right_final"]:.7f} '
             f'CI95=[{lo:.7f},{hi:.7f}] fail={N-k} '
             f'P_reform={o["P_xright_reform"]:.7f} reform={o["reform_ps"]:.2f}ps '
             f'xR={o["mean_x_reform"]:+.5f}+-{o["sigma_x_reform"]:.5f}')
        print(msg); print(f'::notice title=Experiment 03 R80 area99::{msg}')
    print('PASS')
if __name__=='__main__': main()
