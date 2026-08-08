# AGENTS.md — Canonical Recovery and Submission Protocol

**Repository:** `Kajin-0/gedanken`  
**Active experiment:** `experiments/01-causal-quantum-branch-information/`  
**Checkpoint:** 2026-08-08, after external-review physics closure, repository consolidation, broad scientific CI, and isolated submission-package validation.  
**Current mode:** **submission polish only unless a concrete new technical defect appears.**

This is the first operational file a new agent should read.

---

## 1. Mandatory concurrency protocol

Other agents may edit `main` concurrently.

Before every repository write:

1. fetch latest `main`;
2. compare with the last-seen head;
3. inspect relevant intervening commits;
4. fetch the exact current target blob immediately before writing;
5. never force a write against a stale blob SHA;
6. if `main` changes during a long task, recheck before writing;
7. preserve concurrent work and prefer narrowly scoped edits.

**Live `main` always overrides this file and every state snapshot.**

---

## 2. Current paper

**A Source-Resolved Quantum Link Budget for Propagating Linearized Gravity**

Active manuscript:

`experiments/01-causal-quantum-branch-information/manuscript_v7/`

Canonical scientific state:

`experiments/01-causal-quantum-branch-information/CURRENT_STATE_EXTERNAL_REVIEW_CLOSED_V7.md`

External-review closure:

`experiments/01-causal-quantum-branch-information/EXTERNAL_REVIEW_RESPONSE_V7.md`

Artifact-status map:

`experiments/01-causal-quantum-branch-information/ARCHIVE_STATUS.md`

Current internal verdict:

> **No known publication-critical structural physics gap remains from the external review within V7's declared weak-field, nonrelativistic, narrowband linear regime.**

This is not a guarantee of peer-review acceptance.

---

## 3. Central result

The active post-handoff link is

$$
\boxed{
\tau_c(t)
=\beta_{g,A}\eta_{\rm store}(R)\beta_{g,B}\mathcal T_f(t).
}
$$

At leading wave-zone order,

$$
\boxed{
\eta_{\rm store}(R)=\frac{25\mathcal O}{16(kR)^2}.
}
$$

Memory and accessible readout are separated:

$$
\Delta_{\rm mem}=\tau_c-m_c,
$$

$$
\boxed{
\Delta_{\rm acc}=\tau_r\Delta_{\rm mem}-m_r.
}
$$

The publication claim is the **source-resolved serial normalization/capability chain**, not a new Gaussian-channel theorem.

---

## 4. Physics items already closed — do not reopen casually

### Conserved finite-support source

Use the finite-spoke plus mode and local finite-speed controller, not prescribed endpoint trajectories as a complete source.

Canonical support:

- `CONSERVED_SOURCE_ACTUATOR_AUDIT.md`
- `LOCAL_CONTROLLER_FIELD_COMPLETION_V7.md`
- `FINITE_SPEED_LOCAL_ENCODER_AUDIT_V7.md`
- `FINITE_HUB_CONTROLLER_RESIDUAL_BOUND_V7.md`

The endpoint-only source is a controlled limit, not the active model.

### Equal-charge gravitational code

At the retained perturbative order,

$$
V_{\mathcal C}^\dagger P^\mu V_{\mathcal C}=p^\mu I_{\mathcal C},
$$

$$
V_{\mathcal C}^\dagger M^{\mu\nu}V_{\mathcal C}=m^{\mu\nu}I_{\mathcal C}.
$$

Use only within the first-order gravitational-splitting scope.

Canonical audit:

`GRAVITATIONAL_SPLITTING_CODE_SUBSPACE_AUDIT_V7.md`

### $25/16$ normalization

Closed by three conceptually distinct routes:

1. retarded conserved-source field;
2. reciprocal critical-absorption / Friis normalization;
3. canonical TT one-graviton angular-mode overlap.

The TT route independently reproduces the full radial polynomial, not only the far-field coefficient.

Canonical audit:

`TT_ONE_GRAVITON_MODE_OVERLAP_25_OVER_16_AUDIT.md`

Do not restart factor-of-two/four normalization work without a new concrete contradiction.

### Approximation/error budget

Canonical audit:

`APPROXIMATION_ERROR_BUDGET_V7.md`

Do not quote leading formulas outside their stated regime.

### Integrated novelty boundary

Canonical audit:

`FINAL_INTEGRATED_PRIOR_ART_SWEEP_V7.md`

Current verdict: **GO WITH RESTRAINED CLAIMS**.

Do not claim priority for individual Gaussian lemmas, graviton transduction, branch-conditioned graviton radiation, generic propagating-graviton entanglement, or the critical $l=2$ absorption bound.

Never use `first`, `unique`, `unprecedented`, or equivalent priority language without new independent evidence.

---

## 5. Standalone Gaussian branch — STOP

Canonical stop documents:

- `STANDALONE_GAUSSIAN_NOVELTY_VERDICT.md`
- `NOVELTY_COLLISION_FILIPPOV_BINARY_COHERENT.md`
- `NOVELTY_COLLISION_MELE_RANK_TWO.md`

Retain the mathematics as channel/receiver tools only.

Do not restart a standalone Gaussian theorem paper from the existing material.

---

## 6. Superseded material

Use

`experiments/01-causal-quantum-branch-information/ARCHIVE_STATUS.md`

for the current artifact map.

In particular, old `PAPER_CORE_*`, old state files, endpoint-only formulas, old `$25/[4(kR)^2]$` storage normalization, old universal logarithmic-cone language, and universal passive `$\beta^5$` claims are historical unless a current document explicitly invokes a narrowed limit.

Do not resurrect an old result merely because its file remains in the repository.

---

## 7. Reproducibility state

Pinned numerical environment:

- Python `3.12.13`;
- NumPy `2.5.1`;
- SciPy `1.18.0`.

Active workflows:

### Manuscript

`.github/workflows/latex-v7.yml`

Checks LaTeX compilation and unresolved references/citations.

### Publication-critical TT normalization

`.github/workflows/tt-normalization.yml`

Runs the independent TT angular-mode regression.

### Broader scientific regression suite

`.github/workflows/scientific-regressions.yml`

Covers representative

- thermal attenuation;
- thermal amplification;
- additive Gaussian noise;
- near-boundary resolution;
- finite-spoke series coefficients;
- V7 benchmark constants;
- exact-negativity weak-link asymptotics.

First run `31266390454` passed.

### Isolated submission-package build

`.github/workflows/submission-package.yml`

The source set is defined by

`manuscript_v7/SUBMISSION_MANIFEST.txt`.

The workflow

1. copies only manifest-listed files into an isolated directory;
2. applies semantic guards;
3. compiles there;
4. checks unresolved citations/references;
5. strips build products;
6. uploads a clean source ZIP.

Run `31266474558` passed.

---

## 8. Canonical reading order

Before historical research files, read:

1. `AGENTS.md`
2. `README.md`
3. `CONTEXT_HANDOFF.md`
4. `experiments/01-causal-quantum-branch-information/CURRENT_STATE_EXTERNAL_REVIEW_CLOSED_V7.md`
5. `experiments/01-causal-quantum-branch-information/ARCHIVE_STATUS.md`
6. `experiments/01-causal-quantum-branch-information/manuscript_v7/README.md`
7. `experiments/01-causal-quantum-branch-information/EXTERNAL_REVIEW_RESPONSE_V7.md`
8. `experiments/01-causal-quantum-branch-information/numerics/README.md`

Only go backward into legacy files when tracing provenance or auditing a historical correction.

---

## 9. Current allowed work

Unless a concrete technical defect is discovered, work is limited to:

1. final prose copyedit;
2. final bibliography metadata verification;
3. author / acknowledgments / funding metadata;
4. optional removal of the orphaned `sin^4` loading example;
5. finalize PRD cover letter;
6. create the final submission tag/snapshot;
7. respond to actual external peer-review objections.

The repository front door, archive map, broad numerical CI, and clean isolated submission-package workflow are already complete.

---

## 10. Do not do this

Without a concrete new defect, do **not**

- derive another Gaussian theorem;
- invent another source architecture;
- reopen $25/16$ normalization;
- reopen finite-spoke propagation;
- restart the hub residual from zero;
- replace V7 with another paper core for stylistic reasons;
- broaden the work into a near-term experimental proposal;
- claim generic gravitational quantum communication novelty.

The next epistemic step is independent peer review, not another speculative derivation.
