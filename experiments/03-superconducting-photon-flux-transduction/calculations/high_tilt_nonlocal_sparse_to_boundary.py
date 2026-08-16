#!/usr/bin/env python3
"""Sparse exact same-environment nonlocal bounce continuation toward cold fold.

Static topology remains bistable through delta=.260 and fails by .270.  This
workflow supplies zero-T actions at sparse higher tilts so the constant-action
capture optimization can jump efficiently if the .12-.14 frontier is still
improving.
"""
from __future__ import annotations
import math
import full_dynamic_rfsquid as fd
from tilt_nonlocal_continuation import setup, solve_tilt

TILTS=(.050,.10,.14,.15,.16,.18,.20,.22,.24,.25,.26)

def main():
    print('Experiment 03 sparse nonlocal continuation toward cold tilt boundary')
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    try:
        geom=setup(); ai=geom[-1].copy(); ae=geom[-1].copy()
        for tilt in TILTS:
            try:
                model,wc,ai,oi,ae,oe=solve_tilt(tilt,ai,ae,geom)
                Bi,si,gi,xi,evi=oi; Be,se,ge,xe,eve=oe
                fold=model.fold_temperature(hi=.95)
                msg=(f'tilt={tilt:.3f}: fold={fold:.6f}K fc={wc/(2*math.pi)*1e-9:.5f}GHz '
                     f'Biso={Bi:.8f} Benv={Be:.8f} r37={37.61/Be:.8f} '
                     f'nneg_iso={int((evi<0).sum())} nneg_env={int((eve<0).sum())} '
                     f'grad_env={ge:.2e} xc={xe:+.6f}')
                print(msg); print(f'::notice title=Experiment 03 sparse high-tilt bounce::{msg}')
                if int((evi<0).sum())!=1 or int((eve<0).sum())!=1:
                    raise RuntimeError('wrong negative mode count')
            except Exception as exc:
                print(f'tilt={tilt:.3f}: STOP/FAIL {type(exc).__name__}: {exc}')
                print(f'::warning title=Experiment 03 sparse bounce boundary::tilt={tilt:.3f} failed: {exc}')
                break
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot

if __name__=='__main__': main()
