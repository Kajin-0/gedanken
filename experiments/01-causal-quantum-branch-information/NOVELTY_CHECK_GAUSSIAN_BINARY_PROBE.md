# Novelty Check — Binary Coherent Probe Completeness for Phase-Insensitive Gaussian Channels

**Timestamp:** 2026-08-07 17:32 EDT  
**Status:** Targeted primary-literature check; no equivalent theorem located yet.

## Candidate theorem

For every nontrivial finite binary coherent hybrid state

$$
|\Psi\rangle
=\sqrt p|0\rangle|\alpha\rangle
+e^{i\phi}\sqrt{1-p}|1\rangle|\beta\rangle,
$$

with $0<p<1$ and $\alpha\neq\beta$, and every one-mode gauge-covariant phase-insensitive Gaussian channel $\Phi_{\tau,m}$,

$$
\boxed{
(I\otimes\Phi_{\tau,m})(|\Psi\rangle\langle\Psi|)
\text{ is NPT}
\iff
m<\tau,
}
$$

where $m<\tau$ is exactly the non-entanglement-breaking region.

The associated matched principal-minor witness reaches the same exact boundary.

---

## 1. Established channel-level result: Mele, Lami & Giovannetti

**Francesco Anna Mele, Ludovico Lami, Vittorio Giovannetti,** “Maximum tolerable excess noise in continuous-variable quantum key distribution and improved lower bound on two-way capacities,” arXiv:2303.12867; later published in *Nature Photonics*.

They study all phase-insensitive bosonic Gaussian channels:

- thermal attenuators;
- thermal amplifiers;
- additive Gaussian noise.

They prove that the energy-constrained two-way quantum capacity is strictly positive **if and only if** the channel is not entanglement breaking.

Their explicit protocol is not a binary coherent-state hybrid probe. It begins with finite-dimensional Fock-state entanglement of the form

$$
|\Psi_{M,c}\rangle
=c|0\rangle|0\rangle
+\sqrt{1-c^2}|M\rangle|M\rangle,
$$

followed by local projection, twirling, recurrence, and hashing/distillation steps.

Thus this work establishes the broad statement

$$
\text{non-EB phase-insensitive Gaussian channel}
\Rightarrow
\text{some entanglement-distribution protocol exists},
$$

but does not appear to establish

$$
\text{every nontrivial binary coherent hybrid probe remains NPT}.
$$

This distinction matters because the current theorem uses a fixed minimal Schmidt-rank-two hybrid family with no channel-dependent optimization of input dimension.

---

## 2. Earlier two-coherent-state device tests

Häseler, Moroder & Lütkenhaus (PRA 77, 032303, 2008) already use two nonorthogonal coherent states and the effective-entanglement representation to test quantum devices.

Their experimentally motivated criteria are built from limited measured moments and can be necessary/sufficient for compatibility of those **moment data** with a separable explanation under specific symmetric assumptions. Their noise boundary depends on the coherent-state overlap.

This establishes the two-coherent-state testing paradigm, but not the exact output-state NPT/EB equivalence derived here.

See `PRIOR_ART_BINARY_COHERENT_TESTS.md`.

---

## 3. Exact same hybrid state under thermal attenuation

Kreis & van Loock (PRA 85, 032307, 2012) study

$$
(|0\rangle|\alpha\rangle+|1\rangle|-\alpha\rangle)/\sqrt2
$$

through a one-sided thermal beam-splitter channel.

They derive the exact noisy hybrid state but use a finite-order Shchukin–Vogel moment determinant. Their sufficient thermal-entanglement region depends on $|\alpha|$.

They explicitly note that their witness may fail to detect entangled states in part of the region where the thermal attenuator is not entanglement breaking.

The present theorem appears to close that gap for all finite nonzero coherent separations and then generalizes beyond attenuation.

See `NOVELTY_CHECK_FINITE_CAT.md`.

---

## 4. Non-Gaussian robustness literature

Sabapathy, Ivan & Simon (PRL 107, 130501, 2011) develop analytic noisy attenuator/amplifier methods and study survival of non-Gaussian entanglement, including NOON and photon-number entangled families.

Filippov & Ziman (2014) study general entanglement sensitivity to attenuation and amplification and exhibit non-Gaussian states robust under broad gain/noise regimes.

These works demonstrate that non-Gaussian entanglement can survive very noisy phase-insensitive channels, but the targeted search did not locate the binary coherent hybrid completeness theorem above.

---

## 5. Current novelty boundary

### Established and not new

- channel classification and EB thresholds for phase-insensitive Gaussian channels;
- entanglement distribution whenever such a channel is non-EB;
- binary coherent-state testing of quantum devices;
- hybrid coherent/qubit entanglement;
- thermal attenuation of hybrid coherent cats;
- non-Gaussian entanglement robustness under attenuation/amplification.

### Candidate new statement

$$
\boxed{
\text{Every nontrivial finite binary coherent hybrid probe is NPT}
\iff
\text{the gauge-covariant phase-insensitive Gaussian channel is non-EB.}
}
$$

Together with the exact channel-matched $2\times2$ principal-minor witness, this is substantially more specific than the known existence/capacity statements.

No exact equivalent was found in the targeted searches performed through 2026-08-07.

---

## 6. Remaining novelty threats

Before claiming originality, search for:

1. structural theorems on finite coherent-state alphabets detecting Gaussian entanglement-breaking channels;
2. papers citing Häseler et al. that upgrade the two-state effective-entanglement test to exact output-state conditions;
3. papers citing Kreis & van Loock that compute full NPT spectra or exact negativity of their thermal hybrid state;
4. general results on Schmidt-rank-two probes for one-mode Gaussian channels;
5. Gaussian-channel divisibility/entanglement-annihilation papers that may contain an equivalent corollary.

---

## 7. Current assessment

The theorem is now plausible as a **standalone quantum-information lemma**, with the gravitational causal-front construction as its physical application.

The safest wording remains:

> A targeted literature search found strong neighboring results but has not yet found the exact binary coherent probe completeness theorem or matched exact witness. Novelty is promising but unverified.
