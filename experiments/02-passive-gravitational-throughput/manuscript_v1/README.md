# Experiment 02 manuscript v1

**Title:** *An Inertia-Controlled Throughput Bound for Passive Gravitational Transduction*

This is the internally frozen short specialist manuscript source for Experiment 02.

## Frozen science source

Authoritative validated commit:

```text
d05a1e5d5f2f8b4c352f058de73194519c1015e1
```

Internal verdict:

> **INTERNAL AI REVIEW: GO — THEORY/MANUSCRIPT SCIENCE FROZEN.**

Canonical freeze record:

`../INTERNAL_FREEZE_CHECKPOINT_2026-08-10.md`

## Scientific result

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega_0^2}{12c^3R^2}
\min(I_{2,A},I_{2,B})
}
```

The theorem is established only within its declared compact narrowband retained-sector class. The manuscript does not claim novelty for gravitational-antenna eigenmode theory, integrated resonant-mass response, arbitrary-body modal projection, response sum rules, generic passive `H2` mathematics, generic wave-channel bounds, directivity, or multiple-scattering composition.

## Scope

```text
B/omega_0 << 1
k_0 a_A, k_0 a_B << 1
k_0 R >> 1
Omega = omega_0[1+O(B/omega_0)]
finite or countably infinite bounded-port Markov retained modal sectors
```

The simple `omega_0^4` endpoint resource does **not** automatically include uncontrolled higher-frequency modes `omega_n >> omega_0` merely because their off-resonant tails enter a narrow measured band. Such sectors require a separate bound.

Explicitly outside the current theorem:

- broad absolute-frequency operation without retaining frequency-dependent resources;
- uncontrolled higher-frequency off-resonant endpoint sectors;
- arbitrary unbounded PDE boundary ports;
- genuinely non-Markov continua;
- active gain/pumping/feedback;
- extended phased apertures;
- added relays or external gravitational cavities;
- reactive near-field exchange;
- relativistic/nonlinear matter and higher-multipole-dominated regimes.

## Validation

All six physics workflows and the manuscript workflow passed on the frozen source SHA:

```text
passive cut        run 31429984820 — PASS
endpoint resource  run 31429984888 — PASS
TT propagation     run 31429984826 — PASS
combined bound     run 31429984854 — PASS
infinite modal     run 31429984786 — PASS
recurrence         run 31429984808 — PASS
manuscript         run 31429984776, job 93590769191 — PASS
```

Final manuscript: **10 pages**, no unresolved references/citations.

Artifact:

```text
name: experiment02-manuscript-v1
artifact ID: 9078731235
SHA256: 370c852f7a65305ffe5dbdb6a5ce5fcf61d5e620668a6a0c90b0baa63ad9d917
```

## Build

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Workflow:

`.github/workflows/latex-experiment02.yml`

## Audit boundary

Read:

- `../MANUSCRIPT_V1_ADVERSARIAL_AUDIT_2026-08-10.md`
- `../MANUSCRIPT_V1_FINAL_FREEZE_AUDIT_2026-08-10.md`
- `../HOSTILE_PRIOR_ART_COLLISION_AUDIT.md`
- `../META_REFEREE_SIGNIFICANCE_AUDIT.md`
- `../CLAIM_LEDGER.md`

The final audits found no publication-critical internal coefficient or normalization failure. The remaining risk is external historical/significance/model-scope review.

The public manuscript remains `Anonymous`; private author/submission metadata belongs at the external submission boundary.

Do not modify manuscript science without a concrete technical defect or external specialist/journal objection.
