#!/usr/bin/env python3
"""Harmonic HEOM regression for the UV-regular direct Experiment-03 port bath.

This is a method-validation calculation, not detector capture.

Before a nonperturbative hierarchy is applied to the nonlinear time-dependent
latch, the same bath decomposition must reproduce the independently known cold
linear quantum-FDT phase covariance.  The system is therefore the cold harmonic
phase mode at the certified delta=.212 operating point, coupled directly to the
port bath whose exact correlation is validated in
`direct_port_bath_correlation.py`.

Units
-----
QuTiP uses hbar=1.  We nondimensionalize time by the physical cold plasma
frequency omega_c.  The system Hamiltonian is H/(hbar omega_c), bath exponents
are gamma/omega_c, and correlation coefficients are C_X/omega_c^2, with

    X = (Phi_bar/hbar) I_N,

because H_int/hbar = x X for physical coupling q I_N = Phi_bar x I_N.

Counterterm
-----------
A Caldeira-Leggett bath generated from the dissipative spectral density must be
used with the quadratic counterterm if the experimentally defined static phase
potential is to remain unrenormalized.  For

    J_Qutip(omega) = (Phi_bar^2/hbar) omega ReY(omega)

and ReY=G/[1+(omega/omega_D)^4],

    H_ct/(hbar) = x^2/pi * int_0^inf J_Qutip(omega)/omega dω
                = [Phi_bar^2/hbar * G omega_D/(2 sqrt(2))] x^2.

The regression reports both covariance accuracy and hierarchy/Matsubara
convergence.  It must pass before any nonlinear HEOM probability is trusted.
"""
from __future__ import annotations

import math
import numpy as np

import full_dynamic_rfsquid as fd
from direct_port_bath_correlation import (
    HBAR, R, G, WD, bath_poles, bath_coeff, matsubara, mats_coeff,
)
from finite_time_basin_slice import cold_phase_scale
from quantum_initial_capture import PHI_BAR
from two_pole_joint_covariance import covariance_matrix

from qutip import destroy, qeye, expect
from qutip.solver.heom import BosonicBath, HEOMSolver

L=111.5e-12
C=24.262211e-12
DELTA=.212
ALPHA=.90


def add_term(real_terms, imag_terms, c, gamma):
    """Split c exp(-gamma t) into exponential representations of Re C and Im C."""
    real_terms.append((0.5*c, gamma))
    real_terms.append((0.5*np.conj(c), np.conj(gamma)))
    imag_terms.append((c/(2j), gamma))
    imag_terms.append((-np.conj(c)/(2j), np.conj(gamma)))


def bath_expansion(wc: float, nmats: int):
    # Convert physical current correlation to QuTiP correlation of
    # X=(Phi_bar/hbar) I, then nondimensionalize by wc^2.
    cscale=(PHI_BAR/HBAR)**2/(wc*wc)
    real_terms=[]; imag_terms=[]
    for p in bath_poles():
        add_term(real_terms,imag_terms,bath_coeff(p)*cscale,(1j*p)/wc)
    for n in range(1,nmats+1):
        add_term(real_terms,imag_terms,mats_coeff(n)*cscale,matsubara(n)/wc)

    # BosonicBath(combine=True) will merge duplicate conjugate/Matsubara
    # frequencies. Keeping the algebra explicit makes the real/imag split auditable.
    cr=[complex(c) for c,v in real_terms]
    vr=[complex(v) for c,v in real_terms]
    ci=[complex(c) for c,v in imag_terms if abs(c)>1e-28]
    vi=[complex(v) for c,v in imag_terms if abs(c)>1e-28]
    return cr,vr,ci,vi


def solve_case(model, dim: int, nmats: int, depth: int, with_counterterm: bool=True):
    _xc,kappa,wc=cold_phase_scale(model,.6)
    sigma0=math.sqrt(HBAR/(2*C*PHI_BAR**2*wc))
    a=destroy(dim); n=a.dag()*a
    xop=sigma0*(a+a.dag())
    uop=1j*sigma0*(a.dag()-a)
    H=n+0.5*qeye(dim)

    ct_phys=PHI_BAR**2/HBAR * G*WD/(2*math.sqrt(2))
    ct_scaled=ct_phys/wc
    if with_counterterm:
        H=H+ct_scaled*(xop*xop)

    cr,vr,ci,vi=bath_expansion(wc,nmats)
    bath=BosonicBath(xop,cr,vr,ci,vi,combine=True,tag='direct-port')
    solver=HEOMSolver(H,bath,max_depth=depth,
                      options={'progress_bar':'','store_states':False})
    rho,ados=solver.steady_state()
    tr=float(np.real(rho.tr()))
    sx=math.sqrt(max(float(np.real(expect(xop*xop,rho)-expect(xop,rho)**2)),0.0))
    su=math.sqrt(max(float(np.real(expect(uop*uop,rho)-expect(uop,rho)**2)),0.0))
    evals=np.linalg.eigvalsh(rho.full())
    top=float(np.real(rho.diag()[-1]))
    return dict(sx=sx,su=su,trace=tr,eigmin=float(evals.min()),top=top,
                ct_scaled=ct_scaled,nexp=len(bath.exponents))


def main():
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT; original=fd.CASES[.6]
    try:
        fd.BETA_COLD=.80; fd.DELTA_TILT=DELTA; fd.CASES[.6]=(L,C,original[2])
        model=fd.DynamicForce(.6,quick=False,Tmax=1.02)
        M=covariance_matrix(model,.6,R,ALPHA,y_min=-22,y_max=22)
        target_x=math.sqrt(M[0,0]); target_u=math.sqrt(M[1,1])
        _xc,_kappa,wc=cold_phase_scale(model,.6)
        print(f'delta=.212 wc/2pi={wc/(2*math.pi)*1e-9:.8f}GHz '
              f'target_sigma_x={target_x:.10e} target_sigma_u={target_u:.10e}')

        configs=[(10,4,2),(10,4,3),(10,4,4),(10,8,3),(10,8,4),(10,16,3)]
        rows=[]
        for dim,nm,dep in configs:
            q=solve_case(model,dim,nm,dep,True); q.update(dim=dim,nmats=nm,depth=dep)
            q['ex']=q['sx']/target_x-1; q['eu']=q['su']/target_u-1
            rows.append(q)
            print(f'dim={dim} Nmat={nm} depth={dep} nexp={q["nexp"]}: '
                  f'sigx={q["sx"]:.10e} relx={q["ex"]:+.6e} '
                  f'sigu={q["su"]:.10e} relu={q["eu"]:+.6e} '
                  f'trace={q["trace"]:.12f} eigmin={q["eigmin"]:.3e} topPop={q["top"]:.3e} '
                  f'ct/wc={q["ct_scaled"]:.8f}')

        # Counterterm-control calculation at a moderate hierarchy.
        q0=solve_case(model,10,8,3,False)
        print(f'NO_COUNTERTERM Nmat=8 depth=3: sigx={q0["sx"]:.10e} '
              f'relx={q0["sx"]/target_x-1:+.6e} sigu={q0["su"]:.10e} '
              f'relu={q0["su"]/target_u-1:+.6e}')

        # Convergence diagnostics. Compare depth 3->4 at N=8 and Matsubara
        # 8->16 at depth=3. The latter is not expected to be as tight as the
        # 20-ps correlation metric because a stationary covariance samples t~0.
        r83=next(q for q in rows if q['nmats']==8 and q['depth']==3)
        r84=next(q for q in rows if q['nmats']==8 and q['depth']==4)
        r163=next(q for q in rows if q['nmats']==16 and q['depth']==3)
        depth_shift=max(abs(r84['sx']-r83['sx'])/target_x,
                        abs(r84['su']-r83['su'])/target_u)
        mats_shift=max(abs(r163['sx']-r83['sx'])/target_x,
                       abs(r163['su']-r83['su'])/target_u)
        final_err=max(abs(r163['ex']),abs(r163['eu']))
        msg=(f'harmonic HEOM direct-port: final(N16,d3) max_cov_error={final_err:.4e}; '
             f'N8 depth3to4 shift={depth_shift:.4e}; N8to16 depth3 shift={mats_shift:.4e}; '
             f'counterterm_relx={r83["ex"]:+.4e}; no_counterterm_relx={q0["sx"]/target_x-1:+.4e}')
        print(msg); print(f'::notice title=Experiment 03 harmonic HEOM port validation::{msg}')

        if any(abs(q['trace']-1)>2e-8 for q in rows):
            raise RuntimeError('HEOM steady state trace failure')
        if r163['eigmin'] < -2e-6:
            raise RuntimeError('HEOM physical density matrix has material negative eigenvalue')
        if final_err > .03:
            raise RuntimeError('direct-port HEOM harmonic covariance misses exact FDT by >3%')
        if depth_shift > .01:
            raise RuntimeError('HEOM hierarchy depth not converged to 1%')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot; fd.CASES[.6]=original

if __name__=='__main__': main()
