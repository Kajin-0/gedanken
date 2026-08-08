# Scope Audit — The \(25/[16(kR)^2]\) Storage Coefficient

**Date:** 2026-08-08  
**Status:** **NOVELTY DOWNGRADE, NORMALIZATION RETAINED**

## 1. Question

The V5 source-to-receiver calculation uses

$$
\boxed{
\eta_{\rm store}
=\frac{25\mathcal O}{16(kR)^2}
}
$$

for the leading aligned plus-quadrupole wave-zone storage fraction.

The coefficient has been checked in the repository by

1. the retarded source-receiver self-energy;
2. input-output normalization;
3. source radiation pattern × resonant absorption area;
4. an electromagnetic dipole control calculation.

The question here is whether the numerical factor

$$
25/16
$$

should itself be treated as a novel gravitational result.

**Verdict: no.**

The coefficient is best understood as the product of

- a standard source directivity factor for the chosen plus quadrupole; and
- the standard single-channel critical-coupling absorption bound for an \(l=2\) spherical-wave channel.

Its role in V5 is therefore a **correctly normalized interface coefficient**, not a new universal absorption theorem.

---

# 2. Source-side directivity

For the aligned plus-type STF quadrupole

$$
Q_{ij}=q\,\mathrm{diag}(1,-1,0),
$$

the polarization-summed on-axis radiation fraction used in the repository is

$$
\boxed{
\frac{1}{P_G}
\frac{dP_G}{d\Omega}\bigg|_{\hat z}
=\frac{5}{8\pi}.}
$$

This is a property of the ordinary quadrupole radiation pattern. It is not a new quantum-gravity effect.

---

# 3. Receiver-side critical-coupling area

For a passive resonance coupled to one normalized three-dimensional spherical-wave channel, standard partial-wave / temporal coupled-mode theory gives a maximum **absorptive** cross section per angular-momentum/polarization channel

$$
\boxed{
\sigma_{{\rm abs},l}^{\max}
=\frac{(2l+1)\pi}{2k^2}.}
$$

The factor of one half relative to the larger unitary scattering/extinction scale is the critical-coupling absorption penalty: on resonance, useful internal absorption competes with reradiation.

For

$$
l=2,
$$

$$
\boxed{
\sigma_{{\rm abs},2}^{\max}
=\frac{5\pi}{2k^2}.}
$$

This structure is generic wave-scattering physics, not specifically gravitational.

A useful primary coupled-mode reference is:

- Z. Ruan and S. Fan, “Temporal coupled-mode theory for light scattering by an arbitrarily shaped object supporting a single resonance,” **Phys. Rev. A 85, 043828 (2012)**.

Their result establishes the general wavelength/directivity-controlled resonant scattering/absorption framework from which the same single-channel critical-coupling scale follows.

---

# 4. Gravitational reciprocity is independently established

The gravitational resonator literature independently derives both spontaneous graviton emission and stimulated graviton absorption from the same quadrupolar matter-field coupling.

For example, the single-graviton acoustic-resonator work derives a spontaneous gravitational transition rate and the corresponding stimulated absorption/emission rate from the quantized interaction Hamiltonian.

Thus the use of the same gravitational matrix element for emission and absorption in the V5 reciprocity check is not a novel principle.

Relevant source:

- G. Tobar et al., “Detecting single gravitons with quantum sensing,” **Nature Communications 15, 7229 (2024)**.

The later Toccacelo et al. receiver work likewise uses an explicit resonant graviton–phonon beam-splitter Hamiltonian for an incoming GW mode.

---

# 5. Reconstructing \(25/16\)

For a receiver located on the source \(+z\) axis, the intercepted/absorbed fraction in the point-receiver wave-zone approximation is

$$
\eta
=
\left[
\frac1{P_G}
\frac{dP_G}{d\Omega}
\right]_{z}
\frac{\sigma_{\rm abs}}{R^2}.
$$

Insert

$$
\frac1{P_G}
\frac{dP_G}{d\Omega}\bigg|_z
=\frac5{8\pi},
$$

and the critical \(l=2\) absorption area

$$
\sigma_{{\rm abs},2}^{\max}
=\frac{5\pi}{2k^2}.
$$

Then

$$
\boxed{
\eta
=\frac5{8\pi}
\frac{5\pi}{2k^2R^2}
=\frac{25}{16(kR)^2}.}
$$

For imperfect normalized source/receiver mode matching,

$$
\boxed{
\eta_{\rm store}
=\frac{25\mathcal O}{16(kR)^2}.}
$$

This is exactly the coefficient obtained independently from the retarded self-energy/input-output calculation.

---

# 6. Why the old factor four was wrong

The repository previously encountered

$$
\frac{25}{4(kR)^2},
$$

which is four times larger.

That larger scale corresponds to using the **unitary scattering/extinction** maximum rather than the useful critically coupled absorptive/storage maximum.

For the quantum-memory/state-transfer problem, one needs the amplitude that enters and remains in the receiver mode. Therefore the appropriate normalization is the absorptive/storage coefficient,

$$
\boxed{
\frac{25}{16(kR)^2}.}
$$

This distinction remains a valuable normalization result even though the underlying partial-wave limits are standard.

---

# 7. What is still useful in V5

The coefficient should remain prominently in the paper because it connects two separately normalized physical descriptions:

$$
\boxed{
\Sigma_{BA}^R
\quad\longleftrightarrow\quad
\text{source travelling mode}
\quad\longleftrightarrow\quad
\text{receiver input port}.
}
$$

The useful statement is:

> For the aligned compact plus-quadrupole geometry, the retarded self-energy normalization agrees with the standard directivity × critical-coupling absorption picture and yields the travelling-mode storage fraction \(25/[16(kR)^2]\).

That is stronger than presenting an unexplained geometric prefactor and safer than claiming a new cross-section law.

---

# 8. Literature-search result for complete transducers

A targeted search also found prior proposals for

- stimulated graviton absorption by quantum acoustic resonators;
- graviton-magnon resonant detection;
- superconducting gravitational/electromagnetic transducers.

These occupy broad ideas of gravitational transduction, emission/absorption reciprocity, and source/receiver antenna concepts.

No inspected source in this pass was found deriving the specific V5 chain

$$
\beta_{g,A}
\times
\frac{25\mathcal O}{16(kR)^2}
\times
\beta_{g,B}
\times
\text{temporal loading}
$$

for a locally initialized conserved source followed by a noisy entanglement-preserving receiver.

Again, this is a targeted-search result, not proof of priority.

---

# 9. Manuscript consequence

## Remove/downgrade

Do not write that

$$
25/[16(kR)^2]
$$

is a new fundamental gravitational cross section.

Do not write that resonant graviton absorption/storage is new.

Do not use the factor-of-four correction as a headline discovery unless the historical literature comparison is much more exhaustive.

## Retain

Use the coefficient as

1. an independently cross-checked source→receiver normalization;
2. the explicit geometric factor in the end-to-end link budget;
3. a clean bridge between retarded Green-function and antenna/partial-wave language;
4. evidence that the V5 interfaces are mutually consistent.

---

# 10. Current strongest V5 quantitative result after this downgrade

The distinctive quantity is not \(25/16\) in isolation. It is the complete factorization

$$
\boxed{
\tau_{A\to B}^{\max}
=4e^{-2}
\beta_{g,A}
\beta_{g,B}
\frac{25\mathcal O}{16(kR)^2}
}
$$

in the fast-encoder optimized passive limit, together with the finite-\(g\), thermal, finite-source, and reciprocal-feedback corrections.

Each factor has prior conceptual antecedents. The candidate contribution is that all factors arise from one explicit source-resolved gravitational construction and are normalized consistently across the interfaces.
