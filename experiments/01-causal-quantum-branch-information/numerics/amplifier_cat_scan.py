"""Independent finite-Fock audit for a binary coherent hybrid through a thermal amplifier.

This script reconstructs the phase-insensitive thermal amplifier from a two-mode
squeezing Stinespring dilation rather than using the analytic coherent-state kernel.
It is therefore intended as an implementation-independent check of
DIRECT_GAUSSIAN_BINARY_PROBE_PROOF.md.

Channel convention
------------------
    a_out = sqrt(G) a_in + sqrt(G-1) e^dagger

with environment occupation n_env.  In the repository's (tau, m) convention,

    tau = G
    m   = (G - 1) (n_env + 1)

and the exact entanglement-breaking threshold is

    n_env >= 1 / (G - 1).

Finite Fock truncation can produce small spurious negative PT eigenvalues on the
EB side.  Convergence with cutoff is therefore part of the audit, not optional.
"""

from __future__ import annotations

import argparse
import math

import numpy as np
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


def thermal_probabilities(nbar: float, dim: int) -> tuple[np.ndarray, float]:
    """Truncated thermal probabilities and exact omitted geometric tail."""
    if nbar == 0.0:
        p = np.zeros(dim)
        p[0] = 1.0
        return p, 0.0

    r = nbar / (nbar + 1.0)
    p = (1.0 - r) * r ** np.arange(dim)
    omitted_tail = float(r**dim)
    p /= p.sum()
    return p, omitted_tail


def two_mode_squeezer_unitary(gain: float, dim: int) -> np.ndarray:
    """Finite-matrix two-mode squeezer for gain G = cosh(r)^2."""
    if gain < 1.0:
        raise ValueError("Thermal amplifier requires gain >= 1.")

    a = annihilation(dim)
    ident = np.eye(dim)
    a_s = np.kron(a, ident)
    a_e = np.kron(ident, a)

    r = math.acosh(math.sqrt(gain))
    generator = r * (
        a_s.conj().T @ a_e.conj().T
        - a_s @ a_e
    )
    return expm(generator)


def channel_dyad(
    alpha: complex,
    beta: complex,
    gain: float,
    n_env: float,
    dim: int,
    unitary: np.ndarray,
) -> tuple[np.ndarray, float]:
    """Return Phi(|alpha><beta|) from the explicit thermal-amplifier dilation."""
    va = coherent(alpha, dim)
    vb = coherent(beta, dim)
    probs, omitted_tail = thermal_probabilities(n_env, dim)

    # U[s_out, e_out, s_in, e_in]
    u4 = unitary.reshape(dim, dim, dim, dim)
    out = np.zeros((dim, dim), dtype=complex)

    for env_n, prob in enumerate(probs):
        # V[s_out, e_out] = sum_sin U[s_out,e_out,s_in,env_n] v[s_in]
        va_out = np.tensordot(u4[:, :, :, env_n], va, axes=([2], [0]))
        vb_out = np.tensordot(u4[:, :, :, env_n], vb, axes=([2], [0]))

        # Trace e_out: V_a V_b^dagger on the signal indices.
        out += prob * (va_out @ vb_out.conj().T)

    return out, omitted_tail


def cat_pt_spectrum(
    gain: float,
    n_env: float,
    amplitude: float,
    dim: int,
    unitary: np.ndarray | None = None,
) -> tuple[np.ndarray, float, float]:
    """PT spectrum for (|0,+a> + |1,-a>)/sqrt(2)."""
    if unitary is None:
        unitary = two_mode_squeezer_unitary(gain, dim)

    ll, tail = channel_dyad(amplitude, amplitude, gain, n_env, dim, unitary)
    rr, _ = channel_dyad(-amplitude, -amplitude, gain, n_env, dim, unitary)
    lr, _ = channel_dyad(amplitude, -amplitude, gain, n_env, dim, unitary)

    rho = 0.5 * np.block([[ll, lr], [lr.conj().T, rr]])

    # Partial transpose on the source qubit swaps the off-diagonal blocks.
    rho_pt = 0.5 * np.block([[ll, lr.conj().T], [lr, rr]])
    rho_pt = (rho_pt + rho_pt.conj().T) / 2.0

    eigvals = np.linalg.eigvalsh(rho_pt)
    return eigvals, float(np.trace(rho).real), tail


def run_case(
    gain: float,
    n_env: float,
    amplitude: float,
    cutoffs: list[int],
) -> None:
    threshold = math.inf if gain == 1.0 else 1.0 / (gain - 1.0)
    exact_status = "EB" if n_env >= threshold else "non-EB"
    tau = gain
    m = (gain - 1.0) * (n_env + 1.0)

    print(
        f"G={gain:.8g}, n_env={n_env:.8g}, a={amplitude:.8g}; "
        f"tau={tau:.8g}, m={m:.8g}; exact={exact_status}; "
        f"n_env_EB={threshold:.8g}"
    )
    print("cutoff   lambda_min(PT)       negativity          trace          env_tail")

    for dim in cutoffs:
        unitary = two_mode_squeezer_unitary(gain, dim)
        eigvals, trace, tail = cat_pt_spectrum(
            gain, n_env, amplitude, dim, unitary=unitary
        )
        negativity = float(-eigvals[eigvals < 0.0].sum())
        print(
            f"{dim:6d}   {eigvals[0]: .10e}   {negativity: .10e}   "
            f"{trace:.12f}   {tail:.3e}"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--gain", type=float, default=None)
    parser.add_argument("--n-env", type=float, default=None)
    parser.add_argument("--amplitude", type=float, default=0.4)
    parser.add_argument(
        "--cutoffs",
        type=int,
        nargs="+",
        default=[10, 12, 14, 16, 18],
    )
    args = parser.parse_args()

    if args.gain is not None or args.n_env is not None:
        if args.gain is None or args.n_env is None:
            parser.error("--gain and --n-env must be supplied together")
        run_case(args.gain, args.n_env, args.amplitude, args.cutoffs)
        return

    # Canonical regression cases used in NUMERICAL_AUDIT_AMPLIFIER_ADDITIVE_NOISE.md.
    run_case(1.5, 0.5, args.amplitude, args.cutoffs)
    print()
    run_case(1.5, 3.0, args.amplitude, args.cutoffs)


if __name__ == "__main__":
    main()
