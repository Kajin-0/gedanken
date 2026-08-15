#!/usr/bin/env python3
"""Initial phase-zero-point tangent amplification through the photon pulse.

The stationary-history FDT calculation showed order-radian linearized phase
spread at left-well reformation for the marginal 14-um pulse.  This script
isolates how much of that comes from deterministic amplification of the cold
phase mode's *pre-existing* x/v uncertainty.

For each wavelength and causal-filter cutoff, integrate the deterministic
trajectory to cooling-side reformation and the adjoint with terminal observable
x(tf).  If lambda(0) is the adjoint at t=0, then for an initially harmonic phase
ellipse with

    Var x0 = sigma_x^2,
    Var v0 = (omega_c sigma_x)^2,
    Cov(x0,v0)=0,

and filter/bath initial fluctuations deliberately omitted,

    sigma_xf,phase^2 = sigma_x^2 [lambda_x^2 + (omega_c lambda_v)^2].

The amplification factor

    A_phase = sigma_xf,phase/sigma_x

is therefore an exact tangent-map quantity for the deterministic nonlinear
trajectory.  It is not the full open-system variance or capture probability.

The purpose is to determine whether the huge 14-um susceptibility is a generic
architecture problem or a near-fold/marginal-photon operating-point problem.
"""

from __future__ import annotations

import math

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

from causal_two_pole_environment import filter_components
from directional_recovery_barriers import directional_barriers
from finite_time_basin_slice import cold_phase_scale
from full_dynamic_rfsquid import (
    CASES,
    DynamicForce,
    T0,
    TAU0_CONDITIONAL,
    adiabatic_photon_temperature,
)
from quantum_initial_capture import quantum_covariance
from two_pole_cold_variance import variance_ratios


def trajectory_to_reform(model,R,alpha,lambda_um,*,rise_ps=20.0):
    L,C,_=CASES[0.6]
    x_c,_,omega_c=cold_phase_scale(model,0.6)
    omega_d=alpha*omega_c
    Lf,Cf=filter_components(R,omega_d)
    Tf=model.fold_temperature()
    Tad=adiabatic_photon_temperature(lambda_um,100.0)
    u0=T0*T0
    du_total=Tad*Tad-u0
    cool_coeff=1/(2*TAU0_CONDITIONAL*u0)
    tau_r=rise_ps*1e-12
    def source(t): return du_total/tau_r*math.exp(-t/tau_r)
    def rhs(t,y):
        x,v,u,d,w=y
        u=max(float(u),u0); T=math.sqrt(u)
        F=model.force(T,x)
        return np.array([
            v,
            -(d+F)/(L*C),
            source(t)-cool_coeff*(u*u-u0*u0),
            (L/Lf)*(v-w),
            d/(L*Cf)-w/(R*Cf),
        ])
    sol=solve_ivp(rhs,(0,0.5e-9),np.array([x_c,0,u0,0,0],float),
                  method='DOP853',rtol=2e-9,
                  atol=np.array([1e-11,1e2,1e-14,1e-11,1e2]),
                  max_step=0.04e-12,dense_output=True)
    ts=np.linspace(0,0.5e-9,10001)
    T=np.sqrt(np.maximum(sol.sol(ts)[2],u0))
    im=int(np.argmax(T))
    if T[im] <= Tf:
        return sol,math.nan,None,omega_c,omega_d,Lf,Cf,Tf,float(T[im])
    post=np.where(T[im:]<Tf)[0]
    if not len(post):
        raise RuntimeError('no reformation')
    j=im+int(post[0])
    tf=brentq(lambda t: math.sqrt(max(float(sol.sol(t)[2]),u0))-Tf,ts[j-1],ts[j])
    return sol,tf,sol.sol(tf),omega_c,omega_d,Lf,Cf,Tf,float(T[im])


def tangent_case(model,R,alpha,lambda_um):
    L,C,_=CASES[0.6]
    sol,tf,yf,omega_c,omega_d,Lf,Cf,Tf,Tpeak=trajectory_to_reform(
        model,R,alpha,lambda_um)
    if not math.isfinite(tf):
        return {'fold_removed':False,'Tpeak':Tpeak,'Tf':Tf}

    def A(t):
        y=sol.sol(t); x=float(y[0]); T=math.sqrt(max(float(y[2]),T0*T0))
        fx=float(np.asarray(model.spline.ev(T,x,dx=0,dy=1)).reshape(-1)[0])
        return np.array([
            [0,1,0,0],
            [-fx/(L*C),0,-1/(L*C),0],
            [0,L/Lf,0,-L/Lf],
            [0,0,1/(L*Cf),-1/(R*Cf)],
        ],float)
    def adj_rhs(t,lam): return -(A(t).T@lam)
    adj=solve_ivp(adj_rhs,(tf,0),np.array([1,0,0,0],float),
                  method='DOP853',rtol=2e-10,atol=1e-12,
                  max_step=0.02e-12)
    lam0=adj.y[:,-1]

    cov=quantum_covariance(model,0.6)
    rq,rv,sx_ratio,sv_ratio,_=variance_ratios(model,0.6,R,alpha)
    sigx0=cov['sigma_x']*sx_ratio
    sigu0=cov['sigma_x']*sv_ratio  # u=v/omega_c
    var_phase=(lam0[0]*sigx0)**2 + (lam0[1]*omega_c*sigu0)**2
    sigxf=math.sqrt(var_phase)

    b=directional_barriers(model,Tf-2e-5)
    x=float(yf[0]); u=float(yf[1])/omega_c
    dx=x-b['saddle']
    return {
        'fold_removed':True,
        'Tpeak':Tpeak,
        'Tf':Tf,
        'tf':tf,
        'x':x,
        'u':u,
        'saddle':b['saddle'],
        'dx':dx,
        'lambda_x':float(lam0[0]),
        'lambda_v_omegac':float(lam0[1]*omega_c),
        'sigma_x0':sigx0,
        'sigma_xf_phase':sigxf,
        'A_phase':sigxf/sigx0,
        'x_margin_phase_sigma':dx/sigxf if sigxf>0 else math.inf,
    }


def main():
    print('Experiment 03 initial quantum tangent amplification scan')
    print('rDelta=.6, R=250 ohm, rise=20 ps; phase-only initial covariance')
    print('CPR interpolation extended to 0.95 K for the 8-um point')
    model=DynamicForce(0.6,quick=False,Tmax=0.95)
    for alpha in (0.20,0.35,0.50):
        print(f'\nalpha={alpha:.2f}')
        for lam in (8.0,9.0,10.0,11.0,12.0,13.0,14.0,15.0,16.0):
            o=tangent_case(model,250.0,alpha,lam)
            if not o['fold_removed']:
                msg=(f'lambda={lam:.1f} um: Tpeak={o["Tpeak"]:.5f} K < Tf; '
                     'static fold not removed')
            else:
                msg=(
                    f'lambda={lam:.1f} um: Tpeak={o["Tpeak"]:.5f} K, '
                    f'treform={o["tf"]*1e12:.2f} ps, x={o["x"]:+.4f}, '
                    f'dx={o["dx"]:.4f}, Aphase={o["A_phase"]:.3f}, '
                    f'sigma_phase={o["sigma_xf_phase"]:.4f}, '
                    f'margin_phase={o["x_margin_phase_sigma"]:.3f}, '
                    f'lamx={o["lambda_x"]:+.3f}, lamvwc={o["lambda_v_omegac"]:+.3f}'
                )
            print(msg)
            print(f'::notice title=Experiment 03 tangent wavelength scan::{msg}')
    print('PASS')

if __name__=='__main__':
    main()
