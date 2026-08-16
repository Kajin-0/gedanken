#!/usr/bin/env python3
"""Continue the full same-environment nonlocal bounce to higher directional tilt.

This reuses the validated spectral continuation machinery from
`tilt_nonlocal_continuation.py`, but moves from the live delta=.050 point toward
stronger directionality. It is preparatory for a possible strategy:

    higher tilt -> lower thermal fold / stronger directional capture
    electrical similarity -> restore the lost dark action.

No cubic MQT approximation is used.
"""
from __future__ import annotations
import math
import full_dynamic_rfsquid as fd
from tilt_nonlocal_continuation import setup, solve_tilt


def main():
    print('Experiment 03 high-tilt same-environment nonlocal continuation')
    ob, ot = fd.BETA_COLD, fd.DELTA_TILT
    try:
        geom = setup()
        ai = geom[-1].copy()
        ae = geom[-1].copy()
        for tilt in (.050, .055, .060, .065, .070):
            model, wc, ai, oi, ae, oe = solve_tilt(tilt, ai, ae, geom)
            Bi, si, gi, xi, evi = oi
            Be, se, ge, xe, eve = oe
            msg = (f'tilt={tilt:.3f}: fold={model.fold_temperature(hi=.95):.6f}K '
                   f'fc={wc/(2*math.pi)*1e-9:.5f}GHz Biso={Bi:.7f} '
                   f'Benv={Be:.7f} DeltaBenv={Be-Bi:.7f}; '
                   f'iso(success={si},grad={gi:.2e},nneg={int((evi<0).sum())}); '
                   f'env(success={se},grad={ge:.2e},nneg={int((eve<0).sum())},xc={xe:+.6f})')
            print(msg)
            print(f'::notice title=Experiment 03 high-tilt bounce::{msg}')
            if int((evi < 0).sum()) != 1 or int((eve < 0).sum()) != 1:
                raise RuntimeError('wrong negative mode count')
        print('PASS')
    finally:
        fd.BETA_COLD = ob
        fd.DELTA_TILT = ot


if __name__ == '__main__':
    main()
