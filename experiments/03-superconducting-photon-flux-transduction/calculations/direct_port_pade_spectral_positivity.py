#!/usr/bin/env python3
"""Spectral-positivity audit of the finite direct-port Padé bath correlation.

A completely positive interacting-pseudomode realization requires the *finite
exponential correlation being represented* to be a physical stationary
Gaussian correlation, not merely a close time-domain approximation to one.
For a Hermitian bath operator this means its two-sided unsymmetrized Fourier
spectrum is nonnegative for every real frequency.

For t>=0 the present finite correlation is

    C_N(t) = sum_k c_k exp(-gamma_k t),   Re gamma_k > 0,

with C_N(-t)=C_N(t)*.  Its exact two-sided spectrum is therefore

    S_N(w) = 2 Re sum_k c_k / (gamma_k - i w).

This script audits N=4,5,8 Bose-Padé decompositions over a very wide signed
frequency range, adaptively locates any zero crossings, and compares to the
underlying exact physical direct-port greater spectrum where numerically
resolvable.

It also prints the high-frequency expansion moments.  Writing

  1/(gamma-iw) = i/w + gamma/w^2 - i gamma^2/w^3 - gamma^3/w^4 + ...,

shows which algebraic tail controls the sign when the exact negative-frequency
spectrum has already become exponentially small.

This is a bath-physicality prerequisite only.  It does not construct a
pseudomode model and does not alter the accepted HEOM/TEMPO physics.
"""
from __future__ import annotations

import math
import numpy as np
from scipy.optimize import brentq, minimize_scalar

from direct_port_bath_correlation import (
    HBAR, BETA, G, WD, FC, bath_poles, bath_coeff,
)
from direct_port_bath_pade import pade_terms

WC = 2*math.pi*FC
S0 = 2*G/BETA


def terms(N):
    c=[]; gam=[]
    for p in bath_poles():
        c.append(complex(bath_coeff(p)))
        gam.append(complex(1j*p))
    for cj,nu in pade_terms(N):
        c.append(complex(cj)); gam.append(complex(nu))
    return np.asarray(c,complex),np.asarray(gam,complex)


def sfit_dimless(x,c,gam):
    w=np.asarray(x,dtype=float)*WC
    val=2*np.real(np.sum(c/(gam-1j*w[...,None]),axis=-1))
    return val/S0


def exact_dimless(x):
    """Stable exact physical greater spectrum normalized by S(0)."""
    xa=np.asarray(x,dtype=float)
    wabs=np.abs(xa)*WC
    out=np.empty_like(xa,float)
    zero=(wabs==0)
    out[zero]=1.0
    nz=~zero
    if np.any(nz):
        w=wabs[nz]
        J=HBAR*G*w*WD**4/(w**4+WD**4)
        y=BETA*HBAR*w
        sp=2*J/(-np.expm1(-np.minimum(y,700.0)))
        sign=xa[nz]>=0
        vals=np.empty_like(w)
        vals[sign]=sp[sign]
        vals[~sign]=sp[~sign]*np.exp(-np.minimum(y[~sign],745.0))
        out[nz]=vals/S0
    return out


def signed_grid():
    core=np.linspace(-20,20,40001)
    wing=np.geomspace(20.001,1e6,24000)
    return np.concatenate((-wing[::-1],core,wing))


def roots_from_grid(x,y,c,gam):
    roots=[]
    for i in np.where(y[:-1]*y[1:]<0)[0]:
        a=float(x[i]); b=float(x[i+1])
        try:
            r=brentq(lambda q: float(sfit_dimless(q,c,gam)),a,b,
                     xtol=1e-13,rtol=1e-13,maxiter=200)
            if not roots or abs(r-roots[-1])>1e-8*max(1,abs(r)):
                roots.append(r)
        except Exception:
            pass
    return roots


def audit(N):
    c,gam=terms(N)
    x=signed_grid(); y=sfit_dimless(x,c,gam)
    j=int(np.argmin(y)); xmin=float(x[j]); ymin=float(y[j])
    if 0<j<len(x)-1:
        a=float(x[j-1]); b=float(x[j+1])
        opt=minimize_scalar(lambda q: float(sfit_dimless(q,c,gam)),
                            bounds=(a,b),method='bounded',
                            options={'xatol':1e-13})
        if opt.success and opt.fun<ymin:
            xmin=float(opt.x); ymin=float(opt.fun)

    roots=roots_from_grid(x,y,c,gam)
    negfrac=float(np.mean(y < -1e-14))
    print(f'PADE p{N} nterms={len(c)} minS_over_S0={ymin:+.15e} '
          f'at_w_over_wc={xmin:+.15e} negative_grid_fraction={negfrac:.6e}',flush=True)
    print('ROOTS p%d '%N + (' '.join(f'{r:+.15e}' for r in roots) if roots else 'NONE'),flush=True)

    probes=np.array([0,.1,.5,1,2,4,8,12,16,20,40,100,1e3,1e4,1e5,1e6],float)
    for q in probes:
        sfp=float(sfit_dimless(q,c,gam)); sfm=float(sfit_dimless(-q,c,gam))
        sep=float(exact_dimless(np.array(q))); sem=float(exact_dimless(np.array(-q)))
        print(f'PROBE p{N} x={q:.6g} Sfit+={sfp:+.12e} Sfit-={sfm:+.12e} '
              f'Sexact+={sep:+.12e} Sexact-={sem:+.12e}',flush=True)

    for m in range(5):
        M=np.sum(c*gam**m)
        print(f'MOMENT p{N} m={m} M=({M.real:+.15e}{M.imag:+.15e}j)',flush=True)

    mask=np.abs(x)<=20
    ex=exact_dimless(x[mask]); fit=y[mask]
    useful=ex>1e-10
    maxrel=float(np.max(np.abs(fit[useful]-ex[useful])/ex[useful])) if np.any(useful) else math.nan
    maxabs=float(np.max(np.abs(fit-ex)))
    print(f'COMPARE p{N} |x|<=20 exact>1e-10 maxrel={maxrel:.12e} maxabs_S0={maxabs:.12e}',flush=True)

    positive=(ymin >= -1e-12)
    msg=(f'PADE_SPECTRAL_POSITIVITY p{N} min={ymin:+.6e} at={xmin:+.6e} '
         f'roots={len(roots)} physical_on_scan={positive}')
    print(msg,flush=True)
    print(f'::notice title=Experiment 03 Padé bath spectral positivity::{msg}',flush=True)
    return positive,ymin,xmin,roots


def main():
    results={N:audit(N) for N in (4,5,8)}
    if all(v[0] for v in results.values()):
        print('PASS_FINITE_PADE_SPECTRAL_POSITIVITY_ON_SCAN')
    else:
        bad=[N for N,v in results.items() if not v[0]]
        print('FAIL_FINITE_PADE_SPECTRAL_POSITIVITY orders=' + ','.join(map(str,bad)))

if __name__=='__main__': main()
