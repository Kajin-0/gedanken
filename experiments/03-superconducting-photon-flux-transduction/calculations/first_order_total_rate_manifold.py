#!/usr/bin/env python3
"""Branch-aware dark-rate manifold through the first-order quantum/thermal crossover.

The physical one-negative-mode periodic instanton persists above the sphaleron's
local n=1 Matsubara-instability scale r_x.  The actual action crossing occurs at
r_c>r_x and remains finite-amplitude.  Therefore the old `rate_state()` hard
switch at r_x is invalid in this region.

This script works directly at the physical bath T0=20 mK and continues the same
periodic saddle as the electrical scale r increases.  At each point it computes

    Gamma_per = A_1loop exp(-B_per)

using the UV-corrected, cubic-calibrated determinant, and independently computes
the generalized memory-friction thermal rate

    Gamma_th = (omega_m/2pi)(lambda_b/omega_b) exp(-DeltaU/kBT0),

with

    C lambda_b^2 + lambda_b Y_L(lambda_b) + F_s/L = 0.

Because the first-order saddles are distinct, the screening total is taken as

    Gamma_total = Gamma_per + Gamma_th

where the periodic branch exists.  The target is the first descending crossing
Gamma_total=1e-6/s.  If the periodic branch folds before the crossing, the
thermal branch alone is checked.

This remains a reduced-model dark rate: competing quasiparticle, vortex,
stray-photon and technical-flux channels are not included.
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
from R80_dissipative_bounce_screen import Y_laplace

C0=215e-15; R0=80.; L0=111.5e-12
TARGET=1e-6


def thermal_rate(st):
    C,R=st['C'],st['R']
    wm=st['wc']
    wb=math.sqrt(-st['Fs']/(L0*C))
    def f(z):
        return C*z*z + z*float(Y_laplace(z,R,st['wd'])) + st['Fs']/L0
    hi=max(10*wb,10*wm,1e9)
    while f(hi)<=0: hi*=2
    lb=brentq(f,0.0,hi,xtol=1e-4,rtol=1e-12,maxiter=300)
    A=wm/(2*math.pi)*(lb/wb)
    B=st['barrierK']/fd.T0
    return dict(A=A,B=B,Gamma=A*math.exp(-B),lb=lb,wb=wb)


def periodic_rate(st,sys,o,nbasis):
    q=da.orthonormal_hessians(st,sys,o)
    tail,_,_=uv.uv_tail(st,sys,o,nbasis)
    logD=q['logD']+tail
    logA=math.log(st['wc']) + .5*math.log(q['Is']/(2*math.pi)) + logD
    B=float(o['B'])
    return dict(A=math.exp(logA),B=B,Gamma=math.exp(logA-B),logD=logD,
                Is=q['Is'],zero=q['zero_overlap'])


def scan(delta,nbasis=40,ngrid=5120):
    # Local linear crossover at the unscaled reference; similarity gives r_x.
    base=ft2.static_model(delta,C0,R0)
    Txbase,_=ft2.exact_crossover(base)
    rx=Txbase/fd.T0
    r0=.88*rx
    st=ft2.static_model(delta,C0*r0*r0,R0/r0)
    Tx,_=ft2.exact_crossover(st)
    out=ft.finiteT_bounce(st,fd.T0,Tx,nbasis,ngrid)
    if out['kind']!='periodic': raise RuntimeError('failed to seed periodic branch')
    sys,o=out['sys'],out['o']

    # Dense enough to bracket the rate root and action crossing; continuation
    # stops itself if the finite-amplitude branch folds/collapses.
    rs=np.unique(np.concatenate([
        np.linspace(r0,.98*rx,7),
        np.linspace(.99*rx,1.01*rx,9),
        np.linspace(1.015*rx,1.08*rx,14),
    ]))
    rows=[]
    for r in rs:
        r=float(r)
        if abs(r-r0)<1e-12:
            ns, no=st,o; nsys=sys
        else:
            ns=ft2.static_model(delta,C0*r*r,R0/r)
            nsys=ft.periodic_system(ns,fd.T0,nbasis,ngrid)
            a0=ft.project_coeffs(sys,o['a'],nsys)
            no=ft.solve_stationary(nsys,a0,maxfev=12000)
            amp=math.sqrt(float(np.sum((no['a'][1:]**2)*nsys['norms'][1:])))
            nneg=int(np.sum(no['ev']<0))
            if (not no['success']) or no['grad']>3e-6 or nneg!=1 or amp<1e-4:
                print(f'BRANCH_STOP r={r:.9f} r/rx={r/rx:.6f} success={no["success"]} '
                      f'grad={no["grad"]:.3e} nneg={nneg} amp={amp:.6e}')
                break
        amp=math.sqrt(float(np.sum((no['a'][1:]**2)*nsys['norms'][1:])))
        gp=periodic_rate(ns,nsys,no,nbasis)
        gt=thermal_rate(ns)
        total=gp['Gamma']+gt['Gamma']
        Bs=gt['B']
        row=dict(r=r,rrx=r/rx,st=ns,sys=nsys,o=no,amp=amp,gp=gp,gt=gt,total=total,
                 actiondiff=gp['B']-Bs)
        rows.append(row)
        print(f'r={r:.9f} r/rx={r/rx:.6f} fc={ns["wc"]/(2*math.pi)*1e-9:.6f}GHz '
              f'Bper={gp["B"]:.8f} Bsph={Bs:.8f} dB={row["actiondiff"]:+.6e} '
              f'Gper={gp["Gamma"]:.6e}/s Gth={gt["Gamma"]:.6e}/s Gtot={total:.6e}/s '
              f'amp={amp:.6e} zero={gp["zero"]:.9f}')
        st,sys,o=ns,nsys,no

    if not rows: raise RuntimeError('empty branch scan')
    # First descending target bracket.
    target_br=None
    for a,b in zip(rows[:-1],rows[1:]):
        if a['total']>=TARGET and b['total']<=TARGET:
            target_br=(a,b); break
    # First action crossing.
    act_br=None
    for a,b in zip(rows[:-1],rows[1:]):
        if a['actiondiff']<=0 and b['actiondiff']>=0:
            act_br=(a,b); break

    if target_br:
        a,b=target_br
        # log-linear interpolation is a locator only; a follow-up refinement can
        # recompute the exact branch point once the design region is known.
        ya=math.log(a['total']/TARGET); yb=math.log(b['total']/TARGET)
        w=-ya/(yb-ya)
        rt=a['r']+w*(b['r']-a['r'])
        status='PERIODIC_SIDE' if (act_br is None or rt<act_br[1]['r']) else 'NEAR_OR_AFTER_ACTION_CROSSING'
        tmsg=f'target_r~{rt:.8f} target_bracket=[{a["r"]:.8f},{b["r"]:.8f}] status={status}'
    else:
        # Thermal-only algebraic asymptote if needed: Gth=A0/r*exp(-B).
        last=rows[-1]
        tmsg=f'NO_PERIODIC_TARGET_BRACKET last_Gtot={last["total"]:.6e}/s at r={last["r"]:.8f}'
    if act_br:
        a,b=act_br
        w=-a['actiondiff']/(b['actiondiff']-a['actiondiff'])
        rc=a['r']+w*(b['r']-a['r'])
        amsg=f'action_rc~{rc:.8f} action_bracket=[{a["r"]:.8f},{b["r"]:.8f}]'
    else:
        amsg='NO_ACTION_CROSSING_IN_VALID_BRANCH_SCAN'
    msg=f'delta={delta:.3f} rx={rx:.8f}; {tmsg}; {amsg}'
    print(msg); print(f'::notice title=Experiment 03 branch-aware total dark rate::{msg}')
    print('PASS')
    return rows


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--delta',type=float,required=True); a=ap.parse_args()
    d=round(a.delta,3)
    if d not in (.213,.214,.215,.216,.217,.218): raise SystemExit('supported: .213-.218')
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    try: scan(d)
    finally: fd.BETA_COLD=ob; fd.DELTA_TILT=ot

if __name__=='__main__': main()
