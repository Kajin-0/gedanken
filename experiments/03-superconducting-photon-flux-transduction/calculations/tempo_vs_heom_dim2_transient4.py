#!/usr/bin/env python3
"""Short full-history TEMPO-vs-HEOM transient mapping audit to tau=4.

Same finite dim=2 direct-port problem and dt=.2, epsrel=1e-10 as the longer
transient audit, but tcut=tend=4.  No influence term inside the simulated
interval is discarded.  This is an early mapping discriminator only.
"""
from __future__ import annotations

import numpy as np
if not hasattr(np,'trapezoid'):
    np.trapezoid=np.trapz
from scipy.linalg import svdvals
import oqupy
from qutip import basis
from qutip.solver.heom import HEOMSolver, BosonicBath

import heom_fp_harmonic_oracle as fp
import heom_harmonic_pade_depth as base

DIM=2; NPADE=4; DEPTH=9; DT=.2; TEND=4.; TCUT=4.; EPS=1e-10

def half(a,b): return .5*float(np.sum(svdvals(a-b)))
def corr_factory(d,z):
    d=np.asarray(d,complex); z=np.asarray(z,complex)
    def corr(tau):
        a=np.asarray(tau); aa=np.abs(a); cp=np.zeros_like(aa,dtype=complex)
        for dk,zk in zip(d,z): cp += dk*np.exp(-zk*aa)
        return np.where(a>=0,cp,np.conj(cp))
    return corr

def main():
    wc,xop,_u,H,d,z,_=fp.harmonic_setup(DIM,NPADE)
    rho0=basis(DIM,0)*basis(DIM,0).dag(); times=np.arange(0,TEND+.5*DT,DT)
    cr,vr,ci,vi=base.pade_bath_expansion(wc,NPADE)
    hs=HEOMSolver(H,BosonicBath(xop,cr,vr,ci,vi,combine=True,tag='short-map'),
        max_depth=DEPTH,options={'progress_bar':'','method':'bdf','rtol':2e-10,
                                 'atol':2e-12,'nsteps':200000})
    hres=hs.run(rho0,times); hr=[np.asarray(q.full(),complex) for q in hres.states]
    system=oqupy.System(np.asarray(H.full(),complex))
    tbath=oqupy.Bath(np.asarray(xop.full(),complex),
        oqupy.CustomCorrelations(correlation_function=corr_factory(d,z)))
    dyn=oqupy.tempo_compute(system=system,bath=tbath,
        initial_state=np.asarray(rho0.full(),complex),start_time=0,end_time=TEND,
        parameters=oqupy.TempoParameters(dt=DT,tcut=TCUT,epsrel=EPS),
        unique=True,progress_type='silent')
    tr=np.asarray(dyn.states,complex); tt=np.asarray(dyn.times,float)
    if len(tt)!=len(times) or np.max(np.abs(tt-times))>1e-10: raise RuntimeError('grid mismatch')
    ds=[]; te=[]; ah=[]
    for j,(t,a,b) in enumerate(zip(times,tr,hr)):
        ds.append(half(a,b)); te.append(abs(np.trace(a)-1));
        ah.append(np.linalg.norm(a-a.conj().T,ord='fro')/max(np.linalg.norm(a,ord='fro'),1e-300))
        if j%5==0 or j==len(times)-1:
            print(f"POINT tau={t:.3f} half={ds[-1]:.12e} tempo_pop1={a[1,1].real:.12e} "
                  f"heom_pop1={b[1,1].real:.12e} traceerr={te[-1]:.3e} anti={ah[-1]:.3e}",flush=True)
    im=int(np.argmax(ds)); msg=(f"TEMPO_HEOM_TRANSIENT4 maxhalf={max(ds):.6e} at_tau={times[im]:.3f} "
        f"finalhalf={ds[-1]:.6e} maxtrace={max(te):.3e} maxanti={max(ah):.3e}")
    print(msg,flush=True); print(f"::notice title=Experiment 03 short TEMPO-HEOM mapping::{msg}",flush=True)
    if max(te)>1e-7 or max(ah)>1e-7: raise RuntimeError('trace/Hermiticity failure')
    if max(ds)>2e-4: raise RuntimeError('short full-history transients disagree')
    print('PASS_TEMPO_HEOM_TRANSIENT4_MAPPING')
if __name__=='__main__': main()
