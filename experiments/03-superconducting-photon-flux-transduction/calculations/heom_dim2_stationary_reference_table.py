#!/usr/bin/env python3
"""Compact aggregate table for the dim=2 HEOM stationary reference audit."""
from __future__ import annotations

import numpy as np
from qutip.solver.heom import HEOMSolver, BosonicBath

import heom_fp_harmonic_oracle as fp
import heom_harmonic_pade_depth as base
import heom_schur_terminator_harmonic_probe as schur
import heom_harmonic_steady_nullspace_probe as steady

CASES=[('p4d4',4,4),('p4d5',4,5),('p4d6',4,6),('p4d7',4,7),
       ('p4d8',4,8),('p4d9',4,9),('p5d6',5,6),('p5d7',5,7),('p5d8',5,8)]

def solve(npade,depth):
    wc,xop,_u,H,_d,_z,_eref=fp.harmonic_setup(2,npade)
    cr,vr,ci,vi=base.pade_bath_expansion(wc,npade)
    bath=BosonicBath(xop,cr,vr,ci,vi,combine=True,tag='dim2-table')
    s=HEOMSolver(H,bath,max_depth=depth,options={'progress_bar':''})
    L=schur.scipy_rhs(s)
    v,ts,res,_rr,_w=steady.constrained_nullvector(L,2)
    rho=v[:4].reshape((2,2),order='F')
    anti=float(np.linalg.norm(rho-rho.conj().T,ord='fro'))
    rho=.5*(rho+rho.conj().T); rho/=np.trace(rho)
    return float(rho[1,1].real),complex(rho[0,1]),float(np.linalg.eigvalsh(rho).min()),res,anti,len(s.ados.labels),ts

def main():
    vals=[]
    print('case npade depth nado pop1 offabs eigmin residual anti solve_s',flush=True)
    for name,p,d in CASES:
        pop,off,eig,res,anti,nado,ts=solve(p,d)
        vals.append((name,p,d,pop))
        print(f'{name} {p} {d} {nado} {pop:.15e} {abs(off):.3e} {eig:+.15e} {res:.3e} {anti:.3e} {ts:.3f}',flush=True)
    ref=next(v[3] for v in vals if v[0]=='p4d9')
    print('DIFFERENCE_TO_P4D9',flush=True)
    for name,p,d,pop in vals:
        print(f'{name} delta_pop1={pop-ref:+.15e}',flush=True)
    p5=next(v[3] for v in vals if v[0]=='p5d8')
    print(f'PADE_CONTROL p4d9={ref:.15e} p5d8={p5:.15e} delta={p5-ref:+.15e}',flush=True)
    print(f'DIM2_HEOM_REFERENCE_FINAL pop1={ref:.15e} p5delta={p5-ref:+.3e}',flush=True)
    print(f'::notice title=Experiment 03 dim2 HEOM reference::pop1={ref:.12e} p5delta={p5-ref:+.3e}')

if __name__=='__main__': main()
