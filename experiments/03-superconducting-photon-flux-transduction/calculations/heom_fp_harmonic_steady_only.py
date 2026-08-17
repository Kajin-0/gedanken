#!/usr/bin/env python3
"""Stationary-only exact-oracle probe for FP-HEOM dim8/p4/depth3.

The full FP harmonic job computes the rightmost spectrum before solving the
stationary state.  This companion calculation evaluates only the independent
trace-constrained zero mode so the state-convergence axis can be resolved while
the expensive ARPACK spectrum calculation continues.

It uses exactly the same FP generator and exact Gaussian/FDT reference.  No
projection, clipping or positivity repair is applied.
"""
from __future__ import annotations

import math

import heom_fp_harmonic_oracle as fp
import heom_harmonic_steady_nullspace_probe as steady


def main():
    dim=8; npade=4; depth=3
    wc,xop,uop,H,d,z,ref=fp.harmonic_setup(dim,npade)
    L,labels=fp.fp_generator(H,xop,d,z,depth)
    print(f"FP_STEADY_ONLY dim={dim} Npade={npade} depth={depth} nado={len(labels)} "
          f"full_dim={L.shape[0]} nnz={L.nnz} wc/2pi={wc/(2*math.pi)*1e-9:.9f}GHz",flush=True)
    v,solve_s,res_abs,res_rel,warn=steady.constrained_nullvector(L,dim)
    m=steady.reduced_metrics(v,dim,ref)
    maxfdt=max(abs(m['relx']),abs(m['relu']))
    print(f"NULLSPACE solve_s={solve_s:.3f} residual={res_abs:.12e} scaled={res_rel:.12e} warnings={warn or 'NONE'}",flush=True)
    print(f"STATE trace=({m['trace'].real:.12e}{m['trace'].imag:+.2e}j) anti={m['anti']:.12e} "
          f"eigmin={m['eigmin']:+.12e} negmass={m['neg']:.12e}",flush=True)
    print(f"ORACLE relx={m['relx']:+.12e} relu={m['relu']:+.12e} maxFDT={maxfdt:.12e} "
          f"half_nuclear={m['half_nuclear']:.12e} frobenius={m['frob']:.12e}",flush=True)
    checks={
        'reference_basis':ref['basis_err']<1e-7,
        'fdt':maxfdt<1e-6,
        'half_nuclear':m['half_nuclear']<5e-6,
        'negative_mass':m['neg']<5e-8,
        'trace':abs(m['trace']-1)<1e-10,
        'hermiticity':m['anti']<1e-10,
        'null_residual':res_abs<1e-8,
    }
    for k,ok in checks.items():
        print(f"CHECK {k}={'PASS' if ok else 'FAIL'}",flush=True)
    msg=(f"FP_STEADY_D3 maxFDT={maxfdt:.6e} half_nuclear={m['half_nuclear']:.6e} "
         f"negmass={m['neg']:.6e} eigmin={m['eigmin']:.6e} oracle_pass={all(checks.values())}")
    print(msg,flush=True)
    print(f"::notice title=Experiment 03 FP-HEOM depth3 stationary oracle::{msg}",flush=True)
    if res_abs>=1e-8:
        raise RuntimeError('stationary solve residual too large')

if __name__=='__main__': main()
