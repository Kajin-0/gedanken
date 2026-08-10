# Claim Ledger — Experiment 02

This ledger is authoritative for Experiment 02. Conversation history is a source of hypotheses, never proof.

## Status labels

- `PROVISIONAL` — candidate under investigation.
- `ESTABLISHED WITHIN MODEL` — derived and independently checked within explicit assumptions.
- `FAILED AS A CURRENT CLAIM` — contradicted or outside the established scope.
- `HISTORICAL / PRIOR ART` — established ingredient; not a novelty claim.
- `OPEN` — unresolved extension, collision, or significance question.

## Current ledger

| Statement | Status | Evidence |
|---|---|---|
| Complex-envelope `H2` spectral-area metric for stable strictly proper selected cross-port blocks | ESTABLISHED WITHIN MODEL | `PASSIVE_SELECTED_PORT_CUT_DERIVATION.md` |
| Passive selected-port cut `||H||_2^2 <= min[Tr(K_i^dag K_i),Tr(K_o^dag K_o)]` | ESTABLISHED WITHIN MODEL | Stage-A derivation + CI |
| Separated passive cut by source/receiver gravitational traces | ESTABLISHED WITHIN MODEL | Stage-A derivation + random two-ended adversary |
| `sum_n (q_n:q_n)/mu_n <= (20/3) I_2` | ESTABLISHED WITHIN MODEL | Stage-B derivation + CI |
| `Tr(K_g^dag K_g) <= (4G/3c^5) I_2 Omega^4` in the retained quadrupolar modal sector | ESTABLISHED WITHIN MODEL | Stage-B derivation + CI |
| Passive unitary internal mode mixing cannot increase gravitational coupling trace | ESTABLISHED WITHIN MODEL | trace invariance + Stage-B CI |
| Leading compact TT propagation coefficient `limsup (kR)^2 ||P_g||_op^2 <= 25/16` | ESTABLISHED WITHIN MODEL | Stage-C derivation + CI; V7 used only as post-derivation cross-check |
| Narrowband two-ended inertia bound `Gamma_coh lesssim [25 G omega_0^2/(12 c^3 R^2)] min(I_2A,I_2B)` | ESTABLISHED WITHIN MODEL | `FINITE_TWO_ENDED_INERTIA_BOUND.md` + combined CI |
| Countably infinite separable **bounded-port Markov** modal sectors obey the same passive cut | ESTABLISHED WITHIN MODEL | `INFINITE_DIMENSIONAL_BOUNDED_PORT_EXTENSION.md` + infinite-modal CI |
| Stage-B inertia resource makes the countable gravitational port Hilbert–Schmidt | ESTABLISHED WITHIN MODEL | finite trace `Tr(K_g^dag K_g)=sum kappa_g,n` in the bounded-port modal representation |
| Same simple theorem over arbitrary broad absolute frequency | FAILED AS A CURRENT CLAIM | `NARROWBAND_NORMALIZATION_AUDIT.md` |
| Arbitrary unbounded PDE boundary-control/observation ports are covered | FAILED AS A CURRENT CLAIM | admissibility/domain analysis not supplied |
| Genuinely non-Markov continua are covered | FAILED AS A CURRENT CLAIM | outside declared model |
| Repeated passive source↔receiver returns cannot raise the retained leading `1/R^2` ceiling | PROVISIONAL | next physical attack |
| Eigenmode gravitational-antenna emission/reception theory is new here | HISTORICAL / PRIOR ART | Hirakawa–Narihara–Fujimoto 1976 |
| General arbitrary-elastic-body multimode GW response is new here | HISTORICAL / PRIOR ART | Lobo 1995 |
| Infinite-dimensional `H2`/operator-Gramian machinery is new here | HISTORICAL / PRIOR ART | Baras–Brockett 1975; Opmeer–Reis–Wollner 2013 |
| The exact `20/3`/`4/3` cumulative coefficient is novel | OPEN | historical collision search incomplete |
| The complete gravity-specific two-ended inertia closure is novel | OPEN | complete prior-art collision search incomplete |
| Earlier conversation-only Experiment-02 branches/CI/manuscript are repository evidence | FAILED AS A CURRENT CLAIM | only the real `main` history below counts |

## Real validation record

### Stage A — passive cut

```text
workflow: .github/workflows/experiment02-passive-cut.yml
first run: 31391304791
job: 93463450929
PASS
```

Representative output:

```text
worst endpoint H2/resource ratio = 0.410127000961
largest full-scattering singular value = 1
worst two-ended Gamma/bound ratio = 0.089763188389
```

### Stage B — endpoint resource

```text
workflow: .github/workflows/experiment02-endpoint-resource.yml
first run: 31392339989
job: 93466817164
PASS
```

```text
worst 20/3 tensor absolute error = 2.84217094304e-14
worst truncated Bessel ratio = 1
worst full-basis Parseval absolute error = 1.70530256582e-13
worst modal-mixing invariance absolute error = 5.68434188608e-14
worst cumulative linewidth/(4 I2/3) ratio = 0.381072504534
```

### Stage C — TT propagation

```text
workflow: .github/workflows/experiment02-tt-propagation.yml
first run: 31393020114
job: 93469060678
PASS
```

```text
aligned directivity saturation = 2.5
aligned amplitude prefactor = 1.25
aligned power prefactor = 1.5625
PASS: compact TT propagation 25/16 bound
```

### Combined finite narrowband theorem

```text
workflow: .github/workflows/experiment02-combined-bound.yml
commit: 8fc8da7cf5d51e3a56d7e0b15434407c7e493ecb
run: 31393498572
job: 93470648716
PASS
```

```text
worst actual Gamma/(25 min(I2)/(12 R^2)) ratio = 0.0630906707807
largest endpoint resource/budget fraction = 0.99023971892
largest propagation/TT-ceiling fraction = 0.972827931667
```

### Countably infinite bounded-port extension

```text
workflow: .github/workflows/experiment02-infinite-modal.yml
commit: 91566b4ccfb1488b54a403a79452b9dc67347181
run: 31394415776
job: 93473679179
PASS
```

```text
analytic infinite gravitational trace limit = 0.0789987925949
N=64 gravitational trace = 0.0787012072883
N=64 trace tail = 0.000297585306554
largest lambda_max(P_u) = 0.733694365996
worst H2/gravitational-resource ratio = 0.581912323912
modal-mixing resource error = 4.16333634234e-17
modal-mixing H2 error = 8.67361737988e-16
PASS: countably-infinite bounded-port truncation stress test
```

The truncation test is not the infinite-dimensional proof. The proof is the positive contraction-semigroup Gramian bound plus Hilbert–Schmidt gravitational-port regularity in `INFINITE_DIMENSIONAL_BOUNDED_PORT_EXTENSION.md`.

## Frequency convention

```text
omega_0   absolute gravitational carrier angular frequency
nu        complex-envelope detuning
B         envelope bandwidth, B/omega_0 << 1
k_0       omega_0/c
Gamma_coh (1/2pi) integral over nu of Tr[T^dag T]
I_2       int rho r^2 dV about endpoint COM
```

## Priority discipline

Broad ingredients are explicitly not novelty claims. Do not use `first`, `new`, `unique`, `unprecedented`, or equivalent priority wording without a dedicated primary-source collision audit. A negative search is not proof of priority.
