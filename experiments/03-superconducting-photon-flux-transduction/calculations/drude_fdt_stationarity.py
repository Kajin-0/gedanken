#!/usr/bin/env python3
"""Stationarity regression for a stochastic quantum-FDT Drude representation.

Goal
----
Before adding pulse-time environmental fluctuations to nonlinear capture, verify
that a classical Gaussian process with the *symmetrized* quantum-FDT spectrum,
used as a Wigner/truncated-Wigner stochastic representation, reproduces the
known cold harmonic Drude covariance.

The physical current-noise convention is

    <I(t)I(0)>_sym = int dω/(2π) S_I(ω) exp(-iωt)

with the T_b -> 0 best-case spectrum

    S_I(ω)=hbar |ω| Re Y(ω),
    Y(ω)=G0/(1-iω/ωD).

For q=Phi_bar*x, the dimensionless phase equation is

    L C xddot + L j + kappa (x-xc) = L I_N/Phi_bar
    tauD jdot + j = G0 xdot.

A long harmonic pre-run under one continuous colored-noise record automatically
builds the system/noise correlations.  The final ensemble covariance in

    X=(x-xc)/sigma_x0,
    U=xdot/(omega0 sigma_x0),
    J=j/(G0 omega0 sigma_x0)

is compared against the spectral covariance from drude_equilibrium_covariance.

This regression does NOT make nonlinear stochastic propagation quantum exact;
it only verifies that the chosen symmetrized-noise representation has the right
linear stationary limit at the chosen numerical bandwidth.
"""
from __future__ import annotations

import math
import numpy as np

from full_dynamic_rfsquid import CASES, DynamicForce
from finite_time_basin_slice import cold_phase_scale
from quantum_initial_capture import quantum_covariance, HBAR, PHI_BAR
from drude_equilibrium_covariance import covariance_ratios


def synthesize_zeroT_current_noise(ntraj: int, nt: int, dt: float,
                                   G0: float, omegaD: float,
                                   rng: np.random.Generator) -> np.ndarray:
    """Real Gaussian records with the two-sided sym quantum-FDT PSD.

    For f>0 the corresponding one-sided Hz PSD is
        P1(f)=2*S_omega(2*pi*f).
    NumPy irfft coefficients are normalized so that integrating P1 df gives
    the time-domain variance over the represented band.
    """
    freqs=np.fft.rfftfreq(nt,dt)
    omega=2.0*math.pi*freqs
    reY=G0/(1.0+(omega/omegaD)**2)
    Somega=HBAR*omega*reY
    P1=2.0*Somega
    df=1.0/(nt*dt)
    nk=len(freqs)
    spec=np.zeros((ntraj,nk),dtype=np.complex128)
    if nk>2:
        sig=nt*np.sqrt(P1[1:-1]*df)/2.0
        spec[:,1:-1]=(rng.normal(size=(ntraj,nk-2))+1j*rng.normal(size=(ntraj,nk-2)))*sig
    # At T=0 the DC limit is zero.  Set Nyquist to zero to avoid a special-bin
    # convention; its omission vanishes under dt convergence.
    return np.fft.irfft(spec,n=nt,axis=1)


def advance_harmonic(x,v,j,noise,dt,L,C,kappa,xc,G0,tauD):
    """Vectorized RK4 with piecewise-linear noise interpolation."""
    nt=noise.shape[1]
    for k in range(nt-1):
        n1=noise[:,k]/PHI_BAR
        n4=noise[:,k+1]/PHI_BAR
        n2=0.5*(n1+n4)

        def rhs(xx,vv,jj,nn):
            return vv, -(jj + (kappa/L)*(xx-xc) - nn)/C, (G0*vv-jj)/tauD

        kx1,kv1,kj1=rhs(x,v,j,n1)
        kx2,kv2,kj2=rhs(x+0.5*dt*kx1,v+0.5*dt*kv1,j+0.5*dt*kj1,n2)
        kx3,kv3,kj3=rhs(x+0.5*dt*kx2,v+0.5*dt*kv2,j+0.5*dt*kj2,n2)
        kx4,kv4,kj4=rhs(x+dt*kx3,v+dt*kv3,j+dt*kj3,n4)
        x=x+dt*(kx1+2*kx2+2*kx3+kx4)/6.0
        v=v+dt*(kv1+2*kv2+2*kv3+kv4)/6.0
        j=j+dt*(kj1+2*kj2+2*kj3+kj4)/6.0
    return x,v,j


def run(dt_ps=0.2,pre_ns=2.0,n_total=2048,batch=256,seed=1234):
    r=0.6; R0=250.0; d=5.0
    model=DynamicForce(r,quick=False)
    L,C,_=CASES[r]
    xc,kappa,omega0=cold_phase_scale(model,r)
    qcov=quantum_covariance(model,r)
    sigma=qcov['sigma_x']
    G0=1.0/R0; omegaD=d*omega0; tauD=1.0/omegaD
    g=G0/(C*omega0)
    target=covariance_ratios(g,d,qcov['q'])

    dt=dt_ps*1e-12
    nt=int(round(pre_ns*1e-9/dt))+1
    rng=np.random.default_rng(seed)
    finals=[]
    done=0
    while done<n_total:
        nb=min(batch,n_total-done)
        noise=synthesize_zeroT_current_noise(nb,nt,dt,G0,omegaD,rng)
        x=np.full(nb,xc); v=np.zeros(nb); j=np.zeros(nb)
        x,v,j=advance_harmonic(x,v,j,noise,dt,L,C,kappa,xc,G0,tauD)
        X=(x-xc)/sigma
        U=v/(omega0*sigma)
        J=j/(G0*omega0*sigma)
        finals.append(np.column_stack((X,U,J)))
        done+=nb
    Y=np.vstack(finals)
    sample=np.cov(Y,rowvar=False,bias=False)
    rel=(sample-target)/np.where(np.abs(target)>1e-12,np.abs(target),1.0)
    print('Experiment 03 Drude FDT stationarity regression')
    print(f'dt={dt_ps:g} ps pre={pre_ns:g} ns N={n_total} Nyquist={0.5/dt/1e9:.1f} GHz')
    print('target covariance:')
    print(target)
    print('sample covariance:')
    print(sample)
    print('relative diagonal errors:',np.diag(rel))
    print('target rhoXJ=',target[0,2]/math.sqrt(target[0,0]*target[2,2]))
    print('sample rhoXJ=',sample[0,2]/math.sqrt(sample[0,0]*sample[2,2]))
    print('target rhoUJ=',target[1,2]/math.sqrt(target[1,1]*target[2,2]))
    print('sample rhoUJ=',sample[1,2]/math.sqrt(sample[1,1]*sample[2,2]))
    max_diag=float(np.max(np.abs(np.diag(rel))))
    msg=f'max_abs_diagonal_relative_error={max_diag:.4f}'
    print(msg); print(f'::notice title=Experiment 03 Drude FDT stationarity::{msg}')
    # This is a Monte-Carlo regression, so use a loose failure threshold; later
    # dt/N convergence, not this one threshold, determines scientific acceptance.
    if max_diag>0.15:
        raise RuntimeError('stationary covariance regression failed badly')
    print('PASS')


if __name__=='__main__':
    run()
