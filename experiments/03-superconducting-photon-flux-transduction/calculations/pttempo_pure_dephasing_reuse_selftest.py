#!/usr/bin/env python3
"""PT-TEMPO process-tensor reuse audit for Experiment 03.

This validates the specific OQuPy path intended for the final harmonic and
nonlinear convergence program: build one bath process tensor, then reuse it for
multiple system initial states.

The bath is the analytically soluble real-exponential pure-dephasing oracle

    C(t)=d exp(-Gamma |t|), d=.2, Gamma=1,
    H=0, q=diag(0,1).

For an arbitrary initial coherence rho01(0),

    rho01(t)=rho01(0) exp[-d (t - 1 + exp(-t))].

One process tensor is contracted against two materially different initial
states.  This is an implementation/reuse audit only, not a detector result.
"""
from __future__ import annotations

import math
import numpy as np
import oqupy

D=.2
GAMMA=1.0
DT=.10
TCUT=5.0
TEND=5.0
EPS=1e-10


def corr(tau):
    a=np.asarray(tau)
    return D*np.exp(-GAMMA*np.abs(a))


def factor(t):
    return math.exp(-D*(t-1.0+math.exp(-t)))


def check(name,rho0,pt,system):
    dyn=oqupy.compute_dynamics(system=system,initial_state=rho0,
                               process_tensor=pt,start_time=0.0,
                               progress_type='silent')
    times=np.asarray(dyn.times,float); states=np.asarray(dyn.states,complex)
    errs=[]; tr=[]; herm=[]
    for t,rho in zip(times,states):
        exact=rho0[0,1]*factor(float(t))
        den=max(abs(exact),1e-14)
        errs.append(abs(rho[0,1]-exact)/den)
        tr.append(abs(np.trace(rho)-1.0))
        herm.append(np.linalg.norm(rho-rho.conj().T,ord='fro'))
    print(f"PT_REUSE state={name} maxrel={max(errs):.12e} finalrel={errs[-1]:.12e} "
          f"maxtrace={max(tr):.12e} maxherm={max(herm):.12e}",flush=True)
    return max(errs),max(tr),max(herm),states[-1]


def main():
    q=np.diag([0.0,1.0]).astype(complex)
    system=oqupy.System(np.zeros((2,2),complex))
    bath=oqupy.Bath(q,oqupy.CustomCorrelations(correlation_function=corr))
    pars=oqupy.TempoParameters(dt=DT,tcut=TCUT,epsrel=EPS)
    print(f"PT_BUILD dt={DT} tcut={TCUT} tend={TEND} eps={EPS:.1e}",flush=True)
    pt=oqupy.pt_tempo_compute(bath=bath,start_time=0.0,end_time=TEND,
                              parameters=pars,unique=True,
                              progress_type='silent')
    rho_a=np.array([[.5,.5],[.5,.5]],complex)
    rho_b=np.array([[.75,.20+.10j],[.20-.10j,.25]],complex)
    # rho_b is positive: eigenvalues ~.8385,.1615.
    ra=check('A',rho_a,pt,system)
    rb=check('B',rho_b,pt,system)
    worst=max(ra[0],rb[0]); tr=max(ra[1],rb[1]); herm=max(ra[2],rb[2])
    print(f"PT_TEMPO_REUSE worst_rel={worst:.12e} maxtrace={tr:.12e} maxherm={herm:.12e}",flush=True)
    print(f"::notice title=Experiment 03 PT-TEMPO reuse self-test::worst={worst:.3e} trace={tr:.3e} herm={herm:.3e}")
    if worst>3e-8 or tr>1e-10 or herm>1e-10:
        raise RuntimeError('PT-TEMPO reuse audit failed')
    print('PASS_PT_TEMPO_REUSE_AUDIT')

if __name__=='__main__': main()
