# Experiment 03 — non-Hermitian TDVP discriminator freeze

**Date:** 2026-08-17  
**Status:** **FROZEN BEFORE DISCRIMINATOR RESULTS**  
**Scope:** small dense implementation oracle only; no physical harmonic or nonlinear C.1 result

## Trigger

The Experiment-03 MPDO/MPO oracle established that the OpSum/MPO Liouvillian is
correct to dense relative error `1.5877454832948096e-16`, but the default
ITensorMPS two-site TDVP propagation fails the unchanged oracle tolerances:

```text
tau=.001  half trace = 1.6899553596e-08   trace error = 3.3798663535e-08
tau=.003  half trace = 1.5208800125e-07   trace error = 3.0416429253e-07
tau=.005  half trace = 4.2244447625e-07   trace error = 8.4483490725e-07
```

A four-vector global-Krylov basis expansion changed the initial MPS bond from 1
to 15 while leaving the represented state exactly unchanged, yet reproduced the
same propagation errors to numerical precision.  Therefore insufficient initial
bond support is closed as the cause.

Inspection of pinned ITensorMPS v0.4.1 shows:

- `tdvp(operator,t,...)` directly computes `exp(t*operator)`; there is no hidden
  Hamiltonian `-i` convention;
- the default updater is general KrylovKit `exponentiate`;
- projector-splitting TDVP with `reverse_step=true` performs explicit negative-
  time reduced bond evolution between local forward updates;
- the default second-order TDVP sweep uses forward and reverse half-time sweeps.

The remaining question is therefore whether the error converges away under the
projector-splitting controls or whether TDVP is unsuitable for this non-normal
Liouvillian at the required accuracy.

## Frozen oracle

Reuse **exactly** the existing system-plus-two-auxiliary dense oracle and its
independently assembled MPO.  Use the global-Krylov-expanded initial state
(`krylovdim=4`) because it is an exact representation of the same initial MPDO
and removes initial support as a confounder.

Fixed final time:

```text
tau_test = 0.001
```

Fixed local exponential controls:

```text
maxdim       = 64
cutoff       = 1e-14
Krylov tol   = 1e-13
Krylov dim   = 30
normalize    = false
TDVP order   = 2
```

### Matrix A — two-site, standard projector splitting

```text
nsite=2, reverse_step=true
dt = 2e-5, 1e-5, 5e-6, 2.5e-6
```

### Matrix B — one-site, fixed expanded manifold

```text
nsite=1, reverse_step=true
dt = 2e-5, 1e-5, 5e-6, 2.5e-6
```

### Matrix C — no reverse bond update discriminator

This is **diagnostic only**, not an automatically authorized production
integrator:

```text
nsite=2, reverse_step=false
dt = 2e-5, 1e-5, 5e-6, 2.5e-6
```

Its purpose is to determine whether the negative-time projector step dominates
the non-Hermitian error.  Even if it performs well, a separate algorithm freeze
is required before physical use because removing the projector reverse step
changes the TDVP splitting scheme.

## Metrics

For every matrix point compare against exact dense `exp(L*tau_test) rho0` and
report:

```text
half trace distance
trace error
anti-Hermitian Frobenius norm
relative vector error
final maximum MPS bond dimension
```

The existing oracle thresholds remain unchanged:

```text
half trace distance < 1e-9
trace error         < 1e-10
anti-Hermitian norm < 1e-10
```

No threshold is relaxed for this discriminator.

## Predeclared decision rule

### Standard two-site TDVP remains viable only if

1. the error decreases systematically under timestep halving; and
2. at least one tested timestep reaches all existing oracle thresholds without
   exhausting `maxdim=64`.

If the finest standard two-site point remains above threshold or displays a
nonconvergent floor, **standard two-site TDVP is closed** for the C.1
Liouvillian.

### One-site TDVP becomes a candidate only if

it reaches all oracle thresholds while the expanded manifold remains within the
frozen bond cap.  A passing one-site result does not yet authorize production:
a separate pre-result freeze must specify whether/when the Krylov basis is
re-expanded during long evolution.

### `reverse_step=false`

is a mechanism discriminator only.  A pass cannot be promoted directly to the
physical harmonic regression.  If it uniquely removes the error, a distinct
integrator/algorithm acceptance record is required.

### If no TDVP variant passes

close TDVP as the propagation backend and freeze a **global non-Hermitian
Arnoldi/Krylov MPS propagator** before implementation.  The existing ITensorMPS
`applyexp` backend is not accepted as that replacement because its pinned source
uses a three-term Lanczos recurrence, which assumes a Hermitian/symmetric Krylov
structure and is not the desired general Arnoldi method for this Liouvillian.

## Claim boundary

This discriminator contains no accepted-bath rank-16 physical propagation, no
finite-bosonic FDT result, no nonlinear detector result, and no photon drive.
