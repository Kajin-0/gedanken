#!/usr/bin/env python3
"""Exact finite-T sphaleron crossover for the compensated high-tilt family.

For the cold metastable potential and the same passive two-pole environment,
the static sphaleron has one unstable constant mode.  Its first nonzero
Matsubara mode changes sign when

    Lambda_1(T) = C nu_1^2 + nu_1 Y_L(nu_1) + F'(x_s)/L = 0,
    nu_1 = 2 pi k_B T / hbar.

This is the dissipative quantum-to-thermal crossover of the reduced electrical
Euclidean action.  It is stricter and more self-consistent than the earlier
heuristic hbar*omega_c/(2*pi*k_B), because it uses the actual saddle curvature
and exact positive-real two-pole admittance.

It does NOT compute the periodic instanton action or escape prefactor.
"""
from __future__ import annotations
import math
from scipy.optimize import brentq

import full_dynamic_rfsquid as fd
from directional_recovery_barriers import directional_barriers
from R80_dissipative_bounce_screen import Y_laplace
from quantum_initial_capture import HBAR, KB

B_TARGET=37.61
B_DISS={
 .050:29.76563577,.140:12.49903278,.160:9.90315950,.180:7.58847205,
 .190:6.52571286,.200:5.52063406,.210:4.56802352,.220:3.65877371,
}
C0=215e-15; R0=80.; ALPHA=.90


def main():
    ob,ot=fd.BETA_COLD,fd.DELTA_TILT
    L=fd.CASES[.6][0]
    try:
        fd.BETA_COLD=.80
        for delta,B0 in B_DISS.items():
            fd.DELTA_TILT=delta
            model=fd.DynamicForce(.6,quick=False,Tmax=.98)
            b=directional_barriers(model,fd.T0)
            xs=model._scalar(b['saddle'])
            Fs=model._scalar(model.spline.ev(fd.T0,xs,dx=0,dy=1))
            roots=model.roots(fd.T0)
            xm=max(x for x,kap in roots if x<0 and kap>0)
            km=model._scalar(model.spline.ev(fd.T0,xm,dx=0,dy=1))
            r=B_TARGET/B0
            C=C0*r*r; R=R0/r
            wc=math.sqrt(km/(L*C)); wd=ALPHA*wc
            def lam(T):
                nu=2*math.pi*KB*T/HBAR
                Y=model._scalar(Y_laplace(nu,R,wd))
                return C*nu*nu + nu*Y + Fs/L
            # At T->0 the saddle curvature term is negative.  At high T the
            # inertial term is positive, so a root must occur while the reduced
            # harmonic sphaleron description remains regular.
            Tx=brentq(lam,1e-5,.5,xtol=1e-13,rtol=1e-12,maxiter=300)
            lam20=lam(fd.T0)
            nu20=2*math.pi*KB*fd.T0/HBAR
            norm=abs(Fs/L)
            msg=(f'delta={delta:.3f}: r={r:.7f} C={C*1e15:.3f}fF R={R:.4f}ohm '
                 f'fc={wc/(2*math.pi)*1e-9:.5f}GHz Fs={Fs:+.7f} '
                 f'Tx_exact={Tx:.6f}K T0/Tx={fd.T0/Tx:.5f} '
                 f'Lambda1(T0)/|Fs/L|={lam20/norm:+.6f} '
                 f'nu1(T0)/(2pi)={nu20/(2*math.pi)*1e-9:.5f}GHz')
            print(msg); print(f'::notice title=Experiment 03 exact finiteT crossover::{msg}')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot

if __name__=='__main__': main()
