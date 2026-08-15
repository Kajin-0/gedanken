#!/usr/bin/env python3
"""FDT stochastic-work diagnostic on causal two-pole phase trajectories.

For a prescribed deterministic port-voltage waveform V(t) coupled to a linear
equilibrium environment Y(omega),

    Q_diss = integral ReY |V~|^2 d omega/(2 pi)

and with the two-sided symmetrized FDT spectrum

    S_I = hbar |omega| coth[hbar|omega|/(2kT)] ReY,

noise work W_N = integral V I_N dt obeys exactly (for the prescribed waveform)

    Var(W_N) = eps_eff Q_diss,

where

    eps_eff =
      [integral hbar|omega|coth(...) ReY |V~|^2]
      / [integral ReY |V~|^2].

At high temperature eps_eff -> 2 k_B T.  At low temperature it becomes a
dissipation-weighted quantum energy scale.

This script evaluates Q_diss and the unavoidable stochastic-work scale on the
actual deterministic Experiment-03 two-pole trajectories.  It is a first-order
noise diagnostic, not a nonlinear stochastic capture probability: the voltage
waveform itself is not allowed to respond to the noise in this calculation.
"""

from __future__ import annotations

import math

import numpy as np
from scipy.integrate import solve_ivp

from causal_two_pole_environment import filter_components
from finite_time_basin_slice import cold_phase_scale
from full_dynamic_rfsquid import (
    CASES,
    DynamicForce,
    T0,
    TAU0_CONDITIONAL,
    adiabatic_photon_temperature,
)
from quantum_initial_capture import HBAR, KB, PHI_BAR
from two_pole_cold_variance import admittance


def eps_quantum(omega: np.ndarray, T: float) -> np.ndarray:
    out = np.empty_like(omega, dtype=float)
    z = HBAR * omega / (2.0 * KB * T)
    small = z < 1.0e-6
    large = z > 30.0
    mid = ~(small | large)
    out[small] = 2.0 * KB * T
    out[large] = HBAR * omega[large]
    out[mid] = HBAR * omega[mid] / np.tanh(z[mid])
    return out


def trace_case(
    model: DynamicForce,
    R: float,
    alpha: float,
    *,
    r_delta: float = 0.6,
    rise_ps: float = 20.0,
    lambda_um: float = 14.0,
    tend_ns: float = 1.5,
    dt_ps: float = 0.5,
) -> dict[str, float | str]:
    L, C, _ = CASES[r_delta]
    left, right = model.cold_states()
    x_c, _, omega_c = cold_phase_scale(model, r_delta)
    omega_d = alpha * omega_c
    Lf, Cf = filter_components(R, omega_d)

    Tad = adiabatic_photon_temperature(lambda_um, 100.0)
    u0 = T0 * T0
    du_total = Tad * Tad - u0
    cool_coeff = 1.0 / (2.0 * TAU0_CONDITIONAL * u0)
    tau_r = rise_ps * 1.0e-12

    def source(t: float) -> float:
        return du_total / tau_r * math.exp(-t / tau_r)

    def rhs(t: float, y: np.ndarray) -> np.ndarray:
        x, v, u, d, w = y
        u = max(float(u), u0)
        T = math.sqrt(u)
        F = model.force(T, x)
        du = source(t) - cool_coeff * (u * u - u0 * u0)
        dv = -(d + F) / (L * C)
        dd = (L / Lf) * (v - w)
        dw = d / (L * Cf) - w / (R * Cf)
        return np.array([v, dv, du, dd, dw])

    dt = dt_ps * 1.0e-12
    n = int(math.floor(tend_ns * 1.0e-9 / dt))
    t_eval = np.arange(n, dtype=float) * dt
    sol = solve_ivp(
        rhs,
        (0.0, float(t_eval[-1])),
        np.array([x_c, 0.0, u0, 0.0, 0.0]),
        t_eval=t_eval,
        method="DOP853",
        rtol=4.0e-8,
        atol=np.array([1.0e-10, 2.0e2, 1.0e-13, 1.0e-10, 2.0e2]),
        max_step=min(dt, 0.12 / max(omega_c, omega_d)),
    )

    x = sol.y[0]
    v = sol.y[1]
    w = sol.y[4]
    xf = float(x[-1])
    basin = "right" if abs(xf - right) < abs(xf - left) else "left"

    # Exact time-domain resistor dissipation over the simulated interval.
    q_time = float(np.trapezoid((PHI_BAR * w) ** 2 / R, t_eval))

    # Continuous-transform approximation v~(omega_k) = dt FFT[v].
    Vx = np.fft.rfft(v) * dt
    freqs = np.fft.rfftfreq(n, dt)
    omega = 2.0 * math.pi * freqs
    df = 1.0 / (n * dt)
    weights = np.full_like(freqs, 2.0, dtype=float)
    weights[0] = 1.0
    if n % 2 == 0:
        weights[-1] = 1.0

    reY = np.array([admittance(float(om), R, omega_d).real for om in omega])
    amp2 = np.abs(Vx) ** 2
    Dv = float(np.sum(weights * reY * amp2) * df)
    q_spec = PHI_BAR * PHI_BAR * Dv

    eps = eps_quantum(omega, T0)
    Nv = float(np.sum(weights * eps * reY * amp2) * df)
    eps_eff = Nv / Dv if Dv > 0.0 else 0.0
    varW = eps_eff * q_spec
    sigmaW = math.sqrt(max(varW, 0.0))

    # Retained cold barrier scale for orientation only; it is not the dynamic
    # separatrix margin of the driven trajectory.
    cold_barrier = 6.87 * KB

    return {
        "basin": basin,
        "x_final": xf,
        "Q_time": q_time,
        "Q_spec": q_spec,
        "eps_eff": eps_eff,
        "sigmaW": sigmaW,
        "sigmaW_over_cold_barrier": sigmaW / cold_barrier,
        "Q_over_kB_K": q_spec / KB,
        "eps_over_kB_K": eps_eff / KB,
        "sigmaW_over_kB_K": sigmaW / KB,
        "Q_consistency": q_spec / q_time if q_time > 0.0 else math.nan,
    }


def main() -> None:
    print("Experiment 03 FDT stochastic-work trajectory diagnostic")
    print("full CPR grid; 14 um; rise=20 ps; T_bath=20 mK")
    model = DynamicForce(0.6, quick=False)

    for R, alpha in [
        (120.0, 0.35),
        (160.0, 0.35),
        (250.0, 0.20),
        (250.0, 0.35),
        (250.0, 0.50),
        (400.0, 0.35),
    ]:
        out = trace_case(model, R, alpha)
        msg = (
            f"R={R:g} ohm, alpha={alpha:.2f}: basin={out['basin']}, "
            f"Q/kB={float(out['Q_over_kB_K']):.4f} K, "
            f"eps_eff/kB={float(out['eps_over_kB_K']):.4f} K, "
            f"sigmaW/kB={float(out['sigmaW_over_kB_K']):.4f} K, "
            f"sigmaW/coldBarrier={float(out['sigmaW_over_cold_barrier']):.4f}, "
            f"Qspec/Qtime={float(out['Q_consistency']):.4f}"
        )
        print(msg)
        print(f"::notice title=Experiment 03 FDT work-noise::{msg}")

    print("PASS")


if __name__ == "__main__":
    main()
