#!/usr/bin/env python3
"""Direct transient mapping audit: TEMPO vs conventional HEOM for dim=2.

This is a stronger mapping test than comparing TEMPO to an asymptotic HEOM
stationary state.  Both solvers start from the same factorized initial condition:

    rho_S(0)=|0><0|,
    bath initially in its equilibrium reference state,
    all HEOM auxiliary density operators initially zero.

The direct TEMPO run uses

    dt=.2, tcut=8, tend=8, epsrel=1e-10.

Because tcut equals the entire simulated interval, no bath-history term inside
0<=tau<=8 is discarded by TEMPO.  Conventional p4/depth9 HEOM is already
converged for this tiny finite system.  State-by-state agreement over the whole
trajectory therefore tests the actual direct-port correlation, counterterm,
coupling normalization and dimensionless-time mapping independently of late
finite-memory stationary bias.

This is a finite dim=2 mapping audit only, not a Gate-B/C acceptance result.
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

DIM=2
NPADE=4
DEPTH=9
DT=.2
TEND=8.0
TCUT=8.0
EPS=1e-10


def half(a,b):
    return .5*float(np.sum(svdvals(a-b)))


def corr_factory(d,z):
    d=np.asarray(d,complex); z=np.asarray(z,complex)
    def corr(tau):
        a=np.asarray(tau); aa=np.abs(a)
        cp=np.zeros_like(aa,dtype=complex)
        for dk,zk in zip(d,z):
            cp += dk*np.exp(-zk*aa)
        return np.where(a>=0,cp,np.conj(cp))
    return corr


def main():
    wc,xop,_uop,H,d,z,_eref=fp.harmonic_setup(DIM,NPADE)
    rho0=basis(DIM,0)*basis(DIM,0).dag()
    times=np.arange(0.0,TEND+0.5*DT,DT)

    # Conventional HEOM transient from factorized initial condition.
    cr,vr,ci,vi=base.pade_bath_expansion(wc,NPADE)
    hbath=BosonicBath(xop,cr,vr,ci,vi,combine=True,tag='dim2-transient-map')
    hs=HEOMSolver(H,hbath,max_depth=DEPTH,options={
        'progress_bar':'', 'method':'bdf', 'rtol':2e-10, 'atol':2e-12,
        'nsteps':200000,
    })
    hres=hs.run(rho0,times)
    hrhos=[np.asarray(q.full(),complex) for q in hres.states]

    # Direct TEMPO with full history over the same interval.
    system=oqupy.System(np.asarray(H.full(),complex))
    tbath=oqupy.Bath(np.asarray(xop.full(),complex),
        oqupy.CustomCorrelations(correlation_function=corr_factory(d,z)))
    pars=oqupy.TempoParameters(dt=DT,tcut=TCUT,epsrel=EPS)
    dyn=oqupy.tempo_compute(system=system,bath=tbath,
        initial_state=np.asarray(rho0.full(),complex),start_time=0.0,
        end_time=TEND,parameters=pars,unique=True,progress_type='silent')
    ttempo=np.asarray(dyn.times,float); trhos=np.asarray(dyn.states,complex)
    if len(ttempo)!=len(times) or np.max(np.abs(ttempo-times))>1e-10:
        raise RuntimeError('TEMPO and HEOM output grids do not match')

    distances=[]; trerr=[]; anti=[]
    for j,(t,rh,rt) in enumerate(zip(times,hrhos,trhos)):
        dhalf=half(rt,rh); distances.append(dhalf)
        trerr.append(abs(np.trace(rt)-1))
        anti.append(np.linalg.norm(rt-rt.conj().T,ord='fro')/
                    max(np.linalg.norm(rt,ord='fro'),1e-300))
        if j%5==0 or j==len(times)-1:
            print(f"POINT tau={t:.6f} half={dhalf:.12e} "
                  f"tempo_pop1={rt[1,1].real:.12e} heom_pop1={rh[1,1].real:.12e} "
                  f"traceerr={trerr[-1]:.3e} anti={anti[-1]:.3e}",flush=True)

    imax=int(np.argmax(distances))
    msg=(f"TEMPO_HEOM_TRANSIENT maxhalf={max(distances):.6e} at_tau={times[imax]:.3f} "
         f"finalhalf={distances[-1]:.6e} maxtrace={max(trerr):.3e} maxanti={max(anti):.3e}")
    print(msg,flush=True)
    print(f"::notice title=Experiment 03 TEMPO-HEOM transient mapping::{msg}",flush=True)

    # Mapping audit threshold is deliberately much tighter than the previous
    # stationary gross-disagreement guard but still not a Gate-B/C threshold.
    if max(trerr)>1e-7 or max(anti)>1e-7:
        raise RuntimeError('TEMPO transient lost trace/Hermiticity')
    if max(distances)>2e-4:
        raise RuntimeError('TEMPO and HEOM full-history transients disagree')
    print('PASS_TEMPO_HEOM_TRANSIENT_MAPPING')

if __name__=='__main__': main()
