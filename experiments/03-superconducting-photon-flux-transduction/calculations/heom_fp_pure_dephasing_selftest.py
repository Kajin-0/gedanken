#!/usr/bin/env python3
"""Analytic implementation audit for the Experiment-03 FP-HEOM generator.

For H=0 and a single real exponential bath correlation

    C(t) = d exp(-Gamma t),

the pure-dephasing coherence between q eigenstates q_a,q_b is exactly

    rho_ab(t)/rho_ab(0) = exp[-Phi(t)],
    Phi(t) = D/Gamma^2 * (Gamma*t - 1 + exp(-Gamma*t)),
    D = d (q_a-q_b)^2.

This is Eq. (3)/(9) of Krug & Stockburger's HEOM stability analysis.  It is
independent of the Experiment-03 circuit and therefore audits only the sparse
FP-HEOM implementation: hierarchy enumeration, forward/backward superoperator
signs, vectorization convention and complex square-root normalization.
"""
from __future__ import annotations

import math
import numpy as np
from scipy.sparse.linalg import expm_multiply
from qutip import Qobj

import heom_fp_harmonic_oracle as fp


def main():
    dim=2
    d0=0.20
    gamma=1.0
    depth=10
    H=Qobj(np.zeros((dim,dim),complex))
    q=Qobj(np.diag([0.0,1.0]).astype(complex))
    L,labels=fp.fp_generator(H,q,np.asarray([d0],complex),
                            np.asarray([gamma],complex),depth)
    rho0=np.array([[0.5,0.5],[0.5,0.5]],complex)
    v0=np.zeros(L.shape[0],complex)
    v0[:dim*dim]=rho0.reshape(-1,order='F')
    print(f"SELFTEST depth={depth} nado={len(labels)} full_dim={L.shape[0]} nnz={L.nnz}")
    maxerr=0.0
    for t in (0.2,0.5,1.0,2.0,5.0):
        v=expm_multiply(L*t,v0)
        rho=v[:dim*dim].reshape((dim,dim),order='F')
        phi=d0/(gamma*gamma)*(gamma*t-1+math.exp(-gamma*t))
        exact=0.5*math.exp(-phi)
        got=rho[0,1]
        err=abs(got-exact)/abs(exact)
        maxerr=max(maxerr,err)
        tr=np.trace(rho)
        print(f"t={t:.3f} coherence=({got.real:+.12e}{got.imag:+.12e}j) "
              f"exact={exact:+.12e} relerr={err:.3e} trace=({tr.real:.12e}{tr.imag:+.2e}j)")
    print(f"FP_PURE_DEPHASING maxrel={maxerr:.12e}")
    print(f"::notice title=Experiment 03 FP-HEOM analytic self-test::maxrel={maxerr:.6e}")
    if maxerr>2e-8:
        raise RuntimeError("FP-HEOM implementation failed analytic pure-dephasing audit")
    print("PASS_FP_IMPLEMENTATION_AUDIT")


if __name__=='__main__': main()
