#!/usr/bin/env python3
"""Fast strict-CRN gate for the three leading safe-tilt candidates at A=500 um^2.

This imports the fixed-prehistory implementation from
`safe_tilt_strict_crn_pairwise.py` but limits the comparison to

    delta = .21200, .21250, .21275
    N = 1024
    A = 500 um^2.

The purpose is only to decide whether the coarse `.21250` maximum survives a
proper paired stochastic comparison while the larger N=2048/three-area study is
running.
"""
from __future__ import annotations

import math, numpy as np
from scipy.stats import binomtest

import full_dynamic_rfsquid as fd
import nonlinear_fdt_twa_screen as nf
import safe_tilt_optimum_worker as sw
import safe_tilt_strict_crn_pairwise as sc
from nonlinear_fdt_twa_convergence import wilson

DELTAS=(.21200,.21250,.21275)
ROOTS={.21250:10.885578211,.21275:11.035674041}
AREA=500.; N=1024; SEED=9945001


def main():
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT; original=fd.CASES[.6]
    oldN=sc.NTRAJ
    try:
        sc.NTRAJ=N
        r212,_,_,_=sw.solve_root(.21200); roots={.21200:r212,**ROOTS}
        designs=[]
        for d in DELTAS:
            designs.append(sc.make_design(d,roots[d])); fd.CASES[.6]=original; nf.CASES[.6]=original
        tpre=12*max(z['tau'] for z in designs); dt=sc.DT_PS*1e-12
        tpre=math.ceil(tpre/dt)*dt
        print(f'quick strict CRN A={AREA:g}um2 N={N} seed={SEED} common_tpre={tpre*1e9:.6f}ns')
        outs={}
        for z in designs:
            fd.BETA_COLD=.80; fd.DELTA_TILT=z['delta']; fd.CASES[.6]=(sc.L0,z['C'],original[2]); nf.CASES[.6]=fd.CASES[.6]
            o=sc.run_fixed(z,AREA,tpre,SEED); outs[z['delta']]=o
            lo,hi=wilson(N-o['failures'],N)
            print(f'delta={z["delta"]:.5f}: P={o["P"]:.8f} CI95=[{lo:.8f},{hi:.8f}] '
                  f'fail={o["failures"]} Preform={o["Preform"]:.8f} coldReg=({o["coldRegX"]:.4f},{o["coldRegU"]:.4f})')
        for x,y in ((.21200,.21250),(.21250,.21275),(.21200,.21275)):
            n10,n01,diff,se,p=sc.paired(outs[x]['labels'],outs[y]['labels'])
            msg=(f'pair {x:.5f}->{y:.5f}: dP={diff:+.8f} pairedSE={se:.8f} '
                 f'gain={n10} loss={n01} discord={n10+n01} McNemarP={p:.6g}')
            print(msg); print(f'::notice title=Experiment 03 quick strict CRN::{msg}')
        print('PASS')
    finally:
        sc.NTRAJ=oldN; fd.BETA_COLD=ob; fd.DELTA_TILT=ot; fd.CASES[.6]=original; nf.CASES[.6]=original

if __name__=='__main__': main()
