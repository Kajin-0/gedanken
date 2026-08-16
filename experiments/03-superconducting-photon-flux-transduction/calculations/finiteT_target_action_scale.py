#!/usr/bin/env python3
"""Solve the electrical compensation required for B(T0)=37.61.

The earlier high-tilt family imposed B(T=0)=37.61.  The validated finite-period
solver shows thermal/periodic-instanton effects reduce the actual 20-mK action.
This script therefore solves, for each static tilt,

    B_20mK(delta, r) = 37.61

under the same exact electrical similarity family

    C = r^2 C0, R = R0/r, alpha = omega_D/omega_c = .90.

The finite-T action is obtained from the one-negative-mode periodic saddle below
the exact dissipative crossover, or the static sphaleron above it.

This still does NOT provide a physical DCR because the fluctuation determinant
and competing dark channels remain unresolved.
"""
from __future__ import annotations

import argparse
import math
from scipy.optimize import brentq

import full_dynamic_rfsquid as fd
import finiteT_nonlocal_periodic_bounce as ft
import finiteT_nonlocal_periodic_bounce_v2 as ft2

BT=37.61
C0=215e-15; R0=80.0
BZERO_BASE={.180:7.58847205,.190:6.52571286,.200:5.52063406,.210:4.56802352}


def action_at(delta:float,r:float,nbasis:int=40,ngrid:int=5120,verbose:bool=False):
    C=C0*r*r; R=R0/r
    st=ft2.static_model(delta,C,R)
    Tx,_=ft2.exact_crossover(st)
    out=ft.finiteT_bounce(st,fd.T0,Tx,nbasis,ngrid)
    B=float(out['o']['B'])
    if verbose:
        print(f'  r={r:.9f}: B20={B:.8f} kind={out["kind"]} Tx={Tx:.7f}K '
              f'fc={st["wc"]/(2*math.pi)*1e-9:.6f}GHz nneg={int((out["o"]["ev"]<0).sum())}')
    return B,Tx,out,st


def solve(delta:float):
    if delta not in BZERO_BASE:
        raise ValueError(f'missing zero-T base action at delta={delta}')
    r0=BT/BZERO_BASE[delta]
    B0,_,_,_=action_at(delta,r0,verbose=True)
    if B0>=BT:
        raise RuntimeError('unexpected: zero-T target scale already exceeds finite-T target')

    # The static sphaleron action is the r->large upper ceiling.  Grow the
    # bracket only while the physical action remains below target.
    rhi=r0*1.08
    Bhi,_,_,_=action_at(delta,rhi,verbose=True)
    while Bhi<BT and rhi<100:
        rhi*=1.12
        Bhi,_,_,_=action_at(delta,rhi,verbose=True)
    if Bhi<BT:
        raise RuntimeError(f'no finite r reaches B20={BT}; last r={rhi} B={Bhi}')

    cache={}
    def f(r):
        key=round(float(r),12)
        if key not in cache:
            cache[key]=action_at(delta,float(r),verbose=False)[0]
        return cache[key]-BT
    rstar=brentq(f,r0,rhi,xtol=2e-5,rtol=2e-6,maxiter=40)
    # Final publication-screen evaluation at the established 48/6144 resolution.
    B48,Tx,out,st=action_at(delta,rstar,nbasis=48,ngrid=6144,verbose=True)
    C=C0*rstar*rstar; R=R0/rstar
    msg=(f'delta={delta:.3f}: r20={rstar:.8f} C={C*1e15:.3f}fF R={R:.5f}ohm '
         f'fc={st["wc"]/(2*math.pi)*1e-9:.6f}GHz Tx={Tx:.7f}K '
         f'B20_48={B48:.7f} target={BT:.5f} kind={out["kind"]} '
         f'nneg={int((out["o"]["ev"]<0).sum())}')
    print(msg); print(f'::notice title=Experiment 03 B20 target scale::{msg}')
    return rstar,B48


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--delta',type=float,required=True); a=ap.parse_args()
    delta=round(a.delta,3)
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    try:
        solve(delta)
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot

if __name__=='__main__': main()
