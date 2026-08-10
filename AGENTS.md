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

Do not reopen closed V7 physics without a concrete contradiction.

### Experiment 02 — internally frozen theorem / short-manuscript track

`experiments/02-passive-gravitational-throughput/`

Paper source:

`experiments/02-passive-gravitational-throughput/manuscript_v1/`

Authoritative validated science/manuscript SHA:

```text
1ce596493073dbb49e6eb71f1a6df0566ff3c25b
```

Current in-model theorem:

```math
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega_0^2}{12c^3R^2}\min(I_{2,A},I_{2,B}).
```

Status:

> **INTERNAL AI REVIEW: GO — THEORY AND LITERATURE-CORRECTED MANUSCRIPT FROZEN.**

Canonical recovery order:

1. `experiments/02-passive-gravitational-throughput/INTERNAL_FREEZE_CHECKPOINT_2026-08-10.md`
2. `experiments/02-passive-gravitational-throughput/AGENTS.md`
3. `experiments/02-passive-gravitational-throughput/CURRENT_STATE.md`
4. `experiments/02-passive-gravitational-throughput/CLAIM_LEDGER.md`
5. `experiments/02-passive-gravitational-throughput/RECENT_GRAVITY_COMMUNICATION_COLLISION_AUDIT_2026-08-10.md`
6. `experiments/02-passive-gravitational-throughput/MANUSCRIPT_V1_FINAL_FREEZE_AUDIT_2026-08-10.md`
7. `experiments/02-passive-gravitational-throughput/HOSTILE_PRIOR_ART_COLLISION_AUDIT.md`
8. `experiments/02-passive-gravitational-throughput/META_REFEREE_SIGNIFICANCE_AUDIT.md`
9. `experiments/02-passive-gravitational-throughput/manuscript_v1/README.md`

The Experiment-02 theorem is explicitly a compact narrowband retained-sector result. Do not drop

```text
B/omega_0 << 1
k_0 a_A, k_0 a_B << 1
k_0 R >> 1
omega_n <= Omega = omega_0[1+O(B/omega_0)]
finite or countably infinite bounded-port Markov retained modal sectors
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
9. require fresh CI on the exact resulting science/manuscript head before reporting a validated scientific checkpoint.

**Live `main` always overrides conversation history, connector caches, and state snapshots.**

If local git and a connector disagree about branches, commits, or files, stop and resolve the repository-state discrepancy before making scientific claims based on that state.

A later documentation-only commit does not replace an explicitly recorded validated science/manuscript SHA.

## 3. Scientific boundaries

### Experiment 01

The publication claim is the source-resolved physical normalization/capability chain, not a new Gaussian-channel theorem. Its standalone Gaussian novelty route is stopped.

### Experiment 02

`Gamma_coh` is a frequency-integrated coherent-transfer spectral area with units `s^-1`; it is not an information capacity.

The generic passive-system mathematics, gravitational-antenna eigenmode theory, integrated resonant-mass response, material sum rules, directivity, generic wave-channel bounds, and multiple-scattering composition are not novelty claims.

Modern gravity-as-communication results are also explicit prior art: Newtonian communication/noise bounds, LOCC simulation bounds, gravitational oscillator state-transfer benchmarks, and gravity-induced optomechanical communication channels must not be presented as new here.

The only plausible Experiment-02 publication contribution is the gravity-specific cumulative **passive far-zone two-ended inertia closure**. Historical and recent-literature collision audits found no exact equivalent theorem in the inspected literature; this is not proof of priority.

Do not broaden Experiment 02 to active systems, extended apertures, added relays/cavities, near-field transfer, arbitrary unbounded PDE ports, genuinely non-Markov continua, broad absolute-frequency operation with one carrier coefficient, or uncontrolled high-frequency off-resonant sectors.

## 4. Reproducibility state

Pinned scientific Python environment:

- Python `3.12.13`;
- NumPy `2.5.1`;
- SciPy `1.18.0`.

Experiment 01 workflows include manuscript compilation, TT normalization, broader scientific regressions, and isolated submission-package validation.

Experiment 02 workflows include passive-cut, endpoint-resource, TT-propagation, combined-bound, infinite-modal, recurrence, and manuscript checks. All seven passed on the frozen literature-corrected science/manuscript SHA above. Exact run IDs and artifact digest are in `INTERNAL_FREEZE_CHECKPOINT_2026-08-10.md`.

## 5. Allowed work

### Experiment 01

Unless a concrete defect appears:

- final prose/metadata work;
- author, acknowledgments, funding, conflict metadata;
- final submission snapshot/tag;
- journal submission and referee response.

### Experiment 02

Unless a concrete defect or external objection appears:

- submission metadata/editorial preparation;
- external specialist/journal review;
- referee-response work.

Further theorem broadening is stopped.

## 6. Global prohibitions

Do not:

- treat conversation-only artifacts as repository evidence;
- invent branch names, commits, workflow runs, or files;
- report a write as successful before verifying it on the actual remote;
- report a scientific checkpoint as validated before exact-head CI completes;
- use `first`, `new`, `unique`, `unprecedented`, or similar priority language without dedicated evidence;
- claim to be the first gravity-mediated communication bound;
- silently broaden either experiment's scope;
- modify frozen V7 physics merely to align it with Experiment 02;
- modify frozen Experiment-02 science merely because another extension is imaginable.
