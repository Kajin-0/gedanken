#!/usr/bin/env python3
"""Joint electrical dark-action / 14-um capture Pareto screen.

The full nonlocal zero-T dissipative bounce at the baseline R80/alpha=.90 point
has converged action

    B_base = 29.765636.

Under the exact electrical similarity

    C -> r^2 C, R -> R/r, omega_D -> omega_D/r

the zero-T Euclidean action scales exactly as

    B(r)=r B_base,

while the physical graphene thermal pulse is left unchanged and therefore the
photon-capture probability changes.

This workflow maps, for several r values, the largest 14-um absorber area that
still gives approximately >=99% under the existing symmetrized-FDT TWA stress.
The fractions are NOT exact quantum efficiencies.  The dark-rate column

    Gamma_scale=(fc0/r)*exp[-r B_base]

is only a same-dimensionless-prefactor screening scale until the dissipative
fluctuation determinant is calculated.
"""
from __future__ import annotations

import math

import full_dynamic_rfsquid as fd
import nonlinear_fdt_twa_screen as nf
from full_dynamic_rfsquid import DynamicForce
from nonlinear_fdt_twa_convergence import wilson
from quantum_initial_capture import quantum_covariance

L0=111.5e-12
C0=215e-15
R0=80.0
ALPHA=.90
TF=.695
BBASE=29.7656360
FC0=27.255899e9


def main():
    model=DynamicForce(.6,quick=False,Tmax=.95)
    original=fd.CASES[.6]
    print('Experiment 03 joint dark-action / capture Pareto screen')
    print('capture fractions are symmetrized-FDT TWA stresses, not exact quantum efficiencies')
    try:
        for r in (1.0,1.10,1.20,1.263542,1.30,1.40):
            C=C0*r*r; R=R0/r
            fd.CASES[.6]=(L0,C,TF); nf.CASES[.6]=(L0,C,TF)
            cov=quantum_covariance(model,.6); wc=cov['omega_c']
            B=r*BBASE
            gamma_scale=(FC0/r)*math.exp(-B)
            print(f'\nr={r:.6f}: C={C*1e15:.2f}fF R={R:.3f}ohm fc={wc/(2*math.pi)*1e-9:.4f}GHz B={B:.5f} Gamma_scale={gamma_scale:.3e}/s')
            for A in (70.,74.,78.,80.,82.,84.,86.):
                o=nf.run_case(model,14.,R=R,alpha=ALPHA,ntraj=2048,dt_ps=.125,
                              seed=565656,area_um2=A,rise_ps=20.)
                k=int(o['n_right_final']); lo,hi=wilson(k,2048)
                msg=(f'r={r:.6f} A={A:g}: P={o["P_right_final"]:.6f} '
                     f'CI95=[{lo:.6f},{hi:.6f}] fail={2048-k} '
                     f'P_reform={o["P_xright_reform"]:.6f} reform={o["reform_ps"]:.2f}ps')
                print(msg); print(f'::notice title=Experiment 03 dark-capture Pareto::{msg}')
    finally:
        fd.CASES[.6]=original; nf.CASES[.6]=original
    print('PASS')

if __name__=='__main__': main()
