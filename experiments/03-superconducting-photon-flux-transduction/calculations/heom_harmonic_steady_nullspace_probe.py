#!/usr/bin/env python3
"""Direct zero-frequency/nullspace probe for harmonic HEOM truncations.

Purpose
-------
The nonlinear raw hierarchy exhibits spurious exponentially growing modes whose
onset is non-monotone in hierarchy depth.  For Gate C.1 cold-state preparation,
we need to distinguish two questions:

1. Does the finite HEOM generator have unstable dynamical modes?
2. Is its trace-normalized zero mode (stationary reduced state) itself converged?

This probe addresses only (2) in the harmonic problem, where an independent exact
Gaussian/FDT reduced state is available.  It solves L v = 0 with Tr(rho_0)=1 by
replacing one redundant Liouvillian row with the trace constraint.  No time
propagation, eigenvalue clipping, state projection, or positivity repair is used.

The calculation is equivalent to asking for the z=0 stationary mode of the finite
HEOM and is therefore a diagnostic for a zero-frequency Schur/steady-state route.
It does NOT validate finite-time nonlinear dynamics.
"""
from __future__ import annotations

import argparse
import math
import time
import warnings

import numpy as np
import scipy.sparse as sp
from scipy.linalg import svdvals
from scipy.sparse.linalg import spsolve

import heom_schur_terminator_harmonic_probe as schur
import heom_harmonic_final_state_gate as finalgate


CASES = {
    "p4d3": dict(dim=8, npade=4, depth=3),
    "p4d4": dict(dim=8, npade=4, depth=4),
    "p4d5": dict(dim=8, npade=4, depth=5),
}


def constrained_nullvector(L: sp.csr_matrix, dim: int):
    """Solve L v=0 with trace of the physical/top ADO fixed to one."""
    n = L.shape[0]
    A = L.tolil(copy=True)
    b = np.zeros(n, dtype=complex)

    # In QuTiP's column-stacking convention the physical rho is the first dim^2
    # entries and diagonal matrix elements are i + i*dim.
    trace_cols = [i + i*dim for i in range(dim)]
    constraint_row = 0
    A.rows[constraint_row] = trace_cols
    A.data[constraint_row] = [1.0+0.0j] * dim
    b[constraint_row] = 1.0

    A = A.tocsc()
    t0 = time.perf_counter()
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        v = spsolve(A, b)
    runtime = time.perf_counter() - t0
    warn_text = " | ".join(str(w.message) for w in caught)

    residual = L @ v
    res_abs = float(np.max(np.abs(residual)))
    scale = max(float(np.max(np.abs(L.data))) * float(np.max(np.abs(v))), 1.0)
    res_rel = res_abs / scale
    return v, runtime, res_abs, res_rel, warn_text


def reduced_metrics(v, dim, ref):
    rho = np.asarray(v[:dim*dim], dtype=complex).reshape((dim, dim), order="F")
    tr = complex(np.trace(rho))
    anti = np.linalg.norm(rho-rho.conj().T, ord="fro") / max(
        np.linalg.norm(rho, ord="fro"), 1e-300
    )
    rh = 0.5*(rho+rho.conj().T)
    ev = np.linalg.eigvalsh(rh)
    eigmin = float(ev.min())
    neg = float(np.sum(np.maximum(-ev, 0.0)))

    xo = np.asarray(ref["xop"].full(), dtype=complex)
    uo = np.asarray(ref["uop"].full(), dtype=complex)
    mx = complex(np.trace(xo@rho))
    mu = complex(np.trace(uo@rho))
    x2 = complex(np.trace((xo@xo)@rho))
    u2 = complex(np.trace((uo@uo)@rho))
    sx = math.sqrt(max(float(np.real(x2-mx*mx)), 0.0))
    su = math.sqrt(max(float(np.real(u2-mu*mu)), 0.0))
    relx = sx/ref["target_x"] - 1.0
    relu = su/ref["target_u"] - 1.0

    exact = np.asarray(ref["rho"].full(), dtype=complex)
    half_nuclear = 0.5*float(np.sum(svdvals(rho-exact)))
    frob = float(np.linalg.norm(rho-exact, ord="fro"))
    return dict(
        rho=rho, trace=tr, anti=anti, eigmin=eigmin, neg=neg,
        sx=sx, su=su, relx=relx, relu=relu,
        half_nuclear=half_nuclear, frob=frob,
    )


def run_case(name: str):
    cfg = CASES[name]
    dim = cfg["dim"]
    wc, tx, tu, xop, uop, H, bath = schur.harmonic_setup(dim, cfg["npade"])
    from qutip.solver.heom import HEOMSolver
    solver = HEOMSolver(H, bath, max_depth=cfg["depth"], options={"progress_bar": ""})
    L = schur.scipy_rhs(solver)
    nado = len(solver.ados.labels)

    print(
        f"CASE={name} dim={dim} Npade={cfg['npade']} depth={cfg['depth']} "
        f"nexp={len(bath.exponents)} nado={nado} full_dim={L.shape[0]} "
        f"nnz={L.nnz} wc/2pi={wc/(2*math.pi)*1e-9:.9f}GHz",
        flush=True,
    )

    ref = finalgate.exact_reference(dim)
    print(
        f"REFERENCE basis_err={ref['basis_err']:.12e} "
        f"sigma_x={ref['target_x']:.12e} sigma_u={ref['target_u']:.12e}",
        flush=True,
    )

    v, runtime, res_abs, res_rel, warn_text = constrained_nullvector(L, dim)
    m = reduced_metrics(v, dim, ref)
    ado_max = float(np.max(np.abs(v[dim*dim:]))) if len(v) > dim*dim else 0.0

    print(
        f"NULLSPACE solve_s={runtime:.3f} residual_maxabs={res_abs:.12e} "
        f"residual_scaled={res_rel:.12e} warnings={warn_text or 'NONE'}",
        flush=True,
    )
    print(
        f"REDUCED trace=({m['trace'].real:.12e}{m['trace'].imag:+.2e}j) "
        f"anti={m['anti']:.12e} eigmin={m['eigmin']:+.12e} "
        f"negmass={m['neg']:.12e} maxADO={ado_max:.12e}",
        flush=True,
    )
    print(
        f"FDT relx={m['relx']:+.12e} relu={m['relu']:+.12e} "
        f"maxFDT={max(abs(m['relx']),abs(m['relu'])):.12e}",
        flush=True,
    )
    print(
        f"FULLSTATE half_nuclear={m['half_nuclear']:.12e} "
        f"frobenius={m['frob']:.12e}", flush=True
    )

    # Same numerical standards used by the already-passed harmonic Gate-B
    # full-state comparator.  A single case passing here is diagnostic only;
    # adjacent-depth convergence is still required before methodological use.
    checks = {
        "reference_basis": ref["basis_err"] < 1e-7,
        "fdt": max(abs(m["relx"]), abs(m["relu"])) < 1e-6,
        "half_nuclear": m["half_nuclear"] < 5e-6,
        "negative_mass": m["neg"] < 5e-8,
        "trace": abs(m["trace"]-1.0) < 1e-10,
        "hermiticity": m["anti"] < 1e-10,
        "null_residual": res_abs < 1e-8,
    }
    for key,val in checks.items():
        print(f"CHECK {key}={'PASS' if val else 'FAIL'}")
    msg=(
        f"STEADY_NULLSPACE case={name} maxFDT={max(abs(m['relx']),abs(m['relu'])):.6e} "
        f"half_nuclear={m['half_nuclear']:.6e} negmass={m['neg']:.6e} "
        f"eigmin={m['eigmin']:.6e} residual={res_abs:.3e} all_numeric={all(checks.values())}"
    )
    print(msg, flush=True)
    print(f"::notice title=Experiment 03 harmonic HEOM steady nullspace::{msg}", flush=True)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--case", choices=sorted(CASES), required=True)
    args = ap.parse_args()
    run_case(args.case)
