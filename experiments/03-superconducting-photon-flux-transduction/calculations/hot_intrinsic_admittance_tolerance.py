#!/usr/bin/env python3
"""Thermal lower-bound tolerance to photon-activated intrinsic JJ conductance.

The established nonlinear stationary-bath TWA/GLE model includes the engineered
external causal environment but treats the heated weak link itself as purely
reactive apart from its temperature-dependent CPR.  This script adds a
parametric *hot intrinsic conductance* to determine how much internal loss/noise
the current best write branch can tolerate.

Model
-----
Use the current external candidate

    rDelta=.6, delta=.05, C=215 fF,
    R_ext=80 ohm, alpha_ext=.90,
    8-um-equivalent thermal trajectory (thermally identical to 14 um/A~57.14).

Let the intrinsic conductance be zero in the cold state and follow electronic
energy during the pulse:

    G_JJ(t) = G_pk * a_T(t),
    a_T = (T_e^2-T0^2)/(T_pk^2-T0^2), clipped to [0,1].

It adds local damping

    dv/dt |_JJ = -(G_JJ/C) v

and a classical local-equilibrium FDT current-noise increment

    <I_th(t) I_th(t')> = 2 k_B T_e(t) G_JJ(t) delta(t-t').

Thus

    dv_noise = sqrt[2 k_B T_e G_JJ]/(C Phi_bar) dW.

This thermal-noise term is a LOWER-BOUND screen for the symmetrized quantum FDT
spectrum because hbar|omega|coth[hbar|omega|/(2kT)] >= 2 kT.  It intentionally
omits the zero-point/finite-frequency excess and any colored intrinsic memory.
The conductance activation law is phenomenological, not a microscopic
Y_JJ(omega,phi,T_e).

Therefore:
- if a modest G_pk already destroys capture, that is a strong warning;
- if large G_pk is tolerated, a microscopic admittance calculation is still
  required before declaring the gate passed.

Reported fractions remain semiclassical external-bath TWA/GLE + classical hot
intrinsic thermal-noise screening numbers, not physical detector efficiencies.
"""
from __future__ import annotations

import argparse
import math

import numpy as np

from causal_two_pole_environment import filter_components
from directional_recovery_barriers import directional_barriers
from full_dynamic_rfsquid import CASES, DynamicForce, T0
from history_fdt_reformation_margin import cold_pole_data, state_matrix
from nonlinear_fdt_twa_screen import (
    gaussian_noise_batch,
    linear_step_heun,
    thermal_trace,
)
from nonlinear_fdt_twa_convergence import wilson
from quantum_initial_capture import KB, PHI_BAR, quantum_covariance
from two_pole_cold_variance import variance_ratios


def nonlinear_step_hotG(model,x,v,d,w,n0,n1,T0s,T1s,dt,L,C,Lf,Cf,Rext,
                         G0,G1,dW):
    """Deterministic Heun with local G damping + additive thermal SDE kick.

    The stochastic amplitude depends only on the prescribed common T(t), so
    Ito and Stratonovich conventions coincide for the additive state noise.
    """
    Tarr0=np.full_like(x,float(T0s))
    F0=np.asarray(model.spline.ev(Tarr0,x)).reshape(-1)
    kx=v
    kv=-(d+F0-n0)/(L*C) - (G0/C)*v
    kd=(L/Lf)*(v-w)
    kw=d/(L*Cf)-w/(Rext*Cf)

    xp=x+dt*kx; vp=v+dt*kv; dp=d+dt*kd; wp=w+dt*kw
    Tarr1=np.full_like(x,float(T1s))
    F1=np.asarray(model.spline.ev(Tarr1,xp)).reshape(-1)
    qx=vp
    qv=-(dp+F1-n1)/(L*C) - (G1/C)*vp
    qd=(L/Lf)*(vp-wp)
    qw=dp/(L*Cf)-wp/(Rext*Cf)

    xn=x+0.5*dt*(kx+qx)
    vn=v+0.5*dt*(kv+qv)
    dn=d+0.5*dt*(kd+qd)
    wn=w+0.5*dt*(kw+qw)

    # Midpoint thermal lower-bound noise amplitude.
    Tm=0.5*(float(T0s)+float(T1s))
    Gm=0.5*(G0+G1)
    if Gm>0.0:
        sig=math.sqrt(2.0*KB*Tm*Gm)/(C*PHI_BAR)
        vn = vn + sig*dW
    return xn,vn,dn,wn


def run_case(model,Gpk,*,Rext=80.0,alpha=.90,ntraj=1024,batch=64,
             dt_ps=.5,seed=777777,lambda_um=8.0,area_um2=100.0,
             rise_ps=20.0,tpost_ns=.5):
    L,C,_=CASES[0.6]
    cov=quantum_covariance(model,0.6)
    x_c=cov['x_c']; kappa=cov['kappa_c']; wc=cov['omega_c']
    wd=alpha*wc
    Lf,Cf=filter_components(Rext,wd)
    Acold=state_matrix(model,Rext,x_c,T0,Lf,Cf)
    _,_,_,tau_cold=cold_pole_data(Acold)
    dt=dt_ps*1e-12
    npre=int(math.ceil(12.0*tau_cold/dt))
    tpre=npre*dt
    tpost=tpost_ns*1e-9
    npost=int(round(tpost/dt))+1
    ntotal=npre+npost
    _,Tarr=thermal_trace(lambda_um,dt,tpost,area_um2=area_um2,rise_ps=rise_ps)
    Tpk=float(np.max(Tarr)); u0=T0*T0; upk=Tpk*Tpk
    activation=np.clip((Tarr*Tarr-u0)/(upk-u0),0.0,1.0)
    Garr=Gpk*activation

    Tf=model.fold_temperature()
    imax=int(np.argmax(Tarr)); ids=np.where(Tarr[imax:]<Tf)[0]
    ireform=imax+int(ids[0]) if len(ids) else None
    if ireform is None: raise RuntimeError('no cooling-side reformation')
    saddle=directional_barriers(model,Tf-2e-5)['saddle']
    left,right=model.cold_states()

    _rq,_rv,sxr,sur,_=variance_ratios(model,.6,Rext,alpha)
    sxref=cov['sigma_x']*sxr; suref=cov['sigma_x']*sur

    rng_ext=np.random.default_rng(seed)
    rng_hot=np.random.default_rng(seed+1000003)
    x0s=[]; u0s=[]; xrs=[]; urs=[]; xfs=[]
    kr=kf=total=0

    for start in range(0,ntraj,batch):
        nb=min(batch,ntraj-start)
        noise=gaussian_noise_batch(rng_ext,nb,ntotal,dt,L,Rext,wd)
        dx=np.zeros(nb); v=np.zeros(nb); d=np.zeros(nb); w=np.zeros(nb)
        for i in range(npre-1):
            dx,v,d,w=linear_step_heun(dx,v,d,w,noise[:,i],noise[:,i+1],dt,
                                      L,C,kappa,Lf,Cf,Rext)
        x=x_c+dx
        x0s.append(x.copy()); u0s.append((v/wc).copy())

        base=npre-1; xr=ur=None
        for j in range(npost-1):
            # Standard-normal dW for Wiener increment, paired across Gpk scans
            # by using the same intrinsic RNG seed/order.
            dW=math.sqrt(dt)*rng_hot.normal(size=nb)
            x,v,d,w=nonlinear_step_hotG(
                model,x,v,d,w,noise[:,base+j],noise[:,base+j+1],
                Tarr[j],Tarr[j+1],dt,L,C,Lf,Cf,Rext,
                float(Garr[j]),float(Garr[j+1]),dW,
            )
            if j+1==ireform:
                xr=x.copy(); ur=(v/wc).copy()
        xrs.append(xr); urs.append(ur); xfs.append(x.copy())
        kr += int(np.count_nonzero(xr>saddle))
        kf += int(np.count_nonzero(np.abs(x-right)<np.abs(x-left)))
        total += nb

    x0a=np.concatenate(x0s); u0a=np.concatenate(u0s)
    xra=np.concatenate(xrs); ura=np.concatenate(urs); xfa=np.concatenate(xfs)
    return {
        'n':total,'kr':kr,'kf':kf,'P_reform':kr/total,'P_final':kf/total,
        'cold_reg_x':float(np.std(x0a,ddof=1)/sxref),
        'cold_reg_u':float(np.std(u0a,ddof=1)/suref),
        'mean_xr':float(np.mean(xra)),'sig_xr':float(np.std(xra,ddof=1)),
        'mean_ur':float(np.mean(ura)),'sig_ur':float(np.std(ura,ddof=1)),
        'rho':float(np.corrcoef(xra,ura)[0,1]),
        'Tpk':Tpk,'reform_ps':ireform*dt*1e12,'tau_cold_ns':tau_cold*1e9,
        'mean_xf':float(np.mean(xfa)),'sig_xf':float(np.std(xfa,ddof=1)),
    }


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--ntraj',type=int,default=1024)
    p.add_argument('--dt-ps',type=float,default=.5)
    p.add_argument('--seed',type=int,default=777777)
    a=p.parse_args()
    print('Experiment 03 hot intrinsic-admittance tolerance')
    print('external candidate R=80 ohm alpha=.90; 8-um/A100 equivalent; thermal-only intrinsic FDT lower bound')
    model=DynamicForce(.6,quick=False,Tmax=.95)
    # Rhot_peak = 1/Gpk. inf means no intrinsic channel.
    for Rhot in (math.inf,20000.,10000.,5000.,3000.,2000.,1500.,1000.,750.,500.,350.,250.,150.,100.):
        Gpk=0.0 if math.isinf(Rhot) else 1.0/Rhot
        o=run_case(model,Gpk,ntraj=a.ntraj,dt_ps=a.dt_ps,seed=a.seed)
        lo,hi=wilson(o['kf'],o['n'])
        label='inf' if math.isinf(Rhot) else f'{Rhot:g}'
        msg=(
            f'Rhot_peak={label} ohm (Gpk={Gpk*1e6:.3f} uS): '
            f'coldReg=({o["cold_reg_x"]:.4f},{o["cold_reg_u"]:.4f}), '
            f'P_reform={o["P_reform"]:.6f}, '
            f'P_final={o["P_final"]:.6f} CI95=[{lo:.6f},{hi:.6f}] fail={o["n"]-o["kf"]}, '
            f'xR={o["mean_xr"]:+.4f}+-{o["sig_xr"]:.4f}, '
            f'uR={o["mean_ur"]:+.4f}+-{o["sig_ur"]:.4f}, rho={o["rho"]:+.3f}'
        )
        print(msg)
        print(f'::notice title=Experiment 03 intrinsic-hot-admittance tolerance::{msg}')
    print('PASS')

if __name__=='__main__':
    main()
