# Prior Art — Binary Coherent-State Quantum-Channel Tests

**Timestamp:** 2026-08-07 17:05 EDT

## Why this note exists

The generalized theorem in `BINARY_COHERENT_EB_PROBE_THEOREM.md` says that any nontrivial binary coherent hybrid probe detects the entanglement-breaking transition of a one-mode thermal attenuator at the **state level**:

$$
\rho_{AB}\text{ NPT}
\iff
\eta>\frac{\bar n}{\bar n+1}.
$$

Two coherent states have been used for quantum-device tests long before this project, so the exact novelty boundary must distinguish those established prepare-and-measure/effective-entanglement protocols from the current theorem.

---

## 1. Häseler, Moroder & Lütkenhaus (2008)

**H. Häseler, T. Moroder, and N. Lütkenhaus,** “Testing Quantum Devices: Practical Entanglement Verification in Bipartite Optical Systems,” *Physical Review A* **77**, 032303 (2008), arXiv:0711.2709.

Their central idea is already very close conceptually to our channel viewpoint:

- test a device with a small set of nonorthogonal states;
- rewrite the preparation in an entanglement-based picture;
- if effective entanglement survives, the device cannot be purely measure-and-prepare/entanglement breaking.

They explicitly discuss a two-coherent-state alphabet $|\pm\alpha\rangle$ and a loss-plus-noise channel whose noise can be physically modeled by injecting a thermal state into the unused port of a beam splitter.

They construct an expectation-value matrix (EVM) from source information plus output first and second quadrature moments. For the symmetric noise model, they supplement the PPT-based EVM test with an explicit intercept-resend attack and obtain a necessary-and-sufficient boundary for whether **the measured moment data** are compatible with a separable explanation.

The separable-compatible variance boundary is

$$
V_{\rm sep}
=\frac12\left(f+\sqrt{f^2+1}\right),
$$

with

$$
f
=\eta\frac{s^2\ln s}{s^2-1},
\qquad
s=\langle-\alpha|\alpha\rangle.
$$

This boundary depends on the coherent-state overlap $s$.

### Difference from the current theorem

The current result assumes the full thermal attenuator model and characterizes the **actual output state**, rather than asking what can be inferred from only first and second moments.

For the actual thermal output,

$$
\boxed{
\rho_{AB}\text{ NPT}
\iff
\eta>\frac{\bar n}{\bar n+1},
}
$$

independent of the nonzero finite coherent-state separation.

The exact three-element witness uses selected non-Gaussian matrix elements rather than only quadrature moments and reaches this exact state-level boundary.

Thus Häseler et al. establish the broader two-state effective-entanglement testing paradigm, while the present candidate contribution is a thermal-channel-specific exact completion using a matched non-Gaussian witness.

---

## 2. Kreis & van Loock (2012)

Kreis & van Loock later study the exact hybrid qubit–coherent input state and thermal beam-splitter channel used in the symmetric special case of our theorem.

They derive the noisy hybrid state explicitly and apply a finite-order Shchukin–Vogel moment witness. Their detection threshold is amplitude dependent. They explicitly note that the moment witness need not detect all entangled states below the thermal-channel entanglement-breaking boundary.

The present exact partial-transpose theorem and principal-minor witness appear to close precisely that gap.

See `NOVELTY_CHECK_FINITE_CAT.md`.

---

## 3. Consequence for novelty claims

Do **not** claim any of the following as new:

- using two nonorthogonal coherent states to test a quantum memory/channel;
- the effective-entanglement representation of prepare-and-measure tests;
- using partial-transpose/expectation-value matrices for such tests;
- modeling optical loss-plus-noise with a thermal beam-splitter channel;
- the existence of hybrid entanglement after thermal noise.

The sharper candidate result is:

> **For the phase-insensitive thermal attenuator, every nontrivial finite binary coherent hybrid probe is NPT if and only if the channel is non-entanglement-breaking, and a matched $2\times2$ principal-minor witness detects that exact boundary.**

The gravitational result then uses that exact channel characterization inside a retarded source-to-receiver branch-mode transfer problem.

---

## 4. Remaining search target

The strongest possible prior-art threat is a general theorem showing that a binary coherent-state hybrid probe is already known to be a complete detector of the thermal attenuator's EB transition. No such theorem has been located in the targeted searches so far.
