# Gedanken

First-principles theoretical physics and quantum-information thought experiments, developed through explicit derivations, conservation checks, numerical tests, normalization audits, adversarial review, and prior-art comparison.

## Research tracks

### Experiment 01 — publication track

**A Source-Resolved Quantum Link Budget for Propagating Linearized Gravity**

Active manuscript:

[`experiments/01-causal-quantum-branch-information/manuscript_v7/`](experiments/01-causal-quantum-branch-information/manuscript_v7/)

Canonical scientific state:

[`CURRENT_STATE_REVIEW_CLOSED_V7.md`](experiments/01-causal-quantum-branch-information/CURRENT_STATE_REVIEW_CLOSED_V7.md)

Current internal assessment:

> No known publication-critical structural physics gap remains within the manuscript's stated weak-field, nonrelativistic, narrowband linear regime.

Experiment 01 is frozen except for submission/editorial work or a concrete technical defect.

### Experiment 02 — exploratory track

**Passive Gravitational Throughput**

Directory:

[`experiments/02-passive-gravitational-throughput/`](experiments/02-passive-gravitational-throughput/)

Status:

> Open research question. No theorem is yet verified and no manuscript exists.

A previous conversational exploration suggested the provisional target

```math
\Gamma_{\rm coh}
\stackrel{?}{\lesssim}
\frac{25G\omega^2}{12c^3R^2}\min(I_A,I_B),
```

but Experiment 02 is explicitly rebuilding this question from first principles. The candidate coefficient, assumptions, and even the existence of an inertia-only bound must be independently derived or falsified.

Start with:

1. [`QUESTION.md`](experiments/02-passive-gravitational-throughput/QUESTION.md)
2. [`ASSUMPTIONS.md`](experiments/02-passive-gravitational-throughput/ASSUMPTIONS.md)
3. [`HYPOTHESES.md`](experiments/02-passive-gravitational-throughput/HYPOTHESES.md)
4. [`CLAIM_LEDGER.md`](experiments/02-passive-gravitational-throughput/CLAIM_LEDGER.md)
5. [`CURRENT_STATE.md`](experiments/02-passive-gravitational-throughput/CURRENT_STATE.md)
6. [`AGENTS.md`](experiments/02-passive-gravitational-throughput/AGENTS.md)

Earlier conversation-only descriptions of Experiment 02 branches, commits, CI runs, or manuscript files are not repository provenance and are not scientific evidence.

---

## Experiment 01 central result

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

The Experiment 01 publication claim is the **source-resolved physical normalization and capability accounting**. It is not a new Gaussian-channel theorem, not the first graviton transducer proposal, and not a near-term experimental design.

---

## Experiment 01 conserved finite-support source

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

## Experiment 01 equal-charge gravitational code

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

## Experiment 01 independent propagation checks

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

## Experiment 01 start here

For the publication-track scientific state, read:

1. [`CURRENT_STATE_REVIEW_CLOSED_V7.md`](experiments/01-causal-quantum-branch-information/CURRENT_STATE_REVIEW_CLOSED_V7.md)
2. [`CLAIM_LEDGER.md`](experiments/01-causal-quantum-branch-information/CLAIM_LEDGER.md)
3. [`manuscript_v7/README.md`](experiments/01-causal-quantum-branch-information/manuscript_v7/README.md)
4. [`ARCHIVE_STATUS.md`](experiments/01-causal-quantum-branch-information/ARCHIVE_STATUS.md)
5. [`TT_ONE_GRAVITON_MODE_OVERLAP_25_OVER_16_AUDIT.md`](experiments/01-causal-quantum-branch-information/TT_ONE_GRAVITON_MODE_OVERLAP_25_OVER_16_AUDIT.md)
6. [`APPROXIMATION_ERROR_BUDGET_V7.md`](experiments/01-causal-quantum-branch-information/APPROXIMATION_ERROR_BUDGET_V7.md)
7. [`FINAL_INTEGRATED_PRIOR_ART_SWEEP_V7.md`](experiments/01-causal-quantum-branch-information/FINAL_INTEGRATED_PRIOR_ART_SWEEP_V7.md)

Older paper cores and stopped Gaussian-channel novelty branches remain as an audit trail. They are not current recovery points.

---

## Numerical and manuscript checks

Experiment 01 automatically checks:

- V7 manuscript compilation and unresolved references;
- independent one-graviton propagation normalization;
- representative thermal attenuation, amplification, additive noise, finite-spoke corrections, benchmark values, and weak-link negativity;
- independent compilation of the clean manuscript-only source package.

The numerical environment used for the current Experiment 01 checks is Python `3.12.13`, NumPy `2.5.1`, and SciPy `1.18.0`.

Experiment 02 does **not** yet claim its own CI validation. New tests will be added only after the corresponding derivations are real repository artifacts.

---

## Current work

- **Experiment 01:** submission/editorial work only unless a concrete technical defect appears.
- **Experiment 02:** active first-principles reconstruction and falsification of the passive gravitational-throughput question.

`AGENTS.md` contains the repository recovery/editing protocol and the separation rules between the frozen publication track and the exploratory track.
