#!/usr/bin/env python3
"""2-ns photon-capture screen for the crossover-independent delta=.213 design.

A branch-aware finite-temperature dark-rate scan places the first descending
Gamma_dark=1e-6/s crossing at r ~= 11.20596, well below both the local
Matsubara-instability scale r_x=11.64824 and the first-order periodic/sphaleron
action crossing r_c~=12.034.  Therefore this point does not depend on how the
first-order crossover is uniformized.

The electrical scale used here is the log-interpolated target locator from the
branch-aware scan.  Its uncertainty is negligible for this coarse capture
screen; if it becomes the leading point the dark root should be refined before
a high-stat final probability run.
"""
from __future__ import annotations

import math
import full_dynamic_rfsquid as fd
import nonlinear_fdt_twa_screen as nf
from nonlinear_fdt_twa_convergence import wilson
from quantum_initial_capture import quantum_covariance

DELTA=.213
R_SCALE=11.20595576
C0=215e-15; R0=80.; L0=111.5e-12; ALPHA=.90
AREAS=(480.,500.,510.,520.,530.,540.,560.)


def main():
    C=C0*R_SCALE*R_SCALE; R=R0/R_SCALE
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT; original=fd.CASES[.6]
    try:
        fd.BETA_COLD=.80; fd.DELTA_TILT=DELTA
        fd.CASES[.6]=(L0,C,original[2]); nf.CASES[.6]=fd.CASES[.6]
        model=fd.DynamicForce(.6,quick=False,Tmax=1.02)
        fold=model.fold_temperature(hi=.98)
        wc=quantum_covariance(model,.6)['omega_c']
        hdr=(f'delta={DELTA:.3f} r_target={R_SCALE:.8f} C={C*1e12:.6f}pF '
             f'R={R:.6f}ohm fold={fold:.6f}K fc={wc/(2*math.pi)*1e-9:.6f}GHz '
             f'dark_class=crossover-independent-periodic')
        print(hdr); print(f'::notice title=Experiment 03 delta213 design::{hdr}')
        for A in AREAS:
            o=nf.run_case(model,14.,R=R,alpha=ALPHA,ntraj=1024,dt_ps=.125,tpost_ns=2.0,
                          seed=5213000,area_um2=A,rise_ps=20.)
            k=int(o['n_right_final']); lo,hi=wilson(k,1024)
            msg=(f'A={A:g}um2: P_final={o["P_right_final"]:.6f} CI95=[{lo:.6f},{hi:.6f}] '
                 f'fail={1024-k} P_reform={o["P_xright_reform"]:.6f} '
                 f'reform={o["reform_ps"]:.2f}ps xfinal={o["mean_x_final"]:+.5f}+-{o["sigma_x_final"]:.5f} '
                 f'coldReg=({o["cold_reg_x"]:.3f},{o["cold_reg_u"]:.3f})')
            print(msg); print(f'::notice title=Experiment 03 delta213 capture::{msg}')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot; fd.CASES[.6]=original; nf.CASES[.6]=original

if __name__=='__main__': main()
