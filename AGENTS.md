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

### Experiment 02 — exploratory track

`experiments/02-passive-gravitational-throughput/`

Status: independent reconstruction; **no theorem verified and no manuscript yet**.

Start with:

1. `experiments/02-passive-gravitational-throughput/AGENTS.md`
2. `experiments/02-passive-gravitational-throughput/CURRENT_STATE.md`
3. `experiments/02-passive-gravitational-throughput/QUESTION.md`
4. `experiments/02-passive-gravitational-throughput/ASSUMPTIONS.md`
5. `experiments/02-passive-gravitational-throughput/HYPOTHESES.md`
6. `experiments/02-passive-gravitational-throughput/CLAIM_LEDGER.md`

Experiment 02 must independently derive or falsify its candidate throughput bound. Conversation history is a source of hypotheses, not evidence.

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
8. after any important write, fetch the resulting commit and affected files from the actual remote to verify persistence.

**Live `main` always overrides conversation history, connector caches, and state snapshots.**

If local git and a connector disagree about branches, commits, or files, stop and resolve the repository-state discrepancy before making scientific claims based on that state.

## 3. Experiment 01 scientific boundary

The current V7 central link is

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

This is not formal peer review and does not guarantee journal acceptance.

Experiment 01's standalone Gaussian novelty route is stopped. Do not revive it from legacy files.

## 4. Experiment 02 research discipline

The prior conversational candidate

```math
\Gamma_{\rm coh}
\stackrel{?}{\lesssim}
\frac{25G\omega^2}{12c^3R^2}\min(I_A,I_B)
```

is **not an established result**.

Experiment 02 must use an AI-native falsification loop:

1. derive from explicit assumptions;
2. independently reconstruct load-bearing steps;
3. run normalization/dimensional audits;
4. attempt hostile counterexamples;
5. search primary prior art for an exact collision;
6. run numerical adversarial tests where possible;
7. update the claim ledger;
8. only then consider a manuscript.

Human specialists are reserved for the final external/journal-review boundary rather than the normal internal iteration loop.

## 5. Reproducibility state for Experiment 01

Pinned numerical environment:

- Python `3.12.13`;
- NumPy `2.5.1`;
- SciPy `1.18.0`.

Active Experiment 01 checks include:

- `.github/workflows/latex-v7.yml`
- `.github/workflows/tt-normalization.yml`
- `.github/workflows/scientific-regressions.yml`
- `.github/workflows/submission-package.yml`

Do not claim Experiment 02 CI validation until Experiment 02 has its own real workflows or is explicitly covered by a real existing workflow on `main`.

## 6. Allowed work

### Experiment 01

Unless a concrete defect appears:

- final prose/metadata work;
- author, acknowledgments, funding, conflict metadata;
- final submission snapshot/tag;
- journal submission and referee response.

### Experiment 02

Active first-principles research is allowed and expected, subject to its local `AGENTS.md` and claim ledger. The immediate task is the passive selected-port spectral-area cut.

## 7. Global prohibitions

Do not:

- treat conversation-only artifacts as repository evidence;
- invent branch names, commits, workflow runs, or files;
- report a write as successful before verifying it on the actual remote;
- use `first`, `unique`, `unprecedented`, or similar priority language without dedicated evidence;
- silently promote a provisional Experiment 02 hypothesis into a theorem;
- modify frozen V7 physics merely to align it with Experiment 02.
