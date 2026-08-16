#!/usr/bin/env python3
"""Exact pole/Matsubara decomposition of the UV-regular Experiment-03 port bath.

The phase flux q=Phi_bar*x obeys the generalized Langevin form

    C qddot + K q + (Y * qdot) = I_N,

with the two-sided symmetrized quantum FDT convention

    S_I^sym(omega)
      = hbar |omega| coth(beta hbar |omega|/2) ReY(omega).

For the current two-pole positive-real port

    ReY(omega) = G/[1+(omega/omega_D)^4],   G=1/R,

it is convenient to define the odd dissipative function

    J(omega) = hbar G omega omega_D^4/(omega^4+omega_D^4).

Then the unsymmetrized equilibrium force correlation for t>0 is

    C_I(t)=<I_N(t) I_N(0)>
          = (1/pi) int_0^inf dω J(ω)
            [coth(beta hbar ω/2) cos(ωt) - i sin(ωt)].

Equivalently,

    C_I(t)=sum_k c_k exp(-gamma_k t),

with two complex circuit-pole terms plus real Matsubara terms.  This script
validates the residue formulas against independent oscillatory quadrature and
quantifies plain-Matsubara truncation error on the 0-400 ps pulse timescale.

This is the correlation decomposition needed by HEOM / influence-functional
methods.  It avoids introducing the UV-divergent momentum of an explicit ideal-
Ohmic reaction coordinate.
"""
from __future__ import annotations

import math
import numpy as np
from scipy.integrate import quad

HBAR=1.054571817e-34
KB=1.380649e-23
T0=.020
R=7.5308506
FC=1.9844267e9
ALPHA=.90
WD=2*math.pi*ALPHA*FC
G=1/R
BETA=1/(KB*T0)


def coth(z: float) -> float:
    if z < 1e-6:
        return 1/z + z/3
    if z > 30:
        return 1.0
    return 1/math.tanh(z)


def J(w: float) -> float:
    return HBAR*G*w*WD**4/(w**4+WD**4)


def bath_poles():
    # Lower-half-plane roots of z^4 + WD^4 = 0, appropriate for t>0.
    return (WD*np.exp(-1j*math.pi/4), WD*np.exp(-3j*math.pi/4))


def bath_coeff(p: complex) -> complex:
    # C(t)=(1/pi) int_R dz J(z)/(1-exp(-beta hbar z)) exp(-izt),
    # closed clockwise in the lower half plane -> -2i times residues.
    return -1j*HBAR*G*WD**4/(2*p**2)/(1-np.exp(-BETA*HBAR*p))


def matsubara(n: int) -> float:
    return 2*math.pi*n/(BETA*HBAR)


def mats_coeff(n: int) -> float:
    nu=matsubara(n)
    return -2*G*nu*WD**4/(BETA*(nu**4+WD**4))


def corr_series(t: float, nmats: int) -> complex:
    out=0j
    for p in bath_poles():
        out += bath_coeff(p)*np.exp(-1j*p*t)
    for n in range(1,nmats+1):
        out += mats_coeff(n)*math.exp(-matsubara(n)*t)
    return out


def corr_quad(t: float) -> complex:
    """Independent dimensionless oscillatory quadrature of the defining integral."""
    def reamp(x):
        w=WD*x
        return J(w)*coth(BETA*HBAR*w/2)*WD/math.pi
    def imamp(x):
        w=WD*x
        return J(w)*WD/math.pi
    if t == 0:
        re=quad(reamp,0,np.inf,epsabs=1e-28,epsrel=3e-10,limit=1000)[0]
        return complex(re,0.)
    wt=WD*t
    re=quad(reamp,0,np.inf,weight='cos',wvar=wt,
            epsabs=1e-27,epsrel=2e-8,limlst=500,maxp1=200)[0]
    im=-quad(imamp,0,np.inf,weight='sin',wvar=wt,
             epsabs=1e-27,epsrel=2e-8,limlst=500,maxp1=200)[0]
    return complex(re,im)


def greater_spectrum(w: float) -> float:
    # Full two-sided unsymmetrized spectrum S^>(omega). For either sign,
    # Jodd/(1-exp(-beta hbar omega)) is positive.
    if abs(w)<1e-30:
        return 2*G/BETA
    j=HBAR*G*w*WD**4/(w**4+WD**4)
    return 2*j/(1-math.exp(-BETA*HBAR*w))


def main():
    nu1=matsubara(1)
    a=WD/math.sqrt(2)
    print(f'T0={T0:.6f}K R={R:.7f}ohm fc={FC*1e-9:.7f}GHz '
          f'wd/2pi={WD/(2*math.pi)*1e-9:.7f}GHz')
    print(f'nu1/2pi={nu1/(2*math.pi)*1e-9:.7f}GHz nu1/wd={nu1/WD:.9f} '
          f'tau_M1={1/nu1*1e12:.6f}ps bath_pole_decay_tau={1/a*1e12:.6f}ps')
    for j,p in enumerate(bath_poles(),1):
        c=bath_coeff(p); gam=1j*p
        print(f'circuit{j}: gamma=({gam.real:.9e}{gam.imag:+.9e}j)/s '
              f'c=({c.real:.9e}{c.imag:+.9e}j)')

    times_ps=(0.,1.,5.,20.,50.,100.,200.,400.)
    max_ind=0.
    print('independent quadrature versus 512-Matsubara residue series:')
    for tp in times_ps:
        t=tp*1e-12
        cq=corr_quad(t); cs=corr_series(t,512)
        err=abs(cs-cq)/max(abs(cq),1e-300); max_ind=max(max_ind,err)
        print(f't={tp:7.1f}ps Cquad=({cq.real:.9e}{cq.imag:+.9e}j) '
              f'Cseries=({cs.real:.9e}{cs.imag:+.9e}j) relerr={err:.3e}')

    # Use a very long Matsubara sum as the truncation reference; n^-3 coefficients
    # make this straightforward and the exponential suppresses the tail for t>0.
    tref=(0.,1.,5.,20.,50.,100.)
    for N in (2,4,8,16,32,64):
        errs=[]
        for tp in tref:
            ref=corr_series(tp*1e-12,10000)
            val=corr_series(tp*1e-12,N)
            errs.append(abs(val-ref)/max(abs(ref),1e-300))
        print(f'Nmat={N:3d}: ' + ' '.join(f'err@{tp:g}ps={e:.3e}' for tp,e in zip(tref,errs)))

    # Exact KMS/detailed-balance check in frequency space.
    dbmax=0.
    for fGHz in (.25,.5,1.,2.,4.,8.,16.):
        w=2*math.pi*fGHz*1e9
        sp=greater_spectrum(w); sm=greater_spectrum(-w)
        expected=math.exp(-BETA*HBAR*w)
        ratio=sm/sp
        rel=abs(ratio-expected)/max(expected,1e-300); dbmax=max(dbmax,rel)
        print(f'detailed_balance f={fGHz:5.2f}GHz S(-w)/S(+w)={ratio:.9e} '
              f'exp(-beta hbar w)={expected:.9e} relerr={rel:.3e}')

    # Explicit metric relevant to the 20-ps optical rise: N=16 is already
    # essentially converged after one rise time, but not at t=0.
    ref0=corr_series(0.,10000); ref20=corr_series(20e-12,10000)
    e0=abs(corr_series(0.,16)-ref0)/abs(ref0)
    e20=abs(corr_series(20e-12,16)-ref20)/abs(ref20)
    msg=(f'direct-port decomposition: nu1/wd={nu1/WD:.4f}; tauM1={1/nu1*1e12:.2f}ps; '
         f'N16_relerr_t0={e0:.3e}; N16_relerr_20ps={e20:.3e}; '
         f'independent_quad_maxerr={max_ind:.3e}; detailed_balance_maxerr={dbmax:.3e}')
    print(msg); print(f'::notice title=Experiment 03 direct-port bath correlation::{msg}')
    if max_ind>5e-5: raise RuntimeError('analytic bath correlation failed independent quadrature')
    if dbmax>2e-12: raise RuntimeError('detailed balance failed')
    if e20>2e-6: raise RuntimeError('16-term Matsubara decomposition insufficient at 20 ps')
    print('PASS')

if __name__=='__main__': main()
