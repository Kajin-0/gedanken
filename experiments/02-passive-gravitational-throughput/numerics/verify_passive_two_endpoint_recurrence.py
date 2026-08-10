import numpy as np
from scipy.linalg import svdvals


def random_contraction(rng, n, norm_ceiling=1.0):
    z = (rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))) / np.sqrt(2.0)
    u, s, vh = np.linalg.svd(z)
    # Random singular values in [0, norm_ceiling], with at least one close to the ceiling.
    vals = norm_ceiling * rng.uniform(0.0, 1.0, size=n)
    vals[0] = norm_ceiling * rng.uniform(0.85, 1.0)
    return u @ np.diag(vals) @ vh


def scale_to_norm(m, target):
    smax = svdvals(m)[0]
    return m * (target / smax)


def random_matrix_with_norm(rng, n, target):
    z = (rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))) / np.sqrt(2.0)
    return scale_to_norm(z, target)


def opnorm(m):
    return float(svdvals(m)[0])


def effective_propagation(p_plus, p_minus, r_a, r_b):
    n = p_plus.shape[0]
    loop = p_plus @ r_a @ p_minus @ r_b
    return np.linalg.solve(np.eye(n, dtype=complex) - loop, p_plus)


def main():
    rng = np.random.default_rng(20260810)
    c_power = 25.0 / 16.0
    c_amp = np.sqrt(c_power)  # 5/4

    worst_norm_ratio = 0.0
    worst_scaled_power = 0.0

    # Random matrix adversary over increasingly separated links.
    for z in [4.0, 6.0, 10.0, 20.0, 40.0, 80.0]:
        p_target = c_amp / z
        for n in [1, 2, 4]:
            for _ in range(80):
                p_plus = random_matrix_with_norm(rng, n, p_target * rng.uniform(0.5, 1.0))
                p_minus = random_matrix_with_norm(rng, n, p_target * rng.uniform(0.5, 1.0))
                r_a = random_contraction(rng, n)
                r_b = random_contraction(rng, n)

                pp = opnorm(p_plus)
                pm = opnorm(p_minus)
                if pp * pm >= 1.0:
                    raise AssertionError(("test outside convergent loop regime", z, pp, pm))

                p_eff = effective_propagation(p_plus, p_minus, r_a, r_b)
                actual = opnorm(p_eff)
                ceiling = pp / (1.0 - pp * pm)
                ratio = actual / ceiling
                worst_norm_ratio = max(worst_norm_ratio, ratio)

                if actual > ceiling * (1.0 + 2e-11):
                    raise AssertionError((z, n, "recurrence norm bound", actual, ceiling))

                scaled_power = z**2 * actual**2
                worst_scaled_power = max(worst_scaled_power, scaled_power)

    # Scalar aligned-reflection case saturates the resolvent norm bound exactly.
    scalar_errors = []
    scaled_scalar = []
    for z in [4.0, 6.0, 10.0, 20.0, 40.0, 80.0, 160.0]:
        p = c_amp / z
        p_plus = np.array([[p]], dtype=complex)
        p_minus = np.array([[p]], dtype=complex)
        r_a = np.array([[1.0]], dtype=complex)
        r_b = np.array([[1.0]], dtype=complex)
        p_eff = effective_propagation(p_plus, p_minus, r_a, r_b)
        actual = opnorm(p_eff)
        exact_ceiling = p / (1.0 - p**2)
        scalar_errors.append(abs(actual - exact_ceiling))
        scaled_scalar.append(z**2 * actual**2)
        if not np.isclose(actual, exact_ceiling, rtol=2e-14, atol=2e-14):
            raise AssertionError(("scalar saturation", z, actual, exact_ceiling))

    # The scaled recurrent power must approach the same leading 25/16 coefficient.
    asymptotic_error = abs(scaled_scalar[-1] - c_power)
    if asymptotic_error > 4.0e-4:
        raise AssertionError(("leading coefficient convergence", scaled_scalar[-1], c_power))

    # Check the ceiling expansion: eta/(1-eta)^2 - eta is O(eta^2).
    expansion_ratios = []
    for z in [10.0, 20.0, 40.0, 80.0, 160.0]:
        eta = c_power / z**2
        rec_ceiling = eta / (1.0 - eta) ** 2
        ratio = (rec_ceiling - eta) / eta**2
        expansion_ratios.append(ratio)
        if not (1.9 < ratio < 2.2):
            raise AssertionError(("recurrence upper-ceiling expansion", z, ratio))

    print(f"worst random ||P_eff|| / resolvent ceiling ratio = {worst_norm_ratio:.12g}")
    print(f"largest random z^2 ||P_eff||^2 = {worst_scaled_power:.12g}")
    print(f"largest scalar saturation absolute error = {max(scalar_errors):.12g}")
    print(f"scalar z=160 scaled power = {scaled_scalar[-1]:.12g}")
    print(f"target leading coefficient 25/16 = {c_power:.12g}")
    print(f"z=160 leading-coefficient absolute error = {asymptotic_error:.12g}")
    print(f"recurrence ceiling correction / eta^2 at z=160 = {expansion_ratios[-1]:.12g}")
    print("PASS: passive two-endpoint recurrence leaves leading 25/16 coefficient unchanged")


if __name__ == "__main__":
    main()
