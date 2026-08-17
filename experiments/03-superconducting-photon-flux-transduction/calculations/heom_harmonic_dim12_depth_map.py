#!/usr/bin/env python3
"""Map spectrum and stationary-state accuracy versus hierarchy depth at dim=12.

The harmonic dim=12, Npade=4, depth=3 hierarchy is an exact-oracle example in
which the finite HEOM generator has right-half-plane modes.  Biorthogonal
projection removes the exponential growth but does not recover the exact FDT
state at that shallow depth.

This script asks whether a deeper dim=12 hierarchy can simultaneously have:

1. an independently accurate trace-normalized stationary zero mode, and
2. residual right-half-plane modes that make ordinary propagation unusable.

Such a point would be the decisive controlled validation target for stable-mode
projection: the exact stationary state is known from quantum FDT, while the
transient generator is numerically unstable.

For each depth this script computes the rightmost finite-generator spectrum and
then solves L v=0 with Tr(rho_top)=1 directly.  The latter is a diagnostic of the
finite hierarchy's stationary mode, not a positivity repair.
"""
from __future__ import annotations

import argparse
import math
import time
import numpy as np
from scipy.sparse.linalg import eigs, ArpackNoConvergence

from qutip.solver.heom import HEOMSolver

import heom_schur_terminator_harmonic_probe as schur
import heom_harmonic_final_state_gate as finalgate
import heom_harmonic_steady_nullspace_probe as steady

DIM = 12
NPADE = 4
CASES = {
    "dim12_p4d4": 4,
    "dim12_p4d5": 5,
}


def run_case(name: str):
    depth = CASES[name]
    wc, tx, tu, xop, uop, H, bath = schur.harmonic_setup(DIM, NPADE)
    solver = HEOMSolver(H, bath, max_depth=depth, options={"progress_bar": ""})
    L = schur.scipy_rhs(solver)
    ref = finalgate.exact_reference(DIM)

    print(
        f"CASE={name} dim={DIM} Npade={NPADE} depth={depth} "
        f"nexp={len(bath.exponents)} nado={len(solver.ados.labels)} "
        f"full_dim={L.shape[0]} nnz={L.nnz} wc/2pi={wc/(2*math.pi)*1e-9:.9f}GHz",
        flush=True,
    )
    print(
        f"REFERENCE basis_err={ref['basis_err']:.12e} "
        f"target_x={ref['target_x']:.12e} target_u={ref['target_u']:.12e}",
        flush=True,
    )

    # Rightmost spectrum: enough modes to establish whether the returned window
    # crosses into the left half-plane and to count resolved unstable modes.
    t0 = time.perf_counter()
    try:
        vals, vecs = eigs(L, k=12, which="LR", tol=2e-9, maxiter=50000, ncv=48)
        spec_conv = True
        spec_note = "NONE"
    except ArpackNoConvergence as exc:
        vals = np.asarray(exc.eigenvalues)
        vecs = np.asarray(exc.eigenvectors)
        spec_conv = False
        spec_note = f"ARPACK_NO_CONVERGENCE returned={len(vals)}"
    spec_s = time.perf_counter()-t0
    if len(vals) == 0:
        raise RuntimeError("rightmost spectrum returned no eigenpairs")
    order = np.argsort(vals.real)[::-1]
    vals, vecs = vals[order], vecs[:, order]
    print(
        f"SPECTRUM converged={spec_conv} note={spec_note} runtime_s={spec_s:.3f} "
        f"returned={len(vals)} min_returned_Re={vals[-1].real:+.9e}", flush=True
    )
    for j, lam in enumerate(vals):
        v = vecs[:, j]
        r = L@v-lam*v
        den = max(float(np.linalg.norm(L@v)), abs(lam)*float(np.linalg.norm(v)), 1e-12)
        relres = float(np.linalg.norm(r))/den
        print(
            f"EIG {j:02d} lambda=({lam.real:+.12e}{lam.imag:+.12e}j) relres={relres:.3e}",
            flush=True,
        )
    npos = int(np.sum(vals.real > 1e-7))
    nzero = int(np.sum(np.abs(vals) < 1e-7))
    spectrum_window_safe = bool(vals[-1].real < -1e-3)
    print(
        f"SPECTRUM_SUMMARY rightmost_Re={vals[0].real:+.12e} "
        f"positive_returned={npos} near_zero={nzero} "
        f"window_safe={spectrum_window_safe}", flush=True
    )

    # Direct trace-constrained stationary solve.
    vss, solve_s, res_abs, res_rel, warn_text = steady.constrained_nullvector(L, DIM)
    m = steady.reduced_metrics(vss, DIM, ref)
    maxfdt = max(abs(m['relx']), abs(m['relu']))
    print(
        f"NULLSPACE solve_s={solve_s:.3f} residual_maxabs={res_abs:.12e} "
        f"residual_scaled={res_rel:.12e} warnings={warn_text or 'NONE'}", flush=True
    )
    print(
        f"STATIONARY trace=({m['trace'].real:.12e}{m['trace'].imag:+.2e}j) "
        f"anti={m['anti']:.12e} eigmin={m['eigmin']:+.12e} "
        f"negmass={m['neg']:.12e}", flush=True
    )
    print(
        f"ORACLE relx={m['relx']:+.12e} relu={m['relu']:+.12e} "
        f"maxFDT={maxfdt:.12e} half_nuclear={m['half_nuclear']:.12e} "
        f"frobenius={m['frob']:.12e}", flush=True
    )

    oracle = {
        "reference_basis": ref['basis_err'] < 1e-7,
        "fdt": maxfdt < 1e-6,
        "half_nuclear": m['half_nuclear'] < 5e-6,
        "negative_mass": m['neg'] < 5e-8,
        "trace": abs(m['trace']-1.0) < 1e-10,
        "hermiticity": m['anti'] < 1e-10,
        "null_residual": res_abs < 1e-8,
    }
    for k, ok in oracle.items():
        print(f"ORACLE_CHECK {k}={'PASS' if ok else 'FAIL'}", flush=True)

    msg=(
        f"DIM12_DEPTH_MAP case={name} rightmost_Re={vals[0].real:.6e} "
        f"positive={npos} window_safe={spectrum_window_safe} "
        f"maxFDT={maxfdt:.6e} half_nuclear={m['half_nuclear']:.6e} "
        f"negmass={m['neg']:.6e} eigmin={m['eigmin']:.6e} "
        f"oracle_pass={all(oracle.values())}"
    )
    print(msg, flush=True)
    print(f"::notice title=Experiment 03 harmonic dim12 depth map::{msg}", flush=True)

    if not spectrum_window_safe:
        raise RuntimeError("rightmost spectral window did not extend into left half-plane")
    if res_abs >= 1e-8:
        raise RuntimeError("stationary direct solve residual too large")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--case", choices=sorted(CASES), required=True)
    args = ap.parse_args()
    run_case(args.case)
