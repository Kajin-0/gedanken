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

### Experiment 02 — theorem / short-manuscript track

**An Inertia-Controlled Throughput Bound for Passive Gravitational Transduction**

Directory:

[`experiments/02-passive-gravitational-throughput/`](experiments/02-passive-gravitational-throughput/)

Active manuscript:

[`manuscript_v1/`](experiments/02-passive-gravitational-throughput/manuscript_v1/)

Canonical state:

[`CURRENT_STATE.md`](experiments/02-passive-gravitational-throughput/CURRENT_STATE.md)

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

The proof combines

```text
passive selected-port spectral-area cut
        ↓
source and receiver gravitational coupling traces
        ↓
I_2-controlled cumulative quadrupole resource at both endpoints
        ↓
compact TT propagation ceiling 25/16
        ↓
same-two-endpoint passive recurrence control
        ↓
25/12 two-ended inertia closure.
```

The generic passive mathematics, gravitational-antenna modal theory, integrated resonant-mass response, material-response sum rules, directivity, generic wave-channel bounds, and multiple-scattering composition are historical ingredients. No standalone novelty claim is made for them.

A hostile literature audit found strong near-collisions but no inspected primary source stating the exact complete two-ended closure. That negative search is **not** a priority claim.

Start with:

1. [`AGENTS.md`](experiments/02-passive-gravitational-throughput/AGENTS.md)
2. [`CURRENT_STATE.md`](experiments/02-passive-gravitational-throughput/CURRENT_STATE.md)
3. [`CLAIM_LEDGER.md`](experiments/02-passive-gravitational-throughput/CLAIM_LEDGER.md)
4. [`MANUSCRIPT_V1_ADVERSARIAL_AUDIT_2026-08-10.md`](experiments/02-passive-gravitational-throughput/MANUSCRIPT_V1_ADVERSARIAL_AUDIT_2026-08-10.md)
5. [`HOSTILE_PRIOR_ART_COLLISION_AUDIT.md`](experiments/02-passive-gravitational-throughput/HOSTILE_PRIOR_ART_COLLISION_AUDIT.md)
6. [`META_REFEREE_SIGNIFICANCE_AUDIT.md`](experiments/02-passive-gravitational-throughput/META_REFEREE_SIGNIFICANCE_AUDIT.md)
7. [`manuscript_v1/README.md`](experiments/02-passive-gravitational-throughput/manuscript_v1/README.md)

Earlier conversation-only descriptions of branches, commits, CI runs, or files are not repository provenance. Only artifacts verified on the actual remote count.

---

## Experiment 01 key recovery points

For V7 scientific provenance, read:

1. [`CURRENT_STATE_REVIEW_CLOSED_V7.md`](experiments/01-causal-quantum-branch-information/CURRENT_STATE_REVIEW_CLOSED_V7.md)
2. [`CLAIM_LEDGER.md`](experiments/01-causal-quantum-branch-information/CLAIM_LEDGER.md)
3. [`manuscript_v7/README.md`](experiments/01-causal-quantum-branch-information/manuscript_v7/README.md)
4. [`ARCHIVE_STATUS.md`](experiments/01-causal-quantum-branch-information/ARCHIVE_STATUS.md)
5. [`TT_ONE_GRAVITON_MODE_OVERLAP_25_OVER_16_AUDIT.md`](experiments/01-causal-quantum-branch-information/TT_ONE_GRAVITON_MODE_OVERLAP_25_OVER_16_AUDIT.md)
6. [`APPROXIMATION_ERROR_BUDGET_V7.md`](experiments/01-causal-quantum-branch-information/APPROXIMATION_ERROR_BUDGET_V7.md)
7. [`FINAL_INTEGRATED_PRIOR_ART_SWEEP_V7.md`](experiments/01-causal-quantum-branch-information/FINAL_INTEGRATED_PRIOR_ART_SWEEP_V7.md)

Older paper cores and stopped Gaussian-channel novelty branches remain as an audit trail and are not current recovery points.

---

## Automated checks

Pinned scientific Python environment:

- Python `3.12.13`
- NumPy `2.5.1`
- SciPy `1.18.0`

Experiment 01 workflows include manuscript compilation, TT normalization, broader scientific regressions, and isolated submission-package validation.

Experiment 02 has dedicated workflows for

- passive selected-port cut;
- endpoint quadrupole resource;
- compact TT propagation;
- combined `25/12` theorem;
- countably infinite bounded-port truncations;
- same-endpoint passive recurrence;
- manuscript compilation and unresolved-reference checks.

Exact canonical run IDs are recorded in the corresponding `CURRENT_STATE.md` / `CLAIM_LEDGER.md` files rather than inferred from conversation history.

---

## Current work

- **Experiment 01:** submission/editorial work only unless a concrete technical defect appears.
- **Experiment 02:** validate the current manuscript scope-hardening checkpoint, perform the final adversarial manuscript audit, synchronize recovery state, then stop internal theorem broadening and move to external specialist/journal review.

Repository editing/recovery rules are in the root [`AGENTS.md`](AGENTS.md).
