#!/usr/bin/env python3
"""Numerical checks for the compact quadrupole TT propagation bound.

Checks:
1. random complex STF quadrupoles obey D <= 5/2 for random directions;
2. aligned plus and cross quadrupoles saturate D = 5/2 on axis;
3. the angular integral of the TT projection equals (8 pi / 5) ||Q||^2;
4. the directivity product reproduces the 25/[16(kR)^2] wave-zone link ceiling.
"""

from __future__ import annotations

import math
import numpy as np
from scipy.integrate import dblquad

RNG = np.random.default_rng(20260809)


def random_stf() -> np.ndarray:
    x = RNG.normal(size=(3, 3)) + 1j * RNG.normal(size=(3, 3))
    q = 0.5 * (x + x.T)
    q -= np.eye(3) * np.trace(q) / 3.0
    return q


def random_unit() -> np.ndarray:
    v = RNG.normal(size=3)
    return v / np.linalg.norm(v)


def transverse_basis(n: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    # Pick a reference axis safely away from parallel to n.
    ref = np.array([0.0, 0.0, 1.0])
    if abs(float(np.dot(n, ref))) > 0.9:
        ref = np.array([1.0, 0.0, 0.0])
    e1 = np.cross(n, ref)
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(n, e1)
    e2 /= np.linalg.norm(e2)
    return e1, e2


def polarizations(n: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    e1, e2 = transverse_basis(n)
    eps_plus = (np.outer(e1, e1) - np.outer(e2, e2)) / math.sqrt(2.0)
    eps_cross = (np.outer(e1, e2) + np.outer(e2, e1)) / math.sqrt(2.0)
    return eps_plus, eps_cross


def tt_weight(q: np.ndarray, n: np.ndarray) -> float:
    eps_plus, eps_cross = polarizations(n)
    a_plus = np.sum(q * eps_plus)
    a_cross = np.sum(q * eps_cross)
    return float(abs(a_plus) ** 2 + abs(a_cross) ** 2)


def qnorm(q: np.ndarray) -> float:
    return float(np.real(np.sum(np.conj(q) * q)))


def directivity(q: np.ndarray, n: np.ndarray) -> float:
    return 2.5 * tt_weight(q, n) / qnorm(q)


def check_random_directivity(samples: int = 250_000) -> None:
    max_d = 0.0
    for _ in range(samples):
        q = random_stf()
        n = random_unit()
        d = directivity(q, n)
        assert d <= 2.5 * (1.0 + 5e-13), d
        assert d >= -1e-14, d
        max_d = max(max_d, d)
    print(f"random STF directivity: PASS ({samples} samples; max D={max_d:.12g})")


def check_saturation() -> None:
    n = np.array([0.0, 0.0, 1.0])
    q_plus = np.diag([1.0, -1.0, 0.0]).astype(complex)
    q_cross = np.array(
        [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 0.0]], dtype=complex
    )
    d_plus = directivity(q_plus, n)
    d_cross = directivity(q_cross, n)
    assert math.isclose(d_plus, 2.5, rel_tol=1e-13, abs_tol=1e-13)
    assert math.isclose(d_cross, 2.5, rel_tol=1e-13, abs_tol=1e-13)
    print(f"TT saturation: PASS (plus={d_plus:.12g}, cross={d_cross:.12g})")


def n_from_angles(theta: float, phi: float) -> np.ndarray:
    return np.array(
        [math.sin(theta) * math.cos(phi), math.sin(theta) * math.sin(phi), math.cos(theta)]
    )


def check_angular_integral() -> None:
    # A generic complex STF tensor, deliberately not aligned with the integration axes.
    q = np.array(
        [
            [1.2 + 0.3j, -0.4 + 0.2j, 0.7 - 0.1j],
            [-0.4 + 0.2j, -0.8 + 0.5j, -0.2 + 0.4j],
            [0.7 - 0.1j, -0.2 + 0.4j, -0.4 - 0.8j],
        ],
        dtype=complex,
    )
    # Trace is exactly zero.
    assert abs(np.trace(q)) < 1e-14

    def integrand(phi: float, theta: float) -> float:
        return tt_weight(q, n_from_angles(theta, phi)) * math.sin(theta)

    value, _ = dblquad(
        integrand,
        0.0,
        math.pi,
        lambda _: 0.0,
        lambda _: 2.0 * math.pi,
        epsabs=2e-8,
        epsrel=2e-8,
    )
    expected = 8.0 * math.pi / 5.0 * qnorm(q)
    assert math.isclose(value, expected, rel_tol=2e-8, abs_tol=2e-8), (value, expected)
    print(f"TT angular integral: PASS (ratio={value / expected:.12g})")


def check_link_coefficient() -> None:
    # D_A=D_B=5/2 and lambda/(4 pi R)=1/(2 k R).
    k_r = 10.0
    eta = 2.5 * 2.5 * (1.0 / (2.0 * k_r)) ** 2
    expected = 25.0 / (16.0 * k_r * k_r)
    assert math.isclose(eta, expected, rel_tol=1e-15, abs_tol=1e-15)
    print(f"wave-zone coefficient: PASS (eta={eta:.12g})")


def main() -> None:
    check_random_directivity()
    check_saturation()
    check_angular_integral()
    check_link_coefficient()
    print("all Experiment 02 TT propagation checks passed")


if __name__ == "__main__":
    main()
