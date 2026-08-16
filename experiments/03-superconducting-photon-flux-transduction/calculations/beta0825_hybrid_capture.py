#!/usr/bin/env python3
"""Equal-dark-action capture comparison: beta=.825 plus electrical scaling.

The converged same-environment action at beta=.825, delta=.05 is
    B0 = 33.3360645.
Match the established pure-electrical benchmark B_target=37.61 through the exact
zero-temperature electrical similarity
    C -> r^2 C, R -> R/r, omega_D -> omega_D/r,
with r=B_target/B0.

The physical 14-um / 20-ps graphene thermal pulse is NOT rescaled. The resulting
capture curve can therefore be compared directly with the beta=.80 pure-electrical
benchmark at the same dark-action target.

Probabilities are symmetrized-FDT TWA screening quantities, not exact quantum
physical efficiencies.
"""
from __future__ import annotations

import math
import full_dynamic_rfsquid as fd
import nonlinear_fdt_twa_screen as nf
from nonlinear_fdt_twa_convergence import wilson
from quantum_initial_capture import quantum_covariance

B0 = 33.3360645
B_TARGET = 37.61
R0 = 80.0
C0 = 215e-15
L0 = 111.5e-12
ALPHA = .90


def main():
    r = B_TARGET / B0
    C = C0 * r * r
    R = R0 / r
    ob, ot = fd.BETA_COLD, fd.DELTA_TILT
    original = fd.CASES[.6]
    try:
        fd.BETA_COLD = .825
        fd.DELTA_TILT = .05
        # Preserve the static fold entry; the DynamicForce model determines the
        # actual beta=.825 topology, while C only changes the phase inertia.
        fd.CASES[.6] = (L0, C, original[2])
        nf.CASES[.6] = fd.CASES[.6]
        model = fd.DynamicForce(.6, quick=False, Tmax=1.02)
        fold = model.fold_temperature(hi=.98)
        cov = quantum_covariance(model, .6)
        wc = cov['omega_c']
        print(f'beta=.825 tilt=.05 r={r:.9f} C={C*1e15:.3f}fF R={R:.4f}ohm '
              f'fold={fold:.6f}K fc={wc/(2*math.pi)*1e-9:.5f}GHz '
              f'Btarget={B_TARGET:.5f}')
        for A in (70., 72., 74., 76., 78., 80., 82., 84.):
            o = nf.run_case(model, 14., R=R, alpha=ALPHA,
                            ntraj=2048, dt_ps=.125, seed=825128,
                            area_um2=A, rise_ps=20.)
            k = int(o['n_right_final'])
            lo, hi = wilson(k, 2048)
            msg = (f'A={A:g}um2: P_final={o["P_right_final"]:.6f} '
                   f'CI95=[{lo:.6f},{hi:.6f}] fail={2048-k} '
                   f'P_reform={o["P_xright_reform"]:.6f} '
                   f'reform={o["reform_ps"]:.2f}ps '
                   f'coldReg=({o["cold_reg_x"]:.3f},{o["cold_reg_u"]:.3f})')
            print(msg)
            print(f'::notice title=Experiment 03 beta0825 hybrid::{msg}')
    finally:
        fd.BETA_COLD = ob
        fd.DELTA_TILT = ot
        fd.CASES[.6] = original
        nf.CASES[.6] = original
    print('PASS')


if __name__ == '__main__':
    main()
