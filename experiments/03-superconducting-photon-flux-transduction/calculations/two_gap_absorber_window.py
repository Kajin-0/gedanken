#!/usr/bin/env python3
"""Two-gap absorber-area window for Experiment 03.

Uses Huang et al.'s absorbed-photon thermal calibration as a ratio reference:
100 um^2 graphene, lambda=1.55 um, Tpk~2.5 K.  No separate Sommerfeld
coefficient is needed for relative area thresholds if eta_th is held fixed.

For Ce=gamma A T:

    Amax_fold = 2 eta E_gamma/[gamma(Tf^2-T0^2)]
    Amin_gap   = 2 eta E_gamma/[gamma(Tgap^2-T0^2)]

where Tgap=Delta_s/kB.  The script maps the current realistic-skewness,
inductance-retuned fold temperatures across 8-14 um for MoRe Delta_s=1.3 meV.
"""

from __future__ import annotations

T0 = 0.020
A_REF_UM2 = 100.0
LAMBDA_REF_UM = 1.55
T_REF = 2.5
KB_EV = 8.617333262e-5
DELTA_PARENT_EV = 1.3e-3
T_GAP = DELTA_PARENT_EV / KB_EV

FOLDS = {
    "rDelta=1.0": 0.905,
    "rDelta=0.6": 0.695,
    "rDelta=0.4": 0.540,
}


def area_for_temperature(lambda_um: float, target_T: float) -> float:
    """Area in um^2 giving target_T for one absorbed photon by ratio scaling."""
    return (
        A_REF_UM2
        * (LAMBDA_REF_UM / lambda_um)
        * (T_REF**2 - T0**2)
        / (target_T**2 - T0**2)
    )


def lambda_max_for_area(area_um2: float, fold_T: float) -> float:
    """Longest wavelength that still reaches fold_T for fixed absorber area."""
    return (
        LAMBDA_REF_UM
        * (A_REF_UM2 / area_um2)
        * (T_REF**2 - T0**2)
        / (fold_T**2 - T0**2)
    )


def main() -> None:
    print(f"parent gap temperature = {T_GAP:.3f} K")
    print("lambda case A_2.5K[um2] Amin_gap[um2] Amax_fold[um2] ratio")
    for lam in (8.0, 10.0, 12.0, 14.0):
        a25 = area_for_temperature(lam, T_REF)
        amin = area_for_temperature(lam, T_GAP)
        for name, tf in FOLDS.items():
            amax = area_for_temperature(lam, tf)
            print(
                f"{lam:5.1f} {name:12s} {a25:12.3f} {amin:13.3f} "
                f"{amax:14.3f} {amax/amin:8.1f}"
            )

    print("\n100-um^2 absorber wavelength reach:")
    for name, tf in FOLDS.items():
        print(f"{name:12s}: lambda_max = {lambda_max_for_area(100.0, tf):.2f} um")

    # Regression on central 10-um baseline.
    amin10 = area_for_temperature(10.0, T_GAP)
    amax10 = area_for_temperature(10.0, FOLDS["rDelta=1.0"])
    assert 0.42 < amin10 < 0.44
    assert 117.0 < amax10 < 120.0
    assert 11.7 < lambda_max_for_area(100.0, 0.905) < 12.0
    print("PASS: two-gap absorber-window regression")


if __name__ == "__main__":
    main()
