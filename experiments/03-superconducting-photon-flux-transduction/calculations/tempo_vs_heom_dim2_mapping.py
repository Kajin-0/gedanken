#!/usr/bin/env python3
"""Direct-port mapping cross-check: TEMPO vs conventional HEOM at dim=2.

This is not a physical continuum-oracle calculation.  It deliberately fixes a
tiny two-level truncation of the harmonic system so that the same finite-system
open-bath problem can be solved cheaply by two independent methods:

1. conventional Padé HEOM stationary nullspace, depth 6;
2. OQuPy TEMPO relaxation from a factorized system-bath state.

Agreement of their late reduced states tests the actual direct-port correlation,
counterterm, coupling and dimensionless-unit mapping independently of the
continuum Gaussian FDT reference.  No Gate C.1 claim may be based on dim=2.
"""
from __future__ import annotations

import math
import numpy as np
if not hasattr(np, 'trapezoid'):
    np.trapezoid = np.trapz

from scipy.linalg import svdvals
import oqupy
from qutip import basis
from qutip.solver.heom import HEOMSolver, BosonicBath

import heom_fp_harmonic_oracle as fp
import heom_harmonic_pade_depth as base
import heom_schur_terminator_harmonic_probe as schur
import heom_harmonic_steady_nullspace_probe as steady

DIM=2
NPADE=4
HEOM_DEPTH=6
DT=0.20
TCUT=8.0
TEND=32.0
EPSREL=1e-8


def half_distance(a,b):
    return 0.5*float(np.sum(svdvals(a-b)))


def correlation_factory(d,z):
    d=np.asarray(d,complex); z=np.asarray(z,complex)
    def corr(tau):
        a=np.asarray(tau)
        aa=np.abs(a)
        cp=np.zeros_like(aa,dtype=complex)
        for dk,zk in zip(d,z):
            cp += dk*np.exp(-zk*aa)
        return np.where(a>=0,cp,np.conj(cp))
    return corr


def main():
    wc,xop,uop,H,d,z,ref=fp.harmonic_setup(DIM,NPADE)
    cr,vr,ci,vi=base.pade_bath_expansion(wc,NPADE)
    bath=BosonicBath(xop,cr,vr,ci,vi,combine=True,tag='dim2-mapping')
    solver=HEOMSolver(H,bath,max_depth=HEOM_DEPTH,options={'progress_bar':''})
    L=schur.scipy_rhs(solver)
    vss,solve_s,res_abs,res_rel,warn=steady.constrained_nullvector(L,DIM)
    rho_h=vss[:DIM*DIM].reshape((DIM,DIM),order='F')
    rho_h=0.5*(rho_h+rho_h.conj().T)
    rho_h=rho_h/np.trace(rho_h)
    eh=np.linalg.eigvalsh(rho_h)
    print(f"HEOM dim={DIM} p4 depth={HEOM_DEPTH} nado={len(solver.ados.labels)} "
          f"full_dim={L.shape[0]} solve_s={solve_s:.3f} residual={res_abs:.3e} "
          f"eigmin={eh.min():+.12e} trace={np.trace(rho_h)}",flush=True)
    print('HEOM_RHO ' + ' '.join(f'{x.real:+.12e}{x.imag:+.12e}j' for x in rho_h.reshape(-1)),flush=True)

    h=np.asarray(H.full(),complex)
    q=np.asarray(xop.full(),complex)
    rho0=np.asarray((basis(DIM,0)*basis(DIM,0).dag()).full(),complex)
    system=oqupy.System(h)
    correlations=oqupy.CustomCorrelations(correlation_function=correlation_factory(d,z))
    obath=oqupy.Bath(q,correlations)
    pars=oqupy.TempoParameters(dt=DT,tcut=TCUT,epsrel=EPSREL)
    dyn=oqupy.tempo_compute(system=system,bath=obath,initial_state=rho0,
                            start_time=0.0,end_time=TEND,parameters=pars,
                            unique=True,progress_type='silent')
    times=np.asarray(dyn.times,float); states=np.asarray(dyn.states,complex)
    for tt in (8.0,16.0,24.0,32.0):
        j=int(np.argmin(np.abs(times-tt)))
        rho=states[j]
        print(f"TEMPO tau={times[j]:.6f} half_to_HEOM={half_distance(rho,rho_h):.12e} "
              f"trace=({np.trace(rho).real:.12e}{np.trace(rho).imag:+.2e}j) "
              f"eigmin={np.linalg.eigvalsh(0.5*(rho+rho.conj().T)).min():+.12e}",flush=True)
    rho_t=states[-1]
    late=states[int(np.argmin(np.abs(times-24.0)))]
    half=half_distance(rho_t,rho_h)
    latehalf=half_distance(rho_t,late)
    anti=np.linalg.norm(rho_t-rho_t.conj().T,ord='fro')/max(np.linalg.norm(rho_t,ord='fro'),1e-300)
    et=np.linalg.eigvalsh(0.5*(rho_t+rho_t.conj().T))
    print(f"MAPPING half_TEMPO_HEOM={half:.12e} late_half={latehalf:.12e} "
          f"tempo_eigmin={et.min():+.12e} anti={anti:.12e} "
          f"traceerr={abs(np.trace(rho_t)-1):.12e}",flush=True)
    print(f"::notice title=Experiment 03 TEMPO-HEOM dim2 mapping::half={half:.3e} late={latehalf:.3e}")
    if res_abs>1e-9:
        raise RuntimeError('HEOM dim2 stationary solve did not converge')
    if abs(np.trace(rho_t)-1)>1e-8 or anti>1e-8:
        raise RuntimeError('TEMPO dim2 mapping lost trace/Hermiticity')
    # Mapping-only sanity threshold; not a Gate-B/C threshold.
    if half>2e-2:
        raise RuntimeError('TEMPO and HEOM dim2 late states grossly disagree')
    print('PASS_TEMPO_HEOM_DIM2_MAPPING_SANITY')

if __name__=='__main__': main()
