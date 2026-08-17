#!/usr/bin/env python3
"""Converge the finite dim=2 conventional-HEOM stationary reference.

Direct TEMPO is currently compared against a conventional p4/depth6 HEOM
stationary state for the same tiny two-level truncation.  Before interpreting a
long-time TEMPO plateau, this script certifies that the HEOM comparison state is
itself converged in hierarchy depth and Padé order.

This is a reference audit only.  It does not validate nonlinear Gate C.1 and it
does not alter any physical parameter.
"""
from __future__ import annotations

import argparse
import numpy as np
from qutip.solver.heom import HEOMSolver, BosonicBath

import heom_fp_harmonic_oracle as fp
import heom_harmonic_pade_depth as base
import heom_schur_terminator_harmonic_probe as schur
import heom_harmonic_steady_nullspace_probe as steady

DIM=2
CASES={
    'p4d4':(4,4), 'p4d5':(4,5), 'p4d6':(4,6), 'p4d7':(4,7),
    'p4d8':(4,8), 'p4d9':(4,9),
    'p5d6':(5,6), 'p5d7':(5,7), 'p5d8':(5,8),
}


def main(name):
    npade,depth=CASES[name]
    wc,xop,uop,H,d,z,eref=fp.harmonic_setup(DIM,npade)
    cr,vr,ci,vi=base.pade_bath_expansion(wc,npade)
    bath=BosonicBath(xop,cr,vr,ci,vi,combine=True,tag=f'dim2-ref-{name}')
    solver=HEOMSolver(H,bath,max_depth=depth,options={'progress_bar':''})
    L=schur.scipy_rhs(solver)
    v,solve_s,res_abs,res_rel,warn=steady.constrained_nullvector(L,DIM)
    rho=v[:DIM*DIM].reshape((DIM,DIM),order='F')
    anti=np.linalg.norm(rho-rho.conj().T,ord='fro')
    rhoh=.5*(rho+rho.conj().T); rhoh/=np.trace(rhoh)
    ev=np.linalg.eigvalsh(rhoh)
    off=complex(rhoh[0,1])
    pop1=float(np.real(rhoh[1,1]))
    print(f"CASE={name} Npade={npade} depth={depth} nexp={len(solver.ados.exponents)} "
          f"nado={len(solver.ados.labels)} full_dim={L.shape[0]} nnz={L.nnz} solve_s={solve_s:.3f}",flush=True)
    print(f"NULL residual={res_abs:.12e} scaled={res_rel:.12e} warnings={warn or 'NONE'} "
          f"trace=({np.trace(rho).real:.12e}{np.trace(rho).imag:+.2e}j) anti_raw={anti:.12e}",flush=True)
    print(f"STATE pop0={rhoh[0,0].real:.15e} pop1={pop1:.15e} "
          f"off=({off.real:+.15e}{off.imag:+.15e}j) eigmin={ev.min():+.15e}",flush=True)
    msg=(f"DIM2_HEOM_REF case={name} pop1={pop1:.12e} offabs={abs(off):.3e} "
         f"eigmin={ev.min():.12e} residual={res_abs:.3e}")
    print(msg,flush=True)
    print(f"::notice title=Experiment 03 dim2 HEOM stationary reference::{msg}",flush=True)
    if res_abs>1e-8 or anti>1e-9 or abs(np.trace(rho)-1)>1e-9:
        raise RuntimeError('dim2 HEOM stationary reference failed numerical guard')

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--case',choices=sorted(CASES),required=True)
    args=ap.parse_args(); main(args.case)
