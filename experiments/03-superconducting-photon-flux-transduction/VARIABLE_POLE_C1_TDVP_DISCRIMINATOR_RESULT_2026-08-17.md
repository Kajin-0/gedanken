# Experiment 03 — non-Hermitian TDVP discriminator result

**Date:** 2026-08-17  
**Status:** **COMPLETE / ONE-SITE CANDIDATE PASS / STANDARD TWO-SITE BLOCKED PENDING CUTOFF AUDIT**

## Workflow

```text
run: 32061873693
job: 95484763987
status: SUCCESS
```

The workflow success means the frozen diagnostic matrix completed.  Scientific
pass/fail is determined by the predeclared oracle thresholds, not by workflow
exit status.

## Fixed dense oracle

The independently assembled OpSum/MPO generator remained exact:

```text
MPO/dense relative error = 1.5877454832948096e-16
```

The globally expanded initial MPDO was unchanged:

```text
initial relative error = 0
initial trace error    = 0
initial max bond       = 15
```

## Matrix A — standard two-site TDVP

`nsite=2`, `reverse_step=true`:

| dt | half trace | trace error | vector relative error | final bond |
|---:|---:|---:|---:|---:|
| 2e-5 | 1.6899547158e-8 | 3.3798647103e-8 | 3.3796053202e-8 | 3 |
| 1e-5 | 1.6899553596e-8 | 3.3798663535e-8 | 3.3796053206e-8 | 3 |
| 5e-6 | 1.6899558460e-8 | 3.3798668531e-8 | 3.3796053208e-8 | 3 |
| 2.5e-6 | 6.3244881952e-5 | 3.1800215461e-8 | 6.3229990713e-5 | 3 |

The first three points are effectively independent of timestep; their vector
error equals the exact fourth Schmidt amplitude identified independently in the
cutoff-semantics analysis.  This is not a time-integration convergence sequence.

Under the frozen decision rule:

```text
standard two-site TDVP: NOT YET VIABLE
```

It remains blocked pending the separately frozen cutoff-semantics audit, which
changes only the SVD truncation cutoff.

## Matrix B — one-site TDVP on fixed expanded manifold

`nsite=1`, `reverse_step=true`:

| dt | half trace | trace error | vector relative error | final bond |
|---:|---:|---:|---:|---:|
| 2e-5 | 3.8405457220e-14 | 7.3274719625e-14 | 7.5054609117e-14 | 4 |
| 1e-5 | 1.0014273625e-13 | 1.9695356457e-13 | 1.9862487061e-13 | 4 |
| 5e-6 | 2.7461847239e-13 | 5.4412030437e-13 | 5.4668556262e-13 | 4 |
| 2.5e-6 | 6.6085424058e-13 | 1.3141709942e-12 | 1.3179328188e-12 | 4 |

All four points pass the frozen oracle requirements

```text
half trace < 1e-9
trace error < 1e-10
anti-Hermitian norm < 1e-10.
```

The slight growth of roundoff-level error with more sweeps is consistent with
accumulated floating-point/local-Krylov error and remains many orders below the
acceptance gate.

Under the frozen decision rule:

```text
one-site TDVP: CANDIDATE PASS
```

It is not yet authorized for long physical evolution because a separate freeze
would be required to specify deterministic re-expansion of the fixed manifold.

## Matrix C — reverse-step disabled

`nsite=2`, `reverse_step=false` gives essentially timestep-independent

```text
half trace ~= 1.83815557e-4
trace error ~= 1.351894e-7
```

and fails at every tested timestep.

Thus simply removing the negative-time projector step is **not** a valid repair.

## Interpretation

The combined evidence is now strong:

1. the Liouvillian MPO is correct;
2. the local non-Hermitian Krylov exponential is accurate;
3. a sufficiently expressive fixed MPS manifold reproduces dense evolution to
   ~1e-13;
4. the failing standard two-site calculation collapses the bond to 3 and lands
   precisely at the amplitude scale of the exact fourth Schmidt component;
5. timestep refinement does not remove that floor.

The remaining active hypothesis is therefore **SVD truncation semantics in the
adaptive two-site update**, not a general TDVP or Lindblad failure.

## Next gate

The already frozen cutoff-only audit tests

```text
cutoff = 1e-12, 1e-14, 1e-16, 1e-18, 1e-20, 0
```

at fixed `dt=1e-5`, standard two-site TDVP, and unchanged oracle thresholds.

If sufficiently tight cutoff restores the oracle, retain adaptive two-site TDVP
with newly frozen production cutoffs.  Otherwise one-site TDVP with a separately
frozen re-expansion schedule becomes the leading structured solver candidate.

No accepted rank-16 finite-bosonic harmonic propagation and no nonlinear C.1
result have been generated.
