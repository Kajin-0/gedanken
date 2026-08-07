# Checkpoint — 2026-08-07 15:19 EDT

## New result

For every balanced separable source-probe state,

$$
\boxed{C_\Xi\le F(\rho_L,\rho_R)}.
$$

This fidelity form is stronger than the earlier trace-distance witness and is analytically convenient for Gaussian thermal states.

For a thermal attenuator capturing fraction $\eta$ of the gravitational difference mode with thermal loss-port occupation $\bar n$,

$$
F_B
=\exp\left[-\frac{\eta N_\Delta}{2[1+2(1-\eta)\bar n]}\right],
$$

$$
C_\Xi
=\exp\left[-\frac{(1-\eta)(2\bar n+1)N_\Delta}{2[1+2(1-\eta)\bar n]}\right].
$$

Hence

$$
\boxed{
\mathcal M_F
=\ln(C_\Xi/F_B)
=\frac{N_\Delta[2(\bar n+1)\eta-(2\bar n+1)]}{2[1+2(1-\eta)\bar n]}.
}
$$

The fidelity witness is positive iff

$$
\boxed{
\eta>\frac{2\bar n+1}{2\bar n+2}.
}
$$

For a matched receiver with gravitational coupling $\kappa_g$, internal loss $\kappa_i$, and internal bath occupancy $\bar n_i$,

$$
\boxed{
\kappa_g>(2\bar n_i+1)\kappa_i.
}
$$

This is the current thermal history-transfer threshold.

## Important interpretation

Initial thermal occupation can reduce branch distinguishability without necessarily destroying source-receiver entanglement. Continuous thermal loss is more damaging because the uncontrolled bath acquires a branch record. The next problem is to calculate the exact negativity of the source qubit after a thermal-loss channel and determine whether the thermal threshold above is fundamental or only a threshold of the low-cost fidelity witness.