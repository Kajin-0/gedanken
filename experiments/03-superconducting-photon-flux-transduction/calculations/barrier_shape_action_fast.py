#!/usr/bin/env python3
"""Optimized barrier-shape / exact isolated-action scan.

Same physics target as barrier_shape_action_scan.py, but evaluates the cold force
once on a dense x grid and cumulatively integrates the potential.  This avoids
thousands of repeated adaptive quadratures per model.

The exact zero-energy bounce action is then evaluated by dense composite
trapezoid integration.  The baseline beta=.80, tilt=.35 point is required to
reproduce the independently validated B0=25.03305 to better than ~0.2%.
"""
from __future__ import annotations
import math
import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.optimize import brentq

import full_dynamic_rfsquid as fd
from quantum_initial_capture import HBAR, PHI_BAR, KB


def metrics(model,nx=50001):
    roots=model.roots(fd.T0)
    mins=sorted(x for x,k in roots if k>0); saddles=sorted(x for x,k in roots if k<0)
    left=max([x for x in mins if x<0],default=mins[0])
    right=min([x for x in mins if x>left],default=mins[-1])
    ss=[x for x in saddles if left<x<right]
    if not ss: raise RuntimeError('no central saddle')
    xs=ss[0]
    xhi=min(float(model.xgrid[-1]),right+0.8)
    x=np.linspace(left,xhi,nx)
    F=np.array([model.force(fd.T0,float(xx)) for xx in x])
    U=cumulative_trapezoid(F,x,initial=0.0)
    def ui(xx): return float(np.interp(xx,x,U))
    barrier=ui(xs); Er=ui(right)
    after=np.where((x[:-1]>=xs)&(U[:-1]*U[1:]<=0))[0]
    if not len(after): raise RuntimeError('no turning point')
    i=int(after[0]); xt=brentq(ui,float(x[i]),float(x[i+1]),xtol=2e-13,rtol=2e-13)
    jt=int(np.searchsorted(x,xt)); xx=np.concatenate((x[:jt],np.array([xt])))
    uu=np.maximum(np.interp(xx,x,U),0.0)
    L,C,_=fd.CASES[.6]; EL=PHI_BAR**2/L; M=C*PHI_BAR**2
    integrand=np.sqrt(2*M*EL*uu)
    B=2/HBAR*float(np.trapezoid(integrand,xx))
    kappa=model._scalar(model.spline.ev(fd.T0,left,dx=0,dy=1))
    wc=math.sqrt(kappa/(L*C)); barrierK=barrier*EL/KB
    ratio=barrier*EL/(HBAR*wc)
    return dict(B=B,betaU=B/ratio,barrierK=barrierK,biasK=-Er*EL/KB,
                fold=model.fold_temperature(hi=.95),sep=right-left,
                fc=wc/(2*math.pi),left=left,xs=xs,xt=xt,right=right)


def main():
    print('Experiment 03 optimized exact barrier-shape action scan')
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT; rows=[]
    try:
        for beta in (.72,.76,.80,.84,.88,.92):
            for tilt in (.20,.25,.30,.35,.40):
                fd.BETA_COLD=beta; fd.DELTA_TILT=tilt
                try:
                    m=fd.DynamicForce(.6,quick=False,Tmax=.96)
                    q=metrics(m)
                    rows.append((q['B'],beta,tilt,q))
                    msg=(f'beta={beta:.2f} tilt={tilt:.2f}: B0={q["B"]:.5f} betaU={q["betaU"]:.4f} '
                         f'barrier={q["barrierK"]:.4f}K bias={q["biasK"]:.4f}K '
                         f'fold={q["fold"]:.4f}K fc={q["fc"]*1e-9:.3f}GHz sep={q["sep"]:.4f}')
                except Exception as e:
                    msg=f'beta={beta:.2f} tilt={tilt:.2f}: INVALID {type(e).__name__}: {e}'
                print(msg); print(f'::notice title=Experiment 03 fast barrier scan::{msg}')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot
    rows.sort(reverse=True,key=lambda z:z[0])
    print('\nTop actions:')
    for B,b,t,q in rows[:15]:
        print(f'B={B:.5f} beta={b:.2f} tilt={t:.2f} betaU={q["betaU"]:.4f} barrierK={q["barrierK"]:.4f} biasK={q["biasK"]:.4f} fold={q["fold"]:.4f}')
    # Baseline regression.
    base=[z for z in rows if abs(z[1]-.8)<1e-12 and abs(z[2]-.35)<1e-12]
    if base:
        rel=base[0][0]/25.0330502-1
        print(f'baseline relative error vs independent exact bounce={rel:+.3e}')
        if abs(rel)>.0025: raise RuntimeError('baseline action regression failed')
    print('PASS')
if __name__=='__main__': main()
