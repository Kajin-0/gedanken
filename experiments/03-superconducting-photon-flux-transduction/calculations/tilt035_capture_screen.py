#!/usr/bin/env python3
"""Photon-capture screen for the low-tilt dark-action rescue delta=.035.

At live beta_cold=.80 the exact isolated-action scan gives approximately

    delta=.050: B_iso=25.03, Tf=.694 K, right-well bias~5.48 K
    delta=.035: B_iso=28.96, Tf=.703 K, right-well bias~3.84 K.

Thus reducing tilt buys nearly four isolated action units with little thermal-fold
penalty, at the cost of reduced directionality.  This script tests that trade in
the same passive R=80 ohm, alpha=.90 two-pole capture model at 14 um, 20-ps rise.

Fractions are symmetrized-FDT TWA screening values, not exact quantum efficiencies.
"""
from __future__ import annotations
import full_dynamic_rfsquid as fd
import nonlinear_fdt_twa_screen as nf
from nonlinear_fdt_twa_convergence import wilson


def main():
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    try:
        fd.BETA_COLD=.80; fd.DELTA_TILT=.035
        model=fd.DynamicForce(.6,quick=False,Tmax=.98)
        print(f'beta=.80 tilt=.035 fold={model.fold_temperature(hi=.95):.6f}K')
        for A in (75.,80.,84.,86.,88.,90.,95.):
            o=nf.run_case(model,14.,R=80.,alpha=.90,ntraj=2048,dt_ps=.125,
                          seed=757575,area_um2=A,rise_ps=20.)
            k=int(o['n_right_final']); lo,hi=wilson(k,2048)
            msg=(f'A={A:g}: P_final={o["P_right_final"]:.6f} CI95=[{lo:.6f},{hi:.6f}] '
                 f'fail={2048-k} P_reform={o["P_xright_reform"]:.6f} '
                 f'reform={o["reform_ps"]:.2f}ps coldReg=({o["cold_reg_x"]:.3f},{o["cold_reg_u"]:.3f})')
            print(msg); print(f'::notice title=Experiment 03 tilt035 capture::{msg}')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot
    print('PASS')
if __name__=='__main__': main()
