#!/usr/bin/env python3
"""Causal passive two-pole environment for Experiment 03.

Purpose
-------
Replace the unphysical infinite-bandwidth scalar resistor by the lowest-order
passive network used in the next deterministic environment screen:

    port -- L_f --+-- R -- ground
                  |
                  C_f
                  |
                ground

The driving-point impedance is

    Z(s) = s L_f + R/(1+s R C_f)

and Y(s)=1/Z(s).  Choose

    L_f = sqrt(2) R / omega_D
    C_f = 1 / (sqrt(2) R omega_D)

so that, on the real-frequency axis,

    Re Y(omega) = (1/R) / [1 + (omega/omega_D)^4].

Thus the network retains the scalar-R low-frequency damping but suppresses the
high-frequency dissipative spectral density strongly enough that the phase
velocity variance from the quantum FDT integral is ultraviolet convergent.

This script is still a deterministic screening model.  The internal filter
states are initialized at their mean cold values (zero).  A full quantum/open-
system probability calculation must include the equilibrium system-bath
covariance and resistor fluctuations consistently.

State variables
---------------
    x      phase coordinate
    v      xdot [s^-1]
    u      T_e^2 [K^2]
    d      L I_env / Phi_bar   (dimensionless port-current force)
    w      V_C / Phi_bar [s^-1]

The deterministic equations are

    L C vdot + d + F(x,T) = 0
    d_dot = (L/L_f) (v-w)
    w_dot = d/(L C_f) - w/(R C_f).

At low frequency d -> (L/R) v, recovering the scalar-R RCSJ equation.

Exact passive energy balance
----------------------------
With E_L=Phi_bar^2/L and dimensionless potential Ux_x=F,

    E/E_L = 1/2 L C v^2 + Ux(x,T)
            + 1/2 (L_f/L) d^2 + 1/2 L C_f w^2,

and

    d(E/E_L)/dt = Ux_T Tdot - (L/R) w^2.

So the only irreversible term is the resistor loss.  Fast voltage that is
rejected by the filter does not get counted as fictitious scalar-R dissipation.
"""

from __future__ import annotations

import argparse
import math

import numpy as np
from scipy.integrate import solve_ivp

from full_dynamic_rfsquid import (
    CASES,
    DynamicForce,
    T0,
    TAU0_CONDITIONAL,
    adiabatic_photon_temperature,
)
from finite_time_basin_slice import cold_phase_scale

SQRT2 = math.sqrt(2.0)


def filter_components(R: float, omega_d: float) -> tuple[float, float]:
    """Return (Lf,Cf) for ReY/G = 1/[1+(omega/omega_d)^4]."""
    if R <= 0.0 or omega_d <= 0.0:
        raise ValueError("R and omega_d must be positive")
    Lf = SQRT2 * R / omega_d
    Cf = 1.0 / (SQRT2 * R * omega_d)
    return Lf, Cf


def re_y_ratio(omega: float, omega_d: float) -> float:
    """ReY(omega)/(1/R), independent of R for this normalized network."""
    r = float(omega) / float(omega_d)
    return 1.0 / (1.0 + r**4)


def simulate_filtered(
    model: DynamicForce,
    r_delta: float,
    R: float,
    alpha: float,
    *,
    x0: float | None = None,
    v0: float = 0.0,
    d0: float = 0.0,
    w0: float = 0.0,
    lambda_um: float = 14.0,
    area_um2: float = 100.0,
    rise_ps: float = 20.0,
    tend_ns: float = 0.8,
) -> dict[str, float | str]:
    """Integrate pulse dynamics with the passive two-pole environment.

    alpha = omega_D/omega_c.  Internal filter variables default to their mean
    cold values.  This is not yet the equilibrium quantum system-bath state.
    """
    L, C, _ = CASES[r_delta]
    left, right = model.cold_states()
    x_c, _, omega_c = cold_phase_scale(model, r_delta)
    if x0 is None:
        x0 = x_c

    omega_d = float(alpha) * omega_c
    Lf, Cf = filter_components(float(R), omega_d)

    Tad = adiabatic_photon_temperature(lambda_um, area_um2)
    u0 = T0 * T0
    du_total = Tad * Tad - u0
    cool_coeff = 1.0 / (2.0 * TAU0_CONDITIONAL * u0)

    if rise_ps <= 0.0:
        y0 = np.array([x0, v0, Tad * Tad, d0, w0], dtype=float)

        def source(_t: float) -> float:
            return 0.0
    else:
        tau_r = rise_ps * 1.0e-12
        y0 = np.array([x0, v0, u0, d0, w0], dtype=float)

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

    fastest = max(omega_c, omega_d)
    max_step = min(2.0e-12, 0.08 / fastest)
    sol = solve_ivp(
        rhs,
        (0.0, tend_ns * 1.0e-9),
        y0,
        method="DOP853",
        rtol=5.0e-7,
        atol=np.array([2.0e-9, 1.0e3, 1.0e-12, 2.0e-9, 1.0e3]),
        max_step=max_step,
    )

    xf = float(sol.y[0, -1])
    basin = "right" if abs(xf - right) < abs(xf - left) else "left"
    return {
        "basin": basin,
        "x_final": xf,
        "v_final": float(sol.y[1, -1]),
        "d_final": float(sol.y[3, -1]),
        "w_final": float(sol.y[4, -1]),
        "Tpeak": float(np.sqrt(np.max(sol.y[2]))),
        "omega_c": omega_c,
        "omega_d": omega_d,
        "Lf": Lf,
        "Cf": Cf,
        "rey_at_omegac_ratio": re_y_ratio(omega_c, omega_d),
    }


def report_family(
    model: DynamicForce,
    r_delta: float,
    rise_ps: float,
    Rs: list[float],
    alphas: list[float],
) -> None:
    _, _, omega_c = cold_phase_scale(model, r_delta)
    print(
        f"\nrDelta={r_delta:.1f}, rise={rise_ps:g} ps, "
        f"omega_c/2pi={omega_c/(2*math.pi)*1e-9:.3f} GHz"
    )
    print(
        "R[ohm] alpha wd/wc ReY(wc)/G Lf[nH] Cf[fF] basin x_final"
    )
    for R in Rs:
        for alpha in alphas:
            out = simulate_filtered(
                model,
                r_delta,
                R,
                alpha,
                rise_ps=rise_ps,
            )
            print(
                f"{R:7.1f} {alpha:5.2f} {alpha:5.2f} "
                f"{float(out['rey_at_omegac_ratio']):10.5f} "
                f"{float(out['Lf'])*1e9:7.3f} "
                f"{float(out['Cf'])*1e15:7.3f} "
                f"{str(out['basin']):5s} {float(out['x_final']):+.6f}"
            )


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--quick", action="store_true")
    args = p.parse_args()

    print("Experiment 03 causal passive two-pole environment screen")
    print("ReY/G = 1/[1+(omega/omega_D)^4]")
    print("Internal bath states initialized at mean zero: deterministic screen only.")

    # Focus first on the family that survived the initial-Wigner screen.
    m06 = DynamicForce(0.6, quick=args.quick)
    report_family(
        m06,
        0.6,
        20.0,
        Rs=[75.0, 120.0, 160.0, 250.0, 400.0],
        alphas=[0.20, 0.35, 0.50, 0.75, 1.00, 1.50, 3.00],
    )

    print("\nInterpretation:")
    print("  alpha -> infinity approaches scalar-R damping over the phase band.")
    print("  alpha < 1 suppresses fast dissipative loading while preserving DC damping.")
    print("  Any favorable deterministic region must still survive system-bath quantum")
    print("  covariance, FDT noise and dissipative quantum escape before it is physical.")


if __name__ == "__main__":
    main()
