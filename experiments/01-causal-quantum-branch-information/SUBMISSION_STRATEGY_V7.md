# V7 Manuscript Submission Strategy

**Date:** 2026-08-08  
**Target manuscript:** `manuscript_v7/`

## Recommended order

### 1. Physical Review D — first submission

Best current fit.

Why:

- the paper is fundamentally a gravitation / linearized-gravity calculation;
- it contains detailed source, radiation, receiver, causality, and gravitational-dressing analysis;
- the manuscript is long enough that a journal comfortable with detailed theoretical articles is preferable;
- the strongest contribution is a quantitative source-resolved gravitational link normalization, not a near-term device claim.

Recommended PRD framing:

> A source-resolved weak-gravity calculation showing how local quantum preparation, conserved gravitational radiation, free-space mode capture, receiver memory, noise, and accessible readout combine into one end-to-end quantum link budget.

Lead with:

$$
\tau_c
=\beta_{g,A}\eta_{\rm store}\beta_{g,B}\mathcal T_f,
$$

the equal-charge dressing-aware source construction, and the

$$
10^{-22}\to10^{-42}
$$
receiver-local versus end-to-end correction.

Do not lead with quantum-network engineering language alone.

---

### 2. Classical and Quantum Gravity — strongest specialist fallback

Very natural if PRD declines on significance/novelty rather than correctness.

Why:

- gravitational radiation and causal structure are central;
- the finite-support conserved source and gravitational dressing discussion are unusually aligned with a gravity-specialist readership;
- the paper can be presented as a careful benchmark connecting several gravitational quantum-interface descriptions.

Recommended CQG framing:

> A self-contained linearized-gravity construction from an equal-charge conserved quantum source to a remote noisy receiver, with explicit source/receiver normalization and causal support.

For CQG, emphasize

- conserved stress-energy;
- finite-support source mechanics;
- first-order gravitational dressing;
- retarded propagation;
- quadrupole response;
- scope of passive matter.

The Gaussian channel language should remain a tool rather than the front-page identity of the paper.

---

### 3. Physical Review Research — broad/interdisciplinary fallback

Useful if the paper is framed more strongly as a quantum-channel / transducer synthesis across gravitational physics and quantum information.

Recommended framing:

> An end-to-end quantum-interface accounting framework specialized to propagating linearized gravity, identifying where source branching, propagation, memory loss, waveform matching, and readout separately enter.

This version should make the conceptual link diagram especially prominent.

---

### 4. Quantum Science and Technology — not first choice

The paper touches

- quantum communication;
- quantum transduction;
- quantum sensing;
- bosonic channel theory.

However the explicit ordinary-matter benchmark is deliberately pessimistic:

$$
\eta_Q^{\rm link}\sim10^{-42}.
$$

That makes the work more naturally a gravitational capability/normalization paper than a quantum-technology proposal.

QST would become more attractive only if the paper were substantially reframed around a general transducer-design principle with clear implications beyond gravity.

---

# Manuscript changes before PRD submission

## Required

1. Keep the current title unless final external-style review finds a sharper one:

   **A Source-Resolved Quantum Link Budget for Propagating Linearized Gravity**

2. Keep the abstract explicit that the result is

   - a normalization/capability benchmark;
   - not a near-term apparatus proposal;
   - not a new Gaussian-channel theorem.

3. Main-text hierarchy should remain:

   - equal-charge local source;
   - local controller field;
   - virtual-mode handoff;
   - four-factor link;
   - memory quantum excess;
   - accessible readout;
   - exact weak-link negativity;
   - passive matter benchmark.

4. Keep the passive EWSR result as a corollary, not the title claim.

5. Keep active/collective receivers as a scoped loophole discussion, not an undeveloped second paper inside the first.

## Strongly recommended

6. Use only two main conceptual figures:

   - source geometry;
   - serial quantum-link architecture.

7. Keep the benchmark as a table rather than adding a decorative plot unless a plot materially improves the $10^{-42}\to10^{-22}\to10^{-2}$ hierarchy.

8. Keep detailed handoff, charge, EWSR, and broadening derivations in appendices.

9. Add a short data/code availability statement before submission stating that the analytic derivations and supporting numerical checks are contained in the public repository / manuscript source as appropriate.

10. Run one final external-style referee review focused on whether the end-to-end synthesis constitutes a sufficiently significant advance for PRD.

---

# Suggested cover-letter claim

Do not say "first proof" or "first gravitational quantum communication protocol."

Use something close to:

> The manuscript closes source preparation, radiative emission, free propagation, receiver capture, thermal noise, and readout in one explicitly normalized weak-gravity construction. The resulting link budget shows that receiver-local calculations can overestimate the end-to-end coherent scale by an entire source gravitational branching factor; in an aggressive ordinary-matter benchmark this changes the relevant scale from approximately $10^{-22}$ to approximately $10^{-42}$. The paper also gives a dressing-aware equal-charge source initialization and an exact weak-link entanglement measure for the resulting binary-coherent channel.

That is the strongest defensible concise claim.

---

# Submission decision

Current recommendation:

$$
\boxed{
\text{Submit to PRD first.}
}
$$

If rejected for scope/significance without a substantive technical objection:

$$
\boxed{
\text{CQG second.}
}
$$

If reviews indicate the cross-disciplinary quantum-channel synthesis is more compelling than the gravity-specific derivation:

$$
\boxed{
\text{PRR third.}
}
$$
