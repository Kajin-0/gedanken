#!/usr/bin/env python3
"""Controlled Schur-terminator probe for the Experiment-03 harmonic HEOM.

This implements the finite-dimensional HEOM approximation of Vadimov
(arXiv:2604.22568, Eq. 26) directly from QuTiP's own hierarchy RHS blocks:

    L_T = L_TT - L_Tbar (L'_barbar)^(-1) L_barT.

For a total-depth truncation, the retained sector T contains levels <= d.  The
only discarded ADOs directly coupled to T are level d+1.  Because L' keeps only
diagonal hierarchy blocks, the required tail inverse is therefore obtained from
the diagonal blocks of a QuTiP depth-(d+1) RHS.  This avoids re-deriving any
QuTiP bath coefficients or ADO scaling conventions by hand.

The probe first validates that the extracted L_TT exactly reproduces QuTiP's raw
depth-d RHS.  It then compares raw and Schur-terminated harmonic dynamics against
the independent exact FDT covariance oracle already used for Gate B.

This is a method-development diagnostic only.  It does not reopen or alter the
already-passed harmonic Gate B and does not authorize nonlinear detector claims.
"""
from __future__ import annotations

import argparse
import math
import time
import numpy as np
import scipy.linalg as la
import scipy.sparse as sp
from scipy.sparse.linalg import expm_multiply

import full_dynamic_rfsquid as fd
from finite_time_basin_slice import cold_phase_scale
from quantum_initial_capture import HBAR, PHI_BAR
from two_pole_joint_covariance import covariance_matrix
from heom_harmonic_port_validation import R, G, WD, L, C, DELTA, ALPHA
from heom_harmonic_pade_depth import pade_bath_expansion

from qutip import destroy, qeye
from qutip.solver.heom import BosonicBath, HEOMSolver


CASES = {
    "p4d2": dict(dim=8, npade=4, depth=2),
    "p4d3": dict(dim=8, npade=4, depth=3),
}


def scipy_rhs(solver: HEOMSolver) -> sp.csr_matrix:
    """Return constant QuTiP HEOM RHS as SciPy CSR."""
    q = solver.rhs(0)
    data = q.data
    if hasattr(data, "as_scipy"):
        return data.as_scipy().tocsr()
    return sp.csr_matrix(q.full())


def harmonic_setup(dim: int, npade: int):
    ob, ot = fd.BETA_COLD, fd.DELTA_TILT
    original = fd.CASES[.6]
    try:
        fd.BETA_COLD = .80
        fd.DELTA_TILT = DELTA
        fd.CASES[.6] = (L, C, original[2])
        model = fd.DynamicForce(.6, quick=False, Tmax=1.02)
        M = covariance_matrix(model, .6, R, ALPHA, y_min=-22, y_max=22)
        target_x = math.sqrt(M[0, 0])
        target_u = math.sqrt(M[1, 1])
        _xc, _kap, wc = cold_phase_scale(model, .6)

        sigma0 = math.sqrt(HBAR/(2*C*PHI_BAR**2*wc))
        a = destroy(dim)
        n = a.dag()*a
        xop = sigma0*(a+a.dag())
        uop = 1j*sigma0*(a.dag()-a)
        H = n + 0.5*qeye(dim)
        ct_phys = PHI_BAR**2/HBAR * G*WD/(2*math.sqrt(2))
        H = H + (ct_phys/wc)*(xop*xop)

        cr, vr, ci, vi = pade_bath_expansion(wc, npade)
        bath = BosonicBath(
            xop, cr, vr, ci, vi, combine=True, tag="direct-port-pade-schur"
        )
        return wc, target_x, target_u, xop, uop, H, bath
    finally:
        fd.BETA_COLD = ob
        fd.DELTA_TILT = ot
        fd.CASES[.6] = original


def build_schur_rhs(H, bath, dim: int, depth: int):
    """Build Eq.-26 Schur-terminated RHS in raw depth-d ADO ordering."""
    opts = {"progress_bar": ""}
    raw = HEOMSolver(H, bath, max_depth=depth, options=opts)
    ext = HEOMSolver(H, bath, max_depth=depth+1, options=opts)
    Lraw = scipy_rhs(raw)
    Lext = scipy_rhs(ext)
    s = dim*dim

    # Retained flattened indices in precisely the raw solver's ADO ordering.
    tflat_parts = []
    for label in raw.ados.labels:
        j = ext.ados.idx(label)
        tflat_parts.append(j*s + np.arange(s, dtype=int))
    tflat = np.concatenate(tflat_parts)
    A = Lext[tflat, :][:, tflat].tocsr()

    diff = (A-Lraw).tocsr()
    raw_match = 0.0 if diff.nnz == 0 else float(np.max(np.abs(diff.data)))

    rr_all: list[np.ndarray] = []
    cc_all: list[np.ndarray] = []
    vv_all: list[np.ndarray] = []
    omitted = [lab for lab in ext.ados.labels if sum(lab) == depth+1]

    t0 = time.perf_counter()
    for lab in omitted:
        j = ext.ados.idx(lab)
        mflat = j*s + np.arange(s, dtype=int)
        Bm = Lext[tflat, :][:, mflat].tocsr()
        Cm = Lext[mflat, :][:, tflat].tocsr()
        if Bm.nnz == 0 or Cm.nnz == 0:
            continue
        active_r = np.unique(Bm.nonzero()[0])
        active_c = np.unique(Cm.nonzero()[1])
        Dm = Lext[mflat, :][:, mflat].toarray()
        Bsmall = Bm[active_r, :].toarray()
        Csmall = Cm[:, active_c].toarray()
        X = la.solve(Dm, Csmall, assume_a="gen", check_finite=False)
        term = Bsmall @ X

        scale = max(1.0, float(np.max(np.abs(term))))
        ii, jj = np.nonzero(np.abs(term) > 1e-14*scale)
        if len(ii):
            rr_all.append(active_r[ii])
            cc_all.append(active_c[jj])
            vv_all.append(term[ii, jj])

    if rr_all:
        corr = sp.coo_matrix(
            (np.concatenate(vv_all), (np.concatenate(rr_all), np.concatenate(cc_all))),
            shape=A.shape,
            dtype=complex,
        ).tocsr()
        corr.sum_duplicates()
    else:
        corr = sp.csr_matrix(A.shape, dtype=complex)

    Leff = (A-corr).tocsr()
    build_s = time.perf_counter()-t0
    return raw, Lraw, Leff, raw_match, len(omitted), corr.nnz, build_s


def rho_metrics(v, dim, xop, uop, target_x, target_u):
    rho = np.asarray(v[:dim*dim]).reshape((dim, dim), order="F")
    tr = complex(np.trace(rho))
    anti = np.linalg.norm(rho-rho.conj().T, ord="fro") / max(
        np.linalg.norm(rho, ord="fro"), 1e-300
    )
    rh = 0.5*(rho+rho.conj().T)
    ev = np.linalg.eigvalsh(rh)
    neg = float(np.sum(np.maximum(-ev, 0.0)))
    xo = xop.full(); uo = uop.full()
    mx = float(np.real(np.trace(xo@rho)))
    mu = float(np.real(np.trace(uo@rho)))
    x2 = float(np.real(np.trace((xo@xo)@rho)))
    u2 = float(np.real(np.trace((uo@uo)@rho)))
    sx = math.sqrt(max(x2-mx*mx, 0.0))
    su = math.sqrt(max(u2-mu*mu, 0.0))
    return dict(
        trace=tr, anti=anti, eigmin=float(ev.min()), neg=neg,
        sx=sx, su=su,
        relx=sx/target_x-1, relu=su/target_u-1,
    )


def propagate(label, Lmat, dim, xop, uop, target_x, target_u):
    n = Lmat.shape[0]
    v = np.zeros(n, dtype=complex)
    rho0 = np.zeros((dim, dim), dtype=complex); rho0[0, 0] = 1.0
    v[:dim*dim] = rho0.ravel(order="F")
    times = [0., 10., 20., 40., 80., 120.]
    last = 0.0
    rows = []
    t0 = time.perf_counter()
    for tau in times:
        dt = tau-last
        if dt > 0:
            v = expm_multiply(Lmat*dt, v)
        m = rho_metrics(v, dim, xop, uop, target_x, target_u)
        rows.append(m)
        print(
            f"MODE={label} tau={tau:7.1f} relx={m['relx']:+.6e} relu={m['relu']:+.6e} "
            f"trace=({m['trace'].real:+.12e}{m['trace'].imag:+.2e}j) "
            f"anti={m['anti']:.3e} eigmin={m['eigmin']:+.9e} negmass={m['neg']:.9e}",
            flush=True,
        )
        last = tau
    runtime = time.perf_counter()-t0
    f, p = rows[-1], rows[-2]
    drift = max(abs(f['sx']-p['sx'])/target_x, abs(f['su']-p['su'])/target_u)
    print(
        f"MODE={label} FINAL maxFDT={max(abs(f['relx']),abs(f['relu'])):.9e} "
        f"late_rel_drift={drift:.9e} eigmin={f['eigmin']:+.9e} "
        f"negmass={f['neg']:.9e} runtime_s={runtime:.3f}", flush=True
    )
    return f


def run_case(name: str):
    cfg = CASES[name]
    dim, npade, depth = cfg['dim'], cfg['npade'], cfg['depth']
    wc, tx, tu, xop, uop, H, bath = harmonic_setup(dim, npade)
    print(
        f"CASE={name} dim={dim} Npade={npade} depth={depth} "
        f"nexp={len(bath.exponents)} wc/2pi={wc/(2*math.pi)*1e-9:.9f}GHz",
        flush=True,
    )
    print(f"TARGET sigma_x={tx:.12e} sigma_u={tu:.12e}", flush=True)
    raw, Lraw, Leff, rhs_match, nomit, corr_nnz, build_s = build_schur_rhs(
        H, bath, dim, depth
    )
    print(
        f"SCHUR_BUILD retained_ados={len(raw.ados.labels)} omitted_interface={nomit} "
        f"raw_block_match_maxabs={rhs_match:.3e} correction_nnz={corr_nnz} "
        f"build_s={build_s:.3f}", flush=True
    )
    if rhs_match > 1e-12:
        raise RuntimeError(f"retained RHS extraction mismatch {rhs_match}")

    fr = propagate("RAW", Lraw, dim, xop, uop, tx, tu)
    fs = propagate("SCHUR", Leff, dim, xop, uop, tx, tu)
    print(
        f"COMPARISON raw_neg={fr['neg']:.9e} schur_neg={fs['neg']:.9e} "
        f"raw_maxFDT={max(abs(fr['relx']),abs(fr['relu'])):.9e} "
        f"schur_maxFDT={max(abs(fs['relx']),abs(fs['relu'])):.9e}", flush=True
    )
    print("PASS_METHOD_PROBE", flush=True)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--case", choices=sorted(CASES), required=True)
    args = ap.parse_args()
    run_case(args.case)
