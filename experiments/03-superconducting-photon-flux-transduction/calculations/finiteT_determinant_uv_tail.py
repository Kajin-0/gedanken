#!/usr/bin/env python3
"""UV-tail correction for the finite-T periodic-instanton determinant ratio.

The raw determinant anatomy converges as O(1/N) because each omitted high
Matsubara mode contributes O(1/n^2) to log D.  For the full orthonormal
fluctuation operator, the high-n diagonal difference between metastable well
and bounce is controlled by the time-averaged bounce curvature.

For each omitted n, use the exact diagonal reference operator

  lambda_m(n) = Ak*k_n^2
              + (Phi_bar^2/hbar)*k_n*Y_L(omega_c*k_n)
              + Av*kappa_m

and the leading trace correction

  dlogD_n = Av*(kappa_m - <F'(x_b)>)/lambda_m(n).

The factor 1/2 in log D cancels the two equal high-n cosine/sine sectors.
Summing n>N to a large cutoff plus the analytic inertial remainder removes the
leading 1/N UV tail.  Residual N-dependence is then a diagnostic of subleading
off-diagonal/Fourier-curvature effects.

This corrects determinant *convergence only*.  It does not establish the
collective-coordinate/rate normalization of the prefactor.
"""
from __future__ import annotations

import argparse, math
import numpy as np
from scipy.special import polygamma

import full_dynamic_rfsquid as fd
import finiteT_nonlocal_periodic_bounce as ft
import finiteT_nonlocal_periodic_bounce_v2 as ft2
import finiteT_prefactor_determinant_anatomy as da
from R80_dissipative_bounce_screen import Y_laplace
from quantum_initial_capture import PHI_BAR, HBAR

R20={.180:5.06585901,.200:7.19167228,.210:9.23549568}
C0=215e-15; R0=80.0
RES=((24,3072),(32,4096),(40,5120),(48,6144),(64,8192),(80,10240),(96,12288))


def uv_tail(st,sys,o,N,nexact=200000):
    a=o['a']; B=sys['B']; ds=sys['ds']; P=sys['P']
    x=st['xm']+B@a
    W=st['dFv'](x)
    Wbar=float(np.sum(W)*ds/P)
    delta= sys['Av']*(st['km']-Wbar)
    Ak=st['C']*PHI_BAR**2*st['wc']/HBAR

    n=np.arange(N+1,nexact+1,dtype=float)
    k=2*math.pi*n/P
    env=(PHI_BAR**2/HBAR)*k*np.asarray(Y_laplace(st['wc']*k,st['R'],st['wd']),dtype=float)
    lam=Ak*k*k+env+sys['Av']*st['km']
    exact=float(np.sum(delta/lam))

    # Remaining n>nexact: inertial leading term delta/(Ak*(2pi n/P)^2).
    coeff=delta*P*P/(4*math.pi**2*Ak)
    rem=float(coeff*polygamma(1,nexact+1))
    return exact+rem, Wbar, coeff


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
            q=da.orthonormal_hessians(st,out['sys'],out['o'])
            tail,Wbar,coeff=uv_tail(st,out['sys'],out['o'],nb)
            corr=q['logD']+tail
            rows.append((nb,q['logD'],tail,corr,coeff,Wbar))
            msg=(f'delta={d:.3f} N={nb}: B={out["o"]["B"]:.9f} raw_logD={q["logD"]:+.9f} '
                 f'UVtail={tail:+.9f} corr_logD={corr:+.9f} c1overN={coeff:+.7f} '
                 f'Wbar={Wbar:+.7f} km={st["km"]:+.7f} zero_overlap={q["zero_overlap"]:.9f}')
            print(msg); print(f'::notice title=Experiment 03 determinant UV tail::{msg}')
        ref=rows[-1][3]
        print('corrected_relative_to_96: '+', '.join(f'N{nb}:{corr-ref:+.3e}' for nb,raw,tail,corr,c,w in rows))
        # Last two corrected values should be much tighter than raw determinant.
        rawdiff=abs(rows[-2][1]-rows[-1][1])
        corrdiff=abs(rows[-2][3]-rows[-1][3])
        print(f'80to96 raw_diff={rawdiff:.6e} corrected_diff={corrdiff:.6e} improvement={rawdiff/corrdiff if corrdiff else float("inf"):.3g}x')
        if corrdiff>3e-3:
            raise RuntimeError('UV-corrected logD not converged to 3e-3 at N=80->96')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot

if __name__=='__main__': main()
