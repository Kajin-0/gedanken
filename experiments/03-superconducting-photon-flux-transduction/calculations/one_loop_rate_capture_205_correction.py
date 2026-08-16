#!/usr/bin/env python3
"""Correct the delta=.205 2-ns capture row to the current self-consistent one-loop rate root.

The earlier capture worker hard-coded r=8.549474917, whereas the current
finiteT_one_loop_rate_manifold solve gives r=8.517859912.  This reruns the same
area grid at the corrected electrical scale so the frontier is internally
consistent.
"""
from __future__ import annotations
import math
import full_dynamic_rfsquid as fd
import nonlinear_fdt_twa_screen as nf
from nonlinear_fdt_twa_convergence import wilson
from quantum_initial_capture import quantum_covariance

D=.205; RSC=8.517859912
C0=215e-15; R0=80.; L0=111.5e-12; ALPHA=.90
AREAS=(415.,430.,445.,460.,475.)

ob,ot=fd.BETA_COLD,fd.DELTA_TILT; original=fd.CASES[.6]
try:
    C=C0*RSC*RSC; R=R0/RSC
    fd.BETA_COLD=.80; fd.DELTA_TILT=D
    fd.CASES[.6]=(L0,C,original[2]); nf.CASES[.6]=fd.CASES[.6]
    model=fd.DynamicForce(.6,quick=False,Tmax=1.02)
    fold=model.fold_temperature(hi=.98)
    wc=quantum_covariance(model,.6)['omega_c']
    print(f'delta=.205 corrected r_rate={RSC:.9f} C={C*1e15:.3f}fF R={R:.6f}ohm fold={fold:.6f}K fc={wc/(2*math.pi)*1e-9:.6f}GHz')
    for A in AREAS:
        o=nf.run_case(model,14.,R=R,alpha=ALPHA,ntraj=1024,dt_ps=.125,tpost_ns=2.0,
                      seed=4205000,area_um2=A,rise_ps=20.)
        k=int(o['n_right_final']); lo,hi=wilson(k,1024)
        print(f'A={A:g}um2 P_final={o["P_right_final"]:.6f} CI95=[{lo:.6f},{hi:.6f}] fail={1024-k} P_reform={o["P_xright_reform"]:.6f} reform={o["reform_ps"]:.2f}ps')
    print('PASS')
finally:
    fd.BETA_COLD=ob; fd.DELTA_TILT=ot; fd.CASES[.6]=original; nf.CASES[.6]=original
