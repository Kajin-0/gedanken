#!/usr/bin/env python3
"""Solve the cubic-calibrated one-loop dark-rate constraint at T0=20 mK.

The preceding work established:

  * the finite-period same-environment periodic-instanton action B20(delta,r);
  * a UV-converged fluctuation determinant;
  * cubic-local calibration of the determinant/collective-coordinate
    normalization.

The reduced-model one-loop rate is therefore

    Gamma_1l(delta,r)
      = omega_c * sqrt(I_s/(2*pi)) * D_raw,corr * exp[-B20],

away from the immediate soft-mode crossover region.

This script solves

    Gamma_1l(delta,r) = 1e-6 /s

for selected tilts.  It replaces the provisional universal exponent constraint
B20=37.61 with a self-consistent tilt-dependent rate constraint.

Important limits:
  - the standard Gaussian one-loop prefactor is nonuniform as T approaches the
    sphaleron crossover and must eventually be replaced by a soft-mode-uniform
    treatment;
  - competing dark channels remain absent;
  - capture remains a separate sym-FDT TWA screen.

Accordingly the solver also reports T0/Tx and refuses to silently cross into the
static-sphaleron regime.
"""
from __future__ import annotations

import argparse, math
import numpy as np
from scipy.optimize import brentq

import full_dynamic_rfsquid as fd
import finiteT_nonlocal_periodic_bounce as ft
import finiteT_nonlocal_periodic_bounce_v2 as ft2
import finiteT_prefactor_determinant_anatomy as da
import finiteT_determinant_uv_tail as uv

C0=215e-15
R0=80.0
GAMMA_TARGET=1e-6
LOG_TARGET=math.log(GAMMA_TARGET)

# Already solved scales that enforce B20=37.61.  They provide the lower bracket
# and make the new rate solve directly comparable with the matched 2-ns capture
# frontier.
R_B20={
    .1800:5.06585901,
    .1900:5.95415655,
    .2000:7.19167228,
    .2025:7.58724523,
    .2050:8.04749146,
    .2075:8.58207176,
    .2100:9.23549568,
}


def rate_state(delta:float,r:float,nbasis:int=48,ngrid:int=6144):
    C=C0*r*r
    R=R0/r
    st=ft2.static_model(delta,C,R)
    Tx,_=ft2.exact_crossover(st)
    if fd.T0>=Tx:
        return dict(kind='sphaleron',Tx=Tx,logGamma=float('nan'),Gamma=float('nan'),
                    B=st['barrierK']/fd.T0,st=st,r=r)
    out=ft.finiteT_bounce(st,fd.T0,Tx,nbasis,ngrid)
    if out['kind']!='periodic':
        return dict(kind=out['kind'],Tx=Tx,logGamma=float('nan'),Gamma=float('nan'),
                    B=float(out['o']['B']),st=st,r=r)
    o=out['o']; sys=out['sys']
    q=da.orthonormal_hessians(st,sys,o)
    tail,_,_=uv.uv_tail(st,sys,o,nbasis)
    logDraw=q['logD']+tail
    logA=math.log(st['wc']) + .5*math.log(q['Is']/(2*math.pi)) + logDraw
    B=float(o['B'])
    logGamma=logA-B
    return dict(kind='periodic',Tx=Tx,logGamma=logGamma,Gamma=math.exp(logGamma),
                B=B,logA=logA,A=math.exp(logA),logDraw=logDraw,Is=q['Is'],
                zero_overlap=q['zero_overlap'],nneg=int((o['ev']<0).sum()),
                grad=o['grad'],st=st,r=r)


def solve(delta:float):
    d=round(delta,4)
    if d not in R_B20:
        raise ValueError(f'no B20 lower bracket for delta={d}')
    rlo=R_B20[d]
    slo=rate_state(d,rlo,40,5120)
    print(f'lower r={rlo:.9f}: B={slo["B"]:.7f} Gamma={slo["Gamma"]:.6e}/s '
          f'T0/Tx={fd.T0/slo["Tx"]:.6f}')
    if not slo['Gamma']>GAMMA_TARGET:
        raise RuntimeError('lower bracket unexpectedly already satisfies rate target')

    # Exact crossover scale from Tx(r)=Tx_base/r.  Evaluate base Tx once and
    # remain below it because the ordinary one-loop periodic prefactor is not
    # uniform at the soft-mode bifurcation.
    stbase=ft2.static_model(d,C0,R0)
    Txbase,_=ft2.exact_crossover(stbase)
    rx=Txbase/fd.T0
    print(f'exact crossover electrical scale r_x={rx:.9f}')

    # Scan toward crossover to detect a root/minimum instead of assuming
    # monotonicity.  The one-loop soft determinant can grow near r_x.
    rmax=rlo + .94*(rx-rlo)
    grid=np.linspace(rlo,rmax,8)
    vals=[]
    for r in grid[1:]:
        s=rate_state(d,float(r),40,5120)
        vals.append((float(r),s))
        print(f'scan r={r:.9f}: B={s["B"]:.7f} Gamma={s["Gamma"]:.6e}/s '
              f'logGamma={s["logGamma"]:.7f} T0/Tx={fd.T0/s["Tx"]:.6f}')

    points=[(rlo,slo)]+vals
    brackets=[]
    for (ra,sa),(rb,sb) in zip(points[:-1],points[1:]):
        fa=sa['logGamma']-LOG_TARGET
        fb=sb['logGamma']-LOG_TARGET
        if np.isfinite(fa) and np.isfinite(fb) and fa*fb<=0:
            brackets.append((ra,rb))
    if not brackets:
        best=min(points,key=lambda z:z[1]['logGamma'])
        raise RuntimeError(
            f'no one-loop rate root before 0.94 r_x; minimum sampled Gamma='
            f'{best[1]["Gamma"]:.6e}/s at r={best[0]:.9f}, '
            f'T0/Tx={fd.T0/best[1]["Tx"]:.6f}; soft-mode uniformization may be required')

    # Use the first downward crossing from the physical low-r branch.
    a,b=brackets[0]
    cache={}
    def f(r):
        key=round(float(r),10)
        if key not in cache:
            cache[key]=rate_state(d,float(r),40,5120)
        return cache[key]['logGamma']-LOG_TARGET
    rstar=brentq(f,a,b,xtol=3e-5,rtol=2e-6,maxiter=35)

    # High-resolution final evaluation. UV correction makes determinant
    # convergence rapid after the leading 1/N tail is removed.
    sf=rate_state(d,rstar,80,10240)
    C=C0*rstar*rstar; R=R0/rstar
    msg=(f'delta={d:.4f}: r_rate={rstar:.9f} C={C*1e15:.3f}fF R={R:.6f}ohm '
         f'fc={sf["st"]["wc"]/(2*math.pi)*1e-9:.6f}GHz '
         f'B20={sf["B"]:.8f} logDraw={sf["logDraw"]:.8f} Is={sf["Is"]:.8f} '
         f'A1={sf["A"]:.6e}/s Gamma1={sf["Gamma"]:.6e}/s '
         f'Tx={sf["Tx"]:.8f}K T0/Tx={fd.T0/sf["Tx"]:.6f} '
         f'r/r_B20={rstar/rlo:.6f} nneg={sf["nneg"]} zeroOverlap={sf["zero_overlap"]:.9f}')
    print(msg); print(f'::notice title=Experiment 03 self-consistent one-loop manifold::{msg}')
    if sf['nneg']!=1 or sf['zero_overlap']<.999 or sf['grad']>2e-6:
        raise RuntimeError('final periodic-saddle regression failed')
    if abs(math.log(sf['Gamma']/GAMMA_TARGET))>.03:
        raise RuntimeError('high-resolution rate differs from target by >3% in log')
    if fd.T0/sf['Tx']>.92:
        print('::warning title=Experiment 03 soft-mode warning::solution is close to finite-T sphaleron crossover; uniform prefactor treatment is mandatory before physical rate use')
    print('PASS')
    return sf


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--delta',type=float,required=True); a=ap.parse_args()
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    try:
        solve(round(a.delta,4))
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot

if __name__=='__main__': main()
