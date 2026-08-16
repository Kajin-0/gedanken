#!/usr/bin/env python3
"""Photon-capture screen for the mild beta_cold=.825 shape candidate.

The converged same-environment nonlocal continuation gives
    B_diss(beta=.825, delta=.05) = 33.3360645,
compared with 29.7656358 at the beta=.80 baseline.

This is the last mild static-shape point that might outperform the pure
electrical dark-action rescue after a smaller electrical similarity scaling.
Test the unscaled C=215 fF, R=80 ohm, alpha=.90 system first at 14 um / 20 ps.

All probabilities are symmetrized-FDT truncated-Wigner screening quantities,
not exact physical quantum efficiencies.
"""
from __future__ import annotations

import full_dynamic_rfsquid as fd
import nonlinear_fdt_twa_screen as nf
from nonlinear_fdt_twa_convergence import wilson


def main():
    ob, ot = fd.BETA_COLD, fd.DELTA_TILT
    try:
        fd.BETA_COLD = .825
        fd.DELTA_TILT = .05
        model = fd.DynamicForce(.6, quick=False, Tmax=1.02)
        fold = model.fold_temperature(hi=.98)
        print(f'beta=.825 tilt=.05 fold={fold:.6f}K')
        for A in (68., 70., 72., 74., 76., 78., 80., 82., 84.):
            o = nf.run_case(model, 14., R=80., alpha=.90,
                            ntraj=2048, dt_ps=.125, seed=825825,
                            area_um2=A, rise_ps=20.)
            k = int(o['n_right_final'])
            lo, hi = wilson(k, 2048)
            msg = (f'A={A:g}um2: P_final={o["P_right_final"]:.6f} '
                   f'CI95=[{lo:.6f},{hi:.6f}] fail={2048-k} '
                   f'P_reform={o["P_xright_reform"]:.6f} '
                   f'reform={o["reform_ps"]:.2f}ps '
                   f'coldReg=({o["cold_reg_x"]:.3f},{o["cold_reg_u"]:.3f})')
            print(msg)
            print(f'::notice title=Experiment 03 beta0825 capture::{msg}')
    finally:
        fd.BETA_COLD = ob
        fd.DELTA_TILT = ot
    print('PASS')


if __name__ == '__main__':
    main()
