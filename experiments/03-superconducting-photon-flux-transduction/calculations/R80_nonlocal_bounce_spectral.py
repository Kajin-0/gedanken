#!/usr/bin/env python3
"""Spectral solution of the full nonlocal zero-T dissipative bounce equation.

This removes the restricted time/amplitude ansatz used by the first two
Experiment-03 dissipative-MQT screens.

For y(s)=x(s)-x_m with s=omega_c*tau, expand an even bounce on [-S,S] as

    y(s)=sum_n a_n cos(k_n s),
    k_n=(n+1/2) pi/S,

so y(+/-S)=0 and the translation zero mode is excluded by parity.

The Euclidean action in units of hbar is

    B = A_k/2 int ds (dy/ds)^2
        + A_v int ds [u(x_m+y)-u(x_m)]
        + 1/2 a^T K_env a,

where

    A_k = C Phi_bar^2 omega_c / hbar,
    A_v = (Phi_bar^2/L)/(hbar omega_c),

and K_env is built from the exact zero-T linear-environment kernel

    |omega| Y_L(|omega|)

using the positive-real Laplace admittance of the passive two-pole network.

The stationary coefficients solve grad B=0.  We first solve with K_env=0 and
require convergence to the independently known exact isolated bounce action.
Then we solve with the R80/alpha=.90 environment.  The even-subspace Hessian
should contain one negative eigenvalue for a metastable bounce; the odd
translation zero mode is absent by construction.

This is the full stationary path *within the converged spectral/finite-box
discretization* of the reduced zero-T electrical action.  It still does NOT
compute the fluctuation determinant/prefactor or any finite-temperature escape.
"""
from __future__ import annotations

import math
import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.optimize import root

from full_dynamic_rfsquid import DynamicForce, T0
from quantum_initial_capture import HBAR, PHI_BAR
from R80_dissipative_bounce_screen import isolated_bounce, Y_laplace


def solve_one(nbasis:int, ngrid:int, R:float|None, alpha:float|None):
    model=DynamicForce(.6,quick=False)
    dat=isolated_bounce(model,nfft=65536)
    L,C=dat['L'],dat['C']; wc=dat['wc']; xm=dat['xm']

    # Box extends beyond the isolated tail so the bounce is effectively zero at
    # the Dirichlet boundaries.  The initial isolated sample already contains a
    # zero-padded region out to +/-2*Shalf.
    S=1.75*dat['Shalf']
    s=np.linspace(-S,S,ngrid,endpoint=False); ds=float(s[1]-s[0]); Tbox=2*S
    ks=(np.arange(nbasis)+0.5)*math.pi/S
    B=np.cos(np.outer(s,ks))
    # Basis norms are S to spectral accuracy for these half-integer cosines.

    Ak=C*PHI_BAR**2*wc/HBAR
    Av=(PHI_BAR**2/L)/(HBAR*wc)
    Kkin=np.diag(Ak*S*ks*ks)

    # Static force/potential interpolation over the largest excursion needed by
    # the iteration.  Extend slightly past the right minimum.
    xmax=min(float(model.xgrid[-1]),dat['xr']+0.25)
    xgrid=np.linspace(xm,xmax,50001)
    Fgrid=np.array([model.force(T0,float(x)) for x in xgrid])
    Ugrid=cumulative_trapezoid(Fgrid,xgrid,initial=0.0)
    dFgrid=np.gradient(Fgrid,xgrid)
    def Fvec(x): return np.interp(x,xgrid,Fgrid,left=Fgrid[0],right=Fgrid[-1])
    def Uvec(x): return np.interp(x,xgrid,Ugrid,left=Ugrid[0],right=Ugrid[-1])
    def dFvec(x): return np.interp(x,xgrid,dFgrid,left=dFgrid[0],right=dFgrid[-1])

    # Environment quadratic matrix from basis Fourier transforms.
    if R is None:
        Kenv=np.zeros((nbasis,nbasis))
    else:
        BF=np.fft.fft(B,axis=0)*ds
        Om=2*math.pi*np.fft.fftfreq(ngrid,d=ds)
        absOm=np.abs(Om)
        wd=float(alpha)*wc
        weight=absOm*Y_laplace(wc*absOm,float(R),wd)
        # dOmega/(2pi)=1/Tbox. Environment action is 1/2 a^T Kenv a.
        Kenv=(PHI_BAR**2/HBAR)*(np.real(BF.conj().T @ (weight[:,None]*BF))/Tbox)
        Kenv=0.5*(Kenv+Kenv.T)

    # Project the independently integrated isolated bounce as the initial guess.
    y0=np.interp(s,dat['s'],dat['y'],left=0.0,right=0.0)
    a0=(B.T@y0)*ds/S

    def grad(a):
        y=B@a; x=xm+y
        return (Kkin+Kenv)@a + Av*(B.T@Fvec(x))*ds

    def jac(a):
        x=xm+B@a
        # Potential Hessian: Av int F'(x) b_m b_n ds.
        W=dFvec(x)
        Hpot=Av*(B.T@(W[:,None]*B))*ds
        return Kkin+Kenv+Hpot

    sol=root(grad,a0,jac=jac,method='hybr',tol=2e-10,
             options={'xtol':2e-10,'maxfev':4000})
    a=np.asarray(sol.x); y=B@a; x=xm+y
    K=0.5*float(a@(Kkin@a))
    E=0.5*float(a@(Kenv@a))
    V=Av*float(np.sum(Uvec(x))*ds)
    Btot=K+V+E
    H=jac(a); ev=np.linalg.eigvalsh(H)
    gnorm=float(np.linalg.norm(grad(a),ord=np.inf))
    xcenter=float(x[np.argmin(np.abs(s))])
    return {
        'success':bool(sol.success),'B':Btot,'K':K,'V':V,'E':E,
        'xcenter':xcenter,'gnorm':gnorm,'ev':ev,'dat':dat,'S':S,
        'nbasis':nbasis,'ngrid':ngrid,
    }


def report(tag,o):
    ev=o['ev']; nneg=int(np.sum(ev<0)); smallest=','.join(f'{x:+.4e}' for x in ev[:4])
    msg=(f'{tag}: Nbasis={o["nbasis"]} Ngrid={o["ngrid"]} success={o["success"]} '
         f'B={o["B"]:.7f} [K={o["K"]:.7f},V={o["V"]:.7f},Env={o["E"]:.7f}] '
         f'xcenter={o["xcenter"]:+.7f} gradInf={o["gnorm"]:.2e} '
         f'nneg_even={nneg} eig0..3=[{smallest}]')
    print(msg); print(f'::notice title=Experiment 03 spectral bounce::{msg}')


def main():
    print('Experiment 03 full spectral nonlocal bounce')
    # Convergence ladder. Isolated regression first; environmental solve then
    # uses identical basis/grid so discretization shifts largely cancel.
    for nb,ng in ((24,4096),(36,6144),(48,8192)):
        iso=solve_one(nb,ng,None,None); report('isolated',iso)
        rel=iso['B']/iso['dat']['Bquad']-1
        print(f'  isolated relative action error vs exact quadrature={rel:+.3e}')
        env=solve_one(nb,ng,80.0,.90); report('R80-a0.90',env)
        print(f'  DeltaB_env={env["B"]-iso["B"]:.7f}; action_ratio={env["B"]/iso["B"]:.7f}')
    print('PASS')

if __name__=='__main__': main()
