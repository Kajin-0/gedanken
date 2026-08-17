#!/usr/bin/env python3
"""Localize finite-HEOM unstable eigenmodes in hierarchy tier and system level.

The nonlinear and harmonic hard-cutoff HEOM generators have explicitly resolved
right-half-plane eigenmodes.  This script asks where the dominant mode lives.
For its normalized right eigenvector it reports:

* Frobenius-norm weight carried by each hierarchy tier;
* aggregate row/column weight carried by each retained system eigenstate;
* physical/root-ADO fraction;
* cumulative weight in the top one, two, and three retained system states.

The system-level weight for level i is defined as half the sum of squared matrix
entries in row i and column i, aggregated over all ADOs.  It sums to unity and
therefore quantifies localization near the artificial Hilbert-space boundary.

No generator modification or projection is performed.
"""
from __future__ import annotations

import argparse
import math
import time
import numpy as np
from scipy.sparse.linalg import eigs
from qutip.solver.heom import BosonicBath, HEOMSolver

import heom_schur_terminator_harmonic_probe as schur
import heom_nonlinear_leftwell_pilot as pilot
import heom_harmonic_pade_depth as bathbase

CASES = {
    "harmonic_dim12_p4d3": dict(kind="harmonic", dim=12, npade=4, depth=3),
    "nonlinear_dim10_p4d5": dict(kind="nonlinear", dim=10, npade=4, depth=5,
                                  xmin=-3.8, ngrid=2200),
}


def build(cfg):
    if cfg["kind"] == "harmonic":
        wc, _tx, _tu, _xop, _uop, H, bath = schur.harmonic_setup(cfg["dim"], cfg["npade"])
        solver = HEOMSolver(H, bath, max_depth=cfg["depth"], options={"progress_bar":""})
        return wc, solver
    (_model, _xm, _xs, wc, _e, yop, _y2op, _h0, hsys, _rho0, _res) = pilot.nonlinear_system(cfg)
    cr,vr,ci,vi = bathbase.pade_bath_expansion(wc,cfg["npade"])
    bath = BosonicBath(yop,cr,vr,ci,vi,combine=True,tag="direct-port-pade-localize")
    solver = HEOMSolver(hsys,bath,max_depth=cfg["depth"],options={"progress_bar":""})
    return wc, solver


def run_case(name):
    cfg=CASES[name]
    wc,solver=build(cfg)
    L=schur.scipy_rhs(solver)
    dim=cfg["dim"]
    s=dim*dim
    nado=len(solver.ados.labels)
    print(
        f"CASE={name} kind={cfg['kind']} dim={dim} Npade={cfg['npade']} depth={cfg['depth']} "
        f"nexp={len(solver.ados.exponents)} nado={nado} full_dim={L.shape[0]} nnz={L.nnz} "
        f"wc/2pi={wc/(2*math.pi)*1e-9:.9f}GHz",flush=True,
    )

    t0=time.perf_counter()
    vals,vecs=eigs(L,k=4,which="LR",tol=2e-9,maxiter=50000,ncv=32)
    runtime=time.perf_counter()-t0
    j=int(np.argmax(vals.real)); lam=vals[j]; v=vecs[:,j]
    v=v/np.linalg.norm(v)
    r=L@v-lam*v
    relres=float(np.linalg.norm(r))/max(float(np.linalg.norm(L@v)),abs(lam),1e-12)
    print(
        f"DOMINANT lambda=({lam.real:+.12e}{lam.imag:+.12e}j) relres={relres:.3e} "
        f"runtime_s={runtime:.3f}",flush=True,
    )
    if lam.real <= 1e-7:
        raise RuntimeError("selected case has no resolved right-half-plane dominant mode")

    tier_w={}
    level_w=np.zeros(dim,float)
    root_w=0.0
    for a,label in enumerate(solver.ados.labels):
        block=v[a*s:(a+1)*s].reshape((dim,dim),order="F")
        abs2=np.abs(block)**2
        w=float(abs2.sum())
        tier=sum(label)
        tier_w[tier]=tier_w.get(tier,0.0)+w
        if a==0:
            root_w=w
        rows=abs2.sum(axis=1)
        cols=abs2.sum(axis=0)
        level_w += 0.5*(rows+cols)

    normcheck=sum(tier_w.values())
    levelcheck=float(level_w.sum())
    print(f"NORM tier_sum={normcheck:.12e} level_sum={levelcheck:.12e} root_weight={root_w:.12e}",flush=True)
    for tier in sorted(tier_w):
        print(f"TIER {tier:02d} weight={tier_w[tier]:.12e}",flush=True)
    for i,w in enumerate(level_w):
        print(f"LEVEL {i:02d} weight={w:.12e}",flush=True)

    top1=float(level_w[-1])
    top2=float(level_w[-2:].sum()) if dim>=2 else top1
    top3=float(level_w[-3:].sum()) if dim>=3 else top2
    mean_level=float(np.dot(np.arange(dim),level_w))
    print(
        f"BOUNDARY top1={top1:.12e} top2={top2:.12e} top3={top3:.12e} "
        f"mean_level={mean_level:.9f} of_max={dim-1}",flush=True,
    )
    msg=(
        f"UNSTABLE_LOCALIZATION case={name} Re={lam.real:.6e} root={root_w:.6e} "
        f"top1={top1:.6e} top2={top2:.6e} top3={top3:.6e} "
        f"terminal_tier={tier_w.get(cfg['depth'],0.0):.6e} mean_level={mean_level:.6f}"
    )
    print(msg,flush=True)
    print(f"::notice title=Experiment 03 HEOM unstable-mode localization::{msg}",flush=True)


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--case",choices=sorted(CASES),required=True)
    args=ap.parse_args(); run_case(args.case)
