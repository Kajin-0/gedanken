#!/usr/bin/env python3
"""Free-pole HEOM harmonic exact-oracle probe for Experiment 03.

Motivation
----------
The conventional hard-cutoff HEOM representation has now exhibited explicit
right-half-plane spectral pollution.  The dominant unstable eigenmodes are
localized overwhelmingly on the terminal hierarchy tier.  Increasing the raw
hierarchy depth is non-monotone and is no longer an authorized convergence
strategy for Gate C.1.

Krug & Stockburger's stability analysis writes the free-pole HEOM (FP-HEOM)
with independent forward/backward indices for every complex exponential

    C(t) = sum_k d_k exp(-z_k t),  Re z_k > 0,

rather than folding real/imaginary pieces into the conventional hierarchy.
For a single system coupling operator q their Eq. (2) is

  d rho_mn/dt = -i[H,rho_mn] - sum_k(m_k z_k+n_k z_k*) rho_mn
      - i sum_k sqrt((m_k+1)d_k) [q,rho_{m+k,n}]
      - i sum_k sqrt((n_k+1)d_k*) [q,rho_{m,n+k}]
      - i sum_k sqrt(m_k d_k) q rho_{m-k,n}
      + i sum_k sqrt(n_k d_k*) rho_{m,n-k} q .

This script implements that equation directly as a sparse Liouville-space
matrix.  It changes only the finite hierarchy representation.  The physical
Hamiltonian, counterterm, direct-port correlation function, Padé order,
temperature and exact FDT reference are identical to the accepted harmonic
Gate-B problem.

The probe is deliberately falsification-first.  Each case reports:
  * the rightmost generator spectrum;
  * the trace-normalized stationary zero mode;
  * exact FDT width error;
  * full-state half nuclear-norm discrepancy;
  * negative eigenvalue mass.

No clipping, spectral projection or positivity repair is used.  A favorable
single tier is not an acceptance result; adjacent-depth convergence would still
be required before nonlinear use.
"""
from __future__ import annotations

import argparse
import math
import time
import numpy as np
import scipy.sparse as sp
from scipy.sparse import eye, kron
from scipy.sparse.linalg import eigs, ArpackNoConvergence

from quantum_initial_capture import PHI_BAR
from direct_port_bath_correlation import bath_poles, bath_coeff
from direct_port_bath_pade import pade_terms
import heom_harmonic_pade_depth as base
import heom_harmonic_final_state_gate as finalgate
import heom_harmonic_steady_nullspace_probe as steady

from qutip import destroy, qeye


CASES = {
    # Twelve FP hierarchy coordinates = forward/backward copies of the same
    # six-term direct-port Padé correlation used by conventional p4 HEOM.
    "fp_dim8_p4d1": dict(dim=8, npade=4, depth=1),
    "fp_dim8_p4d2": dict(dim=8, npade=4, depth=2),
    "fp_dim8_p4d3": dict(dim=8, npade=4, depth=3),
    # Exact-oracle high-basis discriminator corresponding to the conventional
    # dim12,p4,d3 instability map.  Start shallow; do not brute-force d4+ unless
    # the lower FP sequence is both stable and state-convergent.
    "fp_dim12_p4d2": dict(dim=12, npade=4, depth=2),
    "fp_dim12_p4d3": dict(dim=12, npade=4, depth=3),
}


def compositions(total: int, slots: int, prefix=()):
    if slots == 1:
        yield prefix + (total,)
        return
    for n in range(total + 1):
        yield from compositions(total - n, slots - 1, prefix + (n,))


def hierarchy_labels(ncoord: int, depth: int):
    labels = []
    for tier in range(depth + 1):
        labels.extend(compositions(tier, ncoord))
    return labels


def bath_modes(wc: float, npade: int):
    """Return dimensionless FP coefficients d_k and rates z_k.

    Time is tau=wc*t and the coupling coordinate is the same dimensionless
    phase coordinate used in the conventional harmonic Gate-B hierarchy.
    Therefore d_k = C_k (Phi_bar/hbar)^2 / wc^2 and z_k=gamma_k/wc.
    """
    cscale = (PHI_BAR/base.HBAR)**2/(wc*wc)
    d = []
    z = []
    for p in bath_poles():
        d.append(complex(bath_coeff(p)*cscale))
        z.append(complex(1j*p/wc))
    for c, nu in pade_terms(npade):
        d.append(complex(c*cscale))
        z.append(complex(nu/wc))
    return np.asarray(d, complex), np.asarray(z, complex)


def harmonic_setup(dim: int, npade: int):
    # Reproduce the accepted harmonic Gate-B system exactly.
    ref = finalgate.exact_reference(dim)
    # Recover wc and sigma0 from the exact reference.  sigma0 is already in the
    # same convention used by the conventional harmonic HEOM implementation.
    # base.C, HBAR and PHI_BAR are fixed physical constants.
    sigma0 = ref["sigma0"]
    wc = base.HBAR/(2*base.C*PHI_BAR**2*sigma0*sigma0)
    a = destroy(dim)
    n = a.dag()*a
    xop = sigma0*(a+a.dag())
    uop = 1j*sigma0*(a.dag()-a)
    H = n + 0.5*qeye(dim)
    ct_phys = PHI_BAR**2/base.HBAR * base.G*base.WD/(2*math.sqrt(2))
    H = H + (ct_phys/wc)*(xop*xop)
    d, z = bath_modes(wc, npade)
    return wc, xop, uop, H, d, z, ref


def sparse_superoperators(H, q):
    hm = sp.csr_matrix(np.asarray(H.full(), complex))
    qm = sp.csr_matrix(np.asarray(q.full(), complex))
    dim = H.shape[0]
    I = eye(dim, dtype=complex, format="csr")
    # Column-stacking convention: vec(A rho B)=(B^T kron A)vec(rho).
    Lsys = -1j*(kron(I, hm, format="csr") - kron(hm.T, I, format="csr"))
    Cq = kron(I, qm, format="csr") - kron(qm.T, I, format="csr")
    Lq = kron(I, qm, format="csr")
    Rq = kron(qm.T, I, format="csr")
    return Lsys.tocsr(), Cq.tocsr(), Lq.tocsr(), Rq.tocsr()


def adjacency(rows, cols, vals, nado):
    if not vals:
        return sp.csr_matrix((nado, nado), dtype=complex)
    return sp.coo_matrix((np.asarray(vals, complex),
                          (np.asarray(rows, int), np.asarray(cols, int))),
                         shape=(nado, nado)).tocsr()


def fp_generator(H, q, d, z, depth: int):
    K = len(d)
    ncoord = 2*K
    labels = hierarchy_labels(ncoord, depth)
    lookup = {lab:i for i, lab in enumerate(labels)}
    nado = len(labels)
    dim = H.shape[0]
    s = dim*dim
    Lsys, Cq, Lq, Rq = sparse_superoperators(H, q)

    damp = np.empty(nado, complex)
    for i, lab in enumerate(labels):
        m = lab[:K]
        n = lab[K:]
        damp[i] = sum(m[k]*z[k] + n[k]*np.conj(z[k]) for k in range(K))

    L = kron(eye(nado, dtype=complex, format="csr"), Lsys, format="csr")
    L += kron(sp.diags(-damp, format="csr"), eye(s, dtype=complex, format="csr"), format="csr")

    rr=[]; rc=[]; rv=[]
    mlr=[]; mlc=[]; mlv=[]
    nlr=[]; nlc=[]; nlv=[]
    for i, lab in enumerate(labels):
        tier = sum(lab)
        for k in range(K):
            mk = lab[k]
            nk = lab[K+k]
            if tier < depth:
                up = list(lab); up[k] += 1; j = lookup[tuple(up)]
                rr.append(i); rc.append(j); rv.append(np.sqrt((mk+1)*d[k]))
                up = list(lab); up[K+k] += 1; j = lookup[tuple(up)]
                rr.append(i); rc.append(j); rv.append(np.sqrt((nk+1)*np.conj(d[k])))
            if mk > 0:
                lo = list(lab); lo[k] -= 1; j = lookup[tuple(lo)]
                mlr.append(i); mlc.append(j); mlv.append(np.sqrt(mk*d[k]))
            if nk > 0:
                lo = list(lab); lo[K+k] -= 1; j = lookup[tuple(lo)]
                nlr.append(i); nlc.append(j); nlv.append(np.sqrt(nk*np.conj(d[k])))

    Araise = adjacency(rr, rc, rv, nado)
    Amlow = adjacency(mlr, mlc, mlv, nado)
    Anlow = adjacency(nlr, nlc, nlv, nado)
    L += kron(Araise, -1j*Cq, format="csr")
    L += kron(Amlow, -1j*Lq, format="csr")
    L += kron(Anlow, +1j*Rq, format="csr")
    L.eliminate_zeros()
    return L.tocsr(), labels


def spectrum(L):
    k = min(12, L.shape[0]-2)
    t0 = time.perf_counter()
    try:
        vals, vecs = eigs(L, k=k, which="LR", tol=2e-9, maxiter=60000,
                          ncv=min(max(4*k, 32), L.shape[0]-1))
        conv=True; note="NONE"
    except ArpackNoConvergence as exc:
        vals=np.asarray(exc.eigenvalues); vecs=np.asarray(exc.eigenvectors)
        conv=False; note=f"ARPACK_NO_CONVERGENCE returned={len(vals)}"
    runtime=time.perf_counter()-t0
    if len(vals)==0:
        raise RuntimeError("FP spectrum returned no eigenpairs")
    order=np.argsort(vals.real)[::-1]
    return vals[order], vecs[:,order], conv, note, runtime


def run_case(name: str):
    cfg=CASES[name]
    dim=cfg["dim"]
    wc,xop,uop,H,d,z,ref=harmonic_setup(dim,cfg["npade"])
    L,labels=fp_generator(H,xop,d,z,cfg["depth"])
    tiers=np.asarray([sum(lab) for lab in labels],int)
    expected=math.comb(2*len(d)+cfg["depth"],cfg["depth"])
    print(
        f"CASE={name} dim={dim} Npade={cfg['npade']} depth={cfg['depth']} "
        f"Kcorr={len(d)} ncoord={2*len(d)} nado={len(labels)} expected={expected} "
        f"full_dim={L.shape[0]} nnz={L.nnz} wc/2pi={wc/(2*math.pi)*1e-9:.9f}GHz",
        flush=True,
    )
    if len(labels)!=expected or labels[0]!=(0,)*(2*len(d)):
        raise RuntimeError("FP hierarchy enumeration failure")
    for k,(dk,zk) in enumerate(zip(d,z)):
        print(f"MODE {k:02d} d=({dk.real:+.12e}{dk.imag:+.12e}j) "
              f"z=({zk.real:+.12e}{zk.imag:+.12e}j)",flush=True)
    print(f"REFERENCE basis_err={ref['basis_err']:.12e} "
          f"target_x={ref['target_x']:.12e} target_u={ref['target_u']:.12e}",flush=True)

    vals,vecs,conv,note,spec_s=spectrum(L)
    for j,lam in enumerate(vals):
        v=vecs[:,j]
        r=L@v-lam*v
        den=max(float(np.linalg.norm(L@v)),abs(lam)*float(np.linalg.norm(v)),1e-12)
        rel=float(np.linalg.norm(r))/den
        print(f"EIG {j:02d} lambda=({lam.real:+.12e}{lam.imag:+.12e}j) relres={rel:.3e}",flush=True)
    npos=int(np.sum(vals.real>1e-7))
    nzero=int(np.sum(np.abs(vals)<1e-7))
    window_safe=bool(vals[-1].real < -1e-3)
    print(f"SPECTRUM converged={conv} note={note} runtime_s={spec_s:.3f} "
          f"rightmost_Re={vals[0].real:+.12e} positive={npos} nearzero={nzero} "
          f"minReturnedRe={vals[-1].real:+.12e} window_safe={window_safe}",flush=True)

    vss,solve_s,res_abs,res_rel,warn=steady.constrained_nullvector(L,dim)
    m=steady.reduced_metrics(vss,dim,ref)
    maxfdt=max(abs(m["relx"]),abs(m["relu"]))
    print(f"NULLSPACE solve_s={solve_s:.3f} residual={res_abs:.12e} "
          f"scaled={res_rel:.12e} warnings={warn or 'NONE'}",flush=True)
    print(f"STATE trace=({m['trace'].real:.12e}{m['trace'].imag:+.2e}j) "
          f"anti={m['anti']:.12e} eigmin={m['eigmin']:+.12e} negmass={m['neg']:.12e}",flush=True)
    print(f"ORACLE relx={m['relx']:+.12e} relu={m['relu']:+.12e} maxFDT={maxfdt:.12e} "
          f"half_nuclear={m['half_nuclear']:.12e} frobenius={m['frob']:.12e}",flush=True)

    # Where does the dominant returned nonzero/rightmost mode live in hierarchy
    # tier?  This is descriptive only and does not modify the generator.
    jdom=0
    if abs(vals[0])<1e-7 and len(vals)>1:
        jdom=1
    vv=vecs[:,jdom]/np.linalg.norm(vecs[:,jdom])
    s=dim*dim
    tierw={}
    for a,tier in enumerate(tiers):
        w=float(np.sum(np.abs(vv[a*s:(a+1)*s])**2))
        tierw[int(tier)]=tierw.get(int(tier),0.0)+w
    print("TIER_WEIGHTS " + " ".join(f"t{t}={tierw[t]:.6e}" for t in sorted(tierw)),flush=True)

    checks={
        "reference_basis":ref["basis_err"]<1e-7,
        "fdt":maxfdt<1e-6,
        "half_nuclear":m["half_nuclear"]<5e-6,
        "negative_mass":m["neg"]<5e-8,
        "trace":abs(m["trace"]-1)<1e-10,
        "hermiticity":m["anti"]<1e-10,
        "null_residual":res_abs<1e-8,
    }
    for key,ok in checks.items():
        print(f"CHECK {key}={'PASS' if ok else 'FAIL'}",flush=True)
    msg=(f"FP_HARMONIC case={name} rightmost_Re={vals[0].real:.6e} positive={npos} "
         f"maxFDT={maxfdt:.6e} half_nuclear={m['half_nuclear']:.6e} "
         f"negmass={m['neg']:.6e} eigmin={m['eigmin']:.6e} "
         f"oracle_pass={all(checks.values())}")
    print(msg,flush=True)
    print(f"::notice title=Experiment 03 FP-HEOM harmonic oracle::{msg}",flush=True)

    if not window_safe:
        raise RuntimeError("FP rightmost spectral window did not extend into left half-plane")
    if res_abs>=1e-8:
        raise RuntimeError("FP stationary solve residual too large")


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--case",choices=sorted(CASES),required=True)
    args=ap.parse_args(); run_case(args.case)
