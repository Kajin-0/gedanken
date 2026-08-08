# Experiment 01 — Canonical and Historical Artifact Map

**Date:** 2026-08-08  
**Purpose:** keep the adversarial research trail without letting obsolete files compete with the active V7 manuscript.

> Live `main`, root `AGENTS.md`, and `CURRENT_STATE_EXTERNAL_REVIEW_CLOSED_V7.md` are authoritative.

---

## A. Canonical active publication state

Use these for current scientific or submission work:

1. `CURRENT_STATE_EXTERNAL_REVIEW_CLOSED_V7.md`
2. `manuscript_v7/`
3. `EXTERNAL_REVIEW_RESPONSE_V7.md`
4. `APPROXIMATION_ERROR_BUDGET_V7.md`
5. `FINAL_INTEGRATED_PRIOR_ART_SWEEP_V7.md`
6. `PRD_SUBMISSION_CHECKLIST_V7.md`
7. `PRD_COVER_LETTER_DRAFT_V7.md`
8. `SUBMISSION_STRATEGY_V7.md`

Do not replace the active manuscript with an older `PAPER_CORE_*` file.

---

## B. Canonical source / locality / normalization audits

These support the active V7 manuscript:

- `CONSERVED_SOURCE_ACTUATOR_AUDIT.md`
- `LOCAL_CONTROLLER_FIELD_COMPLETION_V7.md`
- `FINITE_SPEED_LOCAL_ENCODER_AUDIT_V7.md`
- `FINITE_HUB_CONTROLLER_RESIDUAL_BOUND_V7.md`
- `EQUAL_POINCARE_CHARGE_AUDIT_V7.md`
- `GRAVITATIONAL_SPLITTING_CODE_SUBSPACE_AUDIT_V7.md`
- `TT_ONE_GRAVITON_MODE_OVERLAP_25_OVER_16_AUDIT.md`
- `STORAGE_NORMALIZATION_25_OVER_16_AUDIT.md`
- `FRIIS_FORM_25_OVER_16_AUDIT.md`
- `RECIPROCAL_CASCADE_BACKACTION_AUDIT.md`
- `FINITE_SIZE_FORM_FACTOR_COEFFICIENT.md`

These files are active supporting derivations unless a later canonical state explicitly supersedes a particular statement.

---

## C. Canonical channel / receiver tools retained in V7

These are active tools or supporting derivations, but not standalone novelty claims:

- `GENERAL_CAUSAL_QUANTUM_CHANNEL_FRONT.md`
- `MICROCAUSAL_REPLACER_THEOREM.md`
- `ACCESSIBLE_RECEIVER_CASCADE_THEOREM.md`
- `GENERAL_FIXED_WAVEFORM_RECEIVER_FRONT.md`
- `PASSIVE_SOURCE_OPTIMIZATION_NO_GO.md`
- `PASSIVE_RECEIVER_SUM_RULE_BOUND.md`
- `PURE_LOSS_BINARY_COHERENT_NEGATIVITY.md`
- `VIRTUAL_DIFFERENCE_MODE_CHANNEL_REDUCTION.md`
- `CANONICAL_FOUR_FACTOR_QUANTUM_LINK_BUDGET.md`

Where these overlap with `manuscript_v7/`, the manuscript and current-state file define the publication wording and scope.

---

## D. Gaussian-channel branch — mathematically retained, publication branch STOPPED

The broad standalone Gaussian novelty path is closed.

Canonical stop decisions:

- `STANDALONE_GAUSSIAN_NOVELTY_VERDICT.md`
- `NOVELTY_COLLISION_FILIPPOV_BINARY_COHERENT.md`
- `NOVELTY_COLLISION_MELE_RANK_TWO.md`
- `THREE_ELEMENT_WITNESS_VS_FILIPPOV.md`

Retain the underlying calculations only as receiver/channel lemmas and numerical controls.

Do not claim as new:

- finite-rank Fock survival to the Gaussian EB boundary;
- all finite binary coherent-pair survival;
- the matched coherent witness scale;
- the associated exponential sign factor.

---

## E. Superseded manuscript cores

These are historical snapshots, not current paper entry points:

- `PAPER_CORE_V3.md`
- `PAPER_CORE_V4.md`
- `PAPER_CORE_V5_LOCAL_END_TO_END.md`
- `PAPER_CORE_V6_QUANTUM_LINK_BUDGET.md`

Current manuscript:

`manuscript_v7/`

Use older cores only to trace the evolution of a derivation or understand why a claim was changed.

---

## F. Superseded current-state files

Historical recovery notes include

- `CURRENT_STATE_RANK2_UPDATE.md`
- `CURRENT_STATE_LINK_BUDGET_V7.md`
- `CURRENT_STATE_MANUSCRIPT_V7.md`
- `CURRENT_STATE_SUBMISSION_V7.md`

These remain useful provenance, but the current recovery point is

`CURRENT_STATE_EXTERNAL_REVIEW_CLOSED_V7.md`.

---

## G. Legacy source models

Older endpoint-only/four-mass source files remain useful as controlled limits and provenance, including

- `CONSERVED_FOUR_MASS_QUADRUPOLE_SOURCE.md`
- `QUANTIZED_PLUS_MODE_SOURCE.md`
- `EXPLICIT_FOUR_MASS_SOURCE_RECEIVER_LINK.md`

Any endpoint-only result must now be interpreted as a stated limit of the finite-support source, normally

$$
q=\omega L/c_s\to0,
$$

unless a current audit says otherwise.

Do not silently promote an endpoint-only formula over the active finite-spoke/controller source model.

---

## H. Explicitly dead or narrowed historical claims

Do not resurrect without a new derivation and new evidence:

- `25/[4(kR)^2]` as coherent storage probability;
- a universal logarithmic quantum-reception cone for one fixed pulse;
- universal passive $\beta^5$ suppression;
- a universal Planck-area receiver bound;
- the claim that stronger source coherent amplitude automatically improves channel quality;
- the claim that all source-receiver entanglement vanishes outside a light cone;
- prescribed endpoint masses alone as a complete conserved gravitational source;
- generic novelty for propagating-graviton entanglement or graviton transduction.

---

## I. Numerical material

Active directory:

`numerics/`

Publication-critical active regression:

- `tt_mode_overlap_25_16_check.py`

Legacy/receiver audits retained for reproducibility:

- `thermal_cat_scan.py`
- `amplifier_cat_scan.py`
- `additive_noise_cat_scan.py`
- `near_boundary_stress.py`

CI-oriented regression harness:

- `scientific_regression_checks.py`

The exploratory scripts remain intentionally independent of the analytic proof formulas they test.

---

## J. Rule for future archival changes

Do not delete a mathematically useful failed branch merely to make the repository look cleaner.

Instead:

1. update this map;
2. mark the file's status in the current state or README;
3. ensure root `README.md` and `AGENTS.md` point only to current work;
4. preserve the obsolete file for provenance unless it is duplicate/generated junk.
