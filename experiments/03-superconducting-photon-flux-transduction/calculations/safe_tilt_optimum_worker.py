#!/usr/bin/env python3
"""Resolve the interior high-fidelity optimum between delta=.212 and .213.

The coarse one-loop-rate-constrained capture frontier rises through delta=.212
but falls by delta=.213.  Both points lie below their finite-amplitude periodic-
instanton folds, so this turnover can be optimized without invoking the unresolved
fold-uniform rate theory.

For each requested tilt this worker:
  1. solves the same-environment reduced dark constraint

       Gamma_per(T0,r) + Gamma_th(T0,r) = 1e-6 /s

     on the regular one-negative periodic branch below local Tx;
  2. verifies that the root remains below local Tx (the implementation domain of
     rate_state; the actual physical Gaussian singularity is the later fold);
  3. runs an identical 14-um, 20-ps-rise, 2-ns, N=1024 capture screen on a common
     absorber-area grid.

This is a design-screening optimization only.  Capture is still sym-FDT TWA and
the dark rate omits competing quasiparticle/vortex/stray-photon channels.
"""
from __future__ import annotations

import argparse, math
import numpy as np
from scipy.optimize import brentq

import full_dynamic_rfsquid as fd
import finiteT_one_loop_rate_manifold as rm
import first_order_total_rate_manifold as fo
import nonlinear_fdt_twa_screen as nf
from nonlinear_fdt_twa_convergence import wilson
from quantum_initial_capture import quantum_covariance

TARGET=1e-6
C0=215e-15; R0=80.; L0=111.5e-12; ALPHA=.90
AREAS=(480.,490.,500.,510.,520.)


def dark_total(delta,r,nb=40,ng=5120):
    s=rm.rate_state(delta,r,nb,ng)
    if s['kind']!='periodic':
        return None,s,None
    gt=fo.thermal_rate(s['st'])
    return s['Gamma']+gt['Gamma'],s,gt


def solve_root(delta):
    # These tilts have their target root in this conservative bracket and below
    # local Tx.  Scan first rather than assuming monotonicity.
    grid=np.linspace(10.3,11.55,11)
    vals=[]
    for r in grid:
        G,s,gt=dark_total(delta,float(r),32,4096)
        if G is not None:
            vals.append((float(r),math.log(G/TARGET)))
    br=None
    for a,b in zip(vals[:-1],vals[1:]):
        if a[1]>=0 and b[1]<=0:
            br=(a[0],b[0]); break
    if br is None:
        raise RuntimeError(f'no descending dark-rate bracket for delta={delta}: {vals}')
    def f(r):
        G,_,_=dark_total(delta,float(r),40,5120)
        if G is None: raise RuntimeError('root entered unsupported post-Tx branch')
        return math.log(G/TARGET)
    root=brentq(f,*br,xtol=2e-7,rtol=2e-8,maxiter=50)
    G,s,gt=dark_total(delta,root,64,8192)
    if G is None: raise RuntimeError('high-resolution root lost periodic saddle')
    # One correction step using local derivative if basis shift moved the rate.
    eps=2e-3
    Gp,_,_=dark_total(delta,root+eps,48,6144)
    Gm,_,_=dark_total(delta,root-eps,48,6144)
    deriv=(math.log(Gp)-math.log(Gm))/(2*eps)
    root2=root-math.log(G/TARGET)/deriv
    G2,s2,gt2=dark_total(delta,root2,72,9216)
    if G2 is None: raise RuntimeError('corrected root lost periodic saddle')
    return root2,G2,s2,gt2


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--delta',type=float,required=True); a=ap.parse_args()
    d=round(a.delta,5)
    if d not in (.21225,.21250,.21275): raise SystemExit('supported: .21225,.21250,.21275')
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT; original=fd.CASES[.6]
    try:
        root,G,s,gt=solve_root(d)
        C=C0*root*root; R=R0/root
        # rate_state uses the same static model; report local Tx only as an
        # implementation-domain diagnostic, not as the physical fold boundary.
        hdr=(f'delta={d:.5f} r_dark={root:.9f} C={C*1e12:.6f}pF R={R:.7f}ohm '
             f'fc={s["st"]["wc"]/(2*math.pi)*1e-9:.7f}GHz Bper={s["B"]:.8f} '
             f'Gper={s["Gamma"]:.8e}/s Gth={gt["Gamma"]:.8e}/s '
             f'Gtotal={G:.8e}/s T0/Tx={fd.T0/s["Tx"]:.6f} nneg={s["nneg"]}')
        print(hdr); print(f'::notice title=Experiment 03 narrow safe dark root::{hdr}')
        if s['nneg']!=1 or s['zero_overlap']<.999:
            raise RuntimeError('dark saddle mode regression failed')

        fd.BETA_COLD=.80; fd.DELTA_TILT=d
        fd.CASES[.6]=(L0,C,original[2]); nf.CASES[.6]=fd.CASES[.6]
        model=fd.DynamicForce(.6,quick=False,Tmax=1.02)
        fold=model.fold_temperature(hi=.98)
        wc=quantum_covariance(model,.6)['omega_c']
        print(f'capture_model fold={fold:.7f}K fc={wc/(2*math.pi)*1e-9:.7f}GHz')
        for A in AREAS:
            o=nf.run_case(model,14.,R=R,alpha=ALPHA,ntraj=1024,dt_ps=.125,tpost_ns=2.0,
                          seed=6120000+int(round(d*1e5)),area_um2=A,rise_ps=20.)
            k=int(o['n_right_final']); lo,hi=wilson(k,1024)
            msg=(f'delta={d:.5f} A={A:g}um2: P_final={o["P_right_final"]:.6f} '
                 f'CI95=[{lo:.6f},{hi:.6f}] fail={1024-k} '
                 f'P_reform={o["P_xright_reform"]:.6f} reform={o["reform_ps"]:.2f}ps '
                 f'xfinal={o["mean_x_final"]:+.5f}+-{o["sigma_x_final"]:.5f}')
            print(msg); print(f'::notice title=Experiment 03 narrow safe capture::{msg}')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot; fd.CASES[.6]=original; nf.CASES[.6]=original

if __name__=='__main__': main()
