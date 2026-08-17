#!/usr/bin/env python3
"""Harmonic-only numerical preflight before variable-pole nonlinear Gate C.1.

This script is intentionally forbidden from evaluating the nonlinear detector
state.  It deterministically regenerates the already accepted optimized rank-16
and rank-24 physical baths, rechecks the frozen harmonic acceptance, archives the
actual (H, Gamma, g) matrices, and reports structure/occupation/truncation metrics
needed to choose a structured finite-bosonic nonlinear solver.

Importing run_variable_pole_physical_opt is deliberate: that module applies the
pre-result exact-C0 initializer normalization required by the accepted run.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy.linalg import solve_continuous_lyapunov, svdvals
import torch

import run_variable_pole_physical_opt as accepted_launch

v = accepted_launch.opt

RANKS = (16, 24)
LOCAL_RHO_DIM = 64
TAIL_DIMS = (2, 3, 4, 6, 8, 12, 16)


def full_harmonic_covariance(row, sigma0: float):
    bath = dict(
        wc=v.era.WC,
        H=np.asarray(row["opt"]["H"], complex),
        Gamma=np.asarray(row["opt"]["Gamma"], complex),
        g=np.asarray(row["opt"]["g"], complex),
    )
    _Gmat, A, Diff, _Om, lam = v.era.hg.enlarged_matrices(bath, sigma0)
    if float(np.max(np.linalg.eigvals(A).real)) >= 0.0:
        raise RuntimeError("accepted bath became unstable in preflight covariance")
    V = solve_continuous_lyapunov(A, -Diff)
    V = np.asarray(np.real_if_close(V, tol=1000), float)
    V = 0.5 * (V + V.T)
    resid = float(
        np.linalg.norm(A @ V + V @ A.T + Diff, ord="fro")
        / max(np.linalg.norm(Diff, ord="fro"), 1.0)
    )
    return V, float(lam), resid


def local_mode_metrics(V: np.ndarray, rank: int):
    """Return harmonic one-mode occupations and Gaussian marginal Fock tails."""
    n = rank + 1
    rows = []
    for j in range(rank):
        q = 1 + j
        p = n + 1 + j
        Vj = np.array([[V[q, q], V[q, p]], [V[p, q], V[p, p]]], float)
        nbar = max(0.0, 0.5 * (float(np.trace(Vj)) - 1.0))
        nu = math.sqrt(max(float(np.linalg.det(Vj)), 0.0))

        # This is an exact one-mode Gaussian marginal diagnostic of the accepted
        # harmonic state.  It is NOT used as a nonlinear tail guarantee.
        rho, grec = v.era.hg.gaussian_rho_from_cov(Vj, LOCAL_RHO_DIM)
        diag = np.real(np.diag(np.asarray(rho.full(), complex)))
        diag = np.maximum(diag, 0.0)
        z = float(diag.sum())
        if z <= 0.0:
            raise RuntimeError(f"mode {j} Gaussian marginal has invalid trace")
        diag /= z
        tails = {
            str(d): max(0.0, float(1.0 - diag[:d].sum()))
            for d in TAIL_DIMS
            if d <= LOCAL_RHO_DIM
        }
        rows.append(
            dict(
                mode=j,
                nbar=nbar,
                nu=nu,
                covariance=Vj.tolist(),
                rho_reconstruction=float(grec["recerr"]),
                tails=tails,
            )
        )
    return rows


def structure_metrics(row):
    H = np.asarray(row["opt"]["H"], complex)
    Gamma = np.asarray(row["opt"]["Gamma"], complex)
    g = np.asarray(row["opt"]["g"], complex)
    n = H.shape[0]
    diagH = np.diag(np.diag(H))
    triH = diagH + np.diag(np.diag(H, 1), 1) + np.diag(np.diag(H, -1), -1)
    diagG = np.diag(np.diag(Gamma))
    nearG = diagG + np.diag(np.diag(Gamma, 1), 1) + np.diag(np.diag(Gamma, -1), -1)
    normH = max(float(np.linalg.norm(H, ord="fro")), 1e-300)
    normG = max(float(np.linalg.norm(Gamma, ord="fro")), 1e-300)
    eg = np.linalg.eigvalsh(Gamma)
    return dict(
        rank=n,
        H_tridiagonal_leak=float(np.linalg.norm(H - triH, ord="fro") / normH),
        Gamma_offdiag_fraction=float(np.linalg.norm(Gamma - diagG, ord="fro") / normG),
        Gamma_beyond_nearest_fraction=float(np.linalg.norm(Gamma - nearG, ord="fro") / normG),
        Gamma_min=float(eg.min()),
        Gamma_max=float(eg.max()),
        Gamma_condition=float(eg.max() / eg.min()),
        g_tail_fraction=float(np.linalg.norm(g[1:]) / max(np.linalg.norm(g), 1e-300)),
        H_min=float(np.linalg.eigvalsh(H).min()),
        H_max=float(np.linalg.eigvalsh(H).max()),
    )


def tensor_product_scaling():
    out = []
    for ns in (8, 10, 12, 16):
        for d in (2, 3, 4):
            D = int(ns * (d ** 16))
            density_elements = D * D
            bytes_complex128 = 16 * density_elements
            out.append(
                dict(
                    system_dim=ns,
                    uniform_aux_dim=d,
                    hilbert_dim=D,
                    density_elements=density_elements,
                    density_bytes_complex128=bytes_complex128,
                    density_TB_decimal=bytes_complex128 / 1e12,
                )
            )
    return out


def regenerate():
    torch.set_default_dtype(torch.float64)
    torch.manual_seed(0)
    torch.set_num_threads(1)

    v.synthetic_oracle()
    wc, sigma0, ref = v.era.physical_wc_sigma0()
    v.era.WC = wc
    sampler_err = v.era.exact_sampler_audit(wc)
    if sampler_err >= 2e-6:
        raise RuntimeError("exact 10000-Matsubara sampler failed preflight audit")

    ttrain = np.arange(2 * v.era.M) * v.era.DT
    samples = v.era.exact_correlation(ttrain, wc)
    v.era.T_EVAL = (np.arange(2 * v.era.M - 1) + 0.5) * v.era.DT
    exact_eval = v.era.exact_correlation(v.era.T_EVAL, wc)
    c0 = float(np.real(samples[0]))
    v.era.X_SPEC = np.linspace(-4.0, 6.0, 2401)
    base_data = v.make_data(wc)

    rows = {}
    for rank in RANKS:
        gg = np.zeros(rank, complex)
        gg[0] = math.sqrt(c0)
        data = dict(base_data)
        data["g"] = torch.tensor(gg, dtype=torch.complex128)
        rows[rank] = v.run_rank(rank, samples, ref, exact_eval, c0, data)

    return rows, float(wc), float(sigma0), ref, float(c0), float(sampler_err)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--npz", default="variable_pole_c1_baths.npz")
    ap.add_argument("--json", default="variable_pole_c1_preflight.json")
    args = ap.parse_args()

    rows, wc, sigma0, ref, c0, sampler_err = regenerate()

    r16 = rows[16]
    r24 = rows[24]
    primary = r16["opt"]["state"]
    control = 0.5 * float(
        np.sum(
            svdvals(
                np.asarray(r24["opt"]["rho"].full(), complex)
                - np.asarray(r16["opt"]["rho"].full(), complex)
            )
        )
    )
    mandatory = all(rows[r]["opt"]["physical"] and rows[r]["opt"]["impl"] for r in RANKS)
    primary_pass = (
        mandatory
        and ref["basis_err"] < 1e-7
        and r16["jf"] < r16["j0"]
        and primary["maxwidth"] < 1e-6
        and primary["nuclear"] < 5e-6
        and primary["cross"] < 1e-5
    )
    control_ok = r24["opt"]["physical"] and r24["opt"]["impl"] and control < 5e-6
    accepted = bool(primary_pass and control_ok)

    summary = dict(
        purpose="harmonic-only preflight before nonlinear Gate C.1",
        nonlinear_results_used=False,
        ranks=list(RANKS),
        wc=wc,
        sigma0=sigma0,
        C0=c0,
        exact_sampler_max_relerr=sampler_err,
        reference_basis_err=float(ref["basis_err"]),
        rank16=dict(
            objective_initial=float(r16["j0"]),
            objective_best=float(r16["jf"]),
            maxwidth=float(primary["maxwidth"]),
            half_trace_to_exact=float(primary["nuclear"]),
            qp_cross=float(primary["cross"]),
            holdout_Cmaxabs=float(r16["opt"]["cm"][0]),
            holdout_Smaxabs=float(r16["opt"]["sm"][0]),
        ),
        rank24=dict(
            objective_initial=float(r24["j0"]),
            objective_best=float(r24["jf"]),
            maxwidth=float(r24["opt"]["state"]["maxwidth"]),
            half_trace_to_exact=float(r24["opt"]["state"]["nuclear"]),
            qp_cross=float(r24["opt"]["state"]["cross"]),
        ),
        rank24_rank16_half_trace=control,
        accepted_harmonic_reproduction=accepted,
        structure={},
        local_modes={},
        tensor_product_scaling=tensor_product_scaling(),
    )

    Vstore = {}
    for rank in RANKS:
        V, lam, lyap = full_harmonic_covariance(rows[rank], sigma0)
        Vstore[rank] = V
        modes = local_mode_metrics(V, rank)
        structure = structure_metrics(rows[rank])
        structure["counterterm_lambda"] = lam
        structure["full_covariance_lyapunov_residual"] = lyap
        summary["structure"][str(rank)] = structure
        summary["local_modes"][str(rank)] = modes

        print(
            f"C1_PREFLIGHT_STRUCTURE rank={rank} "
            f"HtriLeak={structure['H_tridiagonal_leak']:.12e} "
            f"GammaOffdiag={structure['Gamma_offdiag_fraction']:.12e} "
            f"GammaBeyondNN={structure['Gamma_beyond_nearest_fraction']:.12e} "
            f"GammaCond={structure['Gamma_condition']:.12e} "
            f"maxNbar={max(m['nbar'] for m in modes):.12e} "
            f"maxTailD2={max(m['tails']['2'] for m in modes):.12e} "
            f"maxTailD4={max(m['tails']['4'] for m in modes):.12e}",
            flush=True,
        )

    np.savez_compressed(
        args.npz,
        wc=np.array(wc),
        sigma0=np.array(sigma0),
        C0=np.array(c0),
        H16=np.asarray(r16["opt"]["H"], complex),
        Gamma16=np.asarray(r16["opt"]["Gamma"], complex),
        g16=np.asarray(r16["opt"]["g"], complex),
        V16=Vstore[16],
        H24=np.asarray(r24["opt"]["H"], complex),
        Gamma24=np.asarray(r24["opt"]["Gamma"], complex),
        g24=np.asarray(r24["opt"]["g"], complex),
        V24=Vstore[24],
    )
    Path(args.json).write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(
        f"C1_PREFLIGHT_ACCEPTANCE mandatory={int(mandatory)} "
        f"primary={int(primary_pass)} control={int(control_ok)} "
        f"rank16_rank24_half_trace={control:.12e} accepted={int(accepted)}",
        flush=True,
    )
    print(f"C1_PREFLIGHT_NPZ={args.npz}", flush=True)
    print(f"C1_PREFLIGHT_JSON={args.json}", flush=True)
    if not accepted:
        raise RuntimeError("deterministic regeneration did not reproduce accepted harmonic gate")
    print("VARIABLE_POLE_C1_HARMONIC_PREFLIGHT_PASS", flush=True)


if __name__ == "__main__":
    main()
