#!/usr/bin/env python3
"""Calibrate the periodic-instanton determinant/prefactor normalization on the
canonical local cubic metastable potential.

Use dimensionless time s=omega*t and coordinate z=q/q0 with

    V(z) = (M omega^2 q0^2 / 2) z^2 (1-z).

The isolated bounce is exactly

    z_b(s)=sech^2(s/2),

with

    B = 8 A / 15,
    A = M omega q0^2 / hbar.

For the cubic problem the standard zero-temperature one-loop escape rate is

    Gamma = (omega/2pi) sqrt(120 pi B) exp(-B).

Equivalently, after removing the translation zero mode, the determinant of the
*dimensionless differential operator* obeys

    sqrt(det L_m / |det' L_b|) = sqrt(60).

A Hessian of the dimensionless action B=S/hbar instead carries one unmatched
factor sqrt(A), because the bounce determinant has one fewer eigenvalue after
zero-mode removal. Therefore the physical operator determinant is

    D_op = D_raw/sqrt(A).

This script verifies numerically that:

  1. D_raw scales as sqrt(A);
  2. D_op -> sqrt(60), independent of A;
  3. omega * sqrt(B/(2pi)) * D_op reproduces the standard cubic prefactor.

This is the normalization calibration needed before applying the same determinant
machinery to the nonlocal finite-T Experiment-03 bounce.
"""
from __future__ import annotations

import math
import numpy as np
from scipy.special import polygamma

P=40.0
RES=(32,48,64,80,96,128,160)
AGRID=(5.0,20.0,80.0)
TARGET_D=math.sqrt(60.0)


def sech(x): return 1.0/np.cosh(x)


def determinant(A:float,N:int,ngrid:int=32768):
    s=np.linspace(-P/2,P/2,ngrid,endpoint=False)
    ds=P/ngrid
    n=np.arange(N+1,dtype=float)
    k=2*math.pi*n/P
    z=sech(s/2.0)**2
    W=1.0-3.0*z

    # Orthonormal even basis: constant + cosines.
    Be=np.empty((ngrid,N+1))
    Be[:,0]=1/math.sqrt(P)
    if N:
        Be[:,1:]=math.sqrt(2/P)*np.cos(np.outer(s,k[1:]))
    # Orthonormal odd basis: sines n>=1.
    Bo=math.sqrt(2/P)*np.sin(np.outer(s,k[1:]))

    He=A*np.diag(k*k)+A*(Be.T@(W[:,None]*Be))*ds
    Ho=A*np.diag(k[1:]**2)+A*(Bo.T@(W[:,None]*Bo))*ds
    ee,Ve=np.linalg.eigh(He)
    eo,Vo=np.linalg.eigh(Ho)

    if np.sum(ee<0)!=1:
        raise RuntimeError(f'expected one even negative mode, got {np.sum(ee<0)}')
    iz=int(np.argmin(np.abs(eo)))
    eonz=np.delete(eo,iz)
    if np.any(eonz<=0):
        raise RuntimeError('extra nonpositive odd mode')

    # Analytic translation derivative z'(s)=-z*tanh(s/2).
    zp=-z*np.tanh(s/2)
    zcoef=(Bo.T@zp)*ds
    zcoef/=np.linalg.norm(zcoef)
    overlap=abs(float(np.dot(Vo[:,iz],zcoef)))

    # Metastable well W=1: eigenvalues A(k^2+1).
    le=A*(k*k+1.0)
    lo=A*(k[1:]**2+1.0)
    lograw=.5*(float(np.sum(np.log(le))+np.sum(np.log(lo)))
               -float(np.sum(np.log(np.abs(ee)))+np.sum(np.log(eonz))))

    # Leading omitted high-n tail.  <W_b>=1-3*<z>; int z ds ->4 for P>>1.
    Wbar=float(np.mean(W))
    delta=A*(1.0-Wbar)
    # Reference high-n eigenvalue A(k_n^2+1), so A cancels explicitly.
    nn=np.arange(N+1,200001,dtype=float)
    kk=2*math.pi*nn/P
    tail=float(np.sum(delta/(A*(kk*kk+1.0))))
    coeff=delta/A*P*P/(4*math.pi**2)
    tail+=float(coeff*polygamma(1,200001))

    logcorr=lograw+tail
    Draw=math.exp(logcorr)
    Dop=Draw/math.sqrt(A)

    # Bounce kinetic identity: I=int z'^2 ds = 8/15, B=A*I.
    I=float(np.sum(zp*zp)*ds)
    Bact=A*I
    pref_num=math.sqrt(Bact/(2*math.pi))*Dop # Gamma/omega without exp(-B)
    pref_std=math.sqrt(120*math.pi*Bact)/(2*math.pi)
    return dict(lograw=lograw,tail=tail,logcorr=logcorr,Draw=Draw,Dop=Dop,
                overlap=overlap,zero=float(eo[iz]),neg=float(ee[0]),I=I,B=Bact,
                pref_num=pref_num,pref_std=pref_std)


def main():
    print(f'cubic calibration target sqrt(60)={TARGET_D:.12f}')
    final=[]
    for A in AGRID:
        print(f'-- A={A:g} --')
        rows=[]
        for N in RES:
            q=determinant(A,N)
            rows.append(q)
            msg=(f'A={A:g} N={N}: B={q["B"]:.9f} D_raw_corr={q["Draw"]:.9f} '
                 f'D_op={q["Dop"]:.9f} D_op/sqrt60-1={q["Dop"]/TARGET_D-1:+.3e} '
                 f'pref_num/std-1={q["pref_num"]/q["pref_std"]-1:+.3e} '
                 f'zero={q["zero"]:+.3e} overlap={q["overlap"]:.10f} tail={q["tail"]:+.6e}')
            print(msg); print(f'::notice title=Experiment 03 cubic prefactor calibration::{msg}')
        final.append(rows[-1])
        if abs(rows[-1]['Dop']/TARGET_D-1)>3e-3:
            raise RuntimeError('cubic operator determinant failed sqrt(60) calibration')
        if abs(rows[-1]['pref_num']/rows[-1]['pref_std']-1)>3e-3:
            raise RuntimeError('cubic one-loop prefactor normalization failed')
        if rows[-1]['overlap']<.9999:
            raise RuntimeError('translation zero-mode calibration failed')
    ratios=[q['Draw']/math.sqrt(A) for q,A in zip(final,AGRID)]
    spread=max(ratios)-min(ratios)
    print(f'A-scaling D_raw/sqrt(A): {ratios}; spread={spread:.3e}')
    if spread>1e-5:
        raise RuntimeError('raw determinant did not exhibit expected sqrt(A) scaling')
    print('PASS')

if __name__=='__main__': main()
