#!/usr/bin/env python3
"""Test uniform quantum-to-thermal rate matching at the finite-T crossover.

For the same positive-real two-pole environment, the classical memory-friction
escape rate is the generalized Kramers/Grote-Hynes expression

    Gamma_th = (omega_m/2pi) (lambda_b/omega_b) exp(-B_sph),

where lambda_b is the positive real unstable growth rate satisfying

    C lambda_b^2 + lambda_b Y_L(lambda_b) + F_s/L = 0.

At the second-order Euclidean crossover the n=1 sphaleron eigenvalue vanishes,
so lambda_b = 2*pi*k_B*T_x/hbar.  The quartic O(2) soft-mode correction to the
low-T periodic-instanton rate is

    U = 0.5 * [1 + erf(sqrt(B_sph-B_per))].

This script approaches r_x=Tx_base/T0 from below and tests whether

    U * Gamma_periodic -> Gamma_th(r_x).

Agreement would provide an internal normalization check linking the calibrated
periodic-instanton prefactor to the classical memory-friction limit.  It does
not by itself prove the entire crossover scaling function away from the local
quartic regime.
"""
from __future__ import annotations

import argparse, math
from scipy.optimize import brentq

import full_dynamic_rfsquid as fd
import finiteT_nonlocal_periodic_bounce_v2 as ft2
import finiteT_one_loop_rate_manifold as rm
from R80_dissipative_bounce_screen import Y_laplace

C0=215e-15; R0=80.; L0=111.5e-12
FRACS=(.94,.97,.985,.992,.996)


def thermal_state(delta,r):
    C=C0*r*r; R=R0/r
    st=ft2.static_model(delta,C,R)
    wb=math.sqrt(-st['Fs']/(L0*C))
    wm=st['wc']
    def f(z):
        return C*z*z + z*float(Y_laplace(z,R,st['wd'])) + st['Fs']/L0
    # f(0)<0 and inertia dominates at high z.
    hi=max(10*wb,10*wm,1e9)
    while f(hi)<=0: hi*=2
    lb=brentq(f,0.0,hi,xtol=1e-4,rtol=1e-12,maxiter=300)
    A=wm/(2*math.pi)*(lb/wb)
    Bs=st['barrierK']/fd.T0
    G=A*math.exp(-Bs)
    return st,lb,wb,A,Bs,G


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--delta',type=float,required=True); a=ap.parse_args()
    d=round(a.delta,3)
    if d not in (.212,.213,.214,.215): raise SystemExit('supported: .212-.215')
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    try:
        base=ft2.static_model(d,C0,R0); Txbase,_=ft2.exact_crossover(base)
        rx=Txbase/fd.T0
        stx,lb,wb,Ath,Bs,Gth=thermal_state(d,rx)
        nu1=2*math.pi*fd.KB*fd.T0/fd.HBAR if hasattr(fd,'KB') else None
        # Constants live in ft2 import module; use exact crossover identity via Tx.
        Txx,_=ft2.exact_crossover(stx)
        print(f'delta={d:.3f} r_x={rx:.10f} Tx_at_rx={Txx:.10f}K '
              f'fc={stx["wc"]/(2*math.pi)*1e-9:.6f}GHz wb={wb/(2*math.pi)*1e-9:.6f}GHz '
              f'lambda_b={lb:.9e}/s Bsph={Bs:.9f} Ath={Ath:.9e}/s Gamma_th={Gth:.9e}/s')
        rows=[]
        for q in FRACS:
            r=q*rx
            s=rm.rate_state(d,r,48,6144)
            if s['kind']!='periodic': raise RuntimeError('expected periodic state below crossover')
            dB=Bs-s['B']
            if dB<=0: raise RuntimeError('periodic action not below sphaleron')
            U=.5*(1+math.erf(math.sqrt(dB)))
            Gu=U*s['Gamma']
            ratio=Gu/Gth
            rows.append((q,dB,U,s['Gamma'],Gu,ratio))
            print(f'r/rx={q:.6f} dB={dB:.9e} U={U:.9f} '
                  f'Gamma_gauss={s["Gamma"]:.9e}/s Gamma_uniform={Gu:.9e}/s '
                  f'Uniform/Thermal={ratio:.9f}')
        # The closest point should be moving toward the thermal limit.  Keep a
        # moderate tolerance because omitted sixth-order center-manifold terms
        # and finite distance from r_x remain at q=.996.
        err=abs(rows[-1][-1]-1)
        trend=abs(rows[-1][-1]-1) <= abs(rows[-2][-1]-1)+.03
        msg=(f'delta={d:.3f}: closest_uniform_over_thermal={rows[-1][-1]:.8f} '
             f'closest_rel_err={err:.3e} convergence_trend={trend}')
        print(msg); print(f'::notice title=Experiment 03 crossover rate matching::{msg}')
        if not trend: raise RuntimeError('uniformized low-T rate is not approaching thermal limit')
        if err>.20: raise RuntimeError('uniformized low-T and thermal rates disagree by >20% near crossover')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot

if __name__=='__main__': main()
