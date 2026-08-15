#!/usr/bin/env python3
"""Capacitance window linking cold MQT stability and write dynamics.

Within the provisional cubic-barrier MQT model,

    Gamma_Q = omega/(2 pi) exp[-alpha_Q DeltaU/(hbar omega)],
    omega = sqrt(kappa/(L C)),

where kappa is the dimensionless curvature u'' at the cold metastable minimum.
For a target dark rate D, the minimum capacitance can be solved analytically
with the Lambert W function:

 C_min = [ hbar sqrt(kappa/L) W(alpha_Q DeltaU/(2 pi hbar D))
           /(alpha_Q DeltaU) ]^2.

This is NOT an exact dissipative rf-SQUID MQT result.  It is a useful closure
inside the same 7.2*DeltaU/(hbar omega) diagnostic used earlier in Experiment03.

Dynamic constraints provide upper capacitance scales, e.g.
    2 R_hot C < t_hot
and, for a dimensionless phase-passage factor g,
    g sqrt(L C) < t_hot.
"""

import math
from scipy.special import lambertw

HBAR = 1.054571817e-34
KB = 1.380649e-23
ALPHA_Q = 7.2
D_TARGET = 1e-6


def cmin_mqt(L_H, barrier_K, curvature, D=D_TARGET, alpha_q=ALPHA_Q):
    DeltaU = barrier_K * KB
    z = alpha_q * DeltaU / (2.0 * math.pi * HBAR * D)
    W = float(lambertw(z).real)
    return (
        HBAR * math.sqrt(curvature / L_H) * W / (alpha_q * DeltaU)
    ) ** 2


def cmax_damping(t_hot_s, R_hot_ohm):
    return t_hot_s / (2.0 * R_hot_ohm)


def cmax_phase(t_hot_s, L_H, g_phase=3.5):
    return (t_hot_s / g_phase) ** 2 / L_H


def main():
    # Exact sinusoidal benchmark.
    cases = [
        ("sinusoid beta=1.5", 164.55e-12, 9.44325, 0.79915),
        # Short-Dirac sensitivity points obtained with the idealized short-junction CPR.
        ("short-Dirac beta=0.8", 87.7616e-12, 4.40949, 0.56357),
        ("short-Dirac beta=0.9", 98.7318e-12, 7.30881, 0.67183),
    ]

    print("Experiment 03 provisional capacitance stability window")
    print(f"target diagnostic MQT dark rate = {D_TARGET:.1e} s^-1")
    print("\nMinimum C from the provisional MQT model:")
    for name, L, barrier_K, curvature in cases:
        Cmin = cmin_mqt(L, barrier_K, curvature)
        print(f"{name:24s}: C_min = {Cmin*1e15:9.3f} fF")

    print("\nUpper C from simple hot-state damping envelope 2 R C < t_hot:")
    for t_ns in [1.0, 3.0, 10.0, 30.0, 75.0]:
        vals = []
        for R_kohm in [1.0, 5.0, 10.0, 25.0]:
            Cmax = cmax_damping(t_ns*1e-9, R_kohm*1e3)
            vals.append(f"R={R_kohm:4.0f}k: {Cmax*1e15:8.1f}fF")
        print(f"t_hot={t_ns:5.1f} ns -> " + ", ".join(vals))

    print("\nUpper C from phase-passage scale g sqrt(LC) < t_hot (g=3.5):")
    for t_ns in [0.1, 1.0, 10.0]:
        Cmax = cmax_phase(t_ns*1e-9, 87.7616e-12, 3.5)
        print(f"t_hot={t_ns:4.1f} ns -> C_max,phase={Cmax*1e12:10.3f} pF")

    print("\nKey scaling:")
    print("At fixed cold potential, increasing C leaves the static optical fold")
    print("threshold unchanged, increases the MQT action approximately as sqrt(C),")
    print("and slows phase dynamics approximately as sqrt(C).  A real design therefore")
    print("requires C_min(DCR) < C < min[C_max,phase, C_max,damping].")


if __name__ == "__main__":
    main()
