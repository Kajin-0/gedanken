#!/usr/bin/env python3
"""Eigenspectrum-level harmonic HEOM benchmark for Experiment-03 Gate B.

Second moments alone can hide small unphysical eigenvalues in a truncated HEOM
state.  For the exact linear direct-port problem the reduced one-mode state is
Gaussian.  Its density-operator eigenvalues are therefore fixed by the
symplectic eigenvalue of the exact FDT covariance, independent of squeezing:

    nu = sqrt(det V) / sigma0^2 = 2 nbar + 1,
    p_n = (1-q) q^n,  q = nbar/(nbar+1).

Here sigma0 is the isolated-oscillator vacuum width in the same x,u convention,
[x,u]=2 i sigma0^2.  The exact FDT covariance has <{x,u}>/2=0 in the current
linear network, so sqrt(det V)=sigma_x sigma_u.

The script reruns selected already-converged Padé HEOM points, captures the final
reduced state, and compares its *full sorted eigenvalue spectrum* against this
basis-independent exact Gaussian ladder.  It reports total negative mass and a
spectral L1 discrepancy without clipping or projecting the HEOM state.

This is a method-validation diagnostic only.  It does not authorize nonlinear
or finite-pulse detector HEOM.
"""
from __future__ import annotations

import argparse
import math
import numpy as np

import full_dynamic_rfsquid as fd
from finite_time_basin_slice import cold_phase_scale
from quantum_initial_capture import PHI_BAR
from two_pole_joint_covariance import covariance_matrix
import heom_harmonic_pade_depth as base


CASES = {
    # Deepest completed hierarchy at the economical Padé order.
    "p4d7_spec": dict(dim=8, npade=4, depth=7),
    # Independent enlarged Hilbert basis at the depth-5 frontier.
    "p5d5_dim10_spec": dict(dim=10, npade=5, depth=5),
}


_BaseSolver = base.HEOMSolver


class CaptureSolver(_BaseSolver):
    last_result = None

    def run(self, *args, **kwargs):
        result = super().run(*args, **kwargs)
        CaptureSolver.last_result = result
        return result


def exact_gaussian_spectrum(dim: int):
    """Return exact FDT Gaussian eigenvalues and symplectic occupation."""
    ob, ot = fd.BETA_COLD, fd.DELTA_TILT
    original = fd.CASES[.6]
    try:
        fd.BETA_COLD = .80
        fd.DELTA_TILT = base.DELTA
        fd.CASES[.6] = (base.L, base.C, original[2])
        model = fd.DynamicForce(.6, quick=False, Tmax=1.02)
        V = covariance_matrix(model, .6, base.R, base.ALPHA,
                              y_min=-22, y_max=22)
        target_x = math.sqrt(V[0, 0])
        target_u = math.sqrt(V[1, 1])
        _xc, _kap, wc = cold_phase_scale(model, .6)
        sigma0 = math.sqrt(base.HBAR / (2 * base.C * PHI_BAR**2 * wc))
        nu = target_x * target_u / (sigma0 * sigma0)
        nbar = 0.5 * (nu - 1.0)
        q = nbar / (nbar + 1.0)
        p = np.array([(1.0 - q) * q**n for n in range(dim)], dtype=float)
        tail = q**dim
        return p, tail, nbar, q, sigma0, target_x, target_u
    finally:
        fd.BETA_COLD = ob
        fd.DELTA_TILT = ot
        fd.CASES[.6] = original


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--case', choices=sorted(CASES), required=True)
    args = ap.parse_args()
    cfg = CASES[args.case]

    base.CASES[args.case] = cfg
    base.HEOMSolver = CaptureSolver
    base.run_case(args.case)
    if CaptureSolver.last_result is None:
        raise RuntimeError('failed to capture HEOM result')

    rho = CaptureSolver.last_result.states[-1]
    raw = np.linalg.eigvalsh(rho.full())
    heom = np.sort(np.real(raw))[::-1]
    exact, exact_tail, nbar, q, sigma0, sx, su = exact_gaussian_spectrum(cfg['dim'])

    neg_mass = float(np.sum(np.maximum(-heom, 0.0)))
    # Include the exact probability beyond the finite Hilbert dimension.  It is
    # tiny here, but makes this a comparison to the infinite Gaussian spectrum.
    spectral_l1 = float(np.sum(np.abs(heom - exact)) + exact_tail)
    spectral_tv = 0.5 * spectral_l1
    occupied_mask = exact >= 1e-6
    occupied_abs = float(np.max(np.abs(heom[occupied_mask] - exact[occupied_mask])))
    occupied_rel = float(np.max(
        np.abs(heom[occupied_mask] - exact[occupied_mask]) / exact[occupied_mask]
    ))

    print(f'EXACT sigma0={sigma0:.12e} sigma_x={sx:.12e} sigma_u={su:.12e}')
    print(f'EXACT symplectic_ratio={2*nbar+1:.12e} nbar={nbar:.12e} q={q:.12e} '
          f'tail_beyond_dim={exact_tail:.12e}')
    print('rank exact_p heom_eig abs_error rel_error')
    for i, (pe, ph) in enumerate(zip(exact, heom)):
        ae = abs(ph - pe)
        re = ae / pe if pe > 0 else math.nan
        print(f'{i:2d} {pe:.12e} {ph:+.12e} {ae:.12e} {re:.12e}')

    msg = (f'CASE={args.case} SPECTRUM FINAL negative_mass={neg_mass:.12e} '
           f'spectral_L1={spectral_l1:.12e} spectral_TV={spectral_tv:.12e} '
           f'occupied_max_abs={occupied_abs:.12e} '
           f'occupied_max_rel={occupied_rel:.12e} '
           f'eigmin={float(np.min(raw)):.12e}')
    print(msg)
    print(f'::notice title=Experiment 03 HEOM exact-Gaussian eigenspectrum::{msg}')

    # Diagnostic guards only.  The strict Gate-B disposition is made from the
    # full convergence record, not by silently accepting a chosen tail floor.
    if abs(float(np.trace(rho.full()).real) - 1.0) > 5e-6:
        raise RuntimeError('trace failure')
    if spectral_tv > 5e-3:
        raise RuntimeError('gross HEOM/exact-Gaussian spectral mismatch')
    print('PASS_DIAGNOSTIC')


if __name__ == '__main__':
    main()
