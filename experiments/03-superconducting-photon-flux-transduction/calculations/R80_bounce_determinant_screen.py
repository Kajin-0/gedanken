#!/usr/bin/env python3
"""Fluctuation-determinant scale for the converged R80 nonlocal bounce.

Purpose
-------
The full nonlocal bounce action B~29.77 is now converged, but the physical dark
rate also contains a fluctuation prefactor.  This script estimates the
*dimensionless determinant scale* in the same finite-box spectral
regularization as `R80_nonlocal_bounce_spectral.py`.

It is deliberately reported as

    Abar = sqrt(B/2pi) * sqrt(det H_meta / |det' H_bounce|)

in units of the cold normalized-time frequency scale.  A physical rate would
be of order

    Gamma ~ omega_c * Abar * exp(-B)

up to conventional factors associated with the negative mode/decay-rate
normalization.  We therefore use this screen only to answer the robust question:

    does the prefactor contribute O(1), O(10), or O(exp(8)) enough to erase the
    action deficit?

The bounce is even.  Dirichlet finite-box basis:

    even: cos[(n+1/2) pi s/S], n=0,...
    odd:  sin[n pi s/S],       n=1,...

The even bounce Hessian should contain one negative mode.  The odd Hessian
contains the translation mode; the eigenvalue of smallest absolute magnitude
is removed.  The metastable Hessians are positive.

This is a finite-box determinant screen, not yet a publication-grade decay-rate
prefactor.  Convergence with basis size and the near-zero translation eigenvalue
are the mandatory diagnostics.
"""
from __future__ import annotations

import math
import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.optimize import root

from full_dynamic_rfsquid import DynamicForce, T0
from quantum_initial_capture import HBAR, PHI_BAR
from R80_dissipative_bounce_screen import isolated_bounce, Y_laplace


def matrices(nbasis:int,ngrid:int,R=80.0,alpha=.90):
    model=DynamicForce(.6,quick=False)
    dat=isolated_bounce(model,nfft=65536)
    L,C=dat['L'],dat['C']; wc=dat['wc']; xm=dat['xm']
    S=1.75*dat['Shalf']; s=np.linspace(-S,S,ngrid,endpoint=False); ds=float(s[1]-s[0]); Tbox=2*S
    ke=(np.arange(nbasis)+.5)*math.pi/S
    ko=(np.arange(1,nbasis+1))*math.pi/S
    Be=np.cos(np.outer(s,ke)); Bo=np.sin(np.outer(s,ko))
    Ak=C*PHI_BAR**2*wc/HBAR
    Av=(PHI_BAR**2/L)/(HBAR*wc)
    Kke=np.diag(Ak*S*ke*ke); Kko=np.diag(Ak*S*ko*ko)

    xmax=min(float(model.xgrid[-1]),dat['xr']+.35)
    xgrid=np.linspace(xm,xmax,50001)
    Fgrid=np.array([model.force(T0,float(x)) for x in xgrid])
    dFgrid=np.gradient(Fgrid,xgrid)
    def Fv(x): return np.interp(x,xgrid,Fgrid,left=Fgrid[0],right=Fgrid[-1])
    def dFv(x): return np.interp(x,xgrid,dFgrid,left=dFgrid[0],right=dFgrid[-1])

    def Kenv(Basis):
        BF=np.fft.fft(Basis,axis=0)*ds
        Om=2*math.pi*np.fft.fftfreq(ngrid,d=ds); ao=np.abs(Om); wd=alpha*wc
        weight=ao*Y_laplace(wc*ao,R,wd)
        K=(PHI_BAR**2/HBAR)*np.real(BF.conj().T@(weight[:,None]*BF))/Tbox
        return .5*(K+K.T)
    Kee=Kenv(Be); Keo=Kenv(Bo)

    # Solve even bounce coefficients.
    y0=np.interp(s,dat['s'],dat['y'],left=0,right=0); a0=(Be.T@y0)*ds/S
    def grad(a):
        x=xm+Be@a
        return (Kke+Kee)@a + Av*(Be.T@Fv(x))*ds
    def He(a):
        W=dFv(xm+Be@a)
        return Kke+Kee+Av*(Be.T@(W[:,None]*Be))*ds
    sol=root(grad,a0,jac=He,method='hybr',tol=2e-10,options={'maxfev':5000})
    a=np.asarray(sol.x); xb=xm+Be@a; Wb=dFv(xb)
    Hbe=Kke+Kee+Av*(Be.T@(Wb[:,None]*Be))*ds
    Hbo=Kko+Keo+Av*(Bo.T@(Wb[:,None]*Bo))*ds

    # Metastable Hessian at constant xm.
    km=float(model.spline.ev(T0,xm,dx=0,dy=1))
    Hme=Kke+Kee+Av*km*(Be.T@Be)*ds
    Hmo=Kko+Keo+Av*km*(Bo.T@Bo)*ds

    # Action for solved bounce; potential from one cumulative integration.
    Ugrid=cumulative_trapezoid(Fgrid,xgrid,initial=0.0)
    U=np.interp(xb,xgrid,Ugrid)
    K=.5*float(a@(Kke@a)); E=.5*float(a@(Kee@a)); V=Av*float(np.sum(U)*ds)
    B=K+E+V
    return B,Hbe,Hbo,Hme,Hmo,sol,dat


def log_positive(vals,remove_index=None,abs_negative=False):
    out=[]
    for i,v in enumerate(vals):
        if remove_index is not None and i==remove_index: continue
        if v<0 and abs_negative: out.append(math.log(abs(float(v))))
        elif v>0: out.append(math.log(float(v)))
        else: raise RuntimeError(f'unexpected nonpositive eigenvalue {v}')
    return float(sum(out))


def main():
    print('Experiment 03 R80 bounce determinant PREFactor screen')
    for nb,ng in ((20,4096),(28,6144),(36,8192),(44,10240)):
        B,Hbe,Hbo,Hme,Hmo,sol,dat=matrices(nb,ng)
        ebe=np.linalg.eigvalsh(Hbe); ebo=np.linalg.eigvalsh(Hbo)
        eme=np.linalg.eigvalsh(Hme); emo=np.linalg.eigvalsh(Hmo)
        neg=np.where(ebe<0)[0]
        if len(neg)!=1: raise RuntimeError(f'even bounce negative count={len(neg)}')
        iz=int(np.argmin(np.abs(ebo)))
        # Exclude the odd near-zero translation mode; include magnitude of one even negative mode.
        log_meta=float(np.sum(np.log(eme))+np.sum(np.log(emo)))
        log_b=log_positive(ebe,abs_negative=True)+log_positive(ebo,remove_index=iz,abs_negative=False)
        log_det_ratio=.5*(log_meta-log_b)
        log_Abar=.5*math.log(B/(2*math.pi))+log_det_ratio
        Abar=math.exp(log_Abar) if log_Abar<700 else math.inf
        # Compare to naive fc exp(-B): Gamma/(fc e^-B) ~ 2pi*Abar, up to convention O(1).
        rel_naive=2*math.pi*Abar
        msg=(f'Nb={nb} Ng={ng} success={sol.success} B={B:.6f}; '
             f'evenNeg={ebe[0]:+.5e}; oddZero={ebo[iz]:+.5e} iz={iz}; '
             f'nextOdd={ebo[1 if iz==0 else 0]:+.5e}; '
             f'logSqrtDetRatio={log_det_ratio:+.6f}; logAbar={log_Abar:+.6f}; '
             f'Abar={Abar:.6e}; relTo_fc_pref~{rel_naive:.6e}')
        print(msg); print(f'::notice title=Experiment 03 bounce determinant::{msg}')
    print('Interpretation: only the logarithmic scale and convergence are trusted. Exact decay-rate normalization still requires a careful negative/zero-mode treatment and finite-temperature check.')
    print('PASS')

if __name__=='__main__': main()
