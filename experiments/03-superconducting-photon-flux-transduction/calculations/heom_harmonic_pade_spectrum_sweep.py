#!/usr/bin/env python3
"""Find a controlled unstable harmonic HEOM representation for projection tests.

The nonlinear finite HEOM now has directly demonstrated right-half-plane modes.
Before any stable-mode projection is considered for nonlinear Gate C/D, the
projection method must be tested on a problem with an independent exact oracle.
The harmonic direct-port model supplies that oracle through exact quantum FDT.

This script varies only oscillator Hilbert dimension at fixed Padé bath and
hierarchy depth and computes the rightmost finite-generator eigenvalues.  If a
high-basis harmonic case develops positive-real modes while the low-basis control
does not, that case becomes a controlled projection-validation target.

No projection is performed here.
"""
from __future__ import annotations

import argparse
import math
import time
import numpy as np
from scipy.sparse.linalg import eigs, ArpackNoConvergence
from qutip.solver.heom import HEOMSolver

import heom_schur_terminator_harmonic_probe as schur

CASES = {
    "dim8_p4d3": dict(dim=8,npade=4,depth=3),
    "dim12_p4d3": dict(dim=12,npade=4,depth=3),
    "dim16_p4d3": dict(dim=16,npade=4,depth=3),
}


def run_case(name: str):
    cfg=CASES[name]
    wc,tx,tu,xop,uop,H,bath=schur.harmonic_setup(cfg['dim'],cfg['npade'])
    solver=HEOMSolver(H,bath,max_depth=cfg['depth'],options={'progress_bar':''})
    L=schur.scipy_rhs(solver)
    dim=cfg['dim']; block=dim*dim
    print(
        f"CASE={name} dim={dim} Npade={cfg['npade']} depth={cfg['depth']} "
        f"nexp={len(bath.exponents)} nado={len(solver.ados.labels)} "
        f"full_dim={L.shape[0]} nnz={L.nnz} wc/2pi={wc/(2*math.pi)*1e-9:.9f}GHz",
        flush=True,
    )
    print(f"TARGET sigma_x={tx:.12e} sigma_u={tu:.12e}",flush=True)

    t0=time.perf_counter()
    try:
        vals,vecs=eigs(L,k=8,which='LR',tol=2e-8,maxiter=30000,ncv=36)
        conv=True; note='NONE'
    except ArpackNoConvergence as exc:
        vals=np.asarray(exc.eigenvalues); vecs=np.asarray(exc.eigenvectors)
        conv=False; note=f"ARPACK_NO_CONVERGENCE returned={len(vals)}"
    runtime=time.perf_counter()-t0
    if len(vals)==0:
        raise RuntimeError('no eigenpairs returned')
    order=np.argsort(vals.real)[::-1]; vals=vals[order]; vecs=vecs[:,order]
    print(f"ARPACK converged={conv} note={note} runtime_s={runtime:.3f}",flush=True)
    for j,lam in enumerate(vals):
        v=vecs[:,j]; nv=float(np.linalg.norm(v))
        phys=float(np.linalg.norm(v[:block]))/max(nv,1e-300)
        r=L@v-lam*v
        denom=max(float(np.linalg.norm(L@v)),abs(lam)*nv,1e-12)
        relres=float(np.linalg.norm(r))/denom
        print(
            f"EIG {j:02d} lambda=({lam.real:+.12e}{lam.imag:+.12e}j) "
            f"phys_frac={phys:.6e} relres={relres:.3e}",flush=True,
        )
    right=vals[0]
    npos=int(np.sum(vals.real>1e-7)); nzero=int(np.sum(np.abs(vals)<1e-7))
    msg=(
        f"HARMONIC_RIGHTMOST case={name} Re={right.real:.9e} Im={right.imag:.9e} "
        f"positive_among_returned={npos} near_zero={nzero} returned={len(vals)} "
        f"arpack_converged={conv} runtime_s={runtime:.3f}"
    )
    print(msg,flush=True)
    print(f"::notice title=Experiment 03 harmonic HEOM spectrum sweep::{msg}",flush=True)


if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--case',choices=sorted(CASES),required=True)
    args=ap.parse_args(); run_case(args.case)
