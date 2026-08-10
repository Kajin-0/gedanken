"""Independent regression for the classical quadrupole modal-completeness bound.

Checks
------
1. Pointwise tensor identity
       sum_{i,j,k} |g^{ij}_k|^2 = (20/3) r^2.
2. Mass-weighted Bessel inequality for random retained mode subspaces
       sum_n q_n:q_n / mu_n <= (20/3) I,
   equivalently
       sum_n M A_Gn <= (40/3) I.
3. Parseval saturation for a complete displacement basis.
4. Orthogonality of the quadrupole-gradient fields to rigid translations when
   the spatial origin is the center of mass.
5. Exact Hirakawa effective-area <-> one-quantum linewidth normalization.

The random-subspace test is deliberately independent of any elastic stiffness
matrix: the theorem is a Hilbert-space completeness/Bessel statement, so any
orthonormal retained displacement subspace must satisfy it.
"""

from __future__ import annotations

import numpy as np


RNG = np.random.default_rng(20260809)
RTOL = 2.0e-12
ATOL = 2.0e-12


def build_g_matrix(positions: np.ndarray, masses: np.ndarray) -> np.ndarray:
    """Return mass-weighted quadrupole-gradient fields as columns.

    Rows are the 3N mass-weighted displacement coordinates. The nine columns
    correspond to Cartesian tensor components (i,j). Although only five STF
    combinations are independent, summing all Cartesian components is exactly
    the Frobenius contraction q:q used in the analytic proof.
    """

    npts = positions.shape[0]
    sqrt_m = np.sqrt(masses)
    G = np.zeros((3 * npts, 9), dtype=float)

    col = 0
    for i in range(3):
        for j in range(3):
            field = np.zeros((npts, 3), dtype=float)
            for a in range(npts):
                x = positions[a]
                for k in range(3):
                    field[a, k] = (
                        (1.0 if i == k else 0.0) * x[j]
                        + (1.0 if j == k else 0.0) * x[i]
                        - (2.0 / 3.0)
                        * (1.0 if i == j else 0.0)
                        * x[k]
                    )
            G[:, col] = (sqrt_m[:, None] * field).reshape(-1)
            col += 1

    return G


def random_centered_body(npts: int) -> tuple[np.ndarray, np.ndarray]:
    masses = np.exp(RNG.normal(scale=0.7, size=npts))
    positions = RNG.normal(size=(npts, 3))
    center = np.sum(masses[:, None] * positions, axis=0) / np.sum(masses)
    positions -= center
    return positions, masses


def check_pointwise_identity() -> float:
    max_rel = 0.0
    for _ in range(500):
        x = RNG.normal(size=3)
        positions = x[None, :]
        masses = np.ones(1)
        G = build_g_matrix(positions, masses)
        lhs = np.sum(G * G)
        rhs = (20.0 / 3.0) * np.dot(x, x)
        rel = abs(lhs - rhs) / max(abs(rhs), 1.0)
        max_rel = max(max_rel, rel)
        if not np.isclose(lhs, rhs, rtol=RTOL, atol=ATOL):
            raise AssertionError(f"Pointwise 20/3 identity failed: {lhs=} {rhs=}")
    return max_rel


def rigid_translation_vectors(masses: np.ndarray) -> np.ndarray:
    npts = len(masses)
    sqrt_m = np.sqrt(masses)
    V = np.zeros((3 * npts, 3))
    for axis in range(3):
        field = np.zeros((npts, 3))
        field[:, axis] = 1.0
        V[:, axis] = (sqrt_m[:, None] * field).reshape(-1)
    return V


def check_random_bessel_trials(ntrials: int = 400) -> tuple[float, float, float]:
    max_fraction = 0.0
    max_identity_rel = 0.0
    max_translation_overlap = 0.0

    for _ in range(ntrials):
        npts = int(RNG.integers(4, 18))
        positions, masses = random_centered_body(npts)
        G = build_g_matrix(positions, masses)

        inertia = np.sum(masses * np.sum(positions * positions, axis=1))
        total = np.sum(G * G)
        target = (20.0 / 3.0) * inertia
        rel = abs(total - target) / max(abs(target), 1.0)
        max_identity_rel = max(max_identity_rel, rel)
        if not np.isclose(total, target, rtol=RTOL, atol=ATOL):
            raise AssertionError(
                f"Discrete mass-weighted 20/3 identity failed: {total=} {target=}"
            )

        # Complete displacement basis: exact Parseval saturation.
        complete = np.eye(3 * npts)
        complete_resource = np.sum((complete.T @ G) ** 2)
        if not np.isclose(complete_resource, target, rtol=RTOL, atol=ATOL):
            raise AssertionError("Complete-basis Parseval saturation failed")

        # Random retained orthonormal modal subspace: Bessel inequality.
        dim = int(RNG.integers(1, 3 * npts + 1))
        X = RNG.normal(size=(3 * npts, dim))
        U, _ = np.linalg.qr(X, mode="reduced")
        retained = np.sum((U.T @ G) ** 2)
        fraction = retained / target
        max_fraction = max(max_fraction, fraction)
        if retained > target * (1.0 + 5.0e-12) + 5.0e-12:
            raise AssertionError(
                f"Bessel bound violated: retained={retained}, target={target}"
            )

        # Hirakawa effective-area form: M A_G = 2 q:q/mu.
        # In mass-weighted orthonormal coordinates each retained mode has mu=1.
        effective_area_weight = 2.0 * retained
        effective_area_ceiling = (40.0 / 3.0) * inertia
        if effective_area_weight > effective_area_ceiling * (1.0 + 5.0e-12):
            raise AssertionError("Classical effective-area sum-rule bound violated")

        # At the CM origin, rigid translations have zero linear quadrupole overlap.
        translations = rigid_translation_vectors(masses)
        overlaps = translations.T @ G
        scale = max(np.linalg.norm(translations) * np.linalg.norm(G), 1.0)
        translation_rel = np.max(np.abs(overlaps)) / scale
        max_translation_overlap = max(max_translation_overlap, translation_rel)
        if translation_rel > 2.0e-12:
            raise AssertionError(
                f"Rigid-translation overlap too large: {translation_rel}"
            )

    return max_fraction, max_identity_rel, max_translation_overlap


def check_hirakawa_quantum_normalization(ntrials: int = 500) -> float:
    """Check kappa_g = G M A_G omega^4/(10 c^5) against quantization.

    Constants are sampled in arbitrary positive units; the equality is
    dimensionless algebra and should hold to floating-point precision.
    """

    max_rel = 0.0
    for _ in range(ntrials):
        M = np.exp(RNG.normal())
        mu = np.exp(RNG.normal())
        omega = np.exp(RNG.normal())
        Gnewton = np.exp(RNG.normal())
        c = np.exp(RNG.normal())
        hbar = np.exp(RNG.normal())

        q = RNG.normal(size=(3, 3))
        q = 0.5 * (q + q.T)
        q -= np.eye(3) * np.trace(q) / 3.0
        qnorm = np.sum(q * q)

        A_G = 2.0 * qnorm / (M * mu)
        Qnorm = qnorm * hbar / (2.0 * mu * omega)

        kappa_quantum = (
            2.0 * Gnewton * omega**5 * Qnorm / (5.0 * hbar * c**5)
        )
        kappa_classical = Gnewton * M * A_G * omega**4 / (10.0 * c**5)

        rel = abs(kappa_quantum - kappa_classical) / max(
            abs(kappa_classical), 1.0e-300
        )
        max_rel = max(max_rel, rel)
        if not np.isclose(kappa_quantum, kappa_classical, rtol=5e-12, atol=0.0):
            raise AssertionError(
                "Hirakawa/quantum linewidth normalization mismatch: "
                f"{kappa_quantum=} {kappa_classical=}"
            )

    return max_rel


def main() -> None:
    pointwise = check_pointwise_identity()
    max_fraction, identity_rel, translation_rel = check_random_bessel_trials()
    linewidth_rel = check_hirakawa_quantum_normalization()

    print("Classical modal sum-rule regression: PASS")
    print(f"  max pointwise 20/3 relative error: {pointwise:.3e}")
    print(f"  max discrete identity relative error: {identity_rel:.3e}")
    print(f"  largest random retained/ceiling fraction: {max_fraction:.12f}")
    print(f"  max rigid-translation normalized overlap: {translation_rel:.3e}")
    print(f"  max A_G <-> kappa_g relative mismatch: {linewidth_rel:.3e}")


if __name__ == "__main__":
    main()
