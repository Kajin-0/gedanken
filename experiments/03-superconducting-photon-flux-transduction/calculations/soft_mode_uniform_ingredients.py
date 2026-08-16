#!/usr/bin/env python3
"""Extract uniform-crossover ingredients for Experiment 03.

Near the second-order thermal/quantum crossover the static sphaleron has a
degenerate n=1 cosine/sine Matsubara pair.  Time-translation symmetry makes the
leading reduced action rotationally invariant in this soft plane,

    Bred = Bsph + 1/2 lambda1 rho^2 + 1/4 g4 rho^4 + ...,
    rho^2 = q_c^2 + q_s^2.

For lambda1<0 the periodic instanton is the broken-symmetry ring
rho0^2=-lambda1/g4 and

    DeltaB = Bsph-Binst = lambda1^2/(4 g4).

Hence z=lambda1/(2 sqrt(g4))=-sqrt(DeltaB) on the instanton side.  The exact
quartic soft-plane integral contains the complementary-error-function structure
that appears in rigorous uniform instanton asymptotics.  This script only
extracts/validates the normal-form ingredients; it does NOT claim that the
simple quartic integral alone is the complete physical escape rate.
"""
from __future__ import annotations
import argparse, math
import numpy as np
from scipy.special import erfc

import full_dynamic_rfsquid as fd
import finiteT_nonlocal_periodic_bounce_v2 as ft2
import finiteT_one_loop_rate_manifold as rm
from R80_dissipative_bounce_screen import Y_laplace
from quantum_initial_capture import HBAR, KB, PHI_BAR

L0=111.5e-12
RPTS={
    .210:9.825701561,
    .211:10.18791311,
    .212:10.62175909,
    .213:11.19986413,
    .214:11.49729617,  # closest scanned periodic point, not a rate root
}


def sph_soft_lambda(st,T):
    """Dimensionless-action Hessian eigenvalue of either normalized n=1 soft mode."""
    P=HBAR*st['wc']/(KB*T)
    k1=2*math.pi/P
    nu=st['wc']*k1
    Ak=st['C']*PHI_BAR**2*st['wc']/HBAR
    Av=(PHI_BAR**2/L0)/(HBAR*st['wc'])
    # In an orthonormal cosine/sine mode the kinetic and environment pieces are
    # independent of the P/2 raw coefficient norm after division by that norm.
    return Ak*k1*k1 + (PHI_BAR**2/HBAR)*k1*float(Y_laplace(nu,st['R'],st['wd'])) + Av*st['Fs']


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--delta',type=float,required=True); a=ap.parse_args()
    d=round(a.delta,3)
    if d not in RPTS: raise SystemExit(f'unsupported delta={d}')
    r=RPTS[d]
    s=rm.rate_state(d,r,64,8192)
    if s['kind']!='periodic': raise RuntimeError('expected periodic instanton')
    st=s['st']; B=float(s['B']); Bsph=st['barrierK']/fd.T0
    gap=Bsph-B
    lam=sph_soft_lambda(st,fd.T0)
    if not (gap>0 and lam<0): raise RuntimeError(f'expected below-crossover gap>0, lambda<0; gap={gap}, lambda={lam}')
    g4=lam*lam/(4*gap)
    z=lam/(2*math.sqrt(g4))
    z_gap=-math.sqrt(gap)
    # This is the instanton-side erfc factor multiplying the isolated instanton
    # term in a simple quartic soft-plane uniformization.  A complete uniform
    # rate also contains the companion sphaleron/transition-state term.
    w_inst=.5*erfc(z)
    msg=(f'delta={d:.3f} r={r:.9f} Binst={B:.9f} Bsph={Bsph:.9f} '
         f'DeltaB={gap:.9f} lambda1={lam:+.9e} g4_eff={g4:.9e} '
         f'z_direct={z:+.9f} z_from_gap={z_gap:+.9f} '
         f'half_erfc_z={w_inst:.9f} T0/Tx={fd.T0/s["Tx"]:.9f}')
    print(msg); print(f'::notice title=Experiment 03 soft-mode normal form::{msg}')
    if abs(z-z_gap)>2e-9: raise RuntimeError('normal-form identity z=-sqrt(DeltaB) failed')
    print('CAUTION: half_erfc_z is only the instanton-side uniform weight, not the full uniform escape rate.')
    print('PASS')

if __name__=='__main__': main()
