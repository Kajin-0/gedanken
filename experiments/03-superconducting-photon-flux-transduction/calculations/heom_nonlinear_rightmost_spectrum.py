#!/usr/bin/env python3
"""Rightmost-spectrum diagnostic for nonlinear restricted-well HEOM.

This does not alter the HEOM generator.  It directly tests the hypothesis that
the observed late-time blow-ups are caused by spectral pollution of the finite
hard-cutoff hierarchy.

Two pre-existing time-domain cases are compared under identical bath physics:

* dim=8, Npade=4, depth=5: settled through tau=160;
* dim=10, Npade=4, depth=5: develops exponential nonphysical growth, with an
  empirical amplitude exponent of order +0.3 per dimensionless tau.

For each finite HEOM generator we request the eigenvalues with largest real part.
A trace-preserving physical stationary mode should lie at lambda=0.  A genuine
right-half-plane eigenvalue matching the observed time-domain exponent directly
identifies a finite-generator instability rather than an adaptive-step artifact.

The calculation is diagnostic only.  No unstable-mode projection or state repair
is performed here.
"""
from __future__ import annotations

import argparse
import math
import time
import numpy as np
from scipy.sparse.linalg import eigs, ArpackNoConvergence

from qutip.solver.heom import BosonicBath, HEOMSolver

import heom_nonlinear_leftwell_pilot as pilot
import heom_harmonic_pade_depth as bathbase
import heom_schur_terminator_harmonic_probe as schur

CASES = {
    "dim8_p4d5": dict(xmin=-3.8, ngrid=2200, dim=8, npade=4, depth=5),
    "dim10_p4d5": dict(xmin=-3.8, ngrid=2200, dim=10, npade=4, depth=5),
}


def run_case(name: str):
    cfg = CASES[name]
    (_model, xm, xs, wc, e, yop, y2op, h0, hsys, rho0, residuals) = pilot.nonlinear_system(cfg)
    cr,vr,ci,vi = bathbase.pade_bath_expansion(wc,cfg["npade"])
    bath = BosonicBath(yop,cr,vr,ci,vi,combine=True,tag="direct-port-pade-spectrum")
    solver = HEOMSolver(hsys,bath,max_depth=cfg["depth"],options={"progress_bar":""})
    L = schur.scipy_rhs(solver)
    dim = cfg["dim"]
    block = dim*dim

    print(
        f"CASE={name} dim={dim} Npade={cfg['npade']} depth={cfg['depth']} "
        f"nexp={len(bath.exponents)} nado={len(solver.ados.labels)} "
        f"full_dim={L.shape[0]} nnz={L.nnz}", flush=True
    )
    print(
        f"xm={xm:+.10f} xs={xs:+.10f} wc/2pi={wc/(2*math.pi)*1e-9:.9f}GHz "
        f"max_DVR_residual_K={float(np.max(residuals)):.3e}", flush=True
    )

    k = 8
    t0 = time.perf_counter()
    try:
        vals, vecs = eigs(L, k=k, which="LR", tol=2e-8, maxiter=30000, ncv=36)
        converged = True
        note = "NONE"
    except ArpackNoConvergence as exc:
        vals = np.asarray(exc.eigenvalues)
        vecs = np.asarray(exc.eigenvectors)
        converged = False
        note = f"ARPACK_NO_CONVERGENCE returned={len(vals)}"
    runtime = time.perf_counter()-t0

    if len(vals) == 0:
        raise RuntimeError("ARPACK returned no eigenpairs")
    order = np.argsort(vals.real)[::-1]
    vals = vals[order]
    vecs = vecs[:,order]

    print(f"ARPACK converged={converged} note={note} runtime_s={runtime:.3f}", flush=True)
    for j, lam in enumerate(vals):
        v = vecs[:,j]
        nv = float(np.linalg.norm(v))
        phys = float(np.linalg.norm(v[:block]))/max(nv,1e-300)
        r = L@v-lam*v
        relres = float(np.linalg.norm(r))/max(float(np.linalg.norm(L@v)), abs(lam)*nv, 1e-300)
        # Trace amplitude of the physical ADO is useful for distinguishing the
        # stationary density mode from trace-zero unstable modes.
        rho = v[:block].reshape((dim,dim),order="F")
        tr = complex(np.trace(rho))
        print(
            f"EIG {j:02d} lambda=({lam.real:+.12e}{lam.imag:+.12e}j) "
            f"phys_frac={phys:.6e} top_trace=({tr.real:+.6e}{tr.imag:+.6e}j) "
            f"relres={relres:.3e}", flush=True
        )

    right = vals[0]
    npos = int(np.sum(vals.real > 1e-7))
    nnear0 = int(np.sum(np.abs(vals) < 1e-7))
    msg=(
        f"RIGHTMOST case={name} Re={right.real:.9e} Im={right.imag:.9e} "
        f"positive_among_returned={npos} near_zero={nnear0} returned={len(vals)} "
        f"arpack_converged={converged} runtime_s={runtime:.3f}"
    )
    print(msg,flush=True)
    print(f"::notice title=Experiment 03 nonlinear HEOM rightmost spectrum::{msg}",flush=True)


if __name__ == "__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--case",choices=sorted(CASES),required=True)
    args=ap.parse_args()
    run_case(args.case)
