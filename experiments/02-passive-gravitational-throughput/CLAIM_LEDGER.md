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
| A two-sided complex-envelope `H2` spectral-area metric is mathematically well defined for stable strictly proper selected cross-port blocks | ESTABLISHED WITHIN MODEL | Plancherel/Gramian identity in `PASSIVE_SELECTED_PORT_CUT_DERIVATION.md` |
| Finite-dimensional passive selected-port transfer obeys `||H_{o<-i}||_2^2 <= min[Tr(K_i^dag K_i), Tr(K_o^dag K_o)]` | ESTABLISHED WITHIN MODEL | derivation + Stage-A CI |
| A separated finite-dimensional passive link obeys `Gamma_coh <= eta_max min[Tr(K_gA^dag K_gA), Tr(K_gB^dag K_gB)]` | ESTABLISHED WITHIN MODEL | Stage-A derivation + end-to-end adversarial regression |
| The modal quadrupole strength obeys `sum_n (q_n:q_n)/mu_n <= (20/3) I_2`, with `I_2=int rho r^2 dV` | ESTABLISHED WITHIN MODEL | `GRAVITATIONAL_ENDPOINT_RESOURCE_DERIVATION.md` + Stage-B CI |
| A retained modal sector with `omega_n <= Omega` obeys `sum_n kappa_g,n <= (4G/3c^5) I_2 Omega^4` | ESTABLISHED WITHIN MODEL | independent quadrupole-power derivation + Stage-B CI |
| In an energy-normalized finite-dimensional Markov gravitational port model, `Tr(K_g^dag K_g)=sum_n kappa_g,n` | ESTABLISHED WITHIN MODEL | energy-linewidth/input-output normalization + trace invariance checks |
| Passive internal unitary modal mixing cannot increase total gravitational coupling trace | ESTABLISHED WITHIN MODEL | trace invariance + Stage-B mixing regression |
| Compact quadrupolar TT propagation obeys the leading wave-zone coefficient `limsup_(kR->infty) (kR)^2 ||P_g||_op^2 <= 25/16` | ESTABLISHED WITHIN MODEL | `TT_PROPAGATION_BOUND_DERIVATION.md` + Stage-C CI + independent V7 cross-check after derivation |
| The finite-dimensional narrowband two-ended bound `Gamma_coh lesssim [25 G omega_0^2/(12 c^3 R^2)] min(I_2A,I_2B)` holds in the declared passive compact wave-zone class | ESTABLISHED WITHIN MODEL | `FINITE_TWO_ENDED_INERTIA_BOUND.md` + combined CI run `31393498572`, job `93470648716`, PASS |
| The same simple coefficient is established over an arbitrary broad absolute-frequency interval | FAILED AS A CURRENT CLAIM | `NARROWBAND_NORMALIZATION_AUDIT.md`; carrier/envelope separation is required |
| Repeated passive returns cannot increase the leading `1/R^2` upper-bound coefficient | PROVISIONAL | next adversarial stage |
| Countably infinite bounded-port modal sectors obey the same passive cut | OPEN | next mathematical stage; requires semigroup/operator proof |
| Arbitrary unbounded PDE boundary ports are covered | FAILED AS A CURRENT CLAIM | explicitly outside initial assumptions |
| Eigenmode gravitational-antenna emission/reception theory is new here | HISTORICAL / PRIOR ART | Hirakawa–Narihara–Fujimoto 1976 |
| General arbitrary-elastic-body multimode GW response is new here | HISTORICAL / PRIOR ART | Lobo 1995 / arXiv:gr-qc/0006102 |
| The `20/3` or `4/3` cumulative coefficient is novel | OPEN | detailed historical collision search incomplete; do not claim |
| The complete inertia-only two-ended theorem is novel | OPEN | complete historical/prior-art audit not yet done |
| Previous conversational Experiment 02 CI/branch/manuscript claims are repository evidence | FAILED | the earlier remote state did not exist; only the real commits/runs below count |

## Stage-A validation

```text
workflow: .github/workflows/experiment02-passive-cut.yml
first canonical run: 31391304791
job: 93463450929
result: PASS
```

On the assembled theorem commit `8fc8da7cf5d51e3a56d7e0b15434407c7e493ecb`, Stage A reran as run `31393498735` and passed.

Representative first-run output:

```text
worst endpoint H2/resource ratio = 0.410127000961
largest full-scattering singular value = 1
worst two-ended Gamma/bound ratio = 0.089763188389
```

## Stage-B validation

```text
workflow: .github/workflows/experiment02-endpoint-resource.yml
first canonical run: 31392339989
job: 93466817164
result: PASS
```

Representative output:

```text
worst 20/3 tensor absolute error = 2.84217094304e-14
worst truncated Bessel ratio = 1
worst full-basis Parseval absolute error = 1.70530256582e-13
worst modal-mixing invariance absolute error = 5.68434188608e-14
worst cumulative linewidth/(4 I2/3) ratio = 0.381072504534
```

Stage B also reran successfully on the assembled theorem commit.

## Stage-C validation

```text
workflow: .github/workflows/experiment02-tt-propagation.yml
first canonical run: 31393020114
job: 93469060678
result: PASS
```

Output:

```text
worst TT projector relative excess over q:q = 0
worst 8pi/5 sphere-normalization relative error = 3.73465396589e-15
largest random directivity = 2.46390574729
largest random stationary-phase amplitude prefactor = 0.895467559969
aligned directivity saturation = 2.5
aligned amplitude prefactor = 1.25
aligned power prefactor = 1.5625
PASS: compact TT propagation 25/16 bound
```

The Stage-C derivation was corrected before final assembly to make only a leading-wave-zone limsup claim for arbitrary complex quadrupoles. It does not import the aligned plus-mode even-power finite-distance correction as a universal subleading statement.

## Combined finite-dimensional narrowband validation

```text
workflow: .github/workflows/experiment02-combined-bound.yml
commit:   8fc8da7cf5d51e3a56d7e0b15434407c7e493ecb
run:      31393498572
job:      93470648716
result:   PASS
```

Actual adversarial output:

```text
worst actual Gamma/(25 min(I2)/(12 R^2)) ratio = 0.0630906707807
largest endpoint resource/budget fraction = 0.99023971892
largest propagation/TT-ceiling fraction = 0.972827931667
PASS: finite-dimensional narrowband two-ended 25/12 inertia bound
```

The integrated random-system regression deliberately drives endpoint and propagation resources close to their allowed ceilings. It is not a proof; the analytic assembly is in `FINITE_TWO_ENDED_INERTIA_BOUND.md`.

## Frequency convention

From Stage D onward:

```text
omega_0   absolute gravitational carrier angular frequency
nu        complex-envelope detuning frequency
B         envelope bandwidth, B/omega_0 << 1
k_0       omega_0/c
Gamma_coh (1/2pi) integral over nu of Tr[T^dag T]
I_2       int rho r^2 dV about an endpoint center of mass
```

See `NARROWBAND_NORMALIZATION_AUDIT.md`.

## Prior-art boundary

Generic Stage-A passivity machinery is established systems theory, and broad Stage-B/C antenna ingredients are historical. Current primary anchors include Guta–Yamamoto, Gough–Zhang, Hirakawa–Narihara–Fujimoto (1976), and Lobo (1995).

No priority language is permitted for the cumulative coefficients or the complete two-ended closure until the detailed collision search is complete.

## Promotion discipline

Before expanding the theorem's scope, record the derivation, assumptions, independent check, counterexample attempts, primary-source comparison, and numerical evidence where relevant.

## Priority language

Do not use `first`, `new`, `unique`, `unprecedented`, or equivalent priority wording unless a dedicated primary-source audit supports it. A negative search result is not proof of priority.
