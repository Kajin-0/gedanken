# Gedanken

A repository for first-principles thought experiments and adversarial theoretical research. Claims are treated as hypotheses to be falsified by algebra, counterexample, numerical stress testing, or prior art.

## Start here

For the current research state, read in this order:

1. [`AGENTS.md`](AGENTS.md) — authoritative recovery protocol and exact next actions;
2. [`NOVELTY_COLLISION_FILIPPOV_BINARY_COHERENT.md`](experiments/01-causal-quantum-branch-information/NOVELTY_COLLISION_FILIPPOV_BINARY_COHERENT.md) — confirmed collision that retired the all-finite-binary-coherent survival theorem as novelty;
3. [`NOVELTY_COLLISION_MELE_RANK_TWO.md`](experiments/01-causal-quantum-branch-information/NOVELTY_COLLISION_MELE_RANK_TWO.md) — confirmed collision that retired the rank-two Fock theorem as novelty;
4. [`CURRENT_STATE_RANK2_UPDATE.md`](experiments/01-causal-quantum-branch-information/CURRENT_STATE_RANK2_UPDATE.md) — current Experiment 01 recovery state;
5. [`CLAIM_LEDGER_POST_MELE_ADDENDUM.md`](experiments/01-causal-quantum-branch-information/CLAIM_LEDGER_POST_MELE_ADDENDUM.md) — current claim classification;
6. [`EXACT_THREE_ELEMENT_WITNESS.md`](experiments/01-causal-quantum-branch-information/EXACT_THREE_ELEMENT_WITNESS.md) — strongest surviving possible standalone contribution;
7. [`COHERENT_THEOREM_ADVERSARIAL_PROOF_AUDIT.md`](experiments/01-causal-quantum-branch-information/COHERENT_THEOREM_ADVERSARIAL_PROOF_AUDIT.md) — independent proof rederivation;
8. [`numerics/README.md`](experiments/01-causal-quantum-branch-information/numerics/README.md) — reproducible independent channel simulations.

## Experiment 01 — Causal Transport of Quantum Branch Information by Gravity

**Original question:** If a mass is placed in a coherent spatial superposition, can gravity communicate information about the alternatives to a distant quantum system without first converting those alternatives into classical information?

The experiment developed into a relativistic source→field→receiver channel model. During that work, several continuous-variable quantum-information statements were derived and then subjected to adversarial prior-art review.

### What was killed

The repository independently derived a very short Schmidt-rank-two Fock proof of the phase-insensitive Gaussian entanglement-breaking boundary. The mathematics appears correct, but Mele–Lami–Giovannetti already contain the underlying finite-rank survival result. It is retained as a compact rederivation, not a discovery claim.

The repository also independently proved that every finite nontrivial binary coherent hybrid input remains NPT exactly while a phase-insensitive Gaussian channel is non-entanglement-breaking. That broad survival theorem is likewise not a viable novelty claim: a one-sided specialization of Filippov–Ziman's 2014 coherent-state witness, combined with an invertible local filter on the untouched two-dimensional coherent-state span, implies the same finite-amplitude survival boundary.

Documenting those collisions is part of the project, not a failure mode to hide.

### Strongest surviving possible standalone contribution

The remaining question is substantially narrower: whether the known binary-coherent survival boundary admits a **new minimal exact certificate**.

For symmetric branches `|±a>`, the repository selects a literal two-dimensional block of the actual partial transpose,

$$
M_\Gamma=
\begin{pmatrix}
p_0&z_v^*\\
z_v&p_v
\end{pmatrix}.
$$

NPT is certified by

$$
|z_v|^2>p_0p_v.
$$

For a phase-insensitive Gaussian channel with $m>0$, the matched coherent analysis displacement is

$$
\boxed{
v_*=\frac{2\sqrt\tau\,a}{m},
}
$$

and the exact ratio is

$$
\boxed{
\frac{|z_{v_*}|^2}{p_0p_{v_*}}
=\exp\left[\frac{4a^2}{m}(\tau-m)\right].
}
$$

Thus two selected populations and one coherence expose the full EB boundary through one finite $2\times2$ PT minor.

**This minimal-witness formulation is still under prior-art attack. It is not yet an originality claim.**

The associated selected-block negative eigenvalue and weak-link optimized witness-strength formulas are also being audited as possible quantitative contributions.

### Numerical reproducibility

Independent executable checks are committed for

- thermal attenuation — beam-splitter dilation;
- thermal amplification — two-mode-squeezer dilation;
- additive Gaussian noise — direct random-displacement integration;
- controlled near-boundary stress scans.

The additive-noise stress suite resolves the analytic sign change through at least $|\tau-m|=10^{-4}$ at the current numerical resolution.

See [`numerics/README.md`](experiments/01-causal-quantum-branch-information/numerics/README.md).

## Research status policy

Claims are explicitly classified as

- **ESTABLISHED PRIOR ART**;
- **INTERNALLY DERIVED — MATHEMATICS AUDITED**;
- **CANDIDATE NOVELTY — UNVERIFIED**;
- **COLLISION CONFIRMED — DO NOT CLAIM**;
- **SUPERSEDED / INCORRECT**.

A claim that collides with prior art is removed from the active publication path immediately. The current publication decision is therefore: do not write another broad Gaussian-channel survival theorem; first determine whether the three-element exact PT witness or its quantitative strength is genuinely new and useful. If not, return the research focus to the gravity application.
