# Claim Ledger — Experiment 02

This ledger is authoritative for Experiment 02. Conversation history is a source of hypotheses, never proof.

## Status labels

- `ESTABLISHED WITHIN MODEL` — derived and independently checked within explicit assumptions.
- `FAILED AS A CURRENT CLAIM` — contradicted or outside the established scope.
- `FAILED AS A NOVELTY CLAIM` — useful result/lemma, but not safe to present as an independent novelty contribution.
- `HISTORICAL / PRIOR ART` — established ingredient; not a novelty claim.
- `OPEN — NO EXACT COLLISION FOUND` — candidate contribution after hostile search; negative search is not proof of priority.

## Current ledger

| Statement | Status | Evidence |
|---|---|---|
| Complex-envelope `H2` spectral-area metric for stable strictly proper selected cross-port blocks | ESTABLISHED WITHIN MODEL | `PASSIVE_SELECTED_PORT_CUT_DERIVATION.md` |
| Passive selected-port cut by endpoint port traces | ESTABLISHED WITHIN MODEL | Stage-A derivation + CI |
| Separated passive cut by source/receiver gravitational traces | ESTABLISHED WITHIN MODEL | Stage-A derivation + random two-ended adversary |
| Band-limited `Gamma_coh` is bounded by the corresponding full-line selected-port `H2` norm | ESTABLISHED WITHIN MODEL | positivity of `Tr(T^dag T)`; made explicit in `manuscript_v1/sections/02_passive_cut.tex` |
| `sum_n (q_n:q_n)/mu_n <= (20/3) I_2` | ESTABLISHED WITHIN MODEL | Stage-B derivation + CI |
| `Tr(K_g^dag K_g) <= (4G/3c^5) I_2 Omega^4` for a retained modal sector with `omega_n <= Omega` | ESTABLISHED WITHIN MODEL | Stage-B derivation + CI |
| Carrier replacement `Omega^4 -> omega_0^4` for `Omega=omega_0[1+O(B/omega_0)]` | ESTABLISHED WITHIN MODEL | `NARROWBAND_NORMALIZATION_AUDIT.md`; applies only to the retained carrier-scale sector |
| Passive unitary internal mode mixing cannot increase gravitational coupling trace | ESTABLISHED WITHIN MODEL | trace invariance + Stage-B CI |
| Leading compact TT propagation coefficient `limsup (kR)^2 ||P_g||_op^2 <= 25/16` | ESTABLISHED WITHIN MODEL | Stage-C derivation + CI; V7 used only as post-derivation cross-check |
| Narrowband two-ended inertia bound `Gamma_coh lesssim [25 G omega_0^2/(12 c^3 R^2)] min(I_2A,I_2B)` for the retained carrier-scale bounded-port modal sector | ESTABLISHED WITHIN MODEL | assembled proof + combined CI |
| Countably infinite separable **bounded-port Markov** modal sectors obey the same passive cut | ESTABLISHED WITHIN MODEL | operator proof + infinite-modal CI |
| Same-two-endpoint passive recurrence leaves the retained leading `1/R^2` upper-bound coefficient unchanged | ESTABLISHED WITHIN MODEL | resolvent proof + recurrence CI |
| The compact/wave-zone theorem applies without `k_0 a_A,k_0 a_B << 1` and `k_0 R >> 1` | FAILED AS A CURRENT CLAIM | compact quadrupole and separated stationary-phase derivations require these asymptotic conditions |
| Higher-frequency endpoint modes `omega_n >> omega_0` are automatically controlled by the simple carrier-scale `omega_0^4` resource because the measured envelope is narrow | FAILED AS A CURRENT CLAIM | their gravitational rates scale with their own `omega_n^4`; off-resonant sectors require exclusion from the effective model or a separate bound |
| Same simple theorem over arbitrary broad absolute frequency | FAILED AS A CURRENT CLAIM | `NARROWBAND_NORMALIZATION_AUDIT.md` |
| Arbitrary unbounded PDE boundary-control/observation ports are covered | FAILED AS A CURRENT CLAIM | admissibility/domain analysis not supplied |
| Genuinely non-Markov continua are covered | FAILED AS A CURRENT CLAIM | outside declared model |
| Added relays, external mirrors/cavities, near-field exchange, or active feedback are covered by the recurrence proof | FAILED AS A CURRENT CLAIM | these change the propagation architecture |
| Eigenmode gravitational-antenna emission/reception/directivity theory is new here | HISTORICAL / PRIOR ART | Hirakawa–Narihara–Fujimoto 1976 |
| Resonant-mass gravitational absorption/integrated response is new here | HISTORICAL / PRIOR ART | Paik–Wagoner 1976; Aguiar review |
| The idea that adding a resonant transducer/two normal modes leaves a finite integrated gravitational cross-section resource is new here | HISTORICAL / PRIOR ART | Aguiar review of Paik–Wagoner lineage |
| General arbitrary-elastic-body multimode GW response is new here | HISTORICAL / PRIOR ART | Lobo 1995 |
| Gravitational material-response sum-rule methodology is new here | HISTORICAL / PRIOR ART | Srivastava–Widom–Pizzella 2003 |
| Complete generator–receiver/Hertz gravitational calculations are new here | HISTORICAL / PRIOR ART | Grishchuk–Sazhin 1975; Rudenko 2003 |
| Generic source–receiver orthogonal-channel/coupling-limit mathematics is new here | HISTORICAL / PRIOR ART | Miller 2000 |
| Generic two-body response-plus-propagation bound architecture is new here | HISTORICAL / PRIOR ART | Molesky–Venkataram–Jin–Rodriguez 2020 |
| Infinite-dimensional `H2`/operator-Gramian machinery is new here | HISTORICAL / PRIOR ART | Baras–Brockett 1975; Opmeer–Reis–Wollner 2013 |
| Multiple-scattering / scattering-transfer composition is new here | HISTORICAL / PRIOR ART | Redheffer 1962 |
| The `20/3` Bessel coefficient should be presented as a standalone novelty | FAILED AS A NOVELTY CLAIM | short consequence of historical STF/modal framework + standard Bessel/Parseval |
| The `4/3` cumulative endpoint resource should be presented as a standalone novelty | FAILED AS A NOVELTY CLAIM | integrated resonant-mass response and material sum-rule precedents make standalone novelty too weak |
| The complete gravity-specific two-ended inertia closure is an exact known theorem | OPEN — NO EXACT COLLISION FOUND | `HOSTILE_PRIOR_ART_COLLISION_AUDIT.md`; strong near-collisions found, no inspected source states the complete closure |
| Priority of the complete closure is proved | FAILED AS A CURRENT CLAIM | a negative literature search is not proof of priority |
| Earlier conversation-only Experiment-02 branches/CI/manuscript are repository evidence | FAILED AS A CURRENT CLAIM | only real `main` commits/runs count |

## Real validation record before manuscript scope hardening

```text
Stage A passive cut:
  run 31391304791, job 93463450929 — PASS

Stage B endpoint resource:
  run 31392339989, job 93466817164 — PASS

Stage C TT propagation:
  run 31393020114, job 93469060678 — PASS

Combined finite-dimensional theorem:
  commit 8fc8da7cf5d51e3a56d7e0b15434407c7e493ecb
  run 31393498572, job 93470648716 — PASS

Countably infinite bounded-port extension:
  commit 91566b4ccfb1488b54a403a79452b9dc67347181
  run 31394415776, job 93473679179 — PASS

Passive same-endpoint recurrence:
  commit e040fcaf2f6023fafd02bef1f11846d0a9236d0e
  run 31394879241, job 93475219560 — PASS

Current pre-hardening manuscript head:
  commit 87732887b9139f286e025e470810cdf207706116
  manuscript run 31397765390 — PASS
  combined-bound run 31397765584 — PASS
  infinite-modal run 31397765773 — PASS
  recurrence run 31397765372 — PASS
```

The manuscript scope-hardening checkpoint must receive fresh CI before it is treated as frozen.

## Canonical literature boundary

Read `HOSTILE_PRIOR_ART_COLLISION_AUDIT.md` before making novelty claims. The only plausible publication contribution is the **complete gravity-specific two-ended inertia closure**, not any individual ingredient.

## Frequency and geometry convention

```text
omega_0   absolute gravitational carrier angular frequency
nu        complex-envelope detuning
B         envelope bandwidth, B/omega_0 << 1
k_0       omega_0/c
a_A,a_B   characteristic endpoint radii, k_0 a_A,k_0 a_B << 1
R         endpoint separation, k_0 R >> 1
Omega     upper physical frequency of retained endpoint modal sector,
          Omega=omega_0[1+O(B/omega_0)]
Gamma_coh (1/2pi) integral over nu of Tr[T^dag T]
I_2       int rho r^2 dV about endpoint COM
```

## Manuscript status

`manuscript_v1/` is the active short specialist manuscript. The first adversarial manuscript-scope audit is `MANUSCRIPT_V1_ADVERSARIAL_AUDIT_2026-08-10.md`.

## Priority discipline

Do not use `first`, `new`, `unique`, `unprecedented`, or equivalent priority wording for the complete closure. The strongest accurate statement is:

> no exact equivalent theorem was found in the inspected primary literature.
