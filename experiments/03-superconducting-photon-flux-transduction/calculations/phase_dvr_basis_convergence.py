#!/usr/bin/env python3
"""Phase-coordinate DVR benchmark for the next exact quantum-capture calculation.

This is deliberately a *basis/initial-state* regression, not a quantum-efficiency
calculation. It uses the current safe-optimum neighborhood (default delta=.2125)
and the exact same static force model.

Hamiltonian for q=Phi_bar x:

    H = -hbar^2/(2 C Phi_bar^2) d^2/dx^2 + U(x,T),

with

    U(x,T) = (Phi_bar^2/L) integral F(x,T) dx.

Two spectra are computed:

1. full tilted-double-well spectrum on a large box;
2. left-metastable-well restricted spectrum with a Dirichlet wall at the cold
   separating saddle.

The second is the controlled low-T initialization benchmark. It must reproduce
the local harmonic spacing hbar*omega_m as the grid/domain are converged.

IMPORTANT NUMERICAL NOTE
------------------------
The second-difference kinetic diagonal is tens of kelvin per grid point while
the desired low-lying eigenvalues are sub-kelvin. A first version used raw
`eigsh(...,which='SA')`; ARPACK returned spurious interior Ritz values without
raising an exception. The retained implementation therefore uses shift-invert
around the potential minimum and explicitly checks every eigenpair residual.
"""
from __future__ import annotations

import argparse, math
import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh

import full_dynamic_rfsquid as fd
from quantum_initial_capture import HBAR, KB, PHI_BAR

L0=111.5e-12; C0=215e-15
ROOTS={
    .21200:10.62175909,
    .21225:10.749111487,
    .21250:10.885578211,
    .21275:11.035674041,
    .21300:11.2051409652,
}


def potential_J(model,T,x):
    Tarr=np.full_like(x,float(T)); F=np.asarray(model.spline.ev(Tarr,x)).reshape(-1)
    V=cumulative_trapezoid(F,x,initial=0.0)
    U=(PHI_BAR**2/L0)*V
    U-=U.min()
    return U,F


def hamiltonian(U,x,C):
    dx=float(x[1]-x[0])
    t=HBAR**2/(2*C*PHI_BAR**2*dx*dx)
    n=len(x)
    H=diags((-t*np.ones(n-1),2*t*np.ones(n)+U,-t*np.ones(n-1)),(-1,0,1),format='csc')
    return H,t


def spectrum(model,T,C,xmin,xmax,n,k):
    # Interior points implement Dirichlet walls at xmin/xmax.
    x=np.linspace(xmin,xmax,n+2)[1:-1]
    U,F=potential_J(model,T,x)
    H,t=hamiltonian(U,x,C)
    # Shift-invert is essential here: the finite-difference kinetic diagonal is
    # O(10-100 K), while the target spectrum is O(0.1 K).  sigma=0 returns the
    # eigenvalues closest to the physical potential minimum.
    ev,vec=eigsh(H,k=k,sigma=0.0,which='LM',tol=2e-12,maxiter=100000)
    ii=np.argsort(ev); ev=ev[ii]; vec=vec[:,ii]
    # Reject silent Ritz failures. vec is still Euclidean-normalized here.
    residuals=np.array([np.linalg.norm(H@vec[:,j]-ev[j]*vec[:,j])/KB for j in range(k)])
    if float(residuals.max())>2e-7:
        raise RuntimeError(f'DVR eigenpair residual too large: max={residuals.max():.3e} K')
    # Normalize to integral |psi|^2 dx = 1 rather than Euclidean vector norm.
    dx=x[1]-x[0]; vec=vec/math.sqrt(dx)
    return x,U,ev,vec,residuals


def expectation_x(x,psi):
    dx=x[1]-x[0]
    return float(np.sum(np.abs(psi)**2*x)*dx)


def run(delta):
    r=ROOTS[delta]; C=C0*r*r
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT; original=fd.CASES[.6]
    try:
        fd.BETA_COLD=.80; fd.DELTA_TILT=delta; fd.CASES[.6]=(L0,C,original[2])
        model=fd.DynamicForce(.6,quick=False,Tmax=1.02)
        roots=model.roots(fd.T0)
        mins=[(x,k) for x,k in roots if k>0]; saddles=[(x,k) for x,k in roots if k<0]
        xm=max(x for x,k in mins if x<0); xr=min(x for x,k in mins if x>0)
        xs=min(saddles,key=lambda z:abs(z[0]))[0]
        km=float(np.asarray(model.spline.ev(fd.T0,xm,dx=0,dy=1)).reshape(-1)[0])
        wm=math.sqrt(km/(L0*C)); harmK=HBAR*wm/KB
        Tf=model.fold_temperature(hi=.98); Tad=fd.adiabatic_photon_temperature(14.,500.)
        nbar=1/(math.exp(HBAR*wm/(KB*fd.T0))-1)
        print(f'delta={delta:.5f} r={r:.9f} C={C*1e12:.6f}pF '
              f'xm={xm:+.8f} xs={xs:+.8f} xr={xr:+.8f} '
              f'fm={wm/(2*math.pi)*1e-9:.7f}GHz hbarwm/kB={harmK:.8f}K '
              f'nbar20mK={nbar:.8e} Tf={Tf:.8f}K Tad14umA500={Tad:.8f}K')

        configs=((-2.6,1400),(-3.2,1800),(-3.8,2200))
        refs=[]; rmax=[]
        for xmin,n in configs:
            x,U,e,v,res=spectrum(model,fd.T0,C,xmin,xs,n,12)
            spac=(e[1]-e[0])/KB
            x0=expectation_x(x,v[:,0])
            refs.append((e[:8]-e[0])/KB); rmax.append(float(res.max()))
            print(f'LEFT xmin={xmin:+.2f} N={n}: E0/kB={e[0]/KB:.9f}K '
                  f'dE01/kB={spac:.9f}K ratio_to_harm={spac/harmK:.9f} '
                  f'<x>0={x0:+.9f} boundaryU/kB=({U[0]/KB:.4f},{U[-1]/KB:.4f}) '
                  f'maxResidual/kB={res.max():.3e}K')
        ref=refs[-1]
        for j,z in enumerate(refs[:-1]):
            err=float(np.max(np.abs(z-ref)))
            print(f'LEFT convergence config{j}->final max|Delta (E_n-E0)_0..7|/kB={err:.6e}K')

        full=[]; fullres=[]
        for xmax,n in ((3.2,1800),(3.8,2200)):
            x,U,e,v,res=spectrum(model,fd.T0,C,-xmax,xmax,n,36)
            means=[expectation_x(x,v[:,j]) for j in range(10)]
            full.append((e[:30]-e[0])/KB); fullres.append(float(res.max()))
            print(f'FULL X={xmax:.1f} N={n}: (E0..5-E0)/kB=' + ','.join(f'{q:.6f}' for q in (e[:6]-e[0])/KB))
            print('FULL <x> states0..9=' + ','.join(f'{q:+.5f}' for q in means))
            print(f'FULL maxResidual/kB={res.max():.3e}K')
        fullshift=float(np.max(np.abs(full[0]-full[1])))
        print(f'FULL convergence max|Delta (E_0..29-E0)|/kB={fullshift:.6e}K')

        hotroots=model.roots(Tad)
        x,U,e,v,res=spectrum(model,Tad,C,-3.8,3.8,2200,36)
        print('HOT roots=' + ','.join(f'({q:+.6f},{k:+.6f})' for q,k in hotroots))
        print('HOT (E0..9-E0)/kB=' + ','.join(f'{q:.6f}' for q in (e[:10]-e[0])/KB))
        print('HOT <x> states0..9=' + ','.join(f'{expectation_x(x,v[:,j]):+.5f}' for j in range(10)))
        print(f'HOT maxResidual/kB={res.max():.3e}K')

        ratio=(refs[-1][1]-refs[-1][0])/harmK
        maxerr=float(np.max(np.abs(refs[-2]-refs[-1])))
        msg=(f'delta={delta:.5f}: restricted_spacing_ratio={ratio:.8f} '
             f'restricted_domain_transition_shift={maxerr:.3e}K '
             f'cold_full_transition_shift={fullshift:.3e}K '
             f'max_eigen_residual={max(rmax+fullres+[float(res.max())]):.3e}K '
             f'hot_left_min_exists={any(q<0 and k>0 for q,k in hotroots)}')
        print(msg); print(f'::notice title=Experiment 03 phase DVR basis::{msg}')
        if abs(ratio-1)>.08: raise RuntimeError('restricted left-well spacing too far from harmonic benchmark')
        if maxerr>3e-4: raise RuntimeError('restricted left-well transition spectrum not domain converged')
        if fullshift>3e-3: raise RuntimeError('full-box low-energy transition spectrum not domain converged')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot; fd.CASES[.6]=original


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--delta',type=float,default=.21250); a=ap.parse_args()
    d=round(a.delta,5)
    if d not in ROOTS: raise SystemExit(f'supported: {tuple(ROOTS)}')
    run(d)

if __name__=='__main__': main()
