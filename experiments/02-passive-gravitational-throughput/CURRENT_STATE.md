# Current State — Experiment 02

**Status:** **INTERNAL AI REVIEW GO; 13-PAGE INERTIA-FOCUSED MANUSCRIPT VALIDATED; PHYSICS FROZEN PENDING FINAL EXTERNAL REVIEW / SUBMISSION**

## 1. Current manuscript

Title:

**An Inertia-Controlled Throughput Bound for Passive Gravitational Transduction**

Source:

`manuscript_v1/`

The manuscript has been compressed from the earlier 20-page development-heavy version to **13 pages** while retaining the rigorous appendices.

The conceptual spine is now limited to the five load-bearing statements:

1. the spectral-area metric;
2. the passive selected-port cut;
3. the inertia bound on endpoint gravitational coupling;
4. the compact TT propagation bound;
5. the final two-ended inertia closure.

Experiment 01 / V7 remains frozen and is not modified by Experiment 02.

---

## 2. Headline theorem

For separated compact passive nonrelativistic linear-harmonic source and receiver systems in weak quadrupolar wave-zone gravity,

```math
\Gamma_{\rm coh}
=\frac1{2\pi}\int_{\mathcal B}
\operatorname{Tr}[T^\dagger(\omega)T(\omega)]\,d\omega
```

obeys, at retained leading separated-wave-zone order,

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega^2}{12c^3R^2}
\min(I_A,I_B).
}
```

`I_A` and `I_B` are internal mass inertia moments about the endpoint centers of mass.

The physical ceiling is **classical**. Quantum mechanics reproduces the same oscillator-strength normalization and supplies downstream pure-loss channel/capacity corollaries.

---

## 3. Passive selected-port cut

For an energy-normalized passive realization

```math
A=-iH-\frac12K^\dagger K,
```

the end-to-end transfer obeys

```math
\boxed{
\Gamma_{\rm coh}
\le
\eta_{\max}
\min\!\left[
\operatorname{Tr}(K_{g,A}^\dagger K_{g,A}),
\operatorname{Tr}(K_{g,B}^\dagger K_{g,B})
\right].
}
```

This is generic passive systems mathematics, not a novelty claim.

The argument extends directly to separable **countably infinite bounded-port Markov modal sectors**. For the contraction semigroup `T(t)=exp(At)`,

```math
0\le P_u(\tau)
\le I-T(\tau)T^\dagger(\tau)
\le I.
```

If `K_g` is Hilbert--Schmidt, operator-valued Plancherel gives

```math
\|S_{g\leftarrow u}\|_2^2
\le\operatorname{Tr}(K_g^\dagger K_g).
```

Arbitrary unbounded PDE boundary ports and genuinely non-Markov continua are **not** claimed.

Canonical audit:

`INFINITE_DIMENSIONAL_PASSIVE_H2_AUDIT_2026-08-09.md`

---

## 4. Classical gravitational endpoint resource

For compact linear-harmonic matter, the historical long-wavelength STF tidal coupling plus standard modal Bessel/Parseval completeness gives

```math
\boxed{
\sum_n\frac{q_n:q_n}{\mu_n}
\le\frac{20}{3}I.
}
```

Using Hirakawa's gravitational effective area,

```math
A_{Gn}=\frac{2q_n:q_n}{M\mu_n},
```

this becomes

```math
\boxed{
\sum_nMA_{Gn}\le\frac{40}{3}I.
}
```

The gravitational energy-decay rate is

```math
\boxed{
\kappa_{g,n}
=\frac{GMA_{Gn}\omega_n^4}{10c^5},
}
```

so for retained modes with `omega_n <= Omega`,

```math
\boxed{
\operatorname{Tr}(K_g^\dagger K_g)
=\sum_n\kappa_{g,n}
\le\frac{4G}{3c^5}I\Omega^4.
}
```

This simultaneously supplies the endpoint resource and proves that `K_g` is Hilbert--Schmidt in the retained countably infinite modal sector.

The tidal fields, STF completeness, modal-participation mathematics, and general gravitational response sum-rule methodology are historical/established. The standalone `20/3` relation is **not** a main novelty claim.

Canonical audits:

- `LOBO_SPHERICAL_MODAL_COMPLETENESS_COLLISION_AUDIT_2026-08-09.md`
- `CLASSICAL_MODAL_SUM_RULE_AND_QUANTUM_SCOPE_AUDIT_2026-08-09.md`
- `HIRAKAWA_EFFECTIVE_AREA_QUANTUM_LINEWIDTH_CROSSCHECK.md`

---

## 5. Compact TT propagation

For normalized compact quadrupolar TT radiation,

```math
\boxed{
\|P_g(\omega)\|_{\rm op}^2
\le\frac{25}{16[k(\omega)R]^2}
}
```

at leading wave-zone order.

The same coefficient follows from

- the normalized TT angular-mode calculation; and
- the historical reciprocal-antenna interpretation with `D_A=D_B=5/2`.

The directivity law and `5/2` maximum are historical and are not novelty claims.

---

## 6. Passive two-endpoint recurrence — corrected statement

Repeated passive returns between the same two separated endpoints sum to

```math
P_{\rm eff}
=(I-P_{BA}R_AP_{AB}R_B)^{-1}P_{BA}.
```

For reciprocal one-hop amplitude norm `p` and one-hop power ceiling `eta=p^2`,

```math
\boxed{
\eta_{\rm rec}
\le\frac{\eta}{(1-\eta)^2}.
}
```

Since `eta=O((kR)^-2)`,

```math
\boxed{
\eta_{\rm rec}
\le\eta+O((kR)^{-4}).
}
```

This is an **upper-bound asymptotic**, not an equality for the actual recurrent transfer. Interference can make the actual transfer smaller.

The earlier wording

```math
\eta_{\rm rec}=\eta+O((kR)^{-4})
```

was stronger than the proof supported and has been corrected. The headline theorem is unchanged because it requires only that passive recurrence cannot increase the leading `1/R^2` upper-bound coefficient.

Canonical audit and regression:

- `RECURRENT_SCATTERING_WAVEZONE_AUDIT_2026-08-09.md`
- `numerics/verify_recurrent_scattering_bound.py`

---

## 7. Equivalent quantum normalization

Quantizing the same mode gives

```math
Q^{01}:Q^{10}
=\frac{\hbar M A_{Gn}}{4\omega_n}
```

and exactly reproduces

```math
\boxed{
\kappa_{g,n}
=\frac{2G\omega_n^5}{5\hbar c^5}Q^{01}:Q^{10}
=\frac{GMA_{Gn}\omega_n^4}{10c^5}.
}
```

No factor-of-two or `2 pi` mismatch was found.

The quantum EWSR is an equivalent representation of the classical modal resource in this linear-harmonic class, not the origin of the headline ceiling.

---

## 8. Modern multimode stress test

Tobar--Pikovski--Tobar's multimode resonant-mass proposal is a useful apparent challenge. Its hybrid-mode gravitational rates carry squared participation factors `P_1j^2`; mass-weighted normal-mode orthogonality gives

```math
\sum_j|P_{1j}|^2=1.
```

Thus passive hybridization redistributes the gravitationally driven coordinate rather than creating arbitrarily many copies of its oscillator strength. It can still improve readout transduction and spectral coverage.

Canonical audit:

`TOBAR_MULTIMODE_BAR_STRESS_TEST_2026-08-09.md`

---

## 9. Exact resonator and quantum corollaries

For the explicit two-resonator specialization,

```math
\Gamma_{\rm EBP}
\le\eta_{\rm prop}\min(\kappa_{g,A},\kappa_{g,B}).
```

For equal gravitational linewidths, zero internal loss, and symmetric external coupling, the integrated area is maximized at

```math
\kappa_{\rm in}=\kappa_{\rm out}=2\kappa_g,
```

with

```math
\Gamma_{\rm EBP}^{\rm sym,max}
=\frac8{27}\eta_{\rm prop}\kappa_g.
```

After quantization, for the stationary vacuum pure-loss realization,

```math
\eta_{\max}\le\frac12\Rightarrow Q_1=0,
```

and

```math
Q_2\le
\frac{\Gamma_{\rm coh}}
{\ln2(1-\eta_{\max})}.
```

These are secondary channel-specific consequences.

---

## 10. Prior-art boundary

Explicitly **not novel**:

- gravitational generator--receiver calculations;
- resonant-mass eigenmode/STF tidal theory;
- gravitational effective area and reciprocity;
- `Q`-independent integrated/short-pulse response;
- compact quadrupole directivity / `D=5/2`;
- gravitational response sum-rule methodology;
- modal participation/effective-mass completeness;
- finite/infinite-dimensional passive `H2` machinery;
- generic source--receiver singular channels;
- two-body material-response + Green-operator bounds;
- multiple-scattering/Redheffer composition;
- generic continuous-time frequency-integrated transducer metrics.

The strongest historical end-to-end near-collision found is Rudenko's 2003 complete generator--receiver Hertz-experiment optimization. It remains an architecture-specific SNR/detectability calculation and does not state the inertia-only frequency-integrated passive theorem.

### Surviving candidate contribution

No inspected primary source has been found to state the complete closure

```text
passive selected-port spectral-area cut
-> total gravitational trace at source and receiver
-> cumulative inertia resource at BOTH endpoints
-> compact normalized TT propagation
-> leading passive recurrence controlled
-> explicit inertia-only end-to-end ceiling.
```

The candidate result is therefore the exact gravity-specific closure

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega^2}{12c^3R^2}\min(I_A,I_B).
}
```

This is a **negative prior-art search result, not proof of priority**. Do not use `first`, `unique`, `unprecedented`, or equivalent language.

---

## 11. AI adversarial review

Repository-wide policy:

`AI_RESEARCH_PROTOCOL.md`

### Round 1

Separate branch:

`experiment-02-ai-adversarial-review-2026-08-09`

Reports:

- historical collision agent: surviving exact closure, broad novelty rejected;
- generic-wave agent: mathematically incremental, gravity-specific closure survives;
- infinite-dimensional systems agent: bounded-port theorem survives with hard scope boundary;
- meta-referee: `MAJOR REVISION`, recommending manuscript compression rather than more physics.

### Round 2 — compressed manuscript

Directory:

`ai_adversarial_review_round2/`

Reports:

- `AGENT_A_CLAIM_DISCIPLINE.md` — **PASS**;
- `AGENT_B_GENERIC_METHOD_POSITIONING.md` — **PASS**;
- `AGENT_C_SCOPE_AND_OPERATOR_AUDIT.md` — **PASS**;
- `META_REFEREE_FINAL.md` — **GO FOR SPECIALIST SUBMISSION AFTER FINAL EDITORIAL FREEZE**.

These are role-separated AI audits, not statistically independent human reviewers or independently trained-model replications.

---

## 12. Final validation

Final-title manuscript validation:

```text
run: 31351144558
job: 93342080071
PASS
```

- LaTeX compilation: PASS
- unresolved citation/reference scan: PASS
- PDF artifact upload: PASS
- compiled length: 13 pages

Final-title physics validation:

```text
run: 31351144554
job: 93342080258
PASS
```

All six regressions passed:

1. exact two-port spectral bound;
2. passive selected-port `H2` cut;
3. classical modal resource;
4. recurrent passive scattering upper bound;
5. TT propagation;
6. microscopic gravitational-port factorization.

---

## 13. Final internal decision

```text
PHYSICS THEOREM:                              GO
MANUSCRIPT:                                   GO
INTERNAL AI ADVERSARIAL REVIEW:               GO
COUNTABLY INFINITE BOUNDED-PORT MODES:        GO
PASSIVE TWO-ENDPOINT RECURRENCE UPPER BOUND:  GO
MATERIAL / QUANTUM NORMALIZATION:             GO
TT NORMALIZATION:                             GO
GENERIC METHOD NOVELTY:                       NO
STANDALONE MODAL-SUM NOVELTY:                 NO-GO AS MAIN CLAIM
EXACT INERTIA-CLOSED TWO-ENDED THEOREM:       PROVISIONAL GO
PRIORITY CLAIM:                               NO
MORE INTERNAL THEOREM BROADENING:             NO
HUMAN DEPENDENCY FOR INTERNAL ITERATION:      NO
FINAL EXTERNAL / JOURNAL REVIEW:              NEXT EXTERNAL GATE
V7 MODIFICATION:                              NO
```

The dominant remaining uncertainty is external priority/significance, not a known internal technical defect.

---

## 14. Hard stop

Do not broaden Experiment 02 internally without a concrete new defect or exact prior-art collision.

The internal AI research loop is complete. Human involvement is reserved for the final external-review/submission boundary and ordinary journal peer review.
