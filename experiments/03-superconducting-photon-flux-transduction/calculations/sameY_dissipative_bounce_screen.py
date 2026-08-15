#!/usr/bin/env python3
"""Cold dark-tunneling screen using the SAME causal environment as write capture.

This replaces the historical bare cubic-MQT exponent by two stronger objects:

1. the zero-temperature undamped WKB/bounce action evaluated from the actual
   cold full-CPR rf-SQUID potential;
2. the Euclidean influence-action increment of the retained passive two-pole
   environment, evaluated on a variational sech^2 bounce whose width is
   optimized against the actual local action.

For the phase flux coordinate q=Phi_bar x, the cold Euclidean action is

  S_E = int d tau [ C Phi_bar^2 xdot^2/2 + U(x)-U(x_m) ]
        + (Phi_bar^2 T/2) sum_n |omega_n| Y_E(|omega_n|) |x_n|^2,

where T=beta*hbar and Y_E(s) is the positive-real Laplace admittance of the
same passive network used in real-time capture:

  Y_E(s)= (1/R) [1+s/(sqrt(2)omega_D)]
                 /[1+sqrt(2)s/omega_D+(s/omega_D)^2].

For an Ohmic limit this reduces to the standard |omega_n|/R Caldeira-Leggett
kernel.  The dissipative term is positive for this passive network.

IMPORTANT
---------
- The undamped action from the actual potential is a controlled 1D WKB result.
- The environmental correction is a SAME-Y variational/first-order screen, not
  the exact nonlocal dissipative bounce.  If S_env is small/moderate it is the
  first correction to the undamped bounce action; if large it only signals
  strong suppression and perturbation theory is not quantitative.
- Rate prefactors are not computed.  Report exponents and suppression factors.
- This does not replace a final dissipative instanton calculation if the paper
  depends on precise dark rates.
"""
from __future__ import annotations

import math
import copy

import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.interpolate import CubicSpline, RectBivariateSpline
from scipy.optimize import brentq, minimize_scalar

from directional_recovery_barriers import directional_barriers, kelvin_scale
from full_dynamic_rfsquid import CASES, DELTA_TILT, DynamicForce, T0
from quantum_initial_capture import HBAR, KB, PHI_BAR

SQRT2=math.sqrt(2.0)


def with_tilt(base: DynamicForce,delta: float)->DynamicForce:
    m=copy.copy(base)
    m.Ftab=np.asarray(base.Ftab,dtype=float)-(delta-DELTA_TILT)
    m.spline=RectBivariateSpline(m.Tgrid,m.xgrid,m.Ftab,kx=3,ky=3)
    return m


def potential_data(model:DynamicForce,nx:int=40001):
    b=directional_barriers(model,T0)
    xm=float(b['left']); xs=float(b['saddle']); xr=float(b['right'])

    # Find the post-saddle turning point where U(x_t)=U(x_m).
    def udiff(x):
        xx=np.linspace(xm,x,3001)
        TT=np.full_like(xx,T0)
        FF=np.asarray(model.spline.ev(TT,xx)).reshape(-1)
        return float(np.trapezoid(FF,xx))
    # At saddle positive; at favored right minimum the potential is lower for
    # the retained positive tilt.
    us=udiff(xs); ur=udiff(xr)
    if not (us>0 and ur<0):
        raise RuntimeError(f'no metastable decay turning bracket: Us={us}, Ur={ur}')
    xt=brentq(udiff,xs+1e-8,xr-1e-8,xtol=2e-12)

    x=np.linspace(xm,xt,nx)
    TT=np.full_like(x,T0)
    F=np.asarray(model.spline.ev(TT,x)).reshape(-1)
    u=np.concatenate([[0.0],cumulative_trapezoid(F,x)])
    # Small accumulated endpoint error is removed by a linear correction that
    # vanishes at x_m and forces U(x_t)=0.  With nx=40001 this is tiny; report it.
    end_raw=float(u[-1])
    u=u-end_raw*(x-xm)/(xt-xm)
    uspl=CubicSpline(x,u)
    return xm,xs,xr,xt,x,u,uspl,end_raw


def exact_undamped_action(model:DynamicForce,C:float,L:float):
    xm,xs,xr,xt,x,u,uspl,end_raw=potential_data(model)
    # The barrier region has u>=0 between metastable minimum and turning point.
    integ=float(np.trapezoid(np.sqrt(np.maximum(u,0.0)),x))
    S_over_EL=2.0*math.sqrt(2.0*L*C)*integ
    return S_over_EL,(xm,xs,xr,xt,uspl,end_raw)


def sech2(z):
    # Stable for large |z|.
    az=np.abs(z)
    out=np.empty_like(az)
    mask=az<20.0
    out[mask]=1.0/np.cosh(z[mask])**2
    out[~mask]=4.0*np.exp(-2.0*az[~mask])
    return out


def ansatz_actions(model:DynamicForce,R:float,alpha:float,C:float,L:float,
                   pdata,*,N:int=32768):
    xm,xs,xr,xt,uspl,end_raw=pdata
    # cold curvature/frequency from force derivative at metastable minimum
    kappa=float(np.asarray(model.spline.ev(T0,xm,dx=0,dy=1)).reshape(-1)[0])
    wc=math.sqrt(kappa/(L*C))
    beta_hbar=HBAR/(KB*T0)
    dt=beta_hbar/N
    tau=(np.arange(N)-N//2)*dt
    amp=xt-xm
    EL_over_hbar=(PHI_BAR*PHI_BAR/L)/HBAR

    def local_for_eta(eta:float):
        a=0.5*eta*wc
        s=sech2(a*tau)
        x=xm+amp*s
        # derivative of sech^2(a t): -2a sech^2 tanh
        v=amp*(-2.0*a*s*np.tanh(a*tau))
        pot=np.maximum(uspl(x),0.0)
        S_norm=float(np.trapezoid(0.5*L*C*v*v+pot,tau))
        return S_norm

    opt=minimize_scalar(local_for_eta,bounds=(0.45,1.80),method='bounded',
                        options={'xatol':2e-5})
    eta=float(opt.x)
    a=0.5*eta*wc
    s=sech2(a*tau)
    xb=xm+amp*s
    vb=amp*(-2*a*s*np.tanh(a*tau))
    pot=np.maximum(uspl(xb),0.0)
    Slocal_norm=float(np.trapezoid(0.5*L*C*vb*vb+pot,tau))

    # Fourier-series coefficients x_n=(1/T) int x exp(-iwn t) dt.
    xd=xb-xm
    xn=np.fft.fft(xd)/N
    freq=np.fft.fftfreq(N,dt)
    om=2.0*math.pi*np.abs(freq)
    wd=alpha*wc
    yE=(1.0/R)*(1.0+om/(SQRT2*wd))/(1.0+SQRT2*om/wd+(om/wd)**2)
    kernel=om*yE
    Senv_norm=0.5*L*beta_hbar*float(np.sum(kernel*np.abs(xn)**2))

    return {
        'eta':eta,
        'wc':wc,
        'beta_wc':beta_hbar*wc,
        'Slocal_norm':Slocal_norm,
        'Senv_norm':Senv_norm,
        'Blocal':EL_over_hbar*Slocal_norm,
        'Benv':EL_over_hbar*Senv_norm,
        'Btotal_screen':EL_over_hbar*(Slocal_norm+Senv_norm),
        'log10_suppression_env':(EL_over_hbar*Senv_norm)/math.log(10.0),
    }


def main():
    print('Experiment 03 same-Y dissipative dark-bounce screen')
    base=DynamicForce(0.6,quick=False,Tmax=0.95)
    L,C,_=CASES[0.6]
    for delta in (0.05,):
        model=with_tilt(base,delta)
        S0_norm,pdata=exact_undamped_action(model,C,L)
        EL_over_hbar=(PHI_BAR*PHI_BAR/L)/HBAR
        B0=EL_over_hbar*S0_norm
        b=directional_barriers(model,T0)
        xm=pdata[0]
        kappa=float(np.asarray(model.spline.ev(T0,xm,dx=0,dy=1)).reshape(-1)[0])
        wc=math.sqrt(kappa/(L*C))
        barrierK=b['b_left']*kelvin_scale(0.6)
        Bcubic=7.2*(barrierK*KB)/(HBAR*wc)
        print(
            f'delta={delta:.3f}: exact undamped B0=S/hbar={B0:.6f}, '
            f'cubic B={Bcubic:.6f}, exact/cubic={B0/Bcubic:.6f}, '
            f'barrier/kB={barrierK:.6f} K, wc/2pi={wc/(2*math.pi)*1e-9:.5f} GHz, '
            f'turning_dx={pdata[3]-pdata[0]:.6f}, Uturn_raw_error={pdata[5]:+.3e}'
        )
        for R,alpha in [
            (150.0,.70),(150.0,.80),
            (100.0,.70),(100.0,.80),
            (80.0,.60),(80.0,.80),(80.0,1.00),
            (20.0,.90),(20.0,1.00),
        ]:
            a=ansatz_actions(model,R,alpha,C,L,pdata)
            msg=(
                f'R={R:g} alpha={alpha:.2f}: eta={a["eta"]:.4f}, '
                f'Blocal_ansatz={a["Blocal"]:.5f} ({a["Blocal"]/B0:.4f}x exact), '
                f'Benv={a["Benv"]:.5f}, Bscreen={a["Btotal_screen"]:.5f}, '
                f'env_log10_supp={a["log10_suppression_env"]:.3f}, '
                f'beta_hbar_wc={a["beta_wc"]:.2f}'
            )
            print(msg)
            print(f'::notice title=Experiment 03 same-Y dark bounce::{msg}')
    print('PASS')

if __name__=='__main__':
    main()
