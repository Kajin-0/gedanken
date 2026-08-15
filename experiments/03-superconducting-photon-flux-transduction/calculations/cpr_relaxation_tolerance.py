#!/usr/bin/env python3
"""Tolerance of the current best write branch to finite CPR response time.

The established dynamic solver assumes the equilibrium current-phase relation
responds instantaneously to the prescribed electronic temperature T_e(t).  That
requires Andreev/supercurrent occupations to track the hot distribution on the
write timescale.

As a falsification screen introduce one phenomenological delayed current
coordinate J_eff:

    tau_CPR dJ_eff/dt + J_eff = J_eq[x,T_e(t)],

with

    J_eq(x,T) = x-delta-F_eq(x,T)

in the normalized rf-SQUID units already used by the solver.  The phase equation
becomes

    L C xddot + d + x-delta-J_eff = n_ext.

At t=0 J_eff is initialized to the instantaneous cold equilibrium value for
each prepared phase sample.  The external stationary causal bath is unchanged.

IMPORTANT
---------
This is a response-lag tolerance model, not a microscopic ABS kinetic theory.
It does not add the dissipation/noise that a real delayed susceptibility may
require by causality/FDT.  Therefore:
- rapid failure at small tau_CPR is a strong feasibility warning;
- survival to large tau_CPR does not by itself establish microscopic validity.

Results remain external-bath TWA/GLE screening fractions, not exact quantum
efficiencies.
"""
from __future__ import annotations
import argparse, math
import numpy as np

from causal_two_pole_environment import filter_components
from directional_recovery_barriers import directional_barriers
from full_dynamic_rfsquid import CASES, DELTA_TILT, DynamicForce, T0
from history_fdt_reformation_margin import cold_pole_data, state_matrix
from nonlinear_fdt_twa_screen import gaussian_noise_batch, linear_step_heun, thermal_trace
from nonlinear_fdt_twa_convergence import wilson
from quantum_initial_capture import quantum_covariance
from two_pole_cold_variance import variance_ratios


def eq_current(model,x,T):
    Tarr=np.full_like(x,float(T))
    F=np.asarray(model.spline.ev(Tarr,x)).reshape(-1)
    return x-DELTA_TILT-F


def step_lag(model,x,v,d,w,jj,n0,n1,T0s,T1s,dt,L,C,Lf,Cf,R,tau):
    I0=eq_current(model,x,T0s)
    kx=v
    kv=-(d+x-DELTA_TILT-jj-n0)/(L*C)
    kd=(L/Lf)*(v-w)
    kw=d/(L*Cf)-w/(R*Cf)
    kj=(I0-jj)/tau

    xp=x+dt*kx; vp=v+dt*kv; dp=d+dt*kd; wp=w+dt*kw; jp=jj+dt*kj
    I1=eq_current(model,xp,T1s)
    qx=vp
    qv=-(dp+xp-DELTA_TILT-jp-n1)/(L*C)
    qd=(L/Lf)*(vp-wp)
    qw=dp/(L*Cf)-wp/(R*Cf)
    qj=(I1-jp)/tau
    return (x+.5*dt*(kx+qx),v+.5*dt*(kv+qv),d+.5*dt*(kd+qd),
            w+.5*dt*(kw+qw),jj+.5*dt*(kj+qj))


def step_instant(model,x,v,d,w,n0,n1,T0s,T1s,dt,L,C,Lf,Cf,R):
    T0a=np.full_like(x,float(T0s)); F0=np.asarray(model.spline.ev(T0a,x)).reshape(-1)
    kx=v; kv=-(d+F0-n0)/(L*C); kd=(L/Lf)*(v-w); kw=d/(L*Cf)-w/(R*Cf)
    xp=x+dt*kx; vp=v+dt*kv; dp=d+dt*kd; wp=w+dt*kw
    T1a=np.full_like(x,float(T1s)); F1=np.asarray(model.spline.ev(T1a,xp)).reshape(-1)
    qx=vp; qv=-(dp+F1-n1)/(L*C); qd=(L/Lf)*(vp-wp); qw=dp/(L*Cf)-wp/(R*Cf)
    return (x+.5*dt*(kx+qx),v+.5*dt*(kv+qv),d+.5*dt*(kd+qd),w+.5*dt*(kw+qw))


def run(model,tau_ps,*,R=80.,alpha=.90,ntraj=1024,batch=64,dt_ps=.5,seed=454545):
    L,C,_=CASES[.6]; cov=quantum_covariance(model,.6)
    xc=cov['x_c']; kap=cov['kappa_c']; wc=cov['omega_c']; wd=alpha*wc
    Lf,Cf=filter_components(R,wd); Ac=state_matrix(model,R,xc,T0,Lf,Cf)
    _,_,_,tau_cold=cold_pole_data(Ac)
    dt=dt_ps*1e-12; npre=int(math.ceil(12*tau_cold/dt)); tpost=.5e-9
    npost=int(round(tpost/dt))+1; nt=npre+npost
    _,T=thermal_trace(8.0,dt,tpost,area_um2=100.,rise_ps=20.)
    Tf=model.fold_temperature(); im=int(np.argmax(T)); ids=np.where(T[im:]<Tf)[0]
    ir=im+int(ids[0]); saddle=directional_barriers(model,Tf-2e-5)['saddle']
    left,right=model.cold_states()
    _,_,sxr,sur,_=variance_ratios(model,.6,R,alpha)
    sxref=cov['sigma_x']*sxr; suref=cov['sigma_x']*sur
    rng=np.random.default_rng(seed); kf=kr=tot=0; x0s=[];u0s=[];xrs=[];urs=[]
    tau=tau_ps*1e-12
    for st in range(0,ntraj,batch):
        nb=min(batch,ntraj-st); noise=gaussian_noise_batch(rng,nb,nt,dt,L,R,wd)
        dx=np.zeros(nb);v=np.zeros(nb);d=np.zeros(nb);w=np.zeros(nb)
        for i in range(npre-1):
            dx,v,d,w=linear_step_heun(dx,v,d,w,noise[:,i],noise[:,i+1],dt,L,C,kap,Lf,Cf,R)
        x=xc+dx; x0s.append(x.copy());u0s.append((v/wc).copy()); base=npre-1
        if tau_ps>0: jj=eq_current(model,x,T0)
        xr=ur=None
        for j in range(npost-1):
            if tau_ps<=0:
                x,v,d,w=step_instant(model,x,v,d,w,noise[:,base+j],noise[:,base+j+1],
                                     T[j],T[j+1],dt,L,C,Lf,Cf,R)
            else:
                x,v,d,w,jj=step_lag(model,x,v,d,w,jj,noise[:,base+j],noise[:,base+j+1],
                                    T[j],T[j+1],dt,L,C,Lf,Cf,R,tau)
            if j+1==ir: xr=x.copy();ur=(v/wc).copy()
        xrs.append(xr);urs.append(ur);kr+=int(np.count_nonzero(xr>saddle))
        kf+=int(np.count_nonzero(np.abs(x-right)<np.abs(x-left)));tot+=nb
    x0=np.concatenate(x0s);u0=np.concatenate(u0s);xr=np.concatenate(xrs);ur=np.concatenate(urs)
    return dict(n=tot,kf=kf,kr=kr,Pf=kf/tot,Pr=kr/tot,
                crx=float(np.std(x0,ddof=1)/sxref),cru=float(np.std(u0,ddof=1)/suref),
                mx=float(np.mean(xr)),sx=float(np.std(xr,ddof=1)),
                mu=float(np.mean(ur)),su=float(np.std(ur,ddof=1)),rho=float(np.corrcoef(xr,ur)[0,1]))


def main():
    p=argparse.ArgumentParser();p.add_argument('--ntraj',type=int,default=1024);p.add_argument('--dt-ps',type=float,default=.5);p.add_argument('--seed',type=int,default=454545);a=p.parse_args()
    print('Experiment 03 finite CPR-response tolerance; R80 alpha.90 8-um-equivalent')
    model=DynamicForce(.6,quick=False,Tmax=.95)
    for tau in (0.,.5,1.,2.,3.,5.,7.5,10.,15.,20.,30.,40.,50.,75.,100.,150.):
        o=run(model,tau,ntraj=a.ntraj,dt_ps=a.dt_ps,seed=a.seed);lo,hi=wilson(o['kf'],o['n'])
        msg=(f'tauCPR={tau:g} ps: coldReg=({o["crx"]:.4f},{o["cru"]:.4f}), '
             f'P_reform={o["Pr"]:.6f}, P_final={o["Pf"]:.6f} CI95=[{lo:.6f},{hi:.6f}] fail={o["n"]-o["kf"]}, '
             f'xR={o["mx"]:+.4f}+-{o["sx"]:.4f}, uR={o["mu"]:+.4f}+-{o["su"]:.4f}, rho={o["rho"]:+.3f}')
        print(msg);print(f'::notice title=Experiment 03 CPR-relaxation tolerance::{msg}')
    print('PASS')

if __name__=='__main__': main()
