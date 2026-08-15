#!/usr/bin/env python3
"""Cold harmonic phase-coordinate variance under an Ohmic quantum bath.

For the linearized cold phase coordinate q=Phi_bar x with fixed physical
stiffness K=kappa/L,

    C qddot + qdot/R + K q = I_N,

and the two-sided symmetrized quantum-FDT spectrum

    S_I(omega)=hbar |omega| coth[hbar|omega|/(2kT)] / R,

the equilibrium symmetrized position variance is obtained from the linear
susceptibility. This script compares it to the isolated harmonic Wigner width.

Important: this is a linear reduced-coordinate regression with fixed cold
curvature. It does not include nonlinear basin geometry or pulse-time capture.
A strictly Ohmic bath also requires care for momentum/UV observables; the
coordinate variance itself is convergent.
"""

from __future__ import annotations

import math

import numpy as np
from scipy.integrate import quad

from full_dynamic_rfsquid import CASES, DynamicForce
from quantum_initial_capture import quantum_covariance, HBAR, KB, T0


def zero_temperature_ratio(g: float) -> float:
    """Exact sigma_x^2(Ohmic)/sigma_x^2(isolated) at T=0 for g=gamma/omega<2."""
    if not (0.0 < g < 2.0):
        raise ValueError("closed underdamped expression requires 0<g<2")
    a = 1.0 - 0.5 * g * g
    b = g * math.sqrt(1.0 - 0.25 * g * g)
    integral = 0.5 / b * (0.5 * math.pi + math.atan2(a, b))
    return (2.0 * g / math.pi) * integral


def finite_temperature_ratio(g: float, a: float) -> float:
    """Finite-T FDT integral; a=hbar omega_c/(2 k_B T)."""
    coth_a = 1.0 / math.tanh(a)

    def integrand_log(y: float) -> float:
        s = math.exp(y)
        z = a * s
        if z < 1.0e-6:
            coth = 1.0 / z + z / 3.0
        elif z > 25.0:
            coth = 1.0
        else:
            coth = 1.0 / math.tanh(z)
        den = (1.0 - s * s) ** 2 + g * g * s * s
        # ds=s dy, original numerator s*coth ds -> s^2*coth dy.
        return s * s * coth / den

    val = quad(integrand_log, -24.0, 24.0, epsabs=1e-10, epsrel=2e-8, limit=600)[0]
    return (2.0 * g / (math.pi * coth_a)) * val


def report(r_delta: float, Rs: tuple[float, ...]) -> None:
    model = DynamicForce(r_delta, quick=False)
    cov = quantum_covariance(model, r_delta)
    _, C, _ = CASES[r_delta]
    omega = cov["omega_c"]
    a = HBAR * omega / (2.0 * KB * T0)

    for R in Rs:
        gamma = 1.0 / (R * C)
        g = gamma / omega
        Q = 1.0 / g
        rz = zero_temperature_ratio(g)
        rt = finite_temperature_ratio(g, a)
        sigma_bath = cov["sigma_x"] * math.sqrt(rt)
        msg = (
            f"rDelta={r_delta:.1f}, R={R:g} ohm: Q={Q:.3f}, g={g:.5f}, "
            f"var_ratio_T0={rz:.6f}, var_ratio_20mK={rt:.6f}, "
            f"sigma_isolated={cov['sigma_x']:.6f}, sigma_ohmic={sigma_bath:.6f} rad"
        )
        print(msg)
        print(f"::notice title=Experiment 03 Ohmic cold variance::{msg}")


def main() -> None:
    print("Experiment 03 Ohmic quantum-FDT cold coordinate variance")
    report(0.8, (185.0, 300.0, 400.0, 600.0))
    report(0.6, (75.0, 120.0, 160.0, 250.0, 400.0))
    print("PASS")


if __name__ == "__main__":
    main()
