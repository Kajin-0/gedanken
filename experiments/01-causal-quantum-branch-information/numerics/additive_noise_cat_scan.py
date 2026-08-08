"""Independent Gauss-Hermite audit for binary coherent entanglement under additive Gaussian noise.

This script realizes the unit-gain additive classical-noise channel directly as

    Phi_m(rho) = integral d^2 z/(pi m) exp(-|z|^2/m) D(z) rho D(z)^dagger.

It does not use the analytic coherent-dyad kernel from the theorem proof.

Repository convention
---------------------
    tau = 1
    vacuum-output occupation = m
    entanglement breaking iff m >= 1.

The displacement integral is evaluated with tensor-product Gauss-Hermite
quadrature after z = sqrt(m) (x + i y).  Finite quadrature order and finite Fock
cutoff can leave tiny spurious negative PT eigenvalues on the EB side, so
convergence must be checked explicitly.
"""

from __future__ import annotations

import argparse
import math

import numpy as np
from numpy.polynomial.hermite import hermgauss
from scipy.linalg import expm


def annihilation(dim: int) -> np.ndarray:
    a = np.zeros((dim, dim), dtype=complex)
    for n in range(1, dim):
        a[n - 1, n] = math.sqrt(n)
    return a


def coherent(alpha: complex, dim: int) -> np.ndarray:
    """Normalized coherent state in a truncated Fock basis."""
    v = np.empty(dim, dtype=complex)
    v[0] = 1.0
    for n in range(1, dim):
        v[n] = v[n - 1] * alpha / math.sqrt(n)
    v *= math.exp(-abs(alpha) ** 2 / 2.0)
    return v / np.linalg.norm(v)


def displacement(z: complex, a: np.ndarray) -> np.ndarray:
    """Finite-Fock displacement matrix exp(z a^dagger - z* a)."""
    return expm(z * a.conj().T - np.conj(z) * a)


def additive_noise_dyad(
    alpha: complex,
    beta: complex,
    noise: float,
    dim: int,
    order: int,
    *,
    a_op: np.ndarray | None = None,
) -> np.ndarray:
    """Return Phi_m(|alpha><beta|) by direct Gaussian displacement integration."""
    if noise < 0.0:
        raise ValueError("Additive-noise variance m must be nonnegative.")

    va = coherent(alpha, dim)
    vb = coherent(beta, dim)
    dyad = np.outer(va, vb.conj())

    if noise == 0.0:
        return dyad

    if a_op is None:
        a_op = annihilation(dim)

    nodes, weights = hermgauss(order)
    out = np.zeros((dim, dim), dtype=complex)
    scale = math.sqrt(noise)

    # z = sqrt(m) (x + i y) turns
    # d^2z/(pi m) exp(-|z|^2/m)
    # into dx dy/pi exp(-x^2-y^2).
    for i, x in enumerate(nodes):
        for j, y in enumerate(nodes):
            z = scale * complex(x, y)
            d = displacement(z, a_op)
            out += (weights[i] * weights[j] / math.pi) * (d @ dyad @ d.conj().T)

    return out


def cat_pt_spectrum(
    noise: float,
    amplitude: float,
    dim: int,
    order: int,
) -> tuple[np.ndarray, float]:
    """PT spectrum for (|0,+a> + |1,-a>)/sqrt(2)."""
    a_op = annihilation(dim)

    ll = additive_noise_dyad(amplitude, amplitude, noise, dim, order, a_op=a_op)
    rr = additive_noise_dyad(-amplitude, -amplitude, noise, dim, order, a_op=a_op)
    lr = additive_noise_dyad(amplitude, -amplitude, noise, dim, order, a_op=a_op)

    rho = 0.5 * np.block([[ll, lr], [lr.conj().T, rr]])
    rho_pt = 0.5 * np.block([[ll, lr.conj().T], [lr, rr]])
    rho_pt = (rho_pt + rho_pt.conj().T) / 2.0

    eigvals = np.linalg.eigvalsh(rho_pt)
    return eigvals, float(np.trace(rho).real)


def run_case(
    noise: float,
    amplitude: float,
    dim: int,
    orders: list[int],
) -> None:
    exact_status = "EB" if noise >= 1.0 else "non-EB"
    print(
        f"m={noise:.8g}, a={amplitude:.8g}, dim={dim}; "
        f"tau=1; exact={exact_status}; m_EB=1"
    )
    print("order    lambda_min(PT)       negativity          trace")

    for order in orders:
        eigvals, trace = cat_pt_spectrum(noise, amplitude, dim, order)
        negativity = float(-eigvals[eigvals < 0.0].sum())
        print(
            f"{order:5d}   {eigvals[0]: .10e}   {negativity: .10e}   "
            f"{trace:.12f}"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--noise", type=float, default=None)
    parser.add_argument("--amplitude", type=float, default=0.35)
    parser.add_argument("--dim", type=int, default=16)
    parser.add_argument(
        "--orders",
        type=int,
        nargs="+",
        default=[12, 16, 20],
    )
    args = parser.parse_args()

    if args.noise is not None:
        run_case(args.noise, args.amplitude, args.dim, args.orders)
        return

    # Regression cases spanning the exact m=1 EB threshold.
    for noise in (0.70, 0.95, 1.05, 1.30):
        run_case(noise, args.amplitude, args.dim, args.orders)
        print()


if __name__ == "__main__":
    main()
