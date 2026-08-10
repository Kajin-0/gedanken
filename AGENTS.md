# AGENTS.md — Canonical Repository Recovery Protocol

**Repository:** `Kajin-0/gedanken`

This is the first operational file a new automated contributor should read.

## 1. Research tracks

### Experiment 01 — publication track

`experiments/01-causal-quantum-branch-information/`

Paper: **A Source-Resolved Quantum Link Budget for Propagating Linearized Gravity**

Status: V7 physics is frozen. Work is limited to submission/editorial tasks unless a concrete technical defect appears.

Canonical recovery files:

1. `experiments/01-causal-quantum-branch-information/CURRENT_STATE_REVIEW_CLOSED_V7.md`
2. `experiments/01-causal-quantum-branch-information/CLAIM_LEDGER.md`
3. `experiments/01-causal-quantum-branch-information/manuscript_v7/README.md`
4. `experiments/01-causal-quantum-branch-information/ARCHIVE_STATUS.md`
5. `experiments/01-causal-quantum-branch-information/ADVERSARIAL_REVIEW_RESPONSE_V7_2026-08-08.md`

Do not reopen the `25/16` normalization, conserved-source architecture, finite-spoke propagation, Gaussian novelty branch, or other closed V7 items without a concrete contradiction.

### Experiment 02 — theorem / short-manuscript track

`experiments/02-passive-gravitational-throughput/`

Paper source: `experiments/02-passive-gravitational-throughput/manuscript_v1/`

Current in-model theorem:

```math
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega_0^2}{12c^3R^2}\min(I_{2,A},I_{2,B}).
```

Status: the finite and countably infinite bounded-port passive theorem, retained carrier-scale endpoint resource, compact TT propagation coefficient, and same-endpoint recurrence ceiling have been derived and validated within their declared model. A short manuscript exists. The active checkpoint is manuscript scope hardening and final adversarial validation, not open-ended theorem expansion.

Canonical recovery files:

1. `experiments/02-passive-gravitational-throughput/AGENTS.md`
2. `experiments/02-passive-gravitational-throughput/CURRENT_STATE.md`
3. `experiments/02-passive-gravitational-throughput/CLAIM_LEDGER.md`
4. `experiments/02-passive-gravitational-throughput/MANUSCRIPT_V1_ADVERSARIAL_AUDIT_2026-08-10.md`
5. `experiments/02-passive-gravitational-throughput/HOSTILE_PRIOR_ART_COLLISION_AUDIT.md`
6. `experiments/02-passive-gravitational-throughput/META_REFEREE_SIGNIFICANCE_AUDIT.md`
7. `experiments/02-passive-gravitational-throughput/manuscript_v1/README.md`

The Experiment-02 theorem is explicitly a compact narrowband retained-sector result. Do not drop the conditions

```text
B/omega_0 << 1
k_0 a_A, k_0 a_B << 1
k_0 R >> 1
omega_n <= Omega = omega_0[1+O(B/omega_0)] for the retained endpoint modal sector
```

or silently extend the carrier-scale `omega_0^4` endpoint resource to uncontrolled higher-frequency off-resonant modes.

## 2. Mandatory repository-integrity protocol

Other agents may edit `main` concurrently.

Before every repository write:

1. fetch latest `main`;
2. compare with the last-seen head;
3. inspect relevant intervening commits;
4. fetch the exact current target blob immediately before replacing a file;
5. never force a write against a stale blob SHA;
6. if `main` changes during a long task, recheck before writing;
7. preserve concurrent work and prefer narrowly scoped edits;
8. after any important write, fetch the resulting commit and affected files from the actual remote to verify persistence;
9. require fresh CI on the exact resulting head before reporting a validated checkpoint.

**Live `main` always overrides conversation history, connector caches, and state snapshots.**

If local git and a connector disagree about branches, commits, or files, stop and resolve the repository-state discrepancy before making scientific claims based on that state.

## 3. Experiment 01 scientific boundary

The V7 central link is

```math
\tau_c(t)=\beta_{g,A}\eta_{\rm store}(R)\beta_{g,B}\mathcal T_f(t),
```

with

```math
\eta_{\rm store}(R)=\frac{25\mathcal O}{16(kR)^2}.
```

The publication claim is the source-resolved physical normalization/capability chain, not a new Gaussian-channel theorem.

The current internal assessment is:

> No known publication-critical structural physics gap remains within V7's declared weak-field, nonrelativistic, narrowband linear regime.

Experiment 01's standalone Gaussian novelty route is stopped.

## 4. Experiment 02 scientific boundary

Use

```text
omega_0   absolute carrier angular frequency
nu        complex-envelope detuning
B         envelope bandwidth
k_0       omega_0/c
I_2       int rho r^2 dV about endpoint COM
```

`Gamma_coh` is a frequency-integrated coherent-transfer spectral area with units `s^-1`; it is not an information capacity.

The generic passive-system mathematics, gravitational-antenna eigenmode theory, integrated resonant-mass response, material sum rules, directivity, generic wave-channel bounds, and multiple-scattering composition are not novelty claims.

The only plausible Experiment-02 publication contribution is the gravity-specific cumulative **two-ended inertia closure**. No exact equivalent theorem was found in the inspected literature; this is not proof of priority.

Do not broaden Experiment 02 to active systems, extended apertures, added relays/cavities, near-field transfer, arbitrary unbounded PDE ports, genuinely non-Markov continua, broad absolute-frequency operation with one carrier coefficient, or uncontrolled high-frequency off-resonant sectors.

## 5. Reproducibility state

Pinned numerical environment used by active scientific checks:

- Python `3.12.13`;
- NumPy `2.5.1`;
- SciPy `1.18.0`.

Experiment 01 workflows include:

- `.github/workflows/latex-v7.yml`
- `.github/workflows/tt-normalization.yml`
- `.github/workflows/scientific-regressions.yml`
- `.github/workflows/submission-package.yml`

Experiment 02 workflows include:

- `.github/workflows/experiment02-passive-cut.yml`
- `.github/workflows/experiment02-endpoint-resource.yml`
- `.github/workflows/experiment02-tt-propagation.yml`
- `.github/workflows/experiment02-combined-bound.yml`
- `.github/workflows/experiment02-infinite-modal.yml`
- `.github/workflows/experiment02-recurrence.yml`
- `.github/workflows/latex-experiment02.yml`

Canonical run IDs and exact scope are recorded in each experiment's current-state/claim-ledger files.

## 6. Allowed work

### Experiment 01

Unless a concrete defect appears:

- final prose/metadata work;
- author, acknowledgments, funding, conflict metadata;
- final submission snapshot/tag;
- journal submission and referee response.

### Experiment 02

Unless a concrete defect appears:

- validate manuscript scope hardening;
- final adversarial claim/notation/citation audit;
- final recovery-state synchronization;
- concise editorial/manuscript polish;
- external specialist/journal review.

Further theorem broadening is stopped unless a concrete objection shows the current theorem is internally inconsistent or too narrow to support its stated conclusion.

## 7. Global prohibitions

Do not:

- treat conversation-only artifacts as repository evidence;
- invent branch names, commits, workflow runs, or files;
- report a write as successful before verifying it on the actual remote;
- report a scientific checkpoint as validated before the exact-head CI has completed;
- use `first`, `unique`, `unprecedented`, or similar priority language without dedicated evidence;
- silently broaden either experiment's scope;
- modify frozen V7 physics merely to align it with Experiment 02.
