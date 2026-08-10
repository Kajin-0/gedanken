# Experiment 02 — Passive Gravitational Throughput

## Current result

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

The theorem is a **classical passive resource bound**. Quantum theory gives an equivalent one-graviton normalization and downstream pure-loss channel corollaries.

Current manuscript:

**An Inertia-Controlled Throughput Bound for Passive Gravitational Transduction**

`manuscript_v1/`

The internally approved manuscript is 13 pages, down from the earlier 20-page development-heavy version, with the rigorous appendices retained.

---

## Proof in four lines

### Passive cut

```math
\Gamma_{\rm coh}
\le
\eta_{\max}\min[
\operatorname{Tr}(K_{g,A}^\dagger K_{g,A}),
\operatorname{Tr}(K_{g,B}^\dagger K_{g,B})].
```

### Endpoint inertia resource

```math
\sum_nMA_{Gn}\le\frac{40}{3}I,
```

```math
\operatorname{Tr}(K_g^\dagger K_g)
=\sum_n\kappa_{g,n}
\le\frac{4G}{3c^5}I\Omega^4.
```

### Compact TT propagation

```math
\eta_{\max}
\le\frac{25}{16(kR)^2}.
```

### Combine

With `k=omega/c` in a narrow band,

```math
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega^2}{12c^3R^2}\min(I_A,I_B).
```

---

## What the bound excludes

Within the declared class, the leading integrated ceiling cannot be increased by

- higher endpoint `Q`;
- finite or countably infinite bounded-port passive resonances;
- coherent bright/dark mode mixing;
- compact quadrupole orientation optimization;
- passive repeated returns between the same two endpoints at leading wave-zone order.

Repeated returns obey

```math
\eta_{\rm rec}
\le\frac{\eta}{(1-\eta)^2}
\le\eta+O((kR)^{-4}),
```

where the second relation is an upper-bound asymptotic. The actual recurrent transfer may be smaller because of interference.

---

## Scope

Included:

- weak linearized gravity;
- compact nonrelativistic quadrupolar matter;
- separated wave-zone propagation;
- passive time-invariant linear-harmonic endpoint dynamics;
- finite or countably infinite bounded-port Markov modal sectors;
- passive reciprocal returns between the same two endpoints at retained leading order.

Excluded:

- active gain, inversion, or parametric/time-dependent drive;
- extended phased apertures;
- added gravitational relays, mirrors, or external cavities;
- reactive near-field exchange;
- higher multipoles / relativistic or nonlinear matter;
- arbitrary unbounded PDE boundary ports without admissibility analysis;
- genuinely non-Markov continua;
- universal common-bath or quantum-capacity claims.

---

## Novelty boundary

Not claimed as new:

- gravitational source--receiver calculations;
- resonant-mass eigenmode / STF tidal theory;
- effective area, reciprocity, and `D=5/2`;
- `Q`-independent integrated gravitational response;
- modal participation / effective-mass completeness;
- gravitational response sum-rule methodology;
- passive `H2` / Gramian machinery;
- source--receiver singular channels;
- two-body response + Green-operator bounds;
- multiple-scattering / Redheffer composition;
- generic frequency-integrated transducer metrics.

The only surviving candidate contribution is the **exact gravity-specific two-ended inertia closure**. No inspected primary source has been found stating the same theorem, but that is a negative search result rather than a priority claim.

---

## AI-first review state

Repository-wide protocol:

`../../AI_RESEARCH_PROTOCOL.md`

Round 1 adversarial review is preserved on branch

`experiment-02-ai-adversarial-review-2026-08-09`.

It produced three attacks:

- historical collision;
- generic-wave reduction;
- infinite-dimensional systems attack;

followed by a meta-referee that recommended manuscript compression rather than further physics.

Round 2 is in

`ai_adversarial_review_round2/`.

All three agents passed the compressed manuscript, and `META_REFEREE_FINAL.md` gives

**GO FOR SPECIALIST SUBMISSION AFTER FINAL EDITORIAL FREEZE**.

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

Physics CI contains six independent regressions:

1. exact two-port spectral bound;
2. passive selected-port `H2` cut;
3. classical modal resource;
4. recurrent passive scattering upper bound;
5. TT propagation;
6. microscopic gravitational-port factorization.

---

## Read next

1. `CURRENT_STATE.md`
2. `manuscript_v1/main.tex`
3. `ai_adversarial_review_round2/META_REFEREE_FINAL.md`
4. `PUBLICATION_GO_NO_GO.md`
5. `INFINITE_DIMENSIONAL_PASSIVE_H2_AUDIT_2026-08-09.md`
6. `RECURRENT_SCATTERING_WAVEZONE_AUDIT_2026-08-09.md`
7. `LOBO_SPHERICAL_MODAL_COMPLETENESS_COLLISION_AUDIT_2026-08-09.md`
8. `TOBAR_MULTIMODE_BAR_STRESS_TEST_2026-08-09.md`

## Status

```text
INTERNAL AI REVIEW:             GO
PHYSICS:                        GO
MANUSCRIPT:                     GO
EXACT NOVELTY:                  PROVISIONAL
MORE INTERNAL BROADENING:       NO
HUMAN INTERNAL DEPENDENCY:      NO
NEXT EXTERNAL GATE:             FINAL SPECIALIST / JOURNAL REVIEW
```
