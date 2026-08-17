#!/usr/bin/env python3
"""Combined long-memory + timestep convergence for direct TEMPO at dim=2.

The direct-TEMPO mapping has separately established:

* full-history state error ~ O(dt^2) against depth-converged HEOM;
* tensor physicality at dt=.05 can be controlled with epsrel=1e-12;
* tcut=8 reaches a biased stationary state ~1.531e-3 from HEOM;
* increasing memory alone materially reduces that bias;
* the exact signed integrated bath tail at tcut=20 is 3.41e-6.

This script combines the axes for the first time at tcut=20, tend=64,
epsrel=1e-12, comparing dt=.2 and .1.  The physical finite system, p4 bath,
counterterm and independently converged HEOM stationary reference are unchanged.

The pair is a convergence discriminator, not the final harmonic TEMPO gate.
If the long-memory dt sequence remains coherent and approximately second order,
a dt=.05 long-memory case is then justified.  No nonlinear use is authorized by
this calculation.
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
import heom_schur_terminator_harmonic_probe as schur
import heom_harmonic_steady_nullspace_probe as steady

DIM=2; NPADE=4; HEOM_DEPTH=9; TCUT=20.; TEND=64.; EPS=1e-12
CASES={'d200':.2,'d100':.1}

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
    wc,xop,_u,H,d,z,_eref=fp.harmonic_setup(DIM,NPADE)
    # Independently recompute the canonical p4/depth9 finite-system stationary reference.
    cr,vr,ci,vi=base.pade_bath_expansion(wc,NPADE)
    hbath=BosonicBath(xop,cr,vr,ci,vi,combine=True,tag=f'combined-{name}')
    hs=HEOMSolver(H,hbath,max_depth=HEOM_DEPTH,options={'progress_bar':''})
    L=schur.scipy_rhs(hs)
    v,ss,res,_rr,_w=steady.constrained_nullvector(L,DIM)
    rhoh=v[:4].reshape((2,2),order='F'); rhoh=.5*(rhoh+rhoh.conj().T); rhoh/=np.trace(rhoh)
    print(f"CASE={name} dt={dt} tcut={TCUT} tend={TEND} eps={EPS:.1e} "
          f"HEOM_pop1={rhoh[1,1].real:.15e} HEOM_res={res:.3e}",flush=True)

    system=oqupy.System(np.asarray(H.full(),complex))
    tbath=oqupy.Bath(np.asarray(xop.full(),complex),
        oqupy.CustomCorrelations(correlation_function=corr_factory(d,z)))
    rho0=np.asarray((basis(DIM,0)*basis(DIM,0).dag()).full(),complex)
    pars=oqupy.TempoParameters(dt=dt,tcut=TCUT,epsrel=EPS)
    dyn=oqupy.tempo_compute(system=system,bath=tbath,initial_state=rho0,
        start_time=0.,end_time=TEND,parameters=pars,unique=True,progress_type='silent')
    t=np.asarray(dyn.times,float); states=np.asarray(dyn.states,complex)
    for target in (8.,16.,24.,32.,48.,64.):
        j=int(np.argmin(np.abs(t-target))); rho=states[j]
        ev=np.linalg.eigvalsh(.5*(rho+rho.conj().T))
        anti=np.linalg.norm(rho-rho.conj().T,ord='fro')/max(np.linalg.norm(rho,ord='fro'),1e-300)
        print(f"SAMPLE tau={t[j]:.6f} half={half(rho,rhoh):.12e} "
              f"pop1={rho[1,1].real:.12e} traceerr={abs(np.trace(rho)-1):.3e} "
              f"anti={anti:.3e} eigmin={ev.min():+.12e}",flush=True)
    rf=states[-1]
    j48=int(np.argmin(np.abs(t-48.))); r48=states[j48]
    j32=int(np.argmin(np.abs(t-32.))); r32=states[j32]
    h=half(rf,rhoh); late48=half(rf,r48); late32=half(rf,r32)
    anti=np.linalg.norm(rf-rf.conj().T,ord='fro')/max(np.linalg.norm(rf,ord='fro'),1e-300)
    trerr=abs(np.trace(rf)-1); ev=np.linalg.eigvalsh(.5*(rf+rf.conj().T))
    msg=(f"TEMPO_DIM2_COMBINED case={name} dt={dt:.3f} half={h:.12e} "
         f"late48={late48:.12e} late32={late32:.12e} traceerr={trerr:.3e} "
         f"anti={anti:.3e} eigmin={ev.min():+.12e}")
    print(msg,flush=True); print(f"::notice title=Experiment 03 TEMPO combined dim2::{msg}",flush=True)
    if res>1e-9: raise RuntimeError('HEOM reference residual too large')
    if trerr>1e-8 or anti>1e-8: raise RuntimeError('combined TEMPO numerical physicality guard failed')
    if h>2e-3: raise RuntimeError('combined long-memory state grossly disagrees with HEOM')
    print('PASS_TEMPO_DIM2_COMBINED_SANITY')

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--case',choices=sorted(CASES),required=True)
    args=ap.parse_args(); main(args.case)
