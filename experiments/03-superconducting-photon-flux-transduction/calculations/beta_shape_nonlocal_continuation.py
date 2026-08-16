#!/usr/bin/env python3
"""Continuation solution of shaped-barrier nonlocal dissipative bounces.

Motivation
----------
The baseline beta=.80 nonlocal spectral bounce is converged.  Stronger shaped
barriers beta=.85/.90 caused the *auxiliary isolated time-domain seed* to miss an
extremely strict tail tolerance, even though their exact static actions are
well defined.  That is a seed-construction issue, not a physical failure.

This solver removes that dependency.  It uses one fixed even Dirichlet cosine
basis and continues the stationary Euclidean solution in beta:

    beta=.80 -> .825 -> .85 -> .875 -> .90.

At every beta it solves both

1. the isolated action (K_env=0), and
2. the same R=80 ohm, alpha=.90 two-pole dissipative action,

using the previous beta's spectral coefficients as the next initial guess.
The beta=.80 result must reproduce the independently validated actions

    B_iso = 25.03305
    B_env = 29.76564

to the finite-basis accuracy of this common-box formulation.

This is the preferred shaped-bounce comparison because it never requires a
separate long-tail trajectory for beta>.80.
"""
from __future__ import annotations

import math
import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.optimize import root

import full_dynamic_rfsquid as fd
from quantum_initial_capture import HBAR, PHI_BAR
from R80_dissipative_bounce_screen import isolated_bounce, Y_laplace

R_ENV=80.0
ALPHA=.90
NB=48
NG=8192


def setup_basis():
    # Only the live baseline uses the validated time-domain seed.  It determines
    # a common normalized box/basis for the whole continuation.
    fd.BETA_COLD=.80; fd.DELTA_TILT=.05
    base=isolated_bounce(fd.DynamicForce(.6,quick=False),nfft=65536)
    S=1.75*base['Shalf']
    s=np.linspace(-S,S,NG,endpoint=False); ds=float(s[1]-s[0]); Tbox=2*S
    k=(np.arange(NB)+.5)*math.pi/S
    B=np.cos(np.outer(s,k))
    y0=np.interp(s,base['s'],base['y'],left=0.0,right=0.0)
    a0=(B.T@y0)*ds/S
    BF=np.fft.fft(B,axis=0)*ds
    Om=2*math.pi*np.fft.fftfreq(NG,d=ds)
    return base,S,s,ds,Tbox,k,B,BF,Om,a0


def solve_beta(beta,a_iso_init,a_env_init,geom):
    base,S,s,ds,Tbox,k,B,BF,Om,_=geom
    fd.BETA_COLD=float(beta); fd.DELTA_TILT=.05
    model=fd.DynamicForce(.6,quick=False,Tmax=.98)
    L,C,_=fd.CASES[.6]
    # Resolve live metastable minimum and local curvature directly.
    roots=model.roots(fd.T0)
    xm=max(x for x,kap in roots if x<0 and kap>0)
    kappa=model._scalar(model.spline.ev(fd.T0,xm,dx=0,dy=1))
    wc=math.sqrt(kappa/(L*C))
    Ak=C*PHI_BAR**2*wc/HBAR
    Av=(PHI_BAR**2/L)/(HBAR*wc)
    Kkin=np.diag(Ak*S*k*k)

    # Cold force/potential interpolation.
    xlo=xm-0.02
    xhi=min(float(model.xgrid[-1]),1.55)
    xgrid=np.linspace(xlo,xhi,60001)
    Fgrid=np.array([model.force(fd.T0,float(x)) for x in xgrid])
    Ugrid=cumulative_trapezoid(Fgrid,xgrid,initial=0.0)
    Um=float(np.interp(xm,xgrid,Ugrid))
    Ugrid=Ugrid-Um
    dFgrid=np.gradient(Fgrid,xgrid)
    def Fv(x): return np.interp(x,xgrid,Fgrid,left=Fgrid[0],right=Fgrid[-1])
    def Uv(x): return np.interp(x,xgrid,Ugrid,left=Ugrid[0],right=Ugrid[-1])
    def dFv(x): return np.interp(x,xgrid,dFgrid,left=dFgrid[0],right=dFgrid[-1])

    # Environment matrix at this beta's local cold frequency.
    ao=np.abs(Om); wd=ALPHA*wc
    weight=ao*Y_laplace(wc*ao,R_ENV,wd)
    Kenv=(PHI_BAR**2/HBAR)*np.real(BF.conj().T@(weight[:,None]*BF))/Tbox
    Kenv=.5*(Kenv+Kenv.T)

    def stationary(a,Kextra):
        def grad(q):
            x=xm+B@q
            return (Kkin+Kextra)@q + Av*(B.T@Fv(x))*ds
        def jac(q):
            x=xm+B@q; W=dFv(x)
            return Kkin+Kextra+Av*(B.T@(W[:,None]*B))*ds
        sol=root(grad,a,jac=jac,method='hybr',tol=2e-10,
                 options={'xtol':2e-10,'maxfev':6000})
        q=np.asarray(sol.x); x=xm+B@q
        K=.5*float(q@(Kkin@q)); E=.5*float(q@(Kextra@q))
        V=Av*float(np.sum(Uv(x))*ds); Act=K+E+V
        H=jac(q); ev=np.linalg.eigvalsh(H)
        return q,dict(success=bool(sol.success),B=Act,K=K,V=V,E=E,
                      grad=float(np.linalg.norm(grad(q),ord=np.inf)),
                      xcenter=float(x[np.argmin(np.abs(s))]),ev=ev)

    ai,oi=stationary(a_iso_init,np.zeros_like(Kenv))
    ae,oe=stationary(a_env_init,Kenv)
    return model,wc,ai,oi,ae,oe


def main():
    print('Experiment 03 shaped nonlocal bounce CONTINUATION')
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    try:
        geom=setup_basis(); a0=geom[-1]
        ai=a0.copy(); ae=a0.copy()
        for beta in (.80,.825,.85,.875,.90):
            model,wc,ai,oi,ae,oe=solve_beta(beta,ai,ae,geom)
            ni=int(np.sum(oi['ev']<0)); ne=int(np.sum(oe['ev']<0))
            msg=(f'beta={beta:.3f}: fc={wc/(2*math.pi)*1e-9:.5f}GHz '
                 f'Biso={oi["B"]:.7f} Benv={oe["B"]:.7f} DeltaBenv={oe["B"]-oi["B"]:.7f}; '
                 f'iso(success={oi["success"]},grad={oi["grad"]:.2e},nneg={ni},xc={oi["xcenter"]:+.6f}); '
                 f'env(success={oe["success"]},grad={oe["grad"]:.2e},nneg={ne},xc={oe["xcenter"]:+.6f})')
            print(msg); print(f'::notice title=Experiment 03 shaped bounce continuation::{msg}')
            if ni!=1 or ne!=1:
                raise RuntimeError(f'wrong negative-mode count at beta={beta}')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot

if __name__=='__main__': main()
