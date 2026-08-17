#!/usr/bin/env python3
"""Deep harmonic HEOM convergence using the direct-port Bose-Pade bath.

Gate-B objective
----------------
The ordinary Matsubara hierarchy gives excellent exact-FDT second moments but
small finite-tier density-matrix negativity.  Brute-force N_Mats=16, depth=4
already requires 7315 ADOs.  This script changes only the exponential
representation of the *same* direct-port bath: the thermal Matsubara ladder is
replaced by the independently validated Bose-Pade poles from
`direct_port_bath_pade.py`.

This allows materially deeper hierarchy tests while keeping the physical
spectral density, exact circuit-pole residues, counterterm, temperature and
system Hamiltonian fixed.  The lower Padé orders are not assumed exact; each is
judged directly against the exact FDT covariance and against neighboring Padé
orders.

This remains a harmonic method-validation calculation, not detector capture.
"""
from __future__ import annotations

import argparse
import math
import time
import numpy as np

import full_dynamic_rfsquid as fd
from finite_time_basin_slice import cold_phase_scale
from quantum_initial_capture import PHI_BAR
from two_pole_joint_covariance import covariance_matrix
from heom_harmonic_port_validation import (
    HBAR, R, G, WD, L, C, DELTA, ALPHA, add_term,
)
from direct_port_bath_correlation import bath_poles, bath_coeff
from direct_port_bath_pade import pade_terms

from qutip import destroy, qeye, fock_dm
from qutip.solver.heom import BosonicBath, HEOMSolver


CASES = {
    # Depth sequence at six total bath exponents (2 circuit + 4 thermal).
    "p4d3": dict(dim=8, npade=4, depth=3),
    "p4d4": dict(dim=8, npade=4, depth=4),
    "p4d5": dict(dim=8, npade=4, depth=5),
    "p4d6": dict(dim=8, npade=4, depth=6),
    # Padé-order convergence at a depth beyond the old Matsubara d=4 ceiling.
    "p5d5": dict(dim=8, npade=5, depth=5),
    "p6d5": dict(dim=8, npade=6, depth=5),
    # Strict correlation-certified N=8 reference at still-useful depth 4.
    "p8d4": dict(dim=8, npade=8, depth=4),
}


def pade_bath_expansion(wc: float, npade: int):
    """QuTiP real/imag exponential arrays for the validated direct-port Padé C(t)."""
    cscale=(PHI_BAR/HBAR)**2/(wc*wc)
    real_terms=[]
    imag_terms=[]
    for p in bath_poles():
        add_term(real_terms, imag_terms,
                 bath_coeff(p)*cscale, (1j*p)/wc)
    for c,nu in pade_terms(npade):
        add_term(real_terms, imag_terms, c*cscale, nu/wc)
    cr=[complex(c) for c,v in real_terms]
    vr=[complex(v) for c,v in real_terms]
    ci=[complex(c) for c,v in imag_terms if abs(c)>1e-28]
    vi=[complex(v) for c,v in imag_terms if abs(c)>1e-28]
    return cr,vr,ci,vi


def widths(expect_rows, i):
    x,x2,u,u2=(float(np.real(v[i])) for v in expect_rows)
    return (math.sqrt(max(x2-x*x,0.0)),
            math.sqrt(max(u2-u*u,0.0)))


def run_case(name: str):
    cfg=CASES[name]
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    original=fd.CASES[.6]
    try:
        fd.BETA_COLD=.80
        fd.DELTA_TILT=DELTA
        fd.CASES[.6]=(L,C,original[2])
        model=fd.DynamicForce(.6,quick=False,Tmax=1.02)
        M=covariance_matrix(model,.6,R,ALPHA,y_min=-22,y_max=22)
        target_x=math.sqrt(M[0,0])
        target_u=math.sqrt(M[1,1])
        _xc,_kap,wc=cold_phase_scale(model,.6)

        dim=cfg['dim']; npade=cfg['npade']; depth=cfg['depth']
        sigma0=math.sqrt(HBAR/(2*C*PHI_BAR**2*wc))
        a=destroy(dim); n=a.dag()*a
        xop=sigma0*(a+a.dag())
        uop=1j*sigma0*(a.dag()-a)
        H=n+0.5*qeye(dim)
        ct_phys=PHI_BAR**2/HBAR * G*WD/(2*math.sqrt(2))
        ct_scaled=ct_phys/wc
        H=H+ct_scaled*(xop*xop)

        cr,vr,ci,vi=pade_bath_expansion(wc,npade)
        bath=BosonicBath(xop,cr,vr,ci,vi,combine=True,tag='direct-port-pade')
        nexp=len(bath.exponents)
        nado=math.comb(nexp+depth,depth)
        vmax=max(abs(complex(e.vk)) for e in bath.exponents)
        print(f'CASE={name} dim={dim} Npade={npade} depth={depth} '
              f'nexp={nexp} nado_est={nado} vmax/wc={vmax:.6e}',flush=True)
        print(f'target_sigma_x={target_x:.10e} target_sigma_u={target_u:.10e} '
              f'ct/wc={ct_scaled:.10e}',flush=True)

        # Same equilibrium protocol as the Matsubara Gate-B probe.  A large
        # internal step allowance avoids confusing stiffness with a physical
        # hierarchy failure.
        tlist=np.array([0.,10.,20.,40.,60.,80.,100.,120.])
        solver=HEOMSolver(
            H,bath,max_depth=depth,
            options={
                'progress_bar':'',
                'store_states':True,
                'method':'bdf',
                'rtol':2e-7,
                'atol':2e-9,
                'nsteps':200000,
            },
        )
        t0=time.perf_counter()
        result=solver.run(fock_dm(dim,0),tlist,
                          e_ops=[xop,xop*xop,uop,uop*uop])
        runtime=time.perf_counter()-t0

        sx=[]; su=[]
        for i,tau in enumerate(tlist):
            xx,uu=widths(result.expect,i); sx.append(xx); su.append(uu)
            print(f'tau={tau:7.2f} sigma_x={xx:.10e} relx={xx/target_x-1:+.6e} '
                  f'sigma_u={uu:.10e} relu={uu/target_u-1:+.6e}',flush=True)

        rho=result.states[-1]
        tr=float(np.real(rho.tr()))
        eig=np.linalg.eigvalsh(rho.full())
        eigmin=float(eig.min())
        top=float(np.real(rho.diag()[-1]))
        relx=sx[-1]/target_x-1
        relu=su[-1]/target_u-1
        err=max(abs(relx),abs(relu))
        drift=max(abs(sx[-1]-sx[-2])/target_x,
                  abs(su[-1]-su[-2])/target_u)
        msg=(f'CASE={name} FINAL relx={relx:+.6e} relu={relu:+.6e} '
             f'max_cov_error={err:.6e} late_drift={drift:.6e} '
             f'trace={tr:.12f} eigmin={eigmin:.6e} topPop={top:.6e} '
             f'runtime_s={runtime:.3f}')
        print(msg,flush=True)
        print(f'::notice title=Experiment 03 deep Pade HEOM::{msg}',flush=True)

        # Gross per-job guards only; scientific convergence is assessed across
        # the completed matrix.  Do not suppress a mildly negative tier because
        # the sign/trend is the object being tested.
        if abs(tr-1)>5e-6:
            raise RuntimeError('trace failure')
        if drift>.02:
            raise RuntimeError('not equilibrated by tau=120')
        if eigmin < -5e-3:
            raise RuntimeError('gross density-matrix negativity')
        if err>.05:
            raise RuntimeError('gross exact-FDT miss')
        print('PASS_PROBE',flush=True)
    finally:
        fd.BETA_COLD=ob
        fd.DELTA_TILT=ot
        fd.CASES[.6]=original


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--case',choices=sorted(CASES),required=True)
    args=ap.parse_args()
    run_case(args.case)

if __name__=='__main__':
    main()
