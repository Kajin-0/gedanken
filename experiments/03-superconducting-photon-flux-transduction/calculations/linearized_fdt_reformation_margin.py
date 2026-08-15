#!/usr/bin/env python3
"""Linearized FDT sensitivity of the phase state at left-well reformation.

Purpose
-------
The full 80-ns FDT work variance includes late relaxation after the detector has
already entered the favored right state.  A more local robustness diagnostic is
how strongly port-current fluctuations can move the phase at the instant the
metastable left well/saddle reappear during cooling.

For the deterministic causal-filter trajectory, linearize the augmented state
z=[x,v,d,w] about z0(t):

    delta_zdot = A(t) delta_z + B I_N(t),

where

    B = [0, -1/(C Phi_bar), 0, 0]^T.

For a final observable c^T delta_z(tf), solve the adjoint

    -lambda_dot = A(t)^T lambda,
    lambda(tf)=c,

so its noise sensitivity is h(t)=lambda(t)^T B.  The symmetrized FDT variance
is then

    Var = integral S_I^sym(omega) |H(omega)|^2 d omega/(2 pi).

This is a first-order *symmetrized quantum susceptibility* around a prescribed
trajectory.  It is not a classical activation probability and does not include
nonlinear response, initial system-bath correlations, dissipative MQT, or Moyal
corrections.
"""

from __future__ import annotations

import math

import numpy as np
from scipy.integrate import solve_ivp

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
from quantum_initial_capture import HBAR, KB, PHI_BAR
from two_pole_cold_variance import admittance, coth_stable


def deterministic_to_reform(
    model: DynamicForce,
    R: float,
    alpha: float,
    *,
    r_delta: float=0.6,
    rise_ps: float=20.0,
    lambda_um: float=14.0,
):
    L,C,_=CASES[r_delta]
    x_c,_,omega_c=cold_phase_scale(model,r_delta)
    omega_d=alpha*omega_c
    Lf,Cf=filter_components(R,omega_d)
    Tf=model.fold_temperature()

    Tad=adiabatic_photon_temperature(lambda_um,100.0)
    u0=T0*T0
    du_total=Tad*Tad-u0
    cool_coeff=1.0/(2.0*TAU0_CONDITIONAL*u0)
    tau_r=rise_ps*1e-12

    def source(t): return du_total/tau_r*math.exp(-t/tau_r)
    def rhs(t,y):
        x,v,u,d,w=y
        u=max(float(u),u0)
        T=math.sqrt(u)
        F=model.force(T,x)
        du=source(t)-cool_coeff*(u*u-u0*u0)
        return np.array([
            v,
            -(d+F)/(L*C),
            du,
            (L/Lf)*(v-w),
            d/(L*Cf)-w/(R*Cf),
        ])

    sol=solve_ivp(rhs,(0.0,0.3e-9),np.array([x_c,0.0,u0,0.0,0.0]),
                  method='DOP853',rtol=2e-9,
                  atol=np.array([1e-11,1e2,1e-14,1e-11,1e2]),
                  max_step=0.05e-12,dense_output=True)
    # locate temperature maximum then cooling-side T=Tf root from dense solution
    ts=np.linspace(0,0.2e-9,4001)
    us=np.maximum(sol.sol(ts)[2],u0)
    im=int(np.argmax(us))
    vals=np.sqrt(us[im:])-Tf
    idx=np.where(vals<0)[0]
    if not len(idx): raise RuntimeError('no reformation in bracket')
    j=im+int(idx[0])
    ta,tb=ts[j-1],ts[j]
    from scipy.optimize import brentq
    tf=brentq(lambda t: math.sqrt(max(float(sol.sol(t)[2]),u0))-Tf,ta,tb)
    yf=sol.sol(tf)
    return sol,tf,yf,omega_c,omega_d,Lf,Cf,Tf


def fdt_psd(omega: np.ndarray,R: float,omega_d: float,Tbath: float=T0)->np.ndarray:
    out=np.empty_like(omega)
    for i,om in enumerate(omega):
        if om==0:
            eps=2.0*KB*Tbath
        else:
            eps=HBAR*om*coth_stable(HBAR*om/(2.0*KB*Tbath))
        out[i]=eps*admittance(float(om),R,omega_d).real
    return out


def sensitivity_variance(model,R,alpha,cvec,*,dt_ps=0.02,pad_factor=32):
    L,C,_=CASES[0.6]
    sol,tf,yf,omega_c,omega_d,Lf,Cf,Tf=deterministic_to_reform(model,R,alpha)

    def A_of_t(t):
        y=sol.sol(t)
        x=float(y[0]); T=math.sqrt(max(float(y[2]),T0*T0))
        fx=float(np.asarray(model.spline.ev(T,x,dx=0,dy=1)).reshape(-1)[0])
        return np.array([
            [0.0,1.0,0.0,0.0],
            [-fx/(L*C),0.0,-1.0/(L*C),0.0],
            [0.0,L/Lf,0.0,-L/Lf],
            [0.0,0.0,1.0/(L*Cf),-1.0/(R*Cf)],
        ])

    def adj_rhs(t,lam): return -(A_of_t(t).T@lam)
    adj=solve_ivp(adj_rhs,(tf,0.0),np.asarray(cvec,dtype=float),
                  method='DOP853',rtol=2e-9,atol=1e-11,
                  max_step=0.02e-12,dense_output=True)

    dt=dt_ps*1e-12
    n=int(math.ceil(tf/dt))+1
    t=np.linspace(0.0,tf,n)
    actual_dt=t[1]-t[0]
    lam=adj.sol(t)
    # B=[0,-1/(C Phi_bar),0,0]
    h=-lam[1]/(C*PHI_BAR)

    # The sensitivity kernel is finite-time supported. Zero padding does not
    # change h(t); it only samples its continuous Fourier transform more finely
    # so the colored FDT weighting is numerically resolved even when tf~60 ps.
    base=1 << int(math.ceil(math.log2(n)))
    nfft=pad_factor*base
    H=np.fft.rfft(h,n=nfft)*actual_dt
    freq=np.fft.rfftfreq(nfft,actual_dt)
    omega=2.0*math.pi*freq
    weights=np.full_like(freq,2.0); weights[0]=1.0
    if nfft%2==0: weights[-1]=1.0
    S=fdt_psd(omega,R,omega_d)
    var=float(np.sum(weights*S*np.abs(H)**2)*(freq[1]-freq[0]))
    return var,tf,yf,omega_c,omega_d,Tf


def main():
    print('Experiment 03 linearized FDT reformation margin')
    print('32x zero-padded finite-time sensitivity spectrum')
    model=DynamicForce(0.6,quick=False)
    for R,alpha in [(250.0,0.20),(250.0,0.35),(250.0,0.50)]:
        varx,tf,yf,omega_c,omega_d,Tf=sensitivity_variance(model,R,alpha,[1,0,0,0])
        varv,_,_,_,_,_=sensitivity_variance(model,R,alpha,[0,1,0,0])
        # cross covariance via c=x+v/omega_c identity
        varsum,_,_,_,_,_=sensitivity_variance(model,R,alpha,[1,1/omega_c,0,0])
        covxu=0.5*(varsum-varx-varv/(omega_c*omega_c))
        sigx=math.sqrt(max(varx,0.0))
        sigu=math.sqrt(max(varv,0.0))/omega_c
        x=float(yf[0]); v=float(yf[1]); T=Tf-2e-5
        b=directional_barriers(model,T)
        saddle=b['saddle']
        dx=x-saddle
        mx=dx/sigx if sigx>0 else math.inf
        rho=covxu/(sigx*sigu) if sigx>0 and sigu>0 else math.nan
        msg=(
            f'R={R:g} alpha={alpha:.2f}: tf={tf*1e12:.3f} ps, '
            f'x={x:+.6f}, saddle={saddle:+.6f}, dx={dx:.6f}, '
            f'sigma_x,bath={sigx:.6f}, sigma_u,bath={sigu:.6f}, '
            f'rho_xu={rho:+.4f}, x_margin_sigma={mx:.3f}, '
            f'u_det={v/omega_c:+.6f}'
        )
        print(msg)
        print(f'::notice title=Experiment 03 FDT reformation margin::{msg}')
    print('PASS')

if __name__=='__main__':
    main()
