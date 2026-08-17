#!/usr/bin/env python3
"""PT-TEMPO timestep-convergence audit on the analytic pure-dephasing oracle.

The first reusable-process-tensor audit at dt=.1 gave a reproducible
2.6912e-5 coherence error for two different initial states while preserving
trace/Hermiticity to ~1e-9/~1e-12.  Direct TEMPO on the same oracle is accurate
to ~1e-13, so this script determines whether the PT-TEMPO discrepancy is the
expected finite-time-step/process-tensor discretization error.

Cases dt=.1,.05,.025 keep the full memory window tcut=tend=5 and epsrel=1e-10.
A coherent decreasing analytic error is required.  This is an implementation
convergence audit only; it does not modify any Experiment-03 physics.
"""
from __future__ import annotations

import argparse
import math
import numpy as np
import oqupy

D=.2; GAMMA=1.0; TEND=5.0; EPS=1e-10
CASES={'dt100':.1,'dt050':.05,'dt025':.025}


def corr(tau):
    a=np.asarray(tau); return D*np.exp(-GAMMA*np.abs(a))

def factor(t): return math.exp(-D*(t-1.0+math.exp(-t)))

def main(name):
    dt=CASES[name]
    q=np.diag([0.,1.]).astype(complex)
    system=oqupy.System(np.zeros((2,2),complex))
    bath=oqupy.Bath(q,oqupy.CustomCorrelations(correlation_function=corr))
    pars=oqupy.TempoParameters(dt=dt,tcut=TEND,epsrel=EPS)
    pt=oqupy.pt_tempo_compute(bath=bath,start_time=0.,end_time=TEND,
                              parameters=pars,unique=True,progress_type='silent')
    rho0=np.array([[.5,.5],[.5,.5]],complex)
    dyn=oqupy.compute_dynamics(system=system,initial_state=rho0,
                               process_tensor=pt,start_time=0.,progress_type='silent')
    times=np.asarray(dyn.times,float); states=np.asarray(dyn.states,complex)
    errs=[]; tr=[]; herm=[]
    for t,rho in zip(times,states):
        ex=.5*factor(float(t)); errs.append(abs(rho[0,1]-ex)/abs(ex))
        tr.append(abs(np.trace(rho)-1.)); herm.append(np.linalg.norm(rho-rho.conj().T,ord='fro'))
    msg=(f"PT_DT case={name} dt={dt:.6f} steps={len(times)-1} maxrel={max(errs):.12e} "
         f"finalrel={errs[-1]:.12e} maxtrace={max(tr):.12e} maxherm={max(herm):.12e}")
    print(msg,flush=True); print(f"::notice title=Experiment 03 PT-TEMPO dt convergence::{msg}",flush=True)
    if max(tr)>1e-7 or max(herm)>1e-9:
        raise RuntimeError('PT-TEMPO lost trace/Hermiticity in timestep audit')

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--case',choices=sorted(CASES),required=True)
    args=ap.parse_args(); main(args.case)
