#!/usr/bin/env python3
"""Independent TEMPO interface/units audit for Experiment 03.

This is a fallback-solver validation, not a detector calculation.  It uses the
same analytically soluble real-exponential pure-dephasing problem used to audit
the FP-HEOM implementation:

    C(t) = d exp(-Gamma t), d=0.2, Gamma=1,
    H=0, q=diag(0,1), rho01(0)=1/2.

Exact:
    rho01(t)=1/2 exp[-d/Gamma^2 (Gamma t - 1 + exp(-Gamma t))].

OQuPy TEMPO is supplied the correlation directly through CustomCorrelations.
Two time steps are compared at fixed full-history tcut and tight tensor SVD
tolerance.  The purpose is to validate the dimensionless correlation/coupling
convention before any direct-port bath is used.

If both grids already agree with the analytic solution below a declared
numerical-floor threshold, monotonic timestep improvement is not required:
roundoff/tensor-contraction noise can reorder ~1e-13 errors.  Outside that floor
regime, refinement must reduce the analytic error.
"""
from __future__ import annotations

import math
import numpy as np
import oqupy

D=0.2
GAMMA=1.0
TEND=5.0
NUMERICAL_FLOOR=1e-9


def exact(t):
    phi=D/(GAMMA*GAMMA)*(GAMMA*t-1.0+math.exp(-GAMMA*t))
    return 0.5*math.exp(-phi)


def run(dt):
    H=np.zeros((2,2),complex)
    q=np.diag([0.0,1.0]).astype(complex)
    rho0=np.array([[0.5,0.5],[0.5,0.5]],complex)
    system=oqupy.System(H)
    def corr(tau):
        tau_arr=np.asarray(tau)
        # Equilibrium Hermitian bath convention C(-t)=C(t)*; here C is real.
        return D*np.exp(-GAMMA*np.abs(tau_arr))
    correlations=oqupy.CustomCorrelations(correlation_function=corr)
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
    print(f"TEMPO dt={dt:.6f} steps={len(times)-1} maxrel={max(errs):.12e} "
          f"at_t={times[imax]:.6f} finalrel={errs[-1]:.12e} "
          f"maxherm={max(herm):.12e} maxtrace={max(trerr):.12e}",flush=True)
    return max(errs),errs[-1],max(herm),max(trerr)


def main():
    coarse=run(0.10)
    fine=run(0.05)
    ratio=fine[0]/coarse[0] if coarse[0]>0 else 0.0
    floor_regime=(coarse[0] < NUMERICAL_FLOOR and fine[0] < NUMERICAL_FLOOR)
    print(f"TEMPO_CONVERGENCE coarse={coarse[0]:.12e} fine={fine[0]:.12e} "
          f"ratio={ratio:.6f} numerical_floor={floor_regime}",flush=True)
    print(f"::notice title=Experiment 03 TEMPO analytic self-test::coarse={coarse[0]:.3e} fine={fine[0]:.3e} ratio={ratio:.3f} floor={floor_regime}")
    if fine[0] > 3e-4:
        raise RuntimeError('fine TEMPO pure-dephasing error exceeds audit tolerance')
    if (not floor_regime) and fine[0] >= coarse[0]:
        raise RuntimeError('TEMPO timestep refinement did not improve analytic error outside numerical floor')
    if floor_regime:
        print(f"TEMPO_NUMERICAL_FLOOR threshold={NUMERICAL_FLOOR:.1e}",flush=True)
    if fine[2] > 1e-10 or fine[3] > 1e-10:
        raise RuntimeError('TEMPO lost Hermiticity or trace in analytic audit')
    print('PASS_TEMPO_IMPLEMENTATION_AUDIT')

if __name__=='__main__': main()
