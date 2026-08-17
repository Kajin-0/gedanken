#!/usr/bin/env python3
"""Static nonlinear-system basis preflight for variable-pole Gate C.1.

No open-system nonlinear dynamics are performed here. The purpose is to choose
an unrestricted nonlinear detector basis using only the already validated cold
phase-DVR physics before any Gate-C.1 trajectory/state result is seen.

The calculation asks how well the lowest full-double-well eigenstates represent
(i) the validated left-well thermal preparation and (ii) the states obtained by
applying the physical bath-coupling coordinate y=x-x_m and the projected
Caldeira-Leggett counterterm coordinate y^2.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

import full_dynamic_rfsquid as fd
import phase_dvr_basis_convergence as dvr
from quantum_initial_capture import KB

DELTA = 0.21200
RSC = dvr.ROOTS[DELTA]
L = dvr.L0
C = dvr.C0 * RSC * RSC
T0 = fd.T0
CANDIDATES = (12, 16, 24, 32, 48, 64, 80, 96)


def embed_state(xsrc: np.ndarray, psi: np.ndarray, xdst: np.ndarray) -> np.ndarray:
    y = np.interp(xdst, xsrc, np.real(psi), left=0.0, right=0.0)
    y = y + 1j * np.interp(xdst, xsrc, np.imag(psi), left=0.0, right=0.0)
    dx = float(xdst[1] - xdst[0])
    norm = math.sqrt(float(np.sum(np.abs(y) ** 2) * dx))
    if norm <= 0.0:
        raise RuntimeError("embedded left state vanished")
    return y / norm


def projector_coefficients(vec: np.ndarray, fields: np.ndarray, dx: float) -> np.ndarray:
    return vec.conj().T @ fields * dx


def thermal_weights(e: np.ndarray) -> np.ndarray:
    z = np.exp(-(np.asarray(e, float) - float(e[0])) / (KB * T0))
    z /= z.sum()
    return z


def weighted_grid_norm(fields: np.ndarray, weights: np.ndarray, dx: float) -> float:
    norms = np.sum(np.abs(fields) ** 2, axis=0) * dx
    return float(np.dot(weights, norms))


def weighted_retained_norm(coeff: np.ndarray, weights: np.ndarray, n: int) -> float:
    norms = np.sum(np.abs(coeff[:n, :]) ** 2, axis=0)
    return float(np.dot(weights, norms))


def projected_density(coeff: np.ndarray, weights: np.ndarray, n: int):
    c = coeff[:n, :]
    rho = (c * weights[None, :]) @ c.conj().T
    rho = 0.5 * (rho + rho.conj().T)
    tr = float(np.real(np.trace(rho)))
    if tr <= 0.0:
        raise RuntimeError("projected preparation has zero trace")
    return rho / tr, tr


def run(max_basis: int, full_xmax: float, full_ngrid: int, left_states: int):
    if max_basis < max(CANDIDATES):
        raise ValueError(f"max_basis must be >= {max(CANDIDATES)}")

    ob, ot = fd.BETA_COLD, fd.DELTA_TILT
    original = fd.CASES[.6]
    try:
        fd.BETA_COLD = 0.80
        fd.DELTA_TILT = DELTA
        fd.CASES[.6] = (L, C, original[2])
        model = fd.DynamicForce(.6, quick=False, Tmax=1.02)
        roots = model.roots(T0)
        mins = [(x, k) for x, k in roots if k > 0]
        saddles = [(x, k) for x, k in roots if k < 0]
        xm = max(x for x, k in mins if x < 0)
        xr = min(x for x, k in mins if x > 0)
        xs = min(saddles, key=lambda z: abs(z[0]))[0]
        km = float(np.asarray(model.spline.ev(T0, xm, dx=0, dy=1)).reshape(-1)[0])
        wc = math.sqrt(km / (L * C))

        xl, _Ul, el, vl, resl = dvr.spectrum(
            model, T0, C, -3.8, xs, 2200, left_states
        )
        weights = thermal_weights(el)

        xf, _Uf, ef, vf, resf = dvr.spectrum(
            model, T0, C, -full_xmax, full_xmax, full_ngrid, max_basis
        )
        dxf = float(xf[1] - xf[0])
        psi = np.column_stack([embed_state(xl, vl[:, j], xf) for j in range(left_states)])
        y = xf - xm
        ypsi = y[:, None] * psi
        y2psi = (y * y)[:, None] * psi

        c0 = projector_coefficients(vf, psi, dxf)
        c1 = projector_coefficients(vf, ypsi, dxf)
        c2 = projector_coefficients(vf, y2psi, dxf)
        exact0 = weighted_grid_norm(psi, weights, dxf)
        exact1 = weighted_grid_norm(ypsi, weights, dxf)
        exact2 = weighted_grid_norm(y2psi, weights, dxf)

        Y = vf.conj().T @ (y[:, None] * vf) * dxf
        Y2 = vf.conj().T @ ((y * y)[:, None] * vf) * dxf
        basin = (xf < xs).astype(float)
        PL = vf.conj().T @ (basin[:, None] * vf) * dxf
        Y = 0.5 * (Y + Y.conj().T)
        Y2 = 0.5 * (Y2 + Y2.conj().T)
        PL = 0.5 * (PL + PL.conj().T)

        rows = []
        for n in CANDIDATES:
            rho, retained0 = projected_density(c0, weights, n)
            r1 = weighted_retained_norm(c1, weights, n) / exact1
            r2 = weighted_retained_norm(c2, weights, n) / exact2
            pl = float(np.real(np.trace(rho @ PL[:n, :n])))
            mean_y = float(np.real(np.trace(rho @ Y[:n, :n])))
            mean_y2 = float(np.real(np.trace(rho @ Y2[:n, :n])))
            sigma_y = math.sqrt(max(mean_y2 - mean_y * mean_y, 0.0))
            top = float(np.real(rho[-1, -1]))
            rows.append(dict(
                basis_dim=n,
                prep_retained=retained0 / exact0,
                prep_loss=max(0.0, 1.0 - retained0 / exact0),
                y_image_retained=r1,
                y_image_loss=max(0.0, 1.0 - r1),
                y2_image_retained=r2,
                y2_image_loss=max(0.0, 1.0 - r2),
                left_basin=pl,
                mean_y=mean_y,
                sigma_y=sigma_y,
                top_population=top,
            ))
            print(
                f"C1_NONLINEAR_BASIS dim={n} prepLoss={1-retained0/exact0:.12e} "
                f"yLoss={1-r1:.12e} y2Loss={1-r2:.12e} "
                f"PL={pl:.12e} meanY={mean_y:+.12e} sigmaY={sigma_y:.12e} "
                f"topPop={top:.12e}", flush=True)

        return dict(
            purpose="static nonlinear detector-basis preflight before open Gate C.1",
            nonlinear_open_dynamics_used=False,
            delta=DELTA, r=RSC, C_F=C, T0_K=T0,
            xm=xm, xs=xs, xr=xr, wc_rad_s=wc, fc_Hz=wc/(2*math.pi),
            full_xmax=full_xmax, full_ngrid=full_ngrid, max_basis=max_basis,
            left_states=left_states, left_weights=weights.tolist(),
            max_left_eigen_residual_K=float(np.max(resl)),
            max_full_eigen_residual_K=float(np.max(resf)),
            full_transition_K=((ef-ef[0])/KB).tolist(), rows=rows,
        )
    finally:
        fd.BETA_COLD = ob
        fd.DELTA_TILT = ot
        fd.CASES[.6] = original


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-basis", type=int, default=96)
    ap.add_argument("--full-xmax", type=float, default=4.2)
    ap.add_argument("--full-ngrid", type=int, default=2600)
    ap.add_argument("--left-states", type=int, default=12)
    ap.add_argument("--json", default="variable_pole_c1_nonlinear_basis_preflight.json")
    args = ap.parse_args()

    out = run(args.max_basis, args.full_xmax, args.full_ngrid, args.left_states)
    Path(args.json).write_text(json.dumps(out, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    if out["max_left_eigen_residual_K"] > 2e-7 or out["max_full_eigen_residual_K"] > 2e-7:
        raise RuntimeError("DVR eigen residual regression")
    print(f"C1_NONLINEAR_BASIS_JSON={args.json}", flush=True)
    print("VARIABLE_POLE_C1_NONLINEAR_BASIS_PREFLIGHT_PASS", flush=True)


if __name__ == "__main__":
    main()
