#!/usr/bin/env python3
"""Refine the sharp 14-um absorber-area transition of the R80 candidate.

The coarse area scan found P_final~0.999 at A=80 um^2 and ~0.980 at 90 um^2.
This script resolves the transition at dt=0.125 ps with paired bath histories.
Fractions remain symmetrized-FDT TWA screening values, not exact quantum
 efficiencies.
"""
from __future__ import annotations
from full_dynamic_rfsquid import DynamicForce
from nonlinear_fdt_twa_screen import run_case
from nonlinear_fdt_twa_convergence import wilson


def main():
    model=DynamicForce(.6,quick=False,Tmax=.95)
    R=80.; alpha=.90; lam=14.; rise=20.; dt=.125; N=4096; seed=515151
    print('Experiment 03 R80 area-threshold refinement')
    for A in (80.,82.,84.,86.,88.,90.):
        o=run_case(model,lam,R=R,alpha=alpha,ntraj=N,dt_ps=dt,seed=seed,
                   area_um2=A,rise_ps=rise)
        k=int(o['n_right_final']); lo,hi=wilson(k,N)
        msg=(f'A={A:g} um2 lambda*A={lam*A:.1f}: P_reform={o["P_xright_reform"]:.7f} '
             f'P_final={o["P_right_final"]:.7f} CI95=[{lo:.7f},{hi:.7f}] '
             f'fail={N-k} reform={o["reform_ps"]:.2f}ps '
             f'xR={o["mean_x_reform"]:+.5f}+-{o["sigma_x_reform"]:.5f} '
             f'uR={o["mean_u_reform"]:+.5f}+-{o["sigma_u_reform"]:.5f}')
        print(msg); print(f'::notice title=Experiment 03 R80 area threshold::{msg}')
    print('PASS')
if __name__=='__main__': main()
