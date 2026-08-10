import numpy as np
from scipy.integrate import quad


def random_complex(rng, shape):
    return (rng.normal(size=shape) + 1j * rng.normal(size=shape)) / np.sqrt(2.0)


def scaled_coupling(rng, rows, n, trace_target):
    k = random_complex(rng, (rows, n)) / np.sqrt(n)
    tr = float(np.real(np.trace(k.conj().T @ k)))
    if tr <= 0:
        raise RuntimeError("zero random coupling trace")
    return k * np.sqrt(trace_target / tr)


def endpoint(rng, n, local_ports, gravitational_ports, gravitational_budget):
    x = random_complex(rng, (n, n))
    h = 0.5 * (x + x.conj().T) / np.sqrt(n)

    k_local = 0.55 * random_complex(rng, (local_ports, n)) / np.sqrt(n)
    fraction = rng.uniform(0.15, 1.0)
    k_g = scaled_coupling(
        rng,
        gravitational_ports,
        n,
        fraction * gravitational_budget,
    )
    k_hidden = 0.25 * np.eye(n, dtype=complex)
    k_all = np.vstack([k_local, k_g, k_hidden])
    a = -1j * h - 0.5 * k_all.conj().T @ k_all
    return a, k_local, k_g


def transfer(a, k_out, k_in, nu):
    n = a.shape[0]
    return -k_out @ np.linalg.solve(1j * nu * np.eye(n) - a, k_in.conj().T)


def random_unitary(rng, n):
    x = random_complex(rng, (n, n))
    q, r = np.linalg.qr(x)
    phases = np.diag(r)
    phases = np.where(np.abs(phases) > 0, phases / np.abs(phases), 1.0)
    return q @ np.diag(np.conj(phases))


def resource(k):
    return float(np.real(np.trace(k.conj().T @ k)))


def main():
    rng = np.random.default_rng(20260810)

    # Dimensionless validation units: G = c = omega_0 = k_0 = 1.
    # Stage B: R_g <= (4/3) I2.
    # Stage C: eta <= 25/(16 R^2).
    # Combined: Gamma <= 25/(12 R^2) min(I2_A, I2_B).
    worst_ratio = 0.0
    worst_resource_fraction = 0.0
    worst_propagation_fraction = 0.0

    for case in range(16):
        i_a = np.exp(rng.normal(scale=0.8))
        i_b = np.exp(rng.normal(scale=0.8))
        budget_a = (4.0 / 3.0) * i_a
        budget_b = (4.0 / 3.0) * i_b

        gravitational_ports = 2
        a, k_u, k_ga = endpoint(
            rng,
            n=4 + (case % 2),
            local_ports=2,
            gravitational_ports=gravitational_ports,
            gravitational_budget=budget_a,
        )
        b, k_y, k_gb = endpoint(
            rng,
            n=5 - (case % 2),
            local_ports=2,
            gravitational_ports=gravitational_ports,
            gravitational_budget=budget_b,
        )

        r_sep = 4.0 + 0.9 * case
        eta_max = 25.0 / (16.0 * r_sep**2)
        eta_fraction = rng.uniform(0.1, 1.0)
        p = np.sqrt(eta_fraction * eta_max) * random_unitary(rng, gravitational_ports)

        def integrand(nu):
            h_a = transfer(a, k_ga, k_u, nu)
            h_b = transfer(b, k_y, k_gb, nu)
            t = h_b @ p @ h_a
            return np.linalg.norm(t, "fro") ** 2 / (2.0 * np.pi)

        gamma, error = quad(
            integrand,
            -np.inf,
            np.inf,
            epsabs=2e-9,
            epsrel=2e-8,
            limit=350,
        )

        final_bound = (25.0 / (12.0 * r_sep**2)) * min(i_a, i_b)
        ratio = gamma / final_bound
        worst_ratio = max(worst_ratio, ratio)

        res_frac_a = resource(k_ga) / budget_a
        res_frac_b = resource(k_gb) / budget_b
        worst_resource_fraction = max(worst_resource_fraction, res_frac_a, res_frac_b)
        worst_propagation_fraction = max(worst_propagation_fraction, eta_fraction)

        if res_frac_a > 1 + 1e-12 or res_frac_b > 1 + 1e-12:
            raise AssertionError((case, "Stage-B budget construction", res_frac_a, res_frac_b))

        if gamma > final_bound + max(5e-8 * final_bound, 20.0 * error):
            raise AssertionError((case, "combined 25/12 bound", gamma, final_bound, error))

    print(f"worst actual Gamma/(25 min(I2)/(12 R^2)) ratio = {worst_ratio:.12g}")
    print(f"largest endpoint resource/budget fraction = {worst_resource_fraction:.12g}")
    print(f"largest propagation/TT-ceiling fraction = {worst_propagation_fraction:.12g}")
    print("PASS: finite-dimensional narrowband two-ended 25/12 inertia bound")


if __name__ == "__main__":
    main()
