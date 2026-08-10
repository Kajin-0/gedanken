import numpy as np
from scipy.integrate import quad
from scipy.linalg import solve_continuous_lyapunov, svdvals


def random_coupling(rng, rows, n, scale):
    z = rng.normal(size=(rows, n)) + 1j * rng.normal(size=(rows, n))
    return scale * z / np.sqrt(2 * n)


def random_endpoint(rng, n, local_ports, gravitational_ports):
    x = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    h = (x + x.conj().T) / (2 * np.sqrt(n))

    k_local = random_coupling(rng, local_ports, n, 0.7)
    k_g = random_coupling(rng, gravitational_ports, n, 0.7)

    # Hidden passive channels guarantee damping while remaining part of the
    # physical dilation. They are retained in the full scattering matrix.
    k_hidden = 0.35 * np.eye(n, dtype=complex)
    k_all = np.vstack([k_local, k_g, k_hidden])

    a = -1j * h - 0.5 * k_all.conj().T @ k_all
    return a, k_local, k_g, k_all


def cross_transfer(a, k_out, k_in, omega):
    n = a.shape[0]
    return -k_out @ np.linalg.solve(1j * omega * np.eye(n) - a, k_in.conj().T)


def full_scattering(a, k_all, omega):
    n = a.shape[0]
    return np.eye(k_all.shape[0]) - k_all @ np.linalg.solve(
        1j * omega * np.eye(n) - a, k_all.conj().T
    )


def h2_exact(a, k_out, k_in):
    # A P + P A^dagger + K_in^dagger K_in = 0
    p = solve_continuous_lyapunov(a, -(k_in.conj().T @ k_in))
    value = np.trace(k_out @ p @ k_out.conj().T)
    return float(np.real(value))


def resource(k):
    return float(np.real(np.trace(k.conj().T @ k)))


def random_unitary(rng, n):
    x = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    u, _, vh = np.linalg.svd(x)
    return u @ vh


def main():
    rng = np.random.default_rng(20260810)

    worst_endpoint_ratio = 0.0
    worst_scattering_sv = 0.0
    worst_link_ratio = 0.0

    for case in range(12):
        gravitational_ports = 2

        a, k_u, k_ga, k_a_all = random_endpoint(
            rng,
            n=4 + (case % 2),
            local_ports=2,
            gravitational_ports=gravitational_ports,
        )
        b, k_y, k_gb, k_b_all = random_endpoint(
            rng,
            n=5 - (case % 2),
            local_ports=2,
            gravitational_ports=gravitational_ports,
        )

        # Exact finite-dimensional H2 cuts from Lyapunov Gramians.
        h2_a = h2_exact(a, k_ga, k_u)
        h2_b = h2_exact(b, k_y, k_gb)

        bound_a = min(resource(k_u), resource(k_ga))
        bound_b = min(resource(k_gb), resource(k_y))

        ratio_a = h2_a / bound_a
        ratio_b = h2_b / bound_b
        worst_endpoint_ratio = max(worst_endpoint_ratio, ratio_a, ratio_b)

        if h2_a > bound_a * (1 + 1e-10):
            raise AssertionError((case, "source H2 cut", h2_a, bound_a))
        if h2_b > bound_b * (1 + 1e-10):
            raise AssertionError((case, "receiver H2 cut", h2_b, bound_b))

        # Full passive scattering must be unitary here because every loss
        # channel has been included explicitly.
        for omega in np.linspace(-8.0, 8.0, 41):
            sigma_a = svdvals(full_scattering(a, k_a_all, omega))[0]
            sigma_b = svdvals(full_scattering(b, k_b_all, omega))[0]
            worst_scattering_sv = max(worst_scattering_sv, sigma_a, sigma_b)

            if sigma_a > 1 + 2e-10 or sigma_b > 1 + 2e-10:
                raise AssertionError((case, "passive scattering contraction", omega))

        # Random separated propagation contraction.
        eta = 0.04 + 0.025 * case
        p = np.sqrt(eta) * random_unitary(rng, gravitational_ports)

        def integrand(omega):
            h_a = cross_transfer(a, k_ga, k_u, omega)
            h_b = cross_transfer(b, k_y, k_gb, omega)
            t = h_b @ p @ h_a
            return np.linalg.norm(t, "fro") ** 2 / (2 * np.pi)

        gamma, quad_error = quad(
            integrand,
            -np.inf,
            np.inf,
            epsabs=3e-9,
            epsrel=3e-8,
            limit=300,
        )

        link_bound = eta * min(resource(k_ga), resource(k_gb))
        link_ratio = gamma / link_bound
        worst_link_ratio = max(worst_link_ratio, link_ratio)

        if gamma > link_bound + max(5e-8 * link_bound, 20 * quad_error):
            raise AssertionError((case, "two-ended cut", gamma, link_bound, quad_error))

    print(f"worst endpoint H2/resource ratio = {worst_endpoint_ratio:.12g}")
    print(f"largest full-scattering singular value = {worst_scattering_sv:.12g}")
    print(f"worst two-ended Gamma/bound ratio = {worst_link_ratio:.12g}")
    print("PASS: finite-dimensional passive selected-port cut")


if __name__ == "__main__":
    main()
