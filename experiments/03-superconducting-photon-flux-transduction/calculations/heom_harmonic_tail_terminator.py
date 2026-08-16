#!/usr/bin/env python3
"""Custom Matsubara-tail terminator control for Experiment-03 Gate B.

The direct-port correlation is known analytically as two complete circuit-pole
terms plus real Matsubara terms c_n exp(-nu_n t).  For a truncation after N,
the omitted fast-correlation discrepancy in the dimensionless HEOM units is

    delta_N = sum_{n>N} c_n' / nu_n',

where c_n' and nu_n' are the same coefficients/exponents passed to QuTiP.
QuTiP's system_terminator(Q, delta) represents an omitted correlation
2*delta*delta(t).  No Drude parameters are imported: delta_N is computed from
this project's actual analytic Matsubara series.

This is an independent Gate-B control.  It does not alter the concurrently
running plain-Matsubara hierarchy-depth test.
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
from direct_port_bath_correlation import mats_coeff, matsubara
from heom_harmonic_port_validation import (
    HBAR, R, G, WD, L, C, DELTA, ALPHA, bath_expansion,
)

from qutip import destroy, qeye, fock_dm, liouvillian
from qutip.core.environment import system_terminator
from qutip.solver.heom import BosonicBath, HEOMSolver

CASES = {
    "n8d3t":  (8, 3),
    "n16d2t": (16, 2),
    "n16d3t": (16, 3),
}


def tail_delta(nmats: int, wc: float, nmax: int = 200000) -> float:
    cscale = (PHI_BAR/HBAR)**2/(wc*wc)
    out = 0.0
    for n in range(nmats + 1, nmax + 1):
        out += (mats_coeff(n)*cscale)/(matsubara(n)/wc)
    # Remaining tail is O(n^-4) termwise => O(nmax^-3), negligible here.
    return float(out)


def width(expect, i):
    x, x2, u, u2 = (float(np.real(v[i])) for v in expect)
    return (math.sqrt(max(x2-x*x, 0.0)),
            math.sqrt(max(u2-u*u, 0.0)))


def run(name: str):
    nmats, depth = CASES[name]
    dim = 10
    ob, ot = fd.BETA_COLD, fd.DELTA_TILT
    original = fd.CASES[.6]
    try:
        fd.BETA_COLD=.80; fd.DELTA_TILT=DELTA
        fd.CASES[.6]=(L,C,original[2])
        model=fd.DynamicForce(.6,quick=False,Tmax=1.02)
        M=covariance_matrix(model,.6,R,ALPHA,y_min=-22,y_max=22)
        tx=math.sqrt(M[0,0]); tu=math.sqrt(M[1,1])
        _xc,_kappa,wc=cold_phase_scale(model,.6)

        sigma0=math.sqrt(HBAR/(2*C*PHI_BAR**2*wc))
        a=destroy(dim); n=a.dag()*a
        xop=sigma0*(a+a.dag()); uop=1j*sigma0*(a.dag()-a)
        H=n+0.5*qeye(dim)
        ct_phys=PHI_BAR**2/HBAR*G*WD/(2*math.sqrt(2))
        H=H+(ct_phys/wc)*(xop*xop)

        cr,vr,ci,vi=bath_expansion(wc,nmats)
        bath=BosonicBath(xop,cr,vr,ci,vi,combine=True,tag='direct-port')
        delta=tail_delta(nmats,wc)
        HL=liouvillian(H)+system_terminator(xop,delta)
        print(f'CASE={name} dim={dim} nmats={nmats} depth={depth} '
              f'nexp={len(bath.exponents)} tail_delta={delta:.12e}',flush=True)

        solver=HEOMSolver(HL,bath,max_depth=depth,
            options={'progress_bar':'','store_states':True,'method':'bdf',
                     'rtol':2e-7,'atol':2e-9})
        tlist=np.array([0.,10.,20.,40.,60.,80.,100.,120.])
        t0=time.perf_counter()
        res=solver.run(fock_dm(dim,0),tlist,
                       e_ops=[xop,xop*xop,uop,uop*uop])
        runtime=time.perf_counter()-t0
        vals=[width(res.expect,i) for i in range(len(tlist))]
        for tau,(sx,su) in zip(tlist,vals):
            print(f'tau={tau:7.2f} sigma_x={sx:.10e} relx={sx/tx-1:+.6e} '
                  f'sigma_u={su:.10e} relu={su/tu-1:+.6e}',flush=True)
        sx,su=vals[-1]; sx0,su0=vals[-2]
        rho=res.states[-1]
        relx=sx/tx-1; relu=su/tu-1
        err=max(abs(relx),abs(relu))
        drift=max(abs(sx-sx0)/tx,abs(su-su0)/tu)
        tr=float(np.real(rho.tr()))
        eigmin=float(np.linalg.eigvalsh(rho.full()).min())
        top=float(np.real(rho.diag()[-1]))
        msg=(f'CASE={name} TERMINATED FINAL relx={relx:+.6e} relu={relu:+.6e} '
             f'max_cov_error={err:.6e} late_drift={drift:.6e} trace={tr:.12f} '
             f'eigmin={eigmin:.6e} topPop={top:.6e} delta={delta:.6e} '
             f'runtime_s={runtime:.3f}')
        print(msg,flush=True)
        print(f'::notice title=Experiment 03 custom-tail HEOM::{msg}',flush=True)
        if abs(tr-1)>5e-6: raise RuntimeError('trace failure')
        if drift>.03: raise RuntimeError('not equilibrated')
        print('PASS_CONTROL',flush=True)
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot; fd.CASES[.6]=original


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--case',choices=sorted(CASES),required=True)
    run(ap.parse_args().case)

if __name__=='__main__': main()
