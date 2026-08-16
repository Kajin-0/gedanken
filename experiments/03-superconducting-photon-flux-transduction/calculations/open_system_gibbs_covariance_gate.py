#!/usr/bin/env python3
"""UV-safe test of a weak-coupling bare-Gibbs open-system closure.

The cold linear circuit has exact symmetrized quantum-FDT covariances. A standard
weak-coupling Davies model of the residual resistor bath would instead relax the
*bare coupled phase+filter Hamiltonian* to its Gibbs state.

The explicit filter momentum/voltage variable `s=ydot/omega_c` is NOT included in
the quantitative mismatch norm: with an ideal Ohmic resistor its zero-point
variance diverges logarithmically with the residual-bath UV cutoff. That boundary
is separately certified by `reaction_coordinate_uv_cutoff_gate.py`.

This script therefore compares only the cutoff-independent moments

    [x, y=psi/Phi_bar, u=xdot/omega_c]

plus the coordinate correlation rho_xy. A material filter-coordinate mismatch is
a static strong-coupling/mean-force warning even before time-dependent driving.
"""
from __future__ import annotations
import math
import numpy as np

import full_dynamic_rfsquid as fd
from causal_two_pole_environment import filter_components
from finite_time_basin_slice import cold_phase_scale
from quantum_initial_capture import HBAR, KB, PHI_BAR
from two_pole_joint_covariance import covariance_matrix

L=111.5e-12; C=24.262211e-12; R=7.5308506; DELTA=.212; ALPHA=.90


def coth(x):
    if x>30: return 1.0
    return 1/math.tanh(x)


def bare_gibbs(model):
    _xc,kappa,wc=cold_phase_scale(model,.6)
    wd=ALPHA*wc; Lf,Cf=filter_components(R,wd)
    K=np.array([[kappa/L+1/Lf,-1/Lf],[-1/Lf,1/Lf]],float)
    M=np.diag([C,Cf]); Mi2=np.diag(1/np.sqrt(np.diag(M)))
    Om2=Mi2@K@Mi2
    val,E=np.linalg.eigh(Om2); wn=np.sqrt(val)
    vz=np.array([HBAR/(2*w)*coth(HBAR*w/(2*KB*fd.T0)) for w in wn])
    vv=np.array([HBAR*w/2*coth(HBAR*w/(2*KB*fd.T0)) for w in wn])
    Q=(Mi2@E@np.diag(vz)@E.T@Mi2)/(PHI_BAR**2)
    V=(Mi2@E@np.diag(vv)@E.T@Mi2)/(PHI_BAR**2*wc**2)
    G=np.zeros((4,4)); G[:2,:2]=Q; G[2:,2:]=V
    return G,wn,Lf,Cf,wc


def exact_fdt(model,Lf):
    M=covariance_matrix(model,.6,R,ALPHA,y_min=-22,y_max=22)
    a=Lf/L
    T=np.array([[1,0,0,0],[1,0,-a,0],[0,1,0,0],[0,0,0,1]],float)
    return T@M@T.T


def main():
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT; original=fd.CASES[.6]
    try:
        fd.BETA_COLD=.80; fd.DELTA_TILT=DELTA; fd.CASES[.6]=(L,C,original[2])
        model=fd.DynamicForce(.6,quick=False,Tmax=1.02)
        G,wn,Lf,Cf,wc=bare_gibbs(model)
        F=exact_fdt(model,Lf)
        labels=['x','y','u']
        relsig=[]
        print(f'delta=.212 C={C*1e12:.6f}pF R={R:.7f}ohm alpha={ALPHA:.2f} '
              f'normal_f=({wn[0]/(2*math.pi)*1e-9:.7f},{wn[1]/(2*math.pi)*1e-9:.7f})GHz')
        for i,l in enumerate(labels):
            sg=math.sqrt(max(G[i,i],0)); sf=math.sqrt(max(F[i,i],0))
            r=(sf-sg)/max(sf,sg); relsig.append(abs(r))
            print(f'{l}: sigma_bareGibbs={sg:.9e} sigma_exactFDT={sf:.9e} rel_sigma={r:+.6e}')
        rg=G[0,1]/math.sqrt(G[0,0]*G[1,1]); rf=F[0,1]/math.sqrt(F[0,0]*F[1,1])
        print(f'rho_xy: bareGibbs={rg:+.9f} exactFDT={rf:+.9f} delta={rf-rg:+.6e}')
        # Compare the UV-safe [x,y,u] principal block only.
        idx=np.array([0,1,2]); Fs=F[np.ix_(idx,idx)]; Gs=G[np.ix_(idx,idx)]
        frob=np.linalg.norm(Fs-Gs)/np.linalg.norm(Fs)
        print(f'UV_safe_covariance_relative_frobenius={frob:.9e} '
              f'max_UV_safe_sigma_relative={max(relsig):.9e}')
        print(f'NOTE: s=ydot/omega_c is excluded because ideal-Ohmic Var(s) is UV divergent; '
              f'historical sigma_s(ymax=22)={math.sqrt(F[3,3]):.9e} is not physical.')
        msg=(f'delta=.212: UVsafe exactFDT_vs_bareGibbs_frobenius={frob:.5f}; '
             f'max_sigma_relative={max(relsig):.5f}; '
             f'sigx_rel={relsig[0]:.5f}; sigy_rel={relsig[1]:.5f}; sigu_rel={relsig[2]:.5f}; '
             f'rho_xy_delta={rf-rg:+.5e}')
        print(msg); print(f'::notice title=Experiment 03 UV-safe bare-Gibbs covariance gate::{msg}')
        if np.linalg.eigvalsh(Fs).min()<=0 or np.linalg.eigvalsh(Gs).min()<=0:
            raise RuntimeError('non-positive UV-safe covariance block')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot; fd.CASES[.6]=original

if __name__=='__main__': main()
