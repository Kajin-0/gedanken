# Claim Ledger — Experiment 02

This ledger is authoritative for the research status of Experiment 02. A statement is not a project result merely because it appears in `HYPOTHESES.md` or in conversation history.

## Status labels

- `QUESTION` — research target, no truth value assigned.
- `PROVISIONAL` — plausible candidate under investigation.
- `DERIVED / VALIDATION PENDING` — an explicit repository derivation exists, but the required independent validation gate is not yet complete.
- `ESTABLISHED WITHIN MODEL` — derived and independently checked within explicit assumptions.
- `FAILED` — contradicted or overstrong.
- `HISTORICAL / PRIOR ART` — established elsewhere; not a novelty claim.
- `OPEN` — unresolved boundary or extension.

## Current ledger

| Statement | Status | Evidence |
|---|---|---|
| A two-sided `H2` spectral-area metric is mathematically well defined for stable strictly proper selected cross-port blocks | ESTABLISHED WITHIN MODEL | Plancherel/Gramian identity re-derived in `PASSIVE_SELECTED_PORT_CUT_DERIVATION.md` |
| Finite-dimensional passive selected-port transfer obeys `||H_{o<-i}||_2^2 <= min[Tr(K_i^dag K_i), Tr(K_o^dag K_o)]` | ESTABLISHED WITHIN MODEL | derivation + GitHub Actions run `31391304791`, job `93463450929`, PASS |
| A separated two-ended passive link obeys `Gamma_coh <= eta_max min[Tr(K_gA^dag K_gA), Tr(K_gB^dag K_gB)]` under the Stage-A realization assumptions | ESTABLISHED WITHIN MODEL | derivation + end-to-end random-system regression in run `31391304791`, PASS |
| The modal quadrupole strength obeys `sum_n (q_n:q_n)/mu_n <= (20/3) I_2`, with `I_2=int rho r^2 dV` | DERIVED / VALIDATION PENDING | `GRAVITATIONAL_ENDPOINT_RESOURCE_DERIVATION.md`; Stage-B regression added |
| A retained modal sector with `omega_n <= Omega` obeys `sum_n kappa_g,n <= (4G/3c^5) I_2 Omega^4` | DERIVED / VALIDATION PENDING | independent quadrupole-power derivation in `GRAVITATIONAL_ENDPOINT_RESOURCE_DERIVATION.md`; CI pending |
| In an energy-normalized finite-dimensional Markov gravitational port model, `Tr(K_g^dag K_g)=sum_n kappa_g,n` | DERIVED / VALIDATION PENDING | normalization argument in Stage-B derivation; still needs broader independent audit |
| Compact quadrupolar endpoint coupling has an inertia-only cumulative bound | DERIVED / VALIDATION PENDING | Stage B; coefficient independently re-emerged as `4/3` |
| The relevant compact TT propagation coefficient is `25/16` for the Experiment-02 throughput normalization | PROVISIONAL | candidate H3; must be independently normalized for this metric |
| The final two-ended coefficient is `25/12` | PROVISIONAL | candidate H4 only; must not be inferred until Stage C |
| Passive internal mode mixing cannot increase total gravitational oscillator strength | DERIVED / VALIDATION PENDING | trace/basis-invariance argument in Stage B; regression pending |
| Repeated passive returns cannot increase the leading `1/R^2` upper-bound coefficient | PROVISIONAL | candidate H6 only |
| Countably infinite bounded-port modal sectors obey the same cut | OPEN | requires operator-domain/admissibility analysis |
| Arbitrary unbounded PDE boundary ports are covered | FAILED AS A CURRENT CLAIM | explicitly outside initial assumptions |
| Eigenmode gravitational-antenna emission/reception theory is new here | HISTORICAL / PRIOR ART | Hirakawa–Narihara–Fujimoto 1976 |
| General arbitrary-elastic-body multimode GW response is new here | HISTORICAL / PRIOR ART | Lobo 1995 / arXiv:gr-qc/0006102 |
| The `20/3` or `4/3` cumulative coefficient is novel | OPEN | detailed historical collision search incomplete; do not claim |
| The complete inertia-only two-ended theorem is novel | OPEN | no trustworthy complete prior-art audit yet |
| Previous conversational Experiment 02 CI/branch/manuscript claims are repository evidence | FAILED | real remote did not contain those artifacts |

## Stage-A validation record

Workflow:

`.github/workflows/experiment02-passive-cut.yml`

Canonical first run on `main`:

```text
run: 31391304791
job: 93463450929
PASS
```

Adversarial sample outputs:

```text
worst endpoint H2/resource ratio = 0.410127000961
largest full-scattering singular value = 1
worst two-ended Gamma/bound ratio = 0.089763188389
PASS: finite-dimensional passive selected-port cut
```

## Stage-B evidence currently pending CI

Files:

- `GRAVITATIONAL_ENDPOINT_RESOURCE_DERIVATION.md`
- `STAGE_B_PRIOR_ART_BOUNDARY.md`
- `numerics/verify_gravitational_endpoint_resource.py`
- `.github/workflows/experiment02-endpoint-resource.yml`

The Stage-B derivation independently recovers the inherited `4/3` coefficient but it remains `DERIVED / VALIDATION PENDING` until the actual GitHub Actions result is recorded.

## Prior-art boundary

The generic Stage-A passivity machinery is established systems theory. The Stage-B elastic/GW modal ingredients are also substantially historical. Primary anchors currently checked:

- M. Guta and N. Yamamoto, *System identification for passive linear quantum systems*, arXiv:1303.3771.
- J. E. Gough and G. Zhang, *On Realization Theory of Quantum Linear Systems*, arXiv:1311.1375.
- H. Hirakawa, K. Narihara, and M.-K. Fujimoto, *Theory of Antennas for Gravitational Radiation*, JPSJ 41, 1093 (1976), DOI `10.1143/JPSJ.41.1093`.
- J. Alberto Lobo, *What can we learn about gravitational wave physics with an elastic spherical antenna?*, Phys. Rev. D 52, 591 (1995), arXiv:`gr-qc/0006102`.

No priority language is permitted for the cumulative coefficients or later two-ended closure until the detailed collision search is complete.

## Promotion discipline

Before changing a gravity-specific row to `ESTABLISHED WITHIN MODEL`, record:

1. the exact derivation file;
2. the assumptions used;
3. an independent check or normalization route;
4. counterexample attempts and their scope;
5. primary-source comparison;
6. numerical evidence where relevant.

## Priority language

Do not use `first`, `new`, `unique`, `unprecedented`, or equivalent priority wording unless a dedicated primary-source audit supports it. A negative search result is not proof of priority.
