#!/usr/bin/env python3
"""Reproduce the Experiment-03 biased rf-SQUID bifurcation checkpoint.

Model
-----
Set phi_x = pi + delta, x = phi - pi, and phi0 = 0.  In units of
E_L = (Phi0/2pi)^2/L,

    u(x) = 0.5 (x-delta)^2 + beta cos(x),
    beta = 2 pi L Ic / Phi0.

The left metastable well disappears at a saddle-node satisfying

    delta = tan(a) - a,
    beta_c = sec(a),

with x_c = -a.

This script computes the exact cold stationary points, barriers, flux/current
separation, local plasma frequency, a provisional cubic-barrier MQT exponent,
and a simple deterministic RCSJ tipping simulation under a square beta pulse.
The MQT prefactor/exponent are diagnostics only, not a validated device DCR.
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

H = 6.62607015e-34
HBAR = H / (2.0 * np.pi)
E_CHARGE = 1.602176634e-19
PHI0 = H / (2.0 * E_CHARGE)
KB = 1.380649e-23


def saddle_node(delta: float):
    a = brentq(lambda z: np.tan(z) - z - delta, 1e-12, np.pi / 2 - 1e-10)
    return a, 1.0 / np.cos(a)


def u(x, beta, delta):
    return 0.5 * (x - delta) ** 2 + beta * np.cos(x)


def stationary_points(beta, delta):
    xs = np.linspace(-2.5 * np.pi, 2.5 * np.pi, 50001)
    vals = xs - delta - beta * np.sin(xs)
    roots = []
    for i in range(len(xs) - 1):
        if vals[i] == 0.0 or vals[i] * vals[i + 1] < 0.0:
            r = brentq(lambda x: x - delta - beta * np.sin(x), xs[i], xs[i + 1])
            if not roots or abs(r - roots[-1]) > 1e-8:
                roots.append(r)
    return roots


def cold_metrics(delta=0.05, beta0=1.5, Ic0=3e-6, C=200e-15):
    a, beta_c = saddle_node(delta)
    L = beta0 * PHI0 / (2.0 * np.pi * Ic0)
    E_L = (PHI0 / (2.0 * np.pi)) ** 2 / L
    roots = stationary_points(beta0, delta)
    if len(roots) != 3:
        raise RuntimeError(f"Expected three stationary points, found {roots}")
    x_left, x_saddle, x_right = roots

    barrier_left = (u(x_saddle, beta0, delta) - u(x_left, beta0, delta)) * E_L
    barrier_right = (u(x_saddle, beta0, delta) - u(x_right, beta0, delta)) * E_L
    well_bias = (u(x_left, beta0, delta) - u(x_right, beta0, delta)) * E_L

    delta_flux = PHI0 * (x_right - x_left) / (2.0 * np.pi)
    delta_current = delta_flux / L

    curvature_left = 1.0 - beta0 * np.cos(x_left)
    omega_left = np.sqrt(curvature_left / (L * C))
    fp_left = omega_left / (2.0 * np.pi)

    # Standard cubic-barrier diagnostic used in the preceding exploratory model.
    # Do not interpret as an exact dissipative rf-SQUID dark-count prediction.
    B_mqt = 7.2 * barrier_left / (HBAR * omega_left)

    return {
        "a": a,
        "beta_c": beta_c,
        "q_required": 1.0 - beta_c / beta0,
        "L": L,
        "E_L_over_kB": E_L / KB,
        "x_left": x_left,
        "x_saddle": x_saddle,
        "x_right": x_right,
        "barrier_left_over_kB": barrier_left / KB,
        "barrier_right_over_kB": barrier_right / KB,
        "well_bias_over_kB": well_bias / KB,
        "delta_flux_over_phi0": delta_flux / PHI0,
        "delta_current": delta_current,
        "fp_left": fp_left,
        "B_mqt_diagnostic": B_mqt,
        "sqrt_LC": np.sqrt(L * C),
    }


def local_barrier_asymptotic(delta, beta):
    """Near-saddle-node metastable barrier for beta > beta_c."""
    a, beta_c = saddle_node(delta)
    mu = beta - beta_c
    if mu <= 0:
        return 0.0
    coefficient = (2.0 ** 2.5 / 3.0) * np.sin(a) * np.sqrt(np.cos(a))
    return coefficient * mu ** 1.5  # in E_L units


def tipping_simulation(delta=0.05, beta_cold=1.5, beta_hot=1.05,
                       alpha=0.01, hot_duration_s=5e-9,
                       Ic0=3e-6, C=200e-15):
    """Dimensionless deterministic RCSJ pulse simulation.

    Equation in s=t/sqrt(LC):
        x'' + alpha x' + x - delta - beta(s) sin(x) = 0.
    alpha = sqrt(L/C)/R_eff.
    """
    m = cold_metrics(delta=delta, beta0=beta_cold, Ic0=Ic0, C=C)
    tau0 = m["sqrt_LC"]
    s_hot = hot_duration_s / tau0
    x0 = m["x_left"]

    def rhs(s, y):
        beta = beta_hot if s < s_hot else beta_cold
        x, v = y
        return (v, -alpha * v - x + delta + beta * np.sin(x))

    s_end = s_hot + max(5000.0, 20.0 / max(alpha, 1e-6))
    sol = solve_ivp(rhs, (0.0, s_end), (x0, 0.0), rtol=1e-9, atol=1e-11,
                    max_step=max(0.05, s_hot / 5000.0))
    x = sol.y[0]
    t = sol.t * tau0
    crossed = np.where(x > 0.0)[0]
    t_cross = t[crossed[0]] if crossed.size else np.nan
    return t_cross, x[-1], sol.y[1, -1]


def main():
    m = cold_metrics()
    print("Experiment 03 rf-SQUID bifurcation benchmark")
    for key, val in m.items():
        if key == "L":
            print(f"{key:28s} = {val * 1e12:.6f} pH")
        elif key == "delta_current":
            print(f"{key:28s} = {val * 1e6:.6f} uA")
        elif key == "fp_left":
            print(f"{key:28s} = {val / 1e9:.6f} GHz")
        elif key == "sqrt_LC":
            print(f"{key:28s} = {val * 1e12:.6f} ps")
        else:
            print(f"{key:28s} = {val:.9g}")

    print("\nNear-SN asymptotic check")
    delta = 0.05
    _, beta_c = saddle_node(delta)
    for mu in [1e-4, 1e-3, 1e-2]:
        beta = beta_c + mu
        roots = stationary_points(beta, delta)
        x_left, x_saddle, _ = roots
        exact = u(x_saddle, beta, delta) - u(x_left, beta, delta)
        approx = local_barrier_asymptotic(delta, beta)
        print(f"mu={mu:.0e}: exact/E_L={exact:.8e}, asymptotic={approx:.8e}, ratio={approx/exact:.6f}")

    print("\nDeterministic tipping")
    for alpha in [0.003, 0.01, 0.03, 0.1]:
        t_cross, x_final, v_final = tipping_simulation(alpha=alpha)
        print(f"alpha={alpha:.3f}: first x>0 at {t_cross*1e12:.3f} ps; x_final={x_final:.6f}; v_final={v_final:.3e}")


if __name__ == "__main__":
    main()
