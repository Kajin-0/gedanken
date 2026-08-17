# Experiment 03 — finite-bosonic harmonic MPDO acceptance matrix

**Date:** 2026-08-17  
**Status:** **FROZEN BEFORE ANY ACCEPTED-RANK-16 FINITE-BOSONIC PROPAGATION**

## Purpose

This is the final implementation gate before the full nonlinear phase
Hamiltonian may be enabled.  It asks whether the accepted rank-16 physical
coupled-mode bath can be represented with explicit finite bosonic local spaces
and the structured MPDO solver while reproducing the independent exact-FDT
harmonic equilibrium.

No nonlinear C.1 state and no photon drive are allowed in this gate.

## Fixed physical model

Use the deterministically regenerated accepted rank-16 variable-pole bath with
no refit or simplification:

```text
H_b     = accepted rank-16 Hermitian chain-gauge matrix
Gamma   = accepted full dense positive damping matrix
g       = accepted exact-C0 coupling vector
```

Keep **all** entries of `Gamma` and `g`, even where numerical structure makes
some entries extremely small.

The dimensionless harmonic Hamiltonian is

```math
H_s = a^\dagger a + 1/2 + \lambda x^2,
\qquad
x=\sigma_0(a+a^\dagger),
```

with the exact accepted counterterm `lambda`, and

```math
H_{sb}=x\sum_j(g_j b_j^\dagger+g_j^*b_j),
\qquad
H_b=\sum_{jk}(H_b)_{jk}b_j^\dagger b_k.
```

The Lindblad/Kossakowski part is

```math
\mathcal D\rho=
2\sum_{jk}\Gamma_{jk}
\left(b_k\rho b_j^\dagger-
\frac12\{b_j^\dagger b_k,\rho\}\right).
```

This convention has already passed the independent dense Liouvillian oracle.

## Independent target

The target is the **independently integrated direct-port FDT covariance and its
finite-dimensional squeezed-thermal density operator**, as used by
`heom_harmonic_final_state_gate.py` and the accepted variable-pole harmonic
validation.

The optimized variable-pole covariance is a diagnostic and initialization aid;
it is not substituted for the independent FDT target in the acceptance metric.

## Fixed local Fock spaces

From harmonic-only preflights:

### PRIMARY Fock

```text
system harmonic mode: d_s = 6
bath mode 0:          d_0 = 6
bath modes 1..15:     d_j = 4
```

### HIGH Fock control

```text
system harmonic mode: d_s = 8
bath mode 0:          d_0 = 8
bath modes 1..15:     d_j = 6
```

No local dimension may be changed after a result is seen.

## Tensor controls

The old provisional SVD cutoffs `1e-10/1e-12` are withdrawn by the cutoff audit.
The replacement values are determined mechanically by the already frozen
nonzero-cutoff refinement:

```text
epsilon_star = largest nonzero toy-oracle cutoff that passes

PRIMARY cutoff = epsilon_star * 1e-2
TIGHT cutoff   = epsilon_star * 1e-4
```

Two-site production is authorized only if the frozen refinement returns
`epsilon_star >= 1e-26`.

Other controls remain fixed:

```text
PRIMARY:
  two-site TDVP
  dt       = .02
  maxdim   = 128
  Krylov tolerance = 1e-11

TIGHT:
  two-site TDVP
  dt       = .01
  maxdim   = 256
  Krylov tolerance = 1e-13
```

No state normalization is applied during propagation.

## Initial state and horizon

Initialize the finite harmonic system and every auxiliary in its bare vacuum.
This is only a relaxation initializer; it is not asserted to be the coupled
physical equilibrium.

Propagate to

```text
tau = 240
```

with mandatory stored reduced-system checkpoints

```text
tau = 160, 200, 220, 240.
```

The horizon was frozen from the accepted linear drift gap before finite-bosonic
propagation:

```text
max Re(lambda_drift) = -0.06034486723578
exp(-gap*240)        = 5.131138243379e-7.
```

## Predeclared matrix

Run exactly three rank-16 cases:

```text
H0  PRIMARY Fock + PRIMARY tensor controls
H1  PRIMARY Fock + TIGHT tensor controls
H2  HIGH Fock    + TIGHT tensor controls
```

`H0 -> H1` is the tensor/time-step control.
`H1 -> H2` is the explicit local-Fock control.

There is no post-hoc rescue fourth case in this gate.

## Per-case physicality

At every stored checkpoint require the reduced system state to satisfy

```text
|Tr rho_s - 1|                    < 1e-8
||rho_s-rho_s^dag||_F             < 1e-8
negative eigenvalue mass          < 5e-8.
```

The full MPDO trace must satisfy

```text
|Tr rho_full - 1|                 < 1e-8.
```

No clipping, positivity projection, Hermitization, or trace renormalization may
be applied before acceptance metrics are computed.

## Exact-FDT acceptance

At `tau=240`, every case must satisfy the already frozen finite-bosonic harmonic
gate:

```text
max relative system width error       < 1e-5
half trace distance to exact FDT rho  < 2e-5
normalized q-p covariance             < 2e-5.
```

For unequal finite system dimensions, comparisons to the exact FDT density
operator use a common sufficiently large bare-Fock embedding; missing finite
Fock levels are represented by zeros, not by renormalizing the target into the
retained subspace.

## Late-time stationarity

For each case require

```text
0.5 ||rho_s(240)-rho_s(220)||_1       < 2e-6
0.5 ||rho_s(220)-rho_s(200)||_1       < 5e-6
```

and maximum relative change of either system width over the same intervals

```text
240 vs 220: < 2e-6
220 vs 200: < 5e-6.
```

These thresholds are comfortably above the preflight slow-mode factor at
`tau=240` but materially below the exact-FDT acceptance scale.

## External convergence

At `tau=240`:

### Tensor/time-step convergence

```text
0.5 ||rho_s(H1)-rho_s(H0)||_1         < 5e-5
max relative width difference          < 1e-5.
```

### Fock convergence

Embed H1 and H2 reduced system states in a common bare-Fock space and require

```text
0.5 ||rho_s(H2)-rho_s(H1)||_1         < 5e-5
max relative width difference          < 1e-5.
```

These are implementation convergence tests in addition to each run's independent
FDT comparison.

## Required truncation diagnostics

Each run must report:

```text
maximum MPS bond dimension reached
whether maxdim was saturated
maximum reported SVD truncation error / discarded weight if exposed by backend
final system highest-level population
final highest-level population of every auxiliary mode
```

Saturation of `maxdim` is not automatically a failure if the external H0/H1/H2
convergence tests pass, but it must be reported explicitly and blocks any claim
that the internal bond error alone certifies convergence.

## Decision rule

The finite-bosonic harmonic gate passes only if **all** per-case physicality,
independent-FDT, late-stationarity, tensor-control, and Fock-control requirements
pass simultaneously.

If one axis fails, nonlinear C.1 remains blocked.  No cutoff, timestep, max bond,
Fock dimension, target, or tolerance is changed after seeing the matrix.

## Gate state at freeze

```text
accepted infinite-Gaussian harmonic bath       PASS
small dense Liouvillian/MPO oracle              PASS
small one-site TDVP oracle                      PASS
adaptive two-site zero-truncation oracle        PASS
nonzero two-site cutoff refinement              ACTIVE
rank-16 finite-bosonic harmonic gate            BLOCKED on refinement
nonlinear C.1                                    BLOCKED
photon/capture C.2                               BLOCKED
```
