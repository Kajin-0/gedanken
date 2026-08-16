#!/usr/bin/env python3
"""Quasi-static external-flux sensitivity of the reduced dark rate.

Generation A obtains directionality from DELTA_TILT in the rf-SQUID force

    F = x - delta - beta * CPR(x,T).

In the standard reduced-flux convention, delta is a phase-like external bias,
so a small physical flux perturbation is

    dPhi/Phi0 = ddelta/(2*pi).

At a fixed fabricated design (fixed C,R), low-frequency flux noise changes the
barrier and therefore the dark rate exponentially.  This script finite-
differences the complete *regular* reduced dark rate

    Gamma = Gamma_per + Gamma_th

with respect to delta at the nominal safe-side designs.  It reports:

* S = d ln Gamma / d delta;
* the flux shift producing an e-fold / factor-two rate change;
* the quasi-static Gaussian rms flux noise that would inflate the mean rate by
  10% under the local log-linear approximation

      <Gamma>/Gamma0 ~= exp(S^2 sigma_delta^2/2).

This is a robustness diagnostic, not a technical-noise model: actual 1/f flux
spectra, observation time and non-Gaussian fluctuators are not supplied.
"""
from __future__ import annotations

import argparse, math

import finiteT_one_loop_rate_manifold as rm
import first_order_total_rate_manifold as fo
import safe_tilt_optimum_worker as sw

KNOWN={
    .21250:10.885578211,
    .21300:11.2051409652,
}
H=1.0e-4


def total(delta,r,nb=56,ng=7168):
    s=rm.rate_state(delta,r,nb,ng)
    if s['kind']!='periodic': raise RuntimeError('sensitivity probe left regular periodic branch')
    th=fo.thermal_rate(s['st'])
    return s['Gamma']+th['Gamma'],s,th


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--delta',type=float,required=True); a=ap.parse_args()
    d=round(a.delta,5)
    if d not in (.21200,.21250,.21300): raise SystemExit('supported: .212,.2125,.213')
    if d==.21200:
        r,_,_,_=sw.solve_root(d)
    else:
        r=KNOWN[d]
    vals=[]
    for off in (-H,0.0,H):
        G,s,th=total(d+off,r)
        vals.append((off,G,s,th))
        print(f'delta={d+off:.6f} fixed_r={r:.10f}: G={G:.9e}/s Gper={s["Gamma"]:.9e}/s '
              f'Gth={th["Gamma"]:.9e}/s Bper={s["B"]:.9f} fc={s["st"]["wc"]/(2*math.pi)*1e-9:.7f}GHz')
    lm,l0,lp=[math.log(z[1]) for z in vals]
    S=(lp-lm)/(2*H)
    K=(lp-2*l0+lm)/(H*H)
    d_e=1/abs(S); d_2=math.log(2)/abs(S)
    sig10=math.sqrt(2*math.log(1.10))/abs(S)
    to_uPhi=lambda dd: dd/(2*math.pi)*1e6
    # Fold sensitivity at the same fixed fabricated C,R is cheap and relevant to
    # signal threshold as well as dark robustness.
    Tm=vals[0][2]['st']
    # static_model does not store photon fold; evaluate with the live force model
    # would require rebuilding CPR.  Keep this workflow dark-rate-specific.
    msg=(f'delta={d:.5f} r={r:.9f}: dlnGamma_ddelta={S:+.6e} curvature={K:+.6e}; '
         f'e-fold_flux={to_uPhi(d_e):.3f}uPhi0 factor2_flux={to_uPhi(d_2):.3f}uPhi0; '
         f'sigma_flux_for_10pct_quasistatic_inflation={to_uPhi(sig10):.3f}uPhi0; '
         f'local_curvature_fraction_over_h={0.5*abs(K)*H/abs(S):.3e}')
    print(msg); print(f'::notice title=Experiment 03 flux-bias dark sensitivity::{msg}')
    if 0.5*abs(K)*H/abs(S)>.10:
        print('WARNING: h=1e-4 finite-difference interval is too curved for simple local log-linear noise estimate')
    print('PASS')

if __name__=='__main__': main()
