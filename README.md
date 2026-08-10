# Gedanken

First-principles theoretical physics and quantum-information thought experiments, developed through explicit derivations, conservation checks, normalization audits, numerical falsification, adversarial review, and prior-art comparison.

## Research tracks

### Experiment 01 — publication track

**A Source-Resolved Quantum Link Budget for Propagating Linearized Gravity**

Directory:

[`experiments/01-causal-quantum-branch-information/`](experiments/01-causal-quantum-branch-information/)

Active manuscript:

[`manuscript_v7/`](experiments/01-causal-quantum-branch-information/manuscript_v7/)

Canonical scientific state:

[`CURRENT_STATE_REVIEW_CLOSED_V7.md`](experiments/01-causal-quantum-branch-information/CURRENT_STATE_REVIEW_CLOSED_V7.md)

Current internal assessment:

> No known publication-critical structural physics gap remains within the manuscript's stated weak-field, nonrelativistic, narrowband linear regime.

Experiment 01 is frozen except for submission/editorial work or a concrete technical defect.

Its post-handoff coherent transfer is

```math
\tau_c(t)
=\beta_{g,A}\,\eta_{\rm store}(R)\,\beta_{g,B}\,\mathcal T_f(t),
```

with leading compact wave-zone storage

```math
\eta_{\rm store}(R)=\frac{25\mathcal O}{16(kR)^2}.
```

The Experiment-01 publication claim is the **source-resolved physical normalization and capability accounting**, not a new Gaussian-channel theorem.

### Experiment 02 — internally frozen theorem / manuscript track

**An Inertia-Controlled Throughput Bound for Passive Gravitational Transduction**

Directory:

[`experiments/02-passive-gravitational-throughput/`](experiments/02-passive-gravitational-throughput/)

Manuscript:

[`manuscript_v1/`](experiments/02-passive-gravitational-throughput/manuscript_v1/)

Canonical freeze record:

[`INTERNAL_FREEZE_CHECKPOINT_2026-08-10.md`](experiments/02-passive-gravitational-throughput/INTERNAL_FREEZE_CHECKPOINT_2026-08-10.md)

Canonical state:

[`CURRENT_STATE.md`](experiments/02-passive-gravitational-throughput/CURRENT_STATE.md)

Authoritative validated science/manuscript SHA:

```text
d05a1e5d5f2f8b4c352f058de73194519c1015e1
```

Internal verdict:

> **INTERNAL AI REVIEW: GO — THEORY AND MANUSCRIPT SCIENCE FROZEN.**

Current in-model result:

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega_0^2}{12c^3R^2}
\min(I_{2,A},I_{2,B})
}
```

where

```math
\Gamma_{\rm coh}
=\frac1{2\pi}\int_{\mathcal B_\nu}
\operatorname{Tr}[T^\dagger(\nu)T(\nu)]\,d\nu,
\qquad
I_2=\int\rho r^2d^3x.
```

The established scope is deliberately narrow:

```text
B/omega_0 << 1                         narrow complex-envelope operation
k_0 a_A, k_0 a_B << 1                 compact endpoints
k_0 R >> 1                             separated wave zone
omega_n <= Omega
Omega = omega_0[1+O(B/omega_0)]        retained carrier-scale endpoint modal sector
finite or countably infinite
bounded-port Markov modal sectors      passive endpoint model
```

Higher-frequency off-resonant endpoint sectors are not automatically controlled by the simple carrier-scale `omega_0^4` resource and require separate treatment.

The proof combines passive selected-port spectral-area cuts, two endpoint gravitational coupling traces, an `I_2`-controlled cumulative quadrupole resource, the compact TT `25/16` propagation ceiling, and same-two-endpoint passive recurrence control.

Most ingredients are historical. A hostile literature audit found strong near-collisions but no inspected primary source stating the exact complete two-ended closure. That negative search is **not** a priority claim.

Start with:

1. [`INTERNAL_FREEZE_CHECKPOINT_2026-08-10.md`](experiments/02-passive-gravitational-throughput/INTERNAL_FREEZE_CHECKPOINT_2026-08-10.md)
2. [`CURRENT_STATE.md`](experiments/02-passive-gravitational-throughput/CURRENT_STATE.md)
3. [`CLAIM_LEDGER.md`](experiments/02-passive-gravitational-throughput/CLAIM_LEDGER.md)
4. [`MANUSCRIPT_V1_FINAL_FREEZE_AUDIT_2026-08-10.md`](experiments/02-passive-gravitational-throughput/MANUSCRIPT_V1_FINAL_FREEZE_AUDIT_2026-08-10.md)
5. [`HOSTILE_PRIOR_ART_COLLISION_AUDIT.md`](experiments/02-passive-gravitational-throughput/HOSTILE_PRIOR_ART_COLLISION_AUDIT.md)
6. [`META_REFEREE_SIGNIFICANCE_AUDIT.md`](experiments/02-passive-gravitational-throughput/META_REFEREE_SIGNIFICANCE_AUDIT.md)
7. [`manuscript_v1/README.md`](experiments/02-passive-gravitational-throughput/manuscript_v1/README.md)

Earlier conversation-only descriptions of branches, commits, CI runs, or files are not repository provenance. Only artifacts verified on the actual remote count.

---

## Automated checks

Pinned scientific Python environment:

- Python `3.12.13`
- NumPy `2.5.1`
- SciPy `1.18.0`

Experiment 01 workflows cover manuscript compilation, TT normalization, broader scientific regressions, and isolated submission-package validation.

Experiment 02 has dedicated workflows for passive selected-port cut, endpoint quadrupole resource, compact TT propagation, the combined `25/12` theorem, countably infinite bounded-port truncations, same-endpoint passive recurrence, and manuscript compilation/reference checks.

The final Experiment-02 science/manuscript SHA passed all seven dedicated gates. Exact run IDs and artifact digest are recorded in the freeze checkpoint rather than inferred from conversation history.

---

## Current work

- **Experiment 01:** submission/editorial work only unless a concrete technical defect appears.
- **Experiment 02:** internal theory/manuscript science is frozen. Further technical changes require a concrete new contradiction or external specialist/journal objection; otherwise work is limited to submission-oriented metadata/editorial tasks and external review.

Repository editing/recovery rules are in the root [`AGENTS.md`](AGENTS.md).
