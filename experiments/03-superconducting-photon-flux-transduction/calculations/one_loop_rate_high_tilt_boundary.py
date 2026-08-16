#!/usr/bin/env python3
"""Probe the high-tilt termination of the calibrated one-loop dark-rate manifold.

For delta=.211-.214, scan the exact finite-T periodic-instanton + calibrated
one-loop rate as the electrical similarity scale r approaches the exact
sphaleron crossover scale r_x=Tx_base/T0.

We seek the first downward crossing

    Gamma_1loop(delta,r)=1e-6 /s.

The ordinary Gaussian periodic-instanton prefactor is nonuniform as r->r_x, so
results with T0/Tx > .92 are explicitly classified as soft-mode provisional.
If no downward crossing occurs before .94 of the distance to r_x from the lower
scan point, the point is not accepted and requires uniform crossover theory.
"""
from __future__ import annotations

import argparse, math
import numpy as np
from scipy.optimize import brentq

import full_dynamic_rfsquid as fd
import finiteT_nonlocal_periodic_bounce_v2 as ft2
import finiteT_one_loop_rate_manifold as rm

TARGET=1e-6
LOGT=math.log(TARGET)
C0=215e-15; R0=80.0


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--delta',type=float,required=True); a=ap.parse_args()
    d=round(a.delta,3)
    if d not in (.211,.212,.213,.214): raise SystemExit('supported: .211 .212 .213 .214')
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    try:
        stbase=ft2.static_model(d,C0,R0)
        Txbase,_=ft2.exact_crossover(stbase)
        rx=Txbase/fd.T0
        print(f'delta={d:.3f}: Txbase={Txbase:.8f}K r_x={rx:.8f}')

        # Start below the known .21 rate solution; if Gamma is already below
        # target, move lower until the physical descending branch is bracketed.
        rlo=min(8.5,.72*rx)
        slo=rm.rate_state(d,rlo,40,5120)
        while np.isfinite(slo.get('Gamma',np.nan)) and slo['Gamma']<TARGET and rlo>2.0:
            rlo*=.90
            slo=rm.rate_state(d,rlo,40,5120)
        if not np.isfinite(slo.get('Gamma',np.nan)):
            raise RuntimeError('lower scan point is not a periodic instanton')
        print(f'lower r={rlo:.8f}: Gamma={slo["Gamma"]:.6e}/s B={slo["B"]:.7f} T0/Tx={fd.T0/slo["Tx"]:.6f}')

        rmax=rlo+.965*(rx-rlo)
        grid=np.linspace(rlo,rmax,12)
        pts=[]
        for r in grid:
            s=rm.rate_state(d,float(r),40,5120)
            pts.append((float(r),s))
            if np.isfinite(s.get('Gamma',np.nan)):
                print(f'scan r={r:.8f}: Gamma={s["Gamma"]:.6e}/s B={s["B"]:.7f} T0/Tx={fd.T0/s["Tx"]:.6f}')
            else:
                print(f'scan r={r:.8f}: kind={s["kind"]} B={s["B"]:.7f}')

        brackets=[]
        for (ra,sa),(rb,sb) in zip(pts[:-1],pts[1:]):
            if not np.isfinite(sa.get('logGamma',np.nan)) or not np.isfinite(sb.get('logGamma',np.nan)):
                continue
            fa=sa['logGamma']-LOGT; fb=sb['logGamma']-LOGT
            if fa*fb<=0 and fa>0:
                brackets.append((ra,rb))
        if not brackets:
            finite=[p for p in pts if np.isfinite(p[1].get('Gamma',np.nan))]
            best=min(finite,key=lambda z:z[1]['Gamma'])
            msg=(f'delta={d:.3f}: NO_ACCEPTED_ROOT; min_scan_Gamma={best[1]["Gamma"]:.6e}/s '
                 f'at r={best[0]:.8f}, T0/Tx={fd.T0/best[1]["Tx"]:.6f}; '
                 f'r_x={rx:.8f}. Uniform soft-mode treatment required.')
            print(msg); print(f'::warning title=Experiment 03 one-loop high-tilt boundary::{msg}')
            print('PASS_NO_ROOT')
            return

        lo,hi=brackets[0]
        cache={}
        def f(r):
            key=round(float(r),10)
            if key not in cache: cache[key]=rm.rate_state(d,float(r),40,5120)
            return cache[key]['logGamma']-LOGT
        rs=brentq(f,lo,hi,xtol=3e-5,rtol=2e-6,maxiter=35)
        sf=rm.rate_state(d,rs,80,10240)
        ratio=fd.T0/sf['Tx']
        C=C0*rs*rs; R=R0/rs
        status='ACCEPT_GAUSSIAN' if ratio<=.92 else 'SOFT_MODE_PROVISIONAL'
        msg=(f'delta={d:.3f}: r_rate={rs:.8f} C={C*1e15:.3f}fF R={R:.6f}ohm '
             f'fc={sf["st"]["wc"]/(2*math.pi)*1e-9:.6f}GHz B20={sf["B"]:.7f} '
             f'A1={sf["A"]:.6e}/s Gamma={sf["Gamma"]:.6e}/s '
             f'Tx={sf["Tx"]:.8f}K T0/Tx={ratio:.6f} r_x={rx:.8f} status={status}')
        print(msg); print(f'::notice title=Experiment 03 one-loop high-tilt root::{msg}')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot

if __name__=='__main__': main()
