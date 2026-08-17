#!/usr/bin/env python3
"""Diagnose the dim=10 instability in the nonlinear left-well HEOM pilot.

This is a numerical-diagnostics calculation only.  It does not alter the
physical bath, counterterm, metastable well, or operating point.

The original pilot showed:
  dim=8, Npade=4, depth=5 : stable through tau=160
  dim=10,Npade=4, depth=5 : healthy through tau~20, then exponential blow-up

This script separates four hypotheses:
  1. system-basis threshold (dim 9 versus dim 10),
  2. hierarchy-depth pathology (dim 10 depth 4 versus depth 5),
  3. BDF internal-step artifact (depth 5 with max_step=0.1),
  4. integrator-specific artifact (LSODA with the same step cap).

No acceptance thresholds are defined here.  A growing trajectory is a valid
scientific diagnostic and is not hidden by a positivity projection or state
renormalization.
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
    "dim9_p4d5_bdf": dict(dim=9, depth=5, method="bdf", max_step=0.0),
    "dim10_p4d4_bdf": dict(dim=10, depth=4, method="bdf", max_step=0.0),
    "dim10_p4d5_bdf_cap": dict(dim=10, depth=5, method="bdf", max_step=0.1),
    "dim10_p4d5_lsoda_cap": dict(dim=10, depth=5, method="lsoda", max_step=0.1),
}


def matrix_norm_diagnostics(yop, y2op, h0, hsys):
    y=np.asarray(yop.full(),dtype=complex)
    y2=np.asarray(y2op.full(),dtype=complex)
    h=np.asarray(h0.full(),dtype=complex)
    hs=np.asarray(hsys.full(),dtype=complex)
    last=np.linalg.norm(y[-1,:])
    comm=h@y-y@h
    return {
        "y_2": float(np.linalg.norm(y,2)),
        "y_fro": float(np.linalg.norm(y,"fro")),
        "y_lastrow": float(last),
        "y2_2": float(np.linalg.norm(y2,2)),
        "h0_span": float(np.ptp(np.linalg.eigvalsh(h))),
        "hsys_span": float(np.ptp(np.linalg.eigvalsh(hs))),
        "comm_fro": float(np.linalg.norm(comm,"fro")),
    }


def run_case(name: str):
    c=CASES[name]
    cfg=dict(xmin=-3.8,ngrid=2200,dim=c["dim"],npade=4,depth=c["depth"])
    (_model,xm,xs,wc,e,yop,y2op,h0,hsys,rho0,residuals)=pilot.nonlinear_system(cfg)
    cr,vr,ci,vi=bathbase.pade_bath_expansion(wc,4)
    bath=BosonicBath(yop,cr,vr,ci,vi,combine=True,tag="direct-port-pade-nonlinear")
    nexp=len(bath.exponents)
    nado=math.comb(nexp+c["depth"],c["depth"])
    nd=matrix_norm_diagnostics(yop,y2op,h0,hsys)

    print(f"CASE={name} dim={c['dim']} depth={c['depth']} method={c['method']} "
          f"max_step={c['max_step']} nexp={nexp} nado_est={nado}",flush=True)
    print(f"xm={xm:+.10f} xs={xs:+.10f} wc/2pi={wc/(2*math.pi)*1e-9:.9f}GHz "
          f"max_DVR_residual_K={float(np.max(residuals)):.3e}",flush=True)
    print("transitions_K="+",".join(f"{q:.9e}" for q in (e-e[0])/pilot.KB),flush=True)
    print("NORMS "+" ".join(f"{k}={v:.12e}" for k,v in nd.items()),flush=True)

    opts={
        "progress_bar":"",
        "store_states":True,
        "method":c["method"],
        "rtol":2e-7,
        "atol":2e-9,
        "nsteps":500000,
    }
    if c["max_step"]>0:
        opts["max_step"]=c["max_step"]

    solver=HEOMSolver(hsys,bath,max_depth=c["depth"],options=opts)
    tlist=np.arange(0.0,65.0,5.0)
    t0=time.perf_counter()
    try:
        result=solver.run(rho0,tlist,e_ops=[yop,y2op,h0])
    except Exception as exc:
        print(f"INTEGRATOR_EXCEPTION type={type(exc).__name__} text={exc}",flush=True)
        raise
    runtime=time.perf_counter()-t0

    growth=False
    for i,tau in enumerate(tlist):
        m=pilot.state_metrics(result.states[i],yop,y2op,h0,rho0)
        maxabs=float(np.max(np.abs(np.asarray(result.states[i].full(),dtype=complex))))
        if maxabs>10 or abs(m["trace"]-1)>1e-3 or m["neg"]>1:
            growth=True
        print(f"tau={tau:6.1f} trace=({m['trace'].real:+.9e}{m['trace'].imag:+.2e}j) "
              f"mean_y={m['mean']:+.9e} sigma_y={m['sigma']:.9e} "
              f"E0={m['energy']:+.9e} eigmin={m['eigmin']:+.9e} "
              f"negmass={m['neg']:.9e} maxabsrho={maxabs:.9e}",flush=True)

    f=pilot.state_metrics(result.states[-1],yop,y2op,h0,rho0)
    print(f"FINAL case={name} growth_flag={growth} trace=({f['trace'].real:.12e}{f['trace'].imag:+.2e}j) "
          f"eigmin={f['eigmin']:+.9e} negmass={f['neg']:.9e} "
          f"mean_y={f['mean']:+.9e} sigma_y={f['sigma']:.9e} "
          f"E0={f['energy']:+.9e} runtime_s={runtime:.3f}",flush=True)
    print(f"::notice title=Experiment 03 nonlinear HEOM dim stability::case={name} growth={growth} "
          f"eigmin={f['eigmin']:+.3e} negmass={f['neg']:.3e}",flush=True)


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--case",choices=sorted(CASES),required=True)
    args=ap.parse_args()
    run_case(args.case)
