import numpy as np
from scipy.integrate import quad

SEED = 20260810


def random_complex(rng, shape):
    return (rng.normal(size=shape) + 1j * rng.normal(size=shape)) / np.sqrt(2.0)


def influence_tensor(x):
    g = np.zeros((3, 3, 3), float)
    for i in range(3):
        for j in range(3):
            for k in range(3):
                g[i, j, k] = (i == k) * x[j] + (j == k) * x[i] - (2 / 3) * (i == j) * x[k]
    return g


def com_positions(m, p):
    return p - np.sum(m[:, None] * p, axis=0) / np.sum(m)


def mass_orthonormal_modes(rng, m, n_modes=None):
    d = 3 * len(m)
    if n_modes is None:
        n_modes = d
    z = rng.normal(size=(d, n_modes))
    q, _ = np.linalg.qr(z, mode="reduced")
    w = np.repeat(1 / np.sqrt(m), 3)[:, None] * q
    return w.T.reshape(n_modes, len(m), 3)


def quadrupoles(m, x, modes):
    q = np.zeros((len(modes), 3, 3), float)
    eye = np.eye(3)
    for n, w in enumerate(modes):
        for ma, xa, wa in zip(m, x, w):
            q[n] += ma * (np.outer(wa, xa) + np.outer(xa, wa) - (2 / 3) * eye * np.dot(wa, xa))
    return q


def stf_basis(n):
    ref = np.array([1.0, 0.0, 0.0]) if abs(n[0]) < 0.9 else np.array([0.0, 1.0, 0.0])
    e1 = ref - np.dot(ref, n) * n
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(n, e1)
    return (
        (np.outer(e1, e1) - np.outer(e2, e2)) / np.sqrt(2),
        (np.outer(e1, e2) + np.outer(e2, e1)) / np.sqrt(2),
        (np.outer(e1, n) + np.outer(n, e1)) / np.sqrt(2),
        (np.outer(e2, n) + np.outer(n, e2)) / np.sqrt(2),
        (2 * np.outer(n, n) - np.outer(e1, e1) - np.outer(e2, e2)) / np.sqrt(6),
    )


def sector_strengths(q, e):
    return np.array(
        [
            sum(np.sum(np.einsum("nij,ij->n", q, x) ** 2) for x in e[:2]),
            sum(np.sum(np.einsum("nij,ij->n", q, x) ** 2) for x in e[2:4]),
            np.sum(np.einsum("nij,ij->n", q, e[4]) ** 2),
        ]
    )


def eta(z):
    return np.array(
        [
            25 * (z**8 - 2 * z**6 + 3 * z**4 - 9 * z**2 + 9) / (16 * z**10),
            25 * (z**6 - 3 * z**4 + 36) / (4 * z**10),
            225 * (z**4 + 3 * z**2 + 9) / (4 * z**10),
        ],
        float,
    )


def k_claim(mu):
    return np.array(
        [
            5 / 32 * (1 + 6 * mu**2 + mu**4),
            5 / 8 * (1 - mu**2) * (1 + mu**2),
            15 / 16 * (1 - mu**2) ** 2,
        ]
    )


def tt_power(e, n):
    p = np.eye(3) - np.outer(n, n)
    q = p @ e @ p
    qtt = q - 0.5 * p * np.trace(q)
    return float(np.sum(qtt * qtt))


def numeric_kernel(e, mu, nphi=360):
    ph = np.linspace(0, 2 * np.pi, nphi, endpoint=False)
    s = np.sqrt(max(0.0, 1 - mu * mu))
    vals = []
    for p in ph:
        n = np.array([s * np.cos(p), s * np.sin(p), mu])
        vals.append(tt_power(e, n))
    return 2 * np.pi * np.mean(vals) / (8 * np.pi / 5)


def splus(z):
    s2 = -(5j / (4 * z**5)) * (z**4 + 2j * z**3 - 3 * z**2 - 3j * z + 3) * np.exp(1j * z)
    s1 = -(5 / (2 * z**5)) * (z**3 + 3j * z**2 - 6 * z - 6j) * np.exp(1j * z)
    s0 = (15j / (2 * z**5)) * (z**2 + 3j * z - 3) * np.exp(1j * z)
    return np.array([s2, s1, s0])


def scaled_block(rng, rows, n, target, fraction):
    x = random_complex(rng, (rows, n)) / np.sqrt(n)
    tr = np.linalg.norm(x, "fro") ** 2
    return x * np.sqrt(fraction * target / tr)


def structured_endpoint(rng, n, j, zlong):
    x = random_complex(rng, (n, n))
    h = 0.5 * (x + x.conj().T) / np.sqrt(n)
    kloc = 0.45 * random_complex(rng, (2, n)) / np.sqrt(n)
    budgets = np.array([4 * j, 2 * j + 4 * zlong, 2 * j / 3 + 8 * zlong / 3])
    kg = np.zeros((5, n), complex)
    kg[:2] = scaled_block(rng, 2, n, budgets[0], rng.uniform(0.05, 0.9))
    kg[2:4] = scaled_block(rng, 2, n, budgets[1], rng.uniform(0.05, 0.9))
    kg[4:] = scaled_block(rng, 1, n, budgets[2], rng.uniform(0.05, 0.9))
    kh = 0.25 * np.eye(n, dtype=complex)
    k = np.vstack([kloc, kg, kh])
    a = -1j * h - 0.5 * k.conj().T @ k
    return a, kloc, kg, budgets


def arbitrary_endpoint(rng, n, local_ports, grav_ports, grav_budget):
    x = random_complex(rng, (n, n))
    h = 0.5 * (x + x.conj().T) / np.sqrt(n)
    kloc = 0.55 * random_complex(rng, (local_ports, n)) / np.sqrt(n)
    kg = scaled_block(rng, grav_ports, n, grav_budget, rng.uniform(0.15, 1.0))
    kh = 0.25 * np.eye(n, dtype=complex)
    k = np.vstack([kloc, kg, kh])
    a = -1j * h - 0.5 * k.conj().T @ k
    return a, kloc, kg


def transfer(a, kout, kin, nu):
    n = a.shape[0]
    return -kout @ np.linalg.solve(1j * nu * np.eye(n) - a, kin.conj().T)


def integrate_link(a, ku, kga, b, ky, kgb, p):
    def f(nu):
        ha = transfer(a, kga, ku, nu)
        hb = transfer(b, ky, kgb, nu)
        t = hb @ p @ ha
        return np.linalg.norm(t, "fro") ** 2 / (2 * np.pi)

    return quad(f, -np.inf, np.inf, epsabs=2e-9, epsrel=2e-8, limit=350)


def legacy_scalar_regression(rng):
    worst = 0.0
    for case in range(12):
        ia = np.exp(rng.normal(scale=0.8))
        ib = np.exp(rng.normal(scale=0.8))
        a, ku, kga = arbitrary_endpoint(rng, 4 + (case % 2), 2, 2, (4 / 3) * ia)
        b, ky, kgb = arbitrary_endpoint(rng, 5 - (case % 2), 2, 2, (4 / 3) * ib)
        r = 4 + 0.9 * case
        etamax = 25 / (16 * r**2)
        x = random_complex(rng, (2, 2))
        u, rr = np.linalg.qr(x)
        phases = np.diag(rr)
        phases = np.where(np.abs(phases) > 0, phases / np.abs(phases), 1)
        u = u @ np.diag(np.conj(phases))
        p = np.sqrt(rng.uniform(0.1, 1) * etamax) * u
        gamma, err = integrate_link(a, ku, kga, b, ky, kgb, p)
        bound = 25 / (12 * r**2) * min(ia, ib)
        worst = max(worst, gamma / bound)
        if gamma > bound + max(5e-8 * bound, 20 * err):
            raise AssertionError(("legacy 25/12", case, gamma, bound, err))
    return worst


def endpoint_cross_version(rng):
    worst_scalar = 0.0
    worst_sector = 0.0
    worst_mix = 0.0
    for case in range(60):
        n_atoms = 3 + (case % 6)
        m = np.exp(rng.normal(scale=0.7, size=n_atoms))
        x = com_positions(m, rng.normal(size=(n_atoms, 3)))
        i2 = float(np.sum(m * np.sum(x * x, axis=1)))
        d = 3 * n_atoms
        full = mass_orthonormal_modes(rng, m, d)
        qf = quadrupoles(m, x, full)
        total = np.sum(qf * qf)
        if not np.isclose(total, (20 / 3) * i2, rtol=3e-12, atol=3e-12):
            raise AssertionError("full scalar Parseval")
        n = rng.normal(size=3)
        n /= np.linalg.norm(n)
        zlong = float(np.sum(m * (x @ n) ** 2))
        j = i2 - zlong
        ss = sector_strengths(qf, stf_basis(n))
        target = np.array([4 * j, 2 * j + 4 * zlong, 2 * j / 3 + 8 * zlong / 3])
        if not np.allclose(ss, target, rtol=3e-12, atol=3e-12):
            raise AssertionError(("sector Parseval", ss, target))
        if not np.isclose(ss.sum(), total, rtol=3e-12, atol=3e-12):
            raise AssertionError("sector sum != scalar")
        nr = 1 + (case * 7) % d
        modes = mass_orthonormal_modes(rng, m, nr)
        q = quadrupoles(m, x, modes)
        s = np.sum(q * q)
        worst_scalar = max(worst_scalar, s / ((20 / 3) * i2))
        if s > (20 / 3) * i2 * (1 + 3e-12):
            raise AssertionError("truncated scalar Bessel")
        zz = rng.normal(size=(nr, nr))
        u, _ = np.linalg.qr(zz)
        qm = quadrupoles(m, x, np.einsum("mn,nak->mak", u, modes))
        worst_mix = max(worst_mix, abs(np.sum(qm * qm) - s))
        if not np.isclose(np.sum(qm * qm), s, rtol=4e-12, atol=4e-12):
            raise AssertionError("mixing")
        e = stf_basis(n)
        st = sector_strengths(q, e)
        worst_sector = max(worst_sector, np.max(st / target))
        if np.any(st > target * (1 + 4e-12)):
            raise AssertionError("truncated sector Bessel")
        omega = rng.random(nr)
        qnorm = np.sum(q * q, axis=(1, 2))
        if np.sum(omega**4 * qnorm) / 5 > (4 / 3) * i2 * (1 + 4e-12):
            raise AssertionError("legacy weighted scalar linewidth")
    return worst_scalar, worst_sector, worst_mix


def tt_kernel_regression():
    e = stf_basis(np.array([0.0, 0.0, 1.0]))
    representatives = [e[0], e[2], e[4]]
    worst = 0.0
    for mu in [-1, -0.7, 0, 0.4, 1]:
        num = np.array([numeric_kernel(x, mu) for x in representatives])
        err = np.max(np.abs(num - k_claim(mu)))
        worst = max(worst, err)
        if not np.allclose(num, k_claim(mu), rtol=2e-12, atol=2e-12):
            raise AssertionError(("TT kernels", mu, num, k_claim(mu)))
    for z in [3.0, 10.0, 100.0]:
        for i, kfun in enumerate(
            [
                lambda u: 5 / 32 * (1 + 6 * u * u + u**4),
                lambda u: 5 / 8 * (1 - u * u) * (1 + u * u),
                lambda u: 15 / 16 * (1 - u * u) ** 2,
            ]
        ):
            val = quad(lambda u: kfun(u) * np.cos(z * u), -1, 1, epsabs=2e-12, epsrel=2e-12)[0]
            if not np.isclose(val, 2 * np.real(splus(z)[i]), rtol=2e-11, atol=2e-11):
                raise AssertionError(("outgoing amplitude", z, i, val, 2 * np.real(splus(z)[i])))
        if not np.allclose(np.abs(splus(z)) ** 2, eta(z), rtol=2e-13, atol=2e-13):
            raise AssertionError("eta")
    return worst


def sector_end_to_end(rng):
    worst_actual = 0.0
    worst_geom = 0.0
    worst_oldratio = 0.0
    for case in range(12):
        ja, za = np.exp(rng.normal()), np.exp(rng.normal())
        jb, zb = np.exp(rng.normal()), np.exp(rng.normal())
        a, ku, kga, ba = structured_endpoint(rng, 4 + (case % 2), ja, za)
        b, ky, kgb, bb = structured_endpoint(rng, 5 - (case % 2), jb, zb)
        z = 3 + 1.5 * case
        et = eta(z)
        p = np.diag([np.sqrt(et[0])] * 2 + [np.sqrt(et[1])] * 2 + [np.sqrt(et[2])])
        gamma, err = integrate_link(a, ku, kga, b, ky, kgb, p)
        tra = np.array(
            [
                np.linalg.norm(kga[:2], "fro") ** 2,
                np.linalg.norm(kga[2:4], "fro") ** 2,
                np.linalg.norm(kga[4:], "fro") ** 2,
            ]
        )
        trb = np.array(
            [
                np.linalg.norm(kgb[:2], "fro") ** 2,
                np.linalg.norm(kgb[2:4], "fro") ** 2,
                np.linalg.norm(kgb[4:], "fro") ** 2,
            ]
        )
        actual = min(np.dot(et, tra), np.dot(et, trb))
        geom = min(np.dot(et, ba), np.dot(et, bb))
        if gamma > actual + max(5e-8 * actual, 20 * err):
            raise AssertionError(("weighted trace cut", case, gamma, actual, err))
        if actual > geom * (1 + 3e-12):
            raise AssertionError("resource geometry")
        worst_actual = max(worst_actual, gamma / actual)
        worst_geom = max(worst_geom, gamma / geom)
        olda = (20 / 3) * (ja + za) * et[0]
        oldb = (20 / 3) * (jb + zb) * et[0]
        old = min(olda, oldb)
        if geom > old * (1 + 3e-12):
            raise AssertionError("new not <= old")
        worst_oldratio = max(worst_oldratio, geom / old)
    return worst_actual, worst_geom, worst_oldratio


def main():
    rng = np.random.default_rng(SEED)
    legacy = legacy_scalar_regression(rng)
    scalar, sector, mix = endpoint_cross_version(rng)
    kernel = tt_kernel_regression()
    weighted, geom, oldratio = sector_end_to_end(rng)
    if not np.isclose((1 / 5) * (25 / 16) * 4, 5 / 4, rtol=0, atol=1e-15):
        raise AssertionError("5/4 algebra")
    print(f"legacy 25/12 end-to-end worst ratio = {legacy:.12g}")
    print(f"truncated scalar Bessel worst ratio = {scalar:.12g}")
    print(f"truncated sector Bessel worst ratio = {sector:.12g}")
    print(f"modal-mixing worst absolute error = {mix:.12g}")
    print(f"independent TT-kernel worst absolute error = {kernel:.12g}")
    print(f"sector end-to-end Gamma/weighted-trace worst ratio = {weighted:.12g}")
    print(f"sector end-to-end Gamma/geometry worst ratio = {geom:.12g}")
    print(f"largest new-geometry/old-scalar bound ratio = {oldratio:.12g}")
    print("PASS: cross-version constant regression; 25/12 preserved, 5/4 refinement survives")


if __name__ == "__main__":
    main()
