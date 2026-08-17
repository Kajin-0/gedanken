#!/usr/bin/env python3
"""Padé thermal-pole decomposition for the Experiment-03 direct port.

This is a bath-decomposition validation, not a detector calculation.

The exact direct-port force correlation is already represented by two circuit
poles plus a Matsubara ladder in direct_port_bath_correlation.py.  At low
T, the Matsubara representation is numerically expensive for HEOM because every
retained thermal exponential creates a hierarchy dimension.

Here the Matsubara ladder is replaced by the [N/N] Bose Padé spectrum
decomposition used by QuTiP 5.3's DrudeLorentzPadeBath, following
Hu et al., J. Chem. Phys. 134, 244106 (2011), DOI 10.1063/1.3602466.
The optimized pole locations epsilon_j and residues kappa_j depend only on the
Bose function.  Therefore they may be combined with the present rational
spectral density without changing J(omega).

For the present exact Matsubara thermal coefficient

    c(nu) = -2 G nu omega_D^4 / [beta (nu^4 + omega_D^4)],

the Padé replacement is

    nu_j = epsilon_j / (beta hbar),
    c_j  = kappa_j c(nu_j).

The physical circuit-pole residues are kept exact.  The implementation of
kappa/epsilon below is algebraically the same algorithm used in QuTiP 5.3's
DrudeLorentzEnvironment._kappa_epsilon; it is reproduced locally so the direct-
port decomposition is auditable and does not depend on a private runtime API.

Every order is checked against the independent oscillatory quadrature of the
defining correlation integral and against the converged Matsubara residue sum.
"""
from __future__ import annotations

import math
import numpy as np
from scipy.linalg import eigvalsh

from direct_port_bath_correlation import (
    HBAR, BETA, G, WD, bath_poles, bath_coeff, corr_quad, corr_series,
)


def _delta(i: int, j: int) -> float:
    return 1.0 if i == j else 0.0


def pade_kappa_epsilon(N: int) -> tuple[np.ndarray, np.ndarray]:
    """Return positive [N/N] Bose Padé residues and dimensionless poles."""
    if N < 1:
        return np.array([], float), np.array([], float)

    alpha = np.diag([
        1.0 / math.sqrt((2*k + 5)*(2*k + 3))
        for k in range(2*N - 1)
    ], k=1)
    alpha = alpha + alpha.T
    evals = eigvalsh(alpha)
    eps = np.array([-2.0 / val for val in evals[:N]], dtype=float)

    if N == 1:
        chi = np.array([], dtype=float)
    else:
        alpha_p = np.diag([
            1.0 / math.sqrt((2*k + 7)*(2*k + 5))
            for k in range(2*N - 2)
        ], k=1)
        alpha_p = alpha_p + alpha_p.T
        ep = eigvalsh(alpha_p)
        chi = np.array([-2.0 / val for val in ep[:N-1]], dtype=float)

    kappas=[]
    prefactor = 0.5 * N * (2*(N+1) + 1)
    for j in range(N):
        term = prefactor
        for k in range(N-1):
            term *= ((chi[k]**2 - eps[j]**2) /
                     (eps[k]**2 - eps[j]**2 + _delta(j,k)))
        k=N-1
        term /= (eps[k]**2 - eps[j]**2 + _delta(j,k))
        kappas.append(term)
    return np.asarray(kappas, float), eps


def pade_terms(N: int) -> list[tuple[float, float]]:
    kappa, eps = pade_kappa_epsilon(N)
    out=[]
    for kap, ep in zip(kappa, eps):
        nu = ep/(BETA*HBAR)
        c = kap * (-2*G*nu*WD**4/(BETA*(nu**4 + WD**4)))
        out.append((float(c), float(nu)))
    return out


def corr_pade(t: float, N: int) -> complex:
    out=0j
    for p in bath_poles():
        out += bath_coeff(p)*np.exp(-1j*p*t)
    for c,nu in pade_terms(N):
        out += c*math.exp(-nu*t)
    return out


def coth_pade(x: float, N: int) -> float:
    """Padé Bose coth approximation implied by the optimized poles."""
    if abs(x) < 1e-12:
        return 2.0/x if x != 0 else math.inf
    kappa, eps = pade_kappa_epsilon(N)
    return 2.0/x + 4.0*x*sum(
        kap/(x*x + ep*ep) for kap,ep in zip(kappa,eps)
    )


def main():
    print('Experiment 03 direct-port Bose-Pade decomposition')
    print(f'T={1/(BETA*1.380649e-23):.9f} K wd/2pi={WD/(2*math.pi)*1e-9:.9f} GHz')

    times_ps=(0., .2, .5, 1., 2., 5., 10., 20., 50., 100.)
    exact={tp: corr_quad(tp*1e-12) for tp in times_ps}
    # Cross-check the independent integral against the previously validated
    # high-order Matsubara series so a quadrature accident cannot select N.
    mref={tp: corr_series(tp*1e-12, 10000) for tp in times_ps}
    qxm=max(abs(mref[tp]-exact[tp])/max(abs(exact[tp]),1e-300)
            for tp in times_ps)
    print(f'quad_vs_M10000_maxrel={qxm:.6e}')

    summaries=[]
    for N in (1,2,3,4,5,6,8):
        terms=pade_terms(N)
        print(f'PADE N={N}:')
        for j,(c,nu) in enumerate(terms,1):
            print(f'  j={j:2d} nu/2pi={nu/(2*math.pi)*1e-9:.9f}GHz c={c:.12e}')
        errs=[]
        for tp in times_ps:
            val=corr_pade(tp*1e-12,N)
            ref=exact[tp]
            e=abs(val-ref)/max(abs(ref),1e-300)
            errs.append(e)
            print(f'  t={tp:6.1f}ps relerr={e:.6e} '
                  f'C=({val.real:.9e}{val.imag:+.9e}j)')
        # t >= 20 ps is the optical-rise-and-later metric used by the direct
        # port bath checkpoint; t=0 is kept separately because any finite-pole
        # Bose approximation is least accurate in the UV.
        late=max(e for tp,e in zip(times_ps,errs) if tp>=20.)
        pulse=max(e for tp,e in zip(times_ps,errs) if tp>=1.)
        summaries.append((N,errs[0],pulse,late))
        print(f'  SUMMARY N={N} err_t0={errs[0]:.6e} '
              f'max_t_ge_1ps={pulse:.6e} max_t_ge_20ps={late:.6e}')

    # Direct Bose-function check over a broad frequency interval.  This is a
    # deliberately harsher metric than the weighted correlation because the
    # direct-port spectral density is already strongly suppressed at the high
    # end of the interval.
    for N in (2,3,4,6,8):
        bmax=0.0
        for fGHz in np.geomspace(.05,40.,200):
            w=2*math.pi*fGHz*1e9
            x=BETA*HBAR*w
            exact_c=1/math.tanh(x/2)
            approx=coth_pade(x,N)
            bmax=max(bmax,abs(approx-exact_c)/abs(exact_c))
        print(f'BOSE N={N} maxrel_0p05_to_40GHz={bmax:.6e}')

    # Strict decomposition certification uses N=8.  Lower orders N=4--6 are
    # retained only as controlled HEOM convergence candidates and must be
    # judged against the exact FDT covariance in the harmonic Gate-B sweep.
    n8=next(s for s in summaries if s[0]==8)
    if qxm > 5e-5:
        raise RuntimeError('independent quadrature / Matsubara reference mismatch')
    if n8[3] > 2e-6:
        raise RuntimeError('N=8 Padé decomposition insufficient after 20 ps')
    if n8[2] > 5e-5:
        raise RuntimeError('N=8 Padé decomposition insufficient after 1 ps')
    print('PASS')

if __name__=='__main__':
    main()
