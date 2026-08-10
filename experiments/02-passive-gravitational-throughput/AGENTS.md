# AGENTS.md — Experiment 02 Recovery and Research Protocol

**Experiment:** `02-passive-gravitational-throughput`  
**Mode:** exploratory independent reconstruction.  
**Current theorem status:** none verified.  
**Manuscript status:** none.

This file is the first operational file an automated contributor should read after the repository-level `AGENTS.md`.

## 1. Live-repository discipline

Before every repository write:

1. fetch the current `main` head;
2. verify that this experiment directory exists on that exact ref;
3. fetch the exact target blob immediately before replacing a file;
4. never force-update a stale branch/ref;
5. after writing, fetch the resulting commit and the changed files from `main` to verify persistence;
6. if local git and a connector disagree about remote state, treat the discrepancy as a blocking integrity problem and do not build scientific conclusions on the disputed state.

Repository provenance must be verifiable from the actual remote.

## 2. Experiment 01 is frozen

`../01-causal-quantum-branch-information/` is the V7 publication project.

Do not alter its physics while working here unless Experiment 02 uncovers a concrete defect that directly affects V7. Shared constants or formulas may be compared, but Experiment 02 must independently derive its own operational normalization.

## 3. Independence rule

The previous conversational exploration suggested a candidate bound

```math
\Gamma_{\rm coh}
\stackrel{?}{\lesssim}
\frac{25G\omega^2}{12c^3R^2}\min(I_A,I_B).
```

Do **not** begin by proving this expression.

Begin from:

- the selected-port transfer definition;
- passivity;
- explicit gravitational coupling;
- compact TT propagation;
- the assumptions in `ASSUMPTIONS.md`.

The correct outcome may be a different coefficient, a weaker theorem, an additional material parameter, or a no-go for the entire inertia-only idea.

## 4. Required AI-native research loop

A claim must progress through these roles/stages:

### A. Derivation

Develop the result from explicit assumptions. Separate exact identities, inequalities, asymptotic statements, and conjectures.

### B. Independent reconstruction

Where practical, rederive the same load-bearing result without the original derivational narrative.

### C. Hostile technical attack

Try to reject the claim using:

- counterexamples;
- nonnormal/noncommuting passive systems;
- extreme linewidths;
- degeneracies;
- mode mixing;
- continuum/domain issues;
- repeated scattering;
- normalization inconsistencies.

### D. Prior-art collision

Assume the claim is old. Search primary sources using both modern and historical terminology. Separate ingredient prior art from an exact theorem collision.

### E. Numerical adversary

When possible, optimize or randomly search for systems that maximize `actual / claimed bound`. Tests should be designed to fail the theorem, not merely reproduce examples.

### F. Normalization audit

Check dimensions, `2`, `pi`, Fourier conventions, one/two-sided spectra, polarization sums, field versus power normalization, and asymptotic order.

### G. Meta-referee

Only after the above stages should an agent judge whether the claim is technically viable and significant enough to continue.

Human review is reserved for the final external/journal boundary, not the normal internal iteration loop.

## 5. Documentation requirements

Keep these files current:

- `QUESTION.md`
- `ASSUMPTIONS.md`
- `HYPOTHESES.md`
- `CLAIM_LEDGER.md`
- `CURRENT_STATE.md`

Create narrowly named derivation/audit files as work advances. Never hide a failed derivation; record the correction and update the claim ledger.

## 6. Evidence hierarchy

Prefer, in order:

1. explicit derivation stored in the repository;
2. independent derivation/check;
3. numerical regression/counterexample search;
4. primary literature;
5. secondary literature for navigation only;
6. conversation history only as a source of questions, never as proof.

## 7. No manuscript yet

Do not create a paper manuscript until the central theorem or no-go statement has survived the independent technical stages above.

The next technical task is Stage A from `CURRENT_STATE.md`: derive the passive selected-port spectral-area cut from scratch and state exactly what assumptions are required.
