#!/usr/bin/env python3
"""Spectral/basis convergence of the 20-mK periodic nonlocal bounce.

Evaluate the corrected B20=37.61 design scales at representative high tilts
with several cosine-basis/grid resolutions.  The sphaleron identity is already
an exact quadrature regression; this file checks the nontrivial periodic saddle
action itself.
"""
from __future__ import annotations
import argparse
import full_dynamic_rfsquid as fd
import finiteT_nonlocal_periodic_bounce as ft
import finiteT_nonlocal_periodic_bounce_v2 as ft2

R20={.180:5.06585901,.200:7.19167228,.210:9.23549568}
C0=215e-15; R0=80.
RES=((32,4096),(40,5120),(48,6144),(64,8192))


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--delta',type=float,required=True); a=ap.parse_args()
    d=round(a.delta,3)
    if d not in R20: raise SystemExit(f'unsupported delta {d}')
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    old_static,old_cross=ft.static_model,ft.exact_crossover
    try:
        ft.static_model=ft2.static_model; ft.exact_crossover=ft2.exact_crossover
        r=R20[d]; C=C0*r*r; R=R0/r
        st=ft2.static_model(d,C,R); Tx,_=ft2.exact_crossover(st)
        vals=[]
        for nb,ng in RES:
            out=ft.finiteT_bounce(st,fd.T0,Tx,nb,ng)
            o=out['o']; nneg=int((o['ev']<0).sum())
            vals.append(float(o['B']))
            msg=(f'delta={d:.3f} nbasis={nb} ngrid={ng}: B20={o["B"]:.9f} '
                 f'kind={out["kind"]} Tx={Tx:.8f}K nneg={nneg} grad={o["grad"]:.3e}')
            print(msg); print(f'::notice title=Experiment 03 finiteT convergence::{msg}')
            if nneg!=1 or o['grad']>2e-6: raise RuntimeError('saddle regression failed')
        ref=vals[-1]
        print('relative_to_64: '+', '.join(f'{nb}:{B/ref-1:+.3e}' for (nb,ng),B in zip(RES,vals)))
        if abs(vals[-2]/ref-1)>5e-4: raise RuntimeError('48->64 action not converged to 5e-4')
        print('PASS')
    finally:
        ft.static_model=old_static; ft.exact_crossover=old_cross
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot

if __name__=='__main__': main()
