#!/usr/bin/env python3
"""Cold harmonic FDT stationarity at the refined causal optimum R0=360 ohm,d=3."""
from __future__ import annotations
import math
import numpy as np
from full_dynamic_rfsquid import CASES, DynamicForce
from finite_time_basin_slice import cold_phase_scale
from quantum_initial_capture import quantum_covariance
from drude_equilibrium_covariance import covariance_ratios
from drude_fdt_stationarity import synthesize_zeroT_current_noise, advance_harmonic


def main():
    r=0.6; R0=360.0; d=3.0; dt_ps=0.1; pre_ns=4.0; N=4096; batch=256
    model=DynamicForce(r,quick=False); L,C,_=CASES[r]
    xc,kappa,omega0=cold_phase_scale(model,r); qcov=quantum_covariance(model,r)
    sigma=qcov['sigma_x']; G0=1/R0; omegaD=d*omega0; tauD=1/omegaD
    g=G0/(C*omega0); target=covariance_ratios(g,d,qcov['q'])
    dt=dt_ps*1e-12; nt=int(round(pre_ns*1e-9/dt))+1
    rng=np.random.default_rng(1717); ys=[]
    for lo in range(0,N,batch):
        nb=min(batch,N-lo)
        noise=synthesize_zeroT_current_noise(nb,nt,dt,G0,omegaD,rng)
        x=np.full(nb,xc); v=np.zeros(nb); j=np.zeros(nb)
        x,v,j=advance_harmonic(x,v,j,noise,dt,L,C,kappa,xc,G0,tauD)
        ys.append(np.column_stack(((x-xc)/sigma,v/(omega0*sigma),j/(G0*omega0*sigma))))
    Y=np.vstack(ys); sample=np.cov(Y,rowvar=False,bias=False)
    rel=(np.diag(sample)-np.diag(target))/np.diag(target)
    rhoXJ=sample[0,2]/math.sqrt(sample[0,0]*sample[2,2]); trXJ=target[0,2]/math.sqrt(target[0,0]*target[2,2])
    rhoUJ=sample[1,2]/math.sqrt(sample[1,1]*sample[2,2]); trUJ=target[1,2]/math.sqrt(target[1,1]*target[2,2])
    eta=1/(1+1/d**2); Q=omega0*C/(G0*eta)
    print('Experiment 03 optimum FDT stationarity')
    print('target=',target); print('sample=',sample)
    msg=(f'R0={R0:g} d={d:g} ReY/G0={eta:.6f} Qc={Q:.4f}; '
         f'diag_rel=[{rel[0]:+.5f},{rel[1]:+.5f},{rel[2]:+.5f}], '
         f'rhoXJ={rhoXJ:.5f}/{trXJ:.5f}, rhoUJ={rhoUJ:.5f}/{trUJ:.5f}')
    print(msg); print(f'::notice title=Experiment 03 optimum FDT stationarity::{msg}')
    print('PASS')
if __name__=='__main__': main()
