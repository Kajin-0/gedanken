#!/usr/bin/env python3
"""First-orbit uniform crossover probe for Experiment 03.

This is an exploratory derivation test, not yet an accepted physical DCR.

For the harmonic metastable well / dissipative parabolic sphaleron, evaluate

 Gamma_pb = (omega_m/2pi)(lambda_b/omega_b) exp(-B_sph)
            prod_{n>=1} [nu_n^2 + nu_n gammahat(nu_n) + omega_m^2]
                        /[nu_n^2 + nu_n gammahat(nu_n) - omega_b^2].

Below crossover the n=1 denominator is negative, so Gamma_pb is the signed
analytic continuation of the parabolic-barrier term and diverges negatively as
T -> Tx^-.

Test the first-orbit Lawrence/Bleistein uniform combination

 Gamma_u1 = Gamma_pb
          + Gamma_inst exp(-DeltaB)/sqrt(4*pi*DeltaB)
          + Gamma_inst * 0.5*erfc(-sqrt(DeltaB))

with DeltaB=B_sph-B_inst.

The Hamiltonian embedding / Schur-complement argument in
NONLOCAL_TO_HAMILTONIAN_UNIFORMIZATION_PATH_2026-08-16.md motivates this form
for a linear equilibrium bath, but the real-time flux reduction for the
continuum bath is not yet independently proven.  Therefore Gamma_u1 is a
CONJECTURAL DIAGNOSTIC until local/dissipative benchmark regressions are added.
"""
from __future__ import annotations
import argparse, math
import numpy as np
from scipy.optimize import brentq
from scipy.special import erfc, polygamma

import full_dynamic_rfsquid as fd
import finiteT_one_loop_rate_manifold as rm
from R80_dissipative_bounce_screen import Y_laplace
from quantum_initial_capture import HBAR, KB

L0=111.5e-12
RPTS={
    .210:9.825701561,
    .211:10.18791311,
    .212:10.62175909,
    .213:11.19986413,
    .214:11.49729617,
}


def signed_log_product(st,T,N=200000):
    C=st['C']; wc=st['wc']; Fs=st['Fs']; R=st['R']; wd=st['wd']
    wm=wc
    wb=math.sqrt(-Fs/(L0*C))
    n=np.arange(1,N+1,dtype=float)
    nu=2*math.pi*KB*T/HBAR*n
    gh=np.asarray(Y_laplace(nu,R,wd),dtype=float)/C
    num=nu*nu+nu*gh+wm*wm
    den=nu*nu+nu*gh-wb*wb
    if np.any(num<=0): raise RuntimeError('well Matsubara factor nonpositive')
    sign=float(np.prod(np.sign(den)))
    logabs=float(np.sum(np.log(num)-np.log(np.abs(den))))
    # Leading high-n tail is (wm^2+wb^2)/nu_n^2.  Add the exact sum of this
    # leading term from n=N+1..infinity via trigamma.  Residual is O(N^-3).
    nu1=2*math.pi*KB*T/HBAR
    tail=(wm*wm+wb*wb)/(nu1*nu1)*float(polygamma(1,N+1))
    return sign,logabs+tail,wm,wb


def barrier_growth(st):
    C,R,wd,Fs=st['C'],st['R'],st['wd'],st['Fs']
    def f(s): return C*s*s+s*float(Y_laplace(s,R,wd))+Fs/L0
    hi=max(st['wc'],math.sqrt(abs(Fs)/(L0*C)))
    while f(hi)<=0: hi*=2
    return brentq(f,0.0,hi,xtol=1e-8,rtol=2e-13,maxiter=400)


def undamped_product_regression(T,wm,wb,N=200000):
    n=np.arange(1,N+1,dtype=float)
    nu=2*math.pi*KB*T/HBAR*n
    num=nu*nu+wm*wm; den=nu*nu-wb*wb
    s=float(np.prod(np.sign(den)))
    logv=float(np.sum(np.log(num)-np.log(np.abs(den))))
    nu1=2*math.pi*KB*T/HBAR
    logv+=(wm*wm+wb*wb)/(nu1*nu1)*float(polygamma(1,N+1))
    x=HBAR*wm/(2*KB*T); y=HBAR*wb/(2*KB*T)
    exact=(math.sinh(x)/x)*(y/math.sin(y))
    sex=math.copysign(1.0,exact); lex=math.log(abs(exact))
    return s,logv,sex,lex


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--delta',type=float,required=True); a=ap.parse_args()
    d=round(a.delta,3)
    if d not in RPTS: raise SystemExit(f'unsupported delta={d}')
    r=RPTS[d]
    s=rm.rate_state(d,r,64,8192)
    if s['kind']!='periodic': raise RuntimeError('probe requires periodic instanton below crossover')
    st=s['st']; Binst=float(s['B']); Ginst=float(s['Gamma'])
    Bsph=st['barrierK']/fd.T0; gap=Bsph-Binst
    if gap<=0: raise RuntimeError('expected B_sph>B_inst below crossover')
    sign,logP,wm,wb=signed_log_product(st,fd.T0)
    lb=barrier_growth(st)
    logpref=math.log(wm/(2*math.pi))+math.log(lb/wb)
    logabs_pb=logpref-Bsph+logP
    Gpb=sign*math.exp(logabs_pb)
    cancel=Ginst*math.exp(-gap)/math.sqrt(4*math.pi*gap)
    winst=.5*erfc(-math.sqrt(gap))
    Gorb=Ginst*winst
    Gunif=Gpb+cancel+Gorb

    su,lu,se,le=undamped_product_regression(fd.T0,wm,wb)
    reg_sign_ok=(su==se); reg_rel=math.expm1(lu-le)
    msg=(f'delta={d:.3f} r={r:.9f} Binst={Binst:.9f} Bsph={Bsph:.9f} DeltaB={gap:.9f} '
         f'Gamma_inst={Ginst:.6e}/s Gamma_pb={Gpb:+.6e}/s '
         f'cancel={cancel:+.6e}/s orbit_uniform={Gorb:+.6e}/s '
         f'Gamma_uniform1={Gunif:+.6e}/s lambda_b={lb:.6e}/s '
         f'pb_product_sign={sign:+.0f} logabsP={logP:.9f} '
         f'undamped_reg_sign={reg_sign_ok} undamped_log_rel={reg_rel:+.3e}')
    print(msg); print(f'::notice title=Experiment 03 first-orbit uniform probe::{msg}')
    if not reg_sign_ok or abs(reg_rel)>2e-9:
        raise RuntimeError('undamped Matsubara product regression failed')
    print('CAUTION: Gamma_uniform1 is a conjectural first-orbit diagnostic pending continuum-bath flux proof and multi-orbit treatment.')
    print('PASS')

if __name__=='__main__': main()
