import numpy as np


def influence_tensor(x):
    """Return g[i,j,k] = delta_ik x_j + delta_jk x_i - 2/3 delta_ij x_k."""
    g = np.zeros((3, 3, 3), dtype=float)
    for i in range(3):
        for j in range(3):
            for k in range(3):
                g[i, j, k] = (
                    (1.0 if i == k else 0.0) * x[j]
                    + (1.0 if j == k else 0.0) * x[i]
                    - (2.0 / 3.0) * (1.0 if i == j else 0.0) * x[k]
                )
    return g


def center_of_mass_positions(masses, positions):
    total = masses.sum()
    com = np.sum(masses[:, None] * positions, axis=0) / total
    return positions - com


def random_mass_orthonormal_basis(rng, masses, n_modes=None):
    """Return modes w[m,a,k] with sum_a m_a w_m.w_n = delta_mn."""
    n_atoms = len(masses)
    dim = 3 * n_atoms
    if n_modes is None:
        n_modes = dim

    # Euclidean orthonormal vectors y correspond to w = M^{-1/2} y.
    z = rng.normal(size=(dim, n_modes))
    q, _ = np.linalg.qr(z, mode="reduced")
    inv_sqrt_m = np.repeat(1.0 / np.sqrt(masses), 3)
    w_flat = inv_sqrt_m[:, None] * q
    return w_flat.T.reshape(n_modes, n_atoms, 3)


def modal_quadrupoles(masses, positions, modes):
    n_modes = modes.shape[0]
    q = np.zeros((n_modes, 3, 3), dtype=float)
    for n in range(n_modes):
        for a, (m, x) in enumerate(zip(masses, positions)):
            w = modes[n, a]
            q[n] += m * (
                np.outer(w, x)
                + np.outer(x, w)
                - (2.0 / 3.0) * np.eye(3) * np.dot(w, x)
            )
    return q


def main():
    rng = np.random.default_rng(20260810)

    worst_tensor_abs = 0.0
    worst_bessel_ratio = 0.0
    worst_full_parseval_abs = 0.0
    worst_unitary_abs = 0.0
    worst_linewidth_ratio = 0.0

    # Pointwise tensor identity.
    for _ in range(500):
        x = rng.normal(size=3)
        lhs = np.sum(influence_tensor(x) ** 2)
        rhs = (20.0 / 3.0) * np.dot(x, x)
        err = abs(lhs - rhs)
        worst_tensor_abs = max(worst_tensor_abs, err)
        if not np.isclose(lhs, rhs, rtol=5e-14, atol=5e-14):
            raise AssertionError(("20/3 tensor identity", lhs, rhs))

    # Discrete-mass realizations exercise Bessel/Parseval and the linewidth sum.
    for case in range(80):
        n_atoms = 3 + (case % 6)
        masses = np.exp(rng.normal(scale=0.7, size=n_atoms))
        positions = center_of_mass_positions(masses, rng.normal(size=(n_atoms, 3)))
        i2 = float(np.sum(masses * np.sum(positions**2, axis=1)))
        if i2 <= 1e-14:
            continue

        dim = 3 * n_atoms
        full_modes = random_mass_orthonormal_basis(rng, masses, dim)
        q_full = modal_quadrupoles(masses, positions, full_modes)
        strength_full = float(np.sum(q_full**2))
        expected = (20.0 / 3.0) * i2
        parseval_err = abs(strength_full - expected)
        worst_full_parseval_abs = max(worst_full_parseval_abs, parseval_err)
        if not np.isclose(strength_full, expected, rtol=2e-12, atol=2e-12):
            raise AssertionError((case, "complete-basis Parseval", strength_full, expected))

        n_modes = 1 + (case * 7) % dim
        modes = random_mass_orthonormal_basis(rng, masses, n_modes)
        q_modes = modal_quadrupoles(masses, positions, modes)
        strength = float(np.sum(q_modes**2))
        ratio = strength / expected
        worst_bessel_ratio = max(worst_bessel_ratio, ratio)
        if strength > expected * (1 + 2e-12):
            raise AssertionError((case, "Bessel bound", strength, expected))

        # Unitary/orthogonal mixing of retained modes leaves the total strength invariant.
        z = rng.normal(size=(n_modes, n_modes))
        u, _ = np.linalg.qr(z)
        mixed_modes = np.einsum("mn,nak->mak", u, modes)
        q_mixed = modal_quadrupoles(masses, positions, mixed_modes)
        mixed_strength = float(np.sum(q_mixed**2))
        mix_err = abs(mixed_strength - strength)
        worst_unitary_abs = max(worst_unitary_abs, mix_err)
        if not np.isclose(mixed_strength, strength, rtol=3e-12, atol=3e-12):
            raise AssertionError((case, "mixing invariance", mixed_strength, strength))

        # Set G=c=Omega=1. For mass-normalized modes mu_n=1,
        # sum kappa_n = (1/5) sum omega_n^4 (q_n:q_n) <= (4/3) I2.
        omega = rng.random(n_modes)  # each <= Omega = 1
        qnorm = np.sum(q_modes**2, axis=(1, 2))
        sum_kappa = float(np.sum((omega**4) * qnorm) / 5.0)
        linewidth_bound = (4.0 / 3.0) * i2
        linewidth_ratio = sum_kappa / linewidth_bound
        worst_linewidth_ratio = max(worst_linewidth_ratio, linewidth_ratio)
        if sum_kappa > linewidth_bound * (1 + 2e-12):
            raise AssertionError((case, "4/3 linewidth bound", sum_kappa, linewidth_bound))

    print(f"worst 20/3 tensor absolute error = {worst_tensor_abs:.12g}")
    print(f"worst truncated Bessel ratio = {worst_bessel_ratio:.12g}")
    print(f"worst full-basis Parseval absolute error = {worst_full_parseval_abs:.12g}")
    print(f"worst modal-mixing invariance absolute error = {worst_unitary_abs:.12g}")
    print(f"worst cumulative linewidth/(4 I2/3) ratio = {worst_linewidth_ratio:.12g}")
    print("PASS: gravitational endpoint quadrupole resource")


if __name__ == "__main__":
    main()
