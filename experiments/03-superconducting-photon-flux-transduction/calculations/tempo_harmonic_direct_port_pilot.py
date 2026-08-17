#!/usr/bin/env python3
"""Independent direct-port TEMPO harmonic pilot for Experiment 03.

This is the first non-hierarchy test of the actual direct-port bath.  It is a
small dim=4 pilot only; it does not replace harmonic Gate B or promote nonlinear
Gate C.1.

Physics is held fixed relative to the accepted harmonic HEOM benchmark:
  * same harmonic phase Hamiltonian and physical counterterm;
  * same two exact circuit poles + N=4 Padé thermal correlation terms;
  * same dimensionless tau=omega_c t convention;
  * same exact finite-basis squeezed-thermal Gaussian/FDT reference.

OQuPy TEMPO begins from a factorized system-bath state.  The system is therefore
initialized in the oscillator vacuum and allowed to relax.  The coupled exact
FDT state is an asymptotic oracle, not a t=0 expectation.  The script reports
late-time state error and drift; no clipping or positivity repair is applied.
"""
from __future__ import annotations

import math
import numpy as np
from scipy.linalg import svdvals
import oqupy
from qutip import basis

import heom_fp_harmonic_oracle as fp
import heom_harmonic_final_state_gate as finalgate

DIM=4
NPADE=4
DT=0.20
TCUT=8.0
TEND=32.0
EPSREL=1e-8


def correlation_factory(d,z):
    d=np.asarray(d,complex); z=np.asarray(z,complex)
    def corr(tau):
        a=np.asarray(tau)
        # Build positive-time C and use C(-t)=C(t)* for a Hermitian bath.
        ap=np.abs(a)
        cp=np.zeros_like(ap,dtype=complex)
        for dk,zk in zip(d,z):
            cp += dk*np.exp(-zk*ap)
        return np.where(a>=0,cp,np.conj(cp))
    return corr


def moments(rho,op):
    m=np.trace(rho@op)
    m2=np.trace(rho@op@op)
    var=float(np.real(m2-m*m))
    return float(np.real(m)),math.sqrt(max(var,0.0))


def metrics(rho,ref):
    x=np.asarray(ref['xop'].full(),complex)
    u=np.asarray(ref['uop'].full(),complex)
    exact=np.asarray(ref['rho'].full(),complex)
    _mx,sx=moments(rho,x); _mu,su=moments(rho,u)
    relx=sx/ref['target_x']-1.0
    relu=su/ref['target_u']-1.0
    herm=np.linalg.norm(rho-rho.conj().T,ord='fro')/max(np.linalg.norm(rho,ord='fro'),1e-300)
    tr=np.trace(rho)
    eig=np.linalg.eigvalsh(0.5*(rho+rho.conj().T))
    neg=float(np.sum(np.maximum(-eig,0.0)))
    eigmin=float(eig.min())
    delta=rho-exact
    half=0.5*float(np.sum(svdvals(delta)))
    return dict(sx=sx,su=su,relx=relx,relu=relu,herm=herm,tr=tr,
                eigmin=eigmin,neg=neg,half=half,
                frob=float(np.linalg.norm(delta,ord='fro')))


def main():
    wc,xop,uop,H,d,z,ref=fp.harmonic_setup(DIM,NPADE)
    print(f"TEMPO_HARMONIC_PILOT dim={DIM} Npade={NPADE} dt={DT} tcut={TCUT} "
          f"tend={TEND} epsrel={EPSREL:.1e} wc/2pi={wc/(2*math.pi)*1e-9:.9f}GHz",flush=True)
    print(f"REFERENCE basis_err={ref['basis_err']:.12e} sx={ref['sx']:.12e} su={ref['su']:.12e} "
          f"target_x={ref['target_x']:.12e} target_u={ref['target_u']:.12e}",flush=True)
    for k,(dk,zk) in enumerate(zip(d,z)):
        print(f"MODE {k:02d} d=({dk.real:+.12e}{dk.imag:+.12e}j) z=({zk.real:+.12e}{zk.imag:+.12e}j)",flush=True)

    h=np.asarray(H.full(),complex)
    q=np.asarray(xop.full(),complex)
    rho0=np.asarray((basis(DIM,0)*basis(DIM,0).dag()).full(),complex)
    system=oqupy.System(h)
    correlations=oqupy.CustomCorrelations(correlation_function=correlation_factory(d,z))
    bath=oqupy.Bath(q,correlations)
    pars=oqupy.TempoParameters(dt=DT,tcut=TCUT,epsrel=EPSREL)
    dyn=oqupy.tempo_compute(system=system,bath=bath,initial_state=rho0,
                            start_time=0.0,end_time=TEND,parameters=pars,
                            unique=True,progress_type='silent')
    times=np.asarray(dyn.times,float)
    states=np.asarray(dyn.states,complex)
    sample_targets=[0.0,4.0,8.0,16.0,24.0,32.0]
    for tt in sample_targets:
        j=int(np.argmin(np.abs(times-tt)))
        m=metrics(states[j],ref)
        print(f"SAMPLE tau={times[j]:.6f} relx={m['relx']:+.9e} relu={m['relu']:+.9e} "
              f"half={m['half']:.9e} neg={m['neg']:.3e} trace=({m['tr'].real:.9e}{m['tr'].imag:+.2e}j)",flush=True)

    mf=metrics(states[-1],ref)
    # Late drift over the last quarter of the trajectory in density-matrix Frobenius norm.
    jlate=int(np.argmin(np.abs(times-0.75*TEND)))
    late_drift=float(np.linalg.norm(states[-1]-states[jlate],ord='fro'))
    maxfdt=max(abs(mf['relx']),abs(mf['relu']))
    print(f"FINAL maxFDT={maxfdt:.12e} half_nuclear={mf['half']:.12e} frob={mf['frob']:.12e} "
          f"negmass={mf['neg']:.12e} eigmin={mf['eigmin']:+.12e} anti={mf['herm']:.12e} "
          f"trace=({mf['tr'].real:.12e}{mf['tr'].imag:+.2e}j) late_drift={late_drift:.12e}",flush=True)
    msg=(f"TEMPO_HARMONIC_PILOT basis_err={ref['basis_err']:.3e} maxFDT={maxfdt:.3e} "
         f"half={mf['half']:.3e} neg={mf['neg']:.3e} late_drift={late_drift:.3e}")
    print(msg,flush=True)
    print(f"::notice title=Experiment 03 direct-port TEMPO harmonic pilot::{msg}",flush=True)
    if abs(mf['tr']-1)>1e-8 or mf['herm']>1e-8:
        raise RuntimeError('TEMPO harmonic pilot lost trace or Hermiticity')
    # Pilot-only sanity guard.  Exact Gate-B thresholds are NOT imposed at dim4.
    if maxfdt>0.10 or mf['half']>0.10:
        raise RuntimeError('TEMPO harmonic pilot grossly disagrees with exact FDT state')
    print('PASS_TEMPO_HARMONIC_PILOT_SANITY')

if __name__=='__main__': main()
