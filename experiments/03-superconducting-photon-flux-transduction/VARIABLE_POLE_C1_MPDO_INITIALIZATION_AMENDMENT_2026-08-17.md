# Experiment 03 — MPDO product-start initialization amendment

**Date:** 2026-08-17  
**Status:** **FROZEN BEFORE THE REPAIRED ORACLE RUN**  
**Scope:** tensor-network implementation only; no nonlinear C.1 result has been generated

## Trigger

The first ITensorMPS MPDO oracle run (`32060555857`) established two sharply
separated facts:

1. the independently assembled OpSum/MPO Liouvillian contracts back to the dense
   reference generator with relative error

   ```text
   1.5877454832948096e-16
   ```

   so the local super-operator definitions, Kossakowski terms, signs and
   vectorization mapping are correct;
2. two-site TDVP started directly from the rank-one product MPDO developed a
   trace error of `8.4483490725e-7` by `tau=.005`, exceeding the predeclared
   oracle threshold.  No oracle threshold is changed by this amendment.

The error is therefore classified as a **product-state variational-basis
initialization defect**, not a generator/physics failure.

## Frozen repair

ITensorMPS v0.4.1 provides global Krylov basis expansion

```text
expand(state, operator; alg="global_krylov", ...)
```

which enlarges the internal MPS basis using repeated applications of the
operator while returning an MPS equal to the input state.  The repaired oracle
and all later product-start MPDO evolutions shall use this expansion before the
first TDVP step.

Freeze:

```text
algorithm          = global_krylov
krylovdim          = 4
oracle cutoff      = 1e-14
oracle apply maxdim= 64
production cutoff  = corresponding frozen TDVP cutoff
production maxdim  = corresponding frozen TDVP maxdim
```

The implementation must explicitly verify before evolution that the expanded
MPDO represents the same dense initial state to relative vector error `<1e-13`
and that its trace differs from unity by `<1e-13` in the small dense oracle.

## What is not changed

The following remain exactly as frozen before the failed run:

```text
oracle dt                    = 1e-5
oracle times                 = .001, .003, .005
MPO/dense relative threshold < 1e-12
half trace threshold         < 1e-9
trace error threshold        < 1e-10
Hermiticity threshold        < 1e-10
production TDVP dt/maxdim/cutoff/Krylov tolerances unchanged
C.1 physical acceptance thresholds unchanged
```

No nonlinear state, basin probability or photon-driven result was inspected in
choosing this repair.

## Decision rule

If the repaired small-system oracle still fails the existing thresholds, the
product-start two-site-TDVP implementation remains blocked.  Thresholds are not
to be relaxed.  A different structured propagator must then be frozen before
further physical work.
