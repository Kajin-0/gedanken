#!/usr/bin/env python3
"""Correlated cold equilibrium covariance for the causal Drude bath.

Purpose
-------
Extend the scalar coordinate/velocity variance check to the actual auxiliary
memory variable used by the causal Drude embedding,

    L C xddot + L j + F(x,T) = 0
    tau_D jdot + j = G0 xdot

with

    Y(omega)=G0/(1-i omega/omega_D).

For the cold linearized mode and the symmetrized quantum-FDT source, define

    X = (x-x_c)/sigma_x0
    U = xdot/(omega0 sigma_x0)
    J = j/(G0 omega0 sigma_x0),

where sigma_x0 is the isolated harmonic Wigner width at the same bare omega0.
The exact stationary Gaussian covariance of (X,U,J) follows from the spectral
transfer functions.  This is a regression for the linear cold state; it does
not make the nonlinear pulse dynamics quantum-exact.

The script also evaluates a controlled fast-memory diagnostic.  If the optical
pulse changes only weakly over tau_D, the initial memory current produces an
integrated velocity kick

    Delta U ~= -(g/d) J,

where g=G0/(C omega0) and d=omega_D/omega0.  The associated reduced covariance
therefore estimates whether explicitly sampling J is likely to matter before a
full 3D basin integral is attempted.
"""
from __future__ import annotations

import math
import numpy as np
from scipy.integrate import quad

from full_dynamic_rfsquid import CASES, DynamicForce
from quantum_initial_capture import quantum_covariance, HBAR, KB, T0
from drude_bath_variance import coth_stable


def covariance_ratios(g: float, d: float, a: float) -> np.ndarray:
    """Return normalized covariance matrix of (X,U,J)."""
    coth_a = coth_stable(a)

    def pieces(y: float) -> tuple[float, float, float, float, float]:
        s = math.exp(y)
        r = s / d
        lp = 1.0 / (1.0 + r * r)
        yre = lp
        yim = r * lp

        # D/(C omega0^2) for exp(-i omega t).
        re = 1.0 - s * s + g * s * r * lp
        im = -g * s * lp
        den = re * re + im * im
        c = coth_stable(a * s)

        # q-variance spectral weight after ds=s dy.
        base = s * s * c * lp / den

        # Re transfer-product factors for normalized variables.
        xx = base
        uu = s * s * base
        xj = s * yim * base
        uj = s * s * yre * base
        jj = s * s * (yre * yre + yim * yim) * base
        return xx, uu, xj, uj, jj

    ints = []
    for k in range(5):
        val = quad(
            lambda y, kk=k: pieces(y)[kk],
            -24.0, 24.0,
            epsabs=1e-10, epsrel=2e-8, limit=800,
        )[0]
        ints.append(val)

    pref = 2.0 * g / (math.pi * coth_a)
    rxx, ruu, rxj, ruj, rjj = [pref * v for v in ints]

    # <X U>_sym = 0 by equilibrium time-reversal symmetry.
    cov = np.array(
        [[rxx, 0.0, rxj],
         [0.0, ruu, ruj],
         [rxj, ruj, rjj]],
        dtype=float,
    )
    return cov


def report(r_delta: float, R0: float, d: float, rise_ps: float) -> None:
    model = DynamicForce(r_delta, quick=False)
    cov0 = quantum_covariance(model, r_delta)
    _, C, _ = CASES[r_delta]
    omega0 = cov0["omega_c"]
    a = HBAR * omega0 / (2.0 * KB * T0)
    g = 1.0 / (R0 * C * omega0)
    M = covariance_ratios(g, d, a)

    evals = np.linalg.eigvalsh(M)
    sx, su, sj = np.sqrt(np.diag(M))
    rho_xj = M[0, 2] / (sx * sj)
    rho_uj = M[1, 2] / (su * sj)

    eps = g / d
    # Fast-memory elimination U_eff = U - eps J.
    var_ueff = M[1,1] + eps * eps * M[2,2] - 2.0 * eps * M[1,2]
    cov_xueff = -eps * M[0,2]
    rho_xueff = cov_xueff / math.sqrt(M[0,0] * var_ueff)

    # Characteristic direct phase-position shift accumulated during the memory
    # transient is O((g/d^2) J) in units of sigma_x0.
    rms_du_from_j = eps * sj
    rms_dx_fast = (g / (d*d)) * sj
    tauD_ps = 1.0e12 / (d * omega0)
    memory_to_rise = tauD_ps / rise_ps

    msg = (
        f"rDelta={r_delta:.1f} R0={R0:g}ohm d={d:g}: "
        f"varX={M[0,0]:.6f} varU={M[1,1]:.6f} varJ={M[2,2]:.6f}; "
        f"rhoXJ={rho_xj:.6f} rhoUJ={rho_uj:.6f}; "
        f"eigmin={evals[0]:.6e}; eps=g/d={eps:.6f}; "
        f"varUeff={var_ueff:.6f} rhoXUeff={rho_xueff:.6f}; "
        f"rmsDeltaU_J={rms_du_from_j:.6f} sigmaU0; "
        f"rmsDeltaX_fast={rms_dx_fast:.6f} sigmaX0; "
        f"tauD={tauD_ps:.3f}ps tauD/rise={memory_to_rise:.4f}"
    )
    print(msg)
    print(f"::notice title=Experiment 03 Drude equilibrium covariance::{msg}")


def main() -> None:
    print("Experiment 03 correlated Drude equilibrium covariance")
    for d in (2.0, 5.0, 10.0):
        report(0.6, 250.0, d, 20.0)
    for d in (5.0, 10.0):
        report(0.8, 600.0, d, 5.0)
    print("PASS")


if __name__ == "__main__":
    main()
