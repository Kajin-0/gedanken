#!/usr/bin/env python3
"""Numerical regression of the exact finite-temperature electrical similarity.

For fixed static potential and normalized two-pole bath topology,

    C -> r^2 C0,  R -> R0/r,  omega_D -> omega_D/r

implies after tau=r*u

    B(T; r) = r * B_base(r*T).

The same relation gives Tx(r)=Tx_base/r and reproduces the r-independent
sphaleron action automatically.  This script verifies the identity on the full
finite-period nonlocal saddle, including periodic-instanton continuation.
"""
from __future__ import annotations
import argparse
import full_dynamic_rfsquid as fd
import finiteT_nonlocal_periodic_bounce as ft
import finiteT_nonlocal_periodic_bounce_v2 as ft2

C0=215e-15; R0=80.0
RTEST={
    .180:(4.956202,5.06585901),
    .200:(6.812623,7.19167228),
    .210:(8.233320,9.23549568),
}


def action(st,T,nb=40,ng=5120):
    Tx,_=ft2.exact_crossover(st)
    out=ft.finiteT_bounce(st,T,Tx,nb,ng)
    return float(out['o']['B']),Tx,out['kind']


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--delta',type=float,required=True); a=ap.parse_args()
    d=round(a.delta,3)
    if d not in RTEST: raise SystemExit(f'unsupported delta {d}')
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    try:
        for r in RTEST[d]:
            st_scaled=ft2.static_model(d,C0*r*r,R0/r)
            Bs,Txs,ks=action(st_scaled,fd.T0)
            st_base=ft2.static_model(d,C0,R0)
            Bb,Txb,kb=action(st_base,r*fd.T0)
            pred=r*Bb
            txpred=Txb/r
            msg=(f'delta={d:.3f} r={r:.9f}: Bscaled={Bs:.9f} '
                 f'rBbase(rT)={pred:.9f} relB={Bs/pred-1:+.3e}; '
                 f'Txscaled={Txs:.9f}K Txbase/r={txpred:.9f}K relTx={Txs/txpred-1:+.3e}; '
                 f'kind_scaled={ks} kind_base={kb}')
            print(msg); print(f'::notice title=Experiment 03 finiteT similarity::{msg}')
            if abs(Bs/pred-1)>2e-6 or abs(Txs/txpred-1)>2e-10:
                raise RuntimeError('finite-T electrical similarity regression failed')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot

if __name__=='__main__': main()
