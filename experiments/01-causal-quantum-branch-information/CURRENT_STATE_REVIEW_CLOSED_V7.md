# Current State — V7 Adversarial Review Closure

**Date:** 2026-08-08  
**Status:** **NO KNOWN PUBLICATION-CRITICAL STRUCTURAL PHYSICS GAP REMAINS WITHIN THE DECLARED V7 REGIME; SUBMISSION/EDITORIAL WORK REMAINS**

## Review transparency

The review material in this repository is **not formal journal peer review** and is not presented as endorsement by an external physicist or institution.

The manuscript was hardened through repository-level adversarial review passes, including independent AI-agent critiques, direct equation checks, primary-source comparison, numerical regression, prior-art searches, and manuscript/source validation. These passes are useful for finding errors and sharpening scope, but they do not substitute for journal referees.

Legacy filenames containing `EXTERNAL_REVIEW` are retained only so historical links do not break. This file is the canonical current state.

> Live `main` is authoritative. Check recent commits before any write because concurrent editing may be active.

---

## 1. Active paper

**A Source-Resolved Quantum Link Budget for Propagating Linearized Gravity**

Active manuscript:

`manuscript_v7/`

Central post-handoff coherent transfer:

```math
\boxed{
\tau_c(t)
=\beta_{g,A}\,\eta_{\rm store}(R)\,\beta_{g,B}\,\mathcal T_f(t)
}
```

with leading wave-zone capture

```math
\boxed{
\eta_{\rm store}(R)=\frac{25\mathcal O}{16(kR)^2}.
}
```

The publication claim is the **source-resolved physical normalization and capability chain**, not the multiplication of efficiencies itself.

The active claim boundary is maintained in:

`CLAIM_LEDGER.md`

---

## 2. What V7 does not claim

V7 does not claim a new Gaussian-channel theorem, the first graviton transducer, the first gravity-mediated quantum-information protocol, a near-term experiment, a universal `10^-42` gravitational bound, exact gravitational subsystem locality, or an all-orders quantum-gravity result.

The targeted literature sweep found no inspected work duplicating the same complete source-resolved travelling-radiation normalization. This is a **negative search result, not proof of priority**.

Canonical literature audit:

`FINAL_INTEGRATED_PRIOR_ART_SWEEP_V7.md`

---

## 3. Conserved source: closed at stated model order

The active source is a finite-spoke elastic plus mode with local finite-speed controller completion.

Exact finite-spoke relations include

```math
\boxed{\frac{m_r}{\mu}=q\tan q}
```

and

```math
\boxed{
\Delta Q_{xx}=8\mu Lu\frac{\tan q}{q},
\qquad
\Delta Q_{yy}=-\Delta Q_{xx}.
}
```

The source linewidth is

```math
\boxed{
\kappa_g(q)=
\frac{8G\mu L^2\omega^4}{5c^5}
\frac{(\tan q/q)^2}{\frac12+q/\sin2q}.
}
```

Finite hub/controller residuals have explicit bounds rather than being assumed away.

Canonical audits:

- `CONSERVED_SOURCE_ACTUATOR_AUDIT.md`
- `LOCAL_CONTROLLER_FIELD_COMPLETION_V7.md`
- `FINITE_HUB_CONTROLLER_RESIDUAL_BOUND_V7.md`

---

## 4. Equal-charge gravitational code: closed at first perturbative order

Within the encoded doublet,

```math
\boxed{
V_{\mathcal C}^\dagger P^\mu V_{\mathcal C}=p^\mu I_{\mathcal C},
\qquad
V_{\mathcal C}^\dagger M^{\mu\nu}V_{\mathcal C}=m^{\mu\nu}I_{\mathcal C}.
}
```

The Donnelly–Giddings comparison was made at the matrix-element level. V7 uses only a common **first-order** asymptotic dressing. A branch-common long-range field may remain; the branch-sensitive signal is the retarded difference field.

Canonical audit:

`GRAVITATIONAL_SPLITTING_CODE_SUBSPACE_AUDIT_V7.md`

---

## 5. `25/16` propagation normalization: closed by three routes

The leading storage factor

```math
\boxed{
\eta_{\rm store}=\frac{25\mathcal O}{16(kR)^2}
}
```

is supported by three conceptually distinct derivations:

1. retarded conserved-source field;
2. reciprocal radiation / critical quadrupole absorption;
3. canonical transverse-traceless one-graviton mode overlap.

The one-graviton route reproduces the complete radial polynomial

```math
P(z)=3-3iz-3z^2+2iz^3+z^4
```

and therefore

```math
|t|^2=
\frac{25}{16z^2}
\left(
1-\frac{2}{z^2}
+\frac{3}{z^4}
-\frac{9}{z^6}
+\frac{9}{z^8}
\right).
```

At `kR=10`, the leading wave-zone expression is approximately `1.97%` high.

Canonical audit:

`TT_ONE_GRAVITON_MODE_OVERLAP_25_OVER_16_AUDIT.md`

---

## 6. Approximation hierarchy: centralized and explicitly limited

The controlled regime is organized by

```math
\epsilon_u,\ q,\ q_c,\ \beta,\ B/\omega,\ \mathcal C,\ (kR)^{-1},\ \epsilon_h,\ \epsilon_{\rm fb}\ll1.
```

Mixed corrections are higher product order in the regular perturbative regime, with explicit examples such as `O(beta^2 epsilon_u^2)`. V7 does **not** claim a universal all-orders remainder bound; if a control parameter becomes large or a singular/resonant regime is approached, the separated expansion is no longer sufficient.

Canonical audit:

`APPROXIMATION_ERROR_BUDGET_V7.md`

Manuscript section:

`manuscript_v7/sections/05b_approximation_budget.tex`

---

## 7. Macroscopic source coherence: explicit limitation

The link calculation is conditional on successful preparation and preservation of the modeled source–reference coherence through the encoding/emission interval.

The kilogram-scale benchmark does **not** include a device-specific environmental decoherence calculation. A physical implementation would require the source coherence time to exceed the protocol time after thermal, vibrational, material, controller, and measurement-induced decoherence are included. This practical requirement may be more restrictive than the gravitational transfer coefficient.

This is an explicit limitation, not a solved engineering claim.

---

## 8. Memory, noise, and accessible readout

The memory quantum excess is

```math
\Delta_{\rm mem}=\tau_c-m_c,
```

and the separate readout stage gives

```math
\boxed{
\Delta_{\rm acc}=\tau_r\Delta_{\rm mem}-m_r.
}
```

For vacuum pure loss, the exact optimized binary-coherent negativity obeys

```math
\boxed{
\mathcal N_{\max}(\eta)
=\eta-2\eta^{3/2}+\frac{13}{3}\eta^2+O(\eta^{5/2}).
}
```

The Gaussian entanglement-breaking criterion is established channel theory used as a tool, not a V7 novelty claim.

---

## 9. Passive benchmark

For the deliberately aggressive benchmark

```math
M_e=4\,\mathrm{kg},\qquad
L=1\,\mathrm{m},\qquad
f=1\,\mathrm{MHz},\qquad
Q=10^{12},\qquad
kR=10,
```

ordinary passive matter at both interfaces gives an end-to-end coherent scale near `10^-42`.

This is a **model-dependent passive operating point**, not a fundamental gravitational efficiency bound. If nongravitational loss vanished, gravitational branching could approach unity, but the relevant intrinsic gravitational timescale becomes extraordinarily long.

---

## 10. Historical corrections that materially strengthened V7

The research record includes several substantive corrections:

- the earlier `25/[4(kR)^2]` state-storage coefficient was identified as scattering/extinction normalization and corrected to `25/[16(kR)^2]`;
- a universal logarithmic causal-front claim was narrowed to its actual stationary/optimized conditions;
- the overstrong statement that there is no source–receiver entanglement before `R/c` was replaced by the correct source-controlled communication/input-dependence statement;
- an insufficiently smooth `sin^2` compact waveform was rejected because it is not ultraviolet safe for the ideal coherent-graviton norm.

These corrections are retained in `CLAIM_LEDGER.md` as audit evidence rather than being hidden.

---

## 11. Validation state

The current manuscript/source has passed

- manuscript compilation;
- unresolved citation/reference checks;
- isolated clean submission-source compilation;
- semantic submission safeguards;
- the independent TT overlap regression;
- representative channel, finite-spoke, benchmark, and weak-link negativity regressions.

Numerical environment used by the active checks:

- Python `3.12.13`;
- NumPy `2.5.1`;
- SciPy `1.18.0`.

---

## 12. Current research mode

The strongest current internal statement is:

> **No known publication-critical structural physics gap remains within V7's declared weak-field, nonrelativistic, narrowband linear approximation class.**

This is a submission-readiness assessment, **not** a guarantee of correctness or journal acceptance.

Do not reopen the main theory unless a concrete technical objection appears. Remaining work is submission/editorial metadata, preserving a validated source snapshot, and responding to actual referee comments if they arise.
