#!/usr/bin/env python3
"""Tensor-tolerance refinement at fixed full-history TEMPO timestep.

The dim=2 full-history transient mapping has demonstrated essentially exact
second-order timestep convergence:

    max half-distance TEMPO vs HEOM
      dt=.20 -> 4.022613e-4
      dt=.10 -> 1.004917e-4
      dt=.05 -> 2.510405e-5.

At dt=.05 with epsrel=1e-10, however, the accumulated anti-Hermitian norm rose
to 2.23e-7 over 80 steps.  This script holds dt=.05, tcut=tend=4 and all
physics fixed, tightening only the OQuPy tensor SVD tolerance to 1e-11 and
1e-12.  The purpose is to verify that the physicality defect is numerical and
separable from the already-convergent timestep mapping.
"""
from __future__ import annotations

import argparse
import numpy as np
if not hasattr(np,'trapezoid'):
    np.trapezoid=np.trapz
from scipy.linalg import svdvals
import oqupy
from qutip import basis
from qutip.solver.heom import HEOMSolver, BosonicBath
import heom_fp_harmonic_oracle as fp
import heom_harmonic_pade_depth as base

DIM=2; NPADE=4; DEPTH=9; DT=.05; TEND=4.; TCUT=4.
CASES={'e11':1e-11,'e12':1e-12}

def half(a,b): return .5*float(np.sum(svdvals(a-b)))
def corr_factory(d,z):
    d=np.asarray(d,complex); z=np.asarray(z,complex)
    def corr(tau):
        a=np.asarray(tau); aa=np.abs(a); cp=np.zeros_like(aa,dtype=complex)
        for dk,zk in zip(d,z): cp += dk*np.exp(-zk*aa)
        return np.where(a>=0,cp,np.conj(cp))
    return corr

def main(name):
    eps=CASES[name]
    wc,xop,_u,H,d,z,_=fp.harmonic_setup(DIM,NPADE)
    rho0=basis(DIM,0)*basis(DIM,0).dag(); times=np.arange(0,TEND+.5*DT,DT)
    cr,vr,ci,vi=base.pade_bath_expansion(wc,NPADE)
    hs=HEOMSolver(H,BosonicBath(xop,cr,vr,ci,vi,combine=True,tag=f'eps-{name}'),
        max_depth=DEPTH,options={'progress_bar':'','method':'bdf','rtol':2e-11,'atol':2e-13,'nsteps':300000})
    hr=[np.asarray(q.full(),complex) for q in hs.run(rho0,times).states]
    system=oqupy.System(np.asarray(H.full(),complex))
    tbath=oqupy.Bath(np.asarray(xop.full(),complex),oqupy.CustomCorrelations(correlation_function=corr_factory(d,z)))
    dyn=oqupy.tempo_compute(system=system,bath=tbath,initial_state=np.asarray(rho0.full(),complex),
        start_time=0,end_time=TEND,parameters=oqupy.TempoParameters(dt=DT,tcut=TCUT,epsrel=eps),
        unique=True,progress_type='silent')
    tr=np.asarray(dyn.states,complex); tt=np.asarray(dyn.times,float)
    if len(tt)!=len(times) or np.max(np.abs(tt-times))>1e-9: raise RuntimeError('grid mismatch')
    ds=[]; te=[]; ah=[]
    for a,b in zip(tr,hr):
        ds.append(half(a,b)); te.append(abs(np.trace(a)-1));
        ah.append(np.linalg.norm(a-a.conj().T,ord='fro')/max(np.linalg.norm(a,ord='fro'),1e-300))
    im=int(np.argmax(ds))
    msg=(f"TEMPO_TRANSIENT_EPS case={name} eps={eps:.1e} maxhalf={max(ds):.12e} "
         f"at_tau={times[im]:.3f} finalhalf={ds[-1]:.12e} maxtrace={max(te):.3e} maxanti={max(ah):.3e}")
    print(msg,flush=True); print(f"::notice title=Experiment 03 TEMPO tensor tolerance::{msg}",flush=True)
    if max(te)>1e-8 or max(ah)>1e-8: raise RuntimeError('tightened TEMPO still violates numerical physicality guard')
    print('PASS_FINE_TEMPO_TENSOR_PHYSICALITY')
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--case',choices=sorted(CASES),required=True)
    args=ap.parse_args(); main(args.case)
