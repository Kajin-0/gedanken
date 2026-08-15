#!/usr/bin/env python3
"""Arbitrary-length ballistic graphene Josephson CPR for Experiment 03.

Physics source
--------------
Titov & Beenakker, Phys. Rev. B 74, 041401(R) (2006), Eq. (14), gives the
Andreev-level secular equation for a ballistic graphene SNS junction with
heavily doped superconducting electrodes. Hagymasi, Kormanyos & Cserti,
Phys. Rev. B 82, 134516 (2010), Eqs. (5)-(6), evaluate the finite-temperature
Josephson current from that secular equation using a Matsubara sum and note
that the method is valid for arbitrary junction length.

This script implements the wide-junction continuum version of that ideal model.
It assumes rigid superconducting boundaries and ideal ballistic graphene.
It is therefore a model checkpoint, NOT a calibrated model of the 600-nm
MoRe/graphene photon detector.

Dimensionless parameters
------------------------
ell = L/xi0 = Delta0 L/(hbar vF)
mu  = chemical potential / Delta0(0)
Q   = q L
z   = epsilon / Delta0(0)
t   = k_B T / Delta0(0)

For Matsubara z=i(2n+1)pi t, the secular equation can be written

    F = cos(phi) - G(z,Q),

where G is the right-hand side of Titov-Beenakker Eq. (14). Since G is
phi-independent,

    d_phi ln F = -sin(phi)/(cos(phi)-G).

Overall degeneracy, W/L and current prefactors cancel from normalized CPR/fold
calculations. The temperature prefactor t is retained because current amplitude
ratios across temperature are physically required.

Outputs
-------
1. Short-junction validation against Titov-Beenakker Eq. (20) at mu=0.
2. Cold fold threshold for ell=1.1 and mu/Delta0 = 0, 10, 20.
3. Fold-temperature table versus beta_cold for mu/Delta0=20.
4. Cold barrier/readout/provisional-MQT table for the same family.

The MQT capacitance is only the existing Experiment-03 cubic-barrier diagnostic,
not an exact dissipative rf-SQUID dark-count prediction.
"""

from __future__ import annotations

import argparse
from functools import lru_cache
import math

import numpy as np
from scipy.integrate import quad
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq
from scipy.special import lambertw

# Exact SI constants.
H = 6.62607015e-34
HBAR = H / (2.0 * np.pi)
E_CHARGE = 1.602176634e-19
PHI0 = H / (2.0 * E_CHARGE)
KB = 1.380649e-23
KB_EV = 8.617333262e-5

# Working superconducting scale motivated by the MoRe photon-detector platform.
DELTA0_EV = 1.3e-3
TC_BCS = DELTA0_EV / (1.764 * KB_EV)
T0 = 0.020

# Numerical defaults. qmax~30 is needed for convergence at mu/Delta0~20.
DEFAULT_QMAX = 30.0
DEFAULT_NQ = 500
DEFAULT_WMAX = 20.0
DEFAULT_NPHI = 201


def gap_ratio_bcs(T: float) -> float:
    """Approximate Delta(T)/Delta(0) using the standard BCS interpolation."""
    if T >= TC_BCS:
        return 0.0
    return float(np.tanh(1.74 * np.sqrt(TC_BCS / T - 1.0)))


def secular_rhs(z: np.ndarray, Q: np.ndarray, ell: float, mu_r: float,
                gap_ratio: float) -> np.ndarray:
    """Right-hand side G of Titov-Beenakker Eq. (14) at complex energy z.

    z and Q are broadcastable complex/real arrays. All energies are normalized
    to Delta0(0), while Q=qL and ell=L/xi0.
    """
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


def matsubara_cpr(
    T: float,
    ell: float,
    mu_r: float,
    phis: np.ndarray,
    qmax: float = DEFAULT_QMAX,
    nq: int = DEFAULT_NQ,
    wmax: float = DEFAULT_WMAX,
) -> np.ndarray:
    """Return CPR in arbitrary but temperature-consistent current units."""
    gr = gap_ratio_bcs(T)
    if gr <= 0.0:
        return np.zeros_like(phis)

    t = KB_EV * T / DELTA0_EV
    # Retain Matsubara terms through omega_n/Delta0(0) ~ wmax.
    nmax = max(10, int(np.ceil((wmax / (np.pi * t) - 1.0) / 2.0)) + 1)
    omega_n = (2.0 * np.arange(nmax) + 1.0) * np.pi * t

    Q = np.linspace(1.0e-5, qmax, nq)
    z = 1j * omega_n[:, None]
    G = secular_rhs(z, Q[None, :], ell, mu_r, gr)

    # On the Matsubara axis G should be real apart from roundoff. Keep the real
    # part after checking that the imaginary residue is tiny in validation work.
    G = G.real

    currents = []
    for phi in phis:
        kernel = 1.0 / (np.cos(phi) - G)
        q_integral = np.trapezoid(kernel, Q, axis=1)
        currents.append(t * np.sin(phi) * np.sum(q_integral))
    return np.asarray(currents)


class GrapheneCPRModel:
    def __init__(self, ell: float, mu_r: float, delta: float = 0.05,
                 qmax: float = DEFAULT_QMAX, nq: int = DEFAULT_NQ,
                 wmax: float = DEFAULT_WMAX, nphi: int = DEFAULT_NPHI):
        self.ell = float(ell)
        self.mu_r = float(mu_r)
        self.delta = float(delta)
        self.qmax = float(qmax)
        self.nq = int(nq)
        self.wmax = float(wmax)
        self.phis = np.linspace(0.003, np.pi - 0.003, int(nphi))
        self._cache: dict[float, tuple[float, CubicSpline]] = {}

    def cpr(self, T: float) -> tuple[float, CubicSpline]:
        key = round(float(T), 6)
        if key not in self._cache:
            values = matsubara_cpr(
                key, self.ell, self.mu_r, self.phis,
                qmax=self.qmax, nq=self.nq, wmax=self.wmax,
            )
            Ic = float(np.max(values))
            self._cache[key] = (Ic, CubicSpline(self.phis, values / Ic))
        return self._cache[key]

    @staticmethod
    def _shifted_shape(x: float, spline: CubicSpline) -> float:
        """rf-SQUID x=phi-pi convention; shape is odd in x."""
        if x == 0.0:
            return 0.0
        phi = np.pi - abs(x)
        return float(np.sign(x) * spline(phi))

    @staticmethod
    def _shifted_slope(x: float, spline: CubicSpline) -> float:
        phi = np.pi - abs(x)
        return -float(spline(phi, 1))

    def normalized_fold(self, T: float) -> tuple[float, float]:
        """Return (x_fold, beta_fold) for CPR normalized to Ic(T)."""
        _, spline = self.cpr(T)

        def equation(x: float) -> float:
            f = self._shifted_shape(x, spline)
            fp = self._shifted_slope(x, spline)
            return x - f / fp - self.delta

        grid = np.linspace(-1.5, -1.0e-4, 1200)
        candidates = []
        xa, ya = grid[0], equation(grid[0])
        for xb in grid[1:]:
            yb = equation(xb)
            if np.isfinite(ya) and np.isfinite(yb) and ya * yb < 0.0:
                root = brentq(equation, xa, xb)
                beta_fold = 1.0 / self._shifted_slope(root, spline)
                if beta_fold > 0.0:
                    if all(abs(root - old[0]) > 1.0e-5 for old in candidates):
                        candidates.append((root, beta_fold))
            xa, ya = xb, yb

        if not candidates:
            raise RuntimeError("No selected metastable fold found")

        # The photon-relevant left-well fold is the negative root closest to 0.
        return min(candidates, key=lambda pair: abs(pair[0]))

    def beta_required_from_cold(self, T: float, Tcold: float = T0) -> float:
        """Cold beta that would place the circuit exactly at its fold at T."""
        Ic, _ = self.cpr(T)
        Ic0, _ = self.cpr(Tcold)
        _, beta_fold_norm = self.normalized_fold(T)
        return beta_fold_norm / (Ic / Ic0)

    def fold_temperature(self, beta_cold: float, Tmax: float = 4.0) -> float:
        """Solve beta_required_from_cold(T)=beta_cold."""
        cold_req = self.beta_required_from_cold(T0)
        if beta_cold <= cold_req:
            return float("nan")

        prev_T = T0
        prev = cold_req - beta_cold
        for T in np.linspace(0.03, Tmax, 32):
            val = self.beta_required_from_cold(float(T)) - beta_cold
            if prev * val <= 0.0:
                return float(brentq(
                    lambda temp: self.beta_required_from_cold(temp) - beta_cold,
                    prev_T, float(T), xtol=2.0e-4,
                ))
            prev_T, prev = float(T), val
        return float("nan")

    def cold_metrics(self, beta_cold: float, Ic_phys: float = 3.0e-6,
                     D_target: float = 1.0e-6,
                     alpha_q: float = 7.2) -> dict[str, float]:
        """Cold barrier/readout plus provisional MQT capacitance floor."""
        _, spline = self.cpr(T0)

        def f(x: float) -> float:
            return self._shifted_shape(x, spline)

        def fp(x: float) -> float:
            return self._shifted_slope(x, spline)

        def force(x: float) -> float:
            return x - self.delta - beta_cold * f(x)

        grid = np.linspace(-np.pi + 0.005, np.pi - 0.005, 6000)
        roots = []
        xa, ya = grid[0], force(grid[0])
        for xb in grid[1:]:
            yb = force(xb)
            if ya * yb < 0.0:
                root = brentq(force, xa, xb)
                if all(abs(root - old) > 1.0e-6 for old in roots):
                    roots.append(root)
            xa, ya = xb, yb

        curv = [1.0 - beta_cold * fp(r) for r in roots]
        left = max(r for r, c in zip(roots, curv) if r < 0.0 and c > 0.0)
        right = min(r for r, c in zip(roots, curv) if r > 0.0 and c > 0.0)
        saddle = min((r for r, c in zip(roots, curv) if c < 0.0), key=abs)

        barrier_dimless = quad(force, left, saddle, epsabs=1.0e-10)[0]
        curvature = 1.0 - beta_cold * fp(left)

        L = beta_cold * PHI0 / (2.0 * np.pi * Ic_phys)
        E_L = (PHI0 / (2.0 * np.pi)) ** 2 / L
        barrier = barrier_dimless * E_L

        delta_flux_phi0 = (right - left) / (2.0 * np.pi)
        delta_current = delta_flux_phi0 * PHI0 / L

        # Existing Experiment-03 provisional cubic MQT diagnostic only.
        z = alpha_q * barrier / (2.0 * np.pi * HBAR * D_target)
        W = float(lambertw(z).real)
        Cmin = (
            HBAR * np.sqrt(curvature / L) * W / (alpha_q * barrier)
        ) ** 2

        return {
            "left": left,
            "saddle": saddle,
            "right": right,
            "barrier_K": barrier / KB,
            "curvature": curvature,
            "L_H": L,
            "delta_flux_phi0": delta_flux_phi0,
            "delta_current_A": delta_current,
            "Cmin_Q_F": Cmin,
        }


def titov_dirac_short_shape(phi: np.ndarray) -> np.ndarray:
    """Titov-Beenakker Eq. (20), omitting overall current prefactor."""
    return np.cos(phi / 2.0) * np.arctanh(np.sin(phi / 2.0))


def short_limit_validation() -> tuple[float, float]:
    phis = np.linspace(0.03, np.pi - 0.03, 121)
    calc = matsubara_cpr(
        T0, ell=0.01, mu_r=0.0, phis=phis,
        qmax=15.0, nq=600, wmax=20.0,
    )
    calc /= np.max(calc)
    ref = titov_dirac_short_shape(phis)
    ref /= np.max(ref)
    max_abs = float(np.max(np.abs(calc - ref)))
    rms = float(np.sqrt(np.mean((calc - ref) ** 2)))
    return max_abs, rms


def eta_reference(Tfold: float, Tref: float = 2.5, Tbase: float = T0) -> float:
    """Equal-area graphene heat-capacity energy fraction relative to 2.5-K ref."""
    return (Tfold * Tfold - Tbase * Tbase) / (Tref * Tref - Tbase * Tbase)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--quick", action="store_true",
                        help="Use coarser grids for a faster smoke test")
    args = parser.parse_args()

    if args.quick:
        qmax, nq, wmax, nphi = 25.0, 320, 15.0, 141
    else:
        qmax, nq, wmax, nphi = 30.0, 500, 20.0, 201

    print("Experiment 03 arbitrary-length graphene CPR checkpoint")
    print(f"Delta0 = {DELTA0_EV*1e3:.3f} meV; BCS Tc ~ {TC_BCS:.3f} K")
    print(f"grids: qmax={qmax:g}, nq={nq}, wmax={wmax:g}, nphi={nphi}")

    max_abs, rms = short_limit_validation()
    print("\nShort-junction validation, ell=0.01, mu=0:")
    print(f"max normalized CPR deviation from Titov Eq.(20) = {max_abs:.5f}")
    print(f"RMS normalized CPR deviation                     = {rms:.5f}")

    print("\nCold normalized fold, ell=1.1, delta=0.05:")
    models = {}
    for mu_r in (0.0, 10.0, 20.0):
        model = GrapheneCPRModel(
            1.1, mu_r, delta=0.05,
            qmax=qmax, nq=nq, wmax=wmax, nphi=nphi,
        )
        models[mu_r] = model
        xf, bf = model.normalized_fold(T0)
        print(f"mu/Delta0={mu_r:4.0f}: x_fold={xf: .6f}, beta_fold,cold={bf:.6f}")

    print("\nmu/Delta0=20 fold-temperature / cold-stability family:")
    print("beta   Tfold[K]  eta_ref  barrier/kB[K]  Cmin_Q[fF]  dPhi/Phi0  dI[uA]  L[pH]")
    model = models[20.0]
    for beta in (0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.00, 1.20):
        Tf = model.fold_temperature(beta, Tmax=3.0)
        met = model.cold_metrics(beta)
        print(
            f"{beta:4.2f}  {Tf:8.3f}  {eta_reference(Tf):7.4f}  "
            f"{met['barrier_K']:13.3f}  {met['Cmin_Q_F']*1e15:11.1f}  "
            f"{met['delta_flux_phi0']:10.4f}  "
            f"{met['delta_current_A']*1e6:7.3f}  {met['L_H']*1e12:7.2f}"
        )

    print("\nDoping sensitivity at beta_cold=0.8:")
    print("mu/Delta0  beta_fold,cold  Tfold[K]  eta_ref  barrier/kB[K]  Cmin_Q[fF]")
    for mu_r in (0.0, 10.0, 20.0):
        model = models[mu_r]
        _, bfc = model.normalized_fold(T0)
        Tf = model.fold_temperature(0.8, Tmax=3.0)
        met = model.cold_metrics(0.8)
        print(
            f"{mu_r:9.0f}  {bfc:14.6f}  {Tf:8.3f}  "
            f"{eta_reference(Tf):7.4f}  {met['barrier_K']:13.3f}  "
            f"{met['Cmin_Q_F']*1e15:11.1f}"
        )

    print("\nInterpretation:")
    print("- The arbitrary-length ell~1.1 CPR thermally softens much more strongly")
    print("  than the uncontrolled short-junction toy model used earlier.")
    print("- beta_cold~0.8 is a useful illustrative point: in the mu/Delta0=20")
    print("  ideal model it folds near 1.12 K while retaining a ~16.7-kB-K cold")
    print("  barrier and a provisional MQT capacitance floor near 70 fF.")
    print("- These are ideal ballistic/rigid-boundary calculations, not a calibrated")
    print("  prediction for the MoRe/graphene photon detector.")


if __name__ == "__main__":
    main()
