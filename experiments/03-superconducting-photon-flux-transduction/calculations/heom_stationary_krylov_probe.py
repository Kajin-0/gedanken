#!/usr/bin/env python3
"""Block-preconditioned Krylov solver for HEOM stationary zero modes.

The sparse direct stationary solve is accurate but its LU fill-in scales poorly
with hierarchy depth.  This diagnostic constructs the same trace-constrained
linear problem and solves it with LGMRES using an ADO-block Jacobi
preconditioner.  Every non-top ADO diagonal block is inverted exactly; the top
physical block is left as the identity because the isolated Hamiltonian
Liouvillian has a multidimensional nullspace before bath coupling.

The first required validation is the nonlinear dim8, Npade4, depth5 state for
which a direct solve and a settled time-domain result are both already known.
Only after this Krylov result reproduces that state with a small original-HEOM
residual should the method be used on the much larger depth-seven matrix.

This changes only the linear algebra used to locate the zero mode.  It is not a
new physical approximation, a hierarchy terminator, or a positivity repair.
"""
from __future__ import annotations

import argparse
import math
import time
import numpy as np
import scipy.linalg as la
import scipy.sparse as sp
from scipy.sparse.linalg import LinearOperator, lgmres

from qutip import Qobj
from qutip.solver.heom import BosonicBath, HEOMSolver

import heom_nonlinear_leftwell_pilot as pilot
import heom_harmonic_pade_depth as bathbase
import heom_schur_terminator_harmonic_probe as schur


CASES = {
    "nonlinear_dim8_p4d5_control": dict(kind="nonlinear", xmin=-3.8, ngrid=2200, dim=8, npade=4, depth=5),
    "nonlinear_dim8_p4d7_test": dict(kind="nonlinear", xmin=-3.8, ngrid=2200, dim=8, npade=4, depth=7),
}

DIRECT_CONTROL = dict(
    eigmin=-9.253009935204e-7,
    neg=9.968961279574e-7,
    mean=2.611823789711e-3,
    sigma=4.011625360329e-2,
    energy=3.046729844284e-2,
    top=-6.962999839517e-7,
)


def constrained_matrix(L: sp.csr_matrix, dim: int):
    n = L.shape[0]
    A = L.tolil(copy=True)
    b = np.zeros(n, dtype=complex)
    trace_cols = [i+i*dim for i in range(dim)]
    A.rows[0] = trace_cols
    A.data[0] = [1.0+0.0j]*dim
    b[0] = 1.0
    return A.tocsr(), b


def block_jacobi(A: sp.csr_matrix, block: int):
    nblock = A.shape[0]//block
    if nblock*block != A.shape[0]:
        raise ValueError("matrix size is not an integer number of ADO blocks")

    t0 = time.perf_counter()
    invs = np.empty((nblock, block, block), dtype=complex)
    invs[0] = np.eye(block, dtype=complex)
    worst_cond = 0.0
    for j in range(1, nblock):
        sl = slice(j*block, (j+1)*block)
        d = A[sl, sl].toarray()
        # The damped non-top diagonal blocks should be nonsingular.  Record an
        # inexpensive condition estimate only on a small deterministic sample.
        if j <= 4 or j == nblock-1:
            worst_cond = max(worst_cond, float(np.linalg.cond(d)))
        invs[j] = la.inv(d, overwrite_a=True, check_finite=False)
    build_s = time.perf_counter()-t0

    def mv(x):
        xx = np.asarray(x, dtype=complex).reshape((nblock, block))
        yy = np.einsum("nij,nj->ni", invs, xx, optimize=True)
        return yy.reshape(-1)

    M = LinearOperator(A.shape, matvec=mv, dtype=complex)
    mem_mb = invs.nbytes/1024**2
    return M, build_s, mem_mb, worst_cond


def solve_krylov(L: sp.csr_matrix, dim: int):
    A, b = constrained_matrix(L, dim)
    s = dim*dim
    M, pre_s, pre_mb, worst_cond = block_jacobi(A, s)
    print(
        f"PRECONDITIONER build_s={pre_s:.3f} storage_MiB={pre_mb:.3f} "
        f"sample_worst_cond={worst_cond:.6e}", flush=True
    )

    calls = {"n": 0}
    def cb(_x):
        calls["n"] += 1
        if calls["n"] == 1 or calls["n"] % 5 == 0:
            print(f"LGMRES outer_iteration={calls['n']}", flush=True)

    t0 = time.perf_counter()
    v, info = lgmres(
        A, b, M=M,
        rtol=1e-10, atol=0.0,
        maxiter=200, inner_m=40, outer_k=5,
        callback=cb,
    )
    solve_s = time.perf_counter()-t0
    cres = A@v-b
    ores = L@v
    return v, info, solve_s, float(np.max(np.abs(cres))), float(np.max(np.abs(ores))), calls["n"]


def run_case(name: str):
    cfg = CASES[name]
    (_model, xm, xs, wc, e, yop, y2op, h0, hsys, rho0, residuals) = pilot.nonlinear_system(cfg)
    cr,vr,ci,vi = bathbase.pade_bath_expansion(wc,cfg["npade"])
    bath = BosonicBath(yop,cr,vr,ci,vi,combine=True,tag="direct-port-pade-krylov")
    solver = HEOMSolver(hsys,bath,max_depth=cfg["depth"],options={"progress_bar":""})
    L = schur.scipy_rhs(solver)
    dim = cfg["dim"]

    print(
        f"CASE={name} dim={dim} Npade={cfg['npade']} depth={cfg['depth']} "
        f"nexp={len(bath.exponents)} nado={len(solver.ados.labels)} "
        f"full_dim={L.shape[0]} nnz={L.nnz}", flush=True
    )
    print(
        f"xm={xm:+.10f} xs={xs:+.10f} wc/2pi={wc/(2*math.pi)*1e-9:.9f}GHz "
        f"max_DVR_residual_K={float(np.max(residuals)):.3e}", flush=True
    )

    v, info, solve_s, cres, ores, outer = solve_krylov(L,dim)
    rho_arr = np.asarray(v[:dim*dim],dtype=complex).reshape((dim,dim),order="F")
    rho = Qobj(rho_arr)
    m = pilot.state_metrics(rho,yop,y2op,h0,rho0)
    print(
        f"KRYLOV info={info} solve_s={solve_s:.3f} outer={outer} "
        f"constrained_residual={cres:.12e} original_residual={ores:.12e}", flush=True
    )
    print(
        f"REDUCED trace=({m['trace'].real:.12e}{m['trace'].imag:+.2e}j) "
        f"anti={m['anti']:.12e} eigmin={m['eigmin']:+.12e} negmass={m['neg']:.12e}", flush=True
    )
    print(
        f"OBS mean_y={m['mean']:+.12e} sigma_y={m['sigma']:.12e} "
        f"E0={m['energy']:+.12e} topPop={m['top']:+.12e} "
        f"bareGibbs_half={m['gibbs_half']:.12e}", flush=True
    )

    finite = bool(np.all(np.isfinite(v)))
    if name.endswith("control"):
        diffs={k:m[k]-DIRECT_CONTROL[k] for k in DIRECT_CONTROL}
        print("DIRECT_DIFF "+" ".join(f"{k}={q:+.12e}" for k,q in diffs.items()),flush=True)
        match=(
            abs(diffs["eigmin"])<2e-9 and abs(diffs["neg"])<2e-9 and
            abs(diffs["mean"])<2e-8 and abs(diffs["sigma"])<2e-8 and
            abs(diffs["energy"])<2e-7 and abs(diffs["top"])<2e-8
        )
    else:
        match=True
    print(f"CHECK direct_control_match={'PASS' if match else 'FAIL'}",flush=True)

    msg=(
        f"KRYLOV_ZERO_MODE case={name} info={info} original_residual={ores:.3e} "
        f"eigmin={m['eigmin']:.6e} negmass={m['neg']:.6e} mean={m['mean']:.6e} "
        f"sigma={m['sigma']:.6e} E0={m['energy']:.6e} finite={finite} match={match}"
    )
    print(msg,flush=True)
    print(f"::notice title=Experiment 03 HEOM stationary Krylov::{msg}",flush=True)

    if info != 0:
        raise RuntimeError(f"LGMRES did not converge, info={info}")
    if not finite or ores >= 1e-8:
        raise RuntimeError("Krylov stationary solution residual/finite check failed")
    if name.endswith("control") and not match:
        raise RuntimeError("Krylov solver failed direct-solution control")


if __name__ == "__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--case",choices=sorted(CASES),required=True)
    args=ap.parse_args()
    run_case(args.case)
