#!/usr/bin/env python3
"""Equal-dark-action high-tilt capture frontier at delta=.09,.10,.11.

Uses exact same-environment nonlocal actions from the validated continuation and
restores B_target=37.61 via the exact electrical similarity.  The physical
14-um / 20-ps graphene thermal pulse remains unchanged.

All probabilities are symmetrized-FDT TWA screening values only.
"""
from __future__ import annotations
import argparse, math
import full_dynamic_rfsquid as fd
import nonlinear_fdt_twa_screen as nf
from nonlinear_fdt_twa_convergence import wilson
from quantum_initial_capture import quantum_covariance

B_TARGET=37.61
B_DISS={.090:20.6166869,.100:18.7650379,.110:17.0395912}
AREA_GRID={
 .090:(116.,120.,124.,128.,132.),
 .100:(122.,128.,134.,140.,146.),
 .110:(128.,136.,144.,152.,160.),
}
C0=215e-15; R0=80.; L0=111.5e-12; ALPHA=.90

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--delta',type=float,required=True); a=ap.parse_args()
    delta=round(a.delta,3)
    if delta not in B_DISS: raise SystemExit(f'unsupported delta {delta}')
    r=B_TARGET/B_DISS[delta]; C=C0*r*r; R=R0/r
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT; original=fd.CASES[.6]
    try:
        fd.BETA_COLD=.80; fd.DELTA_TILT=delta
        fd.CASES[.6]=(L0,C,original[2]); nf.CASES[.6]=fd.CASES[.6]
        model=fd.DynamicForce(.6,quick=False,Tmax=1.02)
        fold=model.fold_temperature(hi=.98); cov=quantum_covariance(model,.6); wc=cov['omega_c']
        print(f'delta={delta:.3f} beta=.80 r={r:.9f} C={C*1e15:.3f}fF R={R:.4f}ohm '
              f'fold={fold:.6f}K fc={wc/(2*math.pi)*1e-9:.5f}GHz Btarget={B_TARGET:.5f}')
        for A in AREA_GRID[delta]:
            o=nf.run_case(model,14.,R=R,alpha=ALPHA,ntraj=2048,dt_ps=.125,
                          seed=int(910000+1000*delta),area_um2=A,rise_ps=20.)
            k=int(o['n_right_final']); lo,hi=wilson(k,2048)
            msg=(f'delta={delta:.3f} A={A:g}um2: P_final={o["P_right_final"]:.6f} '
                 f'CI95=[{lo:.6f},{hi:.6f}] fail={2048-k} P_reform={o["P_xright_reform"]:.6f} '
                 f'reform={o["reform_ps"]:.2f}ps coldReg=({o["cold_reg_x"]:.3f},{o["cold_reg_u"]:.3f})')
            print(msg); print(f'::notice title=Experiment 03 high-tilt extension3::{msg}')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot; fd.CASES[.6]=original; nf.CASES[.6]=original
    print('PASS')

if __name__=='__main__': main()
