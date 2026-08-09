#!/usr/bin/env python3
"""Microscopic checks for gravitational port factorization.

The test uses a quadrature representation of the TT one-graviton angular
Hilbert space. Several matter modes are assigned deliberately overlapping
complex STF quadrupole radiation patterns. It verifies that

    Gamma_g = G^dagger G

contains the complete nonorthogonal radiative Gram matrix, while the polar
factorization

    G = V Gamma_g^(1/2)

separates coupling magnitude from normalized angular mode shape. For source
and receiver mode sets it then checks

    G_B^dagger U G_A
      = Gamma_B^(1/2) (V_B^dagger U V_A) Gamma_A^(1/2)

for free fixed-frequency translation U. No independent-bath-channel-per-mode
assumption is used.
"""

from __future__ import annotations

import math
import numpy as np

RNG = np.random.default_rng(20260809)


def sphere_quadrature(n_theta: int = 28, n_phi: int = 56):
    x, w = np.polynomial.legendre.leggauss(n_theta)
    phis = 2.0 * math.pi * np.arange(n_phi) / n_phi
    points = []
    weights = []
    for xi, wi in zip(x, w):
        s = math.sqrt(max(0.0, 1.0 - xi * xi))
        for phi in phis:
            points.append([s * math.cos(phi), s * math.sin(phi), xi])
            weights.append(wi * 2.0 * math.pi / n_phi)
    return np.asarray(points), np.asarray(weights)


def transverse_basis(n: np.ndarray):
    ref = np.array([0.0, 0.0, 1.0])
    if abs(float(np.dot(n, ref))) > 0.9:
        ref = np.array([1.0, 0.0, 0.0])
    e1 = np.cross(n, ref)
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(n, e1)
    e2 /= np.linalg.norm(e2)
    return e1, e2


def polarizations(n: np.ndarray):
    e1, e2 = transverse_basis(n)
    eps_plus = (np.outer(e1, e1) - np.outer(e2, e2)) / math.sqrt(2.0)
    eps_cross = (np.outer(e1, e2) + np.outer(e2, e1)) / math.sqrt(2.0)
    return eps_plus, eps_cross


def random_stf() -> np.ndarray:
    x = RNG.normal(size=(3, 3)) + 1j * RNG.normal(size=(3, 3))
    q = 0.5 * (x + x.T)
    q -= np.eye(3) * np.trace(q) / 3.0
    return q


def stf_inner(a: np.ndarray, b: np.ndarray) -> complex:
    return np.sum(np.conj(a) * b)


def field_coupling_matrix(qs, points, weights) -> np.ndarray:
    """Discretized raw TT angular coupling G.

    The sqrt(5/8pi) normalization is chosen so that G^dagger G equals the STF
    Gram matrix Q_m^*:Q_n under exact angular integration.
    """
    factor = math.sqrt(5.0 / (8.0 * math.pi))
    rows = []
    for n, weight in zip(points, weights):
        eps_plus, eps_cross = polarizations(n)
        for eps in (eps_plus, eps_cross):
            rows.append(
                math.sqrt(weight)
                * factor
                * np.asarray([np.sum(q * eps) for q in qs], dtype=complex)
            )
    return np.asarray(rows)


def psd_sqrt_and_inverse(a: np.ndarray, tol: float = 1e-11):
    h = 0.5 * (a + a.conj().T)
    vals, vecs = np.linalg.eigh(h)
    vals = np.real(vals)
    assert np.min(vals) > -1e-10
    clipped = np.clip(vals, 0.0, None)
    sqrt_a = (vecs * np.sqrt(clipped)) @ vecs.conj().T
    inv_diag = np.zeros_like(clipped)
    inv_diag[clipped > tol] = 1.0 / np.sqrt(clipped[clipped > tol])
    inv_sqrt = (vecs * inv_diag) @ vecs.conj().T
    support = (vecs * (clipped > tol).astype(float)) @ vecs.conj().T
    return sqrt_a, inv_sqrt, support


def check_one_case(n_a: int, n_b: int, z: float) -> tuple[float, float, float]:
    points, weights = sphere_quadrature()

    # Deliberately produce strongly overlapping patterns by mixing a few base
    # quadrupoles rather than drawing every matter mode independently.
    bases_a = [random_stf() for _ in range(max(2, min(3, n_a)))]
    bases_b = [random_stf() for _ in range(max(2, min(3, n_b)))]

    def mixed_modes(n_modes, bases):
        out = []
        for _ in range(n_modes):
            coeff = RNG.normal(size=len(bases)) + 1j * RNG.normal(size=len(bases))
            out.append(sum(c * q for c, q in zip(coeff, bases)))
        return out

    qs_a = mixed_modes(n_a, bases_a)
    qs_b = mixed_modes(n_b, bases_b)

    g_a = field_coupling_matrix(qs_a, points, weights)
    g_b = field_coupling_matrix(qs_b, points, weights)

    gamma_a = g_a.conj().T @ g_a
    gamma_b = g_b.conj().T @ g_b

    expected_a = np.asarray([[stf_inner(qi, qj) for qj in qs_a] for qi in qs_a])
    expected_b = np.asarray([[stf_inner(qi, qj) for qj in qs_b] for qi in qs_b])

    gram_err = max(
        float(np.max(np.abs(gamma_a - expected_a))),
        float(np.max(np.abs(gamma_b - expected_b))),
    )

    sqrt_a, inv_a, support_a = psd_sqrt_and_inverse(gamma_a)
    sqrt_b, inv_b, support_b = psd_sqrt_and_inverse(gamma_b)
    v_a = g_a @ inv_a
    v_b = g_b @ inv_b

    iso_err = max(
        float(np.max(np.abs(v_a.conj().T @ v_a - support_a))),
        float(np.max(np.abs(v_b.conj().T @ v_b - support_b))),
    )

    # Free fixed-frequency translation along +z. The angular phase is unit
    # modulus, so U is exactly unitary in the discretized field space.
    phase = np.repeat(np.exp(1j * z * points[:, 2]), 2)

    direct = g_b.conj().T @ (phase[:, None] * g_a)
    p_g = v_b.conj().T @ (phase[:, None] * v_a)
    reconstructed = sqrt_b @ p_g @ sqrt_a

    factor_err = float(np.max(np.abs(direct - reconstructed)))
    p_norm = float(np.linalg.svd(p_g, compute_uv=False)[0])
    assert p_norm <= 1.0 + 2e-10

    # Trace resource equals summed raw pattern norms in any orthonormal matter
    # basis; nonorthogonality appears in off-diagonal Gamma entries, not as an
    # extra coupling resource.
    trace_a = float(np.real(np.trace(gamma_a)))
    raw_a = float(sum(np.real(stf_inner(q, q)) for q in qs_a))
    assert math.isclose(trace_a, raw_a, rel_tol=3e-10, abs_tol=3e-10)

    return gram_err, iso_err, factor_err


def main() -> None:
    worst_gram = 0.0
    worst_iso = 0.0
    worst_factor = 0.0

    for _ in range(80):
        # Keep <=3 independent STF bases so some realizations are rank
        # deficient when n_modes > 3; the support-projector form must still work.
        n_a = int(RNG.integers(1, 6))
        n_b = int(RNG.integers(1, 6))
        z = float(RNG.uniform(0.1, 30.0))
        ge, ie, fe = check_one_case(n_a, n_b, z)
        worst_gram = max(worst_gram, ge)
        worst_iso = max(worst_iso, ie)
        worst_factor = max(worst_factor, fe)

    assert worst_gram < 2e-10
    assert worst_iso < 2e-9
    assert worst_factor < 2e-8

    print(
        "gravitational port factorization: PASS "
        f"(worst Gram={worst_gram:.3e}, "
        f"partial-isometry={worst_iso:.3e}, "
        f"factorization={worst_factor:.3e})"
    )


if __name__ == "__main__":
    main()
