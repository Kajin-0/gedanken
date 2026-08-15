#!/usr/bin/env python3
"""Dimensionless write-time margin for Experiment 03.

The present benchmark separates three fast circuit/thermal transport scales from
an effective hot interval:

  t_phase  ~ deterministic phase crossing after the fold is removed
  t_diff   ~ absorber thermal diffusion time L_abs^2 / D
  t_damp   ~ 2 R_hot C (simple RCSJ amplitude envelope)

A necessary, not sufficient, latching condition is that the useful interval
above the fold exceed all relevant settling scales.
"""

C = 200e-15
T_PHASE = 20e-12
T_DIFF = 21.97542533081285e-12
TAU_REF = 75e-9

print("Experiment 03 dynamic margin")
print(f"reference hot interval       = {TAU_REF*1e9:.3f} ns")
print(f"phase-cross time             = {T_PHASE*1e12:.3f} ps")
print(f"thermal diffusion time       = {T_DIFF*1e12:.3f} ps")
print(f"tau_ref/t_phase              = {TAU_REF/T_PHASE:.1f}")
print(f"tau_ref/t_diff               = {TAU_REF/T_DIFF:.1f}")

print("\nMaximum R_hot from 2 R C < useful hot interval")
for t_hot in [75e-9, 30e-9, 10e-9, 3e-9, 1e-9, 0.1e-9]:
    rmax = t_hot / (2*C)
    print(f"t_hot={t_hot*1e9:6.2f} ns -> R_hot < {rmax/1e3:9.3f} kOhm")

print("\nNecessary scale ratio M_dyn=t_hot/max(t_phase,t_diff,2RC)")
for R_kohm in [1, 5, 10, 25, 100]:
    tdamp=2*(R_kohm*1e3)*C
    tslow=max(T_PHASE,T_DIFF,tdamp)
    print(f"R_hot={R_kohm:4.0f} kOhm: t_damp={tdamp*1e9:7.3f} ns, M_dyn(75ns)={TAU_REF/tslow:8.2f}")
