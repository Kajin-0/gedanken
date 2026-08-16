#!/usr/bin/env python3
"""Gate the delta=.214 dark target on the dominant large periodic branch.

Branch-topology calculations established that the local first-Matsubara
sphaleron instability is not the physical crossover. A distinct finite-amplitude,
one-negative periodic bounce remains regular through that local boundary and
crosses the sphaleron in action only at r_c/r_x ~= 1.023623633; its later fold is
at r_f ~= 12.0069623.

This regression asks a narrower and safer question than "find a formal root":

    Does the regular, one-negative, dominant periodic contribution reach
    Gamma_per = 1e-6/s before the first-order action crossing?

If a direct crossing exists, it is reported. Otherwise the code resolves the
interior minimum of Gamma_per on the regular pre-crossover branch with a bounded
scalar minimization, re-evaluates that minimum at high basis/grid resolution,
and reports NO_SAFE_ROOT_BEFORE_ACTION_CROSSOVER when the verified minimum still
exceeds the target.

This avoids an invalid monotonicity assumption: the determinant softens near the
first-order region, so Gamma_per can decrease and then turn upward before r_c.
We deliberately do not naively add separate sphaleron and periodic Gaussian rates
through the first-order crossover.
"""
from __future__ import annotations
import math
import numpy as np
from scipy.optimize import brentq, minimize_scalar

import full_dynamic_rfsquid as fd
import finiteT_nonlocal_periodic_bounce as ft
import finiteT_nonlocal_periodic_bounce_v2 as ft2
import finiteT_prefactor_determinant_anatomy as da
import finiteT_determinant_uv_tail as uv

C0=215e-15; R0=80.0; D=.214; TARGET=1e-6; LOGT=math.log(TARGET)
ACTION_RATIO=1.023623633
SAFE_ACTION_FRAC=.998


def large_saddle(st,Tx,Ttarget,nbasis=48,ngrid=6144):
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


def report(prefix,s,rlocal,raction):
    return (f'{prefix} r={s["r"]:.9f} Gamma={s["Gamma"]:.6e}/s B={s["B"]:.8f} '
            f'A1={s["A"]:.6e}/s T0/Tlocal={fd.T0/s["Tx"]:.8f} amp={s["amp"]:.7f} '
            f'nneg={s["nneg"]} zero={s["zero"]:.9f} '
            f'r/r_local={s["r"]/rlocal:.9f} r/r_action={s["r"]/raction:.9f}')


def main():
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    try:
        stbase=ft2.static_model(D,C0,R0); Tx0,_=ft2.exact_crossover(stbase)
        rlocal=Tx0/fd.T0
        raction=rlocal*ACTION_RATIO
        rsafe=raction*SAFE_ACTION_FRAC
        print(f'delta=.214 r_local={rlocal:.9f} r_action_cross_est={raction:.9f} r_safe_edge={rsafe:.9f}')

        grid=np.linspace(11.45,rsafe,13)
        rows=[]
        for r in grid:
            s=state(float(r),40,5120); rows.append(s)
            print(report('scan',s,rlocal,raction))

        bracket=None
        for a,b in zip(rows[:-1],rows[1:]):
            if (a['logGamma']-LOGT)*(b['logGamma']-LOGT)<=0:
                bracket=(a['r'],b['r']); break

        if bracket is not None:
            cache={}
            def f(r):
                k=round(float(r),9)
                if k not in cache: cache[k]=state(float(r),40,5120)
                return cache[k]['logGamma']-LOGT
            rr=brentq(f,*bracket,xtol=2e-5,rtol=1e-6,maxiter=40)
            sf=state(rr,80,10240)
            C=C0*rr*rr; R=R0/rr
            msg=(f'delta=.214 SAFE_GAUSSIAN_ROOT r_rate_large={rr:.9f} C={C*1e15:.3f}fF R={R:.6f}ohm '
                 f'fc={sf["st"]["wc"]/(2*math.pi)*1e-9:.6f}GHz B20={sf["B"]:.9f} '
                 f'A1={sf["A"]:.6e}/s Gamma1={sf["Gamma"]:.6e}/s '
                 f'T0/Tlocal={fd.T0/sf["Tx"]:.9f} amp={sf["amp"]:.8f} '
                 f'nneg={sf["nneg"]} zeroOverlap={sf["zero"]:.9f} '
                 f'r/r_local={rr/rlocal:.9f} r/r_action={rr/raction:.9f}')
            print(msg); print(f'::notice title=Experiment 03 delta .214 safe Gaussian root::{msg}')
            if sf['nneg']!=1 or sf['zero']<.999 or abs(math.log(sf['Gamma']/TARGET))>.04:
                raise RuntimeError('final large-branch root regression failed')
            print('PASS')
            return

        vals=np.array([s['Gamma'] for s in rows])
        j=int(np.argmin(vals))
        # Bracket the observed interior minimum using adjacent coarse points. The
        # endpoint case is retained defensively but is not expected for this branch.
        if 0 < j < len(rows)-1:
            lo,hi=rows[j-1]['r'],rows[j+1]['r']
        elif j==0:
            lo,hi=rows[0]['r'],rows[1]['r']
        else:
            lo,hi=rows[-2]['r'],rows[-1]['r']

        cache_min={}
        def objective(r):
            k=round(float(r),8)
            if k not in cache_min:
                cache_min[k]=state(float(r),40,5120)
            return cache_min[k]['logGamma']

        opt=minimize_scalar(objective,bounds=(lo,hi),method='bounded',
                            options={'xatol':2e-4,'maxiter':24})
        if not opt.success:
            raise RuntimeError(f'bounded rate-minimum solve failed: {opt.message}')
        rmin=float(opt.x)
        smin=state(rmin,80,10240)
        ssafe=state(rsafe,80,10240)

        msg=(f'delta=.214 NO_SAFE_ROOT_BEFORE_ACTION_CROSSOVER '
             f'r_min={rmin:.9f} Gamma_min={smin["Gamma"]:.6e}/s Bmin={smin["B"]:.9f} '
             f'A1min={smin["A"]:.6e}/s amp_min={smin["amp"]:.8f} '
             f'nneg_min={smin["nneg"]} zero_min={smin["zero"]:.9f} '
             f'r_min/r_action={rmin/raction:.9f} '
             f'r_safe={rsafe:.9f} Gamma_safe={ssafe["Gamma"]:.6e}/s '
             f'scan_min_Gamma={float(np.min(vals)):.6e}/s target_margin={smin["Gamma"]/TARGET:.6f}x')
        print(msg); print(f'::notice title=Experiment 03 delta .214 safe-side gate::{msg}')

        for tag,s in [('min',smin),('safe-edge',ssafe)]:
            if s['nneg']!=1 or s['zero']<.999:
                raise RuntimeError(f'{tag} branch anatomy regression failed')
        if smin['Gamma']<=TARGET or ssafe['Gamma']<=TARGET or np.min(vals)<=TARGET:
            raise RuntimeError('target crossing exists but direct bracket detection failed')
        if not (lo <= rmin <= hi):
            raise RuntimeError('rate-minimum solve left its coarse bracket')
        print('PASS: verified interior Gamma_per minimum remains above target before first-order action crossover.')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot

if __name__=='__main__': main()
