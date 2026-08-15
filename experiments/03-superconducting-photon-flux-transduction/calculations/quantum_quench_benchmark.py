#!/usr/bin/env python3
"""Exact closed-system quantum benchmark for Experiment 03 rapid quench.

Purpose
-------
The current initial-Wigner capture calculation samples the exact harmonic cold
Wigner distribution but then propagates each point with classical nonlinear
RCSJ dynamics. That is a truncated-Wigner / classical-Liouville approximation.

This script tests that approximation in a deliberately simpler controlled
subproblem:

    cold harmonic ground-state Gaussian
    -> instantaneous quench to a fixed hot nonlinear rf-SQUID potential
    -> no damping and no cooling during the benchmark interval.

For the same initial Wigner Gaussian we compare

1. exact one-dimensional Schrodinger evolution by split-operator FFT, and
2. vectorized classical Hamiltonian propagation.

The observable is probability to lie to the right of the retained hot saddle
as a function of time. This is NOT the final detector capture probability; it
is a Moyal/nonlinear-quantum regression for the rapid launch stage.
"""

from __future__ import annotations

import argparse
import math

import numpy as np
from scipy.integrate import cumulative_trapezoid

from full_dynamic_rfsquid import CASES, DynamicForce, T0
from quantum_initial_capture import quantum_covariance
from quench_energy_bound import quench_temperature

HBAR = 1.054571817e-34
H = 6.62607015e-34
E_CHARGE = 1.602176634e-19
PHI0 = H / (2.0 * E_CHARGE)
PHIBAR = PHI0 / (2.0 * np.pi)


def hot_saddle(model: DynamicForce, T: float) -> float:
    roots = model.roots(T)
    saddles = [x for x, curvature in roots if curvature < 0.0]
    if not saddles:
        raise ValueError("No hot saddle at requested T")
    return min(saddles, key=abs)


def potential_on_grid(model: DynamicForce, T: float, x: np.ndarray, L: float) -> np.ndarray:
    """Physical U(x)-U(x[0]) from force F=d u_dimless/dx."""
    F = np.asarray([model.force(T, float(xx)) for xx in x])
    u_dimless = cumulative_trapezoid(F, x, initial=0.0)
    return (PHIBAR * PHIBAR / L) * u_dimless


def initial_gaussian(model: DynamicForce, r_delta: float, x: np.ndarray) -> tuple[np.ndarray, dict[str, float]]:
    cov = quantum_covariance(model, r_delta)
    sx = cov["sigma_x"]
    xc = cov["x_c"]
    # Wavefunction whose position probability has variance sigma_x^2.
    psi = np.exp(-((x - xc) ** 2) / (4.0 * sx * sx)).astype(complex)
    dx = x[1] - x[0]
    psi /= math.sqrt(float(np.sum(np.abs(psi) ** 2) * dx))
    return psi, cov


def exact_quantum(
    model: DynamicForce,
    r_delta: float,
    Thot: float,
    *,
    xmax: float,
    nx: int,
    dt_ps: float,
    tmax_ps: float,
    sample_ps: list[float],
) -> tuple[dict[float, float], float, dict[str, float]]:
    L, C, _ = CASES[r_delta]
    m = C * PHIBAR * PHIBAR
    x = np.linspace(-xmax, xmax, nx, endpoint=False)
    dx = x[1] - x[0]
    psi, cov = initial_gaussian(model, r_delta, x)
    U = potential_on_grid(model, Thot, x, L)
    saddle = hot_saddle(model, Thot)

    k = 2.0 * np.pi * np.fft.fftfreq(nx, d=dx)
    p = HBAR * k
    dt = dt_ps * 1.0e-12
    Vhalf = np.exp(-0.5j * U * dt / HBAR)
    K = np.exp(-0.5j * p * p * dt / (m * HBAR))

    target_steps = {int(round(t / dt_ps)): t for t in sample_ps}
    nsteps = int(round(tmax_ps / dt_ps))
    out: dict[float, float] = {}

    for istep in range(1, nsteps + 1):
        psi *= Vhalf
        psi = np.fft.ifft(K * np.fft.fft(psi))
        psi *= Vhalf
        if istep in target_steps:
            prob = float(np.sum(np.abs(psi[x > saddle]) ** 2) * dx)
            out[target_steps[istep]] = prob

    norm = float(np.sum(np.abs(psi) ** 2) * dx)
    return out, norm, cov


def classical_wigner(
    model: DynamicForce,
    r_delta: float,
    Thot: float,
    *,
    dt_ps: float,
    tmax_ps: float,
    sample_ps: list[float],
    nsamp: int,
    seed: int,
) -> dict[float, float]:
    L, C, _ = CASES[r_delta]
    cov = quantum_covariance(model, r_delta)
    rng = np.random.default_rng(seed)
    x = cov["x_c"] + cov["sigma_x"] * rng.standard_normal(nsamp)
    v = cov["sigma_v"] * rng.standard_normal(nsamp)
    saddle = hot_saddle(model, Thot)
    dt = dt_ps * 1.0e-12

    # Interpolate the fixed-hot force for vectorized symplectic stepping.
    xforce = model.xgrid
    fforce = np.asarray([model.force(Thot, float(xx)) for xx in xforce])

    def force_vec(xx: np.ndarray) -> np.ndarray:
        return np.interp(xx, xforce, fforce, left=fforce[0], right=fforce[-1])

    target_steps = {int(round(t / dt_ps)): t for t in sample_ps}
    nsteps = int(round(tmax_ps / dt_ps))
    out: dict[float, float] = {}

    # velocity-Verlet for xddot=-F/(LC)
    a = -force_vec(x) / (L * C)
    for istep in range(1, nsteps + 1):
        x = x + v * dt + 0.5 * a * dt * dt
        anew = -force_vec(x) / (L * C)
        v = v + 0.5 * (a + anew) * dt
        a = anew
        if istep in target_steps:
            out[target_steps[istep]] = float(np.mean(x > saddle))
    return out


def benchmark_case(r_delta: float, offset_K: float, quick: bool) -> None:
    model = DynamicForce(r_delta, quick=quick)
    Tq, Tf = quench_temperature(model)
    Thot = min(Tq + offset_K, Tf - 0.005)
    if Thot <= Tq:
        raise RuntimeError("hot benchmark temperature is not above quench threshold")

    if quick:
        nx, dt_ps, nsamp = 1024, 0.02, 30000
    else:
        nx, dt_ps, nsamp = 2048, 0.01, 120000
    sample_ps = [5.0, 10.0, 20.0, 30.0, 40.0]
    xmax = 5.5

    pq, norm, cov = exact_quantum(
        model, r_delta, Thot,
        xmax=xmax, nx=nx, dt_ps=dt_ps, tmax_ps=max(sample_ps),
        sample_ps=sample_ps,
    )
    pc = classical_wigner(
        model, r_delta, Thot,
        dt_ps=dt_ps, tmax_ps=max(sample_ps), sample_ps=sample_ps,
        nsamp=nsamp, seed=12345 + int(100 * r_delta),
    )

    print(
        f"rDelta={r_delta:.1f}; Tq={Tq:.4f} K; Tf={Tf:.4f} K; "
        f"Thot={Thot:.4f} K; sigma_x={cov['sigma_x']:.5f}; "
        f"quantum_norm={norm:.9f}"
    )
    maxdiff = 0.0
    for t in sample_ps:
        diff = pq[t] - pc[t]
        maxdiff = max(maxdiff, abs(diff))
        msg = (
            f"rDelta={r_delta:.1f}, t={t:.0f} ps: "
            f"P_right_quantum={pq[t]:.6f}, "
            f"P_right_TWA={pc[t]:.6f}, delta={diff:+.6f}"
        )
        print(msg)
        safe = msg.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
        print(f"::notice title=Experiment 03 exact-quantum quench benchmark::{safe}")
    print(f"MAX_ABS_DELTA={maxdiff:.6f}\n")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--quick", action="store_true")
    p.add_argument("--offset-K", type=float, default=0.030,
                   help="fixed-hot temperature offset above Tq")
    args = p.parse_args()

    print("Experiment 03 exact closed-system quantum quench benchmark")
    print("Observable: probability x lies to right of hot saddle; no damping/cooling.\n")
    for r in (0.8, 0.6):
        benchmark_case(r, args.offset_K, args.quick)
    print("PASS")


if __name__ == "__main__":
    main()
