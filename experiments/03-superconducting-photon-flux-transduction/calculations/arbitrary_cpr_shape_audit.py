#!/usr/bin/env python3
"""Shape audit for the ideal arbitrary-length graphene CPR model.

Imports the current Matsubara CPR implementation and reports quantities that are
more directly comparable to measured CPR data:

    S = (2 phi_max - pi)/pi
    x_fold, beta_fold
    fold tangent slope = 1/beta_fold

The purpose is to expose whether the ideal-interface model obtains its favorable
rf-SQUID fold from an unrealistically sawtooth-like CPR tail.
"""

import numpy as np

from arbitrary_length_graphene_cpr import GrapheneCPRModel, T0


def main():
    print("Experiment 03 arbitrary-CPR shape audit")
    print("ell=1.1, delta=0.05, T=20 mK")
    print("mu/Delta0     S_cold      phi_max/pi    x_fold       beta_fold    tangent_slope")

    for mu in (0.0, 10.0, 20.0):
        model = GrapheneCPRModel(1.1, mu, delta=0.05)
        _, spline = model.cpr(T0)
        phis = np.linspace(0.003, np.pi - 0.003, 4001)
        vals = spline(phis)
        phi_max = float(phis[int(np.argmax(vals))])
        S = 2.0 * phi_max / np.pi - 1.0
        x_fold, beta_fold = model.normalized_fold(T0)
        slope = 1.0 / beta_fold
        print(
            f"{mu:9.1f}   {S:9.4f}     {phi_max/np.pi:9.4f}   "
            f"{x_fold:10.5f}   {beta_fold:10.5f}   {slope:12.4f}"
        )

    print("\nInterpretation:")
    print("The favorable finite-doping ideal folds are associated with very large")
    print("forward skewness and steep near-pi tail slopes.  Compare these values to")
    print("measured strong-doping graphene CPR skewness near S~0.23-0.27 and to")
    print("self-consistent calculations near S~0.15 cited by Nanda et al. 2017.")
    print("A favorable beta_fold from the rigid-boundary model must not be promoted")
    print("without showing that the corresponding tail slope survives realistic")
    print("interfaces, proximity depletion and current depairing.")


if __name__ == "__main__":
    main()
