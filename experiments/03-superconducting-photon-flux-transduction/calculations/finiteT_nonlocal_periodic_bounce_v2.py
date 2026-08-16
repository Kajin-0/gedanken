#!/usr/bin/env python3
"""Scalar-safe wrapper for finiteT_nonlocal_periodic_bounce.py.

The v1 workflow exposed a pure NumPy/scipy scalar-conversion bug before any
finite-T physics was evaluated.  This wrapper replaces only `static_model` and
`exact_crossover` with versions using DynamicForce._scalar(), then reuses the
same periodic action, Matsubara kernel, continuation, Hessian tests and
sphaleron regression from v1.
"""
from __future__ import annotations
import argparse, math
import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.optimize import brentq

import full_dynamic_rfsquid as fd
import finiteT_nonlocal_periodic_bounce as ft
from directional_recovery_barriers import directional_barriers
from R80_dissipative_bounce_screen import Y_laplace
from quantum_initial_capture import HBAR, KB, PHI_BAR


def static_model(delta:float,C:float,R:float):
    fd.BETA_COLD=.80
    fd.DELTA_TILT=float(delta)
    model=fd.DynamicForce(.6,quick=False,Tmax=.98)
    roots=model.roots(fd.T0)
    xm=max(x for x,kap in roots if x<0 and kap>0)
    xs=min((x for x,kap in roots if kap<0 and x>xm), key=lambda z:z-xm)
    xr=min((x for x,kap in roots if x>xs and kap>0), key=lambda z:z-xs)
    xm=model._scalar(xm); xs=model._scalar(xs); xr=model._scalar(xr)
    km=model._scalar(model.spline.ev(fd.T0,xm,dx=0,dy=1))
    Fs=model._scalar(model.spline.ev(fd.T0,xs,dx=0,dy=1))
    wc=math.sqrt(km/(ft.L0*C)); wd=ft.ALPHA*wc
    b=directional_barriers(model,fd.T0)
    barrier_dimless=model._scalar(b['b_left'])
    barrierK=barrier_dimless*(PHI_BAR**2/ft.L0)/KB

    xlo=max(model._scalar(model.xgrid[0]),xm-.25)
    xhi=min(model._scalar(model.xgrid[-1]),xr+.45)
    xgrid=np.linspace(xlo,xhi,70001)
    Fgrid=np.array([model.force(fd.T0,float(x)) for x in xgrid])
    Ugrid=cumulative_trapezoid(Fgrid,xgrid,initial=0.0)
    Ugrid-=float(np.interp(xm,xgrid,Ugrid))
    dFgrid=np.gradient(Fgrid,xgrid)
    Fv=lambda x:np.interp(x,xgrid,Fgrid,left=Fgrid[0],right=Fgrid[-1])
    Uv=lambda x:np.interp(x,xgrid,Ugrid,left=Ugrid[0],right=Ugrid[-1])
    dFv=lambda x:np.interp(x,xgrid,dFgrid,left=dFgrid[0],right=dFgrid[-1])
    return dict(model=model,xm=xm,xs=xs,xr=xr,km=km,Fs=Fs,wc=wc,wd=wd,
                barrierK=barrierK,Fv=Fv,Uv=Uv,dFv=dFv,C=C,R=R)


def exact_crossover(st):
    C,R,wc,wd,Fs=st['C'],st['R'],st['wc'],st['wd'],st['Fs']
    model=st['model']
    def lam(T):
        nu=2*math.pi*KB*T/HBAR
        Y=model._scalar(Y_laplace(nu,R,wd))
        return C*nu*nu + nu*Y + Fs/ft.L0
    Tx=brentq(lam,1e-6,.5,xtol=2e-14,rtol=2e-13,maxiter=400)
    return Tx,lam


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--delta',type=float,required=True)
    ap.add_argument('--nbasis',type=int,default=48)
    ap.add_argument('--ngrid',type=int,default=6144)
    a=ap.parse_args(); delta=round(a.delta,3)
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    old_static,old_cross=ft.static_model,ft.exact_crossover
    try:
        ft.static_model=static_model
        ft.exact_crossover=exact_crossover
        ft.run_delta(delta,a.nbasis,a.ngrid)
        print('PASS')
    finally:
        ft.static_model=old_static
        ft.exact_crossover=old_cross
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot

if __name__=='__main__': main()
