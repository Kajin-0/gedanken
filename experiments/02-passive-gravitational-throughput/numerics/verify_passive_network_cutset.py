#!/usr/bin/env python3
"""Numerical checks for the Experiment 02 passive-network cut-set theorem.

The script generates random stable passive linear quantum networks with

    A = -i H - K^\dagger K / 2

and checks:

1. the selected-input controllability Gramian satisfies 0 <= P <= I;
2. the endpoint H2 norm is bounded by Tr(K_g^\dagger K_g);
3. randomly cascaded source -> propagation -> receiver networks obey the
   end-to-end cut-set ceiling by direct frequency quadrature on representative
   low-dimensional cases.
"""

from __future__ import annotations

import math
import numpy as np
from scipy.integrate import quad
from scipy.linalg import solve_continuous_lyapunov

RNG = np.random.default_rng(20260809)


def rand_complex(shape: tuple[int, ...], scale: float = 1.0) -> np.ndarray:
    return scale * (RNG.normal(size=shape) + 1j * RNG.normal(size=shape)) / math.sqrt(2.0)


def passive_endpoint(
    n_modes: int,
    n_selected_in: int,
    n_grav: int,
    n_loss: int,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    k_in = rand_complex((n_selected_in, n_modes))
    k_g = rand_complex((n_grav, n_modes))
    k_loss = rand_complex((n_loss, n_modes))
    k_all = np.vstack((k_in, k_g, k_loss))

    x = rand_complex((n_modes, n_modes))
    h = (x + x.conj().T) / 2.0
    a = -1j * h - 0.5 * k_all.conj().T @ k_all
    return a, k_in, k_g, k_loss, k_all


def cross_transfer(a: np.ndarray, k_out: np.ndarray, k_in: np.ndarray, omega: float) -> np.ndarray:
    eye = np.eye(a.shape[0], dtype=complex)
    return -k_out @ np.linalg.solve(1j * omega * eye - a, k_in.conj().T)


def endpoint_h2_from_gramian(a: np.ndarray, k_in: np.ndarray, k_out: np.ndarray) -> tuple[float, np.ndarray]:
    q = k_in.conj().T @ k_in
    p = solve_continuous_lyapunov(a, -q)
    h2_sq = float(np.real(np.trace(k_out @ p @ k_out.conj().T)))
    return h2_sq, p


def check_endpoint_gramian(samples: int = 20_000) -> None:
    worst_h2_ratio = 0.0
    largest_p_eigenvalue = 0.0
    smallest_p_eigenvalue = 1.0

    for _ in range(samples):
        n = int(RNG.integers(1, 7))
        m_in = int(RNG.integers(1, 4))
        m_g = int(RNG.integers(1, 4))
        m_loss = int(RNG.integers(1, 4))

        a, k_in, k_g, _, _ = passive_endpoint(n, m_in, m_g, m_loss)
        h2_sq, p = endpoint_h2_from_gramian(a, k_in, k_g)

        p_eigs = np.linalg.eigvalsh((p + p.conj().T) / 2.0)
        smallest_p_eigenvalue = min(smallest_p_eigenvalue, float(np.min(p_eigs)))
        largest_p_eigenvalue = max(largest_p_eigenvalue, float(np.max(p_eigs)))

        resource = float(np.real(np.trace(k_g.conj().T @ k_g)))
        assert h2_sq <= resource * (1.0 + 2e-10) + 1e-12
        assert np.min(p_eigs) >= -2e-10
        assert np.max(p_eigs) <= 1.0 + 2e-10

        if resource > 0.0:
            worst_h2_ratio = max(worst_h2_ratio, h2_sq / resource)

    print(
        "endpoint Gramian/H2 bound: PASS "
        f"({samples} samples; max H2/resource={worst_h2_ratio:.12g}; "
        f"P eig range=[{smallest_p_eigenvalue:.3e}, {largest_p_eigenvalue:.12g}])"
    )


def integrated_cascade(
    a_src: np.ndarray,
    k_u: np.ndarray,
    k_ga: np.ndarray,
    a_rec: np.ndarray,
    k_gb: np.ndarray,
    k_v: np.ndarray,
    p_g: np.ndarray,
) -> float:
    def integrand(omega: float) -> float:
        s = cross_transfer(a_src, k_ga, k_u, omega)
        r = cross_transfer(a_rec, k_v, k_gb, omega)
        t = r @ p_g @ s
        return float(np.real(np.trace(t.conj().T @ t))) / (2.0 * math.pi)

    value, _ = quad(integrand, -np.inf, np.inf, epsabs=1e-8, epsrel=2e-7, limit=500)
    return float(value)


def check_cascade_quadrature(samples: int = 100) -> None:
    worst_ratio = 0.0

    for _ in range(samples):
        n_src = int(RNG.integers(1, 4))
        n_rec = int(RNG.integers(1, 4))
        n_g = int(RNG.integers(1, 4))
        n_u = int(RNG.integers(1, 3))
        n_v = int(RNG.integers(1, 3))

        a_src, k_u, k_ga, _, _ = passive_endpoint(n_src, n_u, n_g, int(RNG.integers(1, 3)))

        # For the receiver, the first selected channel block is gravitational;
        # the second block is treated as useful output.
        a_rec, k_gb, k_v, _, _ = passive_endpoint(n_rec, n_g, n_v, int(RNG.integers(1, 3)))

        x = rand_complex((n_g, n_g))
        u, _, vh = np.linalg.svd(x)
        eta_max = float(RNG.uniform(1e-4, 1.0))
        p_g = math.sqrt(eta_max) * (u @ vh)

        gamma = integrated_cascade(a_src, k_u, k_ga, a_rec, k_gb, k_v, p_g)
        source_resource = float(np.real(np.trace(k_ga.conj().T @ k_ga)))
        receiver_resource = float(np.real(np.trace(k_gb.conj().T @ k_gb)))
        ceiling = eta_max * min(source_resource, receiver_resource)

        assert gamma <= ceiling * (1.0 + 5e-7) + 1e-10
        if ceiling > 0.0:
            worst_ratio = max(worst_ratio, gamma / ceiling)

    print(f"end-to-end quadrature cut-set check: PASS ({samples} samples; max ratio={worst_ratio:.12g})")


def main() -> None:
    check_endpoint_gramian()
    check_cascade_quadrature()
    print("all Experiment 02 passive-network checks passed")


if __name__ == "__main__":
    main()
