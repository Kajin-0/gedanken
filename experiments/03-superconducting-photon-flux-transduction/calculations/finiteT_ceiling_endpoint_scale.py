#!/usr/bin/env python3
"""Electrical endpoint at the exact 20-mK action-ceiling tilt.

At delta_ceiling the static sphaleron action equals B_target=37.61.  The minimum
electrical scale that reaches this target is the exact quantum/thermal crossover
scale

    r_x = T_x,base / T0,

because for r<r_x the physical periodic instanton lies below the sphaleron action,
while for r>=r_x the physical escape saddle is the static sphaleron itself.

This script computes r_x and the associated C,R,fc using the same exact two-pole
Matsubara kernel and actual saddle curvature.
"""
from __future__ import annotations
import math
import full_dynamic_rfsquid as fd
import finiteT_nonlocal_periodic_bounce_v2 as ft2

DELTA=0.2150240395
C0=215e-15; R0=80.; BT=37.61


def main():
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    try:
        st0=ft2.static_model(DELTA,C0,R0)
        Tx0,_=ft2.exact_crossover(st0)
        rx=Tx0/fd.T0
        C=C0*rx*rx; R=R0/rx
        stx=ft2.static_model(DELTA,C,R)
        Txx,_=ft2.exact_crossover(stx)
        Bsph=stx['barrierK']/fd.T0
        msg=(f'delta_ceiling={DELTA:.10f}: Tx_base={Tx0:.9f}K r_x={rx:.9f} '
             f'C_x={C*1e15:.3f}fF R_x={R:.6f}ohm '
             f'fc_x={stx["wc"]/(2*math.pi)*1e-9:.6f}GHz Tx_scaled={Txx:.9f}K '
             f'Bsph20={Bsph:.9f} target={BT:.5f}')
        print(msg); print(f'::notice title=Experiment 03 finiteT ceiling endpoint::{msg}')
        if abs(Txx/fd.T0-1)>2e-7 or abs(Bsph/BT-1)>2e-6:
            raise RuntimeError('ceiling endpoint regression failed')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot

if __name__=='__main__': main()
