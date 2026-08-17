#!/usr/bin/env python3
"""Refine the direct-port TEMPO-vs-HEOM dim=2 mapping diagnostic.

The first dim=2 mapping trajectory moved monotonically toward the HEOM steady
state but at epsrel=1e-8 retained ~1e-6 trace/Hermiticity errors and had not
fully equilibrated by tau=32.  This script separates three axes without changing
the physical finite system:

  tol32 : dt=.2, tcut=8,  tend=32, epsrel=1e-10
  long64: dt=.2, tcut=8,  tend=64, epsrel=1e-10
  mem64 : dt=.2, tcut=12, tend=64, epsrel=1e-10

The conventional p4 depth-6 HEOM stationary state is recomputed independently
inside every job.  These are mapping diagnostics only, not Gate-B/C tests.
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

CASES={
    'tol32':  dict(dt=.2,tcut=8.0,tend=32.0,eps=1e-10),
    'long64':dict(dt=.2,tcut=8.0,tend=64.0,eps=1e-10),
    'mem64': dict(dt=.2,tcut=12.0,tend=64.0,eps=1e-10),
}
DIM=2; NPADE=4; HEOM_DEPTH=6


def half(a,b): return .5*float(np.sum(svdvals(a-b)))

def corr_factory(d,z):
    d=np.asarray(d,complex); z=np.asarray(z,complex)
    def corr(tau):
        a=np.asarray(tau); aa=np.abs(a)
        cp=np.zeros_like(aa,dtype=complex)
        for dk,zk in zip(d,z): cp += dk*np.exp(-zk*aa)
        return np.where(a>=0,cp,np.conj(cp))
    return corr


def heom_reference(wc,xop,H):
    cr,vr,ci,vi=base.pade_bath_expansion(wc,NPADE)
    bath=BosonicBath(xop,cr,vr,ci,vi,combine=True,tag='dim2-refine')
    sol=HEOMSolver(H,bath,max_depth=HEOM_DEPTH,options={'progress_bar':''})
    L=schur.scipy_rhs(sol)
    v,ss,res,resrel,warn=steady.constrained_nullvector(L,DIM)
    rho=v[:DIM*DIM].reshape((DIM,DIM),order='F')
    rho=.5*(rho+rho.conj().T); rho/=np.trace(rho)
    return rho,res,len(sol.ados.labels),ss


def main(name):
    cfg=CASES[name]
    wc,xop,uop,H,d,z,eref=fp.harmonic_setup(DIM,NPADE)
    rhoh,res,nado,ss=heom_reference(wc,xop,H)
    print(f"CASE={name} dt={cfg['dt']} tcut={cfg['tcut']} tend={cfg['tend']} eps={cfg['eps']:.1e} "
          f"HEOM_nado={nado} HEOM_res={res:.3e} HEOM_solve={ss:.3f}",flush=True)
    print(f"HEOM pop1={rhoh[1,1].real:.12e} eigmin={np.linalg.eigvalsh(rhoh).min():+.12e}",flush=True)
    system=oqupy.System(np.asarray(H.full(),complex))
    bath=oqupy.Bath(np.asarray(xop.full(),complex),
                    oqupy.CustomCorrelations(correlation_function=corr_factory(d,z)))
    rho0=np.asarray((basis(DIM,0)*basis(DIM,0).dag()).full(),complex)
    pars=oqupy.TempoParameters(dt=cfg['dt'],tcut=cfg['tcut'],epsrel=cfg['eps'])
    dyn=oqupy.tempo_compute(system=system,bath=bath,initial_state=rho0,
                            start_time=0.0,end_time=cfg['tend'],parameters=pars,
                            unique=True,progress_type='silent')
    t=np.asarray(dyn.times,float); states=np.asarray(dyn.states,complex)
    for frac in (.25,.5,.75,1.0):
        target=frac*cfg['tend']; j=int(np.argmin(np.abs(t-target)))
        rho=states[j]
        ev=np.linalg.eigvalsh(.5*(rho+rho.conj().T))
        anti=np.linalg.norm(rho-rho.conj().T,ord='fro')/max(np.linalg.norm(rho,ord='fro'),1e-300)
        print(f"SAMPLE tau={t[j]:.6f} half={half(rho,rhoh):.12e} "
              f"traceerr={abs(np.trace(rho)-1):.12e} anti={anti:.12e} eigmin={ev.min():+.12e}",flush=True)
    rf=states[-1]; jl=int(np.argmin(np.abs(t-.75*cfg['tend']))); rl=states[jl]
    h=half(rf,rhoh); drift=half(rf,rl)
    anti=np.linalg.norm(rf-rf.conj().T,ord='fro')/max(np.linalg.norm(rf,ord='fro'),1e-300)
    trerr=abs(np.trace(rf)-1); ev=np.linalg.eigvalsh(.5*(rf+rf.conj().T))
    msg=(f"TEMPO_DIM2_REFINE case={name} half={h:.6e} late_half={drift:.6e} "
         f"traceerr={trerr:.3e} anti={anti:.3e} eigmin={ev.min():.6e}")
    print(msg,flush=True); print(f"::notice title=Experiment 03 TEMPO dim2 refinement::{msg}",flush=True)
    if res>1e-9: raise RuntimeError('HEOM reference residual too large')
    if trerr>1e-8 or anti>1e-8: raise RuntimeError('TEMPO trace/Hermiticity still outside mapping guard')
    if h>2e-2: raise RuntimeError('TEMPO/HEOM finite-system mapping grossly disagrees')
    print('PASS_TEMPO_DIM2_REFINED_MAPPING_SANITY')

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--case',choices=sorted(CASES),required=True)
    args=ap.parse_args(); main(args.case)
