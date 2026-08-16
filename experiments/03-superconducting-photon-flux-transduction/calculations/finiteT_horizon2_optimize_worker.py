#!/usr/bin/env python3
"""Matched 2-ns capture optimization on the true B20mK=37.61 manifold.

For each tilt in .200-.210:
  1. solve the finite-period nonlocal Euclidean problem for the electrical scale
     r such that B_20mK(delta,r)=37.61;
  2. use that exact compensated C,R,alpha=.90 design;
  3. run a matched 14-um / 20-ps sym-FDT TWA capture screen with tpost=2 ns.

This removes the three main comparability problems of the earlier frontier:
unequal finite-T dark action, unmatched area grids, and a too-short 0.5-ns
post-pulse classification horizon.

Capture remains a semiclassical screening probability, not an exact quantum
physical efficiency.
"""
from __future__ import annotations
import argparse, math
from scipy.optimize import brentq

import full_dynamic_rfsquid as fd
import finiteT_nonlocal_periodic_bounce as ft
import finiteT_nonlocal_periodic_bounce_v2 as ft2
import nonlinear_fdt_twa_screen as nf
from nonlinear_fdt_twa_convergence import wilson
from quantum_initial_capture import quantum_covariance

BT=37.61
C0=215e-15; R0=80.; L0=111.5e-12; ALPHA=.90
KNOWN_R={.2000:7.19167228,.2100:9.23549568}
AREA_GRID={
 .2000:(405.,415.,425.,435.,445.),
 .2025:(415.,430.,445.,460.,475.),
 .2050:(425.,440.,455.,470.,485.),
 .2075:(435.,450.,465.,480.,495.),
 .2100:(440.,450.,460.,470.,480.),
}


def B20(delta,r,nb=32,ng=4096):
    C=C0*r*r; R=R0/r
    st=ft2.static_model(delta,C,R)
    Tx,_=ft2.exact_crossover(st)
    out=ft.finiteT_bounce(st,fd.T0,Tx,nb,ng)
    return float(out['o']['B']),Tx,out,st


def solve_r(delta):
    d4=round(delta,4)
    if d4 in KNOWN_R:
        return KNOWN_R[d4]
    # Monotone bracket inherited from neighboring exact solutions.
    lo=KNOWN_R[.2000]; hi=KNOWN_R[.2100]
    flo=B20(delta,lo)[0]-BT
    fhi=B20(delta,hi)[0]-BT
    if not (flo<0<fhi):
        raise RuntimeError(f'bad r bracket delta={delta}: f(lo)={flo}, f(hi)={fhi}')
    cache={}
    def f(r):
        key=round(float(r),10)
        if key not in cache: cache[key]=B20(delta,float(r))[0]-BT
        return cache[key]
    r=brentq(f,lo,hi,xtol=2e-5,rtol=2e-6,maxiter=40)
    # 48/6144 final action check.
    B,Tx,out,st=B20(delta,r,48,6144)
    if abs(B-BT)>3e-4 or int((out['o']['ev']<0).sum())!=1:
        raise RuntimeError(f'final B20 check failed delta={delta} r={r} B={B}')
    return r


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--delta',type=float,required=True); a=ap.parse_args()
    delta=round(a.delta,4)
    if delta not in AREA_GRID: raise SystemExit(f'unsupported delta {delta}')
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT; original=fd.CASES[.6]
    try:
        r=solve_r(delta); C=C0*r*r; R=R0/r
        fd.BETA_COLD=.80; fd.DELTA_TILT=delta
        fd.CASES[.6]=(L0,C,original[2]); nf.CASES[.6]=fd.CASES[.6]
        model=fd.DynamicForce(.6,quick=False,Tmax=1.02)
        fold=model.fold_temperature(hi=.98)
        wc=quantum_covariance(model,.6)['omega_c']
        B,Tx,out,st=B20(delta,r,48,6144)
        header=(f'delta={delta:.4f} r20={r:.8f} C={C*1e15:.3f}fF R={R:.5f}ohm '
                f'fold={fold:.6f}K fc={wc/(2*math.pi)*1e-9:.6f}GHz '
                f'B20={B:.7f} Tx={Tx:.7f}K kind={out["kind"]}')
        print(header); print(f'::notice title=Experiment 03 matched 2ns design::{header}')
        for A in AREA_GRID[delta]:
            o=nf.run_case(model,14.,R=R,alpha=ALPHA,ntraj=1024,dt_ps=.125,tpost_ns=2.0,
                          seed=3200000+int(round(10000*delta)),area_um2=A,rise_ps=20.)
            k=int(o['n_right_final']); lo,hi=wilson(k,1024)
            msg=(f'delta={delta:.4f} A={A:g}um2: P_final={o["P_right_final"]:.6f} '
                 f'CI95=[{lo:.6f},{hi:.6f}] fail={1024-k} '
                 f'P_reform={o["P_xright_reform"]:.6f} reform={o["reform_ps"]:.2f}ps '
                 f'xfinal={o["mean_x_final"]:+.5f}+-{o["sigma_x_final"]:.5f} '
                 f'coldReg=({o["cold_reg_x"]:.3f},{o["cold_reg_u"]:.3f})')
            print(msg); print(f'::notice title=Experiment 03 matched 2ns capture::{msg}')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot; fd.CASES[.6]=original; nf.CASES[.6]=original

if __name__=='__main__': main()
