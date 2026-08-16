#!/usr/bin/env python3
"""Photon-capture screen for the beta_cold=.85, tilt=.05 hybrid-rescue candidate.

The live exact static scan gives approximately
    B_iso ~31.04
    Tf    ~0.77 K,
placing beta=.85 between the baseline beta=.80 and the stronger but hotter
beta=.90 shape rescue.

Test the same R=80 ohm, alpha=.90 passive two-pole environment at 14 um,
20-ps rise and C=215 fF.  Fractions are symmetrized-FDT TWA screening values,
not exact quantum efficiencies.
"""
from __future__ import annotations
import full_dynamic_rfsquid as fd
import nonlinear_fdt_twa_screen as nf
from nonlinear_fdt_twa_convergence import wilson


def main():
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    try:
        fd.BETA_COLD=.85; fd.DELTA_TILT=.05
        model=fd.DynamicForce(.6,quick=False,Tmax=1.02)
        print(f'beta=.85 tilt=.05 fold={model.fold_temperature(hi=.98):.5f}K')
        for A in (55.,60.,65.,70.,75.,80.,85.):
            o=nf.run_case(model,14.,R=80.,alpha=.90,ntraj=2048,dt_ps=.125,
                          seed=717171,area_um2=A,rise_ps=20.)
            k=int(o['n_right_final']); lo,hi=wilson(k,2048)
            msg=(f'A={A:g}um2: P_final={o["P_right_final"]:.6f} CI95=[{lo:.6f},{hi:.6f}] '
                 f'fail={2048-k} P_reform={o["P_xright_reform"]:.6f} reform={o["reform_ps"]:.2f}ps')
            print(msg); print(f'::notice title=Experiment 03 beta085 capture::{msg}')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot
    print('PASS')
if __name__=='__main__': main()
