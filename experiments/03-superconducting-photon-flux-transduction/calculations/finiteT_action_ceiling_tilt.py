#!/usr/bin/env python3
"""Locate the static finite-temperature action ceiling for Experiment 03.

At bath temperature T0, no electrical mass/damping compensation can make the
escape exponent exceed the static sphaleron action

    B_sph = DeltaU/(k_B*T0).

For a requested target B_target, the high-tilt compensated family is therefore
possible only while B_sph >= B_target.  This script solves the exact cold
potential condition B_sph(delta)=37.61.
"""
from __future__ import annotations
from scipy.optimize import brentq
import full_dynamic_rfsquid as fd
from directional_recovery_barriers import directional_barriers
from quantum_initial_capture import KB, PHI_BAR

BT=37.61


def main():
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    L=fd.CASES[.6][0]; EL=PHI_BAR**2/L
    try:
        fd.BETA_COLD=.80
        def bsph(delta):
            fd.DELTA_TILT=float(delta)
            m=fd.DynamicForce(.6,quick=False,Tmax=.98)
            b=directional_recovery_barriers=directional_barriers(m,fd.T0)
            barrierK=m._scalar(b['b_left'])*EL/KB
            return barrierK/fd.T0,barrierK
        def f(delta): return bsph(delta)[0]-BT
        dc=brentq(f,.21,.22,xtol=2e-12,rtol=2e-12,maxiter=100)
        B,K=bsph(dc)
        for d in (.210,.212,.214,dc,.216,.218,.220):
            b,k=bsph(d)
            print(f'delta={d:.9f}: barrier={k:.9f}K Bsph20mK={b:.8f} margin={b-BT:+.8f}')
        msg=(f'delta_ceiling={dc:.10f} barrier={K:.9f}K '
             f'Bsph={B:.8f} target={BT:.5f}')
        print(msg); print(f'::notice title=Experiment 03 finiteT action ceiling::{msg}')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot

if __name__=='__main__': main()
