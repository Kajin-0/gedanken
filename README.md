# Gedanken

First-principles theoretical physics thought experiments developed through explicit derivations, conservation checks, numerical falsification, adversarial review, and prior-art comparison.

## Research tracks

### Experiment 01 — publication track

**A Source-Resolved Quantum Link Budget for Propagating Linearized Gravity**

Directory: [`experiments/01-causal-quantum-branch-information/`](experiments/01-causal-quantum-branch-information/)

Active manuscript: [`manuscript_v7/`](experiments/01-causal-quantum-branch-information/manuscript_v7/)

Canonical state: [`CURRENT_STATE_REVIEW_CLOSED_V7.md`](experiments/01-causal-quantum-branch-information/CURRENT_STATE_REVIEW_CLOSED_V7.md)

Status: frozen except for submission/editorial work or a concrete technical defect. The publication claim is the source-resolved physical normalization/capability chain, not a new standalone Gaussian-channel theorem.

### Experiment 02 — submission-ready frozen theorem track

**An Inertia-Controlled Throughput Bound for Passive Gravitational Transduction**

Directory: [`experiments/02-passive-gravitational-throughput/`](experiments/02-passive-gravitational-throughput/)

Final PRD package: [`submission_prd/`](experiments/02-passive-gravitational-throughput/submission_prd/)

Canonical state: [`CURRENT_STATE.md`](experiments/02-passive-gravitational-throughput/CURRENT_STATE.md)

Final submission preflight: [`FINAL_SUBMISSION_PREFLIGHT_2026-08-11.md`](experiments/02-passive-gravitational-throughput/FINAL_SUBMISSION_PREFLIGHT_2026-08-11.md)

Underlying validated science/theorem checkpoint:

```text
bfae23af41aefb3104d639099299b3432b4a14fe
```

Validated final submission-manuscript checkpoint:

```text
6f7a60b3b05dea9f288b1b07e6f2e55acaf34e83
```

Status: **GO / submission ready after human sign-off.** The science is frozen unless a concrete defect, prior-art collision, or substantive external objection appears.

The current sector-resolved result includes

```math
\Gamma_{\rm coh}
\lesssim
\frac{5G\omega_0^2}{4c^3R^2}I_{\hat R}
\le
\frac{25G\omega_0^2}{12c^3R^2}I_2,
```

within the retained compact, narrowband, separated-wave-zone, bounded-port Markov modal sector recorded in Experiment 02's canonical files.

### Experiment 03 — active exploratory theory track

**Superconducting Photon-to-Flux Transduction**

Directory: [`experiments/03-superconducting-photon-flux-transduction/`](experiments/03-superconducting-photon-flux-transduction/)

Canonical state: [`CURRENT_STATE.md`](experiments/03-superconducting-photon-flux-transduction/CURRENT_STATE.md)

Logical trail: [`DERIVATION_LOG.md`](experiments/03-superconducting-photon-flux-transduction/DERIVATION_LOG.md)

Claim status: [`CLAIM_LEDGER.md`](experiments/03-superconducting-photon-flux-transduction/CLAIM_LEDGER.md)

Literature boundary: [`LITERATURE_LEDGER.md`](experiments/03-superconducting-photon-flux-transduction/LITERATURE_LEDGER.md)

Manuscript gate: [`NOVELTY_GATES.md`](experiments/03-superconducting-photon-flux-transduction/NOVELTY_GATES.md)

Current question: can a single absorbed LWIR photon transiently alter a Josephson phase-escape landscape so that one direction is selected and the event is captured as a persistent superconducting fluxoid state, while intrinsic false switching remains very low?

Current working chain:

```text
LWIR photon
 -> low-heat-capacity photon-sensitive Josephson element
 -> transient barrier / phase-potential modification
 -> directionally favored phase escape
 -> fluxoid transition n -> n+1
 -> relaxation of the hot/quasiparticle state
 -> persistent superconducting flux/current memory
```

The initial constant-barrier analysis produced a provisional photon-efficiency / MQT feasibility window, but it is **not yet a theorem**. The immediate task is to recompute the time-dependent escape problem from the actual rf-SQUID/Josephson potential, damping regime, and `T_e(t)`.

Known prior-art boundaries already include superconducting MIR/LWIR single-photon detection, graphene Josephson calorimetric switching, field-free superconducting/Josephson diode effects, and illumination-driven superconducting phase batteries and vorticity switching. Experiment 03 currently makes **no novelty claim**.

Status: **GO for continued theory; NO-GO for manuscript until quantitative and hostile collision-audit gates are passed.**

---

## Current work

- **Experiment 01:** frozen publication/submission track.
- **Experiment 02:** submission-ready after human sign-off; science frozen.
- **Experiment 03:** active exploratory theory. Important advances, failures, architecture changes, and literature collisions must be recorded in the experiment's recovery files rather than left only in conversation history.

## Repository continuity

Start with [`AGENTS.md`](AGENTS.md) and [`CONTEXT_HANDOFF.md`](CONTEXT_HANDOFF.md).

Live remote repository state overrides conversation history. Conversation-only branches, commits, equations, or validation claims are not repository provenance.
