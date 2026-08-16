#!/usr/bin/env python3
"""Propagator-only basin-volume stress for the causal Drude environment.

This intentionally keeps the *same isolated harmonic Gaussian* in (x,v) and
sets the Drude auxiliary current j0=0.  It therefore isolates how causal memory
and reactive loading change the pulled-back target basin.  It is NOT a physical
capture efficiency because the initial state is not the correlated equilibrium
state of the Drude-coupled circuit and pulse-time bath noise is absent.
"""
from __future__ import annotations
import math
import numpy as np
from scipy.integrate import solve_ivp, simpson
from scipy.special import ndtr

from full_dynamic_rfsquid import CASES, DynamicForce, T0, TAU0_CONDITIONAL, adiabatic_photon_temperature
from finite_time_basin_slice import cold_phase_scale
from quantum_initial_capture import quantum_covariance

SQRT2PI=math.sqrt(2*math.pi)

def normal_pdf(z): return np.exp(-0.5*z*z)/SQRT2PI


def basin_label(model,R0,d,x0,u_norm,omega0,rise_ps=20.0,tend_ns=0.8):
    r=0.6; L,C,_=CASES[r]; left,right=model.cold_states()
    omegaD=d*omega0; tauD=1/omegaD; G0=1/R0
    Tad=adiabatic_photon_temperature(14.0,100.0)
    uT0=T0*T0; du=Tad*Tad-uT0; tau_r=rise_ps*1e-12
    cool=1/(2*TAU0_CONDITIONAL*uT0)
    def rhs(t,y):
        x,v,j,uT=y; uT=max(float(uT),uT0); T=math.sqrt(uT)
        src=du/tau_r*math.exp(-t/tau_r)
        return np.array([v,-(L*j+model.force(T,x))/(L*C),(G0*v-j)/tauD,
                         src-cool*(uT*uT-uT0*uT0)])
    sol=solve_ivp(rhs,(0,tend_ns*1e-9),np.array([x0,u_norm*omega0,0.0,uT0]),
                  method='DOP853',rtol=7e-7,
                  atol=np.array([2e-9,1e3,1e-7,1e-12]),max_step=5e-12)
    xf=float(sol.y[0,-1])
    return 'right' if abs(xf-right)<abs(xf-left) else 'left'


def p_right_given_x(model,R0,d,x0,sigma_u,omega0,zmax=5.5,nscan=65):
    umax=zmax*sigma_u
    grid=np.linspace(-umax,umax,nscan)
    labs=[basin_label(model,R0,d,x0,float(u),omega0) for u in grid]
    edges=[]
    for ua,ub,la,lb in zip(grid[:-1],grid[1:],labs[:-1],labs[1:]):
        if la==lb: continue
        lo=float(ua); hi=float(ub); leftlab=la
        for _ in range(12):
            mid=0.5*(lo+hi)
            lm=basin_label(model,R0,d,x0,mid,omega0)
            if lm==leftlab: lo=mid
            else: hi=mid
        edges.append((0.5*(lo+hi),la,lb))
    bounds=[-math.inf]+[e[0] for e in edges]+[math.inf]
    ilabs=[labs[0]]+[e[2] for e in edges]
    p=0.0
    for lo,hi,lab in zip(bounds[:-1],bounds[1:],ilabs):
        if lab!='right': continue
        plo=0.0 if lo==-math.inf else float(ndtr(lo/sigma_u))
        phi=1.0 if hi==math.inf else float(ndtr(hi/sigma_u))
        p+=phi-plo
    return p,len(edges)


def integrate(model,R0,d,nxs=(9,17),zmax_x=4.5):
    cov=quantum_covariance(model,0.6); sx=cov['sigma_x']; su=cov['sigma_v']/cov['omega_c']
    nmax=max(nxs); zfine=np.linspace(-zmax_x,zmax_x,nmax)
    pc=[]; ec=[]
    for z in zfine:
        p,e=p_right_given_x(model,R0,d,cov['x_c']+sx*float(z),su,cov['omega_c'])
        pc.append(p); ec.append(e)
    pc=np.asarray(pc); ec=np.asarray(ec)
    for nx in nxs:
        step=(nmax-1)//(nx-1); z=zfine[::step]
        p=float(simpson(pc[::step]*normal_pdf(z),x=z))
        tail=2*(1-float(ndtr(zmax_x)))
        msg=(f"R0={R0:g}ohm d={d:g}: nx={nx} Pprop={p:.6f}; tail<={tail:.3e}; "
             f"edges={int(ec.min())}..{int(ec.max())}")
        print(msg); print(f"::notice title=Experiment 03 Drude propagator basin::{msg}")


def main():
    m=DynamicForce(0.6,quick=False)
    for d in (5.0,10.0): integrate(m,250.0,d)
    print('PASS')

if __name__=='__main__': main()
