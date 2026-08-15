#!/usr/bin/env python3
"""Parameter-level validation of the arbitrary-length graphene CPR implementation.

Reproduce the intermediate-junction parameter set used in Hagymasi, Kormanyos
& Cserti, Phys. Rev. B 82, 134516 (2010), Fig. 1(c,d):

    xi/L = 0.91  -> ell=L/xi = 1/0.91
    mu/Delta0 = 0 and 20
    T/Tc = low-T, 0.18, 0.35

The paper defines skewness S = 2 phi_max/pi - 1 and reports that at low T the
CPR is forward skewed; for mu/Delta0=20 and L/xi~1.1 it is already approaching
a rounded sawtooth; increasing T drives the CPR toward a sinusoid.

This regression checks those parameter-level trends and numerical convergence.
It is not a digitized point-by-point reproduction of the published figure.
"""

from __future__ import annotations

import numpy as np

from arbitrary_length_graphene_cpr import (
    DELTA0_EV,
    KB_EV,
    matsubara_cpr,
)

TC = DELTA0_EV / (1.764 * KB_EV)
ELL = 1.0 / 0.91
PHIS = np.linspace(0.003, np.pi - 0.003, 601)


def metrics(mu_r: float, t_over_tc: float, qmax: float, nq: int, wmax: float):
    # Use 0.01 Tc as a numerically convenient proxy for the plotted T=0 curve.
    frac = max(float(t_over_tc), 0.01)
    current = matsubara_cpr(
        frac * TC,
        ELL,
        float(mu_r),
        PHIS,
        qmax=qmax,
        nq=nq,
        wmax=wmax,
    )
    idx = int(np.argmax(current))
    phi_max = float(PHIS[idx])
    skew = 2.0 * phi_max / np.pi - 1.0
    return float(np.max(current)), phi_max, skew


def main() -> None:
    settings = [
        (25.0, 400, 15.0),
        (30.0, 500, 20.0),
        (35.0, 700, 25.0),
    ]
    temperatures = [0.0, 0.18, 0.35]

    print("Hagymasi intermediate-length CPR validation")
    print(f"ell=L/xi={ELL:.6f}; Tc={TC:.6f} K")

    central = {}
    for qmax, nq, wmax in settings:
        print(f"\nqmax={qmax:g}, nq={nq}, wmax={wmax:g}")
        for mu in (0.0, 20.0):
            for frac in temperatures:
                Ic, phi, S = metrics(mu, frac, qmax, nq, wmax)
                print(
                    f"mu={mu:4.0f} T/Tc={frac:4.2f} "
                    f"Ic[a.u.]={Ic:.9g} phi_max={phi:.6f} S={S:.6f}"
                )
                if (qmax, nq, wmax) == settings[1]:
                    central[(mu, frac)] = (Ic, phi, S)

    # Physics-trend regressions from the paper's textual discussion of Fig. 1.
    s00 = central[(0.0, 0.0)][2]
    s018 = central[(0.0, 0.18)][2]
    s035 = central[(0.0, 0.35)][2]
    s200 = central[(20.0, 0.0)][2]
    s2018 = central[(20.0, 0.18)][2]
    s2035 = central[(20.0, 0.35)][2]

    assert s00 > 0.0 and s200 > 0.0
    assert s00 > s018 > s035 > 0.0
    assert s200 > s2018 > s2035 > 0.0
    assert s200 > s00

    # Numerical convergence: skewness should not move by more than one phase-grid
    # increment between the central and high-resolution integration settings.
    dS_grid = 2.0 * (PHIS[1] - PHIS[0]) / np.pi
    high = {
        (mu, frac): metrics(mu, frac, *settings[2])
        for mu in (0.0, 20.0)
        for frac in temperatures
    }
    for key, (_, _, S) in central.items():
        assert abs(S - high[key][2]) <= dS_grid + 1.0e-12

    print("\nPASS: published intermediate-junction trend regressions and grid convergence")


if __name__ == "__main__":
    main()
