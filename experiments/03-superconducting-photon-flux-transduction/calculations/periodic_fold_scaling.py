#!/usr/bin/env python3
"""Test canonical saddle-node scaling of the finite-amplitude periodic-instanton fold.

The coarse pseudo-arclength scan already shows a one-negative periodic decay
saddle colliding with a two-negative companion.  A genuine fold catastrophe
must additionally satisfy, for mu = p_f-p -> 0+,

    Delta B_12  ~ mu^(3/2),
    |lambda_f| ~ mu^(1/2),

where p=r/r_x and lambda_f is the additional even fluctuation eigenvalue.

This script performs a finer pseudo-arclength continuation, transforms the even
Hessian to an orthonormal cosine-coordinate basis, estimates p_f from
p = p_f - c lambda_f^2, interpolates the two branches at matched p, and fits
the two universal exponents.  Passing this test is a prerequisite for using a
fold/Airy uniform approximation for the dark-rate prefactor.
"""
from __future__ import annotations

import argparse, math
import numpy as np

import full_dynamic_rfsquid as fd
import finiteT_nonlocal_periodic_bounce_v2 as ft2
import periodic_fold_pseudo_arclength as pa

C0=215e-15; R0=80.0


def fold_eig_orth(sys,o):
    H=sys['jac'](o['a'])
    d=np.sqrt(np.asarray(sys['norms'],float))
    Ho=H/(d[:,None]*d[None,:])
    ev=np.linalg.eigvalsh(Ho)
    nneg=int(np.sum(ev<0))
    if nneg==1:
        pos=ev[ev>0]
        return float(pos[0]),nneg
    if nneg>=2:
        neg=np.sort(ev[ev<0])
        return float(neg[-1]),nneg
    raise RuntimeError(f'unexpected nneg={nneg}')


def interp_branch(branch,pvals,key):
    arr=sorted(branch,key=lambda z:z['p'])
    pp=np.array([z['p'] for z in arr]); yy=np.array([z[key] for z in arr])
    return np.interp(pvals,pp,yy)


def run(delta):
    nbasis=32; ngrid=4096
    base=ft2.static_model(delta,C0,R0); Tx,_=ft2.exact_crossover(base); rx=Tx/fd.T0
    (p0,s0,o0),(p1,s1,o1)=pa.direct_seed(base,rx,nbasis,ngrid)
    z0=np.r_[o0['a'],p0]; z1=np.r_[o1['a'],p1]
    ds=.22*np.linalg.norm(z1-z0)
    rows=[]; turned=False
    prev_p=p1
    for j in range(120):
        t=pa.normalized_secant(z0,z1); zpred=z1+ds*t
        sol,z2,sys,o,res=pa.correct(base,rx,zpred,t,nbasis,ngrid)
        p=float(z2[-1]); lam,nneg=fold_eig_orth(sys,o)
        amp=float(math.sqrt(np.sum((o['a'][1:]**2)*sys['norms'][1:])))
        rows.append(dict(p=p,B=float(o['B']),lam=lam,nneg=nneg,amp=amp,res=res))
        if p<prev_p-1e-6: turned=True
        if j%4==0 or nneg>=2:
            print(f'j={j:03d} p={p:.10f} r={rx*p:.10f} B={o["B"]:.10f} '
                  f'nneg={nneg} lambda_orth={lam:+.8e} amp={amp:.8e} res={res:.2e}')
        if (not sol.success) or res>8e-7 or o['grad']>8e-7:
            print('CORRECTOR_STOP'); break
        z0,z1=z1,z2; prev_p=p
        if turned and nneg>=2 and len([q for q in rows if q['nneg']>=2])>=24:
            break
    one=[q for q in rows if q['nneg']==1]
    two=[q for q in rows if q['nneg']>=2]
    if len(one)<8 or len(two)<8: raise RuntimeError('insufficient points on both fold branches')

    # Estimate p_f from the universal lambda^2 linear law using only the nearest
    # points to the fold from both sides.  Orthonormalizing the Hessian removes a
    # basis-normalization artifact from this regression.
    near=sorted(rows,key=lambda q:abs(q['lam']))[:14]
    X=np.array([q['lam']**2 for q in near]); Y=np.array([q['p'] for q in near])
    A=np.c_[np.ones_like(X),X]
    coef=np.linalg.lstsq(A,Y,rcond=None)[0]
    pf=float(coef[0]); slope=float(coef[1])
    yhat=A@coef
    r2=1-float(np.sum((Y-yhat)**2))/float(np.sum((Y-Y.mean())**2))
    print(f'fold_fit p_f={pf:.10f} r_f={rx*pf:.10f} slope_p_vs_lam2={slope:+.8e} R2={r2:.8f}')

    pmin=max(min(q['p'] for q in one),min(q['p'] for q in two))
    maxmu=pf-pmin
    # Stay close enough for the normal form but use enough dynamic range for a
    # meaningful exponent fit.  These fractions adapt to both .214 and .215.
    mus=maxmu*np.array([.06,.10,.16,.25,.38,.55,.75])
    pvals=pf-mus
    # Keep only values inside both interpolation domains.
    lo=max(min(q['p'] for q in one),min(q['p'] for q in two))
    hi=min(max(q['p'] for q in one),max(q['p'] for q in two))
    mask=(pvals>lo)&(pvals<hi)
    mus=mus[mask]; pvals=pvals[mask]
    if len(mus)<5: raise RuntimeError('not enough matched-p fold points')

    B1=interp_branch(one,pvals,'B'); B2=interp_branch(two,pvals,'B')
    L1=np.abs(interp_branch(one,pvals,'lam')); L2=np.abs(interp_branch(two,pvals,'lam'))
    dB=np.abs(B2-B1); Lavg=.5*(L1+L2)
    for p,mu,b1,b2,db,l1,l2 in zip(pvals,mus,B1,B2,dB,L1,L2):
        print(f'matched p={p:.10f} mu={mu:.8e} B1={b1:.10f} B2={b2:.10f} '
              f'DeltaB={db:.8e} |lam1|={l1:.8e} |lam2|={l2:.8e}')
    if np.any(dB<=0) or np.any(Lavg<=0): raise RuntimeError('nonpositive fold observables')
    eB=np.polyfit(np.log(mus),np.log(dB),1)[0]
    eL=np.polyfit(np.log(mus),np.log(Lavg),1)[0]
    # Also check that the prefactors are approaching constants after dividing by
    # their expected powers; report spread rather than imposing excessive rigor.
    cB=dB/mus**1.5; cL=Lavg/mus**.5
    spreadB=float(cB.max()/cB.min()-1); spreadL=float(cL.max()/cL.min()-1)
    msg=(f'delta={delta:.3f}: pf={pf:.9f} rf={rx*pf:.9f} lambda2_R2={r2:.6f} '
         f'DeltaB_exponent={eB:.4f} lambda_exponent={eL:.4f} '
         f'cB_spread={spreadB:.3f} cLambda_spread={spreadL:.3f}')
    print(msg); print(f'::notice title=Experiment 03 fold scaling::{msg}')
    if r2<.985: raise RuntimeError('lambda^2 fold-location fit is not linear enough')
    if abs(eB-1.5)>.22: raise RuntimeError('action splitting does not show 3/2 fold scaling')
    if abs(eL-.5)>.16: raise RuntimeError('soft eigenvalue does not show 1/2 fold scaling')
    print('PASS')


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--delta',type=float,required=True); a=ap.parse_args()
    d=round(a.delta,3)
    if d not in (.214,.215): raise SystemExit('supported: .214,.215')
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    try: run(d)
    finally: fd.BETA_COLD=ob; fd.DELTA_TILT=ot

if __name__=='__main__': main()
