# Claim Ledger — Experiment 02

This ledger is authoritative for the current Experiment 02 theorem. Conversation history is hypothesis-generation, not proof.

## Status labels

- `ESTABLISHED WITHIN MODEL` — derived and independently checked under explicit assumptions.
- `FAILED AS A CURRENT CLAIM` — contradicted or outside established scope.
- `FAILED AS A NOVELTY CLAIM` — valid ingredient, unsafe as an independent novelty claim.
- `HISTORICAL / PRIOR ART` — established ingredient.
- `OPEN — NO EXACT COLLISION FOUND` — candidate contribution after targeted search; not proof of priority.

## Current ledger

| Statement | Status | Evidence |
|---|---|---|
| Stable strictly proper passive selected cross-port blocks obey the `H2` Gramian cut | ESTABLISHED WITHIN MODEL | submission passive-cut derivation + passive-cut regression |
| The weighted passive Gramian inequality `int ||L(i nu I-A)^-1 K_i^dag||_HS^2/(2pi) <= Tr(L^dag L)` holds for bounded `L` | ESTABLISHED WITHIN MODEL | `submission_prd/sections/02_passive_cut.tex` |
| `Gamma_coh` is the band-limited coherent-transfer spectral area and is not capacity/bit rate | ESTABLISHED WITHIN MODEL | definition + dimensional check |
| Scalar completeness `sum (q:q)/mu <= (20/3) I_2` | ESTABLISHED WITHIN MODEL | endpoint derivation + regression |
| Sector completeness `sum Q_2^2/mu <= 4 I_Rhat` | ESTABLISHED WITHIN MODEL | sector Parseval/Bessel derivation + endpoint regression |
| Sector completeness `sum Q_1^2/mu <= 2 I_Rhat + 4 Z_Rhat` | ESTABLISHED WITHIN MODEL | same |
| Sector completeness `sum Q_0^2/mu <= (2/3)I_Rhat + (8/3)Z_Rhat` | ESTABLISHED WITHIN MODEL | same |
| The three sector resources sum exactly to `(20/3) I_2` | ESTABLISHED WITHIN MODEL | algebra + regression |
| For a complete displacement basis, the unweighted sector projection sums are Parseval equalities | ESTABLISHED WITHIN MODEL | Hilbert-space completeness |
| On-shell modal gravitational linewidth is `G omega_n^4(q:q)/(5 c^5 mu)` | ESTABLISHED WITHIN MODEL | quadrupole power / mode-energy derivation |
| For retained `omega_n <= Omega`, each sector fourth-frequency moment is bounded by `Omega^4` times its sector resource | ESTABLISHED WITHIN MODEL | monotonic frequency ceiling + sector completeness |
| Completeness alone bounds an unrestricted fourth modal-frequency moment | FAILED AS A CURRENT CLAIM | square-summable projection sequence can have divergent fourth frequency moment |
| A far-detuned mode may be assigned its on-shell `omega_n^4` linewidth unchanged at a low drive frequency | FAILED AS A CURRENT CLAIM | on-shell linewidth is outside validity of that far-detuned Markov substitution |
| Exact outgoing compact-TT sector powers are `eta_2,eta_1,eta_0` given in the submission derivation | ESTABLISHED WITHIN MODEL | exact angular integrals + TT regression |
| For `z>=3`, `eta_2 >= eta_1,eta_0` | ESTABLISHED WITHIN MODEL | direct subtraction + regression |
| Propagation variation across the measured band can be retained through `sup_band eta_m(omega R/c)` rather than freezing at `omega_0` | ESTABLISHED WITHIN MODEL | finite-band theorem derivation |
| Finite-band sector-resolved bound `Gamma_coh <= [G Omega^4/(5c^5)] min(G_A,G_B)` | ESTABLISHED WITHIN MODEL | weighted cut + sector resource + exact TT propagation + combined regression |
| Far-zone theorem `limsup R^2 Gamma_coh <= [5G Omega^4/(4c^3 omega_-^2)] min(I_Rhat,A,I_Rhat,B)` | ESTABLISHED WITHIN MODEL | asymptotic sector hierarchy + combined regression |
| Carrier-scale form `Gamma_coh lesssim [5G omega_0^2/(4c^3R^2)] min(I_Rhat,A,I_Rhat,B)` | ESTABLISHED WITHIN MODEL | narrowband reduction of rigorous theorem |
| Former `25/12 * min(I_2A,I_2B)` expression is the strongest current closure | FAILED AS A CURRENT CLAIM | superseded by sector-resolved `5/4 * I_Rhat` closure |
| The `5/4` chained coefficient is sharp at the abstract retained projection-sum level | ESTABLISHED WITHIN MODEL | sector Parseval equality + `|m|=2` propagation saturation |
| A generic homogeneous elastic body necessarily realizes simultaneous `5/4` saturation | FAILED AS A CURRENT CLAIM | no constitutive realizability proof |
| Ideal slender bar fundamental occupies `48/pi^4 ~= 0.493` of the leading `|m|=2` resource in its maximum-radiation direction | ESTABLISHED WITHIN MODEL | analytic bar check |
| Countably infinite separable bounded-port Markov sectors obey the same weighted passive cut when the retained gravitational port is Hilbert--Schmidt | ESTABLISHED WITHIN MODEL | operator extension + infinite-modal regression |
| Same-two-endpoint passive recurrence changes the leading `R^-2` coefficient | FAILED AS A CURRENT CLAIM | exact resolvent + propagation round-trip scaling |
| Unbounded PDE boundary ports are automatically covered | FAILED AS A CURRENT CLAIM | admissibility/domain proof required |
| Genuinely non-Markov continua are covered | FAILED AS A CURRENT CLAIM | outside declared model |
| Added relays, external cavities, extended phased apertures, near-field exchange, or active feedback are covered | FAILED AS A CURRENT CLAIM | different architecture/physical class |
| Generic passive `H2`, Fano/Bode matching, Chu--Harrington limits, resonant-mass GW theory, material-response sum rules, directivity, and multiple scattering are new here | HISTORICAL / PRIOR ART | cited literature |
| The gravity-specific two-ended sector-resolved endpoint-resource + compact-TT closure is an exact known theorem | OPEN — NO EXACT COLLISION FOUND | targeted historical/recent collision audits; no exact inspected match |
| Priority is proved | FAILED AS A CURRENT CLAIM | negative search is not proof of priority |

## Authoritative validated science checkpoint

```text
science/manuscript SHA: 3bf26c7535919597d711fdcd781e6098b76b5d68
```

Exact-head gates:

```text
passive cut        run 31452652657 — PASS
endpoint resource  run 31452652672 — PASS
TT propagation     run 31452652787 — PASS
combined bound     run 31452652636 — PASS
infinite modal     run 31452652694 — PASS
recurrence         run 31452652697 — PASS
PRD manuscript     run 31452652653 — PASS
```

Compiled artifact from that science SHA:

```text
artifact: experiment02-prd-submission
artifact ID: 9086872919
ZIP size: 352219 bytes
SHA256: 675e6d67baaf6538f34602f0d3a48c81b3dccb07fe4fabd1caf0076db2945738
```

## Canonical conventions

```text
omega(nu) physical frequency omega_0+nu
omega_-   minimum physical frequency in measured band
Omega     upper retained modal frequency
Rhat      source-receiver direction
I_Rhat    int rho [r^2-(Rhat.x)^2] d^3x
Z_Rhat    int rho (Rhat.x)^2 d^3x
I_2       I_Rhat+Z_Rhat
Gamma_coh (1/2pi) integral over nu of Tr[T^dag T]
```

## Priority discipline

Do not use `first`, `new`, `unique`, `unprecedented`, or equivalent priority wording for the closure. The strongest defensible literature statement is that no exact equivalent was found in the inspected sources.
