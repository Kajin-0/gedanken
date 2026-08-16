#!/usr/bin/env python3
"""State-consistent exact closed-system quantum quench benchmark.

Purpose
-------
Compare exact one-dimensional Schrodinger evolution with classical Hamiltonian
propagation of the *same thermal harmonic initial state* in a controlled fixed-hot
nonlinear rf-SQUID quench:

    cold local harmonic thermal state
    -> instantaneous quench to fixed hot nonlinear potential
    -> no damping, no cooling.

The classical side samples the exact positive thermal harmonic Wigner Gaussian.
The quantum side therefore must NOT use one pure Gaussian whose position width
contains the finite-T coth factor: such a state has minimum uncertainty and does
not have the thermal momentum variance.  Instead this version propagates the
thermal harmonic density operator as a Boltzmann mixture of oscillator Fock
states,

    rho = (1-z) sum_n z^n |n><n|,   z=exp[-hbar omega/(k_B T0)].

The observable is probability to lie right of the retained hot saddle.  This is
still NOT final detector capture probability: damping, cooling and basin
reformation are absent.
"""
from __future__ import annotations
import argparse, math
import numpy as np
from scipy.integrate import cumulative_trapezoid

from full_dynamic_rfsquid import CASES, DynamicForce, T0
from quantum_initial_capture import quantum_covariance
from quench_energy_bound import quench_temperature

HBAR=1.054571817e-34; KB=1.380649e-23
H=6.62607015e-34; E_CHARGE=1.602176634e-19
PHI0=H/(2*E_CHARGE); PHIBAR=PHI0/(2*np.pi)


def hot_saddle(model,T):
    s=[x for x,k in model.roots(T) if k<0]
    if not s: raise ValueError('No hot saddle at requested T')
    return min(s,key=abs)


def potential_on_grid(model,T,x,L):
    F=np.asarray([model.force(T,float(xx)) for xx in x])
    u=cumulative_trapezoid(F,x,initial=0.0)
    return (PHIBAR*PHIBAR/L)*u


def thermal_harmonic_states(model,r_delta,x,tail_tol=1e-12):
    """Return normalized harmonic Fock states and exact thermal weights."""
    L,C,_=CASES[r_delta]; cov=quantum_covariance(model,r_delta)
    omega=cov['omega_c']; xc=cov['x_c']
    a=math.sqrt(HBAR/(C*PHIBAR**2*omega))
    z=math.exp(-HBAR*omega/(KB*T0))
    if z<=0: nstate=1
    else: nstate=max(1,int(math.ceil(math.log(tail_tol)/math.log(z))))
    nstate=min(max(nstate,4),24)
    y=(x-xc)/a
    psi0=np.exp(-0.5*y*y)/(math.pi**0.25*math.sqrt(a))
    states=[psi0.astype(complex)]
    if nstate>1: states.append((math.sqrt(2)*y*psi0).astype(complex))
    for n in range(1,nstate-1):
        nxt=math.sqrt(2/(n+1))*y*states[n]-math.sqrt(n/(n+1))*states[n-1]
        states.append(nxt.astype(complex))
    dx=x[1]-x[0]
    for j in range(len(states)):
        states[j]/=math.sqrt(float(np.sum(np.abs(states[j])**2)*dx))
    weights=(1-z)*z**np.arange(nstate,dtype=float)
    omitted=z**nstate
    weights/=weights.sum()
    return np.stack(states,axis=0),weights,cov,z,omitted


def exact_quantum(model,r_delta,Thot,*,xmax,nx,dt_ps,tmax_ps,sample_ps):
    L,C,_=CASES[r_delta]; m=C*PHIBAR*PHIBAR
    x=np.linspace(-xmax,xmax,nx,endpoint=False); dx=x[1]-x[0]
    psi,w,cov,z,omitted=thermal_harmonic_states(model,r_delta,x)
    U=potential_on_grid(model,Thot,x,L); saddle=hot_saddle(model,Thot)
    k=2*np.pi*np.fft.fftfreq(nx,d=dx); p=HBAR*k
    dt=dt_ps*1e-12; Vh=np.exp(-.5j*U*dt/HBAR); K=np.exp(-1j*(p*p/(2*m))*dt/HBAR)
    target={int(round(t/dt_ps)):t for t in sample_ps}; nsteps=int(round(tmax_ps/dt_ps)); out={}
    for step in range(1,nsteps+1):
        psi*=Vh[None,:]
        psi=np.fft.ifft(np.fft.fft(psi,axis=1)*K[None,:],axis=1)
        psi*=Vh[None,:]
        if step in target:
            pn=np.sum(np.abs(psi[:,x>saddle])**2,axis=1)*dx
            out[target[step]]=float(np.dot(w,pn))
    norms=np.sum(np.abs(psi)**2,axis=1)*dx
    return out,float(np.max(np.abs(norms-1))),cov,z,omitted,len(w)


def classical_wigner(model,r_delta,Thot,*,dt_ps,tmax_ps,sample_ps,nsamp,seed):
    L,C,_=CASES[r_delta]; cov=quantum_covariance(model,r_delta); rng=np.random.default_rng(seed)
    x=cov['x_c']+cov['sigma_x']*rng.standard_normal(nsamp)
    v=cov['sigma_v']*rng.standard_normal(nsamp); saddle=hot_saddle(model,Thot); dt=dt_ps*1e-12
    xforce=model.xgrid; fforce=np.asarray([model.force(Thot,float(xx)) for xx in xforce])
    def force_vec(xx): return np.interp(xx,xforce,fforce,left=fforce[0],right=fforce[-1])
    target={int(round(t/dt_ps)):t for t in sample_ps}; nsteps=int(round(tmax_ps/dt_ps)); out={}
    a=-force_vec(x)/(L*C)
    for step in range(1,nsteps+1):
        x=x+v*dt+.5*a*dt*dt; anew=-force_vec(x)/(L*C); v=v+.5*(a+anew)*dt; a=anew
        if step in target: out[target[step]]=float(np.mean(x>saddle))
    return out


def benchmark_case(r_delta,offset_K,quick):
    model=DynamicForce(r_delta,quick=quick); Tq,Tf=quench_temperature(model); Thot=min(Tq+offset_K,Tf-.005)
    if Thot<=Tq: raise RuntimeError('hot benchmark temperature is not above quench threshold')
    if quick: nx,dt_ps,nsamp=1024,.02,30000
    else: nx,dt_ps,nsamp=2048,.01,120000
    sample_ps=[5.,10.,20.,30.,40.]; xmax=5.5
    pq,normerr,cov,z,omitted,nstate=exact_quantum(model,r_delta,Thot,xmax=xmax,nx=nx,dt_ps=dt_ps,
                                                  tmax_ps=max(sample_ps),sample_ps=sample_ps)
    pc=classical_wigner(model,r_delta,Thot,dt_ps=dt_ps,tmax_ps=max(sample_ps),sample_ps=sample_ps,
                        nsamp=nsamp,seed=12345+int(100*r_delta))
    print(f'rDelta={r_delta:.1f}; Tq={Tq:.4f}K; Tf={Tf:.4f}K; Thot={Thot:.4f}K; '
          f'sigma_x_thermal={cov["sigma_x"]:.5f}; z={z:.6e}; nstate={nstate}; omittedThermalWeight={omitted:.3e}; maxNormErr={normerr:.3e}')
    maxdiff=0.
    for t in sample_ps:
        diff=pq[t]-pc[t]; maxdiff=max(maxdiff,abs(diff))
        msg=(f'rDelta={r_delta:.1f}, t={t:.0f}ps: P_right_quantumThermal={pq[t]:.6f}, '
             f'P_right_TWA={pc[t]:.6f}, delta={diff:+.6f}')
        print(msg); print(f'::notice title=Experiment 03 state-consistent quantum quench::{msg}')
    print(f'MAX_ABS_DELTA={maxdiff:.6f}\n')
    if normerr>2e-9: raise RuntimeError('unitary norm drift too large')
    if omitted>1e-10: raise RuntimeError('thermal Fock truncation too large')


def main():
    p=argparse.ArgumentParser(); p.add_argument('--quick',action='store_true'); p.add_argument('--offset-K',type=float,default=.030); a=p.parse_args()
    print('Experiment 03 state-consistent exact closed-system quantum quench benchmark')
    print('Observable: P[x>hot saddle]; fixed hot potential; no damping/cooling.\n')
    for r in (.8,.6): benchmark_case(r,a.offset_K,a.quick)
    print('PASS')

if __name__=='__main__': main()
