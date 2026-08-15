#!/usr/bin/env python3
"""Full deterministic Experiment-03 CPR/RCSJ pulse solver.

Purpose
-------
Replace the local saddle-node/ghost diagnostic with a direct deterministic
integration of

    L C x_ddot + (L/R) x_dot + F[x,T_e(t)] = 0

where F is precomputed from the arbitrary-length ballistic graphene CPR, then
empirically de-skewed toward the Nanda realistic-interface S~0.27 envelope.

The thermal pulse is represented in u=T_e^2.  For the retained conditional
clean-graphene model

    C_e = gamma A T,
    P_e-ph = Sigma A (T^4-T0^4),

we use

    du/dt = S_u(t) - (u^2-u0^2)/(2 tau0 u0).

For an exponential energy-deposition pulse of rise time tau_r,

    S_u(t) = Delta_u/tau_r exp(-t/tau_r),

so the integrated deposited energy equals the photon-calibrated Delta_u in the
absence of simultaneous cooling.  tau0=75 ns is the *conditional* Huang
mapping documented in HUANG_THERMAL_DWELL_CALIBRATION_2026-08-15.md; it is not
a claim of a measured temperature-independent hot-state lifetime.

The two retained r_Delta points use the retuned L and provisional C_min,Q from
the current static family.  This is still not a calibrated fabricated-device
simulation because:

- the CPR uses ballistic rigid-boundary theory plus a shape-only interface stress;
- scalar R replaces the real causal frequency-dependent admittance;
- C is inherited from the provisional cubic-MQT diagnostic;
- stochastic forces, dissipative MQT and readout backaction are absent.

Nevertheless it is a materially stronger deterministic test than the local
fold normal form because it retains the full nonlinear phase force, inertia,
finite thermal rise, cooling, barrier re-formation and basin capture.
"""

from __future__ import annotations

import argparse
import math

import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import CubicSpline, RectBivariateSpline
from scipy.optimize import brentq

KB_EV = 8.617333262e-5
DELTA_BASE_EV = 1.3e-3
T0 = 0.020
TAU0_CONDITIONAL = 75.0e-9
ELL0 = 1.1
MU0 = 20.0
DELTA_TILT = 0.05
BETA_COLD = 0.8
LAMBDA_MIX = 0.590  # cold S~0.27 scale in current interface sensitivity model

# Current retuned family: rDelta -> (L, provisional Cmin,Q, static Tf checkpoint)
CASES = {
    0.8: (96.8e-12, 181.0e-15, 0.813),
    0.6: (111.5e-12, 215.0e-15, 0.695),
}


def gap_ratio_bcs(T: float, delta_ev: float) -> float:
    Tc = delta_ev / (1.764 * KB_EV)
    if T >= Tc:
        return 0.0
    return float(np.tanh(1.74 * np.sqrt(Tc / T - 1.0)))


def secular_rhs(z: np.ndarray, Q: np.ndarray, ell: float, mu_r: float,
                gap_ratio: float) -> np.ndarray:
    """Titov-Beenakker arbitrary-length secular RHS on complex energy."""
    alpha_p = np.arcsin(Q / (ell * (z + mu_r)))
    alpha_m = np.arcsin(Q / (ell * (-z + mu_r)))
    cp = np.cos(alpha_p)
    cm = np.cos(alpha_m)
    theta_p = ell * (z + mu_r) * cp
    theta_m = ell * (-z + mu_r) * cm
    beta = np.arccos(z / gap_ratio)
    return (
        (
            np.cos(theta_p) * np.cos(theta_m)
            + np.sin(theta_p) * np.sin(theta_m) / (cp * cm)
        )
        * np.cos(2.0 * beta)
        + (
            np.sin(theta_p) * np.cos(theta_m) / cp
            - np.cos(theta_p) * np.sin(theta_m) / cm
        )
        * np.sin(2.0 * beta)
        - np.sin(theta_p)
        * np.sin(theta_m)
        * np.tan(alpha_p)
        * np.tan(alpha_m)
    )


def matsubara_cpr(T: float, r_delta: float, phis: np.ndarray,
                  qmax: float, nq: int, wmax: float) -> np.ndarray:
    """Arbitrary-length CPR in temperature-consistent arbitrary current units."""
    delta_ev = DELTA_BASE_EV * r_delta
    gr = gap_ratio_bcs(T, delta_ev)
    if gr <= 0.0:
        return np.zeros_like(phis)

    ell = ELL0 * r_delta
    mu_r = MU0 / r_delta
    t = KB_EV * T / delta_ev
    nmax = max(10, int(np.ceil((wmax / (np.pi * t) - 1.0) / 2.0)) + 1)
    omega_n = (2.0 * np.arange(nmax) + 1.0) * np.pi * t
    Q = np.linspace(1.0e-5, qmax, nq)
    G = secular_rhs(1j * omega_n[:, None], Q[None, :], ell, mu_r, gr).real

    currents = []
    for phi in phis:
        q_integral = np.trapezoid(1.0 / (np.cos(phi) - G), Q, axis=1)
        currents.append(t * np.sin(phi) * np.sum(q_integral))
    return np.asarray(currents)


def shifted_periodic_shape(xgrid: np.ndarray, spline: CubicSpline) -> np.ndarray:
    """Periodic odd x=phi-pi CPR shape; reproduces sin(x) for sinusoidal CPR."""
    xr = (xgrid + np.pi) % (2.0 * np.pi) - np.pi
    vals = np.sign(xr) * spline(np.pi - np.abs(xr))
    vals[np.abs(xr) < 1.0e-14] = 0.0
    return vals


class DynamicForce:
    def __init__(self, r_delta: float, *, quick: bool = False,
                 Tmax: float = 0.86):
        self.r_delta = float(r_delta)
        if quick:
            nT, nphi, nq, qmax, wmax, nx = 37, 111, 150, 28.0, 7.0, 1001
        else:
            nT, nphi, nq, qmax, wmax, nx = 55, 141, 220, 30.0, 10.0, 1401

        self.Tgrid = np.linspace(T0, Tmax, nT)
        self.xgrid = np.linspace(-6.1, 6.1, nx)
        phis = np.linspace(0.006, np.pi - 0.006, nphi)

        raw0 = matsubara_cpr(T0, self.r_delta, phis, qmax, nq, wmax)
        Ic0 = float(np.max(raw0))
        Ftab = []

        for T in self.Tgrid:
            raw = matsubara_cpr(float(T), self.r_delta, phis, qmax, nq, wmax)
            Ic = float(np.max(raw))
            ideal_shape = raw / Ic
            mixed = (1.0 - LAMBDA_MIX) * np.sin(phis) + LAMBDA_MIX * ideal_shape
            mixed /= np.max(mixed)
            sp = CubicSpline(phis, mixed)
            shifted = shifted_periodic_shape(self.xgrid, sp)
            ratio = Ic / Ic0
            Ftab.append(
                self.xgrid - DELTA_TILT - BETA_COLD * ratio * shifted
            )

        self.Ftab = np.asarray(Ftab)
        self.spline = RectBivariateSpline(
            self.Tgrid, self.xgrid, self.Ftab, kx=3, ky=3
        )

    def force(self, T: float, x: float) -> float:
        Tuse = min(max(float(T), float(self.Tgrid[0])), float(self.Tgrid[-1]))
        return float(self.spline.ev(Tuse, float(x)))

    def roots(self, T: float) -> list[tuple[float, float]]:
        y = self.spline(T, self.xgrid, grid=False)
        roots: list[float] = []
        for xa, xb, ya, yb in zip(
            self.xgrid[:-1], self.xgrid[1:], y[:-1], y[1:]
        ):
            if ya == 0.0 or ya * yb < 0.0:
                root = brentq(lambda xx: self.force(T, xx), xa, xb)
                if not roots or abs(root - roots[-1]) > 1.0e-6:
                    roots.append(root)
        return [
            (r, float(self.spline.ev(T, r, dx=0, dy=1))) for r in roots
        ]

    def cold_states(self) -> tuple[float, float]:
        roots = self.roots(T0)
        left = max(r for r, k in roots if r < 0.0 and k > 0.0)
        right = min(r for r, k in roots if r > 0.0 and k > 0.0)
        return left, right

    def fold_temperature(self, hi: float = 0.85) -> float:
        def has_left(T: float) -> bool:
            return any(r < 0.0 and k > 0.0 for r, k in self.roots(T))

        lo = T0
        if not has_left(lo) or has_left(hi):
            raise RuntimeError("Fold bracket failed")
        for _ in range(32):
            mid = 0.5 * (lo + hi)
            if has_left(mid):
                lo = mid
            else:
                hi = mid
        return 0.5 * (lo + hi)


def adiabatic_photon_temperature(lambda_um: float, area_um2: float = 100.0) -> float:
    """Huang ratio calibration: 100 um2, 1.55 um -> 2.5 K."""
    return math.sqrt(
        T0 * T0
        + (1.55 / lambda_um)
        * (100.0 / area_um2)
        * (2.5 * 2.5 - T0 * T0)
    )


def simulate(model: DynamicForce, r_delta: float, R: float,
             *, lambda_um: float = 14.0, area_um2: float = 100.0,
             rise_ps: float = 0.0, tend_ns: float = 1.5) -> dict[str, float | str]:
    L, C, _ = CASES[r_delta]
    left, right = model.cold_states()
    Tad = adiabatic_photon_temperature(lambda_um, area_um2)
    u0 = T0 * T0
    du_total = Tad * Tad - u0
    cool_coeff = 1.0 / (2.0 * TAU0_CONDITIONAL * u0)

    if rise_ps <= 0.0:
        y0 = np.array([left, 0.0, Tad * Tad])
        def source(_t: float) -> float:
            return 0.0
    else:
        tau_r = rise_ps * 1.0e-12
        y0 = np.array([left, 0.0, u0])
        def source(t: float) -> float:
            return du_total / tau_r * math.exp(-t / tau_r)

    def rhs(t: float, y: np.ndarray) -> np.ndarray:
        x, v, u = y
        u = max(float(u), u0)
        T = math.sqrt(u)
        F = model.force(T, x)
        du = source(t) - cool_coeff * (u * u - u0 * u0)
        return np.array([v, -((L / R) * v + F) / (L * C), du])

    sol = solve_ivp(
        rhs,
        (0.0, tend_ns * 1.0e-9),
        y0,
        method="DOP853",
        rtol=5.0e-7,
        atol=np.array([2.0e-9, 1.0e3, 1.0e-12]),
        max_step=5.0e-12,
    )

    xf = float(sol.y[0, -1])
    basin = "right" if abs(xf - right) < abs(xf - left) else "left"
    Tpeak = float(np.sqrt(np.max(sol.y[2])))
    return {
        "basin": basin,
        "x_final": xf,
        "x_min": float(np.min(sol.y[0])),
        "x_max": float(np.max(sol.y[0])),
        "Tpeak": Tpeak,
    }


def lower_capture_boundary(model: DynamicForce, r_delta: float, rise_ps: float,
                           Rlo: float, Rhi: float, *, iterations: int = 11) -> float:
    blo = simulate(model, r_delta, Rlo, rise_ps=rise_ps)["basin"]
    bhi = simulate(model, r_delta, Rhi, rise_ps=rise_ps)["basin"]
    if blo == bhi:
        raise RuntimeError("Resistance bracket does not straddle capture boundary")
    for _ in range(iterations):
        mid = 0.5 * (Rlo + Rhi)
        bm = simulate(model, r_delta, mid, rise_ps=rise_ps)["basin"]
        if bm == blo:
            Rlo = mid
        else:
            Rhi = mid
    return 0.5 * (Rlo + Rhi)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--quick", action="store_true")
    args = p.parse_args()

    print("Experiment 03 full deterministic CPR/RCSJ pulse checkpoint")
    print("scalar-R + conditional clean-graphene cooling; NOT a device prediction\n")

    models = {r: DynamicForce(r, quick=args.quick) for r in (0.8, 0.6)}
    for r, m in models.items():
        print(f"rDelta={r:.1f}: interpolated static fold Tf={m.fold_temperature():.4f} K")

    print("\n14-um instantaneous-deposition lower capture boundaries:")
    b08 = lower_capture_boundary(models[0.8], 0.8, 0.0, 110.0, 115.0)
    b06 = lower_capture_boundary(models[0.6], 0.6, 0.0, 32.0, 34.0)
    print(f"rDelta=0.8: R_lower ~{b08:.2f} ohm")
    print(f"rDelta=0.6: R_lower ~{b06:.2f} ohm")

    print("\nFinite thermal-rise sensitivity at 14 um:")
    tests = [
        (0.8, 5.0, [150, 170, 200, 500]),
        (0.8, 9.0, [800, 1150, 1500, 2500]),
        (0.8, 10.0, [500, 1200, 2500, 5000]),
        (0.6, 20.0, [50, 65, 100, 500]),
        (0.6, 30.0, [300, 560, 800, 1500]),
        (0.6, 32.0, [500, 1500, 3000, 10000]),
    ]
    for r, rise, Rs in tests:
        results = [simulate(models[r], r, float(R), rise_ps=rise) for R in Rs]
        caps = [R for R, out in zip(Rs, results) if out["basin"] == "right"]
        peak = max(float(out["Tpeak"]) for out in results)
        print(
            f"r={r:.1f}, rise={rise:4.1f} ps, Tpeak~{peak:.4f} K, "
            f"capturing R samples={caps if caps else 'none'}"
        )

    print("\nInterpretation:")
    print("- full inertia can carry the phase through even when the local overdamped")
    print("  saddle-node ghost estimate predicts failure;")
    print("- finite thermal rise suppresses the nonadiabatic kick and creates a new")
    print("  capture boundary;")
    print("- some successful finite-rise trajectories have Tpeak below the static Tf,")
    print("  so static fold crossing is neither necessary nor sufficient in this")
    print("  nonadiabatic deterministic model;")
    print("- the next physical replacement is scalar R -> causal Y(omega,T) plus FDT")
    print("  noise and dissipative MQT.")


if __name__ == "__main__":
    main()
