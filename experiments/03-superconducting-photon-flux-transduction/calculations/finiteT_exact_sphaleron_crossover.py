#!/usr/bin/env python3
"""Exact finite-T sphaleron crossover for the compensated high-tilt family.

For the cold metastable potential and the same passive two-pole environment,
the static sphaleron has one unstable constant mode. Its first nonzero
Matsubara mode changes sign when

    Lambda_1(T) = C nu_1^2 + nu_1 Y_L(nu_1) + F'(x_s)/L = 0,
    nu_1 = 2 pi k_B T / hbar.

The saddle x_s is identified directly as the negative-curvature force root
between the metastable left minimum and favored right minimum.  This avoids any
coordinate-convention ambiguity in barrier-report helpers.

This computes the exact linear crossover of the reduced dissipative action. It
does NOT compute the periodic instanton exponent or escape prefactor.
"""
from __future__ import annotations
import math
import numpy as np
from scipy.optimize import brentq

import full_dynamic_rfsquid as fd
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
            roots=model.roots(fd.T0)
            xm=max(model._scalar(x) for x,kap in roots if x<0 and kap>0)
            saddles=[model._scalar(x) for x,kap in roots if x>xm and kap<0]
            if not saddles:
                raise RuntimeError(f'no negative-curvature saddle at delta={delta}')
            xs=min(saddles)
            km=model._scalar(model.spline.ev(fd.T0,xm,dx=0,dy=1))
            Fs=model._scalar(model.spline.ev(fd.T0,xs,dx=0,dy=1))
            if not Fs<0:
                raise RuntimeError(f'identified saddle has nonnegative curvature Fs={Fs}')
            r=B_TARGET/B0
            C=C0*r*r; R=R0/r
            wc=math.sqrt(km/(L*C)); wd=ALPHA*wc
            def lam(T):
                nu=2*math.pi*KB*T/HBAR
                Y=model._scalar(Y_laplace(nu,R,wd))
                return C*nu*nu + nu*Y + Fs/L

            # Scan logarithmically first so a failed bracket is diagnostic.
            Ts=np.geomspace(1e-7,2.0,240)
            vals=np.array([lam(float(T)) for T in Ts])
            idx=np.where(vals[:-1]*vals[1:]<=0)[0]
            if len(idx)==0:
                raise RuntimeError(
                    f'Lambda1 has no sign change on [{Ts[0]:.1e},{Ts[-1]:.1e}] K: '
                    f'Fs={Fs:+.7e}, lam_lo={vals[0]:+.7e}, lam_hi={vals[-1]:+.7e}')
            i=int(idx[0])
            Tx=brentq(lam,float(Ts[i]),float(Ts[i+1]),xtol=1e-13,rtol=1e-12,maxiter=300)
            lam20=lam(fd.T0)
            nu20=2*math.pi*KB*fd.T0/HBAR
            norm=abs(Fs/L)
            msg=(f'delta={delta:.3f}: r={r:.7f} C={C*1e15:.3f}fF R={R:.4f}ohm '
                 f'xm={xm:+.6f} xs={xs:+.6f} fc={wc/(2*math.pi)*1e-9:.5f}GHz Fs={Fs:+.7f} '
                 f'Tx_exact={Tx:.6f}K T0/Tx={fd.T0/Tx:.5f} '
                 f'Lambda1(T0)/|Fs/L|={lam20/norm:+.6f} '
                 f'nu1(T0)/(2pi)={nu20/(2*math.pi)*1e-9:.5f}GHz')
            print(msg); print(f'::notice title=Experiment 03 exact finiteT crossover::{msg}')
        print('PASS')
    finally:
        fd.BETA_COLD=ob; fd.DELTA_TILT=ot

if __name__=='__main__': main()
