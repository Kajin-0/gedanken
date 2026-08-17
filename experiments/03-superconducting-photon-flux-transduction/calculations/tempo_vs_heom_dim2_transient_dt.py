#!/usr/bin/env python3
"""Full-history TEMPO-vs-HEOM timestep refinement for the dim=2 mapping test.

The first dt=.2, tcut=tend=4 comparison found a maximum half trace-distance
4.022613e-4.  Because H and the bath coupling do not commute, unlike the
analytic pure-dephasing audits, this can be a finite-time-step/Trotter error.

This script holds the physical finite system, full bath history, Padé order,
HEOM depth and tensor tolerance fixed while refining only TEMPO/HEOM output
step:

    dt=.20, .10, .05;  tcut=tend=4; epsrel=1e-10.

No bath-memory term inside the trajectory is discarded.  A systematic decrease
with timestep supports a discretization interpretation; a plateau supports a
mapping/convention failure.  This is a finite-system mapping audit only.
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

DIM=2; NPADE=4; DEPTH=9; TEND=4.; TCUT=4.; EPS=1e-10
CASES={'d200':.20,'d100':.10,'d050':.05}

def half(a,b): return .5*float(np.sum(svdvals(a-b)))
def corr_factory(d,z):
    d=np.asarray(d,complex); z=np.asarray(z,complex)
    def corr(tau):
        a=np.asarray(tau); aa=np.abs(a); cp=np.zeros_like(aa,dtype=complex)
        for dk,zk in zip(d,z): cp += dk*np.exp(-zk*aa)
        return np.where(a>=0,cp,np.conj(cp))
    return corr

def main(name):
    dt=CASES[name]
    wc,xop,_u,H,d,z,_=fp.harmonic_setup(DIM,NPADE)
    rho0=basis(DIM,0)*basis(DIM,0).dag(); times=np.arange(0,TEND+.5*dt,dt)
    cr,vr,ci,vi=base.pade_bath_expansion(wc,NPADE)
    hs=HEOMSolver(H,BosonicBath(xop,cr,vr,ci,vi,combine=True,tag=f'dt-{name}'),
        max_depth=DEPTH,options={'progress_bar':'','method':'bdf','rtol':2e-11,
                                 'atol':2e-13,'nsteps':300000})
    hres=hs.run(rho0,times); hr=[np.asarray(q.full(),complex) for q in hres.states]
    system=oqupy.System(np.asarray(H.full(),complex))
    tbath=oqupy.Bath(np.asarray(xop.full(),complex),
        oqupy.CustomCorrelations(correlation_function=corr_factory(d,z)))
    dyn=oqupy.tempo_compute(system=system,bath=tbath,
        initial_state=np.asarray(rho0.full(),complex),start_time=0,end_time=TEND,
        parameters=oqupy.TempoParameters(dt=dt,tcut=TCUT,epsrel=EPS),
        unique=True,progress_type='silent')
    tr=np.asarray(dyn.states,complex); tt=np.asarray(dyn.times,float)
    if len(tt)!=len(times) or np.max(np.abs(tt-times))>1e-9: raise RuntimeError('grid mismatch')
    ds=[]; te=[]; ah=[]
    for t,a,b in zip(times,tr,hr):
        ds.append(half(a,b)); te.append(abs(np.trace(a)-1));
        ah.append(np.linalg.norm(a-a.conj().T,ord='fro')/max(np.linalg.norm(a,ord='fro'),1e-300))
    im=int(np.argmax(ds))
    msg=(f"TEMPO_TRANSIENT_DT case={name} dt={dt:.3f} maxhalf={max(ds):.12e} "
         f"at_tau={times[im]:.6f} finalhalf={ds[-1]:.12e} "
         f"maxtrace={max(te):.3e} maxanti={max(ah):.3e}")
    print(msg,flush=True)
    for ttgt in (1.,2.,3.,4.):
        j=int(np.argmin(np.abs(times-ttgt)))
        print(f"POINT tau={times[j]:.3f} half={ds[j]:.12e} tempo_pop1={tr[j,1,1].real:.12e} "
              f"heom_pop1={hr[j][1,1].real:.12e}",flush=True)
    print(f"::notice title=Experiment 03 TEMPO transient dt refinement::{msg}",flush=True)
    if max(te)>1e-7 or max(ah)>1e-7: raise RuntimeError('trace/Hermiticity failure')

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--case',choices=sorted(CASES),required=True)
    args=ap.parse_args(); main(args.case)
