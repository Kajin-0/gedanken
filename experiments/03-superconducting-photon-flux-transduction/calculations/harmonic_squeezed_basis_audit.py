#!/usr/bin/env python3
"""Audit a covariance-adapted squeezed basis for the harmonic open-system oracle.

This is a representation optimization only.  No bath, Hamiltonian, counterterm,
or physical observable is changed.

The accepted exact reduced harmonic state is

    rho_exact = S(r) rho_th(nbar) S(r)^dagger

in the original bare-oscillator basis.  Expressing the same physical operators
in the squeezed basis makes the exact state simply thermal.  The transformed
quadratures are

    x = sigma0 exp(-r) (b+b^dagger)
    u = i sigma0 exp(+r) (b^dagger-b),

and the physical dimensionless system Hamiltonian is written directly as

    H = (x^2+u^2)/(4 sigma0^2) + k_ct x^2.

A covariance-adapted basis can therefore reduce the Hilbert dimension needed to
represent the exact coupled equilibrium without altering the physical problem.
This script checks:

1. exact-reference width error versus basis dimension;
2. top-state thermal population;
3. low isolated-system eigenvalue convergence versus a large bare-basis oracle;
4. consistency of the canonical transformed H,x,u with an explicit high-basis
   unitary squeeze transformation in the low retained block.

No Gate-C result is produced here.
"""
from __future__ import annotations

import math
import numpy as np
from qutip import destroy, qeye, thermal_dm, squeeze

import heom_harmonic_final_state_gate as finalgate
import heom_harmonic_pade_depth as base
from quantum_initial_capture import PHI_BAR


def adapted(dim, ref, kct):
    a=destroy(dim)
    sx0=ref['sigma0']*math.exp(-ref['r'])
    su0=ref['sigma0']*math.exp(+ref['r'])
    x=sx0*(a+a.dag())
    u=1j*su0*(a.dag()-a)
    H=(x*x+u*u)/(4*ref['sigma0']**2) + kct*(x*x)
    rho=thermal_dm(dim,ref['nbar'])
    def width(op):
        m=complex((rho*op).tr()); m2=complex((rho*op*op).tr())
        return math.sqrt(max(float(np.real(m2-m*m)),0.0))
    sx=width(x); su=width(u)
    berr=max(abs(sx/ref['target_x']-1),abs(su/ref['target_u']-1))
    top=float(np.real(rho.diag()[-1]))
    return x,u,H,rho,sx,su,berr,top


def bare(dim, ref, kct):
    a=destroy(dim); n=a.dag()*a
    x=ref['sigma0']*(a+a.dag())
    u=1j*ref['sigma0']*(a.dag()-a)
    H=n+0.5*qeye(dim)+kct*(x*x)
    return x,u,H


def relfro(a,b):
    aa=np.asarray(a.full(),complex); bb=np.asarray(b.full(),complex)
    return float(np.linalg.norm(aa-bb,ord='fro')/max(np.linalg.norm(bb,ord='fro'),1e-300))


def main():
    # Large reference ensures the squeeze/unitary audit is not contaminated by
    # the small-basis truncation we are trying to quantify.
    ref=finalgate.exact_reference(20)
    # Recover the same physical counterterm coefficient used everywhere else.
    # fp/base constants obey H_ct=(ct_phys/wc)x^2.
    wc=base.HBAR/(2*base.C*PHI_BAR**2*ref['sigma0']**2)
    ct_phys=PHI_BAR**2/base.HBAR * base.G*base.WD/(2*math.sqrt(2))
    kct=ct_phys/wc
    print(f"ADAPTED_REFERENCE sigma0={ref['sigma0']:.12e} nbar={ref['nbar']:.12e} "
          f"r={ref['r']:.12e} kct={kct:.12e} wc/2pi={wc/(2*math.pi)*1e-9:.9f}GHz",flush=True)
    print(f"TARGET sx={ref['target_x']:.12e} su={ref['target_u']:.12e}",flush=True)

    # Large bare isolated-system eigenvalue oracle.
    xb,ub,Hb=bare(40,ref,kct)
    eval_ref=np.asarray(Hb.eigenenergies(),float)

    for dim in (3,4,5,6,7,8,10):
        x,u,H,rho,sx,su,berr,top=adapted(dim,ref,kct)
        ev=np.asarray(H.eigenenergies(),float)
        nkeep=min(4,dim-1)
        spec=max(abs(ev[:nkeep]-eval_ref[:nkeep])) if nkeep else float('nan')
        print(f"DIM {dim:02d} basis_err={berr:.12e} sx={sx:.12e} su={su:.12e} "
              f"topPop={top:.12e} low{nkeep}_absEerr={spec:.12e}",flush=True)

    # Explicit unitary audit in a large Hilbert space.  QuTiP's convention used
    # by exact_reference is rho=S rho_th S^dag, hence O_adapt=S^dag O_bare S.
    big=40
    xb,ub,Hb=bare(big,ref,kct)
    S=squeeze(big,ref['r'])
    xu=S.dag()*xb*S; uu=S.dag()*ub*S; Hu=S.dag()*Hb*S
    xa,ua,Ha,*_=adapted(big,ref,kct)
    # Compare only a safe low block, avoiding artificial top-state boundary.
    n=12
    def block(q):
        return np.asarray(q.full(),complex)[:n,:n]
    def block_rel(a,b):
        aa=block(a); bb=block(b)
        return float(np.linalg.norm(aa-bb,ord='fro')/max(np.linalg.norm(bb,ord='fro'),1e-300))
    rx=block_rel(xa,xu); ru=block_rel(ua,uu); rh=block_rel(Ha,Hu)
    print(f"UNITARY_LOW_BLOCK n={n} rel_x={rx:.12e} rel_u={ru:.12e} rel_H={rh:.12e}",flush=True)

    # Fixed representation criterion for use in the final TEMPO harmonic gate.
    _,_,_,_,_,_,b6,t6=adapted(6,ref,kct)
    pass_basis=(b6<1e-7 and t6<5e-8 and rx<1e-10 and ru<1e-10 and rh<1e-10)
    msg=f"SQUEEZED_BASIS dim6_basis_err={b6:.6e} topPop={t6:.6e} unitaryH={rh:.3e} pass={pass_basis}"
    print(msg,flush=True)
    print(f"::notice title=Experiment 03 harmonic squeezed-basis audit::{msg}",flush=True)
    if not pass_basis:
        raise RuntimeError('covariance-adapted dim6 basis did not pass representation audit')
    print('PASS_SQUEEZED_HARMONIC_BASIS')

if __name__=='__main__': main()
