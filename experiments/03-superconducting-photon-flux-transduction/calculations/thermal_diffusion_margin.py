#!/usr/bin/env python3
"""Thermal-diffusion timescale checkpoint for Experiment 03.

Uses the published graphene single-photon bolometer characteristic values

    l_D ~ 230 um
    tau_ep ~ 75 ns

and the relation l_D = sqrt(D tau_ep) to infer a characteristic electronic
thermal diffusivity.  It then compares L^2/D with the present 15.5-um^2
square-absorber scale and the rf-SQUID phase timescale.

This is a cross-device scaling diagnostic, not a prediction for a fabricated
LWIR device.  Geometry, contact cooling, density, disorder and proximity
coupling can change D and the thermal boundary conditions.
"""

import math

L_D = 230e-6       # m
TAU_EP = 75e-9     # s
A_TARGET = 15.5e-12  # m^2
PHASE_CROSS = 20e-12 # s, current deterministic benchmark
LC_TIME = 5.74e-12   # s

D = L_D**2 / TAU_EP
SIDE = math.sqrt(A_TARGET)
T_DIFF = SIDE**2 / D

print("Experiment 03 thermal-diffusion margin")
print(f"inferred D                    = {D:.6f} m^2/s")
print(f"target square side            = {SIDE*1e6:.6f} um")
print(f"L^2/D diffusion time          = {T_DIFF*1e12:.6f} ps")
print(f"tau_ep / t_diff               = {TAU_EP/T_DIFF:.3f}")
print(f"t_diff / phase-cross time     = {T_DIFF/PHASE_CROSS:.3f}")
print(f"t_diff / sqrt(LC)             = {T_DIFF/LC_TIME:.3f}")

for length_um in [1.0, 2.0, 4.0, 10.0, 25.0]:
    t = (length_um*1e-6)**2 / D
    print(f"length={length_um:4.1f} um: L^2/D={t*1e12:9.3f} ps")
