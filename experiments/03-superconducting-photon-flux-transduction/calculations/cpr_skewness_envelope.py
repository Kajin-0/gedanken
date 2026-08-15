#!/usr/bin/env python3
"""Empirical CPR-skewness envelope for Experiment 03.

Purpose
-------
Test whether a measured graphene CPR skewness S is sufficient to determine the
rf-SQUID fold.  It is not.

We use a low-order time-reversal-symmetric Fourier family

    I(phi) = sin(phi) + a2 sin(2 phi) + a3 sin(3 phi),

normalize each CPR by its critical current, and impose a target skewness

    S = (2 phi_max - pi)/pi

by analytically choosing a2(a3) so that dI/dphi=0 at the desired phi_max.
We then retain only CPRs that are positive on 0<phi<pi and have the target as
their single interior maximum.

For each accepted CPR we compute:
- endpoint/tail slope chi_pi = -I'(pi)/Ic = f'(0),
- endpoint cubic coefficient zeta_pi = I'''(pi)/Ic = -f'''(0),
- exact tilted rf-SQUID fold beta_fold at delta=0.05,
- small-delta local fold approximation,
- cold bistability/barrier/readout/MQT diagnostic for selected beta_cold.

This is an empirical-shape sensitivity envelope, not a fit to any one graphene
junction.  Its main use is to show that conventional CPR skewness does not fix
the near-pi slope that controls the fold.
"""

from __future__ import annotations

import argparse
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import lambertw

H = 6.62607015e-34
HBAR = H / (2.0 * math.pi)
E_CHARGE = 1.602176634e-19
PHI0 = H / (2.0 * E_CHARGE)
KB = 1.380649e-23

DELTA = 0.05
IC_PHYS = 3.0e-6
D_TARGET = 1.0e-6
ALPHA_Q = 7.2


def a2_for_target_skew(a3: float, S: float) -> float:
    phi_m = 0.5 * math.pi * (1.0 + S)
    den = 2.0 * math.cos(2.0 * phi_m)
    return -(math.cos(phi_m) + 3.0 * a3 * math.cos(3.0 * phi_m)) / den


def physical_current(phi, a2, a3):
    return np.sin(phi) + a2 * np.sin(2.0 * phi) + a3 * np.sin(3.0 * phi)


def accepted_cpr(a3: float, S: float, tol_S=2.0e-3):
    a2 = a2_for_target_skew(a3, S)
    phi_m_target = 0.5 * math.pi * (1.0 + S)
    ph = np.linspace(1.0e-5, math.pi - 1.0e-5, 8000)
    I = physical_current(ph, a2, a3)
    if float(np.min(I)) < -1.0e-6:
        return None

    imax = int(np.argmax(I))
    S_num = 2.0 * ph[imax] / math.pi - 1.0
    if abs(S_num - S) > tol_S:
        return None

    def dI(phi):
        return math.cos(phi) + 2.0 * a2 * math.cos(2.0 * phi) + 3.0 * a3 * math.cos(3.0 * phi)

    maxima = []
    y0 = dI(float(ph[0]))
    for xa, xb in zip(ph[:-1], ph[1:]):
        y1 = dI(float(xb))
        if y0 * y1 < 0.0:
            root = brentq(dI, float(xa), float(xb))
            second = (
                -math.sin(root)
                - 4.0 * a2 * math.sin(2.0 * root)
                - 9.0 * a3 * math.sin(3.0 * root)
            )
            if second < 0.0:
                maxima.append(root)
        y0 = y1

    if len(maxima) != 1 or abs(maxima[0] - phi_m_target) > 3.0e-3:
        return None

    norm = float(np.max(I))
    return a2, norm, S_num


def shifted_shape(x, a2, a3, norm):
    # Canonical x=phi-pi convention used by Experiment 03.
    return (
        np.sin(x)
        - a2 * np.sin(2.0 * x)
        + a3 * np.sin(3.0 * x)
    ) / norm


def shifted_slope(x, a2, a3, norm):
    return (
        np.cos(x)
        - 2.0 * a2 * np.cos(2.0 * x)
        + 3.0 * a3 * np.cos(3.0 * x)
    ) / norm


def exact_fold(a2, a3, norm, delta=DELTA):
    def eq(x):
        f = shifted_shape(x, a2, a3, norm)
        fp = shifted_slope(x, a2, a3, norm)
        return x - f / fp - delta

    grid = np.linspace(-1.5, -1.0e-5, 3000)
    roots = []
    y0 = eq(float(grid[0]))
    for xa, xb in zip(grid[:-1], grid[1:]):
        y1 = eq(float(xb))
        if np.isfinite(y0) and np.isfinite(y1) and y0 * y1 < 0.0:
            root = brentq(eq, float(xa), float(xb))
            beta = 1.0 / shifted_slope(root, a2, a3, norm)
            if beta > 0.0 and all(abs(root - r[0]) > 1.0e-6 for r in roots):
                roots.append((root, beta))
        y0 = y1
    if not roots:
        return None
    return min(roots, key=lambda pair: abs(pair[0]))


def tail_descriptors(a2, a3, norm):
    # f'(0) = -I_phys'(pi)/Ic
    chi = (1.0 - 2.0 * a2 + 3.0 * a3) / norm
    # f'''(0) = (-1 + 8 a2 - 27 a3)/norm;
    # define zeta=-f''' so sinusoid has zeta=+1.
    zeta = (1.0 - 8.0 * a2 + 27.0 * a3) / norm
    return chi, zeta


def local_fold_approx(chi, zeta, delta=DELTA):
    if chi <= 0.0 or zeta <= 0.0:
        return float("nan")
    return (1.0 / chi) * (
        1.0
        + 0.5 * (zeta / chi) ** (1.0 / 3.0) * (3.0 * delta) ** (2.0 / 3.0)
    )


def cold_metrics(beta, a2, a3, norm):
    def f(x):
        return float(shifted_shape(x, a2, a3, norm))

    def fp(x):
        return float(shifted_slope(x, a2, a3, norm))

    def force(x):
        return x - DELTA - beta * f(x)

    grid = np.linspace(-math.pi + 1.0e-4, math.pi - 1.0e-4, 7000)
    roots = []
    y0 = force(float(grid[0]))
    for xa, xb in zip(grid[:-1], grid[1:]):
        y1 = force(float(xb))
        if y0 * y1 < 0.0:
            root = brentq(force, float(xa), float(xb))
            if all(abs(root - r) > 1.0e-6 for r in roots):
                roots.append(root)
        y0 = y1

    curvature = [1.0 - beta * fp(r) for r in roots]
    minima = [r for r, k in zip(roots, curvature) if k > 0.0]
    saddles = [r for r, k in zip(roots, curvature) if k < 0.0]
    lefts = [r for r in minima if r < 0.0]
    rights = [r for r in minima if r > 0.0]
    if not lefts or not rights or not saddles:
        return None

    left = max(lefts)
    right = min(rights)
    saddle = min(saddles, key=abs)

    L = beta * PHI0 / (2.0 * math.pi * IC_PHYS)
    E_L = (PHI0 / (2.0 * math.pi)) ** 2 / L
    barrier = quad(force, left, saddle, epsabs=1.0e-10)[0] * E_L
    kappa = 1.0 - beta * fp(left)
    delta_flux = (right - left) / (2.0 * math.pi)
    delta_current = delta_flux * PHI0 / L

    z = ALPHA_Q * barrier / (2.0 * math.pi * HBAR * D_TARGET)
    W = float(lambertw(z).real)
    Cmin = (
        HBAR * math.sqrt(kappa / L) * W / (ALPHA_Q * barrier)
    ) ** 2

    return {
        "barrier_K": barrier / KB,
        "Cmin_F": Cmin,
        "delta_flux_phi0": delta_flux,
        "delta_current_A": delta_current,
    }


def envelope(S: float, beta_cold: float, nscan=801):
    rows = []
    for a3 in np.linspace(-1.0, 1.0, nscan):
        accepted = accepted_cpr(float(a3), S)
        if accepted is None:
            continue
        a2, norm, S_num = accepted
        fold = exact_fold(a2, float(a3), norm)
        if fold is None:
            continue
        chi, zeta = tail_descriptors(a2, float(a3), norm)
        approx = local_fold_approx(chi, zeta)
        cold = cold_metrics(beta_cold, a2, float(a3), norm)
        rows.append({
            "a3": float(a3),
            "a2": a2,
            "S": S_num,
            "chi": chi,
            "zeta": zeta,
            "x_fold": fold[0],
            "beta_fold": fold[1],
            "beta_fold_local": approx,
            "cold": cold,
        })
    return rows


def describe(S, beta):
    rows = envelope(S, beta)
    if not rows:
        print(f"S={S:.3f}: no accepted CPR family members")
        return

    b = np.asarray([r["beta_fold"] for r in rows])
    chi = np.asarray([r["chi"] for r in rows])
    a3 = np.asarray([r["a3"] for r in rows])
    approx_err = np.asarray([
        (r["beta_fold_local"] / r["beta_fold"] - 1.0)
        for r in rows if np.isfinite(r["beta_fold_local"])
    ])
    stable = [r for r in rows if r["cold"] is not None]

    print(f"\nTarget skewness S={S:.3f}; beta_cold={beta:.3f}")
    print(f"accepted three-harmonic CPRs     = {len(rows)}")
    print(f"a3 range                         = [{a3.min():+.4f}, {a3.max():+.4f}]")
    print(f"tail slope chi_pi range          = [{chi.min():.4f}, {chi.max():.4f}]")
    print(f"exact beta_fold range            = [{b.min():.4f}, {b.max():.4f}]")
    if approx_err.size:
        print(f"local tail formula max |error|  = {100*np.max(np.abs(approx_err)):.2f} %")
    print(f"members bistable at beta_cold   = {len(stable)} / {len(rows)}")

    if stable:
        barriers = np.asarray([r["cold"]["barrier_K"] for r in stable])
        cmins = np.asarray([r["cold"]["Cmin_F"] for r in stable])
        dphis = np.asarray([r["cold"]["delta_flux_phi0"] for r in stable])
        print(f"cold barrier range              = [{barriers.min():.4g}, {barriers.max():.4g}] k_B K")
        print(f"provisional Cmin_Q range        = [{cmins.min()*1e15:.3g}, {cmins.max()*1e15:.3g}] fF")
        print(f"state separation range          = [{dphis.min():.4f}, {dphis.max():.4f}] Phi0")

    # Find family member closest to beta_fold=beta_cold.
    idx = int(np.argmin(np.abs(b - beta)))
    r = rows[idx]
    print("fold-boundary family member:")
    print(
        f"  a2={r['a2']:+.5f}, a3={r['a3']:+.5f}, "
        f"chi_pi={r['chi']:.5f}, zeta_pi={r['zeta']:.5f}, "
        f"beta_fold={r['beta_fold']:.5f}"
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--beta", type=float, default=0.8)
    args = parser.parse_args()

    print("Experiment 03 empirical CPR-skewness envelope")
    print("Fourier family: sin(phi)+a2 sin(2phi)+a3 sin(3phi)")
    print("Constraints: target S, positive 0<phi<pi, single interior maximum")
    print(f"delta={DELTA:.3f}, physical Ic scale={IC_PHYS*1e6:.1f} uA")

    for S in (0.10, 0.15, 0.23, 0.27):
        describe(S, args.beta)

    print("\nKey interpretation:")
    print("Skewness S fixes phi_max but does not fix the near-pi CPR slope chi_pi.")
    print("The rf-SQUID fold is controlled by the load-line tangency near the CPR tail.")
    print("For the same measured S=0.27, acceptable three-harmonic CPRs span both")
    print("sides of beta_fold=0.8.  Thus S alone cannot certify bistability or the")
    print("cold barrier.  Direct tail-slope / harmonic information is required.")


if __name__ == "__main__":
    main()
