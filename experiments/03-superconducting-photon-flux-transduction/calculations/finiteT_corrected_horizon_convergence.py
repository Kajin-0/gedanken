#!/usr/bin/env python3
"""Post-pulse horizon convergence for the corrected finite-T capture frontier.

The nonlinear TWA screen historically used tpost=0.50 ns.  On the corrected
high-tilt B20=37.61 manifold the phase clock slows to only a few GHz, so the
'final basin' at 0.5 ns may not represent asymptotic commitment.

Test tpost = 0.5, 1.0, 2.0 ns at representative near-threshold areas for
corrected delta=.18,.20,.21 designs.  The reformation probability and final
basin probability are both reported.  This is a numerical convergence gate on
the semiclassical screen, not a physical quantum-efficiency calculation.
"""
from __future__ import annotations
import argparse, math
import full_dynamic_rfsquid as fd
import nonlinear_fdt_twa_screen as nf
from nonlinear_fdt_twa_convergence import wilson
from quantum_initial_capture import quantum_covariance

R20={.180:5.06585901,.200:7.19167228,.210:9.23549568}
AREA={.180:330.,.200:430.,.210:560.}
C0=215e-15; R0=80.; L0=111.5e-12; ALPHA=.90


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--delta',type=float,required=True); a=ap.parse_args()
    d=round(a.delta,3)
    if d not in R20: raise SystemExit(f'unsupported delta {d}')
    r=R20[d]; C=C0*r*r; R=R0/r; A=AREA[d]
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT; original=fd.CASES[.6]
    try:
        fd.BETA_COLD=.80; fd.DELTA_TILT=d
        fd.CASES[.6]=(L0,C,original[2]); nf.CASES[.6]=fd.CASES[.6]
        model=fd.DynamicForce(.6,quick=False,Tmax=1.02)
        wc=quantum_covariance(model,.6)['omega_c']
        print(f'delta={d:.3f} r20={r:.8f} A={A:g}um2 fc={wc/(2*math.pi)*1e-9:.6f}GHz')
        for tpost in (.50,1.00,2.00):
            o=nf.run_case(model,14.,R=R,alpha=ALPHA,ntraj=1024,dt_ps=.125,
                          tpost_ns=tpost,seed=771000+int(1000*d),area_um2=A,rise_ps=20.)
            k=int(o['n_right_final']); lo,hi=wilson(k,1024)
            msg=(f'tpost={tpost:.2f}ns: P_final={o["P_right_final"]:.6f} '
                 f'CI95=[{lo:.6f},{hi:.6f}] P_reform={o["P_xright_reform"]:.6f} '
                 f'reform={o["reform_ps"]:.2f}ps xfinal={o["mean_x_final"]:+.5f}+-{o["sigma_x_final"]:.5f} '
                 f'coldReg=({o["cold_reg_x"]:.3f},{o["cold_reg_u"]:.3f})')
            print(msg); print(f'::notice title=Experiment 03 horizon convergence::{msg}')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot; fd.CASES[.6]=original; nf.CASES[.6]=original

if __name__=='__main__': main()
