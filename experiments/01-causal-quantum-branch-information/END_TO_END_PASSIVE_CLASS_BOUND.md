# End-to-End Passive-Class Quantum-Transfer Ceiling

**Date:** 2026-08-08  
**Status:** **COMBINED CLASS BOUND — VALID ONLY FOR THE PASSIVE NONRELATIVISTIC QUADRUPOLE-RESPONSE CLASS**

## 1. Purpose

The current end-to-end controlled-waveform ceiling is

$$
\boxed{
\tau_{A\to B}^{\rm ctrl}(t)
\le
\beta_{g,A}
\eta_{\rm store}(R)
\beta_{g,B}
(1-e^{-\kappa_Bt}).}
$$

In particular,

$$
\boxed{
\tau_{A\to B}^{\rm ctrl}
\le
\beta_{g,A}
\eta_{\rm store}(R)
\beta_{g,B}.}
$$

This note inserts the repository's passive nonrelativistic quadrupole oscillator-strength ceiling to obtain a class-level bound on the link.

The result does **not** apply to

- inverted/active many-body receivers;
- arbitrary nonpassive collective states;
- relativistic QFT receivers;
- strongly self-gravitating objects;
- architectures that change the physical graviton coupling itself.

It is a bound for ordinary passive nonrelativistic quadrupole modes.

---

# 2. Passive quadrupole response ceiling

For a passive stationary nonrelativistic system with characteristic size

$$
L,
$$

mass compactness

$$
\boxed{
\mathcal C
=\frac{2GM}{c^2L},}
$$

and internal velocity parameter

$$
\boxed{
\beta=\frac{\omega L}{c},}
$$

the positive quadrupole-response sum rule gives

$$
\boxed{
\frac{\kappa_{g,\rm net}}{\omega}
\lesssim
\frac23\mathcal C\beta^3.}
$$

For a single passive oscillator transition or narrow mode this gives the corresponding intrinsic gravitational linewidth ceiling at the same parametric scale.

Let the total linewidth be

$$
\kappa=\omega/Q.
$$

Then the gravitational branching fraction satisfies

$$
\boxed{
\beta_g
=\frac{\kappa_g}{\kappa}
\lesssim
\frac23Q\mathcal C\beta^3.}
$$

Since a branching fraction cannot exceed unity,

$$
\boxed{
\beta_g
\lesssim
\min\left[
1,
\frac23Q\mathcal C\beta^3
\right].}
$$

---

# 3. One-ended bound: arbitrary source, passive receiver

Keep the source branching fraction

$$
\beta_{g,A}
$$

explicit, allowing the source to be a special or active architecture.

For a passive nonrelativistic receiver,

$$
\beta_{g,B}
\lesssim
\min\left[
1,
\frac23Q_B\mathcal C_B\beta_B^3
\right].
$$

Therefore even an ideally shaped gravitational source obeys

$$
\boxed{
\tau_{A\to B}^{\rm ctrl}
\lesssim
\beta_{g,A}
\eta_{\rm store}(R)
\min\left[
1,
\frac23Q_B\mathcal C_B\beta_B^3
\right].}
$$

Using the aligned compact-source wave-zone factor

$$
\eta_{\rm store}
=\frac{25\mathcal O}{16(kR)^2},
$$

$$
\boxed{
\tau_{A\to B}^{\rm ctrl}
\lesssim
\beta_{g,A}
\frac{25\mathcal O}{16(kR)^2}
\min\left[
1,
\frac23Q_B\mathcal C_B\beta_B^3
\right].}
$$

This is the most useful class bound when the source is kept explicit but the receiver is assumed to be ordinary passive matter.

---

# 4. Two-ended passive bound

If the source transition and receiver transition both belong to the passive nonrelativistic quadrupole class, then

$$
\boxed{
\tau_{A\to B}^{\rm ctrl}
\lesssim
\eta_{\rm store}(R)
\prod_{j=A,B}
\min\left[
1,
\frac23Q_j\mathcal C_j\beta_j^3
\right].}
$$

In the aligned compact-source wave zone,

$$
\boxed{
\tau_{A\to B}^{\rm ctrl}
\lesssim
\frac{25\mathcal O}{16(kR)^2}
\prod_{j=A,B}
\min\left[
1,
\frac23Q_j\mathcal C_j\beta_j^3
\right].}
$$

This bound already assumes ideal temporal mode shaping; no additional waveform penalty has been inserted.

Thus it is stronger conceptually than any particular passive-pulse calculation:

> **Even if temporal mismatch is removed completely, ordinary passive nonrelativistic matter remains suppressed by its gravitational branching fractions.**

---

# 5. Unsaturated weak-gravity regime

When

$$
\frac23Q_j\mathcal C_j\beta_j^3\ll1
$$

for both ends,

$$
\boxed{
\tau_{A\to B}^{\rm ctrl}
\lesssim
\frac{25\mathcal O}{36(kR)^2}
Q_AQ_B
\mathcal C_A\mathcal C_B
\beta_A^3\beta_B^3.}
$$

At fixed wave-zone phase distance

$$
kR=\zeta,
$$

$$
\boxed{
\tau_{A\to B}^{\rm ctrl}
\lesssim
\frac{25\mathcal O}{36\zeta^2}
Q_AQ_B
\mathcal C_A\mathcal C_B
\beta_A^3\beta_B^3.}
$$

For identical passive source and receiver modes,

$$
\boxed{
\tau_{A\to B}^{\rm ctrl}
\lesssim
\frac{25\mathcal O}{36\zeta^2}
\left(Q\mathcal C\beta^3\right)^2.}
$$

This makes the two-ended weakness explicit: the passive matter suppression enters **twice**.

---

# 6. Explicit finite-spoke V5 specialization

The V5 four-spoke mode has a more specific intrinsic linewidth than the general passive sum-rule ceiling.

Using total endpoint mass

$$
M_e=4\mu
$$

and endpoint compactness

$$
\mathcal C_e=\frac{2GM_e}{c^2L},
$$

the finite-spoke linewidth gives

$$
\boxed{
\frac{\kappa_g}{\omega}
=\frac15
\mathcal C_e\beta^3
\mathcal C_\kappa(q).}
$$

Therefore

$$
\boxed{
\beta_g
=\frac15
Q\mathcal C_e\beta^3
\mathcal C_\kappa(q).}
$$

For two V5-type devices in the unsaturated regime, the ideal controlled-waveform ceiling becomes

$$
\boxed{
\tau_{A\to B}^{\rm ctrl}
\le
\frac{\mathcal O}{16(kR)^2}
Q_AQ_B
\mathcal C_{e,A}\mathcal C_{e,B}
\beta_A^3\beta_B^3
\mathcal C_\kappa(q_A)
\mathcal C_\kappa(q_B).}
$$

At

$$
kR=\zeta,
$$

$$
\boxed{
\tau_{A\to B}^{\rm ctrl}
\le
\frac{\mathcal O}{16\zeta^2}
Q_AQ_B
\mathcal C_{e,A}\mathcal C_{e,B}
\beta_A^3\beta_B^3
\mathcal C_\kappa(q_A)
\mathcal C_\kappa(q_B).}
$$

This is the precise V5 passive-device scaling after ideal temporal shaping.

The general \(2/3\) sum-rule coefficient is looser than the explicit four-spoke coefficient \(1/5\), as expected for a class bound.

---

# 7. Matched passive exponential as a subcase

If the source is not actively shaped and one instead uses the matched natural exponential family at fixed branching fractions, multiply the controlled-waveform ceiling by

$$
\boxed{4e^{-2}\simeq0.541341.}
$$

Thus for two V5 devices,

$$
\boxed{
\tau_{A\to B}^{\rm matched\ pass}
=4e^{-2}
\frac{\mathcal O}{16\zeta^2}
Q_AQ_B
\mathcal C_{e,A}\mathcal C_{e,B}
\beta_A^3\beta_B^3
\mathcal C_\kappa(q_A)
\mathcal C_\kappa(q_B).}
$$

This is an architectural temporal penalty, not the fundamental passive-matter suppression.

---

# 8. What active temporal control cannot remove

The controlled-waveform bound already assumes the source can synthesize the receiver-optimal temporal mode.

Therefore none of the following can be blamed on poor pulse shaping:

$$
\boxed{
\mathcal C_A\beta_A^3,
\qquad
\mathcal C_B\beta_B^3,
\qquad
(kR)^{-2}.}
$$

Within the stated passive nonrelativistic class, these factors arise from

- finite quadrupole oscillator strength;
- weak gravitational coupling;
- free-space mode dilution / partial-wave overlap.

This is why active source shaping can remove a large **mismatch** penalty in special cases while still leaving an extremely weak absolute link.

---

# 9. Scope of the source factor

The two-ended bound must not be applied indiscriminately to every source.

The passive sum-rule argument assumes a stationary passive nonrelativistic state for the positive quadrupole spectral weight.

The V5 source begins from a passive harmonic mode but is later coherently driven. Its intrinsic single-quantum matrix element and linewidth are nevertheless fixed by the explicit four-spoke source formula, so the specific V5 bound in Sec. 6 remains valid for that architecture.

However a different source using

- inversion;
- active collective enhancement;
- relativistic fields;
- strongly self-gravitating modes

may evade the passive class coefficient.

In that case retain only the one-ended receiver bound and insert the source's actual

$$
\beta_{g,A}.
$$

---

# 10. Active-receiver loophole

The receiver sum rule itself identifies its loophole.

A nonpassive/inverted stationary state can have additional positive-frequency quadrupole spectral weight balanced by a negative spectral-weight/activity budget.

Therefore an active receiver may achieve

$$
\kappa_g
$$

larger than the passive \(\mathcal C\beta^3\) ceiling.

But then the receiver supplies a quantum resource and the following must be included:

- preparation energy/ergotropy;
- amplifier added noise;
- instability;
- extra branch records and environmental channels.

The present bound should therefore be advertised as a **passive-class ceiling**, not a universal prohibition on strong gravitational quantum transducers.

---

# 11. Paper-level interpretation

The V5 link has a useful hierarchy of increasingly strong assumptions.

### Pure channel factorization

$$
\tau
\le
\beta_{g,A}\eta_{\rm store}\beta_{g,B}.
$$

### Passive receiver only

$$
\tau
\lesssim
\beta_{g,A}
\frac{25\mathcal O}{16(kR)^2}
\min\left[1,\frac23Q_B\mathcal C_B\beta_B^3\right].
$$

### Passive nonrelativistic source and receiver

$$
\tau
\lesssim
\frac{25\mathcal O}{16(kR)^2}
\prod_{j=A,B}
\min\left[1,\frac23Q_j\mathcal C_j\beta_j^3\right].
$$

### Explicit V5 four-spoke devices

$$
\tau
\le
\frac{\mathcal O}{16\zeta^2}
Q_AQ_B
\mathcal C_{e,A}\mathcal C_{e,B}
\beta_A^3\beta_B^3
\mathcal C_\kappa(q_A)
\mathcal C_\kappa(q_B)
$$

in the unsaturated ideal-controlled-waveform limit.

This nested structure makes clear exactly which assumptions are responsible for each suppression.

---

# 12. Adversarial verdict

The dominant weakness of the ordinary-matter V5 link is not the \(4e^{-2}\) passive waveform coefficient.

Even after granting ideal coherent temporal shaping,

$$
\boxed{
\tau_{A\to B}
\lesssim
\beta_{g,A}\eta_{\rm store}\beta_{g,B}.}
$$

For passive nonrelativistic matter, each

$$
\beta_g
$$

is itself bounded by a compactness/internal-velocity oscillator-strength scale.

Therefore the central practical obstacle is **weak matter–gravity branching at both interfaces**, not merely temporal mismatch.

This is the cleanest class-level explanation currently available for why the end-to-end ordinary-matter link is so small.
