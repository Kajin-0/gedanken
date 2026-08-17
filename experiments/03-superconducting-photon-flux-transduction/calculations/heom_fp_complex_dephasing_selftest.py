#!/usr/bin/env python3
"""Complex-pole analytic audit for the Experiment-03 FP-HEOM generator.

The first pure-dephasing audit used a real coefficient/rate and therefore did
not exercise the complex forward/backward branches used by the direct-port
circuit poles.  Here

    C(t) = d exp(-z t),  Re z > 0,

with genuinely complex d and z.  For H=0, q=diag(0,1), the exact 0->1
coherence is

    rho_01(t) = rho_01(0) exp[-F*(t)],
    F(t) = d/z^2 [z t - 1 + exp(-z t)].

This follows directly from the Gaussian pure-dephasing influence functional.
It audits the conjugate forward/backward terms and complex square-root branches
in the sparse FP generator.  It is an implementation test only.
"""
from __future__ import annotations

import numpy as np
from scipy.sparse.linalg import expm_multiply
from qutip import Qobj

import heom_fp_harmonic_oracle as fp


def main():
    dim=2
    d0=0.20+0.07j
    z0=1.10+0.40j
    depth=12
    H=Qobj(np.zeros((dim,dim),complex))
    q=Qobj(np.diag([0.0,1.0]).astype(complex))
    L,labels=fp.fp_generator(H,q,np.asarray([d0],complex),
                            np.asarray([z0],complex),depth)
    rho0=np.array([[0.5,0.5],[0.5,0.5]],complex)
    v0=np.zeros(L.shape[0],complex)
    v0[:dim*dim]=rho0.reshape(-1,order='F')
    print(f"COMPLEX_SELFTEST depth={depth} nado={len(labels)} full_dim={L.shape[0]} nnz={L.nnz}")
    print(f"d=({d0.real:+.9e}{d0.imag:+.9e}j) z=({z0.real:+.9e}{z0.imag:+.9e}j)")
    maxerr=0.0
    maxherm=0.0
    for t in (0.2,0.5,1.0,2.0,5.0):
        v=expm_multiply(L*t,v0)
        rho=v[:dim*dim].reshape((dim,dim),order='F')
        zz=np.conj(z0); dd=np.conj(d0)
        F=dd/(zz*zz)*(zz*t-1.0+np.exp(-zz*t))
        exact=0.5*np.exp(-F)
        got=rho[0,1]
        err=abs(got-exact)/max(abs(exact),1e-300)
        herm=np.linalg.norm(rho-rho.conj().T,ord='fro')
        maxerr=max(maxerr,float(err)); maxherm=max(maxherm,float(herm))
        tr=np.trace(rho)
        print(f"t={t:.3f} coherence=({got.real:+.12e}{got.imag:+.12e}j) "
              f"exact=({exact.real:+.12e}{exact.imag:+.12e}j) relerr={err:.3e} "
              f"herm={herm:.3e} trace=({tr.real:.12e}{tr.imag:+.2e}j)")
    print(f"FP_COMPLEX_DEPHASING maxrel={maxerr:.12e} maxherm={maxherm:.12e}")
    print(f"::notice title=Experiment 03 FP-HEOM complex analytic self-test::maxrel={maxerr:.6e} maxherm={maxherm:.3e}")
    if maxerr>2e-8 or maxherm>2e-10:
        raise RuntimeError("FP-HEOM failed complex-pole pure-dephasing audit")
    print("PASS_FP_COMPLEX_IMPLEMENTATION_AUDIT")


if __name__=='__main__': main()
