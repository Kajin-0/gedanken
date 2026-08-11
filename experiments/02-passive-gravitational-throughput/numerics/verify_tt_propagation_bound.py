import numpy as np


def random_stf(rng):
    z = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    q = 0.5 * (z + z.T)
    q -= np.eye(3) * np.trace(q) / 3.0
    return q


def random_direction(rng):
    n = rng.normal(size=3)
    return n / np.linalg.norm(n)


def qnorm(q):
    return float(np.real(np.vdot(q, q)))


def tt_power(q, n):
    qn = q @ n
    nqn = n @ q @ n
    value = qnorm(q) - 2.0 * float(np.real(np.vdot(qn, qn))) + 0.5 * abs(nqn) ** 2
    return float(np.real(value))


def polarization_tensors(mu, phi):
    sin_theta = np.sqrt(max(0.0, 1.0 - mu * mu))
    cphi, sphi = np.cos(phi), np.sin(phi)
    e_theta = np.array([mu * cphi, mu * sphi, -sin_theta])
    e_phi = np.array([-sphi, cphi, 0.0])
    n = np.array([sin_theta * cphi, sin_theta * sphi, mu])
    eps_plus = (np.outer(e_theta, e_theta) - np.outer(e_phi, e_phi)) / np.sqrt(2.0)
    eps_cross = (np.outer(e_theta, e_phi) + np.outer(e_phi, e_theta)) / np.sqrt(2.0)
    return n, eps_plus, eps_cross


def angular_amplitudes(q, n):
    ref = np.array([0.0, 0.0, 1.0])
    if abs(np.dot(n, ref)) > 0.9:
        ref = np.array([1.0, 0.0, 0.0])
    e1 = ref - np.dot(ref, n) * n
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(n, e1)
    eps_plus = (np.outer(e1, e1) - np.outer(e2, e2)) / np.sqrt(2.0)
    eps_cross = (np.outer(e1, e2) + np.outer(e2, e1)) / np.sqrt(2.0)
    amps = np.array([np.sum(q * eps_plus), np.sum(q * eps_cross)], dtype=complex)
    denom = np.sqrt((8.0 * np.pi / 5.0) * qnorm(q))
    return amps / denom


def sphere_integral(q, n_mu=32, n_phi=64):
    mu_nodes, mu_weights = np.polynomial.legendre.leggauss(n_mu)
    total = 0.0
    dphi = 2.0 * np.pi / n_phi
    for mu, wmu in zip(mu_nodes, mu_weights):
        for j in range(n_phi):
            phi = (j + 0.5) * dphi
            n, eps_plus, eps_cross = polarization_tensors(mu, phi)
            f_pol = abs(np.sum(q * eps_plus)) ** 2 + abs(np.sum(q * eps_cross)) ** 2
            f_inv = tt_power(q, n)
            if not np.isclose(f_pol, f_inv, rtol=2e-12, atol=2e-12):
                raise AssertionError(("polarization/TT mismatch", f_pol, f_inv))
            total += wmu * dphi * f_inv
    return total


def finite_sector_kernels(mu):
    k2 = (5.0 / 32.0) * (1.0 + 6.0 * mu**2 + mu**4)
    k1 = (5.0 / 8.0) * (1.0 - mu**2) * (1.0 + mu**2)
    k0 = (15.0 / 16.0) * (1.0 - mu**2) ** 2
    return np.array([k0, k1, k2])


def finite_sector_outgoing_amplitudes(z):
    z = float(z)
    phase = np.exp(1j * z)
    a2 = -(5j / 4.0) * phase * (z**4 + 2j * z**3 - 3 * z**2 - 3j * z + 3) / z**5
    a1 = -(5.0 / 2.0) * phase * (z**3 + 3j * z**2 - 6 * z - 6j) / z**5
    a0 = (15j / 2.0) * phase * (z**2 + 3j * z - 3) / z**5
    return np.array([a0, a1, a2])


def finite_sector_powers(z):
    return np.abs(finite_sector_outgoing_amplitudes(z)) ** 2


def main():
    rng = np.random.default_rng(20260810)

    worst_projector_excess = 0.0
    worst_integral_rel = 0.0
    worst_directivity = 0.0
    worst_overlap_prefactor = 0.0

    for case in range(24):
        q = random_stf(rng)
        qq = qnorm(q)
        if qq <= 1e-14:
            continue

        integral = sphere_integral(q)
        expected = (8.0 * np.pi / 5.0) * qq
        rel = abs(integral - expected) / expected
        worst_integral_rel = max(worst_integral_rel, rel)
        if not np.isclose(integral, expected, rtol=2e-11, atol=2e-11):
            raise AssertionError((case, "8pi/5 normalization", integral, expected))

        for _ in range(120):
            n = random_direction(rng)
            f = tt_power(q, n)
            if f < -2e-12 * qq:
                raise AssertionError((case, "negative TT power", f, qq))
            excess = f / qq - 1.0
            worst_projector_excess = max(worst_projector_excess, excess)
            if f > qq * (1 + 2e-12):
                raise AssertionError((case, "TT projector exceeds norm", f, qq))
            directivity = (5.0 / 2.0) * f / qq
            worst_directivity = max(worst_directivity, directivity)
            if directivity > 2.5 * (1 + 2e-12):
                raise AssertionError((case, "directivity bound", directivity))

        q_b = random_stf(rng)
        for _ in range(120):
            n = random_direction(rng)
            u_a = angular_amplitudes(q, n)
            u_b = angular_amplitudes(q_b, n)
            overlap = abs(np.vdot(u_b, u_a))
            prefactor = 2.0 * np.pi * overlap
            worst_overlap_prefactor = max(worst_overlap_prefactor, prefactor)
            if prefactor > 1.25 * (1 + 3e-12):
                raise AssertionError((case, "stationary-phase amplitude prefactor", prefactor))

    q_plus = np.diag([1.0, -1.0, 0.0]).astype(complex)
    n_z = np.array([0.0, 0.0, 1.0])
    f_z = tt_power(q_plus, n_z)
    d_z = (5.0 / 2.0) * f_z / qnorm(q_plus)
    if not np.isclose(d_z, 2.5, rtol=1e-14, atol=1e-14):
        raise AssertionError(("aligned directivity saturation", d_z))

    u = angular_amplitudes(q_plus, n_z)
    amp_prefactor = 2.0 * np.pi * abs(np.vdot(u, u))
    power_prefactor = amp_prefactor**2
    if not np.isclose(amp_prefactor, 5.0 / 4.0, rtol=2e-14, atol=2e-14):
        raise AssertionError(("5/4 amplitude coefficient", amp_prefactor))
    if not np.isclose(power_prefactor, 25.0 / 16.0, rtol=3e-14, atol=3e-14):
        raise AssertionError(("25/16 power coefficient", power_prefactor))

    # Independent finite-distance check: numerical angular integrals of each
    # normalized m-sector kernel must equal outgoing + incoming exact pieces.
    nodes, weights = np.polynomial.legendre.leggauss(192)
    worst_finite_overlap_error = 0.0
    for z in (0.7, 3.0, 4.3, 10.0, 100.0):
        kernels = np.array([finite_sector_kernels(mu) for mu in nodes]).T
        numeric = np.sum(kernels * (weights * np.exp(1j * z * nodes))[None, :], axis=1)
        outgoing = finite_sector_outgoing_amplitudes(z)
        exact_full = 2.0 * np.real(outgoing)
        err = float(np.max(np.abs(numeric - exact_full)))
        worst_finite_overlap_error = max(worst_finite_overlap_error, err)
        if err > 2e-11:
            raise AssertionError(("finite-z sector overlap", z, numeric, exact_full, err))

    # For z >= 3 the |m|=2 sector is the operator maximum.
    for z in np.geomspace(3.0, 1.0e4, 300):
        eta0, eta1, eta2 = finite_sector_powers(z)
        if eta2 + 2e-14 < max(eta0, eta1):
            raise AssertionError(("m=2 not maximal", z, eta0, eta1, eta2))

    eta0_100, eta1_100, eta2_100 = finite_sector_powers(100.0)
    leading_100 = 25.0 / (16.0 * 100.0**2)
    correction_100 = eta2_100 / leading_100
    expected_correction = 1.0 - 2.0 / 100.0**2 + 3.0 / 100.0**4 - 9.0 / 100.0**6 + 9.0 / 100.0**8
    if not np.isclose(correction_100, expected_correction, rtol=2e-14, atol=2e-14):
        raise AssertionError(("finite-z correction", correction_100, expected_correction))

    print(f"worst TT projector relative excess over q:q = {worst_projector_excess:.12g}")
    print(f"worst 8pi/5 sphere-normalization relative error = {worst_integral_rel:.12g}")
    print(f"largest random directivity = {worst_directivity:.12g}")
    print(f"largest random stationary-phase amplitude prefactor = {worst_overlap_prefactor:.12g}")
    print(f"aligned directivity saturation = {d_z:.12g}")
    print(f"aligned amplitude prefactor = {amp_prefactor:.12g}")
    print(f"aligned power prefactor = {power_prefactor:.12g}")
    print(f"worst exact finite-z sector overlap error = {worst_finite_overlap_error:.12g}")
    print(f"z=100 m=2 correction factor = {correction_100:.12g}")
    print("PASS: compact TT propagation 25/16 asymptotic and finite-z sector bound")


if __name__ == "__main__":
    main()
