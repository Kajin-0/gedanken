#!/usr/bin/env python3
"""Resolve the shallow delta=.210-.212 capture optimum at high statistics.

All points use the calibrated Gaussian one-loop dark-rate roots satisfying
Gamma_1loop(20 mK)=1e-6/s, the same 14-um photon, 20-ps rise, dt=.125 ps,
and a 2-ns final classification horizon.

A common absorber-area grid and common base seed are used across deltas to
reduce irrelevant Monte-Carlo mismatch in the pairwise comparison.  A second
independent seed is run at the three central areas as an audit against an
accidental common-random-number realization.

Capture remains a symmetrized-FDT TWA screening quantity, not exact quantum
photodetection efficiency.
"""
from __future__ import annotations
import argparse, math
import full_dynamic_rfsquid as fd
import nonlinear_fdt_twa_screen as nf
from nonlinear_fdt_twa_convergence import wilson
from quantum_initial_capture import quantum_covariance

R_RATE={.210:9.825701561,.211:10.18791311,.212:10.62175909}
AREAS=(472.,476.,480.,484.,488.,492.)
AUDIT=(476.,484.,492.)
C0=215e-15; R0=80.; L0=111.5e-12; ALPHA=.90
NMAIN=8192; NAUDIT=4096


def run_grid(model,d,R,areas,ntraj,seed,label):
    for A in areas:
        o=nf.run_case(model,14.,R=R,alpha=ALPHA,ntraj=ntraj,dt_ps=.125,
                      tpost_ns=2.0,seed=seed,area_um2=A,rise_ps=20.)
        k=int(o['n_right_final']); lo,hi=wilson(k,ntraj)
        msg=(f'{label} delta={d:.3f} A={A:g}um2 N={ntraj} seed={seed}: '
             f'P_final={o["P_right_final"]:.8f} CI95=[{lo:.8f},{hi:.8f}] '
             f'fail={ntraj-k} P_reform={o["P_xright_reform"]:.8f} '
             f'reform={o["reform_ps"]:.2f}ps xfinal={o["mean_x_final"]:+.6f}+-{o["sigma_x_final"]:.6f}')
        print(msg); print(f'::notice title=Experiment 03 plateau highstat::{msg}')


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--delta',type=float,required=True); a=ap.parse_args()
    d=round(a.delta,3)
    if d not in R_RATE: raise SystemExit(f'unsupported delta={d}')
    r=R_RATE[d]; C=C0*r*r; R=R0/r
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT; original=fd.CASES[.6]
    try:
        fd.BETA_COLD=.80; fd.DELTA_TILT=d
        fd.CASES[.6]=(L0,C,original[2]); nf.CASES[.6]=fd.CASES[.6]
        model=fd.DynamicForce(.6,quick=False,Tmax=1.02)
        fold=model.fold_temperature(hi=.98)
        wc=quantum_covariance(model,.6)['omega_c']
        hdr=(f'delta={d:.3f} r_rate={r:.9f} C={C*1e15:.3f}fF R={R:.6f}ohm '
             f'fold={fold:.6f}K fc={wc/(2*math.pi)*1e-9:.6f}GHz '
             f'Nmain={NMAIN} Naudit={NAUDIT}')
        print(hdr); print(f'::notice title=Experiment 03 plateau design::{hdr}')
        # Same seed across all deltas is intentional common-random-number coupling.
        run_grid(model,d,R,AREAS,NMAIN,5210212,'MAIN')
        run_grid(model,d,R,AUDIT,NAUDIT,7310212,'AUDIT')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot; fd.CASES[.6]=original; nf.CASES[.6]=original

if __name__=='__main__': main()
