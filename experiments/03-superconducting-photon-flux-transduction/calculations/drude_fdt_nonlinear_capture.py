#!/usr/bin/env python3
"""Best-case zero-temperature FDT noise screen for nonlinear Drude capture.

This is the first Experiment-03 calculation that keeps one continuous
symmetrized quantum-FDT noise record through bath preparation and the optical
write event.

For each trajectory:

1. Start in the left cold minimum.
2. Pre-run the full *cold nonlinear* Drude dynamics for `pre_ns` under a
   stationary T_b=0 Norton current noise record with

       S_I^sym(omega)=hbar |omega| Re Y(omega).

3. At the photon time, fork the identical conditioned state into three paired
   arms using the same future noise realization:

   A. photon + continued bath fluctuations,
   B. photon + fluctuations switched off after launch,
   C. no photon + continued bath fluctuations.

4. At the recovery time, report right-side occupation and a deterministic
   commitment proxy: if the fluctuation force were removed at that instant,
   is the extended Drude state below the cold separatrix energy on the target
   side?

This is a *symmetrized-noise Wigner/truncated-Wigner screen*, not exact nonlinear
open-quantum dynamics.  The cold harmonic stationarity regression must be
validated separately.  T_b=0 is the minimum equilibrium FDT noise for a fixed
passive Y(omega), so this is deliberately an optimistic bath-noise stress.
"""
from __future__ import annotations

import math
import numpy as np

from full_dynamic_rfsquid import (
    CASES, DynamicForce, T0, TAU0_CONDITIONAL,
    adiabatic_photon_temperature,
)
from finite_time_basin_slice import cold_phase_scale
from quantum_initial_capture import PHI_BAR
from drude_correlated_capture import force_fast, cold_energy_classifier
from drude_fdt_stationarity import synthesize_zeroT_current_noise


def phase_step(model,x,v,j,n1,nm,n4,dt,L,C,G0,tauD,T1,Tm,T4):
    def rhs(xx,vv,jj,nn,TT):
        F=force_fast(model,TT,xx)
        return vv, -(L*jj+F-L*nn)/(L*C), (G0*vv-jj)/tauD
    kx1,kv1,kj1=rhs(x,v,j,n1,T1)
    kx2,kv2,kj2=rhs(x+0.5*dt*kx1,v+0.5*dt*kv1,j+0.5*dt*kj1,nm,Tm)
    kx3,kv3,kj3=rhs(x+0.5*dt*kx2,v+0.5*dt*kv2,j+0.5*dt*kj2,nm,Tm)
    kx4,kv4,kj4=rhs(x+dt*kx3,v+dt*kv3,j+dt*kj3,n4,T4)
    x=x+dt*(kx1+2*kx2+2*kx3+kx4)/6.0
    v=v+dt*(kv1+2*kv2+2*kv3+kv4)/6.0
    j=j+dt*(kj1+2*kj2+2*kj3+kj4)/6.0
    return x,v,j


def thermal_rk4(u,t,dt,du_ph,tau_r,cool,u0):
    def f(tt,uu):
        uu=max(float(uu),u0)
        src=du_ph/tau_r*math.exp(-tt/tau_r)
        return src-cool*(uu*uu-u0*u0)
    k1=f(t,u); k2=f(t+0.5*dt,u+0.5*dt*k1)
    k3=f(t+0.5*dt,u+0.5*dt*k2); k4=f(t+dt,u+dt*k3)
    un=u+dt*(k1+2*k2+2*k3+k4)/6.0
    um=u+0.5*dt*k1  # midpoint predictor is sufficient for phase-force RK stages
    return max(un,u0),max(um,u0)


def propagate_pre(model,x,v,j,noise,dt,npre,L,C,G0,tauD):
    T=T0
    for k in range(npre):
        n1=noise[:,k]/PHI_BAR; n4=noise[:,k+1]/PHI_BAR; nm=0.5*(n1+n4)
        x,v,j=phase_step(model,x,v,j,n1,nm,n4,dt,L,C,G0,tauD,T,T,T)
    return x,v,j


def propagate_post(model,x,v,j,noise,offset,npost,dt,L,C,G0,tauD,
                   *,photon: bool, noisy: bool):
    u0=T0*T0
    if photon:
        Tad=adiabatic_photon_temperature(14.0,100.0)
        du_ph=Tad*Tad-u0; tau_r=20e-12
        cool=1/(2*TAU0_CONDITIONAL*u0)
    else:
        du_ph=0.0; tau_r=20e-12; cool=1/(2*TAU0_CONDITIONAL*u0)
    u=u0; t=0.0
    zeros=np.zeros_like(x)
    for kk in range(npost):
        k=offset+kk
        if noisy:
            n1=noise[:,k]/PHI_BAR; n4=noise[:,k+1]/PHI_BAR; nm=0.5*(n1+n4)
        else:
            n1=nm=n4=zeros
        if photon:
            un,um=thermal_rk4(u,t,dt,du_ph,tau_r,cool,u0)
            T1=math.sqrt(max(u,u0)); Tm=math.sqrt(max(um,u0)); T4=math.sqrt(max(un,u0))
            u=un
        else:
            T1=Tm=T4=T0
        x,v,j=phase_step(model,x,v,j,n1,nm,n4,dt,L,C,G0,tauD,T1,Tm,T4)
        t+=dt
    return x,v,j,math.sqrt(max(u,u0))


def run_seed(seed:int,R0=360.0,d=3.0,ntraj=512,dt_ps=0.2,pre_ns=2.0,post_ns=2.0):
    model=DynamicForce(0.6,quick=False)
    L,C,_=CASES[0.6]; left,right=model.cold_states()
    _,_,omega0=cold_phase_scale(model,0.6)
    omegaD=d*omega0; tauD=1/omegaD; G0=1/R0
    dt=dt_ps*1e-12
    npre=int(round(pre_ns*1e-9/dt)); npost=int(round(post_ns*1e-9/dt))
    nt=npre+npost+1
    rng=np.random.default_rng(seed)
    noise=synthesize_zeroT_current_noise(ntraj,nt,dt,G0,omegaD,rng)

    x=np.full(ntraj,left); v=np.zeros(ntraj); j=np.zeros(ntraj)
    x0,v0,j0=propagate_pre(model,x,v,j,noise,dt,npre,L,C,G0,tauD)
    roots=model.roots(T0); xs=[xx for xx,k in roots if k<0 and left<xx<right][0]
    p_pre_right=float(np.mean(x0>xs))

    xa,va,ja,Tfa=propagate_post(model,x0.copy(),v0.copy(),j0.copy(),noise,npre,npost,dt,L,C,G0,tauD,photon=True,noisy=True)
    xb,vb,jb,Tfb=propagate_post(model,x0.copy(),v0.copy(),j0.copy(),noise,npre,npost,dt,L,C,G0,tauD,photon=True,noisy=False)
    xc,vc,jc,Tfc=propagate_post(model,x0.copy(),v0.copy(),j0.copy(),noise,npre,npost,dt,L,C,G0,tauD,photon=False,noisy=True)

    ta,ra,_=cold_energy_classifier(model,R0,d,xa,va,ja)
    tb,rb,_=cold_energy_classifier(model,R0,d,xb,vb,jb)
    tc,rc,_=cold_energy_classifier(model,R0,d,xc,vc,jc)

    pa=float(np.mean(ta)); pb=float(np.mean(tb)); pc=float(np.mean(tc))
    pra=float(np.mean(ra)); prb=float(np.mean(rb)); prc=float(np.mean(rc))
    flip_ab=float(np.mean(ta!=tb))
    msg=(f'seed={seed} N={ntraj} R0={R0:g} d={d:g} dt={dt_ps:g}ps '
         f'preRight={p_pre_right:.6f}; '
         f'photon+noise Ptrap={pa:.6f} Pright={pra:.6f}; '
         f'photon noiseOff Ptrap={pb:.6f} Pright={prb:.6f}; '
         f'dark+noise Ptrap={pc:.6f} Pright={prc:.6f}; '
         f'pairedOutcomeChange={flip_ab:.6f}; Tph_final={Tfa:.5f}K')
    print(msg); print(f'::notice title=Experiment 03 zero-point noisy capture::{msg}')
    return pa,pb,pc,flip_ab


def main():
    rows=[]
    for seed in (13,47,91,131): rows.append(run_seed(seed))
    a=np.asarray(rows)
    names=('photon+noise','photon-noiseOff','dark+noise','paired-change')
    for i,name in enumerate(names):
        v=a[:,i]
        print(f'{name}: mean={v.mean():.6f} std={v.std(ddof=1):.6f} min={v.min():.6f} max={v.max():.6f}')
    print('PASS')

if __name__=='__main__': main()
