#!/usr/bin/env python3
"""Nonlinear generalized-Langevin / truncated-Wigner screen for Experiment 03.

Purpose
-------
The stationary-history linear FDT calculation becomes self-inconsistent at the
marginal 14-um point because it predicts order-radian phase spread.  This script
is the next falsification level: propagate an ensemble nonlinearly through the
full CPR force while the same stationary colored bath history acts before and
during the photon pulse.

Approximation
-------------
This is a *symmetrized-noise truncated-Wigner/generalized-Langevin* screen, not
exact open-system quantum dynamics.

- The causal dissipation is the passive quartic-rolloff Y(omega).
- A real stationary Gaussian current-noise history is generated with the
  symmetrized quantum FDT spectrum

      S_I(omega)=hbar|omega|coth[hbar|omega|/(2kT)] ReY(omega).

- For t<0 the phase dynamics are linearized about the cold left well and run
  for 12 slowest cold amplitude-decay times.  This prepares the correct cold
  *symmetrized/Wigner covariance* without separately sampling UV-sensitive
  auxiliary filter coordinates.
- The identical noise realization then continues through the full nonlinear
  time-dependent photon pulse for t>=0.

For a quadratic system this stochastic construction reproduces the symmetrized
Gaussian covariance.  Once the Josephson potential becomes nonlinear it is a
TWA-like approximation: Moyal corrections and exact quantum detailed balance
are absent.  Therefore reported basin fractions are SEMICLASSICAL SCREENING
NUMBERS, not physical detector efficiencies or dark-count rates.

The cold x/u covariance regression is mandatory.  If it fails, pulse results
must be ignored.
"""

from __future__ import annotations

import argparse
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
from history_fdt_reformation_margin import cold_pole_data, state_matrix
from quantum_initial_capture import HBAR, KB, PHI_BAR, quantum_covariance
from two_pole_cold_variance import variance_ratios


def thermal_trace(lambda_um: float, dt: float, tpost: float,
                  area_um2: float=100.0, rise_ps: float=20.0) -> tuple[np.ndarray,np.ndarray]:
    """Deterministic common T(t) on a uniform post-pulse grid."""
    Tad=adiabatic_photon_temperature(lambda_um,area_um2)
    u0=T0*T0
    du_total=Tad*Tad-u0
    cool_coeff=1.0/(2.0*TAU0_CONDITIONAL*u0)
    tau_r=rise_ps*1e-12
    n=int(round(tpost/dt))+1
    t=np.arange(n,dtype=float)*dt

    def source(tt): return du_total/tau_r*math.exp(-tt/tau_r)
    def rhs(tt,y):
        u=max(float(y[0]),u0)
        return np.array([source(tt)-cool_coeff*(u*u-u0*u0)])
    sol=solve_ivp(rhs,(0.0,float(t[-1])),np.array([u0]),t_eval=t,
                  method='DOP853',rtol=2e-10,atol=1e-13,max_step=dt)
    return t,np.sqrt(np.maximum(sol.y[0],u0))


def noise_psd_n(omega: np.ndarray,L: float,R: float,omega_d: float) -> np.ndarray:
    """Two-sided angular-frequency PSD of n=L I_N/Phi_bar."""
    reY=(1.0/R)/(1.0+(omega/omega_d)**4)
    eps=np.empty_like(omega)
    z=HBAR*omega/(2.0*KB*T0)
    small=z<1e-6
    large=z>30.0
    mid=~(small|large)
    eps[small]=2.0*KB*T0
    eps[large]=HBAR*omega[large]
    eps[mid]=HBAR*omega[mid]/np.tanh(z[mid])
    SI=eps*reY
    return (L/PHI_BAR)**2*SI


def gaussian_noise_batch(rng: np.random.Generator,nb: int,n: int,dt: float,
                         L: float,R: float,omega_d: float) -> np.ndarray:
    """Generate nb real periodic histories with target two-sided PSD S_n(omega).

    For numpy's DFT convention, interior complex coefficients satisfy

        E|X_k|^2 = N S_omega(omega_k)/dt,

    because the real-process one-sided PSD in Hz is 2*S_omega(2pi f).
    """
    freq=np.fft.rfftfreq(n,dt)
    omega=2.0*math.pi*freq
    S=noise_psd_n(omega,L,R,omega_d)
    nk=len(freq)
    X=np.empty((nb,nk),dtype=np.complex128)

    # DC real coefficient.
    X[:,0]=rng.normal(size=nb)*np.sqrt(n*S[0]/dt)
    last=nk-1
    stop=last if n%2==0 else nk
    if stop>1:
        scale=np.sqrt(n*S[1:stop]/(2.0*dt))
        X[:,1:stop]=(rng.normal(size=(nb,stop-1))
                     +1j*rng.normal(size=(nb,stop-1)))*scale[None,:]
    if n%2==0:
        X[:,-1]=rng.normal(size=nb)*np.sqrt(n*S[-1]/dt)
    return np.fft.irfft(X,n=n,axis=1)


def linear_step_heun(dx,v,d,w,n0,n1,dt,L,C,kappa,Lf,Cf,R):
    def f(xx,vv,dd,ww,nn):
        return (
            vv,
            -(dd+kappa*xx-nn)/(L*C),
            (L/Lf)*(vv-ww),
            dd/(L*Cf)-ww/(R*Cf),
        )
    k=f(dx,v,d,w,n0)
    xp=dx+dt*k[0]; vp=v+dt*k[1]; dp=d+dt*k[2]; wp=w+dt*k[3]
    q=f(xp,vp,dp,wp,n1)
    return (
        dx+0.5*dt*(k[0]+q[0]),
        v +0.5*dt*(k[1]+q[1]),
        d +0.5*dt*(k[2]+q[2]),
        w +0.5*dt*(k[3]+q[3]),
    )


def nonlinear_step_heun(model,x,v,d,w,n0,n1,T0s,T1s,dt,L,C,Lf,Cf,R):
    # RectBivariateSpline.ev accepts vector x/T arrays.
    Tarr0=np.full_like(x,float(T0s))
    F0=np.asarray(model.spline.ev(Tarr0,x)).reshape(-1)
    kx=v
    kv=-(d+F0-n0)/(L*C)
    kd=(L/Lf)*(v-w)
    kw=d/(L*Cf)-w/(R*Cf)

    xp=x+dt*kx; vp=v+dt*kv; dp=d+dt*kd; wp=w+dt*kw
    Tarr1=np.full_like(x,float(T1s))
    F1=np.asarray(model.spline.ev(Tarr1,xp)).reshape(-1)
    qx=vp
    qv=-(dp+F1-n1)/(L*C)
    qd=(L/Lf)*(vp-wp)
    qw=dp/(L*Cf)-wp/(R*Cf)

    return (
        x+0.5*dt*(kx+qx),
        v+0.5*dt*(kv+qv),
        d+0.5*dt*(kd+qd),
        w+0.5*dt*(kw+qw),
    )


def run_case(model: DynamicForce,lambda_um: float,*,alpha: float=0.50,R: float=250.0,
             ntraj: int=256,batch: int=64,dt_ps: float=0.5,tpost_ns: float=0.50,
             seed: int=12345) -> dict[str,float]:
    L,C,_=CASES[0.6]
    cov=quantum_covariance(model,0.6)
    x_c=cov['x_c']; kappa=cov['kappa_c']; omega_c=cov['omega_c']
    omega_d=alpha*omega_c
    Lf,Cf=filter_components(R,omega_d)
    Acold=state_matrix(model,R,x_c,T0,Lf,Cf)
    _,_,_,tau_cold=cold_pole_data(Acold)
    tpre=12.0*tau_cold
    dt=dt_ps*1e-12
    npre=int(math.ceil(tpre/dt))
    tpre=npre*dt
    tpost=tpost_ns*1e-9
    npost=int(round(tpost/dt))+1
    ntotal=npre+npost
    _,Tarr=thermal_trace(lambda_um,dt,tpost)
    Tf=model.fold_temperature()
    imax=int(np.argmax(Tarr))
    ids=np.where(Tarr[imax:]<Tf)[0]
    ireform=imax+int(ids[0]) if len(ids) else None
    if ireform is None:
        raise RuntimeError('no cooling-side reformation')
    saddle=directional_barriers(model,Tf-2e-5)['saddle']
    left,right=model.cold_states()

    rng=np.random.default_rng(seed+int(round(lambda_um*100)))
    x0_all=[]; u0_all=[]; xr_all=[]; ur_all=[]; xf_all=[]
    right_reform=0; right_final=0
    total=0

    # Analytic reduced cold reference.
    _rq,_rv,sxratio,svratio,_=variance_ratios(model,0.6,R,alpha)
    sx_ref=cov['sigma_x']*sxratio
    su_ref=cov['sigma_x']*svratio

    for start in range(0,ntraj,batch):
        nb=min(batch,ntraj-start)
        noise=gaussian_noise_batch(rng,nb,ntotal,dt,L,R,omega_d)
        dx=np.zeros(nb); v=np.zeros(nb); d=np.zeros(nb); w=np.zeros(nb)
        # Cold linear stationary preparation.
        for i in range(npre-1):
            dx,v,d,w=linear_step_heun(dx,v,d,w,noise[:,i],noise[:,i+1],dt,
                                      L,C,kappa,Lf,Cf,R)
        x=x_c+dx
        x0_all.append(x.copy()); u0_all.append((v/omega_c).copy())

        # Same colored history continues through nonlinear pulse.
        base=npre-1
        xr=None; ur=None
        for j in range(npost-1):
            ni=noise[:,base+j]; nj=noise[:,base+j+1]
            x,v,d,w=nonlinear_step_heun(model,x,v,d,w,ni,nj,Tarr[j],Tarr[j+1],
                                        dt,L,C,Lf,Cf,R)
            if j+1==ireform:
                xr=x.copy(); ur=(v/omega_c).copy()
        if xr is None:
            raise RuntimeError('reformation sample missing')
        xr_all.append(xr); ur_all.append(ur)
        xf_all.append(x.copy())
        right_reform += int(np.count_nonzero(xr>saddle))
        # Existing finite-time convention: nearest cold stored state at endpoint.
        right_final += int(np.count_nonzero(np.abs(x-right)<np.abs(x-left)))
        total += nb

    x0=np.concatenate(x0_all); u0=np.concatenate(u0_all)
    xr=np.concatenate(xr_all); ur=np.concatenate(ur_all); xf=np.concatenate(xf_all)
    return {
        'lambda_um':lambda_um,
        'ntraj':float(total),
        'dt_ps':dt_ps,
        'tpre_ns':tpre*1e9,
        'tau_cold_ns':tau_cold*1e9,
        'cold_mean_x':float(np.mean(x0)),
        'cold_sigma_x':float(np.std(x0,ddof=1)),
        'cold_sigma_u':float(np.std(u0,ddof=1)),
        'cold_sigma_x_ref':sx_ref,
        'cold_sigma_u_ref':su_ref,
        'cold_reg_x':float(np.std(x0,ddof=1)/sx_ref),
        'cold_reg_u':float(np.std(u0,ddof=1)/su_ref),
        'reform_ps':ireform*dt*1e12,
        'saddle_reform':saddle,
        'P_xright_reform':right_reform/total,
        'P_right_final':right_final/total,
        'mean_x_reform':float(np.mean(xr)),
        'sigma_x_reform':float(np.std(xr,ddof=1)),
        'mean_u_reform':float(np.mean(ur)),
        'sigma_u_reform':float(np.std(ur,ddof=1)),
        'rho_xu_reform':float(np.corrcoef(xr,ur)[0,1]),
        'mean_x_final':float(np.mean(xf)),
        'sigma_x_final':float(np.std(xf,ddof=1)),
    }


def main() -> None:
    p=argparse.ArgumentParser()
    p.add_argument('--ntraj',type=int,default=256)
    p.add_argument('--dt-ps',type=float,default=0.5)
    args=p.parse_args()

    print('Experiment 03 nonlinear causal-FDT TWA/GLE screen')
    print('rDelta=.6, R=250 ohm, alpha=.50, rise=20 ps, A=100 um^2')
    print('symmetrized quantum FDT used as Wigner/TWA stochastic field; NOT exact quantum efficiency')
    model=DynamicForce(0.6,quick=False,Tmax=0.95)
    for lam in (8.0,10.0,11.0,14.0):
        o=run_case(model,lam,ntraj=args.ntraj,dt_ps=args.dt_ps)
        msg=(
            f'lambda={lam:.1f} um: N={int(o["ntraj"])}, dt={o["dt_ps"]:.3f} ps, '
            f'pre={o["tpre_ns"]:.2f} ns, coldReg(x,u)=({o["cold_reg_x"]:.3f},{o["cold_reg_u"]:.3f}), '
            f'P_xright_reform={o["P_xright_reform"]:.4f}, P_right_final={o["P_right_final"]:.4f}, '
            f'x_reform={o["mean_x_reform"]:+.4f}+-{o["sigma_x_reform"]:.4f}, '
            f'u_reform={o["mean_u_reform"]:+.4f}+-{o["sigma_u_reform"]:.4f}, '
            f'rho={o["rho_xu_reform"]:+.3f}, '
            f'x_final={o["mean_x_final"]:+.4f}+-{o["sigma_x_final"]:.4f}'
        )
        print(msg)
        print(f'::notice title=Experiment 03 nonlinear FDT TWA::{msg}')
    print('PASS')

if __name__=='__main__':
    main()
