#!/usr/bin/env python3
"""Biorthogonal stable-mode projection validation on an unstable harmonic HEOM.

Purpose
-------
The nonlinear hard-cutoff HEOM has directly demonstrated right-half-plane modes.
Before any unstable-mode projection is considered for nonlinear Gate C/D, the
projection must be challenged on a problem with an independent exact open-system
oracle.

The test case is the harmonic direct-port model at dim=12, Npade=4, depth=3.
Its finite HEOM generator has resolved right-half-plane modes while the exact
cold reduced state is independently fixed by quantum FDT.  We construct a
biorthogonal spectral projector from right eigenvectors of L and matching left
eigenvectors of L^dagger,

    P = I - R (W^dagger R)^(-1) W^dagger,

where R and W span only eigenmodes with Re(lambda)>0.  The projected trajectory
is evolved with the *unchanged* HEOM generator and reprojected after each output
interval to suppress roundoff re-entry into the unstable subspace.

This is a diagnostic, not a production solver.  Projection is accepted as a
candidate stabilization mechanism only if it removes exponential growth without
breaking trace/Hermiticity and its late reduced state is quantitatively compared
against the exact FDT/Gaussian state.  No density-matrix clipping, positivity
repair, bath change, counterterm change, or parameter refit is allowed.
"""
from __future__ import annotations

import math
import time
import numpy as np
from scipy.linalg import solve, svdvals
from scipy.optimize import linear_sum_assignment
from scipy.sparse.linalg import eigs, expm_multiply

import heom_schur_terminator_harmonic_probe as schur
import heom_harmonic_final_state_gate as finalgate
import heom_harmonic_steady_nullspace_probe as steady
from qutip.solver.heom import HEOMSolver

DIM = 12
NPADE = 4
DEPTH = 3
POS_TOL = 1.0e-7
K_EIG = 20
TIMES = np.array([0., 10., 20., 40., 80., 120., 160.])


def eig_residual(L, lam, v):
    r = L @ v - lam*v
    den = max(float(np.linalg.norm(L @ v)), abs(lam)*float(np.linalg.norm(v)), 1e-12)
    return float(np.linalg.norm(r))/den


def compute_projector(L):
    """Return callable P plus complete unstable left/right diagnostics."""
    t0 = time.perf_counter()
    rv, Rall = eigs(L, k=K_EIG, which="LR", tol=1e-9,
                    maxiter=50000, ncv=64)
    right_s = time.perf_counter()-t0
    order = np.argsort(rv.real)[::-1]
    rv, Rall = rv[order], Rall[:, order]

    t0 = time.perf_counter()
    lv, Wall = eigs(L.conj().T, k=K_EIG, which="LR", tol=1e-9,
                    maxiter=50000, ncv=64)
    left_s = time.perf_counter()-t0
    order = np.argsort(lv.real)[::-1]
    lv, Wall = lv[order], Wall[:, order]

    ir = np.where(rv.real > POS_TOL)[0]
    il = np.where(lv.real > POS_TOL)[0]
    if len(ir) == 0:
        raise RuntimeError("no unstable right modes found in known unstable oracle case")
    if len(ir) != len(il):
        raise RuntimeError(
            f"unstable left/right mode count mismatch right={len(ir)} left={len(il)}"
        )

    # Ensure the requested spectral window extends beyond the unstable sector.
    # Otherwise a positive mode could be hidden outside the returned set.
    if rv[-1].real >= -1e-3 or lv[-1].real >= -1e-3:
        raise RuntimeError(
            "rightmost spectral window does not extend safely into left half-plane"
        )

    urv = rv[ir]
    R = Rall[:, ir]
    ulv = lv[il]
    Wcand = Wall[:, il]

    # Left eigenvalue mu of L^dagger matches right lambda when mu=conj(lambda).
    cost = np.abs(urv[:, None].conj() - ulv[None, :])
    rows, cols = linear_sum_assignment(cost)
    if not np.array_equal(rows, np.arange(len(ir))):
        raise RuntimeError("unexpected assignment ordering")
    W = Wcand[:, cols]
    mlv = ulv[cols]
    match = np.abs(mlv - urv.conj())

    B = W.conj().T @ R
    condB = float(np.linalg.cond(B))
    Binv = np.linalg.inv(B)

    def project(v):
        return v - R @ (Binv @ (W.conj().T @ v))

    # Projector implementation checks without materializing dense P.
    rng = np.random.default_rng(20260817)
    z = rng.normal(size=L.shape[0]) + 1j*rng.normal(size=L.shape[0])
    pz = project(z)
    ppz = project(pz)
    idem = float(np.linalg.norm(ppz-pz))/max(float(np.linalg.norm(pz)), 1e-300)
    annih_R = float(np.linalg.norm(project(R)))/max(float(np.linalg.norm(R)), 1e-300)
    left_leak = float(np.linalg.norm(W.conj().T @ pz))/max(
        float(np.linalg.norm(W.conj().T @ z)), 1e-300
    )

    print(
        f"SPECTRUM right_s={right_s:.3f} left_s={left_s:.3f} "
        f"right_returned={len(rv)} left_returned={len(lv)} "
        f"unstable={len(ir)} right_edge_minRe={rv[-1].real:+.6e} "
        f"left_edge_minRe={lv[-1].real:+.6e}", flush=True
    )
    for j, lam in enumerate(urv):
        rr = eig_residual(L, lam, R[:, j])
        lr = eig_residual(L.conj().T, mlv[j], W[:, j])
        print(
            f"UNSTABLE {j:02d} lambda=({lam.real:+.12e}{lam.imag:+.12e}j) "
            f"left=({mlv[j].real:+.12e}{mlv[j].imag:+.12e}j) "
            f"match={match[j]:.3e} right_res={rr:.3e} left_res={lr:.3e}",
            flush=True,
        )
    print(
        f"BIORTH cond_WdagR={condB:.6e} max_match={float(np.max(match)):.3e} "
        f"projector_idempotence={idem:.3e} annihilate_R={annih_R:.3e} "
        f"left_leak={left_leak:.3e}", flush=True
    )

    if not np.isfinite(condB) or condB > 1e10:
        raise RuntimeError(f"unstable biorthogonal overlap ill-conditioned: {condB}")
    if np.max(match) > 1e-7:
        raise RuntimeError("left/right unstable eigenvalue matching failed")
    if idem > 1e-10 or annih_R > 1e-10 or left_leak > 1e-10:
        raise RuntimeError("spectral projector numerical validation failed")

    return project, urv, rv, condB


def report_state(mode, tau, v, ref):
    m = steady.reduced_metrics(v, DIM, ref)
    root = np.asarray(v[:DIM*DIM]).reshape((DIM, DIM), order="F")
    top = float(np.real(root[-1, -1]))
    maxabs = float(np.max(np.abs(root)))
    print(
        f"MODE={mode} tau={tau:7.1f} "
        f"trace=({m['trace'].real:+.12e}{m['trace'].imag:+.2e}j) "
        f"anti={m['anti']:.3e} eigmin={m['eigmin']:+.9e} "
        f"negmass={m['neg']:.9e} relx={m['relx']:+.9e} relu={m['relu']:+.9e} "
        f"half_nuclear={m['half_nuclear']:.9e} topPop={top:+.9e} "
        f"maxabsrho={maxabs:.9e}", flush=True
    )
    return m


def main():
    wc, tx, tu, xop, uop, H, bath = schur.harmonic_setup(DIM, NPADE)
    solver = HEOMSolver(H, bath, max_depth=DEPTH, options={"progress_bar": ""})
    L = schur.scipy_rhs(solver)
    ref = finalgate.exact_reference(DIM)

    print(
        f"CASE harmonic_projection dim={DIM} Npade={NPADE} depth={DEPTH} "
        f"nexp={len(bath.exponents)} nado={len(solver.ados.labels)} "
        f"full_dim={L.shape[0]} nnz={L.nnz} wc/2pi={wc/(2*math.pi)*1e-9:.9f}GHz",
        flush=True,
    )
    print(
        f"REFERENCE basis_err={ref['basis_err']:.12e} "
        f"sigma_x={ref['target_x']:.12e} sigma_u={ref['target_u']:.12e}",
        flush=True,
    )

    project, unstable, _rv, condB = compute_projector(L)

    # Bare oscillator ground state in the physical ADO; all auxiliary ADOs zero.
    n = L.shape[0]
    v0 = np.zeros(n, dtype=complex)
    rho0 = np.zeros((DIM, DIM), dtype=complex)
    rho0[0, 0] = 1.0
    v0[:DIM*DIM] = rho0.ravel(order="F")
    vp = project(v0)

    # Quantify how invasive projection is before any propagation.
    root0 = v0[:DIM*DIM].reshape((DIM,DIM), order="F")
    rootp = vp[:DIM*DIM].reshape((DIM,DIM), order="F")
    init_half = 0.5*float(np.sum(svdvals(rootp-root0)))
    init_full_rel = float(np.linalg.norm(vp-v0))/max(float(np.linalg.norm(v0)),1e-300)
    unstable_leak = float(np.linalg.norm(vp-project(vp)))/max(float(np.linalg.norm(vp)),1e-300)
    print(
        f"INITIAL_PROJECTION root_trace_before={np.trace(root0):+.12e} "
        f"root_trace_after={np.trace(rootp):+.12e} "
        f"root_half_nuclear_change={init_half:.12e} full_rel_change={init_full_rel:.12e} "
        f"projector_repeat_residual={unstable_leak:.3e}", flush=True
    )

    vraw = v0.copy()
    vproj = vp.copy()
    last = 0.0
    raw_rows=[]; proj_rows=[]
    for tau in TIMES:
        dt = tau-last
        if dt > 0:
            vraw = expm_multiply(L*dt, vraw)
            vproj = expm_multiply(L*dt, vproj)
            vproj = project(vproj)
        raw_rows.append(report_state("RAW", tau, vraw, ref))
        proj_rows.append(report_state("PROJECTED", tau, vproj, ref))
        last = tau

    fr = raw_rows[-1]
    fp = proj_rows[-1]
    proj_maxfdt=max(abs(fp['relx']),abs(fp['relu']))
    raw_maxfdt=max(abs(fr['relx']),abs(fr['relu']))

    # Projection-validation criteria are intentionally split into stabilization
    # and physical-state accuracy.  A stabilization success is not a Gate-B or
    # Gate-C pass if the finite-depth stationary state remains inaccurate.
    stable_checks = {
        "trace": abs(fp['trace']-1.0) < 1e-10,
        "hermiticity": fp['anti'] < 1e-10,
        "finite": all(np.isfinite(q) for q in [fp['eigmin'],fp['neg'],fp['relx'],fp['relu'],fp['half_nuclear']]),
        "no_exponential_blowup": fp['half_nuclear'] < 1.0,
    }
    oracle_checks = {
        "reference_basis": ref['basis_err'] < 1e-7,
        "fdt": proj_maxfdt < 1e-6,
        "half_nuclear": fp['half_nuclear'] < 5e-6,
        "negative_mass": fp['neg'] < 5e-8,
    }
    for k,v in stable_checks.items():
        print(f"STABILIZATION {k}={'PASS' if v else 'FAIL'}")
    for k,v in oracle_checks.items():
        print(f"ORACLE {k}={'PASS' if v else 'FAIL'}")

    msg=(
        f"PROJECTION_VALIDATION unstable_modes={len(unstable)} cond={condB:.3e} "
        f"raw_maxFDT={raw_maxfdt:.6e} raw_half={fr['half_nuclear']:.6e} "
        f"raw_neg={fr['neg']:.6e} projected_maxFDT={proj_maxfdt:.6e} "
        f"projected_half={fp['half_nuclear']:.6e} projected_neg={fp['neg']:.6e} "
        f"stabilization_pass={all(stable_checks.values())} "
        f"oracle_pass={all(oracle_checks.values())}"
    )
    print(msg,flush=True)
    print(f"::notice title=Experiment 03 harmonic stable-mode projection::{msg}",flush=True)

    # Fail only on projector implementation/stabilization defects, not because
    # an intentionally shallow hierarchy fails the exact-state oracle.
    if not all(stable_checks.values()):
        raise RuntimeError("stable-mode projection failed basic stabilization checks")


if __name__ == "__main__":
    main()
