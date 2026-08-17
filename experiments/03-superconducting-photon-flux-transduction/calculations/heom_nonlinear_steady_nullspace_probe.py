#!/usr/bin/env python3
"""Stationary zero-mode probe for nonlinear restricted-left-well HEOM Gate C.1.

The raw nonlinear HEOM time generator is non-monotone in hierarchy depth and
contains spurious growing modes at the failed depth-seven discriminator.  Gate
C.1, however, concerns cold metastable-state preparation before any finite-time
photon trajectory is attempted.  This script therefore asks a narrower question:

    does the finite hierarchy still possess a trace-normalized stationary zero
    mode whose reduced state is physical and convergent?

It solves L v = 0 with Tr(rho_top)=1 directly, without time propagation,
positivity projection, clipping, or state repair.

Two stages are intentionally separated:
* dim8,p4,d5 is a method control because ordinary propagation at that tier is
  settled and its final reduced state is already recorded.
* dim8,p4,d7 interrogates a deeper raw hierarchy after the time-domain route has
  been rejected.  A favorable result at this single tier cannot pass Gate C.1;
  it only determines whether a stationary-state route deserves basis/depth
  convergence tests.

This calculation does not validate transient dynamics and cannot open Gate D.
"""
from __future__ import annotations

import argparse
import math
import time
import numpy as np

from qutip import Qobj
from qutip.solver.heom import BosonicBath, HEOMSolver

import heom_nonlinear_leftwell_pilot as pilot
import heom_harmonic_pade_depth as bathbase
import heom_schur_terminator_harmonic_probe as schur
import heom_harmonic_steady_nullspace_probe as steady


CASES = {
    "dim8_p4d5_control": dict(xmin=-3.8, ngrid=2200, dim=8, npade=4, depth=5),
    "dim8_p4d7_test": dict(xmin=-3.8, ngrid=2200, dim=8, npade=4, depth=7),
}

# Previously recorded settled time-domain p4,d5,dim8 state.  This is used only
# as an implementation cross-check; it is not a target imposed on the solve.
CONTROL = dict(
    eigmin=-9.253018e-7,
    neg=9.968959e-7,
    mean=2.6118022031e-3,
    sigma=4.0116252752e-2,
    energy=3.0467301249e-2,
    top=-6.963007e-7,
)


def run_case(name: str):
    cfg = CASES[name]
    (_model, xm, xs, wc, e, yop, y2op, h0, hsys, rho0, residuals) = pilot.nonlinear_system(cfg)
    cr, vr, ci, vi = bathbase.pade_bath_expansion(wc, cfg["npade"])
    bath = BosonicBath(
        yop, cr, vr, ci, vi, combine=True, tag="direct-port-pade-nonlinear-steady"
    )
    solver = HEOMSolver(hsys, bath, max_depth=cfg["depth"], options={"progress_bar": ""})
    L = schur.scipy_rhs(solver)
    dim = cfg["dim"]
    nado = len(solver.ados.labels)

    print(
        f"CASE={name} delta={pilot.DELTA:.5f} dim={dim} Npade={cfg['npade']} "
        f"depth={cfg['depth']} nexp={len(bath.exponents)} nado={nado} "
        f"full_dim={L.shape[0]} nnz={L.nnz}", flush=True
    )
    print(
        f"xm={xm:+.10f} xs={xs:+.10f} wc/2pi={wc/(2*math.pi)*1e-9:.9f}GHz "
        f"max_DVR_residual_K={float(np.max(residuals)):.3e}", flush=True
    )

    t0 = time.perf_counter()
    v, solve_s, res_abs, res_rel, warn_text = steady.constrained_nullvector(L, dim)
    total_s = time.perf_counter()-t0
    rho_arr = np.asarray(v[:dim*dim], dtype=complex).reshape((dim, dim), order="F")
    rho = Qobj(rho_arr)
    m = pilot.state_metrics(rho, yop, y2op, h0, rho0)
    ado_max = float(np.max(np.abs(v[dim*dim:]))) if len(v) > dim*dim else 0.0

    print(
        f"NULLSPACE solve_s={solve_s:.3f} total_s={total_s:.3f} "
        f"residual_maxabs={res_abs:.12e} residual_scaled={res_rel:.12e} "
        f"warnings={warn_text or 'NONE'}", flush=True
    )
    print(
        f"REDUCED trace=({m['trace'].real:.12e}{m['trace'].imag:+.2e}j) "
        f"anti={m['anti']:.12e} eigmin={m['eigmin']:+.12e} "
        f"negmass={m['neg']:.12e} maxADO={ado_max:.12e}", flush=True
    )
    print(
        f"OBS mean_y={m['mean']:+.12e} sigma_y={m['sigma']:.12e} "
        f"E0_units={m['energy']:+.12e} topPop={m['top']:+.12e} "
        f"bareGibbs_half={m['gibbs_half']:.12e}", flush=True
    )

    hard = {
        "trace": abs(m["trace"]-1.0) < 1e-10,
        "hermiticity": m["anti"] < 1e-10,
        "negative_mass": m["neg"] < 5e-8,
        "top_population": abs(m["top"]) < 1e-6,
        "null_residual": res_abs < 1e-8,
    }
    for key, val in hard.items():
        print(f"CHECK {key}={'PASS' if val else 'FAIL'}", flush=True)

    if name.endswith("control"):
        diffs = {k: m[k]-CONTROL[k] for k in CONTROL}
        print(
            "CONTROL_DIFF " + " ".join(f"{k}={v:+.12e}" for k,v in diffs.items()),
            flush=True,
        )
        control_match = (
            abs(diffs["eigmin"]) < 5e-11 and
            abs(diffs["neg"]) < 5e-11 and
            abs(diffs["mean"]) < 5e-9 and
            abs(diffs["sigma"]) < 5e-9 and
            abs(diffs["energy"]) < 5e-7
        )
        print(f"CHECK control_match={'PASS' if control_match else 'FAIL'}", flush=True)
    else:
        control_match = True

    finite = np.all(np.isfinite(v))
    msg = (
        f"STEADY_NONLINEAR case={name} eigmin={m['eigmin']:.6e} "
        f"negmass={m['neg']:.6e} mean={m['mean']:.6e} sigma={m['sigma']:.6e} "
        f"E0={m['energy']:.6e} top={m['top']:.6e} residual={res_abs:.3e} "
        f"hard_physical={all(hard.values())} finite={finite} control_match={control_match}"
    )
    print(msg, flush=True)
    print(f"::notice title=Experiment 03 nonlinear HEOM stationary zero mode::{msg}", flush=True)

    if not finite:
        raise RuntimeError("non-finite stationary solution")
    if res_abs >= 1e-8:
        raise RuntimeError("stationary linear solve residual too large")
    if name.endswith("control") and not control_match:
        raise RuntimeError("stationary solver does not reproduce settled nonlinear control")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--case", choices=sorted(CASES), required=True)
    args = ap.parse_args()
    run_case(args.case)
