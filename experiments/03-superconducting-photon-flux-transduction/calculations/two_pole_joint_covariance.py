#!/usr/bin/env python3
"""Joint cold Gaussian covariance of phase + passive two-pole filter.

This extends two_pole_cold_variance.py from the marginal phase variables to the
linearized augmented state used by causal_two_pole_environment.py:

    z = [dx, u, d, s]

where

    dx = x-x_c,
    u  = xdot/omega_c,
    d  = L I_env/Phi_bar,
    s  = V_C/(Phi_bar omega_c).

For the cold harmonic network every augmented variable is a linear transfer of
x(omega).  From

    L C xddot + d + kappa x = 0

we have

    d(omega) = (L C omega^2-kappa) x(omega).

From the filter inductor relation,

    s(omega) = i(omega/omega_c)
               [1-(L_f/L)(L C omega^2-kappa)] x(omega).

Together with u=i(omega/omega_c)x, this gives the complete equal-time
symmetrized covariance from the same quantum-FDT phase spectrum used in the
marginal calculation.

This is still a linear reduced/open-system Gaussian object.  It is useful for
initial-state screening, but nonlinear pulse evolution with quantum bath noise
requires a stronger open-system treatment.
"""

from __future__ import annotations

import math

import numpy as np
from scipy.integrate import quad

from causal_two_pole_environment import filter_components
from full_dynamic_rfsquid import CASES, DynamicForce
from quantum_initial_capture import HBAR, KB, PHI_BAR, T0, quantum_covariance
from two_pole_cold_variance import admittance, coth_stable


def covariance_matrix(
    model: DynamicForce,
    r_delta: float,
    R: float,
    alpha: float,
) -> np.ndarray:
    L, C, _ = CASES[r_delta]
    cov0 = quantum_covariance(model, r_delta)
    omega0 = cov0["omega_c"]
    kappa = cov0["kappa_c"]
    K = kappa / L
    omega_d = alpha * omega0
    Lf, _Cf = filter_components(R, omega_d)

    # Accumulate the six nonzero covariance elements expected from the real,
    # time-stationary spectrum: even block (x,d), odd block (u,s).
    def pieces(y: float) -> tuple[float, float, float, float, float, float]:
        r = math.exp(y)
        omega = omega0 * r
        Y = admittance(omega, R, omega_d)
        den = K - C * omega * omega + 1j * omega * Y
        chi2 = 1.0 / (den.real * den.real + den.imag * den.imag)
        SI = HBAR * omega * coth_stable(HBAR * omega / (2.0 * KB * T0)) * Y.real
        Sx = chi2 * SI / (PHI_BAR * PHI_BAR)
        jac = omega / math.pi  # positive-frequency integral, d omega=omega dy

        Hd = L * C * omega * omega - kappa
        hu = r
        hs = r * (1.0 - (Lf / L) * Hd)

        base = Sx * jac
        return (
            base,              # xx
            hu * hu * base,    # uu
            Hd * Hd * base,    # dd
            hs * hs * base,    # ss
            Hd * base,         # xd
            hu * hs * base,    # us
        )

    vals = []
    for idx in range(6):
        vals.append(
            quad(lambda y, i=idx: pieces(y)[i], -22.0, 22.0,
                 epsabs=0.0, epsrel=5.0e-7, limit=1000)[0]
        )

    xx, uu, dd, ss, xd, us = vals
    M = np.array(
        [
            [xx, 0.0, xd, 0.0],
            [0.0, uu, 0.0, us],
            [xd, 0.0, dd, 0.0],
            [0.0, us, 0.0, ss],
        ],
        dtype=float,
    )
    return M


def corr(a: float, b: float, ab: float) -> float:
    return ab / math.sqrt(a * b)


def main() -> None:
    print("Experiment 03 joint phase/filter quantum-FDT covariance")
    model = DynamicForce(0.6, quick=False)
    cov0 = quantum_covariance(model, 0.6)
    sig0 = cov0["sigma_x"]

    for R in (120.0, 160.0, 250.0, 400.0):
        for alpha in (0.20, 0.35, 0.50, 0.75, 1.00):
            M = covariance_matrix(model, 0.6, R, alpha)
            eig = np.linalg.eigvalsh(M)
            rho_xd = corr(M[0,0], M[2,2], M[0,2])
            rho_us = corr(M[1,1], M[3,3], M[1,3])
            msg = (
                f"R={R:g} ohm, alpha={alpha:.2f}: "
                f"sigx={math.sqrt(M[0,0]):.6f} rad ({math.sqrt(M[0,0])/sig0:.6f} iso), "
                f"sigu={math.sqrt(M[1,1]):.6f}, "
                f"sigd={math.sqrt(M[2,2]):.6f}, sigs={math.sqrt(M[3,3]):.6f}, "
                f"rho_xd={rho_xd:+.6f}, rho_us={rho_us:+.6f}, "
                f"eigmin={float(np.min(eig)):.3e}"
            )
            print(msg)
            print(f"::notice title=Experiment 03 joint filter covariance::{msg}")

    print("PASS")


if __name__ == "__main__":
    main()
