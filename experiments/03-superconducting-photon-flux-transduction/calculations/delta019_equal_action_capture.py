#!/usr/bin/env python3
"""Equal-action capture at delta=.19, just below the finite-T crossover region.

Exact base nonlocal action B0=6.52571286. Restore B_target=37.61 with the exact
electrical similarity; keep the physical 14-um / 20-ps graphene pulse fixed.

This is a symmetrized-FDT TWA screening calculation, not a physical efficiency.
"""
from __future__ import annotations
import math
import full_dynamic_rfsquid as fd
import nonlinear_fdt_twa_screen as nf
from nonlinear_fdt_twa_convergence import wilson
from quantum_initial_capture import quantum_covariance

B0=6.52571286; BT=37.61
C0=215e-15; R0=80.; L0=111.5e-12; ALPHA=.90

def main():
    delta=.19; r=BT/B0; C=C0*r*r; R=R0/r
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT; original=fd.CASES[.6]
    try:
        fd.BETA_COLD=.80; fd.DELTA_TILT=delta
        fd.CASES[.6]=(L0,C,original[2]); nf.CASES[.6]=fd.CASES[.6]
        model=fd.DynamicForce(.6,quick=False,Tmax=1.02)
        fold=model.fold_temperature(hi=.98); cov=quantum_covariance(model,.6); wc=cov['omega_c']
        print(f'delta=.190 r={r:.9f} C={C*1e15:.3f}fF R={R:.4f}ohm fold={fold:.6f}K '
              f'fc={wc/(2*math.pi)*1e-9:.5f}GHz Btarget={BT:.5f}')
        for A in (300.,340.,380.,420.,460.):
            o=nf.run_case(model,14.,R=R,alpha=ALPHA,ntraj=2048,dt_ps=.125,seed=190190,
                          area_um2=A,rise_ps=20.)
            k=int(o['n_right_final']); lo,hi=wilson(k,2048)
            msg=(f'A={A:g}um2: P_final={o["P_right_final"]:.6f} CI95=[{lo:.6f},{hi:.6f}] '
                 f'fail={2048-k} P_reform={o["P_xright_reform"]:.6f} reform={o["reform_ps"]:.2f}ps '
                 f'coldReg=({o["cold_reg_x"]:.3f},{o["cold_reg_u"]:.3f})')
            print(msg); print(f'::notice title=Experiment 03 delta019 equal-action capture::{msg}')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot; fd.CASES[.6]=original; nf.CASES[.6]=original
    print('PASS')

if __name__=='__main__': main()
