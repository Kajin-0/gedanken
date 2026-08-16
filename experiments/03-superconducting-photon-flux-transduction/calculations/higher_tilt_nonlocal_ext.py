#!/usr/bin/env python3
"""Extend same-environment nonlocal bounce continuation to delta=.085.

This supplies exact dark-action values for deciding whether the equal-action
higher-tilt capture frontier should be extended beyond delta=.070.
"""
from __future__ import annotations
import math
import full_dynamic_rfsquid as fd
from tilt_nonlocal_continuation import setup, solve_tilt


def main():
    print('Experiment 03 higher-tilt nonlocal continuation extension')
    ob, ot = fd.BETA_COLD, fd.DELTA_TILT
    try:
        geom = setup()
        ai = geom[-1].copy()
        ae = geom[-1].copy()
        for tilt in (.050,.055,.060,.065,.070,.075,.080,.085):
            model, wc, ai, oi, ae, oe = solve_tilt(tilt, ai, ae, geom)
            Bi, si, gi, xi, evi = oi
            Be, se, ge, xe, eve = oe
            msg = (f'tilt={tilt:.3f}: fold={model.fold_temperature(hi=.95):.6f}K '
                   f'fc={wc/(2*math.pi)*1e-9:.5f}GHz Biso={Bi:.7f} Benv={Be:.7f} '
                   f'DeltaBenv={Be-Bi:.7f}; iso(success={si},grad={gi:.2e},nneg={int((evi<0).sum())}); '
                   f'env(success={se},grad={ge:.2e},nneg={int((eve<0).sum())},xc={xe:+.6f})')
            print(msg)
            print(f'::notice title=Experiment 03 higher-tilt bounce::{msg}')
            if int((evi < 0).sum()) != 1 or int((eve < 0).sum()) != 1:
                raise RuntimeError('wrong negative mode count')
        print('PASS')
    finally:
        fd.BETA_COLD = ob
        fd.DELTA_TILT = ot


if __name__ == '__main__':
    main()
