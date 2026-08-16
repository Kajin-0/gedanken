#!/usr/bin/env python3
"""Continue the exact same-environment nonlocal bounce beyond delta=.085.

Purpose: locate the physically admissible high-tilt range and determine the
electrical compensation required to keep B_target=37.61 before spending further
nonlinear capture Monte Carlo.
"""
from __future__ import annotations
import math
import full_dynamic_rfsquid as fd
from tilt_nonlocal_continuation import setup, solve_tilt

TILTS=(.050,.060,.070,.080,.085,.090,.095,.100,.110,.120,.130,.140)

def main():
    print('Experiment 03 higher-tilt nonlocal continuation extension 2')
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    try:
        geom=setup(); ai=geom[-1].copy(); ae=geom[-1].copy()
        for tilt in TILTS:
            try:
                model,wc,ai,oi,ae,oe=solve_tilt(tilt,ai,ae,geom)
                Bi,si,gi,xi,evi=oi; Be,se,ge,xe,eve=oe
                fold=model.fold_temperature(hi=.95)
                msg=(f'tilt={tilt:.3f}: fold={fold:.6f}K fc={wc/(2*math.pi)*1e-9:.5f}GHz '
                     f'Biso={Bi:.7f} Benv={Be:.7f} DeltaBenv={Be-Bi:.7f} '
                     f'r37={37.61/Be:.7f}; iso(success={si},grad={gi:.2e},nneg={int((evi<0).sum())}); '
                     f'env(success={se},grad={ge:.2e},nneg={int((eve<0).sum())},xc={xe:+.6f})')
                print(msg); print(f'::notice title=Experiment 03 higher-tilt bounce 2::{msg}')
                if int((evi<0).sum())!=1 or int((eve<0).sum())!=1:
                    raise RuntimeError('wrong negative mode count')
            except Exception as exc:
                print(f'tilt={tilt:.3f}: STOP/FAIL {type(exc).__name__}: {exc}')
                print(f'::warning title=Experiment 03 higher-tilt boundary::tilt={tilt:.3f} failed: {exc}')
                break
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot

if __name__=='__main__': main()
