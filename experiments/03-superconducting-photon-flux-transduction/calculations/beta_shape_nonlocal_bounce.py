#!/usr/bin/env python3
"""Same-environment nonlocal dark action for beta=.85 and .90 shape rescues.

Uses the converged spectral solver from R80_nonlocal_bounce_spectral.py with the
live tilt delta=.05 and passive R=80 ohm, alpha=.90 environment.  This isolates
how much total zero-T action is gained by static barrier shaping before any
additional electrical-rescaling rescue.

Numerical note
--------------
The stronger shaped barriers approach the metastable minimum more slowly in the
Euclidean seed trajectory than the live beta=.80 baseline.  The authoritative
isolated action itself is obtained independently by quadrature.  For the shaped
spectral solve we therefore relax only the *seed-tail representation* from
2e-9 rad to 1e-7 rad.  The live baseline solver and its validated action remain
unchanged.  A convergence check at 5e-8 is also reported for beta=.90.

No physical dark-count rate is quoted; prefactor/finite-T normalization remain
separate.
"""
from __future__ import annotations

import full_dynamic_rfsquid as fd
import R80_nonlocal_bounce_spectral as spec
import R80_dissipative_bounce_screen as bounce


def solve_relaxed(nbasis,ngrid,R,alpha,tail_eps=1e-7):
    original=spec.isolated_bounce
    try:
        spec.isolated_bounce=lambda model,nfft=65536: bounce.isolated_bounce(
            model,nfft=nfft,tail_eps=tail_eps
        )
        return spec.solve_one(nbasis,ngrid,R,alpha)
    finally:
        spec.isolated_bounce=original


def main():
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    try:
        for beta in (.80,.85,.90):
            fd.BETA_COLD=beta; fd.DELTA_TILT=.05
            iso=solve_relaxed(36,6144,None,None,1e-7)
            env=solve_relaxed(36,6144,80.0,.90,1e-7)
            msg=(f'beta={beta:.2f} tilt=.050: Biso={iso["B"]:.6f} '
                 f'Benv={env["B"]:.6f} DeltaBenv={env["B"]-iso["B"]:.6f} '
                 f'actionRatio={env["B"]/iso["B"]:.6f} '
                 f'xcenter={env["xcenter"]:+.6f} nneg_even={int((env["ev"]<0).sum())}')
            print(msg); print(f'::notice title=Experiment 03 shaped nonlocal bounce::{msg}')

            if beta==.90:
                env2=solve_relaxed(36,6144,80.0,.90,5e-8)
                cmsg=(f'beta=.90 tail convergence: B(1e-7)={env["B"]:.7f}, '
                      f'B(5e-8)={env2["B"]:.7f}, delta={env2["B"]-env["B"]:+.3e}')
                print(cmsg); print(f'::notice title=Experiment 03 shaped bounce tail convergence::{cmsg}')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot
    print('PASS')
if __name__=='__main__': main()
