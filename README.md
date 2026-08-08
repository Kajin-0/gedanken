# Gedanken

A repository for first-principles thought experiments and adversarial theoretical research. Claims are treated as hypotheses to be falsified by algebra, counterexample, conservation laws, numerical stress testing, normalization audits, or prior art.

## Current status

The active project is now in **V7 submission-preflight**, not open-ended theory development.

Active manuscript:

**A Source-Resolved Quantum Link Budget for Propagating Linearized Gravity**

Location:

[`experiments/01-causal-quantum-branch-information/manuscript_v7/`](experiments/01-causal-quantum-branch-information/manuscript_v7/)

Canonical state:

[`CURRENT_STATE_EXTERNAL_REVIEW_CLOSED_V7.md`](experiments/01-causal-quantum-branch-information/CURRENT_STATE_EXTERNAL_REVIEW_CLOSED_V7.md)

Current internal verdict:

> **No known publication-critical structural physics gap remains from the external review within the manuscript's declared weak-field, nonrelativistic, narrowband linear regime.**

This is not a guarantee of peer-review acceptance. The remaining work is editorial, reproducibility, repository organization, and submission packaging.

---

## Central result

After local source preparation and controller handoff, the coherent source-to-memory transfer factorizes as

$$
\boxed{
\tau_c(t)
=\beta_{g,A}
\eta_{\rm store}(R)
\beta_{g,B}
\mathcal T_f(t).
}
$$

The factors are

$$
\beta_{g,A}=\frac{\kappa_{g,A}}{\kappa_A},
$$

$$
\boxed{
\eta_{\rm store}(R)
=\frac{25\mathcal O}{16(kR)^2}
}
$$

at leading wave-zone order,

$$
\beta_{g,B}=\frac{\kappa_{g,B}}{\kappa_B},
$$

and

$$
0\le\mathcal T_f(t)\le1.
$$

The memory is then tested through

$$
\Delta_{\rm mem}=\tau_c-m_c,
$$

while a separate noisy readout gives

$$
\boxed{
\Delta_{\rm acc}
=\tau_r\Delta_{\rm mem}-m_r.
}
$$

The paper's publication claim is the **source-resolved serial normalization and capability accounting**. It is not a new Gaussian-channel theorem, not the first graviton transducer proposal, and not a near-term experimental design.

---

## What survived the adversarial review

### Conserved finite-support source

The radiating source is an explicit four-spoke elastic plus mode with endpoint mass $\mu$, spoke length $L$, sound speed $c_s$, and

$$
q=\frac{\omega L}{c_s}.
$$

The exact finite-spoke boundary relation is

$$
\boxed{
\frac{m_r}{\mu}=q\tan q.
}
$$

The branch quadrupole is

$$
\boxed{
\Delta Q_{xx}=8\mu Lu\frac{\tan q}{q},
\qquad
\Delta Q_{yy}=-\Delta Q_{xx}.
}
$$

The corrected gravitational linewidth is

$$
\boxed{
\kappa_g(q)
=
\frac{8G\mu L^2\omega^4}{5c^5}
\frac{(\tan q/q)^2}{\frac12+q/\sin2q}.
}
$$

A finite-speed controller bus is included explicitly; the effective modal encoder is treated as the narrowband reduction of that local causal controller.

### Equal-charge gravitational code

At the retained perturbative order the full encoded system satisfies

$$
\boxed{
V_{\mathcal C}^\dagger P^\mu V_{\mathcal C}
=p^\mu I_{\mathcal C},
}
$$

$$
\boxed{
V_{\mathcal C}^\dagger M^{\mu\nu}V_{\mathcal C}
=m^{\mu\nu}I_{\mathcal C}.
}
$$

This is used only within the first-order gravitational-splitting scope: common long-range charge dressing may exist, while source-controlled branch information is carried later by the retarded multipole field.

### Independent normalization checks

The $25/16$ propagation normalization now has three conceptually distinct derivations:

1. retarded conserved-source field;
2. power-flow / critical-absorption / reciprocal-antenna normalization;
3. canonical TT one-graviton mode overlap.

The TT route independently reproduces the complete radial polynomial

$$
P(z)=3-3iz-3z^2+2iz^3+z^4,
$$

not only the far-field coefficient.

See:

- [`TT_ONE_GRAVITON_MODE_OVERLAP_25_OVER_16_AUDIT.md`](experiments/01-causal-quantum-branch-information/TT_ONE_GRAVITON_MODE_OVERLAP_25_OVER_16_AUDIT.md)
- [`APPROXIMATION_ERROR_BUDGET_V7.md`](experiments/01-causal-quantum-branch-information/APPROXIMATION_ERROR_BUDGET_V7.md)

The exact TT transfer gives

$$
|t|^2
=\frac{25}{16z^2}
\left(
1-\frac2{z^2}
+\frac3{z^4}
-\frac9{z^6}
+\frac9{z^8}
\right),
$$

so at $kR=10$ the leading wave-zone expression is about $1.97\%$ high.

---

## Start here

For the active publication state, read in this order:

1. [`AGENTS.md`](AGENTS.md) — operational recovery protocol and current allowed work;
2. [`CURRENT_STATE_EXTERNAL_REVIEW_CLOSED_V7.md`](experiments/01-causal-quantum-branch-information/CURRENT_STATE_EXTERNAL_REVIEW_CLOSED_V7.md) — canonical scientific state;
3. [`manuscript_v7/README.md`](experiments/01-causal-quantum-branch-information/manuscript_v7/README.md) — manuscript build/layout;
4. [`EXTERNAL_REVIEW_RESPONSE_V7.md`](experiments/01-causal-quantum-branch-information/EXTERNAL_REVIEW_RESPONSE_V7.md) — point-by-point closure of the external review;
5. [`TT_ONE_GRAVITON_MODE_OVERLAP_25_OVER_16_AUDIT.md`](experiments/01-causal-quantum-branch-information/TT_ONE_GRAVITON_MODE_OVERLAP_25_OVER_16_AUDIT.md) — third normalization derivation;
6. [`FINITE_HUB_CONTROLLER_RESIDUAL_BOUND_V7.md`](experiments/01-causal-quantum-branch-information/FINITE_HUB_CONTROLLER_RESIDUAL_BOUND_V7.md) — finite source residual bounds;
7. [`GRAVITATIONAL_SPLITTING_CODE_SUBSPACE_AUDIT_V7.md`](experiments/01-causal-quantum-branch-information/GRAVITATIONAL_SPLITTING_CODE_SUBSPACE_AUDIT_V7.md) — primary-source dressing audit;
8. [`FINAL_INTEGRATED_PRIOR_ART_SWEEP_V7.md`](experiments/01-causal-quantum-branch-information/FINAL_INTEGRATED_PRIOR_ART_SWEEP_V7.md) — final restrained novelty boundary;
9. [`numerics/README.md`](experiments/01-causal-quantum-branch-information/numerics/README.md) — numerical audit suite.

---

## Historical / superseded branches

The repository intentionally retains failed and superseded derivations as an audit trail. They are **not** current recovery points.

### Standalone Gaussian-paper branch — STOPPED

The Gaussian calculations remain useful receiver lemmas, but broad standalone novelty collided with prior art.

Canonical stop documents:

- [`STANDALONE_GAUSSIAN_NOVELTY_VERDICT.md`](experiments/01-causal-quantum-branch-information/STANDALONE_GAUSSIAN_NOVELTY_VERDICT.md)
- [`NOVELTY_COLLISION_FILIPPOV_BINARY_COHERENT.md`](experiments/01-causal-quantum-branch-information/NOVELTY_COLLISION_FILIPPOV_BINARY_COHERENT.md)
- [`NOVELTY_COLLISION_MELE_RANK_TWO.md`](experiments/01-causal-quantum-branch-information/NOVELTY_COLLISION_MELE_RANK_TWO.md)

### Legacy paper cores / state files

Files such as

- `PAPER_CORE_V3.md`;
- `PAPER_CORE_V4.md`;
- `PAPER_CORE_V5_LOCAL_END_TO_END.md`;
- `PAPER_CORE_V6_QUANTUM_LINK_BUDGET.md`;
- `CURRENT_STATE_RANK2_UPDATE.md`;
- older endpoint-only source notes

are retained for provenance. They are superseded by `manuscript_v7/` and `CURRENT_STATE_EXTERNAL_REVIEW_CLOSED_V7.md` unless a current document explicitly cites them for a historical derivation.

Do not resurrect superseded claims merely because the old file remains in the repository.

---

## Reproducibility

Active automated checks include

- V7 LaTeX compile + unresolved citation/reference check;
- canonical TT one-graviton overlap regression;
- pinned numerical environment for the active TT suite.

Pinned active numerical environment:

- Python `3.12.13`;
- NumPy `2.5.1`;
- SciPy `1.18.0`.

The repository also contains independent finite-Fock / quadrature audits for

- thermal attenuation;
- thermal amplification;
- additive Gaussian noise;
- near-EB-boundary convergence.

Broader regression CI for this legacy numerical suite is repository-engineering work, not a publication-critical physics blocker.

---

## Current work

Do **not** open another theoretical branch without a concrete technical defect.

Current allowed work is

1. final prose and bibliography copyedit;
2. author / acknowledgments / funding metadata;
3. clean PRD submission package and cover letter;
4. broaden legacy numerical CI;
5. improve archive/superseded navigation;
6. create a clean tagged submission snapshot.

If a new physics objection appears, document it explicitly and attack that objection. Otherwise preserve the frozen V7 result.

---

## Research status policy

Claims are classified as

- **ESTABLISHED PRIOR ART**;
- **INTERNALLY DERIVED — AUDITED**;
- **CANDIDATE NOVELTY — UNVERIFIED**;
- **COLLISION CONFIRMED — DO NOT CLAIM**;
- **SUPERSEDED / INCORRECT**.

A claim that collides with prior art or fails a conservation/normalization audit is removed from the active publication path rather than defended.
