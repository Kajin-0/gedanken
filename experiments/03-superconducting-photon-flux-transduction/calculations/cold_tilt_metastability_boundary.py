#!/usr/bin/env python3
"""Locate the cold metastability boundary versus positive directional tilt.

Static topology only: beta_cold=.80, live CPR mix, T=T0.  Scan the directional
barriers and photon-induced fold temperature to identify where the left dark
minimum/saddle cease to exist.  No tunneling or capture probabilities are
computed here.
"""
from __future__ import annotations
import full_dynamic_rfsquid as fd
from directional_recovery_barriers import directional_barriers


def main():
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    try:
        fd.BETA_COLD=.80
        last=None
        for i in range(5,36):
            delta=i/100
            fd.DELTA_TILT=delta
            try:
                model=fd.DynamicForce(.6,quick=False,Tmax=1.02)
                b=directional_barriers(model,fd.T0)
                try: fold=model.fold_temperature(hi=.98)
                except Exception: fold=float('nan')
                msg=(f'delta={delta:.3f}: bistable=YES left={b["left"]:+.6f} '
                     f'saddle={b["saddle"]:+.6f} right={b["right"]:+.6f} '
                     f'b_left_dimless={b["b_left"]:.8f} fold={fold:.6f}K')
                print(msg); print(f'::notice title=Experiment 03 cold tilt topology::{msg}')
                last=delta
            except Exception as exc:
                msg=f'delta={delta:.3f}: bistable=NO/FAIL {type(exc).__name__}: {exc}'
                print(msg); print(f'::warning title=Experiment 03 cold tilt boundary::{msg}')
                if last is not None:
                    print(f'last_coarse_bistable_delta={last:.3f}')
                break
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot

if __name__=='__main__': main()
