# Gedanken

A repository for first-principles thought experiments and adversarial theoretical research aimed at exposing sharp conceptual tensions between established physical theories.

The method is deliberately simple:

1. isolate one physical principle;
2. remove every unnecessary experimental detail;
3. force accepted descriptions to make predictions about the same idealized situation;
4. identify the smallest observable on which those predictions differ;
5. distinguish established results from genuinely open questions;
6. actively try to falsify every internally derived claim;
7. search prior art at the theorem/equation level, including supplements and appendices;
8. only then ask whether a result supports a practical experiment or publication.

The goal is not speculative model-building for its own sake. The goal is to find situations in which nature is forced to answer a precise question, while documenting failures and prior-art collisions as aggressively as successful derivations.

## Start here

For a new research agent or reviewer, read:

1. [`AGENTS.md`](AGENTS.md) — recovery protocol, active claims, killed claims, and continuation rules;
2. [`CURRENT_STATE_RANK2_UPDATE.md`](experiments/01-causal-quantum-branch-information/CURRENT_STATE_RANK2_UPDATE.md) — current Experiment 01 recovery state;
3. [`NOVELTY_COLLISION_MELE_RANK_TWO.md`](experiments/01-causal-quantum-branch-information/NOVELTY_COLLISION_MELE_RANK_TWO.md) — confirmed prior-art collision that retired the previous rank-two Fock novelty claim;
4. [`CLAIM_LEDGER_POST_MELE_ADDENDUM.md`](experiments/01-causal-quantum-branch-information/CLAIM_LEDGER_POST_MELE_ADDENDUM.md) — current claim classification;
5. [`COHERENT_PRIOR_ART_DEEP_AUDIT.md`](experiments/01-causal-quantum-branch-information/COHERENT_PRIOR_ART_DEEP_AUDIT.md) and [`COHERENT_PRIOR_ART_SECOND_PASS.md`](experiments/01-causal-quantum-branch-information/COHERENT_PRIOR_ART_SECOND_PASS.md) — active novelty audit;
6. [`COHERENT_THEOREM_ADVERSARIAL_PROOF_AUDIT.md`](experiments/01-causal-quantum-branch-information/COHERENT_THEOREM_ADVERSARIAL_PROOF_AUDIT.md) — independent proof rederivation.

## Experiment 01 — Causal Transport of Quantum Branch Information by Gravity

**Original question:** If a mass is placed in a coherent spatial superposition, can gravity communicate information about the alternatives to a distant quantum system without first converting those alternatives into classical information?

The experiment developed from a single spatially superposed source, through gravity-mediated which-path information and reversible entanglement, to a relativistic source→field→receiver channel model.

During that work, a separate continuous-variable quantum-information problem emerged: how little input structure is required to expose the entanglement-breaking boundary of a one-mode Gaussian channel?

### Current mathematical status

The repository independently derived a compact Schmidt-rank-two Fock proof, but the underlying rank-two phenomenon was subsequently found in prior work by Mele, Lami, and Giovannetti. That result is therefore retained as a useful rederivation, **not** as the current discovery claim.

The strongest surviving standalone candidate is narrower:

> For a known gauge-covariant phase-insensitive one-mode Gaussian channel, every finite nontrivial binary coherent hybrid input appears to have NPT output if and only if the channel is not entanglement breaking.

For symmetric coherent branches `|±a>` and thermal parameter `m>0`, the repository derives a matched coherent-state partial-transpose minor with

$$
 v_*=\frac{2\sqrt\tau a}{m},
$$

and

$$
\frac{|z_{v_*}|^2}{p_0p_{v_*}}
=\exp\left[\frac{4a^2}{m}(\tau-m)\right].
$$

The internal proof has survived an independent rederivation. The dominant unresolved question is **prior art**, not current algebra. No originality claim should be made until the ongoing citation-forward search is exhausted.

### Numerical reproducibility

Independent executable checks are committed for

- thermal attenuation — beam-splitter dilation;
- thermal amplification — two-mode-squeezer dilation;
- additive Gaussian noise — direct random-displacement integration;
- controlled near-boundary stress scans.

See [`numerics/README.md`](experiments/01-causal-quantum-branch-information/numerics/README.md).

## Research status policy

These are working theoretical notes, not claims of discovery.

Claims are explicitly classified as

- **ESTABLISHED PRIOR ART**;
- **INTERNALLY DERIVED — MATHEMATICS AUDITED**;
- **CANDIDATE NOVELTY — UNVERIFIED**;
- **COLLISION CONFIRMED — DO NOT CLAIM**;
- **SUPERSEDED / INCORRECT**.

A claim that fails an algebraic audit or collides with prior art is not hidden; it is documented and removed from the active publication path.
