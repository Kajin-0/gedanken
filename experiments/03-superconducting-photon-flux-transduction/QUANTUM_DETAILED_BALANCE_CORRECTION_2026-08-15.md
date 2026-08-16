# Experiment 03 — Quantum detailed-balance correction — 2026-08-15

## Status

**Canonical modeling correction.**

This note prevents a serious interpretation error in the causal-bath branch.

## 1. What the existing symmetrized-FDT TWA/GLE calculations do correctly

Several Experiment-03 workflows generate a real Gaussian stationary force with the **symmetrized** equilibrium spectrum

\[
S_I^{\rm sym}(\omega)
=\hbar|\omega|\coth\!\left(\frac{\hbar|\omega|}{2k_BT_b}\right)
\operatorname{Re}Y(\omega).
\]

For a quadratic cold phase mode, this stochastic representation can reproduce the correct symmetrized/Wigner covariance when the bath history is prepared consistently. The Drude stationarity regressions explicitly verified this numerically.

Therefore these calculations are useful for

- cold covariance regression;
- semiclassical basin sensitivity to the magnitude and correlation time of equilibrium fluctuations;
- comparing causal impedance shapes under one common harsh stochastic convention;
- architecture screening.

## 2. What they do **not** do

A real classical Gaussian force with the symmetrized vacuum spectrum does **not** preserve the emission/absorption asymmetry of a quantum bath once the system becomes nonlinear.

The physical nonsymmetrized quantum noise obeys detailed balance / KMS. At low bath temperature, a passive bath can absorb energy from an excited system, while its ability to emit energy capable of exciting the system is suppressed. At `T_b -> 0`, upward bath-induced transitions vanish in the ordinary weak-coupling energy-basis picture.

A symmetric classical force treats positive- and negative-frequency fluctuations as interchangeable. In a nonlinear metastable potential this can therefore produce spurious vacuum-driven activation (zero-point-energy leakage).

Consequently:

```text
symmetrized-FDT TWA/GLE capture fraction != exact physical quantum efficiency
symmetrized-FDT TWA/GLE dark-switch fraction != physical quantum dark-count rate
```

This correction applies to both the one-pole Drude and passive two-pole stochastic workflows.

## 3. Interpretation of the current noisy results

The one-pole Drude sym-noise scout around `R0=360 ohm, omegaD/omegac=3` gave an apparent large capture penalty when future symmetric vacuum noise was retained. That number is a **harsh semiclassical basin-stress result**, not a quantum no-go result.

The passive two-pole branch can give much higher capture fractions even under the same sym-noise stress. Those values are likewise **screening fractions only**.

The correct comparison is therefore:

```text
Does one passive Y(omega) make the metastable basin robust even against a harsh symmetrized-noise TWA stress?
```

not

```text
What is the exact detector efficiency under vacuum noise?
```

## 4. Mandatory next quantum level

A publication-grade open-system calculation must use one physical environment consistently and preserve detailed balance. Candidate routes include

1. a time-dependent energy-basis master equation using the **nonsymmetrized** noise spectrum and KMS rates, with explicit control of nonadiabatic-basis error;
2. a reaction-coordinate / pseudomode embedding of the selected passive network followed by a quantum master equation for the enlarged system;
3. a numerically exact or systematically convergent open-system benchmark on a reduced phase Hilbert space.

The photon pulse is nonadiabatic on the phase-oscillation scale, so an instantaneous-eigenbasis Lindblad equation must not be assumed controlled without a dedicated comparison.

## 5. Claim discipline

Until a detailed-balance-preserving nonlinear open-system calculation exists:

- do not call any symmetrized-FDT TWA result an exact efficiency;
- do not call its zero-photon switching fraction a dark-count rate;
- do not infer that zero-point noise thermally activates the latch;
- retain these workflows as adversarial semiclassical stress tests and impedance-comparison tools.

No novelty claim is authorized by this correction.
