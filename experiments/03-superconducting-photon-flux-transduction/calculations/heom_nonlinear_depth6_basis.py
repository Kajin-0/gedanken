#!/usr/bin/env python3
"""Depth-six system-basis matrix for nonlinear left-well HEOM Gate C.1.

The preceding diagnostics established that dim=9 and dim=10 develop growing
nonphysical modes at hierarchy depth <=5, and that the dim=10 depth-5 trajectory
is unchanged by a hard BDF max_step cap.  This script changes only hierarchy
depth to 6 and compares dim=8,9,10 under the same physical model and tolerances.

This remains a calibration/convergence calculation, not a Gate-C acceptance run.
"""
from __future__ import annotations

import argparse
import math
import time
import numpy as np

from qutip.solver.heom import BosonicBath, HEOMSolver

import heom_nonlinear_leftwell_pilot as pilot
import heom_harmonic_pade_depth as bathbase

CASES={
    "dim8_p4d6":8,
    "dim9_p4d6":9,
    "dim10_p4d6":10,
}


def run_case(name):
    dim=CASES[name]
    cfg=dict(xmin=-3.8,ngrid=2200,dim=dim,npade=4,depth=6)
    (_model,xm,xs,wc,e,yop,y2op,h0,hsys,rho0,residuals)=pilot.nonlinear_system(cfg)
    cr,vr,ci,vi=bathbase.pade_bath_expansion(wc,4)
    bath=BosonicBath(yop,cr,vr,ci,vi,combine=True,tag="direct-port-pade-nonlinear")
    nexp=len(bath.exponents); depth=6
    nado=math.comb(nexp+depth,depth)
    print(f"CASE={name} dim={dim} Npade=4 depth=6 nexp={nexp} nado_est={nado}",flush=True)
    print(f"xm={xm:+.10f} xs={xs:+.10f} wc/2pi={wc/(2*math.pi)*1e-9:.9f}GHz "
          f"max_DVR_residual_K={float(np.max(residuals)):.3e}",flush=True)
    print("transitions_K="+",".join(f"{q:.9e}" for q in (e-e[0])/pilot.KB),flush=True)

    solver=HEOMSolver(
        hsys,bath,max_depth=depth,
        options={
            "progress_bar":"",
            "store_states":True,
            "method":"bdf",
            "rtol":2e-7,
            "atol":2e-9,
            "nsteps":500000,
        },
    )
    tlist=np.array([0.,10.,20.,40.,80.,120.,160.])
    t0=time.perf_counter()
    result=solver.run(rho0,tlist,e_ops=[yop,y2op,h0])
    runtime=time.perf_counter()-t0
    rows=[]
    for i,tau in enumerate(tlist):
        m=pilot.state_metrics(result.states[i],yop,y2op,h0,rho0); rows.append(m)
        maxabs=float(np.max(np.abs(np.asarray(result.states[i].full(),dtype=complex))))
        print(f"tau={tau:7.1f} trace=({m['trace'].real:+.10e}{m['trace'].imag:+.2e}j) "
              f"mean_y={m['mean']:+.10e} sigma_y={m['sigma']:.10e} E0={m['energy']:+.10e} "
              f"eigmin={m['eigmin']:+.9e} negmass={m['neg']:.9e} "
              f"topPop={m['top']:+.9e} maxabsrho={maxabs:.9e}",flush=True)
    f,p=rows[-1],rows[-2]
    late=max(abs(f["mean"]-p["mean"]),abs(f["sigma"]-p["sigma"]),abs(f["energy"]-p["energy"]))
    msg=(f"CASE={name} FINAL trace=({f['trace'].real:.12e}{f['trace'].imag:+.2e}j) "
         f"antiherm={f['anti']:.3e} eigmin={f['eigmin']:+.9e} negmass={f['neg']:.9e} "
         f"mean_y={f['mean']:+.10e} sigma_y={f['sigma']:.10e} E0={f['energy']:+.10e} "
         f"topPop={f['top']:+.9e} bareGibbs_nuclear_half={f['gibbs_half']:.9e} "
         f"late_abs_drift={late:.9e} runtime_s={runtime:.3f}")
    print(msg,flush=True)
    print(f"::notice title=Experiment 03 nonlinear HEOM depth6 basis::{msg}",flush=True)


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--case",choices=sorted(CASES),required=True)
    args=ap.parse_args(); run_case(args.case)
