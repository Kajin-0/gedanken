#!/usr/bin/env python3
"""Independent numerical regression for the TT one-graviton mode-overlap audit.

Checks:
1. The normalized plus-quadrupole angular overlap integrates to the closed form.
2. The closed form equals the sum of outgoing and time-reversed pieces.
3. The outgoing piece tends to amplitude coefficient 5/4 in the wave zone.

This script does not use the gravitational Green-function/self-energy formula as an
input; P(z) appears only in the independently derived exponential decomposition.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import quad


def polynomial_p(z: float) -> complex:
    return 3.0 - 3.0j * z - 3.0 * z**2 + 2.0j * z**3 + z**4


def overlap_numeric(z: float) -> complex:
    """Direct quadrature of S(z)=5/32 int_{-1}^1 (1+6 mu^2+mu^4)e^{izmu} dmu."""

    def real_integrand(mu: float) -> float:
        weight = (5.0 / 32.0) * (1.0 + 6.0 * mu**2 + mu**4)
        return weight * np.cos(z * mu)

    def imag_integrand(mu: float) -> float:
        weight = (5.0 / 32.0) * (1.0 + 6.0 * mu**2 + mu**4)
        return weight * np.sin(z * mu)

    real = quad(real_integrand, -1.0, 1.0, epsabs=1e-13, epsrel=1e-13)[0]
    imag = quad(imag_integrand, -1.0, 1.0, epsabs=1e-13, epsrel=1e-13)[0]
    return real + 1.0j * imag


def overlap_closed(z: float) -> float:
    return (5.0 / (4.0 * z**5)) * (
        2.0 * z**4 * np.sin(z)
        + 4.0 * z**3 * np.cos(z)
        - 6.0 * z**2 * np.sin(z)
        - 6.0 * z * np.cos(z)
        + 6.0 * np.sin(z)
    )


def outgoing(z: float) -> complex:
    return -(5.0j / 4.0) * polynomial_p(z) * np.exp(1.0j * z) / z**5


def time_reversed(z: float) -> complex:
    return +(5.0j / 4.0) * polynomial_p(-z) * np.exp(-1.0j * z) / z**5


def main() -> None:
    points = (0.5, 1.0, 3.0, 10.0, 30.0, 100.0)

    max_quad_error = 0.0
    max_split_error = 0.0

    for z in points:
        direct = overlap_numeric(z)
        closed = overlap_closed(z)
        split = outgoing(z) + time_reversed(z)

        quad_error = abs(direct - closed)
        split_error = abs(complex(closed) - split)
        max_quad_error = max(max_quad_error, quad_error)
        max_split_error = max(max_split_error, split_error)

        print(
            f"z={z:6.1f}  "
            f"S_num={direct.real:+.15e}{direct.imag:+.2e}j  "
            f"quad_err={quad_error:.3e}  split_err={split_error:.3e}  "
            f"z|S_+|={z * abs(outgoing(z)):.12f}"
        )

    assert max_quad_error < 2e-12, max_quad_error
    assert max_split_error < 2e-12, max_split_error

    # At z=100 the leading wave-zone coefficient should already be within 2e-4
    # of 5/4. The exact value approaches 1.25 from below.
    asymptotic_coefficient = 100.0 * abs(outgoing(100.0))
    assert abs(asymptotic_coefficient - 1.25) < 2e-4, asymptotic_coefficient

    # The normalized fixed-frequency overlap must approach unity at z -> 0.
    small_z_overlap = overlap_numeric(1e-3).real
    assert abs(small_z_overlap - 1.0) < 1e-6, small_z_overlap

    print("\nPASS")
    print(f"max direct-quadrature error : {max_quad_error:.3e}")
    print(f"max outgoing+reverse error  : {max_split_error:.3e}")
    print(f"100*|S_+(100)|             : {asymptotic_coefficient:.12f}")
    print("target wave-zone coefficient: 1.250000000000")
    print("target storage coefficient  : 25/16 = 1.562500000000 (amplitude squared times z^2)")


if __name__ == "__main__":
    main()
