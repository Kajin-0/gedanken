#!/usr/bin/env python3
"""Continue the full nonlocal dissipative bounce from live tilt .050 to .035.

Fixed:
    beta_cold=.80
    R=80 ohm
    alpha=.90
    C=215 fF

Continuation:
    delta=.050 -> .045 -> .040 -> .035.

Uses a common spectral basis and the converged previous stationary path as the
next initial guess, avoiding any shaped/low-tilt tail-seed ambiguity.
"""
from __future__ import annotations
import math
import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.optimize import root

import full_dynamic_rfsquid as fd
from quantum_initial_capture import HBAR, PHI_BAR
from R80_dissipative_bounce_screen import isolated_bounce, Y_laplace

R_ENV=80.; ALPHA=.90; NB=48; NG=8192


def setup():
    fd.BETA_COLD=.80; fd.DELTA_TILT=.05
    base=isolated_bounce(fd.DynamicForce(.6,quick=False),nfft=65536)
    S=1.75*base['Shalf']; s=np.linspace(-S,S,NG,endpoint=False)
    ds=float(s[1]-s[0]); Tbox=2*S
    k=(np.arange(NB)+.5)*math.pi/S; B=np.cos(np.outer(s,k))
    y0=np.interp(s,base['s'],base['y'],left=0,right=0); a0=(B.T@y0)*ds/S
    BF=np.fft.fft(B,axis=0)*ds; Om=2*math.pi*np.fft.fftfreq(NG,d=ds)
    return S,s,ds,Tbox,k,B,BF,Om,a0


def solve_tilt(tilt,ai0,ae0,geom):
    S,s,ds,Tbox,k,B,BF,Om,_=geom
    fd.BETA_COLD=.80; fd.DELTA_TILT=float(tilt)
    model=fd.DynamicForce(.6,quick=False,Tmax=.98)
    L,C,_=fd.CASES[.6]
    roots=model.roots(fd.T0); xm=max(x for x,kap in roots if x<0 and kap>0)
    kap=model._scalar(model.spline.ev(fd.T0,xm,dx=0,dy=1)); wc=math.sqrt(kap/(L*C))
    Ak=C*PHI_BAR**2*wc/HBAR; Av=(PHI_BAR**2/L)/(HBAR*wc)
    Kkin=np.diag(Ak*S*k*k)
    xgrid=np.linspace(xm-0.02,min(float(model.xgrid[-1]),1.55),60001)
    Fgrid=np.array([model.force(fd.T0,float(x)) for x in xgrid])
    Ugrid=cumulative_trapezoid(Fgrid,xgrid,initial=0.0); Ugrid-=float(np.interp(xm,xgrid,Ugrid))
    dFgrid=np.gradient(Fgrid,xgrid)
    Fv=lambda x:np.interp(x,xgrid,Fgrid,left=Fgrid[0],right=Fgrid[-1])
    Uv=lambda x:np.interp(x,xgrid,Ugrid,left=Ugrid[0],right=Ugrid[-1])
    dFv=lambda x:np.interp(x,xgrid,dFgrid,left=dFgrid[0],right=dFgrid[-1])
    ao=np.abs(Om); wd=ALPHA*wc; weight=ao*Y_laplace(wc*ao,R_ENV,wd)
    Kenv=(PHI_BAR**2/HBAR)*np.real(BF.conj().T@(weight[:,None]*BF))/Tbox; Kenv=.5*(Kenv+Kenv.T)
    def station(a,Kx):
        def grad(q): return (Kkin+Kx)@q+Av*(B.T@Fv(xm+B@q))*ds
        def jac(q):
            W=dFv(xm+B@q)
            return Kkin+Kx+Av*(B.T@(W[:,None]*B))*ds
        sol=root(grad,a,jac=jac,method='hybr',tol=2e-10,options={'maxfev':6000})
        q=np.asarray(sol.x); x=xm+B@q
        act=.5*float(q@(Kkin@q))+.5*float(q@(Kx@q))+Av*float(np.sum(Uv(x))*ds)
        ev=np.linalg.eigvalsh(jac(q))
        return q,act,sol.success,float(np.linalg.norm(grad(q),ord=np.inf)),float(x[np.argmin(np.abs(s))]),ev
    ai,Bi,si,gi,xi,evi=station(ai0,np.zeros_like(Kenv))
    ae,Be,se,ge,xe,eve=station(ae0,Kenv)
    return model,wc,ai,(Bi,si,gi,xi,evi),ae,(Be,se,ge,xe,eve)


def main():
    print('Experiment 03 low-tilt nonlocal bounce continuation')
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    try:
        geom=setup(); ai=geom[-1].copy(); ae=geom[-1].copy()
        for tilt in (.050,.045,.040,.035):
            model,wc,ai,oi,ae,oe=solve_tilt(tilt,ai,ae,geom)
            Bi,si,gi,xi,evi=oi; Be,se,ge,xe,eve=oe
            msg=(f'tilt={tilt:.3f}: fold={model.fold_temperature(hi=.95):.6f}K fc={wc/(2*math.pi)*1e-9:.5f}GHz '
                 f'Biso={Bi:.7f} Benv={Be:.7f} DeltaBenv={Be-Bi:.7f}; '
                 f'iso(success={si},grad={gi:.2e},nneg={int((evi<0).sum())}); '
                 f'env(success={se},grad={ge:.2e},nneg={int((eve<0).sum())},xc={xe:+.6f})')
            print(msg); print(f'::notice title=Experiment 03 low-tilt bounce::{msg}')
            if int((evi<0).sum())!=1 or int((eve<0).sum())!=1: raise RuntimeError('wrong negative mode count')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot

if __name__=='__main__': main()
