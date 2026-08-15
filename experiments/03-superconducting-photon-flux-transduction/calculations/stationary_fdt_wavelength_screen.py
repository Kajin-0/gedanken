#!/usr/bin/env python3
"""Stationary-history FDT wavelength screen for the causal Experiment-03 latch.

The 14-um stationary-history calculation produced order-radian linearized phase
spread at cooling-side reformation.  A phase-only tangent scan then found large
standardized margins at shorter wavelength for alpha=omega_D/omega_c~0.5.

This script performs the stronger test at those wavelengths: the same causal
bath is assumed to have equilibrated with the cold phase mode for t<0, and the
complete pre-pulse + pulse-time *symmetrized* FDT history is propagated in
linear response to cooling-side reformation.

The result is a covariance/susceptibility diagnostic, not a capture probability.
If the predicted spread becomes comparable to the basin scale, linear response
has invalidated itself and nonlinear open-system propagation is mandatory.
"""

from __future__ import annotations

import math

import numpy as np
from scipy.integrate import solve_ivp

from directional_recovery_barriers import directional_barriers
from full_dynamic_rfsquid import CASES, DynamicForce, T0
from history_fdt_reformation_margin import (
    cold_history_h,
    cold_pole_data,
    spectral_variance_from_kernel,
    state_matrix,
)
from initial_quantum_tangent_scan import trajectory_to_reform
from quantum_initial_capture import PHI_BAR, quantum_covariance
from two_pole_cold_variance import variance_ratios


def hot_adjoint_lambda(model,R,alpha,lambda_um,cvec):
    L,C,_=CASES[0.6]
    sol,tf,yf,omega_c,omega_d,Lf,Cf,Tf,Tpeak=trajectory_to_reform(
        model,R,alpha,lambda_um)
    if not math.isfinite(tf):
        return None

    def A_hot(t):
        y=sol.sol(t)
        x=float(y[0]); T=math.sqrt(max(float(y[2]),T0*T0))
        return state_matrix(model,R,x,T,Lf,Cf)
    def rhs(t,lam):
        return -(A_hot(t).T@lam)
    adj=solve_ivp(rhs,(tf,0.0),np.asarray(cvec,dtype=float),
                  method='DOP853',rtol=2e-9,atol=1e-11,
                  max_step=0.02e-12,dense_output=True)
    cov=quantum_covariance(model,0.6)
    Acold=state_matrix(model,R,cov['x_c'],T0,Lf,Cf)
    return adj,sol,tf,yf,omega_c,omega_d,Lf,Cf,Tf,Tpeak,Acold


def stationary_variance_lambda(model,R,alpha,lambda_um,cvec,*,dt_ps=1.0,n_tau=12.0,pad_factor=4):
    L,C,_=CASES[0.6]
    B=np.array([0.0,-1.0/(C*PHI_BAR),0.0,0.0])
    pack=hot_adjoint_lambda(model,R,alpha,lambda_um,cvec)
    if pack is None:
        return None
    adj,sol,tf,yf,omega_c,omega_d,Lf,Cf,Tf,Tpeak,Acold=pack
    eig,V,Vinv,tau=cold_pole_data(Acold)
    tpre=n_tau*tau
    dt=dt_ps*1e-12
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
    return var,tf,yf,omega_c,Tf,Tpeak,tau


def cold_regression_once(model,R,alpha):
    """Regression from independent equilibrium marginal formulas."""
    cov=quantum_covariance(model,0.6)
    rq,rv,sxratio,svratio,_=variance_ratios(model,0.6,R,alpha)
    return cov['sigma_x']*sxratio, cov['sigma_x']*svratio


def report_case(model,R,alpha,lam):
    first=stationary_variance_lambda(model,R,alpha,lam,[1,0,0,0])
    if first is None:
        print(f'lambda={lam:.1f} um: fold not removed')
        return
    vx,tf,yf,omega_c,Tf,Tpeak,tau=first
    vu=stationary_variance_lambda(model,R,alpha,lam,[0,1/omega_c,0,0])[0]
    vs=stationary_variance_lambda(model,R,alpha,lam,[1,1/omega_c,0,0])[0]
    covxu=0.5*(vs-vx-vu)
    M=np.array([[vx,covxu],[covxu,vu]],float)
    ev,evec=np.linalg.eigh(M)
    sigx=math.sqrt(max(vx,0)); sigu=math.sqrt(max(vu,0))
    rho=covxu/(sigx*sigu) if sigx*sigu>0 else math.nan
    sig_pr=np.sqrt(np.maximum(ev,0))

    b=directional_barriers(model,Tf-2e-5)
    x=float(yf[0]); u=float(yf[1])/omega_c
    dx=x-b['saddle']
    msg=(
        f'alpha={alpha:.2f}, lambda={lam:.1f} um: Tpeak={Tpeak:.5f} K, '
        f'treform={tf*1e12:.2f} ps, x={x:+.5f}, u={u:+.5f}, '
        f'dx={dx:+.5f}, sigma_x={sigx:.5f}, sigma_u={sigu:.5f}, '
        f'rho={rho:+.5f}, x_margin={dx/sigx:.3f}, '
        f'principal_rms=[{sig_pr[0]:.5f},{sig_pr[1]:.5f}], '
        f'tau_cold={tau*1e9:.3f} ns'
    )
    print(msg)
    print(f'::notice title=Experiment 03 stationary-FDT wavelength::{msg}')


def main():
    print('Experiment 03 stationary-history FDT wavelength screen')
    print('rDelta=.6, R=250 ohm, rise=20 ps, full CPR Tmax=.95 K')
    model=DynamicForce(0.6,quick=False,Tmax=0.95)
    for alpha,lams in [
        (0.50,(8.0,9.0,10.0,11.0,12.0,13.0,14.0)),
        (0.35,(10.0,11.0,12.0,13.0,14.0)),
    ]:
        sx,su=cold_regression_once(model,250.0,alpha)
        print(f'\nalpha={alpha:.2f}: cold sigma_x={sx:.6f}, sigma_u={su:.6f}')
        for lam in lams:
            report_case(model,250.0,alpha,lam)
    print('PASS')

if __name__=='__main__':
    main()
