# Third Critical Review Audit — 2026-08-11

## Purpose

This note records the independent disposition of a new external-style review of the current PRD manuscript. Only scientific, mathematical, framing, and significance claims are evaluated here. Author biography, affiliation matching, credentials, and other provenance/credentialism are intentionally excluded because they do not bear on whether the theorem is correct.

**Validated science/manuscript checkpoint:** `bfae23af41aefb3104d639099299b3432b4a14fe`  
**Theorem status after this audit:** **GO / unchanged.**  
**Manuscript change required:** **No.**

The review was useful mainly as a hostile-reader check on the axial `m`-sector interpretation, physical framing, significance calibration, and Appendix C propagation formulas. No load-bearing scientific defect survived independent checking.

## 1. Claims the review independently got right

### 1.1 Passive selected-port cut

The review accepted the passive Gramian / `H2` step as standard and correctly applied. This agrees with the existing proof and regressions. No action.

### 1.2 Quadrupole-radiation normalization

The review independently reconstructed the standard mass-quadrupole power normalization and obtained the manuscript coefficient

```math
P_{g,n}
=
\frac{G\omega_n^6|\xi_0|^2}{10c^5}(q_n:q_n),
```

which implies

```math
\kappa_{g,n}
=
\frac{G\omega_n^4}{5c^5}\frac{q_n:q_n}{\mu_n}.
```

This is consistent with the earlier audits and numerical regression. No action.

### 1.3 Sector completeness and axial selection rule

The review correctly recognized that the statement

```text
|m|=2 -> R^-2 power,
|m|=1 -> R^-4 power,
m=0   -> R^-6 power
```

is **not** a claim about total radiated power integrated over all directions. The `m` sectors are defined with respect to the source-receiver/separation axis, and the receiver samples the translated compact TT field along that axis. The subleading sectors reflect axial radiation-pattern zeros/selection rules, not a violation of ordinary far-zone `1/R^2` radiation scaling for generic observation directions.

The manuscript already states in the abstract that the sectors are defined by the separation axis, and Sec. IV explicitly chooses `z = Rhat` before diagonalizing axial translation. No correction is required.

### 1.4 Worked sphere example

The review independently reproduced the manuscript's scale example,

```text
M = 1000 kg,
a = 1 m,
f0 = 1 kHz,
k0 R = 100,
R ~= 4.77e6 m,
Gamma_coh ~= 2.15e-39 s^-1.
```

This agrees with the current regression and dimensional checks. No action.

### 1.5 Retained-sector caveat

The review correctly identified the manuscript's fourth-frequency-moment limitation as a substantive and properly stated restriction. The current theorem does **not** claim that unweighted completeness controls an unrestricted `omega_n^4` modal trace. This remains the main unresolved mathematical frontier.

## 2. Appendix C — the review's admitted blind spot was independently closed

The reviewer stated that the exact finite-distance compact-TT formulas were not independently re-derived. This audit therefore re-derived them directly from the Appendix C kernels rather than relying on the manuscript's algebra.

For

```math
K_2(\mu)=\frac{5}{32}(1+6\mu^2+\mu^4),
```

```math
K_1(\mu)=\frac58(1-\mu^2)(1+\mu^2),
```

```math
K_0(\mu)=\frac{15}{16}(1-\mu^2)^2,
```

with

```math
S_m(z)=\int_{-1}^{1}K_m(\mu)e^{iz\mu}\,d\mu,
```

direct symbolic integration and separation of the `e^{+iz}` term gives exactly

```math
S_{+,2}(z)
=-\frac{5i}{4z^5}
(z^4+2iz^3-3z^2-3iz+3)e^{iz},
```

```math
S_{+,1}(z)
=-\frac{5}{2z^5}
(z^3+3iz^2-6z-6i)e^{iz},
```

```math
S_{+,0}(z)
=\frac{15i}{2z^5}
(z^2+3iz-3)e^{iz}.
```

Taking squared magnitudes reproduces the manuscript formulas coefficient-for-coefficient:

```math
\eta_2(z)
=
\frac{25}{16z^{10}}
(z^8-2z^6+3z^4-9z^2+9),
```

```math
\eta_1(z)
=
\frac{25}{4z^{10}}
(z^6-3z^4+36),
```

```math
\eta_0(z)
=
\frac{225}{4z^{10}}
(z^4+3z^2+9).
```

This symbolic route is independent of the manuscript derivation. It also complements the existing `numerics/verify_tt_propagation_bound.py`, which numerically integrates the normalized sector kernels at several finite `z` values and verifies them against the exact outgoing+incoming formulas, while separately checking the `25/16` asymptotic power coefficient and sector ordering.

**Disposition:** Appendix C survives. No normalization or closed-form defect found.

## 3. Motivation-mismatch criticism

The review argued that gravity-mediated quantum-information literature is mostly concerned with Newtonian/quasi-static coupling rather than a radiative far-zone TT channel. That physical distinction is correct in general and is already reflected in the current manuscript.

The present introduction no longer opens with gravity-QI work. It begins with resonant-mass gravitational antennas, material-response sum rules, generic wave-channel/passive `H2` bounds, and classical matching/antenna theory. The gravity-communication papers appear only later in the prior-work/scope discussion, where the manuscript explicitly says that they use different criteria and often different interaction regimes, and that their information-theoretic criteria are not part of this proof.

Therefore the review identifies a **historically real framing risk that was already corrected in an earlier revision**, not a current defect.

**Disposition:** no further motivation rewrite. Do not re-expand quantum-information framing.

## 4. Physical relevance and significance

The review's statement that the worked gravitational scale is extraordinarily small is correct. The manuscript already says this explicitly and presents the theorem as structural rather than near-term experimental engineering.

The stronger statement that physical relevance is "essentially nil" is an evaluative judgment, not a mathematical objection. A fundamental-limit/no-go theorem can be scientifically meaningful even when the coupling being bounded is extremely weak. The correct significance claim is therefore neither experimental promise nor a new gravitational phenomenon.

The defensible contribution remains:

1. a two-ended passive spectral-area closure for coherent far-zone gravitational transduction;
2. a geometry-resolved STF-sector endpoint resource rather than a separately optimized scalar resource times directivity;
3. an exact finite-`kR` compact-TT propagation closure leading to the `5/4 * I_Rhat` far-zone coefficient.

The manuscript already avoids claiming generic `H2`, gain-bandwidth, quadrupole theory, STF representation theory, or resonant-mass response as new.

**Disposition:** significance remains specialized but legitimate. No stronger priority/significance language should be added.

## 5. Novelty claim

The review characterized the work as a legitimate but modest/incremental fundamental-limits contribution rather than a new physical phenomenon. That is compatible with the manuscript's present novelty posture.

The current paper claims only the specific gravity-side synthesis/closure. It explicitly states that the main ingredients have substantial precedents and makes no `first`, `unique`, `unprecedented`, or equivalent priority claim.

No exact prior theorem has been identified that combines the weighted two-ended passive cut, STF-sector endpoint completeness, exact compact-TT translation sectors, and the resulting inertia-about-separation-axis closure. Negative literature search is not proof of priority, so the cautious wording remains appropriate.

**Disposition:** no novelty-language change.

## 6. What does not alter the scientific assessment

The following review material is intentionally not used to judge theorem correctness:

- whether the author's public publication record is easy to discover;
- whether the listed affiliation's public-facing business focus matches gravitation;
- whether a reviewer would assign more or less prior probability to correctness based on credentials;
- the mere fact that AI tools were used.

The relevant question is whether the derivations, assumptions, normalization, literature claims, and reproducible checks survive independent scrutiny. The manuscript already discloses AI assistance and explicitly states that internal checks are not external peer review.

## 7. Net disposition

### Survives

- passive selected-port `H2` cut;
- gravitational quadrupole-power and linewidth prefactors;
- scalar and sector completeness identities;
- exact finite-distance TT sector kernels and outgoing amplitudes;
- `eta_2`, `eta_1`, `eta_0` closed forms;
- `25/16` asymptotic propagation normalization;
- `5/4 * I_Rhat` leading far-zone coefficient;
- sphere scale example;
- retained-sector/high-frequency caveat;
- current cautious novelty framing.

### Useful criticism, already addressed

- distinguish axial source-receiver sector suppression from generic angular radiation scaling;
- avoid presenting near-field/Newtonian gravity-QI work as the physical regime of the theorem;
- state clearly that the result is structural and not experimentally near-term.

The current manuscript already does all three sufficiently clearly. Additional wording changes would be editorial churn rather than correction.

### Still open

- whole-spectrum inertia closure without the retained modal ceiling;
- physical/constitutive approach to abstract projection-level saturation;
- broader unbounded/distributed-system admissibility;
- quantitative engineering slack between the abstract ceiling and realizable devices;
- noise/capacity extensions, which are separate observables.

## 8. Change-control result

**No manuscript source, theorem constant, normalization, or numerical regression is changed by this review.**

The validated science/manuscript checkpoint remains

```text
bfae23af41aefb3104d639099299b3432b4a14fe
```

Future work should not reopen the theorem merely because a reviewer describes the significance as low or the result as incremental. Reopen only for a concrete mathematical/physical defect, a direct prior-art collision, or a genuinely stronger theorem that preserves all inherited regressions.
