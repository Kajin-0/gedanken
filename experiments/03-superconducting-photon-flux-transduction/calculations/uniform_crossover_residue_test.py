#!/usr/bin/env python3
"""Test first-crossover pole-residue cancellation for the dissipative uniform rate.

For a consistent first-orbit uniformization, as the electrical scale approaches
its exact crossover value from the periodic-instanton side,

 |Gamma_pb| /
 [Gamma_inst * exp(-DeltaB)/sqrt(4*pi*DeltaB)] -> 1.

This is a normalization test, not a dark-rate prediction.  It directly checks
whether the signed dissipative parabolic-barrier pole has the residue required
to cancel the instanton-side singular term.
"""
from __future__ import annotations
import argparse, math

import full_dynamic_rfsquid as fd
import finiteT_nonlocal_periodic_bounce_v2 as ft2
import finiteT_one_loop_rate_manifold as rm
import uniform_rate_first_orbit_probe as ur

C0=215e-15; R0=80.0
EPS=(0.10,0.06,0.04,0.025,0.015,0.010,0.006,0.004)


def one(delta,r):
    s=rm.rate_state(delta,r,64,8192)
    if s['kind']!='periodic': raise RuntimeError('expected periodic instanton')
    st=s['st']; Binst=float(s['B']); Ginst=float(s['Gamma'])
    Bsph=st['barrierK']/fd.T0; gap=Bsph-Binst
    sign,logP,wm,wb=ur.signed_log_product(st,fd.T0,N=100000)
    lb=ur.barrier_growth(st)
    logabs_pb=math.log(wm/(2*math.pi))+math.log(lb/wb)-Bsph+logP
    Gpb=sign*math.exp(logabs_pb)
    cancel=Ginst*math.exp(-gap)/math.sqrt(4*math.pi*gap)
    return dict(Gpb=Gpb,cancel=cancel,ratio=abs(Gpb)/cancel,gap=gap,Ginst=Ginst,
                Tfrac=fd.T0/s['Tx'],Binst=Binst,Bsph=Bsph)


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--delta',type=float,required=True); a=ap.parse_args()
    d=round(a.delta,3)
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    try:
        # r_x follows exactly from Tx(r)=Tx_base/r.  Compute unscaled Tx.
        st0=ft2.static_model(d,C0,R0)
        Tx0,_=ft2.exact_crossover(st0)
        rx=Tx0/fd.T0
        print(f'delta={d:.3f} Tx0={Tx0:.9f}K r_x={rx:.9f}')
        rows=[]
        for eps in EPS:
            r=rx*(1-eps)
            q=one(d,r); rows.append((eps,q))
            msg=(f'delta={d:.3f} eps={eps:.4f} r={r:.9f} T0/Tx={q["Tfrac"]:.9f} '
                 f'DeltaB={q["gap"]:.9e} Gamma_inst={q["Ginst"]:.6e}/s '
                 f'Gamma_pb={q["Gpb"]:+.6e}/s cancel={q["cancel"]:.6e}/s '
                 f'residue_ratio={q["ratio"]:.9f}')
            print(msg); print(f'::notice title=Experiment 03 uniform residue::{msg}')
        # Require the closest point to be substantially closer to unity than the farthest.
        e0=abs(rows[0][1]['ratio']-1); e1=abs(rows[-1][1]['ratio']-1)
        print(f'residue_error_far={e0:.6e} residue_error_near={e1:.6e}')
        if not e1 < e0:
            raise RuntimeError('pole-residue ratio does not converge toward unity')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot

if __name__=='__main__': main()
