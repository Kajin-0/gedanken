#!/usr/bin/env python3
"""Stationary-history linear FDT margin at left-well reformation.

The detector is assumed to have equilibrated in the cold left well before the
photon arrives.  For t>=0 the adjoint sensitivity is propagated through the
actual nonlinear deterministic photon trajectory.  For t<0 the system is
linear time invariant, so the infinite stationary prehistory can be generated
analytically from the cold state-matrix poles rather than by a long ODE solve.

The retained prehistory is 12 times the slowest cold amplitude-decay time.  At
that point omitted adjoint amplitude is ~exp(-12) and omitted variance weight is
~exp(-24).  A 1-ps uniform history grid resolves the ~27-GHz phase mode while
remaining practical even for the strongly filtered alpha=.2 case, whose cold
phase equilibration time is tens of nanoseconds.

The complete sensitivity kernel is contracted with the same stationary
symmetrized quantum-FDT spectrum.  This automatically includes, within linear
response, correlations between equilibrium fluctuations present at t=0 and the
same bath acting during the pulse.

This is a quantum covariance/susceptibility diagnostic, NOT an activation or
capture probability.  Symmetrized zero-point noise must not be interpreted as
an ordinary classical random force at 20 mK.
"""

from __future__ import annotations

import math

import numpy as np
from scipy.integrate import solve_ivp

from directional_recovery_barriers import directional_barriers
from full_dynamic_rfsquid import CASES, DynamicForce, T0
from quantum_initial_capture import PHI_BAR, quantum_covariance
from two_pole_cold_variance import variance_ratios
from linearized_fdt_reformation_margin import (
    deterministic_to_reform,
    fdt_psd,
)


def state_matrix(model, R, x, T, Lf, Cf):
    L,C,_=CASES[0.6]
    fx=float(np.asarray(model.spline.ev(T,x,dx=0,dy=1)).reshape(-1)[0])
    return np.array([
        [0.0,1.0,0.0,0.0],
        [-fx/(L*C),0.0,-1.0/(L*C),0.0],
        [0.0,L/Lf,0.0,-L/Lf],
        [0.0,0.0,1.0/(L*Cf),-1.0/(R*Cf)],
    ],dtype=float)


def cold_pole_data(Acold: np.ndarray):
    eig,V=np.linalg.eig(Acold.T.astype(complex))
    Vinv=np.linalg.inv(V)
    neg=[ev for ev in eig if ev.real<0]
    if len(neg)!=len(eig):
        raise RuntimeError(f'cold state is not asymptotically stable: {eig}')
    gamma_slow=-max(ev.real for ev in eig)
    tau=1.0/gamma_slow
    return eig,V,Vinv,tau


def cold_history_h(r: np.ndarray, lam0: np.ndarray, eig, V, Vinv, B) -> np.ndarray:
    """h(t=-r)=B^T exp(A_c^T r) lam0, r>=0."""
    coeff=Vinv@np.asarray(lam0,dtype=complex)
    left=(np.asarray(B,dtype=complex)@V)
    amp=left*coeff
    # four modes x N; real result up to roundoff
    h=np.sum(amp[:,None]*np.exp(eig[:,None]*r[None,:]),axis=0)
    return np.real_if_close(h,tol=1000).real


def hot_adjoint(model,R,alpha,cvec):
    L,C,_=CASES[0.6]
    sol,tf,yf,omega_c,omega_d,Lf,Cf,Tf=deterministic_to_reform(model,R,alpha)

    def A_hot(t):
        y=sol.sol(t)
        x=float(y[0]); T=math.sqrt(max(float(y[2]),T0*T0))
        return state_matrix(model,R,x,T,Lf,Cf)
    def rhs(t,lam): return -(A_hot(t).T@lam)
    adj=solve_ivp(rhs,(tf,0.0),np.asarray(cvec,dtype=float),
                  method='DOP853',rtol=2e-9,atol=1e-11,
                  max_step=0.02e-12,dense_output=True)
    cov=quantum_covariance(model,0.6)
    Acold=state_matrix(model,R,cov['x_c'],T0,Lf,Cf)
    return adj,sol,tf,yf,omega_c,omega_d,Lf,Cf,Tf,Acold


def spectral_variance_from_kernel(h: np.ndarray,dt: float,R: float,omega_d: float,*,pad_factor=4):
    n=len(h)
    base=1 << int(math.ceil(math.log2(n)))
    nfft=pad_factor*base
    H=np.fft.rfft(h,n=nfft)*dt
    freq=np.fft.rfftfreq(nfft,dt)
    omega=2.0*math.pi*freq
    weights=np.full_like(freq,2.0); weights[0]=1.0
    if nfft%2==0: weights[-1]=1.0
    S=fdt_psd(omega,R,omega_d)
    return float(np.sum(weights*S*np.abs(H)**2)*(freq[1]-freq[0]))


def stationary_history_variance(model,R,alpha,cvec,*,dt_ps=1.0,n_tau=12.0,pad_factor=4):
    L,C,_=CASES[0.6]
    B=np.array([0.0,-1.0/(C*PHI_BAR),0.0,0.0])
    adj,sol,tf,yf,omega_c,omega_d,Lf,Cf,Tf,Acold=hot_adjoint(model,R,alpha,cvec)
    eig,V,Vinv,tau=cold_pole_data(Acold)
    tpre=n_tau*tau
    dt=dt_ps*1e-12

    # Build one exactly uniform grid whose origin is a sample.  Choose integer
    # counts on both sides, then evaluate the hot adjoint at the corresponding
    # times; the final sample is allowed to be just below tf, with a final tf
    # endpoint appended only if needed.
    npre=int(math.ceil(tpre/dt))
    npost=int(math.floor(tf/dt))
    tneg=-np.arange(npre,0,-1,dtype=float)*dt
    tpos=np.arange(0,npost+1,dtype=float)*dt

    r=-tneg
    lam0=adj.sol(0.0)
    hneg=cold_history_h(r,lam0,eig,V,Vinv,B)
    hpos=B@adj.sol(tpos)
    h=np.concatenate([hneg,np.asarray(hpos,dtype=float)])

    var=spectral_variance_from_kernel(h,dt,R,omega_d,pad_factor=pad_factor)
    return var,tf,yf,omega_c,omega_d,Tf,tau,tpre,Acold


def cold_regression(model,R,alpha,*,dt_ps=1.0,n_tau=12.0,pad_factor=4):
    L,C,_=CASES[0.6]
    B=np.array([0.0,-1.0/(C*PHI_BAR),0.0,0.0])
    cov=quantum_covariance(model,0.6)
    # obtain physical filter data through the deterministic helper
    _,_,_,_,omega_c,omega_d,Lf,Cf,_,_=hot_adjoint(model,R,alpha,[1,0,0,0])
    Acold=state_matrix(model,R,cov['x_c'],T0,Lf,Cf)
    eig,V,Vinv,tau=cold_pole_data(Acold)
    tpre=n_tau*tau
    dt=dt_ps*1e-12
    npre=int(math.ceil(tpre/dt))
    # causal past r runs from tpre down to zero so h is ordered in time t=-r
    r=np.arange(npre,0,-1,dtype=float)*dt

    def one(cvec):
        h=cold_history_h(r,np.asarray(cvec,float),eig,V,Vinv,B)
        return spectral_variance_from_kernel(h,dt,R,omega_d,pad_factor=pad_factor)

    vx=one([1,0,0,0])
    vu=one([0,1/omega_c,0,0])
    rq,rv,sqx,sqv,_=variance_ratios(model,0.6,R,alpha)
    sx_ref=cov['sigma_x']*sqx
    su_ref=cov['sigma_x']*sqv
    return math.sqrt(vx),math.sqrt(vu),sx_ref,su_ref,tau,tpre


def main():
    print('Experiment 03 stationary-history FDT reformation margin')
    print('cold prehistory = 12 slowest-pole time constants; dt=1 ps')
    model=DynamicForce(0.6,quick=False)
    for R,alpha in [(250.0,0.20),(250.0,0.35),(250.0,0.50)]:
        sx_hist,su_hist,sx_ref,su_ref,tau,tpre=cold_regression(model,R,alpha)
        varx,tf,yf,omega_c,omega_d,Tf,_,_,_=stationary_history_variance(model,R,alpha,[1,0,0,0])
        varu,_,_,_,_,_,_,_,_=stationary_history_variance(model,R,alpha,[0,1/omega_c,0,0])
        varsum,_,_,_,_,_,_,_,_=stationary_history_variance(model,R,alpha,[1,1/omega_c,0,0])
        covxu=0.5*(varsum-varx-varu)
        sigx=math.sqrt(max(varx,0.0)); sigu=math.sqrt(max(varu,0.0))
        rho=covxu/(sigx*sigu) if sigx*sigu>0 else math.nan
        b=directional_barriers(model,Tf-2e-5)
        x=float(yf[0]); u=float(yf[1])/omega_c
        dx=x-b['saddle']
        msg=(
            f'R={R:g} alpha={alpha:.2f}: '
            f'tau_cold={tau*1e9:.3f} ns, pre={tpre*1e9:.1f} ns, '
            f'cold_reg_x={sx_hist/sx_ref:.5f}, cold_reg_u={su_hist/su_ref:.5f}, '
            f'tf={tf*1e12:.3f} ps, x={x:+.6f}, u={u:+.6f}, '
            f'saddle={b["saddle"]:+.6f}, dx={dx:.6f}, '
            f'sigma_x,totalhist={sigx:.6f}, sigma_u,totalhist={sigu:.6f}, '
            f'rho_xu={rho:+.4f}, x_margin_sigma={dx/sigx:.3f}'
        )
        print(msg)
        print(f'::notice title=Experiment 03 stationary-history margin::{msg}')
    print('PASS')

if __name__=='__main__':
    main()
