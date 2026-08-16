#!/usr/bin/env python3
"""Validate the quartic O(2) soft-mode normal form near the finite-T crossover.

At the sphaleron the first nonzero Matsubara mode is a degenerate cosine/sine
pair.  Time-translation invariance therefore makes the leading center-manifold
normal form radial in the pair amplitude q^2=a^2+b^2:

    B = B_sph + (lambda/2) q^2 + (g/4) q^4 + ...

For lambda<0 the periodic-instanton ring has

    q0^2 = -lambda/g,
    B_sph - B_per = lambda^2/(4g).

The exact two-dimensional quartic soft integral is

    I = pi^(3/2)/sqrt(g) * exp(lambda^2/(4g))
        * erfc(lambda/(2*sqrt(g))).

Relative to the ordinary low-T periodic-saddle approximation this gives

    U = 0.5 * erfc(lambda/(2*sqrt(g)))
      = 0.5 * [1 + erf(sqrt(B_sph-B_per))]

for lambda<0.  U -> 1 deep below crossover and U -> 1/2 at the bifurcation.

This script does NOT yet promote U to a final physical rate correction.  It
checks whether the actual nonlocal two-pole periodic saddles enter the expected
quartic second-order normal form by testing:
  * g_eff convergence as T -> Tx^-;
  * q1 / sqrt(-lambda/g_eff) -> 1;
  * equivalence of the two expressions for U.
"""
from __future__ import annotations

import argparse, math

import full_dynamic_rfsquid as fd
import finiteT_nonlocal_periodic_bounce as ft
import finiteT_nonlocal_periodic_bounce_v2 as ft2

R_DESIGN={
    .212:10.62175909,
    .213:11.19986413,
}
C0=215e-15; R0=80.0
FRACS=(.90,.94,.96,.975,.985,.992,.996)


def row(st,Tx,T,nb=40,ng=5120):
    out=ft.finiteT_bounce(st,T,Tx,nb,ng)
    if out['kind']!='periodic': raise RuntimeError('expected periodic branch below Tx')
    sys=out['sys']; o=out['o']
    Bs=st['barrierK']/T; Bp=float(o['B']); dB=Bs-Bp
    if dB<=0: raise RuntimeError('periodic action must be below sphaleron')
    # Exact n=1 cosine/sine sphaleron eigenvalue in the orthonormal basis.
    lam=(sys['Kkin'][1]+sys['Kenv'][1])/sys['norms'][1] + sys['Av']*st['Fs']
    if lam>=0: raise RuntimeError('soft sphaleron mode should be negative below Tx')
    g=lam*lam/(4*dB)
    q1=abs(float(o['a'][1]))*math.sqrt(sys['norms'][1])
    qpred=math.sqrt(-lam/g)
    x=lam/(2*math.sqrt(g))
    U1=.5*math.erfc(x)
    U2=.5*(1+math.erf(math.sqrt(dB)))
    return dict(T=T,frac=T/Tx,Bs=Bs,Bp=Bp,dB=dB,lam=lam,g=g,q1=q1,qpred=qpred,
                qratio=q1/qpred,U1=U1,U2=U2)


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--delta',type=float,required=True); a=ap.parse_args()
    d=round(a.delta,3)
    if d not in R_DESIGN: raise SystemExit('supported: .212 .213')
    r=R_DESIGN[d]; C=C0*r*r; R=R0/r
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    try:
        st=ft2.static_model(d,C,R); Tx,_=ft2.exact_crossover(st)
        print(f'delta={d:.3f} r={r:.9f} Tx={Tx:.9f}K')
        rows=[]
        for f in FRACS:
            z=row(st,Tx,f*Tx)
            rows.append(z)
            print(f'T/Tx={z["frac"]:.6f} dB={z["dB"]:.9e} lambda={z["lam"]:+.9e} '
                  f'g_eff={z["g"]:.9e} q1={z["q1"]:.9e} qpred={z["qpred"]:.9e} '
                  f'qratio={z["qratio"]:.7f} U={z["U1"]:.9f} U_alt={z["U2"]:.9f}')
        # The last three points are the actual near-bifurcation test.  We do not
        # demand exact constancy because higher center-manifold terms enter away
        # from Tx, but g and qratio must visibly approach finite limits.
        tail=rows[-3:]
        gspread=max(z['g'] for z in tail)/min(z['g'] for z in tail)-1
        qerr=max(abs(z['qratio']-1) for z in tail)
        uerr=max(abs(z['U1']-z['U2']) for z in rows)
        msg=(f'delta={d:.3f}: nearTx_gspread={gspread:.3e} nearTx_max_qratio_err={qerr:.3e} '
             f'max_U_identity_err={uerr:.3e} U_at_0.996Tx={rows[-1]["U1"]:.9f}')
        print(msg); print(f'::notice title=Experiment 03 soft-mode Landau validation::{msg}')
        if uerr>2e-10: raise RuntimeError('uniform correction identity failed')
        if qerr>.12: raise RuntimeError('n=1 periodic amplitude has not approached quartic normal form')
        if gspread>.20: raise RuntimeError('effective quartic coefficient not converging near Tx')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot

if __name__=='__main__': main()
