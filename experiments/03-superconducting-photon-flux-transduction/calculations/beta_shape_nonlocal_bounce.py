#!/usr/bin/env python3
"""Same-environment nonlocal dark action for beta=.85 and .90 shape rescues.

Uses the converged spectral solver from R80_nonlocal_bounce_spectral.py with the
live tilt delta=.05 and passive R=80 ohm, alpha=.90 environment.  This isolates
how much total zero-T action is gained by static barrier shaping before any
additional electrical-rescaling rescue.

The script also reports the exact isolated action and fold temperature of each
shape.  No physical dark-count rate is quoted; prefactor/finite-T normalization
remain separate.
"""
from __future__ import annotations
import full_dynamic_rfsquid as fd
from R80_nonlocal_bounce_spectral import solve_one


def main():
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    try:
        for beta in (.80,.85,.90):
            fd.BETA_COLD=beta; fd.DELTA_TILT=.05
            # Nbasis=36 already gave sub-1e-4 action convergence at the live baseline.
            iso=solve_one(36,6144,None,None)
            env=solve_one(36,6144,80.0,.90)
            msg=(f'beta={beta:.2f} tilt=.050: Biso={iso["B"]:.6f} '
                 f'Benv={env["B"]:.6f} DeltaBenv={env["B"]-iso["B"]:.6f} '
                 f'actionRatio={env["B"]/iso["B"]:.6f} '
                 f'xcenter={env["xcenter"]:+.6f} nneg_even={int((env["ev"]<0).sum())}')
            print(msg); print(f'::notice title=Experiment 03 shaped nonlocal bounce::{msg}')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot
    print('PASS')
if __name__=='__main__': main()
