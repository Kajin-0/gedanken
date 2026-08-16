# Experiment 03 — Metastable Quantum Initial-State Specification

**Date:** 2026-08-15  
**Status:** next-solver requirement; no detector-performance claim

## 1. Global Gibbs state is the wrong initial condition

Generation A is a deliberately tilted double-well / metastable flux latch. Before the photon arrives the detector is prepared in the **left metastable basin**, while the favored right basin is lower in free energy.

Therefore a full-system equilibrium Gibbs state

\[
\rho_{G}\propto e^{-\beta H}
\]

is not the detector's operating initial state. At sufficiently long times it weights the lower favored basin and includes equilibrium interwell population transfer, whereas the detector protocol explicitly conditions on the device having remained in the metastable dark state prior to the photon.

The nonlinear quantum capture calculation must therefore initialize a **metastable quasistationary state conditioned on no escape**, not a global Gibbs state.

## 2. Controlled low-temperature approximation

Let `x_m` be the cold metastable minimum and `x_s` the separating saddle. Deep inside the long-lived metastable regime, a practical hierarchy is:

1. construct the local left-well Hamiltonian or Liouvillian;
2. thermalize within that basin against the same passive environment;
3. condition on no crossing/escape through the saddle;
4. use the resulting local quasistationary density matrix as the pre-photon state.

For sufficiently large dark action and low temperature, the leading approximation is simply the local harmonic thermal state about `x_m`, with controlled corrections from anharmonicity and bath dressing.

This is also the quantum object whose Wigner covariance the current sym-FDT/TWA prehistory is intended to reproduce at quadratic order.

## 3. Thermal occupation at the safe frontier is small

The current safe-optimum neighborhood has a cold phase frequency around

```text
fc ~ 1.9–2.0 GHz
T0 = 20 mK.
```

Hence

\[
\frac{hf_c}{k_BT_0}\approx4.5\text{–}4.8.
\]

For a harmonic local mode,

\[
\bar n
=\frac{1}{e^{hf_c/(k_BT_0)}-1}
\approx0.009\text{–}0.011.
\]

Thus the isolated local oscillator is roughly `99%` in its harmonic ground state at 20 mK. The explicit filter reaction coordinate, with resonance of order `1.8 GHz`, likewise has thermal occupation of only order `1–2%` before bath dressing.

This makes a low-energy quantum basis plausible, although strong filter damping means that a bare product of two isolated oscillator thermal states is not automatically the exact correlated equilibrium state.

## 4. Three initialization levels to benchmark

### Level I — local harmonic Gaussian

Use the exact cold curvature and same-environment covariance to construct a Gaussian state centered at the metastable minimum.

Purpose: reproduce the current Wigner/TWA quadratic regression in a quantum representation.

### Level II — restricted anharmonic left-well Gibbs state

Construct the phase Hamiltonian on the left side of the separating saddle, with a controlled boundary treatment, and form

\[
\rho_L\propto e^{-\beta H_L}.
\]

Converge the result against grid/basis size and boundary placement.

Purpose: quantify cold anharmonic corrections without allowing unphysical global equilibration into the favored well.

### Level III — open-system quasistationary state

For the full phase + reaction-coordinate + resistor-bath model, find the long-lived state conditioned on no escape from the metastable basin (equivalently the slow quasistationary mode of the restricted open-system propagator).

Purpose: final internally consistent pre-photon state for a detailed-balance-preserving capture calculation.

## 5. Mandatory regression

Before interpreting a quantum pulse result, the chosen initialization must reproduce in the harmonic limit:

- the cold phase variance used by the current Wigner calculation;
- the phase/momentum covariance implied by the same passive environment;
- the correct detailed-balance ratio for upward/downward local transitions;
- negligible right-basin population under the **conditioned** dark preparation.

A calculation that starts from the global tilted-double-well Gibbs state and then reports photon-trigger probability answers the wrong detector protocol.

## 6. Immediate implication

The small local thermal occupation is favorable computationally, but it does **not** remove the need for metastable conditioning. The central quantum-initialization problem is not high temperature; it is the distinction between a long-lived locally equilibrated metastable detector state and the true global equilibrium of an asymmetric double well.
