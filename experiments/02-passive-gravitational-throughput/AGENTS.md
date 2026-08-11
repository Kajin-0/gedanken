# AGENTS.md — Experiment 02 Recovery and Freeze Protocol

**Experiment:** `02-passive-gravitational-throughput`  
**Mode:** internally frozen core theorem / externally responsive manuscript track.  
**Current theorem status:** established within the declared compact retained-sector bounded-port narrowband model; the canonical submission statement is now an explicit asymptotic coefficient, with a separate exact finite-`kR` compact-TT propagation correction.  
**Original frozen science/manuscript SHA:** `1ce596493073dbb49e6eb71f1a6df0566ff3c25b`.  
**Internal verdict:** **GO — no theorem broadening absent a concrete defect or external objection.**

This file is the first operational file an automated contributor should read after the repository-level `AGENTS.md`.

## 1. Live-repository discipline

Before every repository write:

1. fetch the current `main` head;
2. verify that this experiment directory exists on that exact ref;
3. compare intervening commits with the last-seen head;
4. fetch the exact current target blob immediately before replacement;
5. never force-update a stale branch/ref;
6. after writing, fetch the resulting commit and changed files from `main` to verify persistence;
7. if local git and a connector disagree about remote state, treat the discrepancy as a blocking integrity problem.

Repository provenance must be verifiable from the actual remote. Conversation history is not repository evidence.

## 2. Submission-manuscript style constraint

The physics article itself must **never mention the repository, GitHub, commit hashes, internal experiment labels, source-control state, CI, or project bookkeeping**. Those belong in internal records, not in the manuscript. Numerical checks may be described scientifically as validation calculations without naming their storage or execution infrastructure. Do not refer to an unpublished internal `Experiment 01` or other internal project artifact as a companion paper.

## 3. Canonical recovery order

Read:

1. `INTERNAL_FREEZE_CHECKPOINT_2026-08-10.md`
2. `CURRENT_STATE.md`
3. `CLAIM_LEDGER.md`
4. `RECENT_GRAVITY_COMMUNICATION_COLLISION_AUDIT_2026-08-10.md`
5. `MANUSCRIPT_V1_FINAL_FREEZE_AUDIT_2026-08-10.md`
6. `MANUSCRIPT_V1_ADVERSARIAL_AUDIT_2026-08-10.md`
7. `HOSTILE_PRIOR_ART_COLLISION_AUDIT.md`
8. `META_REFEREE_SIGNIFICANCE_AUDIT.md`
9. `SECOND_CRITICAL_REVIEW_AUDIT_2026-08-10.md`
10. `manuscript_v1/README.md`

For proof provenance, then read:

1. `PASSIVE_SELECTED_PORT_CUT_DERIVATION.md`
2. `GRAVITATIONAL_ENDPOINT_RESOURCE_DERIVATION.md`
3. `TT_PROPAGATION_BOUND_DERIVATION.md`
4. `TT_FINITE_DISTANCE_OPERATOR_DERIVATION.md`
5. `NARROWBAND_NORMALIZATION_AUDIT.md`
6. `FINITE_TWO_ENDED_INERTIA_BOUND.md`
7. `INFINITE_DIMENSIONAL_BOUNDED_PORT_EXTENSION.md`
8. `PASSIVE_TWO_ENDPOINT_RECURRENCE.md`

## 4. Canonical theorem statement

Use

```text
omega_0   absolute gravitational carrier angular frequency
nu        complex-envelope detuning
B         envelope bandwidth, B/omega_0 << 1
k_0       omega_0/c
a_A,a_B   endpoint radii, k_0 a_A,k_0 a_B << 1
R         separation, k_0 R >> 1
Omega     upper retained modal frequency,
          Omega=omega_0[1+O(B/omega_0)]
I_2       int rho r^2 dV about endpoint COM
```

The precise submission theorem is

```math
\boxed{
\limsup_{k_0R\to\infty}
(k_0R)^2\Gamma_{\rm coh}
\le
\frac{25G\Omega^4}{12c^5}
\min(I_{2,A},I_{2,B})
}
```

within the retained compact-quadrupole carrier-frozen model.

The transparent leading carrier form remains

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega_0^2}{12c^3R^2}
\min(I_{2,A},I_{2,B})
}
```

but `lesssim` must be described as the compact/narrowband leading form, not a uniform finite-distance theorem.

The outgoing compact-TT propagation operator has the exact `|m|=2` maximum for `z=kR>=3`:

```math
\|P_g(z)\|_{op}^2
=\frac{25}{16z^2}
\left(1-\frac2{z^2}+\frac3{z^4}-\frac9{z^6}+\frac9{z^8}\right).
```

At `z=100` the correction factor is `0.99980003`.

This is a complex-envelope coherent-transfer spectral-area theorem, not a capacity theorem.

## 5. Scope that must not be dropped

Do not silently broaden to

- broad absolute-frequency operation with one carrier coefficient;
- uncontrolled high-frequency endpoint modes whose off-resonant tails are not separately bounded;
- unbounded PDE boundary-control/observation ports;
- genuinely non-Markov continua;
- extended phased apertures;
- added gravitational relays or external cavities;
- reactive near-field exchange;
- active gain, pumping, inversion, or externally powered feedback;
- relativistic, nonlinear, higher-multipole-dominated, or strong-field regimes.

The theorem does not establish that omitted high-frequency tails are negligible for a particular material. A full-device application needs an explicit tail estimate or justified retained model.

## 6. Historical / novelty boundary

Most ingredients are historical. Do not claim novelty for

- gravitational-antenna eigenmode theory or integrated resonant-mass response;
- arbitrary-body multimode GW response or gravitational material-response sum rules;
- generic passive `H2`, source--receiver wave-channel bounds, directivity, or multiple scattering;
- Fano/Bode broadband matching or Chu--Harrington antenna gain--bandwidth/size limits;
- gravity as a communication mediator;
- Newtonian gravity communication/noise bounds or LOCC simulation bounds;
- state-transfer benchmarks between gravitationally interacting oscillators;
- narrowband gravity-induced optomechanical communication channels;
- the `20/3` or `4/3` intermediate lemmas as standalone results.

The only plausible publication contribution is the **complete gravity-specific passive far-zone two-ended inertia closure**: the selected-port passive cut is closed on both sides by the gravitational endpoint trace-to-`I_2` resource and compact TT propagation. Historical and recent-literature collision audits found no exact equivalent theorem in the inspected primary literature; that negative result is not proof of priority.

Do not use `first`, `new`, `unique`, `unprecedented`, or equivalent priority language.

## 7. Validation state

The original frozen science/manuscript SHA `1ce596493073dbb49e6eb71f1a6df0566ff3c25b` passed all six physics workflows plus the manuscript workflow. Subsequent reviewer-driven submission revisions require their own exact-head validation cycle before being treated as current submission state.

The finite-distance TT extension is checked by the existing TT workflow through the augmented `verify_tt_propagation_bound.py` regression.

## 8. Experiment 01 boundary

`../01-causal-quantum-branch-information/` remains the frozen V7 publication project. Do not alter its physics merely to align it with Experiment 02, and do not mention its internal experiment name in the Experiment 02 submission manuscript.

## 9. Current research mode — HARD STOP

Do **not** add another theorem extension merely because one is imaginable.

Allowed work:

- submission metadata/editorial preparation;
- external specialist/journal review;
- response to a concrete external objection;
- reopening only a proof or literature layer implicated by a concrete new contradiction.

Absent one of those triggers, preserve the validated core science.
