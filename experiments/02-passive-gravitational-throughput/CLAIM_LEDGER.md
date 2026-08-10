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

## Canonical final validation

The authoritative frozen science/manuscript SHA is

```text
d05a1e5d5f2f8b4c352f058de73194519c1015e1
```

All seven gates passed on that exact SHA:

```text
passive cut        run 31429984820 — PASS
endpoint resource  run 31429984888 — PASS
TT propagation     run 31429984826 — PASS
combined bound     run 31429984854 — PASS
infinite modal     run 31429984786 — PASS
recurrence         run 31429984808 — PASS
manuscript         run 31429984776, job 93590769191 — PASS
```

The manuscript compiled to 10 pages with no unresolved references/citations.

Final artifact:

```text
name: experiment02-manuscript-v1
artifact ID: 9078731235
SHA256: 370c852f7a65305ffe5dbdb6a5ce5fcf61d5e620668a6a0c90b0baa63ad9d917
head SHA: d05a1e5d5f2f8b4c352f058de73194519c1015e1
```

Earlier layer-by-layer and scope-hardening validation remains preserved in git history and the audit files. The canonical final freeze is summarized in `INTERNAL_FREEZE_CHECKPOINT_2026-08-10.md`.

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

Active/frozen science source: `manuscript_v1/` at the SHA above.

Read:

- `INTERNAL_FREEZE_CHECKPOINT_2026-08-10.md`
- `MANUSCRIPT_V1_ADVERSARIAL_AUDIT_2026-08-10.md`
- `MANUSCRIPT_V1_FINAL_FREEZE_AUDIT_2026-08-10.md`
- `HOSTILE_PRIOR_ART_COLLISION_AUDIT.md`
- `META_REFEREE_SIGNIFICANCE_AUDIT.md`

Internal verdict:

> **INTERNAL AI REVIEW: GO — THEORY/MANUSCRIPT SCIENCE FROZEN.**

Further technical changes require a concrete new contradiction or external specialist/journal objection.

## Priority discipline

Do not use `first`, `new`, `unique`, `unprecedented`, or equivalent priority wording for the complete closure. The strongest accurate statement is:

> no exact equivalent theorem was found in the inspected primary literature.
