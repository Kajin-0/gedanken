# AGENTS.md — Experiment 02 Recovery and Research Protocol

**Experiment:** `02-passive-gravitational-throughput`  
**Mode:** theorem hardened; short-manuscript validation / adversarial freeze.  
**Current theorem status:** established within the declared compact retained-sector bounded-port narrowband model.  
**Manuscript status:** `manuscript_v1/` active.

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

## 2. Experiment 01 is frozen

`../01-causal-quantum-branch-information/` is the V7 publication project.

Do not alter its physics while working here unless Experiment 02 uncovers a concrete defect that directly affects V7. Shared formulas may be compared only after Experiment 02 has derived its own normalization independently.

## 3. Current theorem

Use the notation

```text
omega_0   absolute gravitational carrier angular frequency
nu        complex-envelope detuning
B         envelope bandwidth, B/omega_0 << 1
k_0       omega_0/c
a_A,a_B   endpoint radii, k_0 a_A,k_0 a_B << 1
R         separation, k_0 R >> 1
Omega     upper frequency of retained endpoint modal sector,
          Omega=omega_0[1+O(B/omega_0)]
I_2       int rho r^2 dV about endpoint COM
```

The established in-model statement is

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega_0^2}{12c^3R^2}
\min(I_{2,A},I_{2,B})
}
```

for finite or countably infinite **bounded-port Markov** modal sectors satisfying the retained carrier-scale frequency assumption.

This is a complex-envelope spectral-area theorem, not a capacity theorem.

## 4. Load-bearing proof files

Read in this order:

1. `PASSIVE_SELECTED_PORT_CUT_DERIVATION.md`
2. `GRAVITATIONAL_ENDPOINT_RESOURCE_DERIVATION.md`
3. `TT_PROPAGATION_BOUND_DERIVATION.md`
4. `NARROWBAND_NORMALIZATION_AUDIT.md`
5. `FINITE_TWO_ENDED_INERTIA_BOUND.md`
6. `INFINITE_DIMENSIONAL_BOUNDED_PORT_EXTENSION.md`
7. `PASSIVE_TWO_ENDPOINT_RECURRENCE.md`
8. `HOSTILE_PRIOR_ART_COLLISION_AUDIT.md`
9. `META_REFEREE_SIGNIFICANCE_AUDIT.md`
10. `MANUSCRIPT_V1_ADVERSARIAL_AUDIT_2026-08-10.md`
11. `CLAIM_LEDGER.md`
12. `CURRENT_STATE.md`
13. `manuscript_v1/README.md`

## 5. What the theorem does not cover

Do not silently broaden to

- arbitrary broad absolute-frequency operation with one carrier coefficient;
- higher-frequency endpoint modes far above the carrier whose off-resonant tails are not separately bounded;
- unbounded PDE boundary-control/observation ports;
- genuinely non-Markov continua;
- extended phased apertures;
- added gravitational relays or external cavities;
- reactive near-field exchange;
- active gain, pumping, inversion, or externally powered feedback;
- relativistic, nonlinear, higher-multipole-dominated, or strong-field regimes.

## 6. Historical / novelty boundary

Most ingredients are historical. Do not claim novelty for

- gravitational-antenna eigenmode theory;
- integrated resonant-mass response;
- arbitrary-body multimode GW response;
- gravitational material-response sum rules;
- generic passive `H2` machinery;
- generic source–receiver wave-channel bounds;
- directivity / reciprocal effective area;
- multiple-scattering composition;
- the `20/3` or `4/3` intermediate lemmas as standalone results.

The only plausible publication contribution is the **complete gravity-specific two-ended inertia closure**. No exact equivalent theorem was found in the inspected literature, but that negative result is not proof of priority.

Do not use `first`, `new`, `unique`, `unprecedented`, or equivalent priority language.

## 7. Validation state

Canonical earlier passing gates are recorded in `CURRENT_STATE.md` and `CLAIM_LEDGER.md`.

The active manuscript has its own workflow:

`.github/workflows/latex-experiment02.yml`

and the theorem has dedicated passive-cut, endpoint-resource, TT-propagation, combined-bound, infinite-modal, and recurrence workflows.

After any manuscript/theorem scope edit, require fresh runs on the exact resulting `main` head before declaring the checkpoint frozen.

## 8. Current research mode

The AI-native derivation, hostile attack, prior-art collision, numerical falsification, infinite-modal, recurrence, significance, and first manuscript-scope stages have been completed.

Do **not** add another theorem extension merely because one is imaginable.

Current allowed work is:

1. validate the current scope-hardening edits;
2. final manuscript claim/notation/citation audit;
3. final repository-state synchronization;
4. manuscript compression/editorial polish only if it preserves the theorem;
5. final external specialist/journal review.

If a new concrete technical defect appears, reopen only the affected proof layer and record the correction explicitly.
