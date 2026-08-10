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
| Passive selected-port transfer is cut by endpoint port traces | ESTABLISHED WITHIN MODEL | Stage-A derivation + CI |
| Band-limited `Gamma_coh` is bounded by the corresponding full-line selected-port `H2` norm | ESTABLISHED WITHIN MODEL | positivity of `Tr(T^dag T)`; explicit in manuscript passive-cut section |
| Separated passive transfer is cut by the smaller source/receiver gravitational trace | ESTABLISHED WITHIN MODEL | Stage-A derivation + random two-ended adversary |
| `sum_n (q_n:q_n)/mu_n <= (20/3) I_2` | ESTABLISHED WITHIN MODEL | Stage-B derivation + CI |
| `Tr(K_g^dag K_g) <= (4G/3c^5) I_2 Omega^4` for `omega_n <= Omega` | ESTABLISHED WITHIN MODEL | Stage-B derivation + CI |
| Carrier replacement `Omega^4 -> omega_0^4` for `Omega=omega_0[1+O(B/omega_0)]` | ESTABLISHED WITHIN MODEL | `NARROWBAND_NORMALIZATION_AUDIT.md`; retained carrier-scale sector only |
| Passive unitary internal mode mixing cannot increase gravitational coupling trace | ESTABLISHED WITHIN MODEL | trace invariance + Stage-B CI |
| Compact TT propagation obeys `limsup (kR)^2 ||P_g||_op^2 <= 25/16` | ESTABLISHED WITHIN MODEL | Stage-C derivation + CI |
| Narrowband two-ended bound `Gamma_coh lesssim [25 G omega_0^2/(12 c^3 R^2)] min(I_2A,I_2B)` | ESTABLISHED WITHIN MODEL | assembled proof + combined CI |
| Countably infinite separable bounded-port Markov modal sectors obey the same passive cut | ESTABLISHED WITHIN MODEL | operator proof + infinite-modal CI |
| Same-two-endpoint passive recurrence leaves the leading `1/R^2` upper coefficient unchanged | ESTABLISHED WITHIN MODEL | resolvent proof + recurrence CI |
| The theorem applies without `k_0a_A,k_0a_B << 1` and `k_0R >> 1` | FAILED AS A CURRENT CLAIM | compact TT/stationary-phase derivation requires these conditions |
| Uncontrolled endpoint modes `omega_n >> omega_0` are automatically bounded by the carrier-scale `omega_0^4` resource | FAILED AS A CURRENT CLAIM | gravitational rates scale with their own `omega_n^4`; off-resonant sectors require separate control |
| Same simple theorem over arbitrary broad absolute frequency | FAILED AS A CURRENT CLAIM | `NARROWBAND_NORMALIZATION_AUDIT.md` |
| Arbitrary unbounded PDE boundary ports are covered | FAILED AS A CURRENT CLAIM | separate admissibility/domain proof required |
| Genuinely non-Markov continua are covered | FAILED AS A CURRENT CLAIM | outside declared model |
| Added relays/external cavities/extended apertures/near-field exchange/active feedback are covered by the recurrence proof | FAILED AS A CURRENT CLAIM | those change the propagation architecture or passive class |
| Eigenmode gravitational-antenna emission/reception/directivity theory is new here | HISTORICAL / PRIOR ART | Hirakawa--Narihara--Fujimoto 1976 |
| Resonant-mass absorption/integrated response is new here | HISTORICAL / PRIOR ART | Paik--Wagoner 1976; Aguiar 2011 review |
| General arbitrary-elastic-body multimode GW response is new here | HISTORICAL / PRIOR ART | Lobo 1995 |
| Gravitational material-response sum-rule methodology is new here | HISTORICAL / PRIOR ART | Srivastava--Widom--Pizzella 2003 |
| Complete generator--receiver/Hertz calculations are new here | HISTORICAL / PRIOR ART | Grishchuk--Sazhin lineage; Rudenko 2003 |
| Generic source--receiver channel/coupling-limit mathematics is new here | HISTORICAL / PRIOR ART | Miller 2000 |
| Generic two-body response-plus-propagation bound architecture is new here | HISTORICAL / PRIOR ART | Molesky et al. 2020 |
| Infinite-dimensional `H2`/operator-Gramian machinery is new here | HISTORICAL / PRIOR ART | Baras--Brockett 1975; Opmeer--Reis--Wollner 2013 |
| Multiple-scattering composition is new here | HISTORICAL / PRIOR ART | Redheffer 1962 |
| `20/3` or `4/3` should be presented as standalone novelty | FAILED AS A NOVELTY CLAIM | short closure of historical modal/sum-rule ingredients |
| The complete gravity-specific two-ended inertia closure is an exact known theorem | OPEN — NO EXACT COLLISION FOUND | `HOSTILE_PRIOR_ART_COLLISION_AUDIT.md`; strong near-collisions, no exact inspected match |
| Priority of the complete closure is proved | FAILED AS A CURRENT CLAIM | negative literature search is not proof of priority |
| Conversation-only branches/commits/CI are repository evidence | FAILED AS A CURRENT CLAIM | only verified real remote artifacts count |

## Validation record

Original layer-by-layer passes:

```text
Stage A passive cut:
  run 31391304791, job 93463450929 — PASS
Stage B endpoint resource:
  run 31392339989, job 93466817164 — PASS
Stage C TT propagation:
  run 31393020114, job 93469060678 — PASS
Combined finite-dimensional theorem:
  run 31393498572, job 93470648716 — PASS
Countably infinite bounded-port extension:
  run 31394415776, job 93473679179 — PASS
Passive same-endpoint recurrence:
  run 31394879241, job 93475219560 — PASS
```

Scope-hardened manuscript/theorem head:

```text
commit 3cfb62e31dfb0905955050f963bdc2bf93706c9e
passive cut        run 31429039197 — PASS
endpoint resource  run 31429039518 — PASS
TT propagation     run 31429039529 — PASS
combined bound     run 31429039256 — PASS
infinite modal     run 31429039819 — PASS
recurrence         run 31429039531 — PASS
manuscript         run 31429039874, job 93587616997 — PASS
```

Manuscript output on that head: 10 pages, no unresolved references/citations. Artifact ID `9078372416`; ZIP SHA256 `9dac950d7f9136aaa8608e82eed819ed23544f5ce50cd9b927357540f8c39026`.

The final bibliography/wording polish commit containing `MANUSCRIPT_V1_FINAL_FREEZE_AUDIT_2026-08-10.md` must receive fresh exact-head CI before the canonical freeze is recorded.

## Frequency and geometry convention

```text
omega_0   absolute gravitational carrier angular frequency
nu        complex-envelope detuning
B         envelope bandwidth, B/omega_0 << 1
k_0       omega_0/c
a_A,a_B   endpoint radii, k_0 a_A,k_0 a_B << 1
R         separation, k_0 R >> 1
Omega     upper physical frequency of retained modal sector,
          Omega=omega_0[1+O(B/omega_0)]
Gamma_coh (1/2pi) integral over nu of Tr[T^dag T]
I_2       int rho r^2 dV about endpoint COM
```

## Manuscript and audit status

Active source: `manuscript_v1/`.

Read:

- `MANUSCRIPT_V1_ADVERSARIAL_AUDIT_2026-08-10.md`
- `MANUSCRIPT_V1_FINAL_FREEZE_AUDIT_2026-08-10.md`
- `HOSTILE_PRIOR_ART_COLLISION_AUDIT.md`
- `META_REFEREE_SIGNIFICANCE_AUDIT.md`

The final audit found no new physics failure. It corrected bibliography metadata and minor wording only; fresh CI remains the final internal gate.

## Priority discipline

Do not use `first`, `new`, `unique`, `unprecedented`, or equivalent priority wording for the complete closure. The strongest accurate statement is:

> no exact equivalent theorem was found in the inspected primary literature.
