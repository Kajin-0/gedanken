#!/usr/bin/env python3
"""Export accepted rank-16 harmonic inputs in solver-neutral text form.

This deterministically regenerates the already accepted physical variable-pole
bath, independently regenerates the exact-FDT reference used by the harmonic
gate, and writes plain CSV/JSON files for the Julia MPDO implementation.  It does
not perform finite-bosonic propagation and does not evaluate a nonlinear state.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

import variable_pole_c1_harmonic_preflight as pre


def save_complex(path: Path, a: np.ndarray):
    a = np.asarray(a, complex)
    flat = np.column_stack([a.real.reshape(-1), a.imag.reshape(-1)])
    np.savetxt(path, flat, delimiter=",", header="real,imag", comments="")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", default="variable_pole_c1_harmonic_input")
    args = ap.parse_args()
    out = Path(args.outdir)
    out.mkdir(parents=True, exist_ok=True)

    rows, wc, sigma0, ref, c0, sampler_err = pre.regenerate()
    row = rows[16]
    V, lam, lyap = pre.full_harmonic_covariance(row, sigma0)

    H = np.asarray(row["opt"]["H"], complex)
    Gamma = np.asarray(row["opt"]["Gamma"], complex)
    g = np.asarray(row["opt"]["g"], complex)
    rho_ref = np.asarray(ref["rho"].full(), complex)

    save_complex(out / "H16.csv", H)
    save_complex(out / "Gamma16.csv", Gamma)
    save_complex(out / "g16.csv", g)
    save_complex(out / "rho_fdt16.csv", rho_ref)
    np.savetxt(out / "V16.csv", np.asarray(V, float), delimiter=",")

    meta = dict(
        nonlinear_results_used=False,
        rank=16,
        H_shape=list(H.shape),
        Gamma_shape=list(Gamma.shape),
        g_shape=list(g.shape),
        rho_fdt_shape=list(rho_ref.shape),
        wc=float(wc),
        sigma0=float(sigma0),
        c0=float(c0),
        counterterm_lambda=float(lam),
        exact_sampler_max_relerr=float(sampler_err),
        full_covariance_lyapunov_residual=float(lyap),
        fdt_target_x=float(ref["target_x"]),
        fdt_target_u=float(ref["target_u"]),
        fdt_nbar=float(ref["nbar"]),
        fdt_squeeze_r=float(ref["r"]),
        fdt_basis_err=float(ref["basis_err"]),
        optimizer_initial=float(row["j0"]),
        optimizer_best=float(row["jf"]),
        accepted_maxwidth=float(row["opt"]["state"]["maxwidth"]),
        accepted_half_trace=float(row["opt"]["state"]["nuclear"]),
        accepted_qp=float(row["opt"]["state"]["cross"]),
    )
    (out / "meta.json").write_text(json.dumps(meta, indent=2, sort_keys=True) + "\n")

    print(
        "C1_HARMONIC_SOLVER_EXPORT "
        f"rank=16 wc={wc:.12e} sigma0={sigma0:.12e} lambda={lam:.12e} "
        f"basis_err={ref['basis_err']:.12e} sampler={sampler_err:.12e} "
        f"accepted_width={row['opt']['state']['maxwidth']:.12e} "
        f"accepted_half={row['opt']['state']['nuclear']:.12e}",
        flush=True,
    )
    if ref["basis_err"] >= 1e-7:
        raise RuntimeError("independent FDT finite-basis reference regressed")
    if sampler_err >= 2e-6:
        raise RuntimeError("exact BCF sampler regressed")
    if row["opt"]["state"]["maxwidth"] >= 1e-6:
        raise RuntimeError("accepted rank16 harmonic reproduction regressed")
    print("VARIABLE_POLE_C1_HARMONIC_SOLVER_EXPORT_PASS", flush=True)


if __name__ == "__main__":
    main()
