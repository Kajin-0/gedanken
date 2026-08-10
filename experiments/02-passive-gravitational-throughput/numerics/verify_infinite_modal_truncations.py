import numpy as np
from scipy.linalg import solve_continuous_lyapunov
from scipy.special import zeta


def fixed_ports(n):
    idx = np.arange(1, n + 1, dtype=float)

    # Both selected local rows are l2 sequences, so the limiting operator
    # from the modal l2 space to C^2 is bounded.
    ku = np.vstack(
        [
            0.50 / idx**0.80,
            0.37 * np.exp(0.31j * idx) / idx**0.90,
        ]
    ).astype(complex)

    # Gravitational rows are square summable; K_g is Hilbert-Schmidt and its
    # trace resource has an analytic infinite-N limit.
    kg = np.vstack(
        [
            0.19 / idx**1.10,
            0.13 * (-1.0) ** np.arange(n) / idx**1.10,
        ]
    ).astype(complex)
    return ku, kg


def hamiltonian(n):
    # Increasing diagonal mimics an unbounded modal frequency operator;
    # bounded nearest-neighbor mixing prevents a trivial commuting example.
    diag = 0.55 * np.arange(1, n + 1, dtype=float)
    h = np.diag(diag).astype(complex)
    if n > 1:
        off = 0.08 * np.ones(n - 1)
        h += np.diag(off, 1) + np.diag(off, -1)
    return h


def build_system(n):
    ku, kg = fixed_ports(n)
    kh = 0.32 * np.eye(n, dtype=complex)  # bounded hidden passive port
    k_all = np.vstack([ku, kg, kh])
    h = hamiltonian(n)
    a = -1j * h - 0.5 * k_all.conj().T @ k_all
    return a, ku, kg


def resource(kg):
    return float(np.real(np.trace(kg.conj().T @ kg)))


def gramian(a, ku):
    b = ku.conj().T @ ku
    p = solve_continuous_lyapunov(a, -b)
    return 0.5 * (p + p.conj().T)


def h2_from_p(p, kg):
    return float(np.real(np.trace(kg @ p @ kg.conj().T)))


def random_unitary(rng, n):
    z = (rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))) / np.sqrt(2.0)
    q, r = np.linalg.qr(z)
    phase = np.diag(r)
    phase = np.where(np.abs(phase) > 0, phase / np.abs(phase), 1.0)
    return q @ np.diag(np.conj(phase))


def main():
    rng = np.random.default_rng(20260810)
    ns = [8, 16, 32, 64]

    analytic_trace_limit = (0.19**2 + 0.13**2) * float(zeta(2.20, 1.0))

    worst_p_eig = 0.0
    worst_h2_ratio = 0.0
    trace_errors = []

    for n in ns:
        a, ku, kg = build_system(n)
        p = gramian(a, ku)
        evals = np.linalg.eigvalsh(p)
        lam_max = float(evals[-1])
        worst_p_eig = max(worst_p_eig, lam_max)
        if lam_max > 1.0 + 5e-10:
            raise AssertionError((n, "P_u <= I", lam_max))
        if evals[0] < -5e-10:
            raise AssertionError((n, "P_u >= 0", evals[0]))

        r_g = resource(kg)
        h2 = h2_from_p(p, kg)
        ratio = h2 / r_g
        worst_h2_ratio = max(worst_h2_ratio, ratio)
        if h2 > r_g * (1.0 + 5e-10):
            raise AssertionError((n, "H2 gravitational trace cut", h2, r_g))

        trace_error = analytic_trace_limit - r_g
        if trace_error < -5e-13:
            raise AssertionError((n, "truncated trace exceeds infinite limit", r_g, analytic_trace_limit))
        trace_errors.append(trace_error)

    if any(trace_errors[i + 1] > trace_errors[i] + 5e-13 for i in range(len(trace_errors) - 1)):
        raise AssertionError(("trace tail not converging", trace_errors))

    # Basis-invariance stress test on a nontrivial truncation.
    n = 24
    a, ku, kg = build_system(n)
    p = gramian(a, ku)
    base_resource = resource(kg)
    base_h2 = h2_from_p(p, kg)

    u = random_unitary(rng, n)
    a_m = u.conj().T @ a @ u
    ku_m = ku @ u
    kg_m = kg @ u
    p_m = gramian(a_m, ku_m)
    mixed_resource = resource(kg_m)
    mixed_h2 = h2_from_p(p_m, kg_m)

    resource_mix_error = abs(mixed_resource - base_resource)
    h2_mix_error = abs(mixed_h2 - base_h2)
    if not np.isclose(mixed_resource, base_resource, rtol=2e-11, atol=2e-12):
        raise AssertionError(("resource basis invariance", mixed_resource, base_resource))
    if not np.isclose(mixed_h2, base_h2, rtol=2e-10, atol=2e-11):
        raise AssertionError(("H2 basis invariance", mixed_h2, base_h2))

    print(f"analytic infinite gravitational trace limit = {analytic_trace_limit:.12g}")
    print(f"N=64 gravitational trace = {resource(fixed_ports(64)[1]):.12g}")
    print(f"N=64 trace tail = {trace_errors[-1]:.12g}")
    print(f"largest lambda_max(P_u) = {worst_p_eig:.12g}")
    print(f"worst H2/gravitational-resource ratio = {worst_h2_ratio:.12g}")
    print(f"modal-mixing resource error = {resource_mix_error:.12g}")
    print(f"modal-mixing H2 error = {h2_mix_error:.12g}")
    print("PASS: countably-infinite bounded-port truncation stress test")


if __name__ == "__main__":
    main()
