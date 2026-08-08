# Gedanken

A repository for first-principles thought experiments and adversarial theoretical research. Claims are treated as hypotheses to be falsified by algebra, counterexample, numerical stress testing, or prior art.

## Start here

For the current research state, read in this order:

1. [`AGENTS.md`](AGENTS.md) — authoritative recovery protocol and exact next actions;
2. [`CONSERVED_SOURCE_ACTUATOR_AUDIT.md`](experiments/01-causal-quantum-branch-information/CONSERVED_SOURCE_ACTUATOR_AUDIT.md) — current gravity-source result and finite-spoke conservation completion;
3. [`STANDALONE_GAUSSIAN_NOVELTY_VERDICT.md`](experiments/01-causal-quantum-branch-information/STANDALONE_GAUSSIAN_NOVELTY_VERDICT.md) — formal stop decision on the standalone Gaussian-theorem branch;
4. [`NOVELTY_COLLISION_FILIPPOV_BINARY_COHERENT.md`](experiments/01-causal-quantum-branch-information/NOVELTY_COLLISION_FILIPPOV_BINARY_COHERENT.md) — coherent-state prior-art collision;
5. [`NOVELTY_COLLISION_MELE_RANK_TWO.md`](experiments/01-causal-quantum-branch-information/NOVELTY_COLLISION_MELE_RANK_TWO.md) — rank-two Fock prior-art collision;
6. [`CURRENT_STATE_RANK2_UPDATE.md`](experiments/01-causal-quantum-branch-information/CURRENT_STATE_RANK2_UPDATE.md) — legacy-named current-state recovery note;
7. [`numerics/README.md`](experiments/01-causal-quantum-branch-information/numerics/README.md) — reproducible Gaussian-channel audit suite retained for the gravity receiver lemmas.

## Experiment 01 — Causal Transport of Quantum Branch Information by Gravity

**Original question:** If a mass is placed in a coherent spatial superposition, can gravity communicate information about the alternatives to a distant quantum system without first converting those alternatives into classical information?

The project has developed into a source→quantized gravitational field→noisy receiver model with explicit causality, mode matching, thermal entanglement-breaking thresholds, and finite source/receiver geometry.

### Gaussian detour: mathematically useful, no longer the publication center

The repository independently derived several compact Gaussian-channel results, including

- a vacuum–one-photon rank-two PT determinant;
- an exact binary-coherent PT principal minor;
- a three-element negativity lower bound;
- weak-link optimized witness asymptotics.

The broad novelty claims did not survive prior-art review. Mele–Lami–Giovannetti already contain the substantive finite-rank Fock phenomenon, while Filippov–Ziman's coherent-state witness already encodes the all-finite-coherent survival boundary and the same matched coherent scale/exponential sign factor.

These calculations are retained as short lemmas and quantitative tools. The standalone Gaussian paper path is stopped unless a genuinely new operational result emerges.

### Current gravity bottleneck: make the source genuinely closed

The strongest source-level objection was that prescribed accelerated endpoint masses alone do not define a conserved stress-energy tensor. An unspecified actuator might carry compensating branch-dependent stress-energy and alter or cancel the claimed radiation.

The repository now contains an explicit finite-mass conservation completion: a central hub with four longitudinal elastic spokes and four endpoint masses.

For one spoke define

$$
q=\frac{\omega L}{c_s},
$$

where $c_s$ is the longitudinal sound speed. The exact endpoint boundary condition gives

$$
\boxed{
\frac{m_r}{\mu}=q\tan q,
}
$$

where $m_r$ is the mass of one spoke and $\mu$ the endpoint mass.

Including the rest-mass quadrupole of the spokes, the branch-difference plus quadrupole becomes

$$
\boxed{
\Delta Q_{xx}
=8\mu L u_c\frac{\tan q}{q},
}
$$

$$
\boxed{
\Delta Q_{yy}
=-8\mu L u_c\frac{\tan q}{q}.
}
$$

Thus the support does **not** cancel the endpoint quadrupole in this closed architecture. For the endpoint-dominated fundamental mode,

$$
\frac{\tan q}{q}
=1+\frac{q^2}{3}+O(q^4),
$$

so the previous endpoint-only source is the controlled $q\to0$ limit.

The exact generalized mode mass is

$$
\boxed{
M_{\rm eff}(q)
=4\mu\left[
\frac12+\frac{q}{\sin2q}
\right],
}
$$

and the corrected gravitational linewidth is

$$
\boxed{
\kappa_g(q)
=
\frac{8G\mu L^2\omega^4}{5c^5}
\frac{(\tan q/q)^2}
{\frac12+q/\sin2q}.
}
$$

For $q\ll1$,

$$
\kappa_g(q)
=
\frac{8G\mu L^2\omega^4}{5c^5}
\left[
1+\frac{q^2}{3}+\frac{q^4}{9}+O(q^6)
\right].
$$

The branch controller can also be modeled autonomously with

$$
H=H_m+H_c-\sigma_z g(q_c)u.
$$

A controlled mechanical-parity transformation removes the source-qubit label from the nongravitational source/controller dynamics, showing that the work reservoir need not acquire a hidden which-branch record before gravitational coupling is included.

### Current next step

Propagate the finite-spoke corrections through the quantized plus mode and source→receiver formulas:

- corrected $q_{01}(q)$;
- corrected $\kappa_g(q)$;
- corrected emitted branch-distance $N_\Delta$;
- corrected source→receiver storage/coupling factors;
- finite hub/controller residual bounds.

Then rebuild the gravity-paper core around the **total conserved source**, not prescribed endpoint trajectories.

## Research status policy

Claims are explicitly classified as

- **ESTABLISHED PRIOR ART**;
- **INTERNALLY DERIVED — MATHEMATICS AUDITED**;
- **CANDIDATE NOVELTY — UNVERIFIED**;
- **COLLISION CONFIRMED — DO NOT CLAIM**;
- **SUPERSEDED / INCORRECT**.

A claim that collides with prior art or fails a conservation audit is removed from the active publication path rather than defended.
