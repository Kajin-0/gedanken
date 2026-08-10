#!/usr/bin/env python3
"""Regression for the recurrent two-endpoint scattering bound.

For arbitrary noncommuting contraction-valued endpoint reflections R_A,R_B
and bidirectional propagation operators P_BA,P_AB, verify

    P_eff = (I - P_BA R_A P_AB R_B)^(-1) P_BA

obeys

    ||P_eff||_op <= p_plus / (1 - p_plus p_minus),

where p_plus=||P_BA||_op and p_minus=||P_AB||_op.

In the reciprocal case p_plus=p_minus=p, this becomes

    ||P_eff||_op^2 <= eta/(1-eta)^2, eta=p^2.

The test deliberately uses non-normal, noncommuting random contractions.
"""

from __future__ import annotations

import math
import numpy as np

RNG = np.random.default_rng(20260809)


def rand_complex(shape: tuple[int, ...]) -> np.ndarray:
    return (RNG.normal(size=shape) + 1j * RNG.normal(size=shape)) / math.sqrt(2.0)


def opnorm(a: np.ndarray) -> float:
    return float(np.linalg.svd(a, compute_uv=False)[0])


def random_contraction(n_out: int, n_in: int, target_norm: float) -> np.ndarray:
    a = rand_complex((n_out, n_in))
    nrm = opnorm(a)
    if nrm == 0.0:
        return a
    return a * (target_norm / nrm)


def check_general_nonreciprocal(samples: int = 20_000) -> tuple[float, float]:
    worst_ratio = 0.0
    worst_loop_ratio = 0.0

    for _ in range(samples):
        n = int(RNG.integers(1, 8))

        p_plus = float(RNG.uniform(1.0e-4, 0.93))
        p_minus_max = min(0.93, 0.98 / p_plus)
        p_minus = float(RNG.uniform(1.0e-4, p_minus_max))

        P_ba = random_contraction(n, n, p_plus)
        P_ab = random_contraction(n, n, p_minus)
        R_a = random_contraction(n, n, float(RNG.uniform(0.0, 1.0)))
        R_b = random_contraction(n, n, float(RNG.uniform(0.0, 1.0)))

        L = P_ba @ R_a @ P_ab @ R_b
        loop_norm = opnorm(L)
        loop_ceiling = p_plus * p_minus
        assert loop_norm <= loop_ceiling * (1.0 + 2e-12) + 2e-13

        I = np.eye(n, dtype=complex)
        P_eff = np.linalg.solve(I - L, P_ba)
        eff_norm = opnorm(P_eff)
        ceiling = p_plus / (1.0 - p_plus * p_minus)

        assert eff_norm <= ceiling * (1.0 + 2e-11) + 2e-12

        if ceiling > 0.0:
            worst_ratio = max(worst_ratio, eff_norm / ceiling)
        if loop_ceiling > 0.0:
            worst_loop_ratio = max(worst_loop_ratio, loop_norm / loop_ceiling)

    return worst_ratio, worst_loop_ratio


def check_reciprocal_scaling(samples: int = 10_000) -> tuple[float, float]:
    worst_power_ratio = 0.0
    worst_series_ratio = 0.0

    for _ in range(samples):
        n = int(RNG.integers(1, 8))
        p = float(RNG.uniform(1.0e-4, 0.93))
        eta = p * p

        P_ba = random_contraction(n, n, p)
        # Independent reverse map with the same operator norm; reciprocity of
        # singular values is all the norm bound needs.
        P_ab = random_contraction(n, n, p)
        R_a = random_contraction(n, n, float(RNG.uniform(0.0, 1.0)))
        R_b = random_contraction(n, n, float(RNG.uniform(0.0, 1.0)))

        L = P_ba @ R_a @ P_ab @ R_b
        I = np.eye(n, dtype=complex)
        P_eff = np.linalg.solve(I - L, P_ba)

        exact_power = opnorm(P_eff) ** 2
        power_ceiling = eta / (1.0 - eta) ** 2
        assert exact_power <= power_ceiling * (1.0 + 2e-11) + 2e-12
        worst_power_ratio = max(worst_power_ratio, exact_power / power_ceiling)

        # Explicit Neumann partial sums must converge to the resolvent result.
        partial = np.zeros_like(P_ba)
        term = P_ba.copy()
        for _m in range(120):
            partial += term
            term = L @ term
        rel = np.linalg.norm(partial - P_eff) / max(np.linalg.norm(P_eff), 1.0e-15)
        worst_series_ratio = max(worst_series_ratio, rel)
        assert rel < 2e-10

    return worst_power_ratio, worst_series_ratio


def check_wavezone_order() -> None:
    # Verify numerically that eta/(1-eta)^2 - eta = O(eta^2), hence
    # O((kR)^-4) when eta ~ (kR)^-2.
    kR = np.array([10.0, 20.0, 40.0, 80.0, 160.0])
    eta = 25.0 / (16.0 * kR**2)
    correction = eta / (1.0 - eta) ** 2 - eta
    ratio = correction / eta**2

    # The ratio tends to 2 as eta -> 0.
    assert np.all(np.isfinite(ratio))
    assert abs(ratio[-1] - 2.0) < 5e-4

    # Doubling kR should asymptotically reduce the absolute correction by 16.
    scale = correction[:-1] / correction[1:]
    assert np.all(scale > 15.0)
    assert np.all(scale < 17.2)


def main() -> None:
    general_ratio, loop_ratio = check_general_nonreciprocal()
    reciprocal_ratio, series_rel = check_reciprocal_scaling()
    check_wavezone_order()

    print("Recurrent scattering regression: PASS")
    print(f"  worst loop/bound ratio: {loop_ratio:.12f}")
    print(f"  worst general P_eff/bound ratio: {general_ratio:.12f}")
    print(f"  worst reciprocal power/bound ratio: {reciprocal_ratio:.12f}")
    print(f"  worst 120-term Neumann relative error: {series_rel:.3e}")
    print("  wave-zone recurrent power correction: O((kR)^-4) verified")


if __name__ == "__main__":
    main()
