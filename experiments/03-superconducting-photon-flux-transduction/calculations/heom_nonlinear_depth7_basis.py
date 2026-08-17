#!/usr/bin/env python3
"""Depth-seven basis discriminator for nonlinear left-well HEOM Gate C.1.

Depth six is stationary and mutually consistent for dim=8,9 but dim=10 develops
a delayed nonphysical finite-tier mode.  This script changes only hierarchy depth
to 7 and compares dim=9 and dim=10 under the same physical model, Padé order,
domain, time grid, and tolerances.  It is a convergence discriminator, not a
Gate-C acceptance calculation.
"""
from __future__ import annotations

import argparse
import math
import time
import numpy as np

from qutip.solver.heom import BosonicBath, HEOMSolver

import heom_nonlinear_leftwell_pilot as pilot
import heom_harmonic_pade_depth as bathbase

CASES = {
    "dim9_p4d7": 9,
    "dim10_p4d7": 10,
}


def run_case(name):
    dim = CASES[name]
    depth = 7
    npade = 4
    cfg = dict(xmin=-3.8, ngrid=2200, dim=dim, npade=npade, depth=depth)
    (_model, xm, xs, wc, e, yop, y2op, h0, hsys, rho0, residuals) = pilot.nonlinear_system(cfg)
    cr, vr, ci, vi = bathbase.pade_bath_expansion(wc, npade)
    bath = BosonicBath(yop, cr, vr, ci, vi, combine=True, tag="direct-port-pade-nonlinear")
    nexp = len(bath.exponents)
    nado = math.comb(nexp + depth, depth)

    print(
        f"CASE={name} dim={dim} Npade={npade} depth={depth} "
        f"nexp={nexp} nado_est={nado}", flush=True
    )
    print(
        f"xm={xm:+.10f} xs={xs:+.10f} wc/2pi={wc/(2*math.pi)*1e-9:.9f}GHz "
        f"max_DVR_residual_K={float(np.max(residuals)):.3e}", flush=True
    )
    print(
        "transitions_K=" + ",".join(f"{q:.9e}" for q in (e-e[0])/pilot.KB),
        flush=True,
    )

    solver = HEOMSolver(
        hsys,
        bath,
        max_depth=depth,
        options={
            "progress_bar": "",
            "store_states": True,
            "method": "bdf",
            "rtol": 2e-7,
            "atol": 2e-9,
            "nsteps": 1000000,
        },
    )
    tlist = np.array([0., 10., 20., 40., 80., 120., 160.])
    t0 = time.perf_counter()
    result = solver.run(rho0, tlist, e_ops=[yop, y2op, h0])
    runtime = time.perf_counter() - t0

    rows = []
    for i, tau in enumerate(tlist):
        m = pilot.state_metrics(result.states[i], yop, y2op, h0, rho0)
        rows.append(m)
        maxabs = float(np.max(np.abs(np.asarray(result.states[i].full(), dtype=complex))))
        print(
            f"tau={tau:7.1f} trace=({m['trace'].real:+.10e}{m['trace'].imag:+.2e}j) "
            f"mean_y={m['mean']:+.10e} sigma_y={m['sigma']:.10e} E0={m['energy']:+.10e} "
            f"eigmin={m['eigmin']:+.9e} negmass={m['neg']:.9e} "
            f"topPop={m['top']:+.9e} maxabsrho={maxabs:.9e}", flush=True
        )

    f, p = rows[-1], rows[-2]
    late = max(
        abs(f["mean"] - p["mean"]),
        abs(f["sigma"] - p["sigma"]),
        abs(f["energy"] - p["energy"]),
    )
    msg = (
        f"CASE={name} FINAL trace=({f['trace'].real:.12e}{f['trace'].imag:+.2e}j) "
        f"antiherm={f['anti']:.3e} eigmin={f['eigmin']:+.9e} negmass={f['neg']:.9e} "
        f"mean_y={f['mean']:+.10e} sigma_y={f['sigma']:.10e} E0={f['energy']:+.10e} "
        f"topPop={f['top']:+.9e} bareGibbs_nuclear_half={f['gibbs_half']:.9e} "
        f"late_abs_drift={late:.9e} runtime_s={runtime:.3f}"
    )
    print(msg, flush=True)
    print(f"::notice title=Experiment 03 nonlinear HEOM depth7 basis::{msg}", flush=True)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--case", choices=sorted(CASES), required=True)
    args = ap.parse_args()
    run_case(args.case)
