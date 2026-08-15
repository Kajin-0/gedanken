#!/usr/bin/env python3
"""Conditional Mahalanobis basin-margin screen at 14 um.

The fully stationary-history linear FDT covariance at left-well reformation is
strongly anisotropic.  A coordinate-only margin (x-x_s)/sigma_x can therefore
be misleading.

This script computes the reduced phase covariance Sigma in z=(x,u),
u=v/omega_c, at reformation and probes the *future deterministic basin* in
standardized coordinates

    delta z = r Sigma^(1/2) e_theta.

The filter-memory variables d,w and thermal state are held at their deterministic
reformation values while x,u are perturbed.  The full nonlinear causal-filter
recovery is then integrated forward.  The smallest radius that no longer gives
a clearly right-basin tail is reported as a conditional Mahalanobis basin
radius.

IMPORTANT
---------
This is not a physical capture probability:
- future bath noise is omitted;
- system/bath correlations not representable by reduced (x,u) are conditioned
  on the deterministic memory state;
- Sigma itself is a linear symmetrized-FDT covariance;
- near a true nonlinear quantum basin boundary the approximation can fail.

Its purpose is narrower: determine whether the alarming <1-sigma x projection
at 14 um is simply a projection artifact of a long thin covariance filament.
"""

from __future__ import annotations

import math

import numpy as np
from scipy.integrate import solve_ivp

from causal_two_pole_environment import filter_components
from directional_recovery_barriers import directional_barriers
from full_dynamic_rfsquid import (
    CASES,
    DynamicForce,
    T0,
    TAU0_CONDITIONAL,
    adiabatic_photon_temperature,
)
from history_fdt_reformation_margin import stationary_history_variance
from linearized_fdt_reformation_margin import deterministic_to_reform


def phase_covariance(model,R,alpha):
    vx,tf,yf,wc,wd,Tf,_,_,_=stationary_history_variance(model,R,alpha,[1,0,0,0])
    vu=stationary_history_variance(model,R,alpha,[0,1/wc,0,0])[0]
    vs=stationary_history_variance(model,R,alpha,[1,1/wc,0,0])[0]
    cov=0.5*(vs-vx-vu)
    M=np.array([[vx,cov],[cov,vu]],float)
    return M,tf,yf,wc,wd,Tf


def future_classification(model,R,alpha,tf,yf,wc,x0,u0,*,tend_ns=1.0,rise_ps=20.0,lambda_um=14.0):
    L,C,_=CASES[0.6]
    wd=alpha*wc
    Lf,Cf=filter_components(R,wd)
    Tad=adiabatic_photon_temperature(lambda_um,100.0)
    ubase=T0*T0
    du_total=Tad*Tad-ubase
    cool_coeff=1/(2*TAU0_CONDITIONAL*ubase)
    tau_r=rise_ps*1e-12
    def source(t): return du_total/tau_r*math.exp(-t/tau_r)
    def rhs(t,y):
        x,v,uth,d,w=y
        uth=max(float(uth),ubase); T=math.sqrt(uth)
        F=model.force(T,x)
        return np.array([
            v,
            -(d+F)/(L*C),
            source(t)-cool_coeff*(uth*uth-ubase*ubase),
            (L/Lf)*(v-w),
            d/(L*Cf)-w/(R*Cf),
        ])
    ystart=np.array([x0,u0*wc,float(yf[2]),float(yf[3]),float(yf[4])])
    tend=tf+tend_ns*1e-9
    tail_start=tend-0.12e-9
    teval=np.linspace(tail_start,tend,81)
    sol=solve_ivp(rhs,(tf,tend),ystart,t_eval=teval,method='DOP853',
                  rtol=3e-7,atol=np.array([2e-9,1e3,1e-12,2e-9,1e3]),
                  max_step=0.5e-12)
    xs=sol.y[0]
    Tfinal=math.sqrt(max(float(sol.y[2,-1]),ubase))
    roots=model.roots(Tfinal)
    saddles=[x for x,k in roots if k<0]
    if not saddles:
        return 'mixed'
    saddle=min(saddles,key=abs)
    # Conservative tail classifier.  A true right basin must remain on the
    # right of the separating saddle over the last 120 ps.
    if np.min(xs)>saddle:
        return 'right'
    if np.max(xs)<saddle:
        return 'left'
    return 'mixed'


def boundary_radius(model,R,alpha,*,nangle=24,rmax=8.0):
    M,tf,yf,wc,wd,Tf=phase_covariance(model,R,alpha)
    ev,Q=np.linalg.eigh(M)
    if np.min(ev)<=0:
        raise RuntimeError(f'non-positive reduced covariance {ev}')
    S=Q@np.diag(np.sqrt(ev))
    zdet=np.array([float(yf[0]),float(yf[1])/wc])
    center=future_classification(model,R,alpha,tf,yf,wc,zdet[0],zdet[1])
    if center!='right':
        raise RuntimeError(f'deterministic center is not robustly right: {center}')

    rows=[]
    best=(math.inf,None,None)
    for j in range(nangle):
        theta=2*math.pi*j/nangle
        e=np.array([math.cos(theta),math.sin(theta)])
        direction=S@e
        lo=0.0; hi=None; label='right'
        # coarse radial search
        for r in np.arange(0.5,rmax+0.001,0.5):
            z=zdet+r*direction
            label=future_classification(model,R,alpha,tf,yf,wc,float(z[0]),float(z[1]))
            if label!='right':
                hi=float(r); lo=float(r-0.5); break
        if hi is None:
            rows.append((theta,math.inf,'right_to_rmax'))
            continue
        # conservative first non-right boundary
        for _ in range(9):
            mid=0.5*(lo+hi)
            z=zdet+mid*direction
            lab=future_classification(model,R,alpha,tf,yf,wc,float(z[0]),float(z[1]))
            if lab=='right': lo=mid
            else: hi=mid; label=lab
        rb=hi
        rows.append((theta,rb,label))
        if rb<best[0]: best=(rb,theta,label)
    return M,ev,Q,zdet,tf,yf,wc,Tf,rows,best


def main():
    print('Experiment 03 conditional Mahalanobis basin geometry at 14 um')
    print('rDelta=.6, R=250 ohm; future bath noise omitted')
    model=DynamicForce(0.6,quick=False,Tmax=0.86)
    for alpha in (0.20,0.35,0.50):
        M,ev,Q,zdet,tf,yf,wc,Tf,rows,best=boundary_radius(model,250.0,alpha)
        sig=np.sqrt(ev)
        major=Q[:,1]
        msg=(
            f'alpha={alpha:.2f}: principal_rms=[{sig[0]:.5f},{sig[1]:.5f}], '
            f'major_slope_u/x={major[1]/major[0]:+.5f}, '
            f'zdet=({zdet[0]:+.5f},{zdet[1]:+.5f}), '
            f'r_min={best[0]:.4f}, theta_min={best[1]:.4f} rad, boundary_label={best[2]}'
        )
        print('\n'+msg)
        print(f'::notice title=Experiment 03 Mahalanobis basin margin::{msg}')
        for th,r,lab in rows:
            rr='inf' if not math.isfinite(r) else f'{r:.4f}'
            print(f'  theta={th:.4f} r_boundary={rr} label={lab}')
    print('PASS')

if __name__=='__main__':
    main()
