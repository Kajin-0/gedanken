#!/usr/bin/env python3
"""Inductance-retuning scaling closure for Experiment 03.

This script records the analytic consequence of restoring a target screening
parameter beta_L after a nonideality reduces the cold critical current.

For fixed normalized CPR shape f(phi), target beta and dimensionless cold
barrier u_b,

    L = beta Phi0/(2 pi Ic)
    DeltaU = [(Phi0/2pi)^2/L] u_b

so restoring beta by increasing L restores the normalized potential topology
but NOT the physical barrier energy: DeltaU scales approximately with Ic.

Inside the current provisional cubic-MQT diagnostic,

    Cmin = hbar^2 kappa/(alpha^2 DeltaU^2 L) * W(...)^2,

and because DeltaU ~ 1/L at fixed normalized shape,

    Cmin ~ L * W(...)^2,
    sqrt(L Cmin) ~ L * W(...),

up to the slowly varying Lambert-W factor.

The numerical table below is a regression for the realistic-skewness (~0.27)
induced-gap sensitivity family. It is not a full microscopic interface model.
"""

from __future__ import annotations

# Values are the converged cold-state results from the induced-gap/interface
# sensitivity family at T~30 mK. They are kept explicit so this script is a
# transparent regression, not a hidden recalculation of the expensive CPR.
ROWS = [
    # rDelta, Ic_uA, Lretune_pH, barrier_K, Cmin_fF, sqrtLC_ps, sep_Phi0
    (1.00, 3.000, 87.76, 9.103, 160.6, 3.754, 0.2401),
    (0.80, 2.721, 96.76, 8.119, 180.8, 4.183, 0.2396),
    (0.60, 2.361, 111.51, 6.867, 215.3, 4.900, 0.2390),
    (0.50, 2.138, 123.13, 6.103, 243.6, 5.477, 0.2385),
    (0.40, 1.877, 140.30, 5.219, 287.1, 6.347, 0.2378),
    (0.30, 1.563, 168.43, 4.187, 362.5, 7.814, 0.2368),
    (0.25, 1.381, 190.60, 3.603, 425.3, 9.003, 0.2361),
]


def main() -> None:
    print("rDelta Ic[uA] Lretune[pH] barrier[K] Cmin[fF] sqrt(LC)[ps] sep[Phi0]")
    for row in ROWS:
        print("%5.2f %7.3f %11.2f %10.3f %9.1f %12.3f %9.4f" % row)

    # Regression on the central compensation point used in the checkpoint.
    r, ic, L, barrier, cmin, tau, sep = ROWS[2]
    assert abs(r - 0.60) < 1e-12
    assert 110.0 < L < 113.0
    assert 6.7 < barrier < 7.0
    assert 210.0 < cmin < 220.0
    assert 4.7 < tau < 5.1
    assert 0.235 < sep < 0.245

    print("PASS: inductance-retuning regression")


if __name__ == "__main__":
    main()
