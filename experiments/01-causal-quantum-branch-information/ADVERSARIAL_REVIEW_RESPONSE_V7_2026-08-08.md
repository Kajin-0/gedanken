# Adversarial Referee Pass on V7 — 2026-08-08

**Scope:** current V7 manuscript after external-review closure.  
**Question:** does the strongest conceptual referee critique expose a new physics failure, or mainly a framing/interpretation risk?

## Overall verdict

No new algebraic or structural physics failure was found.

The critique identified two real presentation vulnerabilities:

1. the four-factor result could be mistaken for a bookkeeping identity if the common physical normalization is not stated immediately;
2. the passive benchmark could be misread as a universal gravitational efficiency bound.

Both points have now been made explicit in the manuscript.

The remaining objections were already addressed by the existing derivations but are recorded below because they are exactly the questions a strong referee is likely to ask.

---

## 1. Is the central factorization only bookkeeping?

Central result:

```math
\tau_c(t)=
\beta_{g,A}\,
\eta_{\rm store}(R)\,
\beta_{g,B}\,
\mathcal T_f(t).
```

### Referee concern

A product of emission, propagation, absorption, and temporal-overlap efficiencies is structurally familiar. If each factor were independently assumed, the multiplication would not by itself be a new physical result.

### V7 answer

The contribution is the common operational normalization connecting all stages without inserting an already normalized incoming graviton wavepacket.

Specifically:

- source branching is measured relative to the complete locally prepared branch-distance norm;
- propagation is independently normalized as a source-to-receiver one-graviton mode overlap;
- receiver branching is normalized to the actual receiver linewidth;
- memory capture and later readout remain distinct.

The manuscript now states this directly in the abstract, the link-budget derivation, and the discussion.

**Status: CLOSED as a framing vulnerability.**

The residual publication question is editorial rather than algebraic: whether a referee considers this integration sufficiently consequential for the journal.

---

## 2. Is source gravitational branching an unavoidable fundamental penalty?

```math
\beta_{g,A}=\frac{\kappa_{g,A}}{\kappa_A}.
```

### Referee concern

If nongravitational damping vanishes, then

```math
\kappa_A=\kappa_{g,A}
\quad\Rightarrow\quad
\beta_{g,A}=1.
```

Therefore the small branching fraction in the benchmark cannot be a universal gravitational bound.

### V7 answer

Correct. The small value is a finite-bandwidth passive operating point, not a fundamental constant of matter.

For the benchmark, the intrinsic gravitational linewidth is approximately

```math
\kappa_g\simeq6.87\times10^{-26}\,\mathrm{s}^{-1},
```

corresponding to a characteristic gravitational lifetime of roughly

```math
4.6\times10^{17}\ \mathrm{yr}.
```

A source can raise gravitational branching toward unity by removing faster nongravitational loss, but then emission becomes correspondingly slow. Conversely, adding ordinary loss shortens the source lifetime and reduces gravitational branching.

The manuscript now states explicitly that this is a speed--loss tradeoff.

**Status: CLOSED.**

---

## 3. How universal is the four-spoke result?

### Referee concern

The explicit conserved four-spoke elastic quadrupole proves consistency for one source architecture. It does not prove that all gravitational quantum emitters share the same microscopic branching behavior.

### V7 answer

Agreed and already scoped correctly.

The four-spoke construction is an existence proof that a finite-support conserved source can realize the required branch quadrupole while including its support and controller.

The passive spectral-weight bound is explicitly restricted to passive, stationary, nonrelativistic matter. The manuscript does not extend it to active or inverted states, relativistic field systems, or strongly self-gravitating matter.

**Status: CLOSED by scope.**

V7 is not a universal no-go theorem for all conceivable gravitational transducers.

---

## 4. Does the one-way product survive reciprocal dynamics?

### Referee concern

The actual gravitational field is reciprocal. A fully interacting source--field--receiver system can contain reabsorption, multiple scattering, and delayed feedback.

### V7 answer

The one-way result is explicitly the leading term of a controlled weak-feedback regime.

The audited loop amplitude obeys

```math
|L(\nu)|
\le
4\eta_{\rm store}\beta_{g,A}\beta_{g,B},
```

and the first source-controlled round-trip echo appears only after approximately

```math
3R/c.
```

Thus the factorized one-way transfer is not asserted as an exact solution of arbitrary strong reciprocal coupling.

**Status: CLOSED at the stated weak one-way order.**

---

## 5. What exactly is the `25/16` quantity?

### Referee concern

Classical emitted power, extinction, scattering, absorption, coherent overlap, and stored quantum probability are not automatically the same quantity.

### V7 answer

The coefficient is supported by three conceptually distinct calculations:

1. retarded conserved-source field;
2. reciprocal radiation/absorption normalization;
3. canonical transverse-traceless one-graviton mode overlap.

The third route supplies the operational chain directly:

```math
\text{normalized emitted one-graviton mode}
\to
\text{reciprocal receiver amplitude}
\to
|t_{BA}|^2
\to
\eta_{\rm store}
```

in the weak one-way wave zone.

The manuscript now says explicitly that the storage probability is not being identified with an arbitrary classical power or extinction coefficient.

The reactive near zone remains outside this probability interpretation.

**Status: CLOSED at the stated wave-zone order.**

---

## 6. Is gravitational splitting being asked to prove too much?

### Referee concern

First-order gravitational splitting does not establish exact tensor-factor locality or absence of all exterior gravitational fields.

### V7 answer

V7 does not require either claim.

It imposes the equal-charge code condition

```math
V_{\mathcal C}^{\dagger}Q_A V_{\mathcal C}=q_A I_{\mathcal C}
```

for the total Poincare generators at the retained perturbative order.

A common long-range gravitational dressing may remain. The only claim is that the logical branch is absent from that first-order charge data before the branch-dependent retarded multipole disturbance arrives.

No exact nonperturbative subsystem theorem is claimed.

**Status: CLOSED at first perturbative order.**

---

## 7. Is the virtual difference mode physically real?

### Referee concern

The collective mode

```math
d=\frac{1}{A}\sum_j\alpha_j^* b_j
```

could be misread as a new localized oscillator or propagating physical mode.

### V7 answer

It is neither.

It is a basis-defined collective coordinate obtained by rotating the coherent displacement vector onto one mode coordinate. Its physical content is the total branch-dependent coherent norm and the projection of that norm onto actual receiver-coupled modes.

The manuscript now states this explicitly.

**Status: CLOSED as an interpretation vulnerability.**

---

# Final referee-level assessment

The strongest surviving criticism is not that V7 contains a hidden factor-of-two error or an inconsistent gravitational source. It is the higher-level question:

> Is the common source-to-readout normalization itself a sufficiently important conceptual advance beyond the already known individual ingredients?

V7 is now positioned to answer that question as strongly as the current physics permits:

```math
\boxed{
\text{receiver-local gravitational quantum sensitivity}
\neq
\text{end-to-end source-resolved quantum transfer}
}
```

because the source must first place its branch-dependent quantum record into the gravitational radiation channel.

The passive numerical benchmark near `10^{-42}` is evidence for the size of that distinction in one aggressive ordinary-matter operating point; it is not the theorem.

The durable result is the source-resolved normalized factorization together with its stated domain of validity.

## Publication verdict

**No new publication-blocking physics defect found.**

The manuscript should not reopen the main derivations on the basis of this review. The remaining uncertainty is normal referee judgment about conceptual significance, generality, and presentation.