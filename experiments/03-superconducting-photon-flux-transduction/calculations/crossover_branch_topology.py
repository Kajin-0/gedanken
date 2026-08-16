#!/usr/bin/env python3
"""Map stationary periodic branches near the first Matsubara crossover.

The production finite-T solver seeds at 0.94 Tx and selects the lowest-action
one-negative-mode periodic solution.  Near Tx this need not be the branch born
continuously from the sphaleron if multiple branches exist.

This diagnostic solves independently at fixed T/Tx from many first-harmonic
seed amplitudes, clusters stationary solutions by path amplitude/action, and
reports Morse index.  It is designed to distinguish:
  (i) supercritical continuous bifurcation;
  (ii) subcritical / first-order branch structure;
  (iii) continuation/seed artifact.
"""
from __future__ import annotations
import argparse, math
import numpy as np

import full_dynamic_rfsquid as fd
import finiteT_nonlocal_periodic_bounce as ft
import finiteT_nonlocal_periodic_bounce_v2 as ft2

C0=215e-15; R0=80.0
R_REF={.212:10.62175909,.213:11.19986413,.214:11.49729617}
TRATIOS=(0.9995,0.998,0.995,0.990,0.980,0.960,0.940)
FRACS=(1e-5,3e-5,1e-4,3e-4,1e-3,3e-3,1e-2,2e-2,4e-2,7e-2,.12,.20,.32,.48,.70)


def cluster(rows):
    out=[]
    for q in sorted(rows,key=lambda z:(z['amp'],z['B'])):
        if any(abs(q['amp']-p['amp'])<2e-5 and abs(q['B']-p['B'])<2e-5 for p in out):
            continue
        out.append(q)
    return out


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--delta',type=float,required=True); a=ap.parse_args()
    d=round(a.delta,3)
    if d not in R_REF: raise SystemExit(f'unsupported delta={d}')
    r=R_REF[d]; C=C0*r*r; R=R0/r
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    try:
        st=ft2.static_model(d,C,R); Tx,_=ft2.exact_crossover(st)
        ys=st['xs']-st['xm']; scale=max(st['xr']-st['xs'],st['xs']-st['xm'])
        print(f'delta={d:.3f} r={r:.9f} Tx={Tx:.9f}K')
        for tr in TRATIOS:
            T=tr*Tx
            sys=ft.periodic_system(st,T,48,6144)
            Bsph=st['barrierK']/T
            rows=[]
            # Include exact sphaleron explicitly.
            a0=np.zeros(49); a0[0]=ys
            os=ft.solve_stationary(sys,a0)
            rows.append(dict(seed=0.0,amp=0.0,B=float(os['B']),nneg=int(np.sum(os['ev']<0)),grad=os['grad'],success=os['success']))
            for frac in FRACS:
                for sgn in (+1.,-1.):
                    aa=np.zeros(49); aa[0]=ys; aa[1]=sgn*frac*scale
                    o=ft.solve_stationary(sys,aa,maxfev=16000)
                    path=sys['B']@o['a']
                    amp=.5*(float(np.max(path))-float(np.min(path)))
                    rows.append(dict(seed=sgn*frac,amp=amp,B=float(o['B']),nneg=int(np.sum(o['ev']<0)),grad=o['grad'],success=o['success']))
            good=[q for q in rows if q['success'] and q['grad']<2e-7]
            sols=cluster(good)
            print(f'Tratio={tr:.4f} T={T:.9f}K Bsph={Bsph:.9f} sph_nneg={int(np.sum(os["ev"]<0))} nsol={len(sols)}')
            for j,q in enumerate(sols):
                print(f'  sol{j}: amp={q["amp"]:.9e} B={q["B"]:.9f} DeltaBsph={Bsph-q["B"]:+.9e} nneg={q["nneg"]} seed={q["seed"]:+.5g} grad={q["grad"]:.2e}')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot

if __name__=='__main__': main()
