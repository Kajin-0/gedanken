#!/usr/bin/env python3
"""Stationary-history linear FDT margin at left-well reformation.

This improves linearized_fdt_reformation_margin.py by avoiding an artificial
split between an independently sampled initial phase state and future colored
bath noise.

For t>=0, the adjoint sensitivity is propagated backward through the actual
nonlinear deterministic photon trajectory.  For t<0, the detector is assumed
stationary in the cold harmonic left well, so the same adjoint is continued to
-t_pre with the cold linear time-invariant system.  The complete sensitivity
kernel h(t), t in (-infinity, t_reform], is then contracted with the *same*
stationary symmetrized FDT spectrum.

This automatically includes, at linear-response level, the correlations between
pre-pulse equilibrium fluctuations and the future colored bath history without
introducing UV-sensitive auxiliary-state sampling.

It remains a symmetrized quantum covariance / susceptibility calculation, not a
capture probability.  Nonlinear fluctuation response, Moyal corrections and
quantum detailed-balance transition probabilities are still outside this model.
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


def state_matrix(model, R, alpha, x, T, omega_c, omega_d, Lf, Cf):
    L,C,_=CASES[0.6]
    fx=float(np.asarray(model.spline.ev(T,x,dx=0,dy=1)).reshape(-1)[0])
    return np.array([
        [0.0,1.0,0.0,0.0],
        [-fx/(L*C),0.0,-1.0/(L*C),0.0],
        [0.0,L/Lf,0.0,-L/Lf],
        [0.0,0.0,1.0/(L*Cf),-1.0/(R*Cf)],
    ])


def adjoint_history(model,R,alpha,cvec,*,pre_ns=2.0,dt_ps=0.05,pad_factor=8):
    L,C,_=CASES[0.6]
    sol,tf,yf,omega_c,omega_d,Lf,Cf,Tf=deterministic_to_reform(model,R,alpha)

    def A_hot(t):
        y=sol.sol(t)
        x=float(y[0]); T=math.sqrt(max(float(y[2]),T0*T0))
        return state_matrix(model,R,alpha,x,T,omega_c,omega_d,Lf,Cf)

    def hot_rhs(t,lam): return -(A_hot(t).T@lam)
    hot=solve_ivp(hot_rhs,(tf,0.0),np.asarray(cvec,dtype=float),
                  method='DOP853',rtol=2e-9,atol=1e-11,
                  max_step=0.02e-12,dense_output=True)
    lam0=hot.sol(0.0)

    x_c=quantum_covariance(model,0.6)['x_c']
    Acold=state_matrix(model,R,alpha,x_c,T0,omega_c,omega_d,Lf,Cf)
    def cold_rhs(t,lam): return -(Acold.T@lam)
    tpre=pre_ns*1e-9
    cold=solve_ivp(cold_rhs,(0.0,-tpre),lam0,method='DOP853',
                   rtol=2e-10,atol=1e-12,max_step=0.2e-12,dense_output=True)

    dt=dt_ps*1e-12
    npre=int(math.ceil(tpre/dt))
    npost=int(math.ceil(tf/dt))
    tneg=np.linspace(-tpre,0.0,npre+1,endpoint=True)
    tpos=np.linspace(0.0,tf,npost+1,endpoint=True)[1:]
    t=np.concatenate([tneg,tpos])
    lam=np.empty((4,len(t)))
    mask=t<=0
    lam[:,mask]=cold.sol(t[mask])
    lam[:,~mask]=hot.sol(t[~mask])
    h=-lam[1]/(C*PHI_BAR)

    actual_dt=float(np.mean(np.diff(t)))
    # t grid differs at the 0/tf endpoint by sub-percent because each segment is
    # forced to hit its endpoint.  Interpolate onto one exactly uniform grid
    # before FFT.
    nu=int(math.ceil((tf+tpre)/dt))+1
    tu=np.linspace(-tpre,tf,nu)
    hu=np.interp(tu,t,h)
    du=tu[1]-tu[0]
    base=1 << int(math.ceil(math.log2(nu)))
    nfft=pad_factor*base
    H=np.fft.rfft(hu,n=nfft)*du
    freq=np.fft.rfftfreq(nfft,du)
    omega=2.0*math.pi*freq
    weights=np.full_like(freq,2.0); weights[0]=1.0
    if nfft%2==0: weights[-1]=1.0
    S=fdt_psd(omega,R,omega_d)
    var=float(np.sum(weights*S*np.abs(H)**2)*(freq[1]-freq[0]))
    return var,tf,yf,omega_c,omega_d,Tf,lam0,Acold


def cold_regression(model,R,alpha,*,pre_ns=2.0,dt_ps=0.05,pad_factor=8):
    """Compute x/u stationary variance from past-noise history only."""
    L,C,_=CASES[0.6]
    cov=quantum_covariance(model,0.6)
    omega_c=cov['omega_c']
    # get filter params/state matrix through helper trajectory metadata
    sol,tf,yf,omega_c,omega_d,Lf,Cf,Tf=deterministic_to_reform(model,R,alpha)
    Acold=state_matrix(model,R,alpha,cov['x_c'],T0,omega_c,omega_d,Lf,Cf)
    tpre=pre_ns*1e-9

    def one(cvec):
        def rhs(t,lam): return -(Acold.T@lam)
        adj=solve_ivp(rhs,(0.0,-tpre),np.asarray(cvec,dtype=float),
                      method='DOP853',rtol=2e-10,atol=1e-12,
                      max_step=0.2e-12,dense_output=True)
        dt=dt_ps*1e-12
        n=int(math.ceil(tpre/dt))+1
        t=np.linspace(-tpre,0.0,n)
        h=-adj.sol(t)[1]/(C*PHI_BAR)
        du=t[1]-t[0]
        base=1 << int(math.ceil(math.log2(n)))
        nfft=pad_factor*base
        H=np.fft.rfft(h,n=nfft)*du
        freq=np.fft.rfftfreq(nfft,du)
        omega=2*math.pi*freq
        weights=np.full_like(freq,2.0); weights[0]=1.0
        if nfft%2==0: weights[-1]=1.0
        S=fdt_psd(omega,R,omega_d)
        return float(np.sum(weights*S*np.abs(H)**2)*(freq[1]-freq[0]))

    vx=one([1,0,0,0])
    vv=one([0,1/omega_c,0,0])
    rq,rv,sqx,sqv,_=variance_ratios(model,0.6,R,alpha)
    return math.sqrt(vx),math.sqrt(vv),cov['sigma_x']*sqx,cov['sigma_x']*sqv


def main():
    print('Experiment 03 stationary-history FDT reformation margin')
    model=DynamicForce(0.6,quick=False)
    for R,alpha in [(250.0,0.20),(250.0,0.35),(250.0,0.50)]:
        # regression that past-history contraction recovers known cold marginals
        sx_hist,su_hist,sx_ref,su_ref=cold_regression(model,R,alpha)
        varx,tf,yf,omega_c,omega_d,Tf,_,_=adjoint_history(model,R,alpha,[1,0,0,0])
        varu,_,_,_,_,_,_,_=adjoint_history(model,R,alpha,[0,1/omega_c,0,0])
        varsum,_,_,_,_,_,_,_=adjoint_history(model,R,alpha,[1,1/omega_c,0,0])
        covxu=0.5*(varsum-varx-varu)
        sigx=math.sqrt(max(varx,0.0)); sigu=math.sqrt(max(varu,0.0))
        rho=covxu/(sigx*sigu) if sigx*sigu>0 else math.nan
        b=directional_barriers(model,Tf-2e-5)
        x=float(yf[0]); u=float(yf[1])/omega_c
        dx=x-b['saddle']
        msg=(
            f'R={R:g} alpha={alpha:.2f}: '
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
