# Claim Ledger — Experiment 01

**Updated:** 2026-08-08  
**Status:** **CURRENT V7 CLAIM BOUNDARY**  
**Purpose:** State what the active manuscript does and does not claim, while preserving the important correction history from earlier research stages.

> This file supersedes the older exploratory novelty ledger. Earlier Gaussian-channel investigations and waveform-specific branches remain in Git history and supporting notes, but they are **not current publication claims**.

---

## 1. Active manuscript claim

**A Source-Resolved Quantum Link Budget for Propagating Linearized Gravity**

For the stated weak-field, nonrelativistic, narrowband linear regime, the post-handoff coherent source-to-memory transfer is

```math
\boxed{
\tau_c(t)
=\beta_{g,A}\,\eta_{\rm store}(R)\,\beta_{g,B}\,\mathcal T_f(t)
}
```

with

```math
\beta_{g,A}=\frac{\kappa_{g,A}}{\kappa_A},
\qquad
\eta_{\rm store}(R)=\frac{25\mathcal O}{16(kR)^2},
\qquad
\beta_{g,B}=\frac{\kappa_{g,B}}{\kappa_B},
\qquad
0\le\mathcal T_f\le1.
```

The publication claim is the **source-resolved physical normalization and capability chain**: local quantum preparation, conserved gravitational emission, normalized travelling-mode propagation, receiver capture, noise, and later readout are kept in one consistent calculation without assuming a normalized incoming gravitational mode for free.

The product form itself is not claimed as new.

---

## 2. Claims explicitly not made

V7 does **not** claim

- that gravity-mediated quantum information transfer is new;
- that Gaussian entanglement-breaking boundaries are new;
- that coherent graviton radiation from a source is new;
- that propagating gravitons can causally correlate or entangle distant matter for the first time;
- that graviton absorption or quantum transduction is new;
- that the critical quadrupole absorption area is new;
- that the binary-coherent Gaussian lemmas constitute a new standalone theorem paper;
- that the kilogram-scale benchmark is experimentally feasible;
- that the passive `~10^-42` benchmark is a universal gravitational bound;
- exact gravitational tensor-factor locality or an all-orders quantum-gravity result.

Avoid `first`, `unique`, `unprecedented`, or equivalent priority language.

---

## 3. Load-bearing V7 results

### 3.1 Conserved finite-support source

The active source is the finite-spoke elastic plus mode with local finite-speed control. Its exact finite-spoke relations include

```math
\boxed{\frac{m_r}{\mu}=q\tan q}
```

and

```math
\boxed{
\Delta Q_{xx}=8\mu Lu\frac{\tan q}{q},
\qquad
\Delta Q_{yy}=-\Delta Q_{xx}.
}
```

The corresponding gravitational linewidth is

```math
\boxed{
\kappa_g(q)=
\frac{8G\mu L^2\omega^4}{5c^5}
\frac{(\tan q/q)^2}{\frac12+q/\sin2q}.
}
```

### 3.2 Equal-charge gravitational code

At the retained perturbative order,

```math
\boxed{
V_{\mathcal C}^\dagger P^\mu V_{\mathcal C}=p^\mu I_{\mathcal C},
\qquad
V_{\mathcal C}^\dagger M^{\mu\nu}V_{\mathcal C}=m^{\mu\nu}I_{\mathcal C}.
}
```

This is used only within the first-order gravitational-splitting scope. A branch-common long-range dressing may remain; the branch-sensitive signal is the later retarded difference field.

### 3.3 Propagation normalization

The wave-zone storage factor

```math
\boxed{
\eta_{\rm store}=\frac{25\mathcal O}{16(kR)^2}
}
```

is closed by three conceptually distinct routes:

1. retarded conserved-source field;
2. reciprocal radiation/critical-absorption normalization;
3. canonical transverse-traceless one-graviton mode overlap.

The third route reproduces the full radial polynomial

```math
P(z)=3-3iz-3z^2+2iz^3+z^4
```

and the exact aligned transfer probability

```math
|t|^2=
\frac{25}{16z^2}
\left(1-\frac{2}{z^2}+\frac{3}{z^4}-\frac{9}{z^6}+\frac{9}{z^8}\right).
```

At `kR=10`, the leading wave-zone expression is about `1.97%` high.

### 3.4 Memory and accessible readout

The memory quantum excess is

```math
\Delta_{\rm mem}=\tau_c-m_c,
```

while a separate noisy readout gives

```math
\boxed{
\Delta_{\rm acc}=\tau_r\Delta_{\rm mem}-m_r.
}
```

The Gaussian-channel criterion is prior theory used as a tool, not a novelty claim.

### 3.5 Exact weak-link entanglement amount

For the fixed binary-coherent pure-loss problem used in V7,

```math
\boxed{
\mathcal N_{\max}(\eta)
=\eta-2\eta^{3/2}+\frac{13}{3}\eta^2+O(\eta^{5/2}).
}
```

Its role is quantitative: a fantastically weak end-to-end link is not rescued by arbitrarily increasing branch separation.

---

## 4. Current novelty boundary

The targeted 2025–2026 prior-art sweep did **not** find an inspected work that closes the same separated chain

```math
\boxed{
\text{local physical source preparation}
\to
\text{normalized gravitational emission}
\to
\text{free propagation}
\to
\text{remote receiver capture}
\to
\text{receiver noise/readout}
}
```

with both matter–gravity interfaces explicitly normalized.

The defensible V7 contribution is therefore:

> **A source-resolved weak-linearized-gravity construction that closes local preparation, conserved radiative emission, normalized travelling-mode propagation, remote memory capture, Gaussian noise, and accessible readout in one serial normalization, exposing the separate source and receiver gravitational branching penalties.**

This is a **negative literature search result, not proof of priority**. Publication significance remains subject to normal referee judgment.

Canonical literature audit:

`FINAL_INTEGRATED_PRIOR_ART_SWEEP_V7.md`

---

## 5. Historical corrections retained as audit evidence

These were real earlier errors or overclaims and are preserved because they document how the present result was hardened.

### H1. Universal logarithmic quantum cone — superseded

The logarithmic front holds only for the stated stationary/target-time-optimized conditions, not as a universal causal front.

### H2. Universal `beta^5` receiver penalty — superseded

That scaling applies to geometric-aperture-limited absorbers, not to every compact resonant receiver.

### H3. `25/[4(kR)^2]` state-storage coefficient — incorrect

That coefficient belongs to scattering/extinction bookkeeping. State storage uses

```math
\boxed{\frac{25}{16(kR)^2}}.
```

### H4. “No source-receiver entanglement before `R/c`” — too strong

The correct causal statement concerns **source-controlled input dependence/communication**, not the absence of all vacuum or background correlations.

### H5. Hard `sin^2` compact quadrupole pulse — not ultraviolet safe

Its endpoint smoothness is insufficient for the ideal `omega^5 |Q_tilde|^2` coherent-graviton norm. Later work used smoother waveforms, and the active V7 manuscript no longer depends on that orphaned waveform example.

---

## 6. Stopped exploratory branches

### Standalone Gaussian novelty branch — STOP

The exact coherent-dyad formulas, binary-coherent partial-transpose witnesses, and related Gaussian calculations remain useful supporting mathematics. They are **not the active paper's novelty claim** and should not be presented as such.

Canonical stop documents:

- `STANDALONE_GAUSSIAN_NOVELTY_VERDICT.md`
- `NOVELTY_COLLISION_FILIPPOV_BINARY_COHERENT.md`
- `NOVELTY_COLLISION_MELE_RANK_TWO.md`

### Waveform-specific historical branches

Earlier `sin^4` quantum-capability bubbles and source-specific receiver optimizations are retained as research history/supporting calculations, not as the V7 publication center.

---

## 7. Explicit limitations still open by design

The manuscript does not solve every physical problem surrounding a realizable experiment.

In particular:

- the kilogram-scale benchmark is conditional on successful preparation and preservation of macroscopic source coherence;
- no device-specific environmental decoherence budget for such a source is claimed;
- the approximation hierarchy is perturbative and does not constitute a universal all-orders remainder bound;
- the material model is a controlled linear-elastic source, not an exact relativistic hyperelastic body;
- the novelty conclusion is restrained and remains subject to referee judgment.

These are stated limitations, not hidden assumptions.

---

## 8. Current verification state

The active manuscript and supporting physics have been checked through

- analytic conservation and source audits;
- three propagation-normalization routes;
- direct numerical transverse-traceless overlap regression;
- representative Gaussian-channel/negativity regressions;
- centralized approximation/error accounting;
- primary-source gravitational-splitting comparison;
- targeted prior-art comparison;
- independent manuscript compilation and clean submission-source compilation.

The current research mode is **submission polish only unless a concrete new technical defect appears**.
