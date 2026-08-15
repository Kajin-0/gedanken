#!/usr/bin/env python3
"""Quantum-FDT cold variance for the passive two-pole Experiment-03 bath.

For the cold harmonic phase coordinate q=Phi_bar x,

    C qddot + Y * qdot + K q = I_N,
    K = kappa_c/L,

with the two-sided symmetrized FDT convention

    S_I(omega) = hbar |omega| coth[hbar|omega|/(2 k_B T)] Re Y(omega),

this script evaluates the reduced-coordinate equilibrium variances

    <q^2>       = integral |chi|^2 S_I d omega/(2 pi)
    <qdot^2>    = integral omega^2 |chi|^2 S_I d omega/(2 pi)

for the passive network

    Z = i omega L_f + R/(1+i omega R C_f),

with

    L_f = sqrt(2) R/omega_D,
    C_f = 1/(sqrt(2) R omega_D).

For this choice

    Re Y = (1/R)/[1+(omega/omega_D)^4],

so both coordinate and velocity variances are ultraviolet convergent.  This is
a linear equilibrium calculation only; it is not nonlinear pulse capture and
is not a substitute for a full dissipative quantum treatment.
"""

from __future__ import annotations

import math

import numpy as np
from scipy.integrate import quad

from causal_two_pole_environment import filter_components
from full_dynamic_rfsquid import CASES, DynamicForce
from quantum_initial_capture import HBAR, KB, T0, quantum_covariance


def admittance(omega: float, R: float, omega_d: float) -> complex:
    Lf, Cf = filter_components(R, omega_d)
    jw = 1j * float(omega)
    Zp = R / (1.0 + jw * R * Cf)
    Z = jw * Lf + Zp
    return 1.0 / Z


def coth_stable(z: float) -> float:
    if z < 1.0e-6:
        return 1.0 / z + z / 3.0
    if z > 30.0:
        return 1.0
    return 1.0 / math.tanh(z)


def variance_ratios(
    model: DynamicForce,
    r_delta: float,
    R: float,
    alpha: float,
) -> tuple[float, float, float, float, float]:
    L, C, _ = CASES[r_delta]
    cov = quantum_covariance(model, r_delta)
    omega0 = cov["omega_c"]
    kappa = cov["kappa_c"]
    K = kappa / L
    omega_d = alpha * omega0
    a0 = HBAR * omega0 / (2.0 * KB * T0)
    coth0 = coth_stable(a0)

    # Integrate on logarithmic frequency y=ln(omega/omega0).
    def integrands(y: float) -> tuple[float, float]:
        s = math.exp(y)
        omega = omega0 * s
        Y = admittance(omega, R, omega_d)
        den = K - C * omega * omega + 1j * omega * Y
        chi2 = 1.0 / (den.real * den.real + den.imag * den.imag)
        S = HBAR * omega * coth_stable(HBAR * omega / (2.0 * KB * T0)) * Y.real
        # d omega = omega dy.
        q = chi2 * S * omega / math.pi
        v = omega * omega * q
        return q, v

    qint = quad(lambda y: integrands(y)[0], -22.0, 22.0,
                epsabs=0.0, epsrel=3.0e-7, limit=800)[0]
    vint = quad(lambda y: integrands(y)[1], -22.0, 22.0,
                epsabs=0.0, epsrel=3.0e-7, limit=800)[0]

    q_iso = HBAR / (2.0 * C * omega0) * coth0
    v_iso = HBAR * omega0 / (2.0 * C) * coth0
    rq = qint / q_iso
    rv = vint / v_iso
    return rq, rv, math.sqrt(rq), math.sqrt(rv), omega_d


def main() -> None:
    print("Experiment 03 passive two-pole quantum-FDT cold variance")
    print("ratios are relative to isolated harmonic variances at 20 mK")

    model = DynamicForce(0.6, quick=False)
    cov = quantum_covariance(model, 0.6)
    omega0 = cov["omega_c"]

    for R in (120.0, 160.0, 250.0, 400.0):
        for alpha in (0.20, 0.35, 0.50, 0.75, 1.00, 1.50, 3.00):
            rq, rv, sq, sv, omega_d = variance_ratios(model, 0.6, R, alpha)
            Lf, Cf = filter_components(R, omega_d)
            msg = (
                f"R={R:g} ohm, alpha={alpha:.2f}: "
                f"var_x_ratio={rq:.6f}, var_v_ratio={rv:.6f}, "
                f"sigma_x_ratio={sq:.6f}, sigma_v_ratio={sv:.6f}, "
                f"sigma_x={cov['sigma_x']*sq:.6f} rad, "
                f"Lf={Lf*1e9:.3f} nH, Cf={Cf*1e15:.3f} fF"
            )
            print(msg)
            print(f"::notice title=Experiment 03 two-pole FDT variance::{msg}")

    print(f"omega_c/2pi={omega0/(2*math.pi)*1e-9:.3f} GHz")
    print("PASS")


if __name__ == "__main__":
    main()
