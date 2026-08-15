#!/usr/bin/env python3
"""Thermal energy margin for Experiment-03 rf-SQUID bifurcation.

This is a scaling calculation, not a device prediction.  It uses the published
Dirac-fermion single-photon bolometer thermal relation

    T_pk^2 - T0^2 = 2 E_abs / (gamma_S A)

as a reference calorimeter and asks how much absorbed energy is required to
reach a critical electron temperature Tcrit at which Ic(Tcrit)/Ic(T0) equals
the rf-SQUID bifurcation ratio beta_c/beta_cold.

The calculation deliberately keeps Tcrit external because equilibrium Ic(T)
is not yet a validated model for the nonequilibrium photon pulse.
"""

import numpy as np

H = 6.62607015e-34
C0 = 299792458.0
EV = 1.602176634e-19


def photon_energy(wavelength_m):
    return H * C0 / wavelength_m


def thermalization_fraction_required(A_target_um2, lambda_target_um,
                                     Tcrit_K,
                                     A_ref_um2=100.0,
                                     lambda_ref_um=1.55,
                                     Tpk_ref_K=2.5,
                                     T0_K=0.020):
    """Eliminate gamma_S using the reference calorimeter scaling."""
    E_target = photon_energy(lambda_target_um * 1e-6)
    E_ref = photon_energy(lambda_ref_um * 1e-6)
    return (
        (A_target_um2 / A_ref_um2)
        * (E_ref / E_target)
        * ((Tcrit_K**2 - T0_K**2) / (Tpk_ref_K**2 - T0_K**2))
    )


def max_area_um2(lambda_target_um, Tcrit_K, eta_th=1.0,
                  A_ref_um2=100.0, lambda_ref_um=1.55,
                  Tpk_ref_K=2.5, T0_K=0.020):
    E_target = photon_energy(lambda_target_um * 1e-6)
    E_ref = photon_energy(lambda_ref_um * 1e-6)
    return (
        eta_th
        * A_ref_um2
        * (E_target / E_ref)
        * ((Tpk_ref_K**2 - T0_K**2) / (Tcrit_K**2 - T0_K**2))
    )


def main():
    # Static rf-SQUID benchmark from rfsquid_bifurcation_scan.py
    beta_cold = 1.5
    beta_c = 1.1471219433332678
    gcrit = beta_c / beta_cold
    qreq = 1.0 - gcrit

    # Published equilibrium-temperature benchmark: switching-current scale
    # decreases by ~30% between 0.02 K and 1.2 K in Huang et al. 2026.
    # If g(T)=Ic(T)/Ic(T0) is monotone and comparable for our transducer,
    # qreq=23.5% would be crossed at some Tcrit <= 1.2 K.
    Tcrit_upper = 1.2

    # Earlier energy-scaled target area for a 10-um photon.
    A_target = 100.0 * 1.55 / 10.0

    eta_min = thermalization_fraction_required(
        A_target_um2=A_target,
        lambda_target_um=10.0,
        Tcrit_K=Tcrit_upper,
    )
    Amax = max_area_um2(10.0, Tcrit_upper, eta_th=1.0)
    E10_meV = photon_energy(10e-6) / EV * 1e3

    print("Experiment 03 thermal bifurcation margin")
    print(f"beta_c/beta_cold               = {gcrit:.6f}")
    print(f"required fractional Ic drop    = {qreq:.4%}")
    print(f"conditional Tcrit upper bound  = {Tcrit_upper:.3f} K")
    print(f"10-um photon energy             = {E10_meV:.3f} meV")
    print(f"energy-scaled target area       = {A_target:.3f} um^2")
    print(f"max area at eta_th=1            = {Amax:.3f} um^2")
    print(f"area/heat-capacity margin       = {Amax/A_target:.3f} x")
    print(f"minimum eta_th at A=15.5 um^2  = {eta_min:.4%}")
    print(f"required electronic heat        = {eta_min*E10_meV:.3f} meV")

    print("\nSensitivity to thermalization fraction")
    for eta in [1.0, 0.75, 0.50, 0.25, 0.20]:
        print(f"eta_th={eta:4.2f}: Amax={max_area_um2(10.0, Tcrit_upper, eta):8.3f} um^2")

    print("\nSensitivity to critical temperature at eta_th=1")
    for Tc in [0.3, 0.5, 0.8, 1.0, 1.2, 1.5, 2.0, 2.5]:
        print(f"Tcrit={Tc:3.1f} K: Amax={max_area_um2(10.0, Tc):8.3f} um^2")


if __name__ == "__main__":
    main()
