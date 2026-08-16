#!/usr/bin/env python3
"""Solve the delta=.214 one-loop dark-rate target on the dominant large periodic branch.

The branch-topology calculation proves that the local first-Matsubara sphaleron
instability is not the physical action crossover.  A distinct finite-amplitude,
one-negative periodic bounce remains lower in action through the local boundary
and crosses the thermal sphaleron only at T*/T_local ~= 1.02362.

This script explicitly seeds/continues that large branch and evaluates the same
UV-corrected, cubic-calibrated Gaussian one-loop determinant.  The first goal is
only to determine whether Gamma=1e-6/s is reached before the *local* boundary;
if so, no soft-mode uniformization is needed for the accepted .214 design point.
"""
from __future__ import annotations
import math
import numpy as np
from scipy.optimize import brentq

import full_dynamic_rfsquid as fd
import finiteT_nonlocal_periodic_bounce as ft
import finiteT_nonlocal_periodic_bounce_v2 as ft2
import finiteT_prefactor_determinant_anatomy as da
import finiteT_determinant_uv_tail as uv

C0=215e-15; R0=80.0; D=.214; TARGET=1e-6; LOGT=math.log(TARGET)


def large_saddle(st,Tx,Ttarget,nbasis=48,ngrid=6144):
    # Seed the finite-amplitude one-negative branch at .94 Tx exactly as in the
    # branch-topology / first-order continuation diagnostics.
    Tcur=.94*Tx; sys=ft.periodic_system(st,Tcur,nbasis,ngrid)
    ys=st['xs']-st['xm']; scale=max(st['xr']-st['xs'],st['xs']-st['xm'])
    cand=[]
    for frac in (.12,.20,.32,.48,.70,1.0):
        for sgn in (+1.,-1.):
            a=np.zeros(nbasis+1); a[0]=ys; a[1]=sgn*frac*scale
            o=ft.solve_stationary(sys,a,maxfev=20000)
            path=sys['B']@o['a']; amp=.5*(float(np.max(path))-float(np.min(path)))
            if o['success'] and o['grad']<3e-7 and int(np.sum(o['ev']<0))==1 and amp>.04:
                cand.append((o,amp))
    if not cand: raise RuntimeError('failed to seed large branch')
    o,amp=min(cand,key=lambda z:z[0]['B'])
    # Continue gently from .94 Tx to actual Ttarget, whether below or above Tx.
    nstep=max(10,int(math.ceil(abs(Ttarget-Tcur)/max(.00015,.008*Ttarget))))
    for T in np.linspace(Tcur,Ttarget,nstep+1)[1:]:
        ns=ft.periodic_system(st,float(T),nbasis,ngrid)
        a0=ft.project_coeffs(sys,o['a'],ns)
        no=ft.solve_stationary(ns,a0,maxfev=20000)
        path=ns['B']@no['a']; amp=.5*(float(np.max(path))-float(np.min(path)))
        if (not no['success']) or no['grad']>2e-6 or int(np.sum(no['ev']<0))!=1 or amp<.02:
            raise RuntimeError(f'large branch lost at T={T}: success={no["success"]} grad={no["grad"]} nneg={int(np.sum(no["ev"]<0))} amp={amp}')
        sys,o=ns,no
    return sys,o,amp


def state(r,nbasis=48,ngrid=6144):
    C=C0*r*r; R=R0/r
    st=ft2.static_model(D,C,R); Tx,_=ft2.exact_crossover(st)
    sys,o,amp=large_saddle(st,Tx,fd.T0,nbasis,ngrid)
    q=da.orthonormal_hessians(st,sys,o)
    tail,_,_=uv.uv_tail(st,sys,o,nbasis)
    logD=q['logD']+tail
    logA=math.log(st['wc'])+.5*math.log(q['Is']/(2*math.pi))+logD
    B=float(o['B']); lg=logA-B
    return dict(r=r,st=st,Tx=Tx,sys=sys,o=o,amp=amp,B=B,logD=logD,
                Is=q['Is'],zero=q['zero_overlap'],A=math.exp(logA),logGamma=lg,
                Gamma=math.exp(lg),nneg=int(np.sum(o['ev']<0)))


def main():
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    try:
        stbase=ft2.static_model(D,C0,R0); Tx0,_=ft2.exact_crossover(stbase)
        rlocal=Tx0/fd.T0
        # The first-order action crossover ratio from the independent continuation.
        raction=rlocal*1.023623633
        print(f'delta=.214 r_local={rlocal:.9f} r_action_cross_est={raction:.9f}')
        # Start from the old near-boundary scan point and remain below local first.
        grid=np.linspace(11.45,rlocal*.9995,7)
        rows=[]
        for r in grid:
            s=state(float(r),40,5120); rows.append(s)
            print(f'scan r={r:.9f} Gamma={s["Gamma"]:.6e}/s B={s["B"]:.8f} A1={s["A"]:.6e}/s T0/Tlocal={fd.T0/s["Tx"]:.8f} amp={s["amp"]:.7f}')
        bracket=None
        for a,b in zip(rows[:-1],rows[1:]):
            if (a['logGamma']-LOGT)*(b['logGamma']-LOGT)<=0:
                bracket=(a['r'],b['r']); break
        if bracket is None:
            print('NO_ROOT_BELOW_LOCAL; extending on regular large branch toward true action crossing')
            grid2=np.linspace(rlocal*1.0005,raction*.985,7)
            prev=rows[-1]
            for r in grid2:
                s=state(float(r),40,5120)
                print(f'postlocal r={r:.9f} Gamma={s["Gamma"]:.6e}/s B={s["B"]:.8f} A1={s["A"]:.6e}/s T0/Tlocal={fd.T0/s["Tx"]:.8f} amp={s["amp"]:.7f}')
                if (prev['logGamma']-LOGT)*(s['logGamma']-LOGT)<=0:
                    bracket=(prev['r'],s['r']); break
                prev=s
        if bracket is None:
            raise RuntimeError('no large-branch Gamma target root before conservative true-action-crossover margin')
        cache={}
        def f(r):
            k=round(float(r),9)
            if k not in cache: cache[k]=state(float(r),40,5120)
            return cache[k]['logGamma']-LOGT
        rr=brentq(f,*bracket,xtol=2e-5,rtol=1e-6,maxiter=40)
        sf=state(rr,80,10240)
        C=C0*rr*rr; R=R0/rr
        msg=(f'delta=.214 r_rate_large={rr:.9f} C={C*1e15:.3f}fF R={R:.6f}ohm '
             f'fc={sf["st"]["wc"]/(2*math.pi)*1e-9:.6f}GHz B20={sf["B"]:.9f} '
             f'A1={sf["A"]:.6e}/s Gamma1={sf["Gamma"]:.6e}/s '
             f'T0/Tlocal={fd.T0/sf["Tx"]:.9f} amp={sf["amp"]:.8f} '
             f'nneg={sf["nneg"]} zeroOverlap={sf["zero"]:.9f} '
             f'r/r_local={rr/rlocal:.9f} r/r_action={rr/raction:.9f}')
        print(msg); print(f'::notice title=Experiment 03 delta .214 large-branch rate::{msg}')
        if sf['nneg']!=1 or sf['zero']<.999 or abs(math.log(sf['Gamma']/TARGET))>.04:
            raise RuntimeError('final large-branch rate regression failed')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot

if __name__=='__main__': main()
