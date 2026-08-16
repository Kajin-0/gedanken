#!/usr/bin/env python3
"""Test the electrical-similarity dark-stability rescue against photon capture.

The zero-T Euclidean electrical subsystem has the exact scaling

    C -> r^2 C
    R -> R/r
    omega_D -> omega_D/r

at fixed L/static CPR and fixed alpha=omega_D/omega_c.  Since omega_c->omega_c/r,
this preserves the electrical dimensionless controls

    g=1/(R C omega_c), alpha=omega_D/omega_c,

and scales the full Euclidean action by r.

However, a real photon pulse does NOT automatically scale its physical rise and
cooling times by r.  This script therefore applies the electrical scaling while
leaving the existing graphene thermal trace in physical time unchanged and asks
whether the capture branch survives.

The stochastic fractions are the existing symmetrized-FDT TWA screening numbers,
not exact physical quantum efficiencies.  The purpose is to test whether the
dark-rescue direction is dynamically compatible with the finite thermal pulse.
"""
from __future__ import annotations

import math

import full_dynamic_rfsquid as fd
import nonlinear_fdt_twa_screen as nf
from full_dynamic_rfsquid import DynamicForce

C0=215e-15
L0=111.5e-12
R0=80.0
ALPHA=.90
TF=.695


def main():
    print('Experiment 03 electrical-similarity dark-rescue capture screen')
    model=DynamicForce(.6,quick=False,Tmax=.95)
    original=fd.CASES[.6]
    try:
        for r in (1.0,1.15,1.28824,1.45):
            C=C0*r*r
            R=R0/r
            # Mutate the shared CASES dict object; modules imported CASES by
            # reference, so quantum covariance/cold poles/run_case all use C'.
            fd.CASES[.6]=(L0,C,TF)
            # nf.CASES is the same dict object but write explicitly as a guard.
            nf.CASES[.6]=(L0,C,TF)
            for A in (57.142857,80.0,86.5):
                o=nf.run_case(model,14.,R=R,alpha=ALPHA,ntraj=1024,dt_ps=.125,
                              seed=424242,area_um2=A,rise_ps=20.)
                wc=2*math.pi/(2*math.pi)  # placeholder overwritten below
                from quantum_initial_capture import quantum_covariance
                cov=quantum_covariance(model,.6)
                wc=cov['omega_c']
                g=1/(R*C*wc)
                rho=wc*20e-12
                msg=(f'r={r:.5f} C={C*1e15:.2f}fF R={R:.3f}ohm A={A:g}um2: '
                     f'fc={wc/(2*math.pi)*1e-9:.4f}GHz g={g:.5f} rho={rho:.5f}; '
                     f'P_final={o["P_right_final"]:.6f} P_reform={o["P_xright_reform"]:.6f} '
                     f'reform={o["reform_ps"]:.2f}ps '
                     f'coldReg=({o["cold_reg_x"]:.3f},{o["cold_reg_u"]:.3f})')
                print(msg); print(f'::notice title=Experiment 03 electrical dark rescue::{msg}')
    finally:
        fd.CASES[.6]=original
        nf.CASES[.6]=original
    print('PASS')

if __name__=='__main__': main()
