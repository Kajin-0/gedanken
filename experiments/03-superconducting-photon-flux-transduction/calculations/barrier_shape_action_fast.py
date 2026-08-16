#!/usr/bin/env python3
"""Optimized exact barrier-shape / isolated-action scan near the LIVE baseline.

CRITICAL baseline synchronization
---------------------------------
The current canonical force model in `full_dynamic_rfsquid.py` uses

    DELTA_TILT = 0.05
    BETA_COLD  = 0.80
    LAMBDA_MIX = 0.590.

An earlier exploratory scan accidentally used a stale handoff value and searched
tilt=.20-.40.  Those rankings are NOT applicable to the current detector.
This corrected scan is centered on the live low-tilt operating point and requires
(beta=.80, tilt=.05) to reproduce the independently validated exact isolated
bounce action B0=25.0330502.

Physics target
--------------
The current R80 dark failure is partly a barrier-shape problem: the exact
isolated bounce exponent is ~25 rather than the cubic estimate ~38.  Scan the two
static rf-SQUID controls

    beta_cold : screening/Josephson-force scale
    delta     : directional linear tilt

and compute the exact zero-energy isolated bounce action, barrier height, local
phase frequency, fold temperature, well-energy directionality and phase-state
separation.

This is a static/dark screen only.  A larger B0 is not automatically a better
photon detector; promising points must retain enough directional bias and then
survive the full finite-pulse causal capture calculation.
"""
from __future__ import annotations
import math
import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.optimize import brentq

import full_dynamic_rfsquid as fd
from quantum_initial_capture import HBAR, PHI_BAR, KB

BASE_B=0.80
BASE_TILT=0.05
BASE_ACTION=25.0330502


def metrics(model,nx=60001):
    roots=model.roots(fd.T0)
    mins=sorted(x for x,k in roots if k>0)
    saddles=sorted(x for x,k in roots if k<0)
    if len(mins)<2:
        raise RuntimeError('not bistable')

    # The live family uses the adjacent left/right pair straddling zero.
    lefts=[x for x in mins if x<0]
    rights=[x for x in mins if x>0]
    if not lefts or not rights:
        raise RuntimeError('no minima straddling zero')
    left=max(lefts); right=min(rights)
    ss=[x for x in saddles if left<x<right]
    if not ss:
        raise RuntimeError('no central saddle')
    xs=ss[0]

    xhi=min(float(model.xgrid[-1]),right+1.0)
    x=np.linspace(left,xhi,nx)
    F=np.array([model.force(fd.T0,float(xx)) for xx in x])
    U=cumulative_trapezoid(F,x,initial=0.0)
    def ui(xx): return float(np.interp(xx,x,U))

    barrier=ui(xs)
    Er=ui(right)
    if barrier<=0:
        raise RuntimeError('nonpositive barrier')

    # First zero-energy turning point beyond the central saddle.
    mask=np.where(x[:-1]>=xs)[0]
    ids=[i for i in mask if U[i]>0 and U[i+1]<=0]
    if not ids:
        # Also allow an exact/tiny numerical sign crossing.
        ids=[i for i in mask if U[i]*U[i+1]<=0 and x[i]>xs+1e-6]
    if not ids:
        raise RuntimeError('no turning point')
    i=int(ids[0])
    xt=brentq(ui,float(x[i]),float(x[i+1]),xtol=2e-13,rtol=2e-13)

    jt=int(np.searchsorted(x,xt))
    xx=np.concatenate((x[:jt],np.array([xt])))
    uu=np.maximum(np.interp(xx,x,U),0.0)

    L,C,_=fd.CASES[.6]
    EL=PHI_BAR**2/L
    M=C*PHI_BAR**2
    B=2/HBAR*float(np.trapezoid(np.sqrt(2*M*EL*uu),xx))

    kappa=model._scalar(model.spline.ev(fd.T0,left,dx=0,dy=1))
    wc=math.sqrt(kappa/(L*C))
    barrierK=barrier*EL/KB
    action_ratio=barrier*EL/(HBAR*wc)
    betaU=B/action_ratio
    biasK=-Er*EL/KB  # positive => right well lower than left
    fold=model.fold_temperature(hi=.95)

    return dict(B=B,betaU=betaU,barrierK=barrierK,biasK=biasK,
                fold=fold,sep=right-left,fc=wc/(2*math.pi),
                left=left,xs=xs,xt=xt,right=right,kappa=kappa,
                action_ratio=action_ratio)


def main():
    print('Experiment 03 corrected LIVE barrier-shape/action scan')
    print(f'live regression baseline beta={BASE_B:.2f}, tilt={BASE_TILT:.3f}, expected B0={BASE_ACTION:.7f}')
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    rows=[]
    betas=(.70,.75,.80,.85,.90,.95,1.00)
    tilts=(.020,.035,.050,.065,.080,.100,.120)
    try:
        for beta in betas:
            for tilt in tilts:
                fd.BETA_COLD=float(beta)
                fd.DELTA_TILT=float(tilt)
                try:
                    m=fd.DynamicForce(.6,quick=False,Tmax=.96)
                    q=metrics(m)
                    rows.append((q['B'],beta,tilt,q))
                    msg=(f'beta={beta:.2f} tilt={tilt:.3f}: B0={q["B"]:.6f} '
                         f'betaU={q["betaU"]:.4f} barrier={q["barrierK"]:.4f}K '
                         f'biasRlower={q["biasK"]:.4f}K fold={q["fold"]:.4f}K '
                         f'fc={q["fc"]*1e-9:.3f}GHz sep={q["sep"]:.4f}rad')
                except Exception as e:
                    msg=f'beta={beta:.2f} tilt={tilt:.3f}: INVALID {type(e).__name__}: {e}'
                print(msg)
                print(f'::notice title=Experiment 03 live barrier scan::{msg}')
    finally:
        fd.BETA_COLD=ob
        fd.DELTA_TILT=ot

    rows.sort(reverse=True,key=lambda z:z[0])
    print('\nTop exact isolated actions in the live low-tilt neighborhood:')
    for B,b,t,q in rows[:18]:
        print(f'B={B:.6f} beta={b:.2f} tilt={t:.3f} betaU={q["betaU"]:.4f} '
              f'barrierK={q["barrierK"]:.4f} biasK={q["biasK"]:.4f} '
              f'fold={q["fold"]:.4f} fc={q["fc"]*1e-9:.3f}GHz')

    base=[z for z in rows if abs(z[1]-BASE_B)<1e-12 and abs(z[2]-BASE_TILT)<1e-12]
    if len(base)!=1:
        raise RuntimeError('live baseline was not evaluated exactly once')
    rel=base[0][0]/BASE_ACTION-1
    print(f'baseline B={base[0][0]:.7f}; relative error vs independent exact bounce={rel:+.3e}')
    if abs(rel)>.003:
        raise RuntimeError('live baseline action regression failed')
    print('PASS')

if __name__=='__main__': main()
