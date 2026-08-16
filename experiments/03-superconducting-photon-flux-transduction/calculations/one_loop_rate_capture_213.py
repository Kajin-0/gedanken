#!/usr/bin/env python3
"""2-ns capture screen for delta=.213 on the calibrated Gaussian one-loop rate root.

The crossover branch-topology analysis shows that the production finite-T saddle
is a finite-amplitude one-negative-mode branch distinct from the tiny branch
that merges into the sphaleron.  The .213 rate root lies at T0/T_local=.9615,
well below the local Matsubara bifurcation, so it is restored as an accepted
Gaussian one-loop dark point.

Capture remains a symmetrized-FDT TWA screening quantity.
"""
from __future__ import annotations
import math
import full_dynamic_rfsquid as fd
import nonlinear_fdt_twa_screen as nf
from nonlinear_fdt_twa_convergence import wilson
from quantum_initial_capture import quantum_covariance

D=.213; RSC=11.19986413
AREAS=(455.,465.,475.,485.,495.,505.)
C0=215e-15; R0=80.; L0=111.5e-12; ALPHA=.90; N=4096

ob,ot=fd.BETA_COLD,fd.DELTA_TILT; original=fd.CASES[.6]
try:
    C=C0*RSC*RSC; R=R0/RSC
    fd.BETA_COLD=.80; fd.DELTA_TILT=D
    fd.CASES[.6]=(L0,C,original[2]); nf.CASES[.6]=fd.CASES[.6]
    model=fd.DynamicForce(.6,quick=False,Tmax=1.02)
    fold=model.fold_temperature(hi=.98)
    wc=quantum_covariance(model,.6)['omega_c']
    print(f'delta=.213 r_rate={RSC:.9f} C={C*1e15:.3f}fF R={R:.6f}ohm fold={fold:.6f}K fc={wc/(2*math.pi)*1e-9:.6f}GHz N={N}')
    for A in AREAS:
        o=nf.run_case(model,14.,R=R,alpha=ALPHA,ntraj=N,dt_ps=.125,tpost_ns=2.0,
                      seed=5210212,area_um2=A,rise_ps=20.)
        k=int(o['n_right_final']); lo,hi=wilson(k,N)
        msg=(f'A={A:g}um2 P_final={o["P_right_final"]:.8f} CI95=[{lo:.8f},{hi:.8f}] '
             f'fail={N-k} P_reform={o["P_xright_reform"]:.8f} reform={o["reform_ps"]:.2f}ps '
             f'coldReg=({o["cold_reg_x"]:.4f},{o["cold_reg_u"]:.4f})')
        print(msg); print(f'::notice title=Experiment 03 delta .213 capture::{msg}')
    print('PASS')
finally:
    fd.BETA_COLD=ob; fd.DELTA_TILT=ot; fd.CASES[.6]=original; nf.CASES[.6]=original
