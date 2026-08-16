#!/usr/bin/env python3
"""Phase-coordinate DVR benchmark for the next exact quantum-capture calculation.

This is deliberately a *basis/initial-state* regression, not a quantum-efficiency
calculation.  It uses the current safe-optimum neighborhood (default delta=.2125)
and the exact same static force model.

Hamiltonian for q=Phi_bar x:

    H = -hbar^2/(2 C Phi_bar^2) d^2/dx^2 + U(x,T),

with

    U(x,T) = (Phi_bar^2/L) integral F(x,T) dx.

Two spectra are computed:

1. full tilted-double-well spectrum on a large box;
2. left-metastable-well restricted spectrum with a Dirichlet wall at the cold
   separating saddle.

The second is the controlled low-T initialization benchmark.  It must reproduce
the local harmonic spacing hbar*omega_m as the grid/domain are converged.

The script also evaluates the photon-heated potential at the reduced-model
14-um / 500-um^2 adiabatic temperature to confirm that the left well has been
removed and to establish the energy/basis window needed for later unitary pulse
propagation.
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
    ev,vec=eigsh(H,k=k,which='SA',tol=2e-11,maxiter=100000)
    ii=np.argsort(ev); ev=ev[ii]; vec=vec[:,ii]
    # Normalize to integral |psi|^2 dx = 1 rather than Euclidean vector norm.
    dx=x[1]-x[0]; vec=vec/math.sqrt(dx)
    return x,U,ev,vec


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
        km=float(model.spline.ev(fd.T0,xm,dx=0,dy=1).reshape(-1)[0])
        wm=math.sqrt(km/(L0*C)); harmK=HBAR*wm/KB
        Tf=model.fold_temperature(hi=.98); Tad=fd.adiabatic_photon_temperature(14.,500.)
        nbar=1/(math.exp(HBAR*wm/(KB*fd.T0))-1)
        print(f'delta={delta:.5f} r={r:.9f} C={C*1e12:.6f}pF '
              f'xm={xm:+.8f} xs={xs:+.8f} xr={xr:+.8f} '
              f'fm={wm/(2*math.pi)*1e-9:.7f}GHz hbarwm/kB={harmK:.8f}K '
              f'nbar20mK={nbar:.8e} Tf={Tf:.8f}K Tad14umA500={Tad:.8f}K')

        # Restricted metastable left-well convergence.  The left box boundary is
        # moved as a regression; the saddle wall is fixed by the physical static
        # topology.  Only lowest states well below the saddle are interpreted.
        configs=(( -2.6,1400),( -3.2,1800),( -3.8,2200))
        refs=[]
        for xmin,n in configs:
            x,U,e,v=spectrum(model,fd.T0,C,xmin,xs,n,12)
            spac=(e[1]-e[0])/KB
            x0=expectation_x(x,v[:,0])
            refs.append(e[:8]/KB)
            print(f'LEFT xmin={xmin:+.2f} N={n}: E0/kB={e[0]/KB:.9f}K '
                  f'dE01/kB={spac:.9f}K ratio_to_harm={spac/harmK:.9f} '
                  f'<x>0={x0:+.9f} boundaryU/kB=({U[0]/KB:.4f},{U[-1]/KB:.4f})')
        ref=refs[-1]
        for j,z in enumerate(refs[:-1]):
            err=float(np.max(np.abs(z-ref)))
            print(f'LEFT convergence config{j}->final max|Delta E_0..7|/kB={err:.6e}K')

        # Full-box convergence and localization anatomy.  Because the right well
        # is energetically favored, the global ground state is *not* the detector
        # preparation; this spectrum is only the propagation basis benchmark.
        full=[]
        for xmax,n in ((3.2,1800),(3.8,2200)):
            x,U,e,v=spectrum(model,fd.T0,C,-xmax,xmax,n,36)
            means=[expectation_x(x,v[:,j]) for j in range(10)]
            full.append(e[:30]/KB)
            print(f'FULL X={xmax:.1f} N={n}: E0..5/kB=' + ','.join(f'{q:.6f}' for q in e[:6]/KB))
            print('FULL <x> states0..9=' + ','.join(f'{q:+.5f}' for q in means))
        print(f'FULL convergence max|Delta E_0..29|/kB={np.max(np.abs(full[0]-full[1])):.6e}K')

        # Hot full-box spectrum / topology at the lumped adiabatic photon scale.
        hotroots=model.roots(Tad)
        x,U,e,v=spectrum(model,Tad,C,-3.8,3.8,2200,36)
        print('HOT roots=' + ','.join(f'({q:+.6f},{k:+.6f})' for q,k in hotroots))
        print('HOT E0..9/kB=' + ','.join(f'{q:.6f}' for q in e[:10]/KB))
        print('HOT <x> states0..9=' + ','.join(f'{expectation_x(x,v[:,j]):+.5f}' for j in range(10)))

        # Acceptance: low left-well spacing should be close to local harmonic
        # scale and lowest restricted levels/domain should be numerically stable.
        ratio=(refs[-1][1]-refs[-1][0])/harmK
        maxerr=float(np.max(np.abs(refs[-2]-refs[-1])))
        msg=(f'delta={delta:.5f}: restricted_spacing_ratio={ratio:.8f} '
             f'restricted_domain_E0to7_shift={maxerr:.3e}K '
             f'cold_full_basis_E0to29_shift={np.max(np.abs(full[0]-full[1])):.3e}K '
             f'hot_left_min_exists={any(q<0 and k>0 for q,k in hotroots)}')
        print(msg); print(f'::notice title=Experiment 03 phase DVR basis::{msg}')
        if abs(ratio-1)>.08: raise RuntimeError('restricted left-well spacing too far from harmonic benchmark')
        if maxerr>3e-4: raise RuntimeError('restricted left-well spectrum not domain converged')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot; fd.CASES[.6]=original


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--delta',type=float,default=.21250); a=ap.parse_args()
    d=round(a.delta,5)
    if d not in ROOTS: raise SystemExit(f'supported: {tuple(ROOTS)}')
    run(d)

if __name__=='__main__': main()
