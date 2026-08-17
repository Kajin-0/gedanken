#!/usr/bin/env python3
"""Complex-correlation TEMPO interface audit for Experiment 03.

This is an independent fallback-solver validation, not a detector calculation.
It exercises OQuPy CustomCorrelations with a genuinely complex exponential,
matching the convention needed for the two direct-port circuit poles.

For t>=0:
    C(t) = d exp(-z t),
with d=0.20+0.07i and z=1.10+0.40i, Re z>0.  For negative times the
Hermitian-bath equilibrium continuation C(-t)=C(t)* is supplied explicitly.
For H=0, q=diag(0,1), the exact rho01 coherence is

    rho01(t) = rho01(0) exp[-F*(t)],
    F(t)=d/z^2 [z t - 1 + exp(-z t)].

Two timesteps are checked.  As in the real-correlation audit, if both are below
a declared numerical floor, monotonic refinement is not required because the
remaining error is roundoff/tensor-contraction noise.
"""
from __future__ import annotations

import numpy as np
import oqupy

D=0.20+0.07j
Z=1.10+0.40j
TEND=5.0
NUMERICAL_FLOOR=1e-9


def exact(t):
    zz=np.conj(Z); dd=np.conj(D)
    F=dd/(zz*zz)*(zz*t-1.0+np.exp(-zz*t))
    return 0.5*np.exp(-F)


def correlation(tau):
    a=np.asarray(tau)
    pos=D*np.exp(-Z*a)
    neg=np.conj(D*np.exp(-Z*(-a)))
    return np.where(a>=0,pos,neg)


def run(dt):
    H=np.zeros((2,2),complex)
    q=np.diag([0.0,1.0]).astype(complex)
    rho0=np.array([[0.5,0.5],[0.5,0.5]],complex)
    system=oqupy.System(H)
    correlations=oqupy.CustomCorrelations(correlation_function=correlation)
    bath=oqupy.Bath(q,correlations)
    pars=oqupy.TempoParameters(dt=dt,tcut=TEND,epsrel=1e-10)
    dyn=oqupy.tempo_compute(system=system,bath=bath,initial_state=rho0,
                            start_time=0.0,end_time=TEND,
                            parameters=pars,unique=True,
                            progress_type='silent')
    times=np.asarray(dyn.times,float)
    states=np.asarray(dyn.states,complex)
    errs=[]; herm=[]; trerr=[]
    for t,rho in zip(times,states):
        ex=exact(float(t)); got=rho[0,1]
        errs.append(abs(got-ex)/max(abs(ex),1e-300))
        herm.append(np.linalg.norm(rho-rho.conj().T,ord='fro'))
        trerr.append(abs(np.trace(rho)-1.0))
    imax=int(np.argmax(errs))
    print(f"TEMPO_COMPLEX dt={dt:.6f} steps={len(times)-1} maxrel={max(errs):.12e} "
          f"at_t={times[imax]:.6f} finalrel={errs[-1]:.12e} "
          f"maxherm={max(herm):.12e} maxtrace={max(trerr):.12e}",flush=True)
    return max(errs),errs[-1],max(herm),max(trerr)


def main():
    coarse=run(0.10)
    fine=run(0.05)
    ratio=fine[0]/coarse[0] if coarse[0]>0 else 0.0
    floor=(coarse[0]<NUMERICAL_FLOOR and fine[0]<NUMERICAL_FLOOR)
    print(f"TEMPO_COMPLEX_CONVERGENCE coarse={coarse[0]:.12e} fine={fine[0]:.12e} "
          f"ratio={ratio:.6f} numerical_floor={floor}",flush=True)
    print(f"::notice title=Experiment 03 TEMPO complex analytic self-test::coarse={coarse[0]:.3e} fine={fine[0]:.3e} ratio={ratio:.3f} floor={floor}")
    if fine[0] > 3e-4:
        raise RuntimeError('fine complex TEMPO error exceeds audit tolerance')
    if (not floor) and fine[0] >= coarse[0]:
        raise RuntimeError('complex TEMPO timestep refinement did not improve outside numerical floor')
    if fine[2] > 1e-10 or fine[3] > 1e-10:
        raise RuntimeError('complex TEMPO lost Hermiticity or trace')
    if floor:
        print(f"TEMPO_COMPLEX_NUMERICAL_FLOOR threshold={NUMERICAL_FLOOR:.1e}",flush=True)
    print('PASS_TEMPO_COMPLEX_IMPLEMENTATION_AUDIT')

if __name__=='__main__': main()
