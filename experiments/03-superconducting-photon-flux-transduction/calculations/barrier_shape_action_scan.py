#!/usr/bin/env python3
"""Exact isolated-bounce scan versus rf-SQUID static barrier-shape controls.

The current R80 dark failure is driven partly by barrier shape: the exact
isolated action is B~25 rather than the cubic estimate ~38.  This script asks
whether changing the *static* normalized rf-SQUID potential can increase the
zero-T Euclidean action without first slowing the electrical circuit.

Scanned controls
----------------
- BETA_COLD: loop/Josephson screening scale in the reduced force model;
- DELTA_TILT: external directional tilt.

For each viable rDelta=.6 model, compute

- cold left/right minima and central saddle;
- left metastable barrier height;
- exact zero-energy isolated bounce action

      B0 = (2/hbar) int_xm^xt dx sqrt(2 M [U(x)-U(xm)]),

  with M=C Phi_bar^2;
- shape factor beta_U = B0 / [DeltaU/(hbar omega_c)];
- cold phase frequency;
- static fold temperature;
- cold well-energy bias U_left-U_right;
- minimum-state phase separation.

This is a static/dark screening scan only.  Larger B0 is not automatically a
better detector: reducing tilt may destroy directionality, and changing beta
or tilt changes the photon-capture dynamics.  Promising points must be rerun
through the full causal finite-pulse model.
"""
from __future__ import annotations

import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

import full_dynamic_rfsquid as fd
from quantum_initial_capture import HBAR, PHI_BAR, KB


def Udiff(model,x0,x):
    return float(quad(lambda xx:model.force(fd.T0,xx),x0,x,
                      epsabs=2e-12,epsrel=3e-9,limit=250)[0])


def metrics(model):
    roots=model.roots(fd.T0)
    mins=sorted([x for x,k in roots if k>0])
    saddles=sorted([x for x,k in roots if k<0])
    if len(mins)<2: raise RuntimeError('not bistable')
    # Select adjacent left/right pair around zero and saddle between them.
    left=max([x for x in mins if x<0],default=mins[0])
    right=min([x for x in mins if x>left],default=mins[-1])
    between=[x for x in saddles if left<x<right]
    if not between: raise RuntimeError('no separating saddle')
    xs=between[0]
    barrier_dim=Udiff(model,left,xs)
    Er=Udiff(model,left,right)
    if barrier_dim<=0: raise RuntimeError('nonpositive barrier')

    # Zero-energy turning point beyond saddle. Search from saddle to right and,
    # if necessary, farther on the model grid for first U=U(left) crossing.
    xscan=np.linspace(xs+1e-6,float(model.xgrid[-1]),2500)
    vals=np.array([Udiff(model,left,float(x)) for x in xscan])
    ids=np.where(vals[:-1]*vals[1:]<=0)[0]
    if not len(ids): raise RuntimeError('no zero-energy turning point')
    i=int(ids[0]); xt=float(brentq(lambda x:Udiff(model,left,x),xscan[i],xscan[i+1],
                                  xtol=2e-12,rtol=2e-12))

    L,C,_=fd.CASES[.6]
    EL=PHI_BAR**2/L
    M=C*PHI_BAR**2
    # Physical potential = EL * dimensionless integral of F dx.
    def integ(x):
        ud=max(Udiff(model,left,float(x)),0.0)
        return math.sqrt(2*M*EL*ud)
    B0=2/HBAR*quad(integ,left,xt,epsabs=1e-33,epsrel=2e-8,limit=300)[0]

    # Local curvature / phase frequency at metastable left well.
    kappa=float(model.spline.ev(fd.T0,left,dx=0,dy=1))
    wc=math.sqrt(kappa/(L*C))
    barrierK=barrier_dim*EL/KB
    ratio=(barrier_dim*EL)/(HBAR*wc)
    betaU=B0/ratio

    # Exact well energy bias: positive means right well lower than left.
    biasK=-Er*EL/KB
    fold=model.fold_temperature(hi=.95)
    return dict(left=left,right=right,xs=xs,xt=xt,sep=right-left,
                kappa=kappa,fc=wc/(2*math.pi),barrierK=barrierK,
                biasK=biasK,B0=B0,betaU=betaU,fold=fold,
                action_ratio=ratio)


def main():
    print('Experiment 03 exact barrier-shape/action scan')
    old_beta=fd.BETA_COLD; old_tilt=fd.DELTA_TILT
    rows=[]
    try:
        for beta in (.72,.76,.80,.84,.88,.92):
            for tilt in (.20,.25,.30,.35,.40):
                fd.BETA_COLD=float(beta); fd.DELTA_TILT=float(tilt)
                try:
                    m=fd.DynamicForce(.6,quick=False,Tmax=.96)
                    q=metrics(m)
                    rows.append((q['B0'],beta,tilt,q))
                    msg=(f'beta={beta:.2f} tilt={tilt:.2f}: B0={q["B0"]:.5f} '
                         f'betaU={q["betaU"]:.4f} barrier={q["barrierK"]:.4f}K '
                         f'fc={q["fc"]*1e-9:.3f}GHz fold={q["fold"]:.4f}K '
                         f'biasRlower={q["biasK"]:.4f}K sep={q["sep"]:.4f}rad '
                         f'xL/xS/xT=({q["left"]:+.4f},{q["xs"]:+.4f},{q["xt"]:+.4f})')
                except Exception as e:
                    msg=f'beta={beta:.2f} tilt={tilt:.2f}: INVALID {type(e).__name__}: {e}'
                print(msg); print(f'::notice title=Experiment 03 barrier-shape scan::{msg}')
    finally:
        fd.BETA_COLD=old_beta; fd.DELTA_TILT=old_tilt

    rows.sort(reverse=True,key=lambda r:r[0])
    print('\nTop exact isolated actions:')
    for B,b,t,q in rows[:12]:
        print(f'B0={B:.5f} beta={b:.2f} tilt={t:.2f} betaU={q["betaU"]:.4f} '
              f'barrierK={q["barrierK"]:.4f} fold={q["fold"]:.4f} biasK={q["biasK"]:.4f}')
    print('PASS')

if __name__=='__main__': main()
