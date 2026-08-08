# AGENTS.md — Canonical Recovery and Submission Protocol

**Repository:** `Kajin-0/gedanken`  
**Active experiment:** `experiments/01-causal-quantum-branch-information/`  
**Checkpoint:** 2026-08-08, after the V7 manuscript survived the external-review closure pass.  
**Current mode:** **submission / repository consolidation, not open-ended theory development.**

This is the first operational file a new agent should read.

---

## 1. Mandatory concurrency protocol

Other agents may edit `main` concurrently.

Before every repository write:

1. fetch the latest `main` head;
2. compare it with the last-seen head;
3. inspect intervening commits relevant to the file being changed;
4. fetch the exact current target blob immediately before writing;
5. never force a write against a stale blob SHA;
6. if `main` changes during a long task, recheck immediately before the write;
7. preserve concurrent work and prefer narrowly scoped edits.

**Live `main` always overrides this file and every state snapshot.**

---

## 2. Research operating rule

Try to kill every claim before trying to publish it.

Attack by

1. counterexample;
2. hidden assumption;
3. convention/normalization error;
4. singular limit;
5. conservation-law failure;
6. stronger theorem that makes the result trivial;
7. prior art under different notation;
8. numerical truncation artifact;
9. omitted parts of a supposedly closed system;
10. scope inflation.

If a claim dies, downgrade or remove it immediately.

However, **do not keep opening new theory branches after the current V7 freeze unless a concrete technical defect is identified.**

---

## 3. Current canonical paper

**A Source-Resolved Quantum Link Budget for Propagating Linearized Gravity**

Active manuscript:

`experiments/01-causal-quantum-branch-information/manuscript_v7/`

Canonical scientific state:

`experiments/01-causal-quantum-branch-information/CURRENT_STATE_EXTERNAL_REVIEW_CLOSED_V7.md`

External-review response:

`experiments/01-causal-quantum-branch-information/EXTERNAL_REVIEW_RESPONSE_V7.md`

Current internal verdict:

> **No known publication-critical structural physics gap remains from the external review within V7's declared weak-field, nonrelativistic, narrowband linear regime.**

This does **not** mean referee-proof or guaranteed publication.

---

## 4. Central post-handoff link

The active result is

$$
\boxed{
\tau_c(t)
=\beta_{g,A}
\eta_{\rm store}(R)
\beta_{g,B}
\mathcal T_f(t).
}
$$

with

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

The memory quantum excess is

$$
\boxed{
\Delta_{\rm mem}=\tau_c-m_c,
}
$$

and a separate readout gives

$$
\boxed{
\Delta_{\rm acc}=\tau_r\Delta_{\rm mem}-m_r.
}
$$

The publication claim is the **source-resolved serial normalization/capability chain**, not a new Gaussian-channel theorem.

---

## 5. Current source architecture

The radiating source is a finite-support four-spoke elastic plus mode.

Define

$$
q=\frac{\omega L}{c_s}.
$$

The exact spoke boundary relation is

$$
\boxed{
\frac{m_r}{\mu}=q\tan q.
}
$$

The branch-difference quadrupole is

$$
\boxed{
\Delta Q_{xx}
=8\mu Lu\frac{\tan q}{q},
\qquad
\Delta Q_{yy}=-\Delta Q_{xx}.
}
$$

The exact generalized mode mass is

$$
M_{\rm eff}
=4\mu\mathcal A(q),
$$

$$
\boxed{
\mathcal A(q)=\frac12+\frac{q}{\sin2q}.
}
$$

The corrected graviton linewidth is

$$
\boxed{
\kappa_g(q)
=\frac{8G\mu L^2\omega^4}{5c^5}
\frac{(\tan q/q)^2}{\mathcal A(q)}.
}
$$

The old endpoint-only formulas are controlled $q\to0$ limits, not the active source model.

---

## 6. Local controller completion

Do not use an instantaneous distributed `sigma_z` actuator as the physical model.

The active source uses a local controller bus field

$$
\Phi_a^{(s)}(x,t)
=sX_C(t-x/v_c),
\qquad
v_c\le c,
$$

with local eigenstrain coupling.

Define

$$
q_c=\frac{\omega L}{v_c}.
$$

The projected controller form factor is

$$
F_c(\omega)
=\int_0^Ldx\,W_c(x)e^{i\omega x/v_c},
$$

with

$$
|F_c|^2
=1-q_c^2\operatorname{Var}_{W_c}(x/L)+O(q_c^4).
$$

A physical handoff has

$$
T_*^{\rm local}
=T_*^{\rm modal}+O(L/v_c).
$$

Canonical source/controller notes:

- `LOCAL_CONTROLLER_FIELD_COMPLETION_V7.md`
- `FINITE_SPEED_LOCAL_ENCODER_AUDIT_V7.md`
- `FINITE_HUB_CONTROLLER_RESIDUAL_BOUND_V7.md`

---

## 7. Equal-charge gravitational code

The full encoded system, including controller/radiation/loss ports, satisfies at the retained perturbative order

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

This fixes all Poincare-charge matrix elements on the logical code.

Use this only within the first-order Donnelly--Giddings gravitational-splitting scope:

- common branch-independent long-range dressing may exist;
- source-controlled branch information is absent before causal escape;
- later branch-dependent quadrupole/precursor radiation is the signal;
- no exact tensor-factor locality or nonperturbative quantum-gravity theorem is claimed.

Canonical audit:

`GRAVITATIONAL_SPLITTING_CODE_SUBSPACE_AUDIT_V7.md`

---

## 8. $25/16$ normalization — CLOSED

Do not reopen the factor-of-four/factor-of-two normalization problem without a new concrete contradiction.

There are now three distinct checks:

1. retarded conserved-source field;
2. critical absorption / reciprocal-antenna / Friis normalization;
3. canonical TT one-graviton mode overlap.

The TT route gives

$$
S_+(z)
=-\frac{5i}{4}
\frac{P(z)e^{iz}}{z^5},
$$

$$
P(z)=3-3iz-3z^2+2iz^3+z^4,
$$

and therefore

$$
|S_+|^2
\to\frac{25}{16z^2}.
$$

It independently reproduces the entire radial polynomial, not only the asymptotic coefficient.

Canonical audit:

`TT_ONE_GRAVITON_MODE_OVERLAP_25_OVER_16_AUDIT.md`

Numerical regression:

`numerics/tt_mode_overlap_25_16_check.py`

Workflow:

`.github/workflows/tt-normalization.yml`

Pinned active numerical environment:

- Python `3.12.13`;
- NumPy `2.5.1`;
- SciPy `1.18.0`.

---

## 9. Approximation hierarchy

Do not quote the leading formulas without their regime.

The centralized control parameters are

$$
\boxed{
\epsilon_u,
q,
q_c,
\beta,
B/\omega,
\mathcal C,
(kR)^{-1},
\epsilon_h,
\epsilon_{\rm fb}
\ll1.
}
$$

Canonical audit:

`APPROXIMATION_ERROR_BUDGET_V7.md`

The exact TT propagation correction is

$$
|t|^2
=\frac{25}{16z^2}
\left(
1-\frac2{z^2}
+\frac3{z^4}
-\frac9{z^6}
+\frac9{z^8}
\right).
$$

At the benchmark $kR=10$, the leading wave-zone expression is about $1.97\%$ high.

---

## 10. Finite hub/controller residual — CLOSED TO BOUNDS

The symmetric controller bus has branch-even quadratic energy and therefore

$$
\Delta Q_{ij}^{\rm ctrl}=0
$$

at the retained order.

The generic finite-hub residual is bounded by

$$
\boxed{
\frac{|\Delta Q_h|}{Q_0}
\le
\frac{C_h}{8}
\frac{M_h}{\mu}
\frac{r_h}{L}
\frac{|u_h|}{|u|}
\frac{q}{\tan q}.
}
$$

Define

$$
\epsilon_h
=\frac{M_h}{\mu}
\frac{r_h}{L}
\frac{u_h}{u}.
$$

Controlled source design requires $\epsilon_h\ll1$.

Do not describe the model as an exact relativistic hyperelastic material theory.

---

## 11. Novelty boundary

Current novelty verdict: **GO WITH RESTRAINED CLAIMS**.

Final integrated sweep:

`FINAL_INTEGRATED_PRIOR_ART_SWEEP_V7.md`

Do not claim novelty for any of the following individually:

- finite-rank Gaussian survival;
- all finite binary coherent survival;
- matched coherent witness scale;
- branch-difference graviton mode or $N_\Delta$ by itself;
- generic propagating-graviton entanglement;
- graviton transduction as a concept;
- critical $l=2$ absorption cross section;
- generic Gaussian non-EB criterion.

The surviving candidate contribution is the **closed separated-source serial normalization**

$$
\text{local source}
\to
\beta_{g,A}
\to
\eta_{\rm store}
\to
\beta_{g,B}
\to
\text{memory/noise}
\to
\text{readout}.
$$

This is a negative-search novelty boundary, not proof of priority.

Never use `first`, `unique`, `unprecedented`, or equivalent priority language unless new independent evidence justifies it.

---

## 12. Standalone Gaussian branch — STOP

The Gaussian work is retained as mathematics/tools only.

Canonical stop files:

- `STANDALONE_GAUSSIAN_NOVELTY_VERDICT.md`
- `NOVELTY_COLLISION_FILIPPOV_BINARY_COHERENT.md`
- `NOVELTY_COLLISION_MELE_RANK_TWO.md`

Do not restart a standalone Gaussian theorem paper from the existing rank-two/coherent-witness material.

---

## 13. Superseded files

The repository intentionally retains the research trail.

The following are historical unless a current document explicitly cites them for provenance:

- `CURRENT_STATE_RANK2_UPDATE.md`;
- `PAPER_CORE_V3.md`;
- `PAPER_CORE_V4.md`;
- `PAPER_CORE_V5_LOCAL_END_TO_END.md`;
- `PAPER_CORE_V6_QUANTUM_LINK_BUDGET.md`;
- endpoint-only source formulas not labeled as $q\to0$ limits;
- old logarithmic single-pulse quantum-cone claims;
- old $25/[4(kR)^2]$ coherent-storage normalization;
- universal $\beta^5$ passive-receiver claims.

Do not resurrect an old result merely because the file still exists.

---

## 14. Canonical reading order

Read current `main` first, then:

1. `AGENTS.md`
2. `experiments/01-causal-quantum-branch-information/CURRENT_STATE_EXTERNAL_REVIEW_CLOSED_V7.md`
3. `experiments/01-causal-quantum-branch-information/manuscript_v7/README.md`
4. `experiments/01-causal-quantum-branch-information/EXTERNAL_REVIEW_RESPONSE_V7.md`
5. `experiments/01-causal-quantum-branch-information/TT_ONE_GRAVITON_MODE_OVERLAP_25_OVER_16_AUDIT.md`
6. `experiments/01-causal-quantum-branch-information/FINITE_HUB_CONTROLLER_RESIDUAL_BOUND_V7.md`
7. `experiments/01-causal-quantum-branch-information/APPROXIMATION_ERROR_BUDGET_V7.md`
8. `experiments/01-causal-quantum-branch-information/GRAVITATIONAL_SPLITTING_CODE_SUBSPACE_AUDIT_V7.md`
9. `experiments/01-causal-quantum-branch-information/FINAL_INTEGRATED_PRIOR_ART_SWEEP_V7.md`
10. `experiments/01-causal-quantum-branch-information/numerics/README.md`

Only go backward into legacy files when tracing a derivation or historical correction.

---

## 15. Current allowed work

### Priority 1 — submission polish

- final prose copyedit;
- final bibliography metadata pass;
- author / acknowledgments / funding metadata;
- optional removal of the orphaned `sin^4` loading example;
- rebuild clean manuscript-only source package from current `main`;
- finalize PRD cover letter;
- tag the submission commit.

### Priority 2 — repository reproducibility

- broaden CI over the committed Gaussian-channel numerical audits;
- add regression checks for benchmark constants, finite-spoke coefficients, and exact-negativity asymptotics;
- keep the active numerical environment pinned.

### Priority 3 — public repository hygiene

- make superseded branches visibly historical;
- keep `README.md`, `AGENTS.md`, and the canonical state synchronized;
- avoid deleting the adversarial research history unless there is a specific maintenance reason.

---

## 16. Do not do this

Unless a concrete defect is identified, do **not**

- derive another Gaussian theorem;
- invent another source architecture;
- reopen $25/16$ normalization;
- reopen finite-spoke propagation;
- reopen the hub residual from zero;
- broaden the paper into a near-term experimental proposal;
- claim generic gravitational quantum communication novelty;
- replace V7 with a new paper core merely for stylistic reasons.

The correct next score increase comes from reproducibility, clarity, and external peer review—not another speculative derivation.
