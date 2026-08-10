# Claim Ledger — Experiment 02

This ledger is authoritative for the research status of Experiment 02. A statement is not a project result merely because it appears in `HYPOTHESES.md` or in conversation history.

## Status labels

- `QUESTION` — research target, no truth value assigned.
- `PROVISIONAL` — plausible candidate under investigation.
- `DERIVED / VALIDATION PENDING` — an explicit repository derivation exists, but the required independent validation gate is not yet complete.
- `ESTABLISHED WITHIN MODEL` — derived and independently checked within explicit assumptions.
- `FAILED` — contradicted or overstrong.
- `HISTORICAL / PRIOR ART` — established elsewhere; not a novelty claim.
- `OPEN` — unresolved boundary or extension.

## Current ledger

| Statement | Status | Evidence |
|---|---|---|
| A two-sided `H2` spectral-area metric is mathematically well defined for stable strictly proper selected cross-port blocks | ESTABLISHED WITHIN MODEL | standard Plancherel/Gramian identity, re-derived in `PASSIVE_SELECTED_PORT_CUT_DERIVATION.md` |
| Finite-dimensional passive selected-port transfer obeys `||H_{o<-i}||_2^2 <= min[Tr(K_i^dag K_i), Tr(K_o^dag K_o)]` | DERIVED / VALIDATION PENDING | `PASSIVE_SELECTED_PORT_CUT_DERIVATION.md`; adversarial regression added, CI pending |
| A separated two-ended passive link obeys `Gamma_coh <= eta_max min[Tr(K_gA^dag K_gA), Tr(K_gB^dag K_gB)]` under the Stage-A realization assumptions | DERIVED / VALIDATION PENDING | `PASSIVE_SELECTED_PORT_CUT_DERIVATION.md`; end-to-end random-system regression added, CI pending |
| Compact quadrupolar endpoint coupling has an inertia-only cumulative bound | PROVISIONAL | candidate H2 only |
| The relevant endpoint coefficient is `4/3` in `G I Omega^4 / c^5` normalization | PROVISIONAL | inherited candidate; must be re-derived |
| The relevant compact TT propagation coefficient is `25/16` for the Experiment-02 throughput normalization | PROVISIONAL | candidate H3; must be independently normalized for this metric |
| The final two-ended coefficient is `25/12` | PROVISIONAL | candidate H4 only |
| Passive internal mode mixing cannot increase total gravitational oscillator strength | PROVISIONAL | candidate H5 only |
| Repeated passive returns cannot increase the leading `1/R^2` upper-bound coefficient | PROVISIONAL | candidate H6 only |
| Countably infinite bounded-port modal sectors obey the same cut | OPEN | requires operator-domain/admissibility analysis |
| Arbitrary unbounded PDE boundary ports are covered | FAILED AS A CURRENT CLAIM | explicitly outside initial assumptions |
| The complete inertia-only theorem is novel | OPEN | no trustworthy complete prior-art audit yet |
| Previous conversational Experiment 02 CI/branch/manuscript claims are repository evidence | FAILED | real remote did not contain those artifacts |

## Stage-A prior-art boundary

The passive realization used in Stage A is established systems machinery, not a novelty claim. Primary examples checked during reconstruction include:

- M. Guta and N. Yamamoto, *System identification for passive linear quantum systems*, arXiv:1303.3771 — passive realization `A=-i Omega-C^dag C/2`, transfer function `Xi(s)=I-C(sI-A)^{-1}C^dag`, and frequency-axis unitarity with all channels retained.
- J. E. Gough and G. Zhang, *On Realization Theory of Quantum Linear Systems*, arXiv:1311.1375 — passive minimal/Hurwitz and lossless-bounded-real realization structure.

The Experiment-02 content, if any, must therefore come later from the gravity-specific endpoint resource and its two-ended closure, not from the generic Stage-A passivity lemma.

## Promotion discipline

Before changing a gravity-specific row to `ESTABLISHED WITHIN MODEL`, record:

1. the exact derivation file;
2. the assumptions used;
3. an independent check or normalization route;
4. counterexample attempts and their scope;
5. primary-source comparison;
6. numerical evidence where relevant.

Before changing a row to `HISTORICAL / PRIOR ART`, cite the primary source that actually contains the equivalent statement.

## Priority language

Do not use `first`, `new`, `unique`, `unprecedented`, or equivalent priority wording unless a dedicated primary-source audit supports it. A negative search result is not proof of priority.
