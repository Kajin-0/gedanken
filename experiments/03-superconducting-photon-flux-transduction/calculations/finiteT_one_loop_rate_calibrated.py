#!/usr/bin/env python3
"""Cubic-calibrated one-loop dark-rate diagnostic for Experiment 03.

The cubic local calibration establishes that a determinant built from Hessians
of the dimensionless action B=S/hbar contains one unmatched factor sqrt(Ak)
after translation-zero-mode removal.  The operator determinant entering the
physical bounce prefactor is therefore

    D_op = D_raw / sqrt(Ak),

with

    Ak = C Phi_bar^2 omega_c / hbar.

The collective-coordinate Jacobian is

    J = sqrt(Ak * I_s / (2*pi)),
    I_s = int (dx_b/ds)^2 ds.

Hence the calibrated one-loop prefactor becomes

    A_1l = omega_c * J * D_op
         = omega_c * sqrt(I_s/(2*pi)) * D_raw.

`D_raw` below includes the validated analytic UV-tail correction from
finiteT_determinant_uv_tail.py.

The corresponding rate diagnostic is

    Gamma_1l = A_1l exp(-B_20mK).

This is still not a final physical DCR because:
  - the soft-mode crossover requires uniform treatment very near Tx;
  - competing dark channels are absent;
  - the target 1e-6/s is provisional.

But the absolute normalization is no longer an arbitrary GHz attempt frequency:
the same procedure reproduces the canonical cubic MQT prefactor in the local
zero-temperature benchmark.
"""
from __future__ import annotations

import argparse, math

import full_dynamic_rfsquid as fd
import finiteT_nonlocal_periodic_bounce as ft
import finiteT_nonlocal_periodic_bounce_v2 as ft2
import finiteT_prefactor_determinant_anatomy as da
import finiteT_determinant_uv_tail as uv

R20={.180:5.06585901,.200:7.19167228,.210:9.23549568}
C0=215e-15; R0=80.0
GAMMA_TARGET=1e-6


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--delta',type=float,required=True); a=ap.parse_args()
    d=round(a.delta,3)
    if d not in R20: raise SystemExit(f'unsupported delta {d}')
    r=R20[d]; C=C0*r*r; R=R0/r
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    try:
        st=ft2.static_model(d,C,R)
        Tx,_=ft2.exact_crossover(st)
        out=ft.finiteT_bounce(st,fd.T0,Tx,96,12288)
        o=out['o']; sys=out['sys']
        q=da.orthonormal_hessians(st,sys,o)
        tail,Wbar,coeff=uv.uv_tail(st,sys,o,96)
        logDraw=q['logD']+tail
        Draw=math.exp(logDraw)
        I=q['Is']
        A1=st['wc']*math.sqrt(I/(2*math.pi))*Draw
        B=float(o['B'])
        logGamma=math.log(A1)-B
        Gamma=math.exp(logGamma)
        Breq=math.log(A1/GAMMA_TARGET)
        dB=Breq-B
        Dop=Draw/math.sqrt(st['C']*da.PHI_BAR**2*st['wc']/da.HBAR)
        msg=(f'delta={d:.3f}: B20={B:.9f} Tx={Tx:.8f}K T0/Tx={fd.T0/Tx:.6f} '
             f'logDraw_corr={logDraw:.9f} Draw={Draw:.6g} D_op={Dop:.6g} '
             f'Is={I:.9f} A1={A1:.6e}/s A1/fc={A1/(st["wc"]/(2*math.pi)):.6g} '
             f'Gamma1={Gamma:.6e}/s log10Gamma={logGamma/math.log(10):+.5f} '
             f'Breq_for_1e-6_if_A_fixed={Breq:.6f} DeltaB={dB:+.6f}')
        print(msg); print(f'::notice title=Experiment 03 calibrated one-loop rate::{msg}')
        if int((o['ev']<0).sum())!=1 or q['zero_overlap']<.999:
            raise RuntimeError('periodic-saddle mode regression failed')
        print('CAUTION: Breq is a fixed-prefactor diagnostic, not yet the self-consistent redesigned exponent.')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot

if __name__=='__main__': main()
