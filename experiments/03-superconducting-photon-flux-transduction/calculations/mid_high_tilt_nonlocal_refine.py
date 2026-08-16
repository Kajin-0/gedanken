#!/usr/bin/env python3
"""Refine exact same-environment nonlocal action across delta=.18-.22.

The capture frontier is still rising at .18, while the 20-mK finite-temperature
dark diagnostic becomes marginal by .20-.22.  This continuation supplies exact
base actions at .19 and .21 for a joint dark/capture refinement.
"""
from __future__ import annotations
import math
import full_dynamic_rfsquid as fd
from tilt_nonlocal_continuation import setup, solve_tilt

TILTS=(.18,.19,.20,.21,.22)

def main():
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    try:
        geom=setup(); ai=geom[-1].copy(); ae=geom[-1].copy()
        for tilt in TILTS:
            model,wc,ai,oi,ae,oe=solve_tilt(tilt,ai,ae,geom)
            Bi,si,gi,xi,evi=oi; Be,se,ge,xe,eve=oe
            fold=model.fold_temperature(hi=.95)
            msg=(f'tilt={tilt:.3f}: fold={fold:.6f}K fc={wc/(2*math.pi)*1e-9:.5f}GHz '
                 f'Biso={Bi:.8f} Benv={Be:.8f} r37={37.61/Be:.8f} '
                 f'nneg_iso={int((evi<0).sum())} nneg_env={int((eve<0).sum())} grad_env={ge:.2e}')
            print(msg); print(f'::notice title=Experiment 03 mid-high-tilt action::{msg}')
            if int((evi<0).sum())!=1 or int((eve<0).sum())!=1:
                raise RuntimeError('wrong negative mode count')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot

if __name__=='__main__': main()
