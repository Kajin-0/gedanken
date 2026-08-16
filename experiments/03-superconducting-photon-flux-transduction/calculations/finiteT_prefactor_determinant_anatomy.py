#!/usr/bin/env python3
"""Fluctuation-determinant anatomy of the finite-T nonlocal periodic instanton.

This is the first prefactor gate beyond the converged exponent.  It constructs
the *full* real fluctuation Hessian around the even periodic saddle:

  - even sector: constant + cosine Matsubara modes;
  - odd sector: sine Matsubara modes;
  - one negative even mode;
  - one translation zero mode in the odd sector.

All Hessians are transformed to an orthonormal basis under int ds, avoiding the
basis-normalization ambiguity of raw cosine coefficients.

The metastable-well determinant is diagonal in Matsubara index.  Define

    D = sqrt(det H_well / |det' H_bounce|),

where det' removes the odd translation zero mode and the absolute value retains
the magnitude of the single negative mode.

A *candidate* one-loop rate scale is also reported,

    A_cand = omega_c * sqrt(Ak * I_s / (2*pi)) * D,

with

    Ak = C Phi_bar^2 omega_c / hbar,
    I_s = int (dx_b/ds)^2 ds.

This follows the standard collective-coordinate structure, but is NOT YET
promoted to a physical prefactor.  It still requires independent normalization
against a known local metastable problem / primary finite-T dissipative rate
formula, especially near the crossover where a soft mode requires uniform
handling.

The immediate goals are:
  1. verify one negative even mode and one odd translation zero mode;
  2. verify the zero eigenvector overlaps x_b'(s);
  3. determine UV/basis convergence of log D;
  4. bound how many logarithmic action units the prefactor could shift the
     provisional B=37.61 target.
"""
from __future__ import annotations

import argparse, math
import numpy as np

import full_dynamic_rfsquid as fd
import finiteT_nonlocal_periodic_bounce as ft
import finiteT_nonlocal_periodic_bounce_v2 as ft2
from quantum_initial_capture import PHI_BAR, HBAR

R20={.180:5.06585901,.200:7.19167228,.210:9.23549568}
C0=215e-15; R0=80.0
RES=((24,3072),(32,4096),(40,5120),(48,6144),(64,8192))


def orthonormal_hessians(st,sys,o):
    a=o['a']; B=sys['B']; s=sys['s']; ds=sys['ds']; P=sys['P']; k=sys['k']
    norms=sys['norms']; nb=len(a)-1
    x=st['xm']+B@a
    W=st['dFv'](x)

    # Even raw coefficient Hessian is already available analytically.
    He_raw=sys['jac'](a)
    de=1.0/np.sqrt(norms)
    He=(de[:,None]*He_raw)*de[None,:]

    # Odd sine sector n=1..N.  Kinetic/environment diagonal is the same raw
    # coefficient diagonal as for cosine modes n>=1.
    S=np.sin(np.outer(s,k[1:]))
    no=np.full(nb,P/2.0)
    Ho_raw=np.diag((sys['Kkin']+sys['Kenv'])[1:]) + sys['Av']*(S.T@(W[:,None]*S))*ds
    do=1.0/np.sqrt(no)
    Ho=(do[:,None]*Ho_raw)*do[None,:]

    # Harmonic metastable-well operator in the same orthonormal basis.
    # For normalized basis functions, potential curvature contributes Av*km.
    lam_e=(sys['Kkin']+sys['Kenv'])/norms + sys['Av']*st['km']
    lam_o=(sys['Kkin']+sys['Kenv'])[1:]/no + sys['Av']*st['km']

    ee,Ve=np.linalg.eigh(He)
    eo,Vo=np.linalg.eigh(Ho)

    # Translation zero mode: derivative of even saddle, expanded in normalized
    # sine basis.  x'(s)=-sum_n a_n k_n sin(k_n s).
    zcoef=-a[1:]*k[1:]*np.sqrt(no)
    znorm=float(np.linalg.norm(zcoef))
    iz=int(np.argmin(np.abs(eo)))
    overlap=abs(float(np.dot(Vo[:,iz],zcoef/znorm))) if znorm>0 else float('nan')
    Is=float(np.sum((a[1:]*k[1:])**2*no))

    if np.sum(ee<0)!=1:
        raise RuntimeError(f'even sector expected one negative mode, got {np.sum(ee<0)}')
    # The odd sector may report the zero eigenvalue with either tiny sign.
    eo_nz=np.delete(eo,iz)
    if np.any(eo_nz<=0):
        raise RuntimeError('odd sector has nonpositive mode besides translation zero mode')
    if np.any(lam_e<=0) or np.any(lam_o<=0):
        raise RuntimeError('metastable-well Hessian is not positive')

    logdet_w=float(np.sum(np.log(lam_e))+np.sum(np.log(lam_o)))
    logdet_b=float(np.sum(np.log(np.abs(ee)))+np.sum(np.log(eo_nz)))
    logD=.5*(logdet_w-logdet_b)
    D=math.exp(logD) if logD<700 else float('inf')

    Ak=st['C']*PHI_BAR**2*st['wc']/HBAR
    J=math.sqrt(Ak*Is/(2*math.pi))
    Acand=st['wc']*J*D
    return dict(logD=logD,D=D,Acand=Acand,J=J,Is=Is,
                neg=float(ee[0]),oddzero=float(eo[iz]),zero_overlap=overlap,
                even_gap=float(ee[1]),odd_gap=float(np.min(eo_nz)))


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--delta',type=float,required=True); a=ap.parse_args()
    d=round(a.delta,3)
    if d not in R20: raise SystemExit(f'unsupported delta {d}')
    r=R20[d]; C=C0*r*r; R=R0/r
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    try:
        rows=[]
        for nb,ng in RES:
            st=ft2.static_model(d,C,R)
            Tx,_=ft2.exact_crossover(st)
            out=ft.finiteT_bounce(st,fd.T0,Tx,nb,ng)
            if out['kind']!='periodic':
                raise RuntimeError('determinant anatomy intended for periodic saddle below crossover')
            q=orthonormal_hessians(st,out['sys'],out['o'])
            rows.append(q)
            msg=(f'delta={d:.3f} N={nb} grid={ng}: B={out["o"]["B"]:.9f} '
                 f'logD={q["logD"]:+.9f} D={q["D"]:.6g} J={q["J"]:.6g} '
                 f'Acand={q["Acand"]:.6e}/s Acand/fc={q["Acand"]/(st["wc"]/(2*math.pi)):.6g}; '
                 f'lambda_neg={q["neg"]:+.3e} lambda_zero={q["oddzero"]:+.3e} '
                 f'zero_overlap={q["zero_overlap"]:.9f} even_gap={q["even_gap"]:.3e} odd_gap={q["odd_gap"]:.3e}')
            print(msg); print(f'::notice title=Experiment 03 finiteT determinant anatomy::{msg}')
            if q['zero_overlap']<.995:
                raise RuntimeError('odd zero mode does not match translated bounce derivative')
        ref=rows[-1]['logD']
        print('logD_relative_to_64: '+', '.join(f'{nb}:{q["logD"]-ref:+.3e}' for (nb,ng),q in zip(RES,rows)))
        if abs(rows[-2]['logD']-ref)>2e-3:
            raise RuntimeError('48->64 log determinant ratio not converged to 2e-3')
        print('IMPORTANT: Acand is a normalization hypothesis pending local-problem calibration; logD convergence is the accepted result.')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot

if __name__=='__main__': main()
