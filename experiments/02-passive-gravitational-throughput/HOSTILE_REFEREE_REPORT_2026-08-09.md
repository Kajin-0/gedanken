# Hostile Referee-Style Assessment — Experiment 02

## Recommendation

**Technically promising, but publication significance is borderline and depends entirely on the final gravity-specific closure.**

If submitted as a broad claim about gravitational quantum transduction, efficiency--bandwidth tradeoffs, antenna reciprocity, modal sum rules, or singular-channel transfer, I would recommend rejection because those ingredients are established.

If submitted as a short, tightly scoped theorem paper whose contribution is explicitly

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega^2}{12c^3R^2}
\min(I_A,I_B),
}
```

for compact passive linear-harmonic source and receiver networks, with all historical ingredients credited, I would regard it as potentially publishable after specialist verification of the remaining subsystem/normalization assumptions.

The present state is much stronger than the earlier quantum-first framing because the main result is now exposed as a classical physical bound with quantum-information corollaries rather than as a purportedly fundamental quantum theorem.

---

# 1. What I think the paper actually contributes

Almost every method in the derivation has identifiable prior art:

```text
compact gravitational antenna eigenmodes       old
emission/reception reciprocity                 old
Q-independent integrated response              old
compact quadrupole directivity                 old
gravity-specific material-response sum rules   old
modal participation / effective modal mass     old
passive H2 / Gramian identities                old
source-receiver singular wave channels         old
two-body response + propagation bounds         old
```

The only potentially new object is the **closed gravitational consequence** obtained when these pieces are forced to coexist in the same passive direct-link problem:

```text
source passive local-port network
        ↓
source total gravitational coupling trace
        ↓
compact TT free-space channel
        ↓
receiver total gravitational coupling trace
        ↓
receiver passive local-port network
```

with both endpoint traces eliminated in favor of the matter inertias.

The result then states something that none of the individual ingredients states alone:

> Increasing passive quality factor, adding arbitrarily many passive resonances, coherently mixing them into bright modes, or rotating within the compact quadrupole channel cannot raise the frequency-integrated end-to-end transfer above one explicit inertia-controlled ceiling.

That is the publication case.

---

# 2. Strongest aspect: the final parameter elimination

The best feature of the theorem is not the numerical coefficient `25/12`; it is the disappearance of phenomenological architecture parameters.

A device-level calculation normally contains

```text
Q factors
external coupling rates
internal loss rates
branching fractions
individual modal oscillator strengths
mode count
internal mixing matrices
quadrupole orientation.
```

The theorem removes all of them from the ceiling and leaves only

```math
G,\;c,\;\omega,\;R,\;I_A,\;I_B.
```

That is genuinely useful if correct because it answers a practical theoretical question:

> Can a cleverer **passive compact** architecture evade the terrible gravitational coupling merely by resonant engineering?

Inside the stated class the answer is no.

This is more compelling than presenting the work as another gravitational antenna calculation.

---

# 3. Strongest new intermediate statement

The cleanest material relation is

```math
\boxed{
\sum_n M A_{Gn}\le\frac{40}{3}I.
}
```

However, I would not sell this as a new mathematical sum-rule method. Its proof is a generalized modal-participation/effective-mass completeness argument:

```math
\sum_n\frac{|\langle w_n,g\rangle|^2}{\mu_n}
\le\|g\|^2.
```

The gravity-specific content is instead

```math
(g^{ij})_k
=\delta_{ik}x_j+\delta_{jk}x_i
-\frac23\delta_{ij}x_k
```

and

```math
\sum_{ijk}|(g^{ij})_k|^2
=\frac{20}{3}r^2,
```

which turns standard modal completeness into the gravitational effective-area bound.

This is a respectable specialization, not a new completeness theorem.

---

# 4. Major technical question: finite H2 realization versus an infinite elastic spectrum

The passive cut-set theorem is stated for a stable finite-dimensional passive realization, whereas an elastic continuum has an infinite normal-mode spectrum.

I do not see a counterexample because every modal gravitational contribution is nonnegative and the cumulative modal resource is bounded. Nevertheless the manuscript should make the limiting logic explicit:

1. apply the H2 theorem to any finite retained band-local modal sector;
2. apply the modal-completeness bound to that same subset;
3. the bound is uniform in the retained mode count;
4. if an infinite-sector limit is required, take the monotone limit only when the corresponding passive transfer operator is well defined/trace class.

Without such a sentence, “arbitrarily many modes” can sound stronger mathematically than the finite-dimensional theorem actually proves.

**Assessment:** likely a clarification, not a fatal defect.

---

# 5. Major physical question: one-way propagation versus a common gravitational bath

The microscopic factorization

```math
G_B^\dagger U_R G_A
=
\Gamma_{g,B}^{1/2}P_g\Gamma_{g,A}^{1/2}
```

is clean, and the port-overlap numerics with nonorthogonal radiation patterns are useful.

The remaining conceptual question is the subsystem boundary. Two radiating matter systems coupled to the same gravitational continuum generally admit

- reciprocal backaction;
- collective damping;
- multiple scattering;
- coherent bath-mediated interactions.

The present theorem removes these by assuming a weak **one-way direct wave-zone channel**. That is a legitimate architecture class, but it must remain conspicuous. A referee should not be left to infer that the theorem also bounds the fully recurrent two-body scattering problem.

A useful sentence would state that the result is the first-Born/one-pass direct-link ceiling; recurrent propagation or strongly hybridized common-bath normal modes define a different network problem.

**Assessment:** scope condition, not presently a contradiction.

---

# 6. The `25/16` factor is no longer a novelty risk

The wave-zone coefficient has unusually strong internal support:

1. historical compact antenna directivity reaches `5/2`;
2. reciprocal far-field transfer gives

```math
D_AD_B\left(\frac{\lambda}{4\pi R}\right)^2
=\frac{25}{16(kR)^2};
```

3. the normalized TT angular-mode calculation gives the same coefficient;
4. the aligned-plus exact outgoing polynomial reproduces the same leading term.

I would not spend further manuscript space defending its novelty. Its value is as a normalization anchor.

**Assessment:** strong.

---

# 7. Classical-to-quantum bridge is now cleaner

The historical effective-area normalization and the one-quantum linewidth agree exactly:

```math
\kappa_{g,n}
=\frac{GMA_{Gn}\omega_n^4}{10c^5}
=\frac{2G\omega_n^5}{5\hbar c^5}Q^{01}:Q^{10}.
```

This is an important consistency check.

The manuscript is correct to remove “Quantum” from the title. The headline bound contains no intrinsically quantum resource and can be derived from classical passive linear systems, classical modal completeness, and classical reciprocal propagation.

The genuinely quantum content begins when the same transfer matrix is interpreted as a bosonic channel and one asks about

```text
finite-use entanglement
antidegradability
unassisted quantum capacity
two-way-assisted capacity.
```

**Assessment:** the revised scope is substantially more defensible.

---

# 8. Novelty/significance objection remains serious

A skeptical expert can summarize the derivation as

> “Hirakawa effective area + standard modal participation + passive H2 + Friis/TT.”

That summary is not entirely unfair.

The paper therefore needs to demonstrate why performing the closure is not trivial bookkeeping. The strongest answer is that no one ingredient implies the final no-go against **all four passive escape routes simultaneously**:

```text
high Q
parallel resonances
coherent bright-mode engineering
compact quadrupole orientation.
```

The cumulative theorem converts those separate observations into one architecture-independent spectral-area ceiling.

If the intended journal expects a new mathematical technique, I would not expect acceptance. If it values a clean physics bound that closes a long-standing engineering intuition into an explicit theorem, the paper is defensible.

---

# 9. Sharpness: acceptable for a bound paper, but do not oversell the coefficient

The explicit compact plus realization

- reaches 30% of the endpoint modal/EWSR resource ceiling;
- saturates the compact TT geometry ceiling;
- does not simultaneously saturate the complete end-to-end theorem.

This is sufficient to show that the scaling is physically represented rather than purely formal.

It is not sufficient to claim that `25/12` is globally optimal.

The manuscript already avoids that claim and should continue to do so.

**Assessment:** acceptable.

---

# 10. Quantum-capacity corollaries are useful but secondary

For the vacuum pure-loss specialization,

```math
\eta_{\max}\le\frac12
\Rightarrow Q_1=0
```

and

```math
Q_2
\le
\frac{\Gamma_{\rm coh}}
{\ln2(1-\eta_{\max})}.
```

These are conceptually useful because they explain why a nonzero finite-use entanglement signal does not imply nonzero asymptotic unassisted capacity.

They should not be used to inflate the novelty of the classical throughput theorem.

**Assessment:** retain as corollaries.

---

# 11. Recommended final paper identity

The manuscript should read as a short theorem paper in classical gravitational transduction with a quantum-information coda.

Best one-sentence identity:

> **Passive resonant engineering can redistribute compact gravitational oscillator strength in frequency and among modes, but for a direct wave-zone link the total integrated source-to-receiver transfer remains bounded by the smaller endpoint inertia resource and free-space quadrupole propagation.**

Best equation:

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega^2}{12c^3R^2}
\min(I_A,I_B).
}
```

Everything else should support those two statements.

---

# 12. Referee scores at the present checkpoint

These are subjective publication-risk scores, not measurements.

```text
internal mathematical consistency:       8.5 / 10
normalization confidence:                9.0 / 10
scope discipline:                        9.0 / 10
novelty of individual ingredients:       2.0 / 10
novelty of exact closed inequality:      6.0 / 10
physical usefulness of the closure:      7.5 / 10
broad-field significance:                5.5 / 10
specialist gravitational-antenna value:  7.0 / 10
publication readiness after current edits:
                                          7.5 / 10
```

---

# Final referee verdict

**I would not reject this because the physics is obviously inconsistent.**

I would challenge the paper on whether the final closure is sufficiently nontrivial relative to its established ingredients. If the authors maintain the present restrained positioning, explicitly close the finite-mode/infinite-mode wording, keep the one-way architecture boundary visible, and avoid priority rhetoric, I would support publication as a focused theoretical bound rather than as a fundamental new principle of gravity or quantum information.

The next useful epistemic step is an actual gravitational-antenna / passive-wave specialist trying to identify either

1. an equivalent published inertia-closed two-ended theorem under different notation, or
2. a hidden failure of the H2-to-gravitational-continuum interface.

Absent one of those, further internal generalization is more likely to dilute the result than strengthen it.
