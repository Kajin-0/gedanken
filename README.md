# Gedanken

First-principles theoretical physics and quantum-information thought experiments, developed through explicit derivations, conservation checks, numerical tests, normalization audits, and prior-art comparison.

## Current project

**A Source-Resolved Quantum Link Budget for Propagating Linearized Gravity**

Active manuscript:

[`experiments/01-causal-quantum-branch-information/manuscript_v7/`](experiments/01-causal-quantum-branch-information/manuscript_v7/)

Canonical scientific state:

[`CURRENT_STATE_EXTERNAL_REVIEW_CLOSED_V7.md`](experiments/01-causal-quantum-branch-information/CURRENT_STATE_EXTERNAL_REVIEW_CLOSED_V7.md)

Current internal assessment:

> No known publication-critical structural physics gap remains from the external review within the manuscript's stated weak-field, nonrelativistic, narrowband linear regime.

This is a submission-readiness statement, not a guarantee of peer-review acceptance.

---

## Central result

After local source preparation and controller handoff, the coherent source-to-memory transfer separates into four physical factors:

```math
\boxed{
\tau_c(t)
=\beta_{g,A}\,\eta_{\rm store}(R)\,\beta_{g,B}\,\mathcal T_f(t)
}
```

with source gravitational branching

```math
\beta_{g,A}=\frac{\kappa_{g,A}}{\kappa_A},
```

free-space mode capture

```math
\boxed{
\eta_{\rm store}(R)=\frac{25\mathcal O}{16(kR)^2}
}
```

receiver gravitational branching

```math
\beta_{g,B}=\frac{\kappa_{g,B}}{\kappa_B},
```

and temporal loading

```math
0\le \mathcal T_f(t)\le1.
```

The memory quantum excess is

```math
\Delta_{\rm mem}=\tau_c-m_c,
```

and a separate noisy readout gives

```math
\boxed{
\Delta_{\rm acc}=\tau_r\Delta_{\rm mem}-m_r.
}
```

The publication claim is the **source-resolved physical normalization and capability accounting**. It is not a new Gaussian-channel theorem, not the first graviton transducer proposal, and not a near-term experimental design.

---

## Conserved finite-support source

For the explicit four-spoke elastic plus mode,

```math
q=\frac{\omega L}{c_s},
```

with exact finite-spoke boundary relation

```math
\boxed{
\frac{m_r}{\mu}=q\tan q.
}
```

The branch quadrupole is

```math
\boxed{
\Delta Q_{xx}=8\mu Lu\frac{\tan q}{q},
\qquad
\Delta Q_{yy}=-\Delta Q_{xx}.
}
```

The corrected gravitational linewidth is

```math
\boxed{
\kappa_g(q)=
\frac{8G\mu L^2\omega^4}{5c^5}
\frac{(\tan q/q)^2}{\frac12+q/\sin 2q}.
}
```

A finite-speed local controller is included explicitly. The simplified resonant controller used in the manuscript is the narrowband limit of that causal model.

---

## Equal-charge gravitational code

At the retained perturbative order, the encoded system satisfies

```math
\boxed{
V_{\mathcal C}^\dagger P^\mu V_{\mathcal C}=p^\mu I_{\mathcal C},
}
```

```math
\boxed{
V_{\mathcal C}^\dagger M^{\mu\nu}V_{\mathcal C}=m^{\mu\nu}I_{\mathcal C}.
}
```

This does **not** mean gravity vanishes outside the source. A branch-independent long-range gravitational field may remain. The claim is only that source-controlled branch information is absent before its causal disturbance reaches the receiver, within the stated first-order gravitational approximation.

---

## Independent propagation checks

The factor `25/16` has three independent derivations:

1. retarded conserved-source field;
2. reciprocal radiation/absorption normalization;
3. canonical transverse-traceless one-graviton mode overlap.

The third derivation reproduces the complete radial polynomial

```math
P(z)=3-3iz-3z^2+2iz^3+z^4.
```

The exact transfer probability is

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

At `kR = 10`, the leading wave-zone expression is about `1.97%` high.

---

## Start here

For the active scientific state, read:

1. [`AGENTS.md`](AGENTS.md) — current recovery and editing rules;
2. [`CURRENT_STATE_EXTERNAL_REVIEW_CLOSED_V7.md`](experiments/01-causal-quantum-branch-information/CURRENT_STATE_EXTERNAL_REVIEW_CLOSED_V7.md) — canonical scientific state;
3. [`ARCHIVE_STATUS.md`](experiments/01-causal-quantum-branch-information/ARCHIVE_STATUS.md) — active versus historical notes;
4. [`manuscript_v7/README.md`](experiments/01-causal-quantum-branch-information/manuscript_v7/README.md) — manuscript layout and build instructions;
5. [`TT_ONE_GRAVITON_MODE_OVERLAP_25_OVER_16_AUDIT.md`](experiments/01-causal-quantum-branch-information/TT_ONE_GRAVITON_MODE_OVERLAP_25_OVER_16_AUDIT.md) — independent one-graviton normalization;
6. [`APPROXIMATION_ERROR_BUDGET_V7.md`](experiments/01-causal-quantum-branch-information/APPROXIMATION_ERROR_BUDGET_V7.md) — approximation hierarchy;
7. [`FINAL_INTEGRATED_PRIOR_ART_SWEEP_V7.md`](experiments/01-causal-quantum-branch-information/FINAL_INTEGRATED_PRIOR_ART_SWEEP_V7.md) — restrained novelty boundary.

Older paper cores and stopped Gaussian-channel novelty branches remain in the repository as an audit trail. They are not current recovery points. See [`ARCHIVE_STATUS.md`](experiments/01-causal-quantum-branch-information/ARCHIVE_STATUS.md).

---

## Numerical and manuscript checks

The repository automatically checks:

- that the V7 manuscript compiles and has no unresolved references;
- the independent one-graviton propagation normalization;
- representative thermal attenuation, amplification, additive noise, finite-spoke corrections, benchmark values, and weak-link negativity;
- that the clean manuscript-only source package compiles independently.

The numerical environment used for the current checks is Python `3.12.13`, NumPy `2.5.1`, and SciPy `1.18.0`.

---

## Current work

Do not open another theoretical branch unless a concrete physics defect appears.

The remaining work is limited to private author/submission information, preserving the final validated manuscript snapshot, and responding to actual peer-review objections if they arise.
