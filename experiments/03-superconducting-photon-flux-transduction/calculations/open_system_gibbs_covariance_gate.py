#!/usr/bin/env python3
"""Test whether a weak-coupling bare-Gibbs open-system closure is credible.

The validated linear cold circuit has an exact symmetrized quantum-FDT covariance
for the augmented phase/filter variables. A standard weak-coupling Davies model
of the residual resistor bath would instead relax the *bare coupled phase+filter
Hamiltonian* to its Gibbs state.

This script compares those two stationary Gaussian covariances at the certified
`.212` operating point. A material discrepancy is a static mean-force/strong-
coupling warning: a master equation whose stationary state is bare Gibbs cannot
be used as a quantitatively controlled final quantum-capture model.

Coordinates compared:

    r = [x, y=psi/Phi_bar, u=xdot/omega_c, s=ydot/omega_c].

The exact FDT covariance is transformed from the existing augmented variables
[x,u,d,s], where y=x-(Lf/L)d.
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
    xc,kappa,wc=cold_phase_scale(model,.6)
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
    M=covariance_matrix(model,.6,R,ALPHA)
    # Original ordering [x,u,d,s]. Transform to [x,y,u,s], y=x-a*d.
    a=Lf/L
    T=np.array([[1,0,0,0],[1,0,-a,0],[0,1,0,0],[0,0,0,1]],float)
    return T@M@T.T


def rel(a,b):
    scale=max(abs(a),abs(b),1e-30)
    return (a-b)/scale


def main():
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT; original=fd.CASES[.6]
    try:
        fd.BETA_COLD=.80; fd.DELTA_TILT=DELTA; fd.CASES[.6]=(L,C,original[2])
        model=fd.DynamicForce(.6,quick=False,Tmax=1.02)
        G,wn,Lf,Cf,wc=bare_gibbs(model)
        F=exact_fdt(model,Lf)
        labels=['x','y','u','s']
        print(f'delta=.212 C={C*1e12:.6f}pF R={R:.7f}ohm alpha={ALPHA:.2f} '
              f'normal_f=({wn[0]/(2*math.pi)*1e-9:.7f},{wn[1]/(2*math.pi)*1e-9:.7f})GHz')
        max_var=0.
        for i,l in enumerate(labels):
            sg=math.sqrt(max(G[i,i],0)); sf=math.sqrt(max(F[i,i],0))
            r=(sf-sg)/max(sf,sg)
            max_var=max(max_var,abs(r))
            print(f'{l}: sigma_bareGibbs={sg:.9e} sigma_exactFDT={sf:.9e} rel_sigma={r:+.6e}')
        for i,j,name in [(0,1,'rho_xy'),(2,3,'rho_us')]:
            rg=G[i,j]/math.sqrt(G[i,i]*G[j,j]); rf=F[i,j]/math.sqrt(F[i,i]*F[j,j])
            print(f'{name}: bareGibbs={rg:+.9f} exactFDT={rf:+.9f} delta={rf-rg:+.6e}')
        frob=np.linalg.norm(F-G)/np.linalg.norm(F)
        evalF=np.linalg.eigvalsh(F); evalG=np.linalg.eigvalsh(G)
        print(f'covariance_relative_frobenius={frob:.9e} max_sigma_relative={max_var:.9e} '
              f'eigmin_exact={evalF.min():.9e} eigmin_gibbs={evalG.min():.9e}')
        msg=(f'delta=.212: exactFDT_vs_bareGibbs_frobenius={frob:.5f}; '
             f'max_sigma_relative={max_var:.5f}; '
             f'rho_xy_exact={F[0,1]/math.sqrt(F[0,0]*F[1,1]):+.5f}; '
             f'rho_us_exact={F[2,3]/math.sqrt(F[2,2]*F[3,3]):+.5f}')
        print(msg); print(f'::notice title=Experiment 03 bare-Gibbs covariance gate::{msg}')
        if evalF.min()<=0 or evalG.min()<=0: raise RuntimeError('non-positive covariance')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot; fd.CASES[.6]=original

if __name__=='__main__': main()
