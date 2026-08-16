#!/usr/bin/env python3
"""2-ns capture screen at the last trustworthy one-loop dark-rate tilts.

This extends the calibrated Gamma_1loop(20 mK)=1e-6/s manifold to delta=.211
and .212, the last Gaussian one-loop points before the soft-mode-provisional
region begins at .213.

Capture remains a symmetrized-FDT TWA screening quantity, not an exact quantum
efficiency.
"""
from __future__ import annotations

import argparse, math
import full_dynamic_rfsquid as fd
import nonlinear_fdt_twa_screen as nf
from nonlinear_fdt_twa_convergence import wilson
from quantum_initial_capture import quantum_covariance

R_RATE={
    .2110:10.18791311,
    .2120:10.62175909,
}
AREA_GRID={
    .2110:(455.,470.,485.,500.,515.),
    .2120:(460.,475.,490.,505.,520.),
}
C0=215e-15; R0=80.; L0=111.5e-12; ALPHA=.90


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--delta',type=float,required=True); a=ap.parse_args()
    d=round(a.delta,4)
    if d not in R_RATE: raise SystemExit(f'unsupported delta {d}')
    r=R_RATE[d]; C=C0*r*r; R=R0/r
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT; original=fd.CASES[.6]
    try:
        fd.BETA_COLD=.80; fd.DELTA_TILT=d
        fd.CASES[.6]=(L0,C,original[2]); nf.CASES[.6]=fd.CASES[.6]
        model=fd.DynamicForce(.6,quick=False,Tmax=1.02)
        fold=model.fold_temperature(hi=.98)
        wc=quantum_covariance(model,.6)['omega_c']
        hdr=(f'delta={d:.4f} r_rate={r:.9f} C={C*1e15:.3f}fF R={R:.6f}ohm '
             f'fold={fold:.6f}K fc={wc/(2*math.pi)*1e-9:.6f}GHz '
             f'constraint=Gamma1loop_20mK=1e-6/s')
        print(hdr); print(f'::notice title=Experiment 03 one-loop boundary design::{hdr}')
        for A in AREA_GRID[d]:
            o=nf.run_case(model,14.,R=R,alpha=ALPHA,ntraj=2048,dt_ps=.125,tpost_ns=2.0,
                          seed=4211000+int(round(10000*d)),area_um2=A,rise_ps=20.)
            k=int(o['n_right_final']); lo,hi=wilson(k,2048)
            msg=(f'delta={d:.4f} A={A:g}um2: P_final={o["P_right_final"]:.6f} '
                 f'CI95=[{lo:.6f},{hi:.6f}] fail={2048-k} '
                 f'P_reform={o["P_xright_reform"]:.6f} reform={o["reform_ps"]:.2f}ps '
                 f'xfinal={o["mean_x_final"]:+.5f}+-{o["sigma_x_final"]:.5f} '
                 f'coldReg=({o["cold_reg_x"]:.3f},{o["cold_reg_u"]:.3f})')
            print(msg); print(f'::notice title=Experiment 03 one-loop boundary capture::{msg}')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot; fd.CASES[.6]=original; nf.CASES[.6]=original

if __name__=='__main__': main()
