#!/usr/bin/env python3
"""Pseudo-arclength continuation through the finite-amplitude periodic-instanton fold.

The high-tilt first-order branch cannot be continued through its endpoint by
using electrical scale r as the continuation parameter.  This script promotes
p=r/r_x to an unknown and solves

    grad_a B(a,p) = 0
    t . [(a,p)-(a_pred,p_pred)] = 0

with a secant predictor and Newton corrector.  This passes through a saddle-node
turning point in p and should recover the companion periodic stationary branch.

At a genuine periodic-instanton bifurcation there must be one additional even
zero mode beyond the odd translation zero mode.  Therefore the decisive
regressions are:
  1. the one-negative physical branch approaches an even Hessian eigenvalue 0;
  2. p reaches a turning point;
  3. the companion branch emerges with two negative even modes;
  4. both solutions remain finite-amplitude periodic stationary paths.

This script maps topology only.  It does not yet assign a uniform Airy rate.
"""
from __future__ import annotations

import argparse, math
import numpy as np
from scipy.optimize import root

import full_dynamic_rfsquid as fd
import finiteT_nonlocal_periodic_bounce as ft
import finiteT_nonlocal_periodic_bounce_v2 as ft2

C0=215e-15; R0=80.0


def scaled_state(base,r):
    st=dict(base)
    C=C0*r*r; R=R0/r
    wc=math.sqrt(base['km']/(ft.L0*C))
    st.update(C=C,R=R,wc=wc,wd=ft.ALPHA*wc)
    return st


def system_at(base,rx,p,nbasis,ngrid):
    return ft.periodic_system(scaled_state(base,rx*p),fd.T0,nbasis,ngrid)


def direct_seed(base,rx,nbasis,ngrid):
    # Seed well below the fold and march to p=1.020, where all investigated
    # high-tilt cases still have the physical finite-amplitude branch.
    p0=.94
    sys=system_at(base,rx,p0,nbasis,ngrid)
    ys=base['xs']-base['xm']; scale=max(base['xr']-base['xs'],base['xs']-base['xm'])
    candidates=[]
    for frac in (.08,.14,.22,.32,.45):
        a=np.zeros(nbasis+1); a[0]=ys; a[1]=frac*scale
        o=ft.solve_stationary(sys,a,maxfev=10000)
        if o['success'] and o['grad']<2e-7 and int(np.sum(o['ev']<0))==1 and np.linalg.norm(o['a'][1:])>1e-4:
            candidates.append(o)
    if not candidates: raise RuntimeError('could not seed physical periodic branch')
    o=min(candidates,key=lambda z:z['B'])
    sols=[(p0,sys,o)]
    for p in np.arange(.945,1.0200001,.005):
        ns=system_at(base,rx,float(p),nbasis,ngrid)
        a0=ft.project_coeffs(sys,o['a'],ns)
        no=ft.solve_stationary(ns,a0,maxfev=12000)
        if not no['success'] or no['grad']>2e-7 or int(np.sum(no['ev']<0))!=1:
            raise RuntimeError(f'direct seed continuation failed at p={p}')
        sols.append((float(p),ns,no)); sys,o=ns,no
    return sols[-2],sols[-1]


def normalized_secant(z0,z1):
    t=z1-z0
    n=np.linalg.norm(t)
    if n==0: raise RuntimeError('zero secant')
    return t/n


def correct(base,rx,zpred,t,nbasis,ngrid):
    na=nbasis+1
    def residual(z):
        a=z[:na]; p=float(z[-1])
        sys=system_at(base,rx,p,nbasis,ngrid)
        g=sys['grad'](a)
        c=float(np.dot(t,z-zpred))
        return np.r_[g,c]
    def jac(z):
        a=z[:na]; p=float(z[-1])
        sys=system_at(base,rx,p,nbasis,ngrid)
        H=sys['jac'](a)
        hp=max(2e-6,2e-5*abs(p))
        gp=system_at(base,rx,p+hp,nbasis,ngrid)['grad'](a)
        gm=system_at(base,rx,p-hp,nbasis,ngrid)['grad'](a)
        dp=(gp-gm)/(2*hp)
        J=np.empty((na+1,na+1)); J[:na,:na]=H; J[:na,-1]=dp; J[-1,:]=t
        return J
    sol=root(residual,zpred,jac=jac,method='hybr',tol=3e-10,options={'xtol':3e-10,'maxfev':2000})
    z=np.asarray(sol.x,float); a=z[:na]; p=float(z[-1])
    sys=system_at(base,rx,p,nbasis,ngrid)
    o=ft.solve_stationary(sys,a,maxfev=3000)
    return sol,z,sys,o,float(np.linalg.norm(residual(z),ord=np.inf))


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--delta',type=float,required=True); a=ap.parse_args()
    d=round(a.delta,3)
    if d not in (.214,.215,.216,.217,.218): raise SystemExit('supported: .214-.218')
    nbasis=28; ngrid=3584
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    try:
        base=ft2.static_model(d,C0,R0); Tx,_=ft2.exact_crossover(base); rx=Tx/fd.T0
        (p0,s0,o0),(p1,s1,o1)=direct_seed(base,rx,nbasis,ngrid)
        z0=np.r_[o0['a'],p0]; z1=np.r_[o1['a'],p1]
        # Initial secant norm sets a natural arclength step.  Slightly shorten it
        # near the fold to avoid jumping between remote stationary branches.
        ds=.65*np.linalg.norm(z1-z0)
        print(f'delta={d:.3f} rx={rx:.9f} pseudo_ds={ds:.6e} seed_p=[{p0:.6f},{p1:.6f}]')
        rows=[]; turned=False; found_two=False; minabs=1e99
        prev_p=p1
        for j in range(48):
            t=normalized_secant(z0,z1)
            zpred=z1+ds*t
            sol,z2,sys,o,res=correct(base,rx,zpred,t,nbasis,ngrid)
            p=float(z2[-1]); ev=np.asarray(o['ev']); nneg=int(np.sum(ev<0))
            idx=np.argsort(np.abs(ev)); soft=float(ev[idx[0]])
            # On the one-negative branch the extra fold mode is the smallest
            # positive eigenvalue; on the companion it has crossed negative.
            if nneg==1:
                pos=ev[ev>0]; foldmode=float(pos[0]) if len(pos) else float('nan')
            else:
                neg=np.sort(ev[ev<0]); foldmode=float(neg[-1]) if len(neg)>=2 else float('nan')
            amp=float(math.sqrt(np.sum((o['a'][1:]**2)*sys['norms'][1:])))
            minabs=min(minabs,abs(foldmode))
            if p<prev_p-2e-5: turned=True
            if nneg>=2: found_two=True
            print(f'j={j:02d} p={p:.9f} r={rx*p:.9f} B={o["B"]:.9f} nneg={nneg} '
                  f'foldmode={foldmode:+.6e} minAbsEig={abs(soft):.6e} amp={amp:.7e} '
                  f'grad={o["grad"]:.2e} augRes={res:.2e} success={sol.success}')
            rows.append((p,o['B'],nneg,foldmode,amp,res))
            if (not sol.success) or res>2e-6 or o['grad']>2e-6:
                print('CORRECTOR_STOP'); break
            z0,z1=z1,z2; prev_p=p
            # Once clearly on the two-negative return branch for several steps,
            # topology has been established.
            if found_two and turned and j>8 and sum(1 for q in rows[-4:] if q[2]>=2)>=3:
                break
        imax=int(np.argmax([q[0] for q in rows])) if rows else -1
        if rows:
            q=rows[imax]
            msg=(f'delta={d:.3f}: p_turn~{q[0]:.9f} r_turn~{rx*q[0]:.9f} '
                 f'B_turn~{q[1]:.9f} nneg_at_nearest={q[2]} foldmode={q[3]:+.3e} '
                 f'min_abs_foldmode_seen={minabs:.3e} turned={turned} two_negative_branch={found_two}')
        else: raise RuntimeError('no pseudo-arclength points')
        print(msg); print(f'::notice title=Experiment 03 periodic fold topology::{msg}')
        if not turned: raise RuntimeError('pseudo-arclength did not pass a turning point in r')
        if not found_two: raise RuntimeError('companion two-negative periodic branch not recovered')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot

if __name__=='__main__': main()
