#!/usr/bin/env python3
"""High-stat capture certification for the engineering representative delta=.212.

Strict fixed-history paired comparisons over delta=.21200-.21300 found no
statistically resolved fine-tilt winner at A=490,495,500 um^2.  The lower-tilt
edge delta=.212 is therefore selected as the engineering representative because
it has the smallest compensated C, highest phase clock and best fixed-design
flux-noise tolerance within the statistically flat capture band.

This worker no longer ranks tilts.  It estimates the 14-um capture frontier for
that single representative at its self-consistent reduced dark-rate root using
N=8192 trajectories and reports both the central probability and 95% Wilson
interval.  The intended outputs are:

  A99_point   -- central-probability crossing near P=.99;
  A99_95lower -- largest tested area whose Wilson lower bound is >=.99.

Capture remains a symmetrized-FDT truncated-Wigner screening quantity, not exact
physical quantum efficiency.
"""
from __future__ import annotations

import argparse, math

import full_dynamic_rfsquid as fd
import nonlinear_fdt_twa_screen as nf
from nonlinear_fdt_twa_convergence import wilson
import safe_tilt_optimum_worker as sw

DELTA=.21200
NTRAJ=8192
DT_PS=.125
TPOST_NS=2.0
AREAS=(470.,475.,480.,485.,490.)
SEEDS={470.:9214701,475.:9214751,480.:9214801,485.:9214851,490.:9214901}
C0=215e-15; R0=80.; L0=111.5e-12; ALPHA=.90


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--area',type=float,required=True); a=ap.parse_args()
    area=float(a.area)
    if area not in AREAS: raise SystemExit(f'supported areas: {AREAS}')
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT; original=fd.CASES[.6]
    try:
        root,G,s,gt=sw.solve_root(DELTA)
        C=C0*root*root; R=R0/root
        fd.BETA_COLD=.80; fd.DELTA_TILT=DELTA
        fd.CASES[.6]=(L0,C,original[2]); nf.CASES[.6]=fd.CASES[.6]
        model=fd.DynamicForce(.6,quick=False,Tmax=1.02)
        fold=model.fold_temperature(hi=.98)
        out=nf.run_case(model,14.,R=R,alpha=ALPHA,ntraj=NTRAJ,dt_ps=DT_PS,
                        tpost_ns=TPOST_NS,seed=SEEDS[area],area_um2=area,rise_ps=20.)
        k=int(out['n_right_final']); lo,hi=wilson(k,NTRAJ)
        msg=(f'delta={DELTA:.5f} area={area:g}um2 N={NTRAJ} seed={SEEDS[area]} '
             f'r_dark={root:.10f} C={C*1e12:.6f}pF R={R:.7f}ohm '
             f'fc={s["st"]["wc"]/(2*math.pi)*1e-9:.7f}GHz fold={fold:.7f}K '
             f'Gper={s["Gamma"]:.9e}/s Gth={gt["Gamma"]:.9e}/s Gtotal={G:.9e}/s '
             f'P_final={out["P_right_final"]:.8f} CI95=[{lo:.8f},{hi:.8f}] '
             f'fail={NTRAJ-k} P_reform={out["P_xright_reform"]:.8f} '
             f'reform={out["reform_ps"]:.2f}ps coldReg=({out["cold_reg_x"]:.4f},{out["cold_reg_u"]:.4f}) '
             f'xfinal={out["mean_x_final"]:+.6f}+-{out["sigma_x_final"]:.6f} '
             f'WilsonLower_ge_0p99={lo>=.99}')
        print(msg); print(f'::notice title=Experiment 03 delta212 certification::{msg}')
        if s['nneg']!=1 or s['zero_overlap']<.999:
            raise RuntimeError('dark saddle mode regression failed')
        if not (.94<out['cold_reg_x']<1.06 and .94<out['cold_reg_u']<1.06):
            raise RuntimeError('cold covariance regression outside 6%')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot; fd.CASES[.6]=original; nf.CASES[.6]=original

if __name__=='__main__': main()
