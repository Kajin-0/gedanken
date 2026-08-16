#!/usr/bin/env python3
"""Map absorber-area margin of the strongest current two-pole candidate.

Current candidate:
    rDelta=.6, R=80 ohm, alpha=omega_D/omega_c=.90,
    lambda=14 um, rise=20 ps.

The reduced graphene thermal model has the exact similarity variable

    lambda_um * area_um2,

because the photon-induced increment in T_e^2 is proportional to 1/(lambda A).
The previously validated A=57.142857 um^2 point is therefore exactly similar to
8 um at A=100 um^2.  This script asks how much larger A can become before the
high-capture sym-FDT/TWA margin degrades.

These remain semiclassical symmetrized-noise screening fractions, not exact
quantum efficiencies.  See QUANTUM_DETAILED_BALANCE_CORRECTION_2026-08-15.md.
"""
from __future__ import annotations
import numpy as np

from full_dynamic_rfsquid import DynamicForce
from nonlinear_fdt_twa_screen import run_case
from nonlinear_fdt_twa_convergence import wilson


def report(A,o):
    n=int(o['ntraj']); k=int(o['n_right_final']); lo,hi=wilson(k,n)
    return (
        f'A={A:g} um2, lambda*A={14*A:.3f}: N={n}, '
        f'coldReg=({o["cold_reg_x"]:.4f},{o["cold_reg_u"]:.4f}), '
        f'P_reform={o["P_xright_reform"]:.6f}, '
        f'P_final={o["P_right_final"]:.6f} CI95=[{lo:.6f},{hi:.6f}], '
        f'fail={n-k}, reform={o["reform_ps"]:.2f} ps, '
        f'xR={o["mean_x_reform"]:+.4f}+-{o["sigma_x_reform"]:.4f}, '
        f'uR={o["mean_u_reform"]:+.4f}+-{o["sigma_u_reform"]:.4f}'
    )


def main():
    R=80.0; alpha=.90; lam=14.0; rise=20.0
    model=DynamicForce(.6,quick=False,Tmax=.95)
    print('Experiment 03 R80 14-um absorber-area margin')
    print('symmetrized-FDT TWA stress only; not exact quantum efficiency')
    # Paired noise histories via fixed seed reduce uncertainty in area differences.
    for A in (50.0,57.142857,65.0,72.0,80.0,90.0,100.0,110.0,120.0):
        o=run_case(model,lam,R=R,alpha=alpha,ntraj=2048,dt_ps=.25,
                   seed=919191,area_um2=A,rise_ps=rise)
        msg=report(A,o); print(msg)
        print(f'::notice title=Experiment 03 R80 area margin::{msg}')

    # Timestep refinement at the exact-similarity reference and near the expected
    # practical margin; use N=4096 for the reference and N=2048 near margin.
    for A,N in ((57.142857,4096),(80.0,2048)):
        for dt in (.25,.125):
            o=run_case(model,lam,R=R,alpha=alpha,ntraj=N,dt_ps=dt,
                       seed=737373,area_um2=A,rise_ps=rise)
            msg=f'dt={dt:.3f} ps '+report(A,o); print(msg)
            print(f'::notice title=Experiment 03 R80 dt refine::{msg}')
    print('PASS')

if __name__=='__main__': main()
