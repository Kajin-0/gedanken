# Novelty Addendum — Coherent-State Benchmarks versus Schmidt-Rank-Two State Tests

**Date:** 2026-08-07  
**Status:** Additional prior-art constraint on the standalone Gaussian theorem candidate.

## 1. Namiki–Azuma coherent-state benchmark

Ryo Namiki and Koji Azuma, **Quantum Benchmark via an Uncertainty Product of Canonical Variables**, Phys. Rev. Lett. 114, 140503 (2015), arXiv:1404.2643, derive an uncertainty-product benchmark for continuous-variable channels using

- a Gaussian-distributed ensemble of coherent input states;
- homodyne measurements;
- an optimal quadrature-noise tradeoff that no entanglement-breaking channel can beat.

They state that the benchmark can verify quantum-domain performance for **all one-mode Gaussian channels**.

Therefore the following broad claim is already prior art:

$$
\boxed{
\text{experimentally simple coherent-state resources can certify nonclassical/quantum-domain one-mode Gaussian channel behavior.}
}
$$

The standalone paper must not imply that a bosonic ancilla-entangled state is the first simple finite-resource way to benchmark arbitrary one-mode Gaussian channels.

---

## 2. Why this does not duplicate the rank-two theorem

The Namiki–Azuma protocol is an **ensemble benchmark**:

1. prepare many coherent inputs drawn from a classical distribution;
2. measure output quadrature statistics;
3. compare averaged noise against the EB benchmark.

The present candidate theorem is a **single-state entanglement-preservation statement**:

$$
\boxed{
\mathcal N\text{ non-EB}
\iff
\exists\text{ one Schmidt-rank-two pure input with NPT output}.
}
$$

The probe is

$$
\sqrt p|0\rangle|\psi_0\rangle
+e^{i\phi}\sqrt{1-p}|1\rangle|\psi_1\rangle,
$$

where the reference dimension is exactly two and the bosonic branches are two displaced equal-covariance pure Gaussian states.

Thus the claimed resource reduction is **not**

> coherent states are enough to benchmark Gaussian channels.

That is known.

It is

> **one pure Schmidt-rank-two entangled probe is enough to expose every non-EB one-mode Gaussian channel through NPT survival.**

---

## 3. Relation to finite-TMSV tests

De Pasquale et al. already show that arbitrarily weak finite TMSV squeezing suffices to test Gaussian EB behavior.

Namiki–Azuma show that coherent-state ensembles and homodyne measurements can benchmark all one-mode Gaussian channels.

Together these prior results remove two possible overclaims:

- finite energy is not new;
- simple coherent-state benchmarking is not new.

The remaining candidate novelty is therefore narrowly

$$
\boxed{
\text{Schmidt-rank-two single-state sufficiency}
}
$$

plus the stronger phase-insensitive statement that every nontrivial finite binary coherent hybrid probe is front faithful to the EB boundary.

---

## 4. Practical implication

Even if the rank-two theorem is mathematically new, it is not automatically the experimentally simplest Gaussian-channel benchmark.

Its value would instead be conceptual and structural:

- minimal reference Hilbert-space dimension;
- finite Schmidt rank;
- explicit NPT output rather than an averaged ensemble inequality;
- exact two-branch state witness in the phase-insensitive case.

This distinction should be explicit in any standalone manuscript.