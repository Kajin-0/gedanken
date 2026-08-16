#!/usr/bin/env python3
"""Focused high-stat capture test at the current dark-action rescue scale.

Full nonlocal baseline action:
    B_base = 29.765636.

Using the similarity-prefactor screening equation
    (fc0/r) exp(-r B_base)=1e-6 /s
puts r=1.263542 near the current dark-action target scale.

This script tests only that r, with C=r^2*215 fF, R=80/r, alpha=.90,
physical 20-ps graphene rise unchanged, at 14 um and A=76..84 um^2.

Capture fractions are symmetrized-FDT TWA stresses, not exact quantum
 efficiencies.  The 1e-6/s dark target remains prefactor-conditional until the
 determinant calculation is converged.
"""
from __future__ import annotations
import math
import full_dynamic_rfsquid as fd
import nonlinear_fdt_twa_screen as nf
from full_dynamic_rfsquid import DynamicForce
from nonlinear_fdt_twa_convergence import wilson
from quantum_initial_capture import quantum_covariance

RSC=1.263542
L0=111.5e-12; C0=215e-15; R0=80.; TF=.695; ALPHA=.90
BBASE=29.765636; FC0=27.255899e9


def main():
    model=DynamicForce(.6,quick=False,Tmax=.95)
    old=fd.CASES[.6]
    C=C0*RSC**2; R=R0/RSC
    try:
        fd.CASES[.6]=(L0,C,TF); nf.CASES[.6]=(L0,C,TF)
        cov=quantum_covariance(model,.6); fc=cov['omega_c']/(2*math.pi)
        B=RSC*BBASE; gamma=(FC0/RSC)*math.exp(-B)
        print(f'r={RSC:.6f} C={C*1e15:.3f}fF R={R:.4f}ohm fc={fc*1e-9:.5f}GHz B={B:.6f} crudeGamma={gamma:.3e}/s')
        for A in (76.,78.,80.,82.,84.):
            o=nf.run_case(model,14.,R=R,alpha=ALPHA,ntraj=4096,dt_ps=.125,
                          seed=969696,area_um2=A,rise_ps=20.)
            k=int(o['n_right_final']); lo,hi=wilson(k,4096)
            msg=(f'A={A:g}: P_final={o["P_right_final"]:.7f} CI95=[{lo:.7f},{hi:.7f}] '
                 f'fail={4096-k} P_reform={o["P_xright_reform"]:.7f} '
                 f'reform={o["reform_ps"]:.2f}ps')
            print(msg); print(f'::notice title=Experiment 03 focused dark rescue::{msg}')
    finally:
        fd.CASES[.6]=old; nf.CASES[.6]=old
    print('PASS')
if __name__=='__main__': main()
