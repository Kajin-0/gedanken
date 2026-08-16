#!/usr/bin/env python3
"""Photon-capture probe at the exact finite-T dark-action ceiling.

At
    delta = 0.2150240395
    T0 = 20 mK
    B_sph = 37.61

the minimal electrical compensation that reaches the target is the exact
quantum/thermal crossover scale
    r_x = 11.563620471.

This script asks whether the nonlinear photon latch is still functional at that
finite endpoint.  It does NOT promote the endpoint to a physical design: the
dark prefactor and the symmetrized-FDT capture approximation remain unresolved.

The 2-ns recovery horizon used by the current capture code is also explicitly
reported as a possible limitation because the compensated phase clock is only
~1.80 GHz.
"""
from __future__ import annotations
import math
import full_dynamic_rfsquid as fd
import nonlinear_fdt_twa_screen as nf
from nonlinear_fdt_twa_convergence import wilson
from quantum_initial_capture import quantum_covariance

DELTA=0.2150240395
R_SCALE=11.563620471
C0=215e-15; R0=80.; L0=111.5e-12; ALPHA=.90


def main():
    C=C0*R_SCALE*R_SCALE; R=R0/R_SCALE
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT; original=fd.CASES[.6]
    try:
        fd.BETA_COLD=.80; fd.DELTA_TILT=DELTA
        fd.CASES[.6]=(L0,C,original[2]); nf.CASES[.6]=fd.CASES[.6]
        model=fd.DynamicForce(.6,quick=False,Tmax=1.02)
        fold=model.fold_temperature(hi=.98)
        cov=quantum_covariance(model,.6); wc=cov['omega_c']
        print(f'delta={DELTA:.10f} r={R_SCALE:.9f} C={C*1e15:.3f}fF R={R:.6f}ohm '
              f'fold={fold:.6f}K fc={wc/(2*math.pi)*1e-9:.6f}GHz')
        for A in (420.,500.,580.,660.,740.,820.):
            o=nf.run_case(model,14.,R=R,alpha=ALPHA,ntraj=2048,dt_ps=.125,
                          seed=215024,area_um2=A,rise_ps=20.)
            k=int(o['n_right_final']); lo,hi=wilson(k,2048)
            msg=(f'A={A:g}um2: P_final={o["P_right_final"]:.6f} '
                 f'CI95=[{lo:.6f},{hi:.6f}] fail={2048-k} '
                 f'P_reform={o["P_xright_reform"]:.6f} reform={o["reform_ps"]:.2f}ps '
                 f'coldReg=({o["cold_reg_x"]:.3f},{o["cold_reg_u"]:.3f})')
            print(msg); print(f'::notice title=Experiment 03 ceiling capture::{msg}')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot; fd.CASES[.6]=original; nf.CASES[.6]=original
    print('PASS')

if __name__=='__main__': main()
