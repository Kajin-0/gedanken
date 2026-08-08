# Current State — V7 External Review Closure

**Date:** 2026-08-08  
**Status:** **PUBLICATION-CRITICAL EXTERNAL-REVIEW PHYSICS ITEMS CLOSED AT DECLARED WORKING ORDER; FINAL EDITORIAL/SUBMISSION PREFLIGHT REMAINS**

> Live `main` is authoritative. Check recent commits before future writes because concurrent editing may be active.

---

## 1. Canonical paper

**A Source-Resolved Quantum Link Budget for Propagating Linearized Gravity**

Active manuscript:

`manuscript_v7/`

Central post-handoff link:

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
\boxed{
\eta_{\rm store}(R)
=\frac{25\mathcal O}{16(kR)^2}
}
$$

at leading wave-zone order.

The publication claim is the **source-resolved serial normalization**, not a new Gaussian-channel theorem, not the first graviton transducer, and not a near-term experimental proposal.

---

# 2. External-review item 1 — $25/16$ normalization: CLOSED

The reviewer identified this as the highest-value independent audit because normalization is central to the paper.

There are now three independent routes.

## A. Retarded conserved-source field

Retarded electric-Weyl / receiver tidal response:

$$
 t_{BA}
=-\frac{5i}{4}
\frac{P(z)e^{iz}}{z^5}.
$$

## B. Power flow / critical absorption / Friis

Source directivity and critical $l=2$ absorption give

$$
\eta_{\rm store}
=\frac{25}{16z^2}.
$$

## C. Canonical TT one-graviton mode overlap

New audit:

`TT_ONE_GRAVITON_MODE_OVERLAP_25_OVER_16_AUDIT.md`

The normalized plus-quadrupole one-graviton mode gives

$$
S(z)
=\frac5{32}
\int_{-1}^{1}d\mu
(1+6\mu^2+\mu^4)e^{iz\mu},
$$

with outgoing component

$$
\boxed{
S_+(z)
=-\frac{5i}{4}
\frac{P(z)e^{iz}}{z^5},
}
$$

and

$$
\boxed{
P(z)
=3-3iz-3z^2+2iz^3+z^4.
}
$$

Thus the canonical TT overlap independently reproduces not only the $5/4$ far-field coefficient but the entire radial polynomial previously obtained from the retarded field calculation.

Wave zone:

$$
\boxed{
S_+(z)
\sim
-\frac{5i}{4}
\frac{e^{iz}}z,
}
$$

so

$$
\boxed{
|S_+|^2
\to
\frac{25}{16z^2}.
}
$$

The TT derivation is also included in the manuscript appendix:

`manuscript_v7/sections/tt_normalization_appendix.tex`.

The live symbol definition was semantically checked and corrected to

$$
\boxed{u_\lambda(\hat{\mathbf n})}
$$

rather than the accidental TeX-valid $\nu_\lambda$ variant.

---

# 3. TT normalization numerical regression: PASS

New script:

`numerics/tt_mode_overlap_25_16_check.py`

New workflow:

`.github/workflows/tt-normalization.yml`

The regression checks

1. direct quadrature of the TT angular overlap;
2. equality with the closed trigonometric form;
3. equality with outgoing + time-reversed decomposition;
4. wave-zone convergence to amplitude coefficient $5/4$;
5. normalization $S(0)\to1$.

Initial workflow run:

`31264071100`

passed.

The numerical environment was then pinned to the versions that produced that passing run:

- Python `3.12.13`;
- NumPy `2.5.1`;
- SciPy `1.18.0`.

Pinned workflow run:

`31264964946`

also passed.

Therefore the publication-critical normalization now has both analytic and executable independent checks.

---

# 4. External-review item 2 — finite hub/controller residuals: CLOSED TO EXPLICIT BOUNDS

New audit:

`FINITE_HUB_CONTROLLER_RESIDUAL_BOUND_V7.md`

Main branch quadrupole:

$$
Q_0
=8\mu L|u|\frac{\tan q}{q}.
$$

The symmetric controller bus satisfies

$$
\Phi_-=-\Phi_+,
$$

and its local quadratic energy is branch even, so

$$
\boxed{
\Delta Q_{ij}^{\rm ctrl}=0
}
$$

at the retained symmetric quadratic controller/linear-elastic order.

Internal kinetic/elastic mass-energy corrections scale as

$$
\boxed{
\frac{|\Delta Q_E|}{Q_0}
=O\left[\beta^2(u/L)^2\right].
}
$$

A compact branch-asymmetric controller energy tied to the mechanical excitation scale gives

$$
\boxed{
\frac{|\Delta Q_{\rm ctrl}^{\rm asym}|}{Q_0}
=O\left[
\delta_E\beta^2(u/L)(r_c/L)^2
\right].
}
$$

The only generic finite-source residual not automatically killed by symmetry is hub deformation:

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
\boxed{
\epsilon_h
=\frac{M_h}{\mu}
\frac{r_h}{L}
\frac{u_h}{u}.
}
$$

Controlled source design requires

$$
\boxed{\epsilon_h\ll1.}
$$

The ideal rigid central hub has $u_h=0$.

This does not turn V7 into an exact relativistic material theory. It converts the former qualitative residual caveat into a measurable/computable source-design parameter plus parametrically suppressed internal-energy corrections.

---

# 5. External-review item 3 — approximation/error budget: CLOSED

New audit:

`APPROXIMATION_ERROR_BUDGET_V7.md`

Manuscript section:

`manuscript_v7/sections/05b_approximation_budget.tex`

The main hierarchy is now centralized as

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

where

$$
\epsilon_u=|u|/L,
$$

$$
q=\omega L/c_s,
$$

$$
q_c=\omega L/v_c,
$$

$$
\beta=\omega L/c,
$$

$$
B=\max(g,\kappa_A,\kappa_B,1/T),
$$

$$
\mathcal C=2GM/(c^2L).
$$

The exact TT transfer gives

$$
\boxed{
|t|^2
=\frac{25}{16z^2}
\left(
1-\frac2{z^2}
+\frac3{z^4}
-\frac9{z^6}
+\frac9{z^8}
\right).
}
$$

At the benchmark

$$
kR=10,
$$

the leading $25/[16(kR)^2]$ expression is approximately $1.97\%$ high.

The manuscript table is anchored directly under its section heading and has been rendered/read at normal page scale.

---

# 6. External-review item 4 — gravitational splitting: PRIMARY-SOURCE AUDIT CLOSED

New audit:

`GRAVITATIONAL_SPLITTING_CODE_SUBSPACE_AUDIT_V7.md`

Primary comparison:

William Donnelly and Steven B. Giddings,
*Phys. Rev. D* **98**, 086006 (2018), arXiv:1805.11095.

Their first-order exterior metric matrix element depends on the **matrix elements** of the total Poincare generators $P^\mu$ and $M^{\mu\nu}$.

V7 uses the stronger operator/code condition

$$
\boxed{
V_C^\dagger Q_A V_C
=q_AI_C,
}
$$

so for arbitrary logical states

$$
\boxed{
\langle\chi|Q_A|\chi'\rangle
=q_A\langle\chi|\chi'\rangle.
}
$$

Thus all charge matrix elements are fixed on the code.

This is the appropriate structure for the first-order splitting construction; no simultaneous Poincare-charge eigenstate assumption is required.

Safe scope retained:

- common branch-independent long-range dressing may exist;
- only branch dependence is hidden before causal escape;
- the statement is first perturbative order;
- later branch-dependent quadrupole/precursor radiation is the intended signal;
- no exact tensor-factor locality or nonperturbative quantum-gravity theorem is claimed.

No structural mismatch was found with the cited first-order construction.

---

# 7. Final integrated 2025--2026 prior-art sweep: GO WITH RESTRAINED CLAIMS

New file:

`FINAL_INTEGRATED_PRIOR_ART_SWEEP_V7.md`

The collision target was specifically a separated calculation that closes

$$
\text{local source}
\to
\text{source gravitational branching}
\to
\text{travelling selected mode}
\to
\text{remote receiver branching/noise}
\to
\text{readout}.
$$

The closest inspected works occupy individual or alternative interfaces:

- conserved/classical source to quantum radiation;
- branch source to graviton difference state;
- incident normalized GW mode to resonant detector;
- propagating-graviton matter entanglement with effective coupling;
- direct Newtonian/optomechanical gravity channels;
- local photon--graviton transduction.

No inspected work was found that duplicates the same V7 serial source-resolved normalization.

This remains a **negative search result, not proof of priority**.

Do not use “first,” “unique,” or “unprecedented.”

---

# 8. Manuscript validation after review closure

The V7 manuscript now includes

- the centralized approximation table;
- the independent TT normalization appendix;
- the previously integrated source/controller, virtual-mode, noise/readout, passive-bound, and exact-negativity sections.

Manuscript workflow after the final semantic TT symbol correction:

`31264889125`

passed all steps:

1. TeX installation;
2. `latexmk` compile;
3. unresolved citation/reference check;
4. PDF artifact upload.

Rendered PDF QA at 160 dpi:

- approximation hierarchy heading appears before the table;
- table is readable at normal page scale;
- TT appendix renders the corrected $u_\lambda$ definition;
- exact $P(z)$ / $S_+(z)$ equations are legible;
- no new clipping or overlap observed in the reviewed pages.

---

# 9. Point-by-point external review response

Canonical response document:

`EXTERNAL_REVIEW_RESPONSE_V7.md`

Current state of review items:

| Review item | Status |
|---|---|
| independent $25/16$ derivation | **closed** |
| finite hub/controller residual bound | **closed to stated model/design bounds** |
| centralized approximation/error budget | **closed / manuscript integrated** |
| specialist gravitational-splitting audit | **closed at first perturbative order** |
| Python numerical CI | **publication-critical TT regression added and passing** |
| pin numerical environment | **closed for active numerical suite** |
| final integrated prior-art sweep | **closed as negative search result** |
| broad legacy numerical regression CI | open, nonblocking repository work |
| archive/superseded-note reorganization | open, nonblocking repository work |

---

# 10. Publication readiness

The external review originally characterized V7 as close but not yet referee-proof because the remaining issues concentrated in

$$
\text{normalization verification}
+
\text{source/controller residuals}
+
\text{perturbative dressing scope}.
$$

Those three issues now have explicit independent derivations/bounds/primary-source audits.

The strongest current internal verdict is therefore

$$
\boxed{
\text{No known publication-critical structural physics gap remains from the external review within V7's declared approximation class.}
}
$$

This is **not** a guarantee of peer-review acceptance.

The remaining pre-submission work is editorial and repository-facing:

1. final prose copyedit;
2. final bibliography metadata pass;
3. author/acknowledgment/funding metadata;
4. optional removal of the orphaned $\sin^4$ loading example;
5. rebuild the clean manuscript-only source archive from current `main`;
6. finalize PRD cover letter;
7. tag the submission commit.

Do not reopen the main physics derivations unless a new concrete technical objection appears.
