#!/usr/bin/env python3
"""Photon-capture screen on the corrected finite-temperature dark-action manifold.

The finite-period same-environment Euclidean solver has determined the electrical
scale r20(delta) required to enforce

    B_20mK(delta,r) = 37.61

for delta=.18-.21.  This script uses those independently solved values and
recomputes the 14-um / 20-ps nonlinear capture frontier.

The dark exponent is therefore held at the actual bath temperature rather than
at T=0.  Capture probabilities remain symmetrized-FDT TWA screening quantities,
not exact quantum efficiencies.
"""
from __future__ import annotations

import argparse, math
import full_dynamic_rfsquid as fd
import nonlinear_fdt_twa_screen as nf
from nonlinear_fdt_twa_convergence import wilson
from quantum_initial_capture import quantum_covariance

BT=37.61
R20={
    .180:5.06585901,
    .190:5.95415655,
    .200:7.19167228,
    .210:9.23549568,
}
AREAS={
    .180:(290.,310.,330.,350.,370.),
    .190:(320.,340.,360.,380.,400.),
    .200:(390.,410.,430.,450.,470.),
    .210:(480.,520.,560.,600.,640.),
}
C0=215e-15; R0=80.; L0=111.5e-12; ALPHA=.90


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--delta',type=float,required=True); a=ap.parse_args()
    delta=round(a.delta,3)
    if delta not in R20: raise SystemExit(f'unsupported delta {delta}')
    r=R20[delta]; C=C0*r*r; R=R0/r
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT; original=fd.CASES[.6]
    try:
        fd.BETA_COLD=.80; fd.DELTA_TILT=delta
        fd.CASES[.6]=(L0,C,original[2]); nf.CASES[.6]=fd.CASES[.6]
        model=fd.DynamicForce(.6,quick=False,Tmax=1.02)
        fold=model.fold_temperature(hi=.98)
        cov=quantum_covariance(model,.6); wc=cov['omega_c']
        print(f'delta={delta:.3f} r20={r:.8f} C={C*1e15:.3f}fF R={R:.5f}ohm '
              f'fold={fold:.6f}K fc={wc/(2*math.pi)*1e-9:.6f}GHz B20target={BT:.5f}')
        for A in AREAS[delta]:
            o=nf.run_case(model,14.,R=R,alpha=ALPHA,ntraj=2048,dt_ps=.125,
                          seed=int(2100000+10000*delta),area_um2=A,rise_ps=20.)
            k=int(o['n_right_final']); lo,hi=wilson(k,2048)
            msg=(f'delta={delta:.3f} A={A:g}um2: P_final={o["P_right_final"]:.6f} '
                 f'CI95=[{lo:.6f},{hi:.6f}] fail={2048-k} '
                 f'P_reform={o["P_xright_reform"]:.6f} reform={o["reform_ps"]:.2f}ps '
                 f'coldReg=({o["cold_reg_x"]:.3f},{o["cold_reg_u"]:.3f})')
            print(msg); print(f'::notice title=Experiment 03 corrected finiteT capture::{msg}')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot; fd.CASES[.6]=original; nf.CASES[.6]=original
    print('PASS')

if __name__=='__main__': main()
