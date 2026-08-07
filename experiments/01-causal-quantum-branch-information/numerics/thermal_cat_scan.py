"""Exploratory finite-cat thermal attenuator scan for Experiment 01.

Constructs the thermal attenuator by mixing the signal mode with a thermal
environment on a beam splitter, traces the environment, and computes the
source-qubit / output-mode negativity.

This is a truncation-based numerical check, not a proof.
"""

import math
import numpy as np
from scipy.linalg import expm


def annihilation(dim: int) -> np.ndarray:
    a = np.zeros((dim, dim), dtype=complex)
    for n in range(1, dim):
        a[n - 1, n] = math.sqrt(n)
    return a


def coherent(alpha: complex, dim: int) -> np.ndarray:
    v = np.array(
        [alpha**n / math.sqrt(math.factorial(n)) for n in range(dim)],
        dtype=complex,
    )
    v *= math.exp(-abs(alpha) ** 2 / 2)
    return v / np.linalg.norm(v)


def thermal_probabilities(nbar: float, dim: int) -> np.ndarray:
    if nbar == 0:
        p = np.zeros(dim)
        p[0] = 1.0
        return p
    r = nbar / (nbar + 1.0)
    p = (1.0 - r) * r ** np.arange(dim)
    return p / p.sum()


def beam_splitter_unitary(eta: float, dim: int) -> np.ndarray:
    """Beam splitter with signal transmissivity eta."""
    a = annihilation(dim)
    ident = np.eye(dim)
    a_s = np.kron(a, ident)
    a_e = np.kron(ident, a)
    theta = math.acos(math.sqrt(eta))
    generator = theta * (a_s.conj().T @ a_e - a_s @ a_e.conj().T)
    return expm(generator)


def channel_dyad(
    alpha: complex,
    beta: complex,
    eta: float,
    nbar: float,
    dim: int,
    unitary: np.ndarray,
) -> np.ndarray:
    """Return Lambda(|alpha><beta|) for a thermal attenuator."""
    va = coherent(alpha, dim)
    vb = coherent(beta, dim)
    probs = thermal_probabilities(nbar, dim)
    u4 = unitary.reshape(dim, dim, dim, dim)
    out = np.zeros((dim, dim), dtype=complex)

    for env_n, prob in enumerate(probs):
        # V[s_out,e_out] = sum_sin U[s_out,e_out,s_in,env_n] v[s_in]
        va_out = np.tensordot(u4[:, :, :, env_n], va, axes=([2], [0]))
        vb_out = np.tensordot(u4[:, :, :, env_n], vb, axes=([2], [0]))
        out += prob * (va_out @ vb_out.conj().T)
    return out


def cat_negativity(
    eta: float,
    nbar: float,
    n_delta: float,
    dim: int = 24,
    unitary: np.ndarray | None = None,
) -> tuple[float, float]:
    """Negativity for (|L,+a> + |R,-a>)/sqrt(2) after thermal loss.

    n_delta = |(+a)-(-a)|^2 = 4 |a|^2.
    Returns (negativity, output trace).
    """
    amp = math.sqrt(n_delta) / 2.0
    if unitary is None:
        unitary = beam_splitter_unitary(eta, dim)

    ll = channel_dyad(amp, amp, eta, nbar, dim, unitary)
    rr = channel_dyad(-amp, -amp, eta, nbar, dim, unitary)
    lr = channel_dyad(amp, -amp, eta, nbar, dim, unitary)

    rho = 0.5 * np.block([[ll, lr], [lr.conj().T, rr]])

    # Partial transpose on the source qubit swaps the off-diagonal blocks.
    rho_pt = 0.5 * np.block([[ll, lr.conj().T], [lr, rr]])
    rho_pt = (rho_pt + rho_pt.conj().T) / 2.0
    eigvals = np.linalg.eigvalsh(rho_pt)
    negativity = float(-eigvals[eigvals < 0].sum())
    return negativity, float(np.trace(rho).real)


def run_scan() -> None:
    n_deltas = [0.01, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 4.0, 8.0]

    for nbar, dim in [(0.1, 24), (0.5, 24), (1.0, 28)]:
        eta_eb = nbar / (nbar + 1.0)
        etas = [0.95 * eta_eb, 1.05 * eta_eb, min(0.9, eta_eb + 0.15), 0.8]

        print(f"\nnbar={nbar:.3g}; eta_EB={eta_eb:.8f}; dim={dim}")
        for eta in etas:
            u = beam_splitter_unitary(eta, dim)
            print(f"  eta={eta:.8f}")
            for n_delta in n_deltas:
                neg, trace = cat_negativity(
                    eta, nbar, n_delta, dim=dim, unitary=u
                )
                print(
                    f"    N_delta={n_delta:>5g}  negativity={neg:.8e}  "
                    f"trace={trace:.12f}"
                )


if __name__ == "__main__":
    run_scan()
