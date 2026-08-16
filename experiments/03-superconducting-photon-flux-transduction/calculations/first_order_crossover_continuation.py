#!/usr/bin/env python3
"""Continue the dominant finite-amplitude periodic bounce through the local sphaleron instability.

Branch-topology scans show coexistence near the first-Matsubara sphaleron
stability boundary: a tiny branch merges continuously into the sphaleron, while
a distinct finite-amplitude one-negative-mode periodic bounce has substantially
lower action.  Therefore Lambda_1=0 is only a local bifurcation, not the physical
action crossover.

This script follows the large one-negative-mode branch from T/Tx=.94 upward,
including T>Tx, and locates the first action equality

    B_large(T*) = B_sph(T*)

while both competing saddles have the correct Morse index.  That is the
candidate first-order quantum/thermal action crossover.
"""
from __future__ import annotations
import argparse, math
import numpy as np

import full_dynamic_rfsquid as fd
import finiteT_nonlocal_periodic_bounce as ft
import finiteT_nonlocal_periodic_bounce_v2 as ft2

C0=215e-15; R0=80.0
R_REF={.210:9.825701561,.211:10.18791311,.212:10.62175909,.213:11.19986413,.214:11.49729617}


def seed_large(st,Tx,nb=48,ng=6144):
    T=.94*Tx; sys=ft.periodic_system(st,T,nb,ng)
    ys=st['xs']-st['xm']; scale=max(st['xr']-st['xs'],st['xs']-st['xm'])
    rows=[]
    for frac in (.12,.20,.32,.48,.70,1.0):
        for sgn in (+1.,-1.):
            a=np.zeros(nb+1); a[0]=ys; a[1]=sgn*frac*scale
            o=ft.solve_stationary(sys,a,maxfev=20000)
            path=sys['B']@o['a']; amp=.5*(float(np.max(path))-float(np.min(path)))
            if o['success'] and o['grad']<3e-7 and int(np.sum(o['ev']<0))==1 and amp>.04:
                rows.append((o,amp))
    if not rows: raise RuntimeError('failed to seed finite-amplitude one-negative branch')
    o,amp=min(rows,key=lambda z:z[0]['B'])
    return T,sys,o,amp


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--delta',type=float,required=True); a=ap.parse_args()
    d=round(a.delta,3)
    if d not in R_REF: raise SystemExit(f'unsupported delta={d}')
    r=R_REF[d]; C=C0*r*r; R=R0/r
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    try:
        st=ft2.static_model(d,C,R); Tx,_=ft2.exact_crossover(st)
        T,sys,o,amp=seed_large(st,Tx)
        print(f'delta={d:.3f} r={r:.9f} local_Tx={Tx:.9f}K seed_amp={amp:.9e}')
        # Dense across local bifurcation, then wider upward search.
        ratios=np.concatenate([
            np.arange(.945,1.051,0.0025),
            np.arange(1.055,1.151,0.005),
            np.arange(1.16,1.301,0.01),
        ])
        prev=None; crossing=None
        for tr in ratios:
            Tn=float(tr*Tx); ns=ft.periodic_system(st,Tn,48,6144)
            a0=ft.project_coeffs(sys,o['a'],ns)
            no=ft.solve_stationary(ns,a0,maxfev=20000)
            path=ns['B']@no['a']; amp=.5*(float(np.max(path))-float(np.min(path)))
            nneg=int(np.sum(no['ev']<0)); Bsph=st['barrierK']/Tn
            diff=float(no['B']-Bsph)
            # exact sphaleron Morse index for interpretation
            ss,so,sex=ft.sphaleron(st,Tn,48,6144)
            sn=int(np.sum(so['ev']<0))
            msg=(f'Tratio={tr:.4f} T={Tn:.9f}K amp={amp:.9e} Blarge={no["B"]:.9f} '
                 f'Bsph={Bsph:.9f} Blarge-Bsph={diff:+.9e} large_nneg={nneg} '
                 f'sph_nneg={sn} success={no["success"]} grad={no["grad"]:.2e}')
            print(msg); print(f'::notice title=Experiment 03 first-order continuation::{msg}')
            if (not no['success']) or no['grad']>2e-6 or amp<1e-4:
                print('BRANCH_TERMINATED_OR_LOST')
                break
            if prev is not None and prev[1]<0<=diff and nneg==1 and sn==1:
                # linear interpolation is only a bracket estimate; a refined root follows in a separate gate if needed.
                t0,f0=prev; tc=t0+(tr-t0)*(-f0)/(diff-f0)
                crossing=(tc,prev[0],tr,f0,diff)
                print(f'ACTION_CROSSING_BRACKET tr=[{prev[0]:.6f},{tr:.6f}] estimate={tc:.9f}')
                break
            prev=(tr,diff)
            sys,o=ns,no
        if crossing is None:
            print('NO_ACTION_CROSSING_FOUND_IN_CONTINUED_RANGE')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot

if __name__=='__main__': main()
