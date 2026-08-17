#!/usr/bin/env python3
"""Harmonic-only system-site Fock cutoff preflight for Experiment-03 C1.

This calculation uses only the already accepted harmonic variable-pole model.
It is deliberately run before the finite-bosonic harmonic MPDO regression and
before any nonlinear C1 open-system evolution.

It reports the exact Gaussian reduced-system density matrix in the bare
harmonic Fock basis, its tail versus candidate local dimensions, and the
accepted enlarged-system drift gap used to choose a fixed equilibration horizon.
No nonlinear detector state is evaluated.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

import variable_pole_c1_harmonic_preflight as pre

CANDIDATES = (4, 6, 8, 10, 12, 14, 16, 20, 24)
RHO_DIM = 96


def main():
    rows, wc, sigma0, ref, c0, sampler_err = pre.regenerate()
    row = rows[16]
    V, lam, lyap = pre.full_harmonic_covariance(row, sigma0)

    rank = 16
    nquad = rank + 1
    Vsys = np.array(
        [[V[0, 0], V[0, nquad]], [V[nquad, 0], V[nquad, nquad]]],
        dtype=float,
    )
    rho, grec = pre.v.era.hg.gaussian_rho_from_cov(Vsys, RHO_DIM)
    rr = np.asarray(rho.full(), complex)
    diag = np.maximum(np.real(np.diag(rr)), 0.0)
    diag /= diag.sum()
    tails = {str(d): max(0.0, float(1.0 - diag[:d].sum())) for d in CANDIDATES}

    nbar = max(0.0, 0.5 * (float(np.trace(Vsys)) - 1.0))
    nu = math.sqrt(max(float(np.linalg.det(Vsys)), 0.0))
    qp_norm = abs(float(Vsys[0, 1])) / max(math.sqrt(Vsys[0, 0] * Vsys[1, 1]), 1e-300)

    bath = dict(
        wc=pre.v.era.WC,
        H=np.asarray(row["opt"]["H"], complex),
        Gamma=np.asarray(row["opt"]["Gamma"], complex),
        g=np.asarray(row["opt"]["g"], complex),
    )
    _Gmat, A, _Diff, _Om, _lam = pre.v.era.hg.enlarged_matrices(bath, sigma0)
    drift_eigs = np.linalg.eigvals(A)
    max_real = float(np.max(drift_eigs.real))
    if max_real >= 0.0:
        raise RuntimeError("accepted enlarged harmonic drift is not stable")
    gap = -max_real

    # Freeze-candidate horizon based only on the linear drift gap.  At tau=240
    # the slowest first-moment transient is bounded by exp(-gap*tau), absent
    # nonnormal amplification.  The later MPDO regression still checks explicit
    # late-time stationarity rather than assuming this estimate is sufficient.
    tau_final = 240.0
    slow_exp = math.exp(-gap * tau_final)

    summary = dict(
        purpose="harmonic-only system Fock cutoff and horizon preflight",
        nonlinear_results_used=False,
        rank=16,
        wc=wc,
        sigma0=sigma0,
        counterterm_lambda=lam,
        exact_sampler_max_relerr=sampler_err,
        lyapunov_residual=lyap,
        system_covariance=Vsys.tolist(),
        system_nbar=nbar,
        system_symplectic_nu=nu,
        normalized_qp=qp_norm,
        gaussian_reconstruction_error=float(grec["recerr"]),
        fock_tails=tails,
        drift_max_real=max_real,
        drift_gap=gap,
        proposed_tau_final=tau_final,
        slow_mode_amplitude_factor_at_tau_final=slow_exp,
    )
    Path("variable_pole_c1_harmonic_system_cutoff.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    print(
        "C1_HARMONIC_SYSTEM "
        f"nbar={nbar:.12e} nu={nu:.12e} qp={qp_norm:.12e} "
        f"Vqq={Vsys[0,0]:.12e} Vpp={Vsys[1,1]:.12e} Vqp={Vsys[0,1]:+.12e} "
        f"recerr={float(grec['recerr']):.12e}",
        flush=True,
    )
    for d in CANDIDATES:
        print(f"C1_HARMONIC_SYSTEM_TAIL dim={d} tail={tails[str(d)]:.12e}", flush=True)
    print(
        f"C1_HARMONIC_DRIFT max_real={max_real:+.12e} gap={gap:.12e} "
        f"tau240_factor={slow_exp:.12e}",
        flush=True,
    )

    if float(grec["recerr"]) >= 1e-12:
        raise RuntimeError("system Gaussian reconstruction is not accurate enough for cutoff preflight")
    if slow_exp >= 2e-6:
        raise RuntimeError("tau=240 drift-gap horizon is not sufficiently asymptotic")
    print("VARIABLE_POLE_C1_HARMONIC_SYSTEM_CUTOFF_PREFLIGHT_PASS", flush=True)


if __name__ == "__main__":
    main()
