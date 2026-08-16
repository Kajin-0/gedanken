#!/usr/bin/env python3
"""Cold harmonic equilibrium variances for a causal one-pole Drude bath.

Use Fourier convention exp(-i omega t) and

    Y(omega)=G0/(1-i omega/omega_D).

For q=Phi_bar*x, the linearized cold equation is

    C qddot + int Y(t-t') qdot(t') dt' + K q = I_N,

with K=C*omega0^2 and quantum FDT

    S_I^sym(omega)=hbar |omega| coth(hbar|omega|/2kT) Re Y(omega).

The one-pole rolloff makes both coordinate and velocity variances finite,
unlike the infinite-bandwidth Ohmic limit whose velocity variance diverges
logarithmically.  Results are normalized to the isolated harmonic oscillator
variance at the same bare omega0.
"""
from __future__ import annotations

import math
from scipy.integrate import quad

from full_dynamic_rfsquid import CASES, DynamicForce
from quantum_initial_capture import quantum_covariance, HBAR, KB, T0


def coth_stable(z: float) -> float:
    if z < 1e-6:
        return 1.0/z + z/3.0
    if z > 25.0:
        return 1.0
    return 1.0/math.tanh(z)


def variance_ratios(g: float, d: float, a: float) -> tuple[float,float]:
    """Return (q variance ratio, qdot variance ratio).

    g=G0/(C omega0)=1/(R0 C omega0), d=omega_D/omega0,
    a=hbar omega0/(2kT).
    """
    coth_a=coth_stable(a)

    def pieces(y: float) -> tuple[float,float]:
        s=math.exp(y)
        r=s/d
        lp=1.0/(1.0+r*r)
        # D/(C omega0^2) = 1-s^2-i*s*Y/(C omega0)
        # Y/(C omega0)=g*(1+i*r)/(1+r^2)
        re=1.0-s*s + g*s*r*lp
        im=-g*s*lp
        den=re*re+im*im
        c=coth_stable(a*s)
        # Original ds integrand is s*c*lp/den. ds=s dy.
        base=s*s*c*lp/den
        return base, s*s*base

    iq=quad(lambda y: pieces(y)[0],-24.0,24.0,epsabs=1e-10,epsrel=2e-8,limit=800)[0]
    iv=quad(lambda y: pieces(y)[1],-24.0,24.0,epsabs=1e-10,epsrel=2e-8,limit=800)[0]
    pref=2.0*g/(math.pi*coth_a)
    return pref*iq,pref*iv


def report(r_delta: float,R0: float,ds: tuple[float,...]) -> None:
    model=DynamicForce(r_delta,quick=False)
    cov=quantum_covariance(model,r_delta)
    _,C,_=CASES[r_delta]
    omega0=cov['omega_c']
    a=HBAR*omega0/(2.0*KB*T0)
    g=1.0/(R0*C*omega0)
    for d in ds:
        rq,rv=variance_ratios(g,d,a)
        reY_ratio=1.0/(1.0+(1.0/d)**2)  # ReY(omega0)/G0
        msg=(f"rDelta={r_delta:.1f}, R0={R0:g} ohm, omegaD/omega0={d:g}: "
             f"ReYwc/G0={reY_ratio:.6f}, var_x/isolated={rq:.6f}, "
             f"var_v/isolated={rv:.6f}, sigma_x={cov['sigma_x']*math.sqrt(rq):.6f} rad")
        print(msg)
        print(f"::notice title=Experiment 03 Drude bath variance::{msg}")


def main():
    print('Experiment 03 causal Drude-bath cold covariance')
    report(0.6,250.0,(2.0,5.0,10.0,20.0))
    report(0.8,600.0,(2.0,5.0,10.0,20.0))
    print('PASS')

if __name__=='__main__':
    main()
