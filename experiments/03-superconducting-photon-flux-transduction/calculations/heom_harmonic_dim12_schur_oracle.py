#!/usr/bin/env python3
"""Exact-oracle test of the diagonal NZ/Schur terminator on unstable dim12 HEOM.

The harmonic dim=12, Npade=4, raw depth=3 generator has resolved right-half-plane
modes and an independently known exact FDT/Gaussian reduced equilibrium state.
This script compares the native raw depth-3 generator with the first-omitted-tier
Schur/Nakajima-Zwanzig terminated generator already implemented and audited in
`heom_schur_terminator_harmonic_probe.py`.

Questions:
1. Does the terminator remove the spurious right-half-plane spectrum?
2. Does its trace-normalized stationary reduced state improve against the exact
   FDT/Gaussian oracle?

No projection, density-matrix repair, bath change, or parameter refit is used.
"""
from __future__ import annotations

import time
import numpy as np
from scipy.sparse.linalg import eigs, ArpackNoConvergence

import heom_schur_terminator_harmonic_probe as schur
import heom_harmonic_steady_nullspace_probe as steady
import heom_harmonic_final_state_gate as finalgate

DIM=12
NPADE=4
DEPTH=3


def spectrum(label,L):
    t0=time.perf_counter()
    try:
        vals,vecs=eigs(L,k=12,which='LR',tol=2e-9,maxiter=50000,ncv=48)
        conv=True; note='NONE'
    except ArpackNoConvergence as exc:
        vals=np.asarray(exc.eigenvalues); vecs=np.asarray(exc.eigenvectors)
        conv=False; note=f'ARPACK_NO_CONVERGENCE returned={len(vals)}'
    runtime=time.perf_counter()-t0
    if len(vals)==0:
        raise RuntimeError(f'{label}: no eigenpairs')
    order=np.argsort(vals.real)[::-1]; vals=vals[order]; vecs=vecs[:,order]
    print(f'SPECTRUM mode={label} converged={conv} note={note} runtime_s={runtime:.3f} minReturnedRe={vals[-1].real:+.9e}',flush=True)
    for j,lam in enumerate(vals):
        v=vecs[:,j]; r=L@v-lam*v
        den=max(float(np.linalg.norm(L@v)),abs(lam)*float(np.linalg.norm(v)),1e-12)
        print(f'EIG mode={label} j={j:02d} lambda=({lam.real:+.12e}{lam.imag:+.12e}j) relres={float(np.linalg.norm(r))/den:.3e}',flush=True)
    npos=int(np.sum(vals.real>1e-7)); nzero=int(np.sum(np.abs(vals)<1e-7))
    safe=bool(vals[-1].real < -1e-3)
    print(f'SPECTRUM_SUMMARY mode={label} rightmost_Re={vals[0].real:+.12e} positive={npos} nearzero={nzero} window_safe={safe}',flush=True)
    return vals,npos,safe


def stationary(label,L,ref):
    v,solve_s,res_abs,res_rel,warn=steady.constrained_nullvector(L,DIM)
    m=steady.reduced_metrics(v,DIM,ref)
    maxfdt=max(abs(m['relx']),abs(m['relu']))
    print(f'NULLSPACE mode={label} solve_s={solve_s:.3f} residual={res_abs:.12e} scaled={res_rel:.12e} warnings={warn or "NONE"}',flush=True)
    print(f'STATE mode={label} trace=({m["trace"].real:.12e}{m["trace"].imag:+.2e}j) anti={m["anti"]:.3e} eigmin={m["eigmin"]:+.12e} negmass={m["neg"]:.12e}',flush=True)
    print(f'ORACLE mode={label} relx={m["relx"]:+.12e} relu={m["relu"]:+.12e} maxFDT={maxfdt:.12e} half_nuclear={m["half_nuclear"]:.12e} frob={m["frob"]:.12e}',flush=True)
    checks={
        'fdt':maxfdt<1e-6,
        'half_nuclear':m['half_nuclear']<5e-6,
        'negative_mass':m['neg']<5e-8,
        'trace':abs(m['trace']-1)<1e-10,
        'hermiticity':m['anti']<1e-10,
        'residual':res_abs<1e-8,
    }
    for k,vv in checks.items(): print(f'ORACLE_CHECK mode={label} {k}={"PASS" if vv else "FAIL"}',flush=True)
    return m,maxfdt,all(checks.values())


def main():
    wc,tx,tu,xop,uop,H,bath=schur.harmonic_setup(DIM,NPADE)
    raw,Lraw,Leff,match,nomit,corr_nnz,build_s=schur.build_schur_rhs(H,bath,DIM,DEPTH)
    ref=finalgate.exact_reference(DIM)
    print(f'CASE dim={DIM} Npade={NPADE} depth={DEPTH} nexp={len(bath.exponents)} retained_ados={len(raw.ados.labels)} omitted_interface={nomit} raw_match={match:.3e} corr_nnz={corr_nnz} build_s={build_s:.3f}',flush=True)
    print(f'REFERENCE basis_err={ref["basis_err"]:.12e} target_x={tx:.12e} target_u={tu:.12e}',flush=True)
    if match>1e-12: raise RuntimeError('retained-block audit failed')

    _,rpos,rsafe=spectrum('RAW',Lraw)
    rm,rfdt,rpass=stationary('RAW',Lraw,ref)
    _,spos,ssafe=spectrum('SCHUR',Leff)
    sm,sfdt,spass=stationary('SCHUR',Leff,ref)

    msg=(f'DIM12_SCHUR raw_positive={rpos} schur_positive={spos} raw_maxFDT={rfdt:.6e} '
         f'schur_maxFDT={sfdt:.6e} raw_half={rm["half_nuclear"]:.6e} schur_half={sm["half_nuclear"]:.6e} '
         f'raw_neg={rm["neg"]:.6e} schur_neg={sm["neg"]:.6e} schur_oracle_pass={spass}')
    print(msg,flush=True)
    print(f'::notice title=Experiment 03 dim12 Schur oracle::{msg}',flush=True)
    if not rsafe or not ssafe: raise RuntimeError('spectral window failed to reach left half-plane')

if __name__=='__main__': main()
