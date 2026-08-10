# AGENTS.md — Experiment 02 Recovery Protocol

## Status

Experiment 02 has completed its internal AI research loop.

**Current mode:** submission/final external review only unless a concrete technical defect or exact prior-art collision appears.

Repository-wide AI-first policy:

`../../AI_RESEARCH_PROTOCOL.md`

Experiment 01 / V7 remains frozen and must not be modified from Experiment 02 work.

---

## Current manuscript

Title:

**An Inertia-Controlled Throughput Bound for Passive Gravitational Transduction**

Source:

`manuscript_v1/`

Current internally approved length: **13 pages**.

The earlier 20-page version is superseded by the compressed manuscript.

---

## Canonical theorem

For separated compact passive nonrelativistic linear-harmonic endpoints in weak quadrupolar wave-zone gravity,

```math
\Gamma_{\rm coh}
=\frac1{2\pi}\int_{\mathcal B}
\operatorname{Tr}[T^\dagger(\omega)T(\omega)]d\omega
```

obeys

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega^2}{12c^3R^2}\min(I_A,I_B).
}
```

The physical bound is classical. Quantum theory supplies an equivalent one-graviton normalization and secondary pure-loss channel/capacity corollaries.

---

## Proof skeleton — do not re-expand without necessity

### 1. Passive selected-port cut

```math
\Gamma_{\rm coh}
\le
\eta_{\max}\min[
\operatorname{Tr}(K_{g,A}^\dagger K_{g,A}),
\operatorname{Tr}(K_{g,B}^\dagger K_{g,B})].
```

This is generic passive systems mathematics.

### 2. Endpoint inertia resource

```math
\sum_n\frac{q_n:q_n}{\mu_n}\le\frac{20}{3}I,
```

```math
\sum_nMA_{Gn}\le\frac{40}{3}I,
```

```math
\operatorname{Tr}(K_g^\dagger K_g)
\le\frac{4G}{3c^5}I\Omega^4.
```

The tidal fields, STF completeness, and modal-participation method are historical/established. Do not present the `20/3` identity as new mathematics.

### 3. Compact normalized TT propagation

```math
\|P_g\|_{\rm op}^2
\le\frac{25}{16(kR)^2}.
```

The `D=5/2` directivity law is historical.

### 4. Combine

With `k=omega/c`,

```math
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega^2}{12c^3R^2}\min(I_A,I_B).
```

---

## Closed technical clarifications

### Countably infinite modes

The passive endpoint theorem extends directly to separable **bounded-port Markov modal Hilbert spaces**:

```math
0\le P_u(\tau)
\le I-T(\tau)T^\dagger(\tau)
\le I.
```

The inertia bound makes `K_g` Hilbert--Schmidt, giving the same selected-port `H2` bound.

Do not say this covers arbitrary unbounded boundary-controlled PDEs or non-Markov continua.

Canonical audit:

`INFINITE_DIMENSIONAL_PASSIVE_H2_AUDIT_2026-08-09.md`

### Passive recurrence — corrected wording

The exact two-endpoint recurrent propagator obeys

```math
P_{\rm eff}
=(I-P_{BA}R_AP_{AB}R_B)^{-1}P_{BA},
```

and for reciprocal one-hop power ceiling `eta`,

```math
\boxed{
\eta_{\rm rec}
\le\frac{\eta}{(1-\eta)^2}
\le\eta+O((kR)^{-4}).
}
```

The final relation is an **upper-bound asymptotic**. Do not restore the superseded equality

```math
\eta_{\rm rec}=\eta+O((kR)^{-4}).
```

The actual recurrent transfer may be smaller because of interference.

Canonical audit:

`RECURRENT_SCATTERING_WAVEZONE_AUDIT_2026-08-09.md`

### Classical / quantum normalization

```math
\kappa_{g,n}
=\frac{GMA_{Gn}\omega_n^4}{10c^5}
=\frac{2G\omega_n^5}{5\hbar c^5}Q^{01}:Q^{10}.
```

No factor-of-two or `2 pi` mismatch was found.

### Modern multimode stress test

For the Tobar--Pikovski--Tobar multimode architecture, the gravitationally driven coordinate is redistributed among hybrid modes with

```math
\sum_j|P_{1j}|^2=1.
```

Do not misstate the theorem as forbidding improved readout transduction or spectral coverage. It forbids passive multiplication of the cumulative external gravitational resource.

---

## Prior-art boundary

Do **not** claim novelty for

- gravitational generator--receiver calculations;
- resonant-mass eigenmode / STF tidal theory;
- gravitational effective area and reciprocity;
- `Q`-independent integrated response;
- compact quadrupole directivity / `D=5/2`;
- gravitational response sum-rule methodology;
- modal participation / effective-mass completeness;
- passive finite/infinite-dimensional `H2` machinery;
- generic source--receiver singular channels;
- two-body material-response + Green-operator transfer architecture;
- multiple-scattering / Redheffer composition;
- generic continuous-time frequency-integrated transducer metrics.

The only surviving candidate contribution is the exact gravity-specific two-ended inertia closure

```math
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega^2}{12c^3R^2}\min(I_A,I_B).
```

Rudenko's 2003 complete generator--receiver Hertz-experiment calculation is the strongest additional historical end-to-end near-collision found. It does not state the final inertia-only spectral-area theorem.

This remains a negative-search conclusion, not proof of priority.

Never use `first`, `unique`, `unprecedented`, or equivalent language without substantially stronger external evidence.

---

## AI adversarial review

Round 1 is preserved on branch

`experiment-02-ai-adversarial-review-2026-08-09`.

Its meta-referee returned `MAJOR REVISION` and recommended compression rather than additional theorem development.

Round 2 is in

`ai_adversarial_review_round2/`.

Results:

```text
historical claim discipline:       PASS
generic-method positioning:        PASS
scope/operator audit:              PASS
final AI meta-referee:             GO
```

Final report:

`ai_adversarial_review_round2/META_REFEREE_FINAL.md`

These are role-separated AI audits, not independent human peer review.

---

## Validation

Final-title manuscript:

```text
run 31351144558
job 93342080071
PASS
```

Final-title physics:

```text
run 31351144554
job 93342080258
PASS
```

Six physics regressions pass:

1. exact two-port spectral bound;
2. passive selected-port `H2` cut;
3. classical modal resource;
4. recurrent-scattering upper bound;
5. TT propagation;
6. microscopic gravitational-port factorization.

---

## Canonical reading order

1. `CURRENT_STATE.md`
2. `README.md`
3. `manuscript_v1/main.tex`
4. `ai_adversarial_review_round2/META_REFEREE_FINAL.md`
5. `PUBLICATION_GO_NO_GO.md`
6. `INFINITE_DIMENSIONAL_PASSIVE_H2_AUDIT_2026-08-09.md`
7. `RECURRENT_SCATTERING_WAVEZONE_AUDIT_2026-08-09.md`
8. `LOBO_SPHERICAL_MODAL_COMPLETENESS_COLLISION_AUDIT_2026-08-09.md`
9. `TOBAR_MULTIMODE_BAR_STRESS_TEST_2026-08-09.md`

---

## Hard stop

Do not internally broaden this paper to

- arbitrary interacting/non-Markov matter;
- unbounded PDE boundary control;
- active/inverted or parametrically driven systems;
- extended phased apertures;
- higher multipoles / relativistic beaming;
- near-field gravity;
- relay/repeater networks or external cavities;
- curved backgrounds;
- universal gravitational quantum-capacity statements.

The AI research loop is complete. Reopen only for a concrete technical defect, exact prior-art collision, or actual referee objection.

Human specialists are a **final external validation layer**, not an internal iteration dependency.
