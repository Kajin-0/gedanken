# Response to External V7 Repository / Manuscript Review

**Date:** 2026-08-08  
**Status:** **PUBLICATION-CRITICAL PHYSICS ITEMS ADDRESSED AT THE MANUSCRIPT'S DECLARED WORKING ORDER**

## 1. Review context

The external review rated the repository approximately

- research methodology: 9.5/10;
- conceptual architecture: 9.1/10;
- mathematical/internal consistency: 8.7/10;
- physical-model rigor: 8.1/10;
- novelty defensibility: 7.8/10;
- referee readiness: 7.8/10.

Its most important recommendation was not to open new speculative branches, but to harden the surviving source-resolved gravitational link against three concrete referee objections:

1. independently verify the $25/16$ propagation normalization;
2. bound finite hub/controller residuals;
3. centralize the approximation/error hierarchy.

It additionally recommended

4. specialist scrutiny of the gravitational-splitting code argument;
5. Python CI;
6. dependency pinning;
7. repository archival/reorganization;
8. one final integrated prior-art sweep.

This file records the resulting closure state.

---

# 2. $25/16$ normalization — CLOSED AT WORKING ORDER

## Review concern

Because the proposed paper is fundamentally a normalization paper, the coefficient

$$
\eta_{\rm store}
=\frac{25\mathcal O}{16(kR)^2}
$$

should survive three genuinely independent routes rather than algebraically related reformulations.

## Action

A third route was derived in

`TT_ONE_GRAVITON_MODE_OVERLAP_25_OVER_16_AUDIT.md`.

It begins from canonical TT plane-wave quantization and the normalized one-graviton plus-quadrupole angular mode, not from

- the retarded source--receiver self-energy; or
- the critical-coupling/Friis cross section.

The normalized fixed-frequency source/receiver overlap is

$$
S(z)
=\frac5{32}
\int_{-1}^{1}d\mu\,
(1+6\mu^2+\mu^4)e^{iz\mu}.
$$

Its outgoing component is

$$
\boxed{
S_+(z)
=-\frac{5i}{4}
\frac{P(z)e^{iz}}{z^5},
}
$$

where

$$
\boxed{
P(z)=3-3iz-3z^2+2iz^3+z^4.
}
$$

Thus the TT mode overlap independently regenerates the complete radial polynomial from the earlier retarded-field calculation.

In the wave zone,

$$
S_+(z)
\sim
-\frac{5i}{4}\frac{e^{iz}}z,
$$

so

$$
\boxed{
|S_+|^2
\to
\frac{25}{16z^2}.
}
$$

The three routes are now:

1. retarded conserved-source electric-Weyl response;
2. power flow / critical quadrupole absorption / Friis;
3. canonical TT one-graviton reciprocal mode overlap.

## Numerical regression

Added:

`numerics/tt_mode_overlap_25_16_check.py`

and workflow:

`.github/workflows/tt-normalization.yml`.

The regression directly quadratures the angular overlap, checks the closed form, checks the outgoing/time-reversed decomposition, and verifies the $5/4$ wave-zone amplitude.

GitHub Actions run

`31264071100`

passed.

## Verdict

$$
\boxed{\text{$25/16$ normalization vulnerability: CLOSED at V7 working order.}}
$$

---

# 3. Finite hub/controller residuals — CLOSED TO EXPLICIT DESIGN BOUNDS

## Review concern

The conserved four-spoke source is a controlled nonrelativistic elastic construction, not an exact relativistic hyperelastic body. Finite hub/controller/internal-energy contributions should therefore be bounded rather than merely called small.

## Action

Added:

`FINITE_HUB_CONTROLLER_RESIDUAL_BOUND_V7.md`.

For the retained main branch quadrupole

$$
Q_0
=8\mu L|u|\frac{\tan q}{q},
$$

a generic compact branch-odd energy residual supported inside $r_c$ obeys

$$
\boxed{
\frac{|\Delta Q^{\rm res}|}{Q_0}
\le
\frac{M_\Delta}{8\mu}
\frac{r_c^2}{L|u|}
\frac{q}{\tan q},
}
$$

where

$$
M_\Delta=c^{-2}\int d^3x\,|\Delta T^{00}|.
$$

More specifically:

### symmetric controller bus

Because

$$
\Phi_-=-\Phi_+,
$$

and the controller energy is quadratic,

$$
\boxed{
\Delta Q_{ij}^{\rm ctrl}=0
}
$$

at the retained symmetric quadratic order.

### kinetic / elastic internal energy

$$
\boxed{
\frac{|\Delta Q_E|}{Q_0}
=O\left[\beta^2(u/L)^2\right].
}
$$

### compact controller-energy asymmetry

If the asymmetric energy is bounded by the mechanical excitation scale,

$$
\boxed{
\frac{|\Delta Q_{\rm ctrl}^{\rm asym}|}{Q_0}
=O\left[
\delta_E\beta^2
(u/L)(r_c/L)^2
\right].
}
$$

### finite hub deformation

Let $M_h,r_h,u_h$ characterize hub mass, radius, and branch-odd deformation. Then

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

Define the design parameter

$$
\boxed{
\epsilon_h
=\frac{M_h}{\mu}
\frac{r_h}{L}
\frac{u_h}{u}.
}
$$

The sufficient controlled-source condition is

$$
\boxed{\epsilon_h\ll1.}
$$

An ideal rigid central hub has $u_h=0$.

## Verdict

The source is still not advertised as an exact relativistic material solution. The previous unquantified residual is now an explicit device/compliance parameter plus relativistically suppressed internal-energy corrections.

$$
\boxed{\text{finite hub/controller residual issue: CLOSED to stated model/design bounds.}}
$$

---

# 4. Central approximation/error budget — CLOSED

## Review concern

The approximation parameters were physically controlled but dispersed throughout many notes and manuscript sections.

## Action

Added:

`APPROXIMATION_ERROR_BUDGET_V7.md`

and manuscript section:

`manuscript_v7/sections/05b_approximation_budget.tex`.

The central hierarchy is now explicitly collected in terms of

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
\epsilon_{\rm fb}.
}
$$

The exact TT transfer also gives the propagation probability correction

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

At

$$
kR=10,
$$

the leading $25/[16(kR)^2]$ wave-zone expression is approximately $1.97\%$ high.

## Verdict

$$
\boxed{\text{central approximation hierarchy: CLOSED / manuscript-integrated.}}
$$

---

# 5. Equal-charge gravitational splitting — PRIMARY-SOURCE SPECIALIST AUDIT CLOSED

## Review concern

The equal-charge/dressing step is specialist perturbative quantum-gravity territory and should be checked against the actual Donnelly--Giddings matrix-element condition.

## Action

Added:

`GRAVITATIONAL_SPLITTING_CODE_SUBSPACE_AUDIT_V7.md`.

Donnelly and Giddings' first-order exterior metric matrix element depends on matrix elements of the total Poincare generators.

The V7 condition is

$$
\boxed{
V_C^\dagger Q_A V_C
=q_A I_C,
}
$$

for every

$$
Q_A\in\{P^\mu,M^{\mu\nu}\}.
$$

Therefore, for any two logical states,

$$
\boxed{
\langle\chi|Q_A|\chi'\rangle
=q_A\langle\chi|\chi'\rangle.
}
$$

This fixes **all** charge matrix elements on the code, not only the two diagonal expectations.

No simultaneous Poincare-charge eigenstate assumption is required.

The audit also records the necessary scope:

- a common first-order dressing may carry a branch-common long-range gravitational field;
- the claim is first perturbative order only;
- later branch-dependent quadrupole radiation is the intended causal signal;
- precursor radiation is not hidden once it causally leaves the source neighborhood;
- no exact nonperturbative subsystem/locality theorem is claimed.

## Verdict

$$
\boxed{\text{no structural mismatch found with the cited first-order gravitational-splitting construction.}}
$$

---

# 6. Python CI — PARTIALLY CLOSED / IMPROVED

The external review correctly noted that the repository had scientific numerical audits but only LaTeX CI.

The new TT normalization regression is now executable in GitHub Actions and directly guards the publication-critical propagation coefficient.

Still open as repository-engineering work:

- automated reduced-size Gaussian-channel numerical regressions;
- trace/Hermiticity assertions across legacy channel scripts;
- threshold regression for the historical Gaussian tests.

These are useful reproducibility improvements but are no longer publication-critical to the gravity manuscript's central coefficient.

Status:

$$
\boxed{\text{Python CI: improved, broader legacy regression suite still open.}}
$$

---

# 7. Dependency pinning — OPEN / LOW PUBLICATION PRIORITY

`numerics/requirements.txt` remains minimal rather than version pinned.

A bounded/pinned environment should be added before declaring the repository fully reproducible as software.

This does not currently affect the analytic gravity result, and the publication-critical TT regression passes under the CI environment.

Status:

$$
\boxed{\text{open repository-engineering item.}}
$$

---

# 8. Repository reorganization / archival — OPEN / NONBLOCKING

The external review is correct that legacy research notes make the repository harder for a human to navigate than the current science warrants.

The current continuity/state files reduce the ambiguity for agents but are not a substitute for a human-oriented archive structure.

Recommended eventual work:

- one canonical top-level `STATUS.md`;
- mark legacy notes `superseded` / `superseded_by`;
- move dead paper cores and old Gaussian novelty paths to `archive/`;
- keep one canonical claim ledger.

This should be done **after** the paper state is frozen to avoid destabilizing references during active manuscript work.

Status:

$$
\boxed{\text{open repository-hygiene item; not a physics blocker.}}
$$

---

# 9. Final integrated 2025--2026 prior-art sweep — CLOSED AS A NEGATIVE SEARCH RESULT

Added:

`FINAL_INTEGRATED_PRIOR_ART_SWEEP_V7.md`.

The targeted collision was not generic quantum gravitational communication. It was specifically a separated calculation that closes

$$
\text{local source}
\rightarrow
\text{gravitational branching}
\rightarrow
\text{travelling selected mode}
\rightarrow
\text{remote receiver branching/noise}
\rightarrow
\text{readout}.
$$

The closest inspected works divide across the individual interfaces but do not reproduce the same serial source-resolved normalization.

This is a negative search result, not proof of priority.

The manuscript must continue to avoid “first,” “unique,” or “unprecedented” language.

Status:

$$
\boxed{\text{novelty framing: GO, subject to normal peer-review uncertainty.}}
$$

---

# 10. Manuscript integration / validation

The TT derivation is now included as

`manuscript_v7/sections/tt_normalization_appendix.tex`.

The approximation table is included as

`manuscript_v7/sections/05b_approximation_budget.tex`.

The expanded manuscript compiled successfully in GitHub Actions run

`31264345399`

before the table-placement-only edit.

The approximation table is now explicitly anchored beneath its section heading rather than floating above it; the resulting manuscript is being recompiled through the existing LaTeX workflow.

---

# 11. Updated readiness verdict

The external review's three most important technical vulnerabilities have now been converted into explicit derivations/bounds rather than assurances:

$$
\boxed{
\text{$25/16$ normalization}
\quad+\quad
\text{hub/controller residuals}
\quad+\quad
\text{error hierarchy}
}
$$

and the specialist gravitational-splitting issue has been checked directly against the primary first-order matrix-element criterion.

Within the manuscript's declared

- weak-field;
- nonrelativistic;
- finite-support elastic;
- narrowband;
- linear amplitude-damping;
- first-order gravitational-dressing

regime, no known publication-critical structural physics gap remains from the external review.

The remaining work is predominantly

1. broader software/repository reproducibility;
2. final copyedit and bibliography metadata;
3. submission packaging;
4. normal peer-review uncertainty.

Current internal verdict:

$$
\boxed{\text{V7 has moved from ``close but not referee-proof'' to ``reasonable to submit after final editorial preflight.''}}
$$
