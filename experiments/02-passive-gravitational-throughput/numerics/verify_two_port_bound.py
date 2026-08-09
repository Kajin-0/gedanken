#!/usr/bin/env python3
"""Numerical checks for Experiment 02 passive gravitational throughput bounds.

Checks:
1. closed-form EBP equals numerical frequency integration;
2. random passive rate sets obey Gamma_EBP <= eta * min(kappa_gA,kappa_gB);
3. symmetric no-internal-loss optimum occurs at kappa_in=kappa_out=2*kappa_g;
4. V7 benchmark eta*kappa_g scale is reproduced.
"""

from __future__ import annotations

import math
import random

import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize_scalar


def tau(
    omega: float,
    eta: float,
    k_in: float,
    kg_a: float,
    kg_b: float,
    k_out: float,
    k_a: float,
    k_b: float,
) -> float:
    return (
        eta
        * k_in
        * kg_a
        * kg_b
        * k_out
        / ((omega * omega + (k_a / 2.0) ** 2) * (omega * omega + (k_b / 2.0) ** 2))
    )


def ebp_closed(
    eta: float,
    k_in: float,
    kg_a: float,
    kg_b: float,
    k_out: float,
    k_a: float,
    k_b: float,
) -> float:
    return 4.0 * eta * k_in * kg_a * kg_b * k_out / (k_a * k_b * (k_a + k_b))


def ebp_numeric(
    eta: float,
    k_in: float,
    kg_a: float,
    kg_b: float,
    k_out: float,
    k_a: float,
    k_b: float,
) -> float:
    value, _ = quad(
        lambda w: tau(w, eta, k_in, kg_a, kg_b, k_out, k_a, k_b),
        -np.inf,
        np.inf,
        epsabs=1e-11,
        epsrel=1e-11,
        limit=500,
    )
    return value / (2.0 * math.pi)


def check_integral_identity() -> None:
    params = dict(
        eta=0.17,
        k_in=1.3,
        kg_a=0.7,
        kg_b=2.1,
        k_out=0.9,
        k_a=2.4,
        k_b=3.4,
    )
    closed = ebp_closed(**params)
    numeric = ebp_numeric(**params)
    assert math.isclose(closed, numeric, rel_tol=2e-10, abs_tol=1e-12), (closed, numeric)


def check_random_bound(samples: int = 100_000, seed: int = 7) -> None:
    rng = random.Random(seed)
    worst_ratio = 0.0

    for _ in range(samples):
        # Log-uniform gravitational rates over many decades.
        kg_a = 10.0 ** rng.uniform(-9.0, 3.0)
        kg_b = 10.0 ** rng.uniform(-9.0, 3.0)

        # Passive local couplings and internal losses are nonnegative.
        k_in = kg_a * 10.0 ** rng.uniform(-3.0, 3.0)
        k_out = kg_b * 10.0 ** rng.uniform(-3.0, 3.0)
        k_i_a = kg_a * 10.0 ** rng.uniform(-6.0, 2.0)
        k_i_b = kg_b * 10.0 ** rng.uniform(-6.0, 2.0)

        k_a = k_in + kg_a + k_i_a
        k_b = kg_b + k_out + k_i_b
        eta = rng.random()

        gamma = ebp_closed(eta, k_in, kg_a, kg_b, k_out, k_a, k_b)
        ceiling = eta * min(kg_a, kg_b)

        assert gamma <= ceiling * (1.0 + 2e-14) + 1e-300
        if ceiling > 0.0:
            worst_ratio = max(worst_ratio, gamma / ceiling)

    print(f"random passive bound check: PASS ({samples} samples; max ratio={worst_ratio:.12g})")


def symmetric_ratio(x: float) -> float:
    # Gamma_EBP / (eta*kappa_g) for kgA=kgB=kg, no internal loss,
    # kappa_in=kappa_out=x*kappa_g.
    return 2.0 * x * x / (1.0 + x) ** 3


def check_symmetric_optimum() -> None:
    result = minimize_scalar(lambda x: -symmetric_ratio(x), bounds=(1e-8, 100.0), method="bounded")
    x_opt = result.x
    ratio = -result.fun

    assert math.isclose(x_opt, 2.0, rel_tol=2e-6, abs_tol=2e-6), x_opt
    assert math.isclose(ratio, 8.0 / 27.0, rel_tol=1e-10, abs_tol=1e-10), ratio
    print(f"symmetric optimum: PASS (x={x_opt:.9f}, ratio={ratio:.12f})")


def check_v7_benchmark() -> None:
    eta = 0.015625
    kg = 6.87e-26
    scale = eta * kg
    years = 1.0 / scale / (365.25 * 24.0 * 3600.0)

    assert math.isclose(scale, 1.0734375e-27, rel_tol=1e-15)
    assert math.isclose(years, 2.952019825469946e19, rel_tol=1e-15)
    print(f"V7 interface scale: PASS ({scale:.8e} s^-1; inverse={years:.8e} yr)")


def main() -> None:
    check_integral_identity()
    print("closed-form frequency integral: PASS")
    check_random_bound()
    check_symmetric_optimum()
    check_v7_benchmark()
    print("all Experiment 02 two-port checks passed")


if __name__ == "__main__":
    main()
