#!/usr/bin/env python3
"""Converged dim=2 HEOM transient relaxation reference.

This cheap control evolves the same factorized initial state |0><0| used by the
direct TEMPO mapping tests with conventional p4/depth9 HEOM and reports the
half trace-distance to the depth/order-converged stationary state at the same
times already logged by TEMPO.  It does not use TEMPO and therefore provides an
independent relaxation-timescale reference.
"""
from __future__ import annotations

import numpy as np
from scipy.linalg import svdvals
from qutip import basis
from qutip.solver.heom import HEOMSolver, BosonicBath

import heom_fp_harmonic_oracle as fp
import heom_harmonic_pade_depth as base
import heom_schur_terminator_harmonic_probe as schur
import heom_harmonic_steady_nullspace_probe as steady

DIM=2; NPADE=4; DEPTH=9

def half(a,b): return .5*float(np.sum(svdvals(a-b)))

def main():
    wc,xop,_u,H,_d,_z,_ref=fp.harmonic_setup(DIM,NPADE)
    cr,vr,ci,vi=base.pade_bath_expansion(wc,NPADE)
    bath=BosonicBath(xop,cr,vr,ci,vi,combine=True,tag='dim2-transient-ref')
    solver=HEOMSolver(H,bath,max_depth=DEPTH,options={
        'progress_bar':'','method':'bdf','rtol':2e-10,'atol':2e-12,'nsteps':200000})
    L=schur.scipy_rhs(solver)
    v,ss,res,_rr,_w=steady.constrained_nullvector(L,DIM)
    rho_ss=v[:4].reshape((2,2),order='F'); rho_ss=.5*(rho_ss+rho_ss.conj().T); rho_ss/=np.trace(rho_ss)
    times=np.arange(0.,64.0+.2/2,.2)
    rho0=basis(DIM,0)*basis(DIM,0).dag()
    out=solver.run(rho0,times)
    print(f"HEOM_TRANSIENT_REF nado={len(solver.ados.labels)} stationary_pop1={rho_ss[1,1].real:.15e} nullres={res:.3e}",flush=True)
    for tt in (1.,2.,4.,8.,16.,24.,32.,48.,64.):
        j=int(np.argmin(np.abs(times-tt))); rho=np.asarray(out.states[j].full(),complex)
        d=half(rho,rho_ss); off=abs(rho[0,1]); ev=np.linalg.eigvalsh(.5*(rho+rho.conj().T))
        print(f"POINT tau={times[j]:.3f} half_to_ss={d:.12e} pop1={rho[1,1].real:.12e} offabs={off:.3e} eigmin={ev.min():+.12e}",flush=True)
    print('PASS_HEOM_DIM2_TRANSIENT_REFERENCE')

if __name__=='__main__': main()
