#!/usr/bin/env python3
"""Constructive continuum-scaling audit for independent physical pseudomodes.

The first nonnegative Lorentzian dictionary fit showed that broad independent
thermal modes cannot simultaneously reproduce the direct-port positive spectrum,
the exponentially suppressed negative spectrum, and the time correlation.
That does not rule out a very dense set of narrow modes.

This script therefore uses no optimizer.  It discretizes the *exact* positive-
frequency spectrum on 0<x<XMAX into N positive-frequency thermal pseudomodes.
For cell width dx and center O_j,

    q_j = s_exact(O_j) dx / [2 pi (n_j+1)]

matches the positive-frequency spectral area in the delta-line limit.  Each
mode is broadened by gamma=eta*dx and automatically carries the physical thermal
negative-frequency partner with n_j/(n_j+1)=exp(-theta O_j).

The resulting correlation is globally positive and CPTP-realizable as
independent damped thermal oscillators.  We scan N=64..512 and eta=.2,.5,1 to
measure the unavoidable tradeoff between spectral smoothing and artificial
long memory.  This is a feasibility/scaling audit only; no system dynamics are
performed.
"""
from __future__ import annotations

import math
import numpy as np

from direct_port_bath_correlation import HBAR,BETA,FC,G,WD,corr_series

WC=2*math.pi*FC
S0=2*G/BETA
THETA=BETA*HBAR*WC
XMAX=24.0


def exact_s(x):
    a=np.asarray(x,float); out=np.empty_like(a)
    zero=np.abs(a)<1e-15; out[zero]=1.0
    nz=~zero
    if np.any(nz):
        w=WC*a[nz]; aw=np.abs(w)
        J=HBAR*G*aw*WD**4/(aw**4+WD**4)
        y=BETA*HBAR*aw
        sp=2*J/(-np.expm1(-np.minimum(y,700.0)))
        out[nz]=np.where(w>=0,sp,sp*np.exp(-np.minimum(y,745.0)))/S0
    return out


def build(N,eta):
    dx=XMAX/N
    O=(np.arange(N)+.5)*dx
    g=np.full(N,eta*dx)
    n=1/np.expm1(THETA*O)
    sp=exact_s(O)
    q=sp*dx/(2*math.pi*(n+1))
    return O,g,n,q,dx


def spectrum(x,O,g,n,q):
    a=np.asarray(x,float)[...,None]
    return np.sum(q*(2*g*(n+1)/((a-O)**2+g*g)
                     +2*g*n/((a+O)**2+g*g)),axis=-1)


def corr(tau,O,g,n,q):
    return np.sum(q*((n+1)*np.exp(-(g+1j*O)*tau)
                     +n*np.exp(-(g-1j*O)*tau)))


def exact_corr(tau):
    return corr_series(float(tau)/WC,10000)/(S0*WC)


def audit(N,eta):
    O,g,n,q,dx=build(N,eta)
    x=np.linspace(-6,12,7201); ex=exact_s(x); sf=spectrum(x,O,g,n,q)
    abs_err=np.abs(sf-ex)
    useful=ex>1e-5; useful8=ex>1e-8
    maxrel5=float(np.max(abs_err[useful]/ex[useful]))
    maxrel8=float(np.max(abs_err[useful8]/ex[useful8]))
    rms=float(np.sqrt(np.mean(abs_err**2)))
    # KMS log ratio error at system-relevant frequencies.
    db=[]
    for xp in (.25,.5,1.,2.,3.,4.):
        spp=float(spectrum(np.array([xp]),O,g,n,q)[0])
        smm=float(spectrum(np.array([-xp]),O,g,n,q)[0])
        ratio=smm/spp; exact=math.exp(-THETA*xp)
        db.append(abs(math.log(max(ratio,1e-300))-math.log(exact)))
    taus=(0.,.25,.5,1.,2.,4.,8.,12.,16.,20.,24.)
    crel=[]; cabs=[]
    for t in taus:
        cf=corr(t,O,g,n,q); ce=exact_corr(t)
        crel.append(abs(cf-ce)/max(abs(ce),1e-14)); cabs.append(abs(cf-ce))
    c0=abs(corr(0,O,g,n,q)-exact_corr(0))/abs(exact_corr(0))
    msg=(f'LORENTZ_CONTINUUM N={N} eta={eta:.2f} dx={dx:.6e} gamma={eta*dx:.6e} '
         f'maxrelS5={maxrel5:.6e} maxrelS8={maxrel8:.6e} rmsS={rms:.6e} '
         f'db_logmax={max(db):.6e} maxrelC={max(crel):.6e} maxabsC={max(cabs):.6e} '
         f'C0rel={c0:.6e} minS={float(np.min(sf)):.3e}')
    print(msg,flush=True)
    print(f'::notice title=Experiment 03 physical continuum scaling::{msg}',flush=True)
    return dict(N=N,eta=eta,maxrel5=maxrel5,maxrel8=maxrel8,rms=rms,
                db=max(db),crel=max(crel),cabs=max(cabs),c0=c0)


def main():
    rows=[]
    for N in (64,128,256,512):
        for eta in (.2,.5,1.0):
            rows.append(audit(N,eta))
    print('SUMMARY')
    for r in rows:
        print(f'N={r["N"]:3d} eta={r["eta"]:.1f} spec5={r["maxrel5"]:.3e} '
              f'db={r["db"]:.3e} corrRel={r["crel"]:.3e} C0={r["c0"]:.3e}',flush=True)
    viable=[r for r in rows if r['maxrel5']<.05 and r['db']<.1 and r['c0']<.01 and r['crel']<.1]
    if viable:
        print('INDEPENDENT_PHYSICAL_CONTINUUM_FEASIBLE_AT_TESTED_SCALE')
    else:
        print('INDEPENDENT_PHYSICAL_CONTINUUM_NOT_PRACTICAL_AT_N_LE_512')

if __name__=='__main__': main()
