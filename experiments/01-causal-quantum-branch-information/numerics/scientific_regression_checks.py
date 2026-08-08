"""Fast regression checks for the active Experiment 01 scientific numerics.

This suite is intentionally smaller than the exploratory scan scripts. It is
meant for CI: representative channel checks plus closed-form constants used by
V7. The analytic paper does not depend on these tests as proofs.
"""

from __future__ import annotations

import math

import numpy as np

from additive_noise_cat_scan import cat_pt_spectrum as additive_pt_spectrum
from amplifier_cat_scan import cat_pt_spectrum as amplifier_pt_spectrum
from amplifier_cat_scan import two_mode_squeezer_unitary
from thermal_cat_scan import beam_splitter_unitary, cat_negativity


G_NEWTON = 6.67430e-11
C_LIGHT = 299_792_458.0


def assert_close(name: str, actual: float, expected: float, atol: float, rtol: float = 0.0) -> None:
    err = abs(actual - expected)
    tol = atol + rtol * abs(expected)
    if err > tol:
        raise AssertionError(
            f"{name}: actual={actual:.16e}, expected={expected:.16e}, "
            f"error={err:.3e}, tolerance={tol:.3e}"
        )


def check_thermal_attenuator() -> None:
    dim = 12

    # Safely non-EB: eta > nbar/(nbar+1) for nbar=0.1.
    eta = 0.80
    nbar = 0.10
    u = beam_splitter_unitary(eta, dim)
    neg, trace = cat_negativity(eta, nbar, n_delta=1.0, dim=dim, unitary=u)
    if not neg > 1e-3:
        raise AssertionError(f"thermal non-EB negativity unexpectedly small: {neg}")
    assert_close("thermal trace", trace, 1.0, atol=2e-10)

    # Strong EB control. Finite truncation may leave a tiny numerical floor, so
    # only require it to be parametrically below the non-EB case.
    eta_eb = 0.02
    u_eb = beam_splitter_unitary(eta_eb, dim)
    neg_eb, trace_eb = cat_negativity(
        eta_eb, nbar, n_delta=1.0, dim=dim, unitary=u_eb
    )
    if not neg_eb < 0.10 * neg:
        raise AssertionError(
            f"thermal EB control did not suppress negativity enough: "
            f"nonEB={neg}, EB={neg_eb}"
        )
    assert_close("thermal EB trace", trace_eb, 1.0, atol=2e-10)


def check_thermal_amplifier() -> None:
    gain = 1.5
    amplitude = 0.4
    dim = 12

    # Canonical non-EB case documented in numerics/README.md.
    u = two_mode_squeezer_unitary(gain, dim)
    eigvals, trace, tail = amplifier_pt_spectrum(
        gain=gain,
        n_env=0.5,
        amplitude=amplitude,
        dim=dim,
        unitary=u,
    )
    lam_min = float(eigvals[0])
    assert_close(
        "amplifier non-EB lambda_min",
        lam_min,
        -5.85734e-2,
        atol=8e-5,
    )
    assert_close("amplifier trace", trace, 1.0, atol=2e-8)
    if not tail < 1e-5:
        raise AssertionError(f"amplifier thermal omitted tail too large: {tail}")

    # EB-side truncation floor should shrink as cutoff increases.
    vals = []
    for cutoff in (10, 12):
        u_eb = two_mode_squeezer_unitary(gain, cutoff)
        e, tr, _ = amplifier_pt_spectrum(
            gain=gain,
            n_env=3.0,
            amplitude=amplitude,
            dim=cutoff,
            unitary=u_eb,
        )
        vals.append(abs(float(e[0])))
        assert_close(f"amplifier EB trace N={cutoff}", tr, 1.0, atol=5e-7)
    if not vals[1] < vals[0]:
        raise AssertionError(f"amplifier EB truncation floor did not shrink: {vals}")


def check_additive_noise_and_boundary() -> None:
    amplitude = 0.35
    dim = 12
    order = 12

    eig_non, trace_non = additive_pt_spectrum(
        noise=0.70, amplitude=amplitude, dim=dim, order=order
    )
    if not float(eig_non[0]) < -1e-2:
        raise AssertionError(
            f"additive non-EB lambda_min unexpectedly weak: {float(eig_non[0])}"
        )
    assert_close("additive non-EB trace", trace_non, 1.0, atol=2e-9)

    eig_eb, trace_eb = additive_pt_spectrum(
        noise=1.30, amplitude=amplitude, dim=dim, order=order
    )
    if not abs(float(eig_eb[0])) < 2e-3:
        raise AssertionError(
            f"additive EB numerical floor unexpectedly large: {float(eig_eb[0])}"
        )
    assert_close("additive EB trace", trace_eb, 1.0, atol=2e-9)

    # Near-boundary sign-resolution check. On the non-EB side the finite result
    # should be clearly negative; the EB side should collapse toward the much
    # smaller numerical floor.
    eig_near_non, _ = additive_pt_spectrum(
        noise=0.95, amplitude=amplitude, dim=dim, order=14
    )
    eig_near_eb, _ = additive_pt_spectrum(
        noise=1.05, amplitude=amplitude, dim=dim, order=14
    )
    l_non = abs(float(eig_near_non[0]))
    l_eb = abs(float(eig_near_eb[0]))
    if not float(eig_near_non[0]) < -5e-4:
        raise AssertionError(
            f"near-boundary non-EB case not resolved: {float(eig_near_non[0])}"
        )
    if not l_eb < 0.25 * l_non:
        raise AssertionError(
            f"near-boundary EB floor not sufficiently below non-EB signal: "
            f"nonEB={l_non}, EB={l_eb}"
        )


def check_finite_spoke_series() -> None:
    q = 0.05
    exact_a = 0.5 + q / math.sin(2.0 * q)
    exact_cq = (math.tan(q) / q) / math.sqrt(exact_a)
    exact_ck = (math.tan(q) / q) ** 2 / exact_a

    series_a = 1.0 + q**2 / 3.0 + 7.0 * q**4 / 45.0
    series_cq = 1.0 + q**2 / 6.0 + q**4 / 24.0
    series_ck = 1.0 + q**2 / 3.0 + q**4 / 9.0

    assert_close("finite-spoke A(q) series", exact_a, series_a, atol=4e-9)
    assert_close("finite-spoke C_Q series", exact_cq, series_cq, atol=4e-9)
    assert_close("finite-spoke C_kappa series", exact_ck, series_ck, atol=4e-9)


def check_link_benchmark_constants() -> None:
    # Deliberately aggressive benchmark used in V7:
    # four 1 kg endpoint masses, L=1 m, f=1 MHz, Q=1e12, kR=10.
    mu = 1.0
    length = 1.0
    frequency = 1.0e6
    omega = 2.0 * math.pi * frequency
    q_mech = 1.0e12

    kappa_g = (
        8.0
        * G_NEWTON
        * mu
        * length**2
        * omega**4
        / (5.0 * C_LIGHT**5)
    )
    beta_g = kappa_g / (omega / q_mech)
    eta_store = 25.0 / (16.0 * 10.0**2)
    eta_link = beta_g**2 * eta_store
    passive_matched = 4.0 * math.exp(-2.0) * eta_link

    assert_close("benchmark kappa_g", kappa_g, 6.872925955226083e-26, atol=2e-39, rtol=2e-13)
    assert_close("benchmark beta_g", beta_g, 1.0938601392788179e-20, atol=2e-33, rtol=2e-13)
    assert_close("benchmark eta_store", eta_store, 0.015625, atol=1e-15)
    assert_close("benchmark eta_link", eta_link, 1.8695781317235544e-42, atol=2e-55, rtol=2e-13)
    assert_close("benchmark passive matched", passive_matched, 1.0120795439591377e-42, atol=2e-55, rtol=2e-13)


def exact_pure_loss_negativity(eta: float, amplitude_sq: float) -> float:
    s_b = math.exp(-2.0 * eta * amplitude_sq)
    s_e = math.exp(-2.0 * (1.0 - eta) * amplitude_sq)
    return (
        math.sqrt((1.0 + s_e) ** 2 - 4.0 * s_e * s_b**2)
        - (1.0 - s_e)
    ) / 4.0


def check_exact_negativity_asymptotic() -> None:
    eta = 1.0e-6
    # Leading optimized scaling A_opt^2 ~ sqrt(eta).
    amp_sq = math.sqrt(eta)
    exact = exact_pure_loss_negativity(eta, amp_sq)
    series = eta - 2.0 * eta ** 1.5 + (13.0 / 3.0) * eta**2

    if not exact > 0.0:
        raise AssertionError(f"exact pure-loss negativity not positive: {exact}")
    assert_close("weak-link negativity asymptotic", exact, series, atol=2e-13)


def main() -> None:
    checks = [
        ("thermal attenuator", check_thermal_attenuator),
        ("thermal amplifier", check_thermal_amplifier),
        ("additive noise / boundary", check_additive_noise_and_boundary),
        ("finite-spoke series", check_finite_spoke_series),
        ("link benchmark constants", check_link_benchmark_constants),
        ("exact negativity asymptotic", check_exact_negativity_asymptotic),
    ]

    for name, fn in checks:
        print(f"[RUN] {name}")
        fn()
        print(f"[PASS] {name}")

    print("All scientific regression checks passed.")


if __name__ == "__main__":
    main()
