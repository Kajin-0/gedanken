#!/usr/bin/env python3
"""Audit the counterterm-renormalized system-normal-mode basis.

The covariance-adapted squeezed basis represents the exact reduced equilibrium
very compactly, but a small hard truncation of its non-diagonal system
Hamiltonian can distort higher isolated levels.  For TEMPO dynamics a better
basis is the exact normal mode of the quadratic *system Hamiltonian including
the physical counterterm*.

For
    H = n + 1/2 + k_ct x^2,
    x = sigma0(a+a^dag),
we have
    Omega_s = sqrt(1 + 4 k_ct sigma0^2),
    r_s = (1/4) log(1 + 4 k_ct sigma0^2).

In the system-mode basis b:
    H = Omega_s (b^dag b + 1/2),
    x = sigma0 exp(-r_s)(b+b^dag),
    u = i sigma0 exp(+r_s)(b^dag-b).

The exact open-system Gaussian equilibrium becomes
    rho = S(r_eq-r_s) rho_th(nbar) S^dag(r_eq-r_s).

Thus H is exactly diagonal at every retained dimension while the reduced state
remains compact.  This script verifies the transformation against a large bare
basis and finds the minimum dimension meeting the frozen <1e-7 exact-reference
width criterion.
"""
from __future__ import annotations

import math
import numpy as np
from qutip import destroy, qeye, thermal_dm, squeeze

import heom_harmonic_final_state_gate as finalgate
import heom_harmonic_pade_depth as base
from quantum_initial_capture import PHI_BAR


def setup_constants():
    ref=finalgate.exact_reference(24)
    wc=base.HBAR/(2*base.C*PHI_BAR**2*ref['sigma0']**2)
    ct_phys=PHI_BAR**2/base.HBAR * base.G*base.WD/(2*math.sqrt(2))
    kct=ct_phys/wc
    fac=1+4*kct*ref['sigma0']**2
    Omega=math.sqrt(fac)
    rs=.25*math.log(fac)
    reff=ref['r']-rs
    return ref,wc,kct,Omega,rs,reff


def system_basis(dim,ref,Omega,rs,reff):
    a=destroy(dim); n=a.dag()*a
    x=ref['sigma0']*math.exp(-rs)*(a+a.dag())
    u=1j*ref['sigma0']*math.exp(+rs)*(a.dag()-a)
    H=Omega*(n+.5*qeye(dim))
    S=squeeze(dim,reff)
    rho=S*thermal_dm(dim,ref['nbar'])*S.dag()
    def width(op):
        m=complex((rho*op).tr()); m2=complex((rho*op*op).tr())
        return math.sqrt(max(float(np.real(m2-m*m)),0.0))
    sx=width(x); su=width(u)
    berr=max(abs(sx/ref['target_x']-1),abs(su/ref['target_u']-1))
    ev=np.real(np.linalg.eigvalsh(rho.full()))
    return x,u,H,rho,sx,su,berr,float(ev.min()),float(np.real(rho.diag()[-1]))


def bare(dim,ref,kct):
    a=destroy(dim); n=a.dag()*a
    x=ref['sigma0']*(a+a.dag())
    u=1j*ref['sigma0']*(a.dag()-a)
    H=n+.5*qeye(dim)+kct*(x*x)
    return x,u,H


def main():
    ref,wc,kct,Omega,rs,reff=setup_constants()
    print(f"SYSTEM_MODE sigma0={ref['sigma0']:.12e} nbar={ref['nbar']:.12e} "
          f"r_eq={ref['r']:.12e} r_sys={rs:.12e} r_eff={reff:+.12e} "
          f"Omega={Omega:.12e} kct={kct:.12e} wc/2pi={wc/(2*math.pi)*1e-9:.9f}GHz",flush=True)
    for dim in (3,4,5,6,7,8,10):
        x,u,H,rho,sx,su,berr,eigmin,top=system_basis(dim,ref,Omega,rs,reff)
        # H is analytic diagonal, so its retained levels must be exact by construction.
        ev=np.asarray(H.eigenenergies(),float)
        expected=Omega*(np.arange(dim)+.5)
        herr=float(np.max(np.abs(ev-expected)))
        print(f"DIM {dim:02d} basis_err={berr:.12e} sx={sx:.12e} su={su:.12e} "
              f"rho_eigmin={eigmin:+.12e} topDiag={top:.12e} Hdiag_err={herr:.3e}",flush=True)

    # High-basis explicit squeeze check: S(rs)^dag H_bare S(rs) and operators
    # must match the canonical system-mode formulas in a safe low block.
    big=48; ncheck=14
    xb,ub,Hb=bare(big,ref,kct)
    S=squeeze(big,rs)
    xu=S.dag()*xb*S; uu=S.dag()*ub*S; Hu=S.dag()*Hb*S
    xs,us,Hs,*_=system_basis(big,ref,Omega,rs,reff)
    def block(q): return np.asarray(q.full(),complex)[:ncheck,:ncheck]
    def rel(a,b):
        aa=block(a); bb=block(b)
        return float(np.linalg.norm(aa-bb,ord='fro')/max(np.linalg.norm(bb,ord='fro'),1e-300))
    rx=rel(xs,xu); ru=rel(us,uu); rh=rel(Hs,Hu)
    print(f"UNITARY_LOW_BLOCK n={ncheck} rel_x={rx:.12e} rel_u={ru:.12e} rel_H={rh:.12e}",flush=True)

    *_,b7,e7,t7=system_basis(7,ref,Omega,rs,reff)
    ok=(b7<1e-7 and rx<1e-10 and ru<1e-10 and rh<1e-10 and e7>-1e-12)
    msg=(f"SYSTEM_MODE_BASIS dim7_basis_err={b7:.6e} rho_eigmin={e7:.3e} "
         f"topDiag={t7:.3e} unitaryH={rh:.3e} pass={ok}")
    print(msg,flush=True)
    print(f"::notice title=Experiment 03 harmonic system-mode basis::{msg}",flush=True)
    if not ok: raise RuntimeError('system-mode dim7 representation audit failed')
    print('PASS_HARMONIC_SYSTEM_MODE_BASIS')

if __name__=='__main__': main()
