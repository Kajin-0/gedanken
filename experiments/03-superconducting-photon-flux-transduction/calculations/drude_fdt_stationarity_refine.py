#!/usr/bin/env python3
"""Convergence refinement for the Drude quantum-FDT stationarity regression.

Separates finite-ensemble scatter from timestep/Nyquist and finite-prehistory
errors before pulse-time bath noise is allowed into the nonlinear latch model.
"""
from __future__ import annotations

import math
import numpy as np

from full_dynamic_rfsquid import CASES, DynamicForce
from finite_time_basin_slice import cold_phase_scale
from quantum_initial_capture import quantum_covariance
from drude_equilibrium_covariance import covariance_ratios
from drude_fdt_stationarity import synthesize_zeroT_current_noise, advance_harmonic


def one_case(dt_ps: float, pre_ns: float, n_total: int, seed: int=4321, batch: int=256):
    r=0.6; R0=250.0; d=5.0
    model=DynamicForce(r,quick=False)
    L,C,_=CASES[r]
    xc,kappa,omega0=cold_phase_scale(model,r)
    qcov=quantum_covariance(model,r); sigma=qcov['sigma_x']
    G0=1/R0; omegaD=d*omega0; tauD=1/omegaD
    g=G0/(C*omega0)
    target=covariance_ratios(g,d,qcov['q'])

    dt=dt_ps*1e-12
    nt=int(round(pre_ns*1e-9/dt))+1
    rng=np.random.default_rng(seed)
    sums=np.zeros(3); cross=np.zeros((3,3)); done=0
    while done<n_total:
        nb=min(batch,n_total-done)
        noise=synthesize_zeroT_current_noise(nb,nt,dt,G0,omegaD,rng)
        x=np.full(nb,xc); v=np.zeros(nb); j=np.zeros(nb)
        x,v,j=advance_harmonic(x,v,j,noise,dt,L,C,kappa,xc,G0,tauD)
        Y=np.column_stack(((x-xc)/sigma,v/(omega0*sigma),j/(G0*omega0*sigma)))
        sums+=Y.sum(axis=0); cross+=Y.T@Y; done+=nb
    mean=sums/n_total
    sample=(cross-n_total*np.outer(mean,mean))/(n_total-1)
    diag_rel=(np.diag(sample)-np.diag(target))/np.diag(target)
    rho_xj=sample[0,2]/math.sqrt(sample[0,0]*sample[2,2])
    rho_uj=sample[1,2]/math.sqrt(sample[1,1]*sample[2,2])
    trho_xj=target[0,2]/math.sqrt(target[0,0]*target[2,2])
    trho_uj=target[1,2]/math.sqrt(target[1,1]*target[2,2])
    msg=(f'dt={dt_ps:g}ps pre={pre_ns:g}ns N={n_total}: '
         f'diag_rel=[{diag_rel[0]:+.5f},{diag_rel[1]:+.5f},{diag_rel[2]:+.5f}], '
         f'rhoXJ={rho_xj:.5f} target={trho_xj:.5f}, '
         f'rhoUJ={rho_uj:.5f} target={trho_uj:.5f}, '
         f'maxdiag={np.max(np.abs(diag_rel)):.5f}')
    print(msg); print(f'::notice title=Experiment 03 FDT convergence::{msg}')
    return sample,target


def main():
    print('Experiment 03 Drude FDT stationarity convergence')
    # Same bandwidth with much larger ensemble.
    one_case(0.2,2.0,8192,seed=4321)
    # Nyquist/timestep refinement at same physical prehistory.
    one_case(0.1,2.0,8192,seed=4321)
    # Finite-prehistory stress at the refined timestep.
    one_case(0.1,4.0,4096,seed=9871)
    print('PASS')

if __name__=='__main__': main()
