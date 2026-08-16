#!/usr/bin/env python3
"""Common-random-number comparison of the safe interior tilt optimum.

Independent N=1024 screens located a turnover between delta=.212 and .213, but
seed-to-seed binomial variation is large enough to obscure sub-0.001 tilt
increments.  This worker removes that avoidable ranking noise:

* each tilt solves its own reduced dark root
    Gamma_per + Gamma_th = 1e-6 /s;
* all tilts use the same stochastic seed at a given absorber area;
* N=4096 trajectories are propagated for 2 ns at common areas near the P=.99
  boundary.

Because run_case is deterministic for a given seed/model, the random initial
and bath variates are paired across tilts.  Marginal binomial Wilson intervals
are still reported, but the main purpose is a lower-variance *between-design*
comparison before the final single-point certification run.
"""
from __future__ import annotations

import argparse, math

import full_dynamic_rfsquid as fd
import nonlinear_fdt_twa_screen as nf
from nonlinear_fdt_twa_convergence import wilson
from quantum_initial_capture import quantum_covariance
import safe_tilt_optimum_worker as sw

C0=215e-15; R0=80.; L0=111.5e-12; ALPHA=.90
AREAS=(490.,495.,500.)
SEEDS={490.:7724901,495.:7724951,500.:7725001}
NTRAJ=4096


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--delta',type=float,required=True); a=ap.parse_args()
    d=round(a.delta,5)
    if d not in (.21200,.21225,.21250,.21275,.21300):
        raise SystemExit('supported: .21200,.21225,.21250,.21275,.21300')
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT; original=fd.CASES[.6]
    try:
        root,G,s,gt=sw.solve_root(d)
        C=C0*root*root; R=R0/root
        hdr=(f'delta={d:.5f} r_dark={root:.10f} C={C*1e12:.6f}pF R={R:.7f}ohm '
             f'fc={s["st"]["wc"]/(2*math.pi)*1e-9:.7f}GHz Bper={s["B"]:.9f} '
             f'Gper={s["Gamma"]:.9e}/s Gth={gt["Gamma"]:.9e}/s Gtotal={G:.9e}/s '
             f'nneg={s["nneg"]} CRN=yes N={NTRAJ}')
        print(hdr); print(f'::notice title=Experiment 03 CRN dark root::{hdr}')
        if s['nneg']!=1 or s['zero_overlap']<.999:
            raise RuntimeError('dark saddle mode regression failed')

        fd.BETA_COLD=.80; fd.DELTA_TILT=d
        fd.CASES[.6]=(L0,C,original[2]); nf.CASES[.6]=fd.CASES[.6]
        model=fd.DynamicForce(.6,quick=False,Tmax=1.02)
        fold=model.fold_temperature(hi=.98)
        wc=quantum_covariance(model,.6)['omega_c']
        print(f'capture_model fold={fold:.8f}K fc={wc/(2*math.pi)*1e-9:.7f}GHz')
        for A in AREAS:
            o=nf.run_case(model,14.,R=R,alpha=ALPHA,ntraj=NTRAJ,dt_ps=.125,tpost_ns=2.0,
                          seed=SEEDS[A],area_um2=A,rise_ps=20.)
            k=int(o['n_right_final']); lo,hi=wilson(k,NTRAJ)
            msg=(f'delta={d:.5f} A={A:g}um2 seed={SEEDS[A]}: '
                 f'P_final={o["P_right_final"]:.8f} CI95=[{lo:.8f},{hi:.8f}] '
                 f'fail={NTRAJ-k} P_reform={o["P_xright_reform"]:.8f} '
                 f'reform={o["reform_ps"]:.2f}ps xfinal={o["mean_x_final"]:+.6f}+-{o["sigma_x_final"]:.6f}')
            print(msg); print(f'::notice title=Experiment 03 CRN safe-tilt capture::{msg}')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot; fd.CASES[.6]=original; nf.CASES[.6]=original

if __name__=='__main__': main()
