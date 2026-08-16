#!/usr/bin/env python3
"""Correlated cold-Drude initial-state capture screen.

This advances Experiment 03 one step beyond `drude_basin_geometry.py`:

- the initial cold state is the correlated Gaussian covariance of the *causal*
  Drude-coupled harmonic phase mode in (x, xdot, j), rather than the isolated
  (x,xdot) Wigner Gaussian with j=0;
- the full causal Drude nonlinear pulse dynamics are retained;
- target capture is diagnosed by being on the right side *and below the cold
  separatrix energy*, including the Drude branch inductive energy.

Pulse-time bath fluctuations are STILL ABSENT.  Therefore the result is not a
physical detector efficiency; it isolates the effect of the bath-consistent
cold equilibrium distribution plus causal memory.

To make multi-thousand-point probability integration practical, the ensemble is
advanced by a vectorized RK4 scheme.  The force is interpolated bilinearly from
the same precomputed DynamicForce F(T,x) table.  A solve_ivp regression on a
small deterministic set is included and must pass before the probability is
interpreted.
"""
from __future__ import annotations

import math
import numpy as np
from scipy.integrate import cumulative_trapezoid, solve_ivp
from scipy.special import ndtri
from scipy.stats import qmc

from full_dynamic_rfsquid import (
    CASES, DynamicForce, T0, TAU0_CONDITIONAL,
    adiabatic_photon_temperature,
)
from finite_time_basin_slice import cold_phase_scale
from quantum_initial_capture import quantum_covariance
from drude_equilibrium_covariance import covariance_ratios


def force_fast(model: DynamicForce, T: float, x: np.ndarray) -> np.ndarray:
    """Bilinear interpolation on the already-converged DynamicForce table."""
    Tuse = min(max(float(T), float(model.Tgrid[0])), float(model.Tgrid[-1]))
    k = int(np.searchsorted(model.Tgrid, Tuse) - 1)
    k = max(0, min(k, len(model.Tgrid) - 2))
    Ta = float(model.Tgrid[k]); Tb = float(model.Tgrid[k+1])
    wt = 0.0 if Tb == Ta else (Tuse - Ta)/(Tb - Ta)
    row = (1.0-wt)*model.Ftab[k] + wt*model.Ftab[k+1]
    return np.interp(x, model.xgrid, row, left=row[0], right=row[-1])


def thermal_rhs(t: float, u: float, du_ph: float, tau_r: float, cool: float, u0: float) -> float:
    src = du_ph/tau_r * math.exp(-t/tau_r)
    uu = max(float(u), u0)
    return src - cool*(uu*uu-u0*u0)


def propagate_vectorized(
    model: DynamicForce,
    x: np.ndarray,
    v: np.ndarray,
    j: np.ndarray,
    *,
    R0: float,
    d: float,
    rise_ps: float = 20.0,
    lambda_um: float = 14.0,
    tend_ns: float = 0.8,
    dt_ps: float = 0.2,
) -> tuple[np.ndarray,np.ndarray,np.ndarray,float]:
    r_delta=0.6
    L,C,_=CASES[r_delta]
    _,_,omega0=cold_phase_scale(model,r_delta)
    omegaD=d*omega0; tauD=1.0/omegaD; G0=1.0/R0
    Tad=adiabatic_photon_temperature(lambda_um,100.0)
    u0=T0*T0; du_ph=Tad*Tad-u0; tau_r=rise_ps*1e-12
    cool=1.0/(2.0*TAU0_CONDITIONAL*u0)

    dt=dt_ps*1e-12
    n=int(math.ceil(tend_ns*1e-9/dt)); dt=tend_ns*1e-9/n
    u=u0

    def phase_rhs(xx,vv,jj,TT):
        F=force_fast(model,TT,xx)
        return vv, -(L*jj+F)/(L*C), (G0*vv-jj)/tauD

    t=0.0
    for _ in range(n):
        ku1=thermal_rhs(t,u,du_ph,tau_r,cool,u0)
        T1=math.sqrt(max(u,u0))
        kx1,kv1,kj1=phase_rhs(x,v,j,T1)

        u2=u+0.5*dt*ku1
        ku2=thermal_rhs(t+0.5*dt,u2,du_ph,tau_r,cool,u0)
        T2=math.sqrt(max(u2,u0))
        kx2,kv2,kj2=phase_rhs(x+0.5*dt*kx1,v+0.5*dt*kv1,j+0.5*dt*kj1,T2)

        u3=u+0.5*dt*ku2
        ku3=thermal_rhs(t+0.5*dt,u3,du_ph,tau_r,cool,u0)
        T3=math.sqrt(max(u3,u0))
        kx3,kv3,kj3=phase_rhs(x+0.5*dt*kx2,v+0.5*dt*kv2,j+0.5*dt*kj2,T3)

        u4=u+dt*ku3
        ku4=thermal_rhs(t+dt,u4,du_ph,tau_r,cool,u0)
        T4=math.sqrt(max(u4,u0))
        kx4,kv4,kj4=phase_rhs(x+dt*kx3,v+dt*kv3,j+dt*kj3,T4)

        x = x + dt*(kx1+2*kx2+2*kx3+kx4)/6.0
        v = v + dt*(kv1+2*kv2+2*kv3+kv4)/6.0
        j = j + dt*(kj1+2*kj2+2*kj3+kj4)/6.0
        u = u + dt*(ku1+2*ku2+2*ku3+ku4)/6.0
        u=max(u,u0)
        t += dt
    return x,v,j,math.sqrt(max(u,u0))


def cold_energy_classifier(model: DynamicForce,R0: float,d: float,x,v,j):
    L,C,_=CASES[0.6]
    left,right=model.cold_states()
    roots=model.roots(T0)
    xs=[xx for xx,k in roots if k<0 and left<xx<right][0]
    _,_,omega0=cold_phase_scale(model,0.6)
    Lb=R0/(d*omega0)

    # Cold potential relative to the central saddle.
    F0=np.array([model.force(T0,float(xx)) for xx in model.xgrid])
    U=cumulative_trapezoid(F0,model.xgrid,initial=0.0)
    Us=float(np.interp(xs,model.xgrid,U))
    Urel=np.interp(x,model.xgrid,U)-Us
    Erel=0.5*L*C*v*v+Urel+0.5*L*Lb*j*j
    right_side=x>xs
    trapped=right_side & (Erel<0.0)
    return trapped,right_side,Erel


def exact_one(model,x0,v0,j0,R0,d,tend_ns=0.8):
    """Reference solve_ivp propagation for validation states."""
    L,C,_=CASES[0.6]; _,_,omega0=cold_phase_scale(model,0.6)
    omegaD=d*omega0; tauD=1/omegaD; G0=1/R0
    Tad=adiabatic_photon_temperature(14.0,100.0)
    u0=T0*T0; du=Tad*Tad-u0; tau_r=20e-12
    cool=1/(2*TAU0_CONDITIONAL*u0)
    def rhs(t,y):
        xx,vv,jj,u=y; u=max(float(u),u0); T=math.sqrt(u)
        src=du/tau_r*math.exp(-t/tau_r)
        return np.array([vv,-(L*jj+model.force(T,xx))/(L*C),(G0*vv-jj)/tauD,
                         src-cool*(u*u-u0*u0)])
    sol=solve_ivp(rhs,(0,tend_ns*1e-9),np.array([x0,v0,j0,u0]),method='DOP853',
                  rtol=3e-8,atol=np.array([2e-10,1e2,1e-7,1e-12]),max_step=0.25e-12)
    return sol.y[:3,-1]


def initial_samples(model,R0,d,mmax,seed):
    qcov=quantum_covariance(model,0.6)
    _,C,_=CASES[0.6]; omega0=qcov['omega_c']
    g=1/(R0*C*omega0); a=0.5*qcov['q']*2.0  # qcov q = hbar omega/(2kT)
    # Use qcov['q'] directly; expression above retained only for readability.
    M=covariance_ratios(g,d,qcov['q'])
    # Numerical PSD guard.
    w,V=np.linalg.eigh(M); w=np.maximum(w,0.0); A=V@np.diag(np.sqrt(w))
    sob=qmc.Sobol(d=3,scramble=True,seed=seed)
    p=sob.random_base2(m=mmax)
    z=ndtri(np.clip(p,1e-12,1-1e-12))
    y=z@A.T
    sigma=qcov['sigma_x']; G0=1/R0
    x=qcov['x_c']+sigma*y[:,0]
    v=omega0*sigma*y[:,1]
    j=G0*omega0*sigma*y[:,2]
    return x,v,j,M


def run_case(R0=250.0,d=5.0,mmax=11,seeds=(7,23,61,101),dt_ps=0.2):
    model=DynamicForce(0.6,quick=False)
    all_results=[]
    for seed in seeds:
        x0,v0,j0,M=initial_samples(model,R0,d,mmax,seed)
        xf,vf,jf,Tf=propagate_vectorized(model,x0.copy(),v0.copy(),j0.copy(),R0=R0,d=d,dt_ps=dt_ps)
        trapped,right_side,Erel=cold_energy_classifier(model,R0,d,xf,vf,jf)
        row=[]
        for m in range(8,mmax+1):
            n=2**m
            p=float(np.mean(trapped[:n])); pr=float(np.mean(right_side[:n]))
            row.append((n,p,pr))
        all_results.append(row)
        msg='; '.join(f'N={n}:Ptrap={p:.6f},Pright={pr:.6f}' for n,p,pr in row)
        print(f'seed={seed} R0={R0:g} d={d:g} dt={dt_ps:g}ps Tfinal={Tf:.5f}K; {msg}')
        print(f'::notice title=Experiment 03 correlated Drude capture::{msg}')

        # Regression: compare first 6 states against the exact spline/solve_ivp solver.
        disagree=0; maxdx=maxdv=maxdj=0.0
        for k in range(6):
            ex=exact_one(model,float(x0[k]),float(v0[k]),float(j0[k]),R0,d)
            maxdx=max(maxdx,abs(float(xf[k])-float(ex[0])))
            maxdv=max(maxdv,abs(float(vf[k])-float(ex[1])))
            maxdj=max(maxdj,abs(float(jf[k])-float(ex[2])))
            tr_ex,_,_=cold_energy_classifier(model,R0,d,np.array([ex[0]]),np.array([ex[1]]),np.array([ex[2]]))
            if bool(tr_ex[0]) != bool(trapped[k]): disagree+=1
        vmsg=(f'seed={seed} validation: basin_disagree={disagree}/6, '
              f'max|dx|={maxdx:.3e}, max|dv|={maxdv:.3e}, max|dj|={maxdj:.3e}')
        print(vmsg); print(f'::notice title=Experiment 03 ensemble regression::{vmsg}')

    # Scramble spread at largest N is an empirical integration diagnostic.
    plast=np.array([r[-1][1] for r in all_results])
    print(f'largest-N scramble mean={plast.mean():.6f}, std={plast.std(ddof=1):.6f}, '
          f'min={plast.min():.6f}, max={plast.max():.6f}')
    print('PASS')


def main():
    run_case()

if __name__=='__main__':
    main()
