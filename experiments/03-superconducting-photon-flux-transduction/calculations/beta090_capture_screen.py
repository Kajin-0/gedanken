#!/usr/bin/env python3
"""Photon-capture screen for the live barrier-shape rescue beta_cold=.90.

The corrected exact static scan found, at the same live tilt delta=.05,

    beta=.80: B_iso ~25.03, Tf~.694 K
    beta=.90: B_iso ~37.63, Tf~.846 K.

Thus beta=.90 may solve much of the dark-action deficit without slowing the
phase circuit, but it also raises the thermal fold.  This workflow tests that
trade directly in the same passive two-pole capture model.

Environment is initially held at the baseline screening choice

    R=80 ohm, alpha=.90,

with C=215 fF, 14-um photon, 20-ps physical rise.  Absorber area is swept from
small/high-headroom to large/low-headroom.

Fractions are symmetrized-FDT TWA screening values, not exact quantum
 efficiencies.  If beta=.90 survives, its same-environment nonlocal bounce must
then be recomputed before any dark conclusion.
"""
from __future__ import annotations

import full_dynamic_rfsquid as fd
import nonlinear_fdt_twa_screen as nf
from nonlinear_fdt_twa_convergence import wilson


def main():
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    try:
        fd.BETA_COLD=.90; fd.DELTA_TILT=.05
        # nf imported DynamicForce/global constants from fd; build after mutation.
        model=fd.DynamicForce(.6,quick=False,Tmax=1.05)
        print(f'beta={fd.BETA_COLD:.2f} tilt={fd.DELTA_TILT:.3f} fold={model.fold_temperature(hi=1.0):.5f}K')
        for A in (45.,50.,55.,60.,65.,70.,75.,80.):
            o=nf.run_case(model,14.,R=80.,alpha=.90,ntraj=2048,dt_ps=.125,
                          seed=707070,area_um2=A,rise_ps=20.)
            k=int(o['n_right_final']); lo,hi=wilson(k,2048)
            msg=(f'A={A:g}um2: P_final={o["P_right_final"]:.6f} '
                 f'CI95=[{lo:.6f},{hi:.6f}] fail={2048-k} '
                 f'P_reform={o["P_xright_reform"]:.6f} reform={o["reform_ps"]:.2f}ps '
                 f'coldReg=({o["cold_reg_x"]:.3f},{o["cold_reg_u"]:.3f})')
            print(msg); print(f'::notice title=Experiment 03 beta090 capture::{msg}')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot
    print('PASS')
if __name__=='__main__': main()
