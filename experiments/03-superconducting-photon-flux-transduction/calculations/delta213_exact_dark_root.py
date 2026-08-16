#!/usr/bin/env python3
"""Refine the crossover-independent delta=.213 dark-rate root.

At this tilt the 1e-6/s crossing lies below the local Matsubara instability and,
more importantly, below the first-order action crossing and periodic-instanton
fold.  The old rule rejecting T0/Tx > .94 is obsolete: direct continuation has
shown that the physical finite-amplitude one-negative branch survives through
local Tx and becomes singular only at its later saddle-node fold.

We solve

    Gamma_per(r) + Gamma_th(r) = 1e-6 /s

with the cubic-calibrated UV-corrected periodic prefactor and independent
same-environment memory-friction thermal rate.  A separate fold-continuation
workflow supplies the actual distance from this root to the periodic fold.
"""
from __future__ import annotations

import math
from scipy.optimize import brentq

import full_dynamic_rfsquid as fd
import finiteT_one_loop_rate_manifold as rm
import first_order_total_rate_manifold as fo

DELTA=.213
TARGET=1e-6


def total(r,nb=64,ng=8192,verbose=False):
    s=rm.rate_state(DELTA,r,nb,ng)
    if s['kind']!='periodic': raise RuntimeError('root left pre-Tx implementation domain')
    gt=fo.thermal_rate(s['st'])
    G=s['Gamma']+gt['Gamma']
    if verbose:
        print(f'r={r:.10f} Bper={s["B"]:.10f} Aper={s["A"]:.9e}/s '
              f'Gper={s["Gamma"]:.9e}/s Gth={gt["Gamma"]:.9e}/s Gtot={G:.9e}/s '
              f'T0/Tx={fd.T0/s["Tx"]:.8f} nneg={s["nneg"]} zero={s["zero_overlap"]:.10f}')
    return G,s,gt


def main():
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    try:
        def f(r): return math.log(total(r,48,6144)[0]/TARGET)
        lo,hi=11.12,11.28
        flo,fhi=f(lo),f(hi)
        if flo*fhi>0: raise RuntimeError(f'bad bracket f(lo)={flo} f(hi)={fhi}')
        root=brentq(f,lo,hi,xtol=2e-9,rtol=2e-10,maxiter=80)
        G,s,gt=total(root,72,9216,True)
        G2,s2,gt2=total(root,88,11264,True)
        rel=abs(G2-G)/TARGET
        C=s2['st']['C']; R=s2['st']['R']; fc=s2['st']['wc']/(2*math.pi)
        msg=(f'delta=.213 exact_root_r={root:.10f} C={C*1e12:.6f}pF R={R:.7f}ohm '
             f'fc={fc*1e-9:.7f}GHz Bper={s2["B"]:.9f} Gper={s2["Gamma"]:.9e}/s '
             f'Gth={gt2["Gamma"]:.9e}/s Gtotal={G2:.9e}/s '
             f'basis_rate_shift_over_target={rel:.3e} T0/Tx={fd.T0/s2["Tx"]:.7f}')
        print(msg); print(f'::notice title=Experiment 03 delta213 exact dark root::{msg}')
        if abs(math.log(G2/TARGET))>2e-3: raise RuntimeError('high-basis root moved >0.2% in rate')
        if s2['nneg']!=1 or s2['zero_overlap']<.999999:
            raise RuntimeError('periodic saddle mode regression failed')
        print('NOTE: local T0/Tx is diagnostic only; physical Gaussian-validity margin is set by the later periodic fold.')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot

if __name__=='__main__': main()
