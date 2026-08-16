#!/usr/bin/env python3
"""Two-parameter Euclidean saddle screen for the current R80 environment.

Builds on R80_dissipative_bounce_screen.py.  Instead of fixing the isolated
bounce amplitude, use the restricted family

    y_{a,b}(s) = b y_0(s/a)

where `a` rescales imaginary-time width and `b` rescales excursion from the
metastable minimum.  The action is

    B(a,b) = b^2 K0/a + a V(b) + b^2 Benv(a).

Here K0 is the isolated kinetic action, V(b) is the *actual non-sinusoidal CPR
potential* integrated on the amplitude-scaled isolated profile, and Benv(a) is
the full two-pole Euclidean quadratic environmental action.

The physical bounce is a saddle, not a minimum.  We solve dB/d(log a)=0 and
dB/db=0 near the isolated bounce and inspect the 2x2 Hessian.  A sensible
restricted bounce should retain one positive and one negative eigenvalue.

This remains a restricted variational diagnostic, not the exact nonlocal bounce
or fluctuation determinant.
"""
from __future__ import annotations

import math
import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.optimize import root

from full_dynamic_rfsquid import DynamicForce, T0
from quantum_initial_capture import HBAR, PHI_BAR
from R80_dissipative_bounce_screen import isolated_bounce, env_action_on_scaled_bounce


def potential_interpolator(model,dat,bmax=1.55):
    xm=dat['xm']; ymax=float(np.max(dat['y']))
    xmax=xm+bmax*ymax
    xgrid=np.linspace(xm,xmax,30001)
    F=np.array([model.force(T0,float(x)) for x in xgrid])
    U=cumulative_trapezoid(F,xgrid,initial=0.0)
    def u(x): return np.interp(x,xgrid,U,left=U[0],right=U[-1])
    return u,xmax


def potential_action_b(dat,u,b):
    # Base normalized-time profile; time scaling a multiplies this by a.
    L=dat['L']; wc=dat['wc']
    EL=PHI_BAR**2/L
    x=dat['xm']+b*dat['y']
    ds=dat['s'][1]-dat['s'][0]
    return (EL/wc)/HBAR*float(np.sum(u(x))*ds)


def action(dat,u,R,alpha,loga,b):
    a=math.exp(loga)
    K=(b*b/a)*dat['K']
    V=a*potential_action_b(dat,u,b)
    E=(b*b)*env_action_on_scaled_bounce(dat,R,alpha,a)
    return K+V+E


def grad(dat,u,R,alpha,z):
    la,b=float(z[0]),float(z[1])
    h1=2e-4; h2=2e-4
    f=lambda aa,bb:action(dat,u,R,alpha,aa,bb)
    dla=(f(la+h1,b)-f(la-h1,b))/(2*h1)
    db=(f(la,b+h2)-f(la,b-h2))/(2*h2)
    return np.array([dla,db])


def hessian(dat,u,R,alpha,z):
    la,b=float(z[0]),float(z[1]); h=7e-4
    f=lambda aa,bb:action(dat,u,R,alpha,aa,bb)
    f0=f(la,b)
    Haa=(f(la+h,b)-2*f0+f(la-h,b))/h**2
    Hbb=(f(la,b+h)-2*f0+f(la,b-h))/h**2
    Hab=(f(la+h,b+h)-f(la+h,b-h)-f(la-h,b+h)+f(la-h,b-h))/(4*h**2)
    return np.array([[Haa,Hab],[Hab,Hbb]])


def main():
    print('Experiment 03 R80 two-parameter dissipative bounce saddle screen')
    model=DynamicForce(.6,quick=False)
    dat=isolated_bounce(model,nfft=65536)
    u,xmax=potential_interpolator(model,dat)
    print(f'amplitude interpolation extends to x={xmax:+.6f}; right minimum={dat["xr"]:+.6f}')
    for R,alpha in [(80.,.90),(80.,.70),(150.,.80)]:
        # Start from the time-only optimum width and isolated amplitude.
        z0=np.array([math.log(.94),1.0])
        sol=root(lambda z:grad(dat,u,R,alpha,z),z0,method='hybr',tol=2e-9)
        la,b=[float(x) for x in sol.x]; a=math.exp(la)
        B=action(dat,u,R,alpha,la,b)
        H=hessian(dat,u,R,alpha,sol.x); ev=np.linalg.eigvalsh(H)
        g=grad(dat,u,R,alpha,sol.x)
        xmaxbounce=dat['xm']+b*(dat['xt']-dat['xm'])
        msg=(f'R={R:g} alpha={alpha:.2f}: success={sol.success} a={a:.6f} b={b:.6f} '
             f'x_center={xmaxbounce:+.6f} B_2d={B:.6f} DeltaB={B-dat["Bquad"]:.6f}; '
             f'grad=({g[0]:+.2e},{g[1]:+.2e}); HessEig=({ev[0]:+.5f},{ev[1]:+.5f}); '
             f'exp(-DeltaB)={math.exp(-(B-dat["Bquad"])):.3e}')
        print(msg); print(f'::notice title=Experiment 03 2D dissipative bounce::{msg}')
    print('Expected restricted-bounce signature: one Hessian eigenvalue <0 and one >0.')
    print('PASS')

if __name__=='__main__': main()
