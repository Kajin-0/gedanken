# Experiment 03 — MPDO cutoff-semantics audit result

**Date:** 2026-08-17  
**Status:** **PASS / FAILURE MECHANISM IDENTIFIED / PRODUCTION CUTOFF NOT YET FROZEN**

## Workflow

```text
run:    32062179864
job:    95485730109
head:   4df3bbc7c1464232b24014d2fbd145880e857501
status: SUCCESS
```

The workflow success means the frozen cutoff matrix completed. Scientific
acceptance is determined by the predeclared dense-oracle thresholds.

## Exact dense Schmidt spectrum at tau=.001

For the exact dense toy Lindblad state, the four singular values across the two
MPS cuts are

```text
cut 1:
0.9999999959993386
6.322998135897237e-5
6.322998135864594e-5
3.998030558630122e-9

cut 2:
0.999999966201316
1.8383702504591473e-4
1.838370250455688e-4
3.37960529199308e-8
```

The fourth squared singular weights are

```text
cut 1: 1.5984248347740287e-17
cut 2: 1.1421731929667629e-15.
```

This is important because ITensor's `cutoff` controls discarded **squared
singular weight**, not discarded singular amplitude.

## Frozen cutoff matrix

All points use the same exact toy Liouvillian and MPO, `tau=.001`, `dt=1e-5`,
standard two-site TDVP, `reverse_step=true`, order 2, `maxdim=64`, no
normalization, and the same local Krylov tolerance/dimension.

| cutoff | half trace | trace error | anti-Hermitian Frobenius | vector relative error | final bond | oracle |
|---:|---:|---:|---:|---:|---:|:---:|
| 1e-12 | 1.902081745886e-4 | 1.497773460879e-8 | 7.633099380652e-5 | 1.944070061941e-4 | 2 | FAIL |
| 1e-14 | 1.689955359563e-8 | 3.379866353459e-8 | 1.581637695118e-17 | 3.379605320618e-8 | 3 | FAIL |
| 1e-16 | 1.689955359563e-8 | 3.379866353459e-8 | 1.581637695118e-17 | 3.379605320618e-8 | 3 | FAIL |
| 1e-18 | 1.689955359563e-8 | 3.379866353459e-8 | 1.581637695118e-17 | 3.379605320618e-8 | 3 | FAIL |
| 1e-20 | 3.340240613677e-9 | 6.680473285670e-9 | 5.576713968263e-17 | 5.010562901092e-9 | 4 | FAIL |
| 0 | 1.458747144402e-15 | 2.886579864025e-15 | 3.801724724107e-17 | 2.886717704712e-15 | 4 | **PASS** |

The MPO/dense generator regression remained at

```text
1.7388895832145421e-16.
```

## Interpretation

This audit closes the main implementation ambiguity.

1. **The Liouvillian construction is correct.**  It agrees with the independent
   dense generator at machine precision.
2. **Standard two-site TDVP itself is capable of essentially exact propagation.**
   With no SVD truncation, the result is at the `1e-15` level.
3. **The previous `~1e-8` floor is an adaptive-SVD truncation artifact.**  The
   surviving bond dimension tracks which exact Schmidt components the requested
   squared-weight cutoff permits the SVD to discard.
4. `cutoff=1e-20` is still too loose for the existing small-system oracle:
   although the final exact fourth Schmidt weights are larger than `1e-20`,
   intermediate sweep truncations accumulate a `~5e-9` vector error and
   `~6.7e-9` trace error.
5. The original proposed production cutoffs `1e-10` and `1e-12` are therefore
   **withdrawn before any accepted rank-16 finite-bosonic harmonic run**.  They
   are inconsistent with the density-matrix accuracy demanded by Gate C.1.

The one-site TDVP candidate remains valid as a fallback because the independent
TDVP discriminator reproduced the same dense evolution at `~1e-13` without
adaptive SVD truncation.  It is not needed unless a practical nonzero two-site
cutoff cannot be established.

## Disposition

```text
MPO construction                         PASS
non-Hermitian local Krylov propagation   PASS
two-site TDVP with zero truncation       PASS
original production SVD cutoffs          REJECTED
finite nonzero production cutoff         UNRESOLVED
physical rank-16 harmonic regression     BLOCKED
nonlinear C.1                             BLOCKED
```

A tighter **nonzero** cutoff refinement must be frozen and run before selecting
the production MPDO cutoff. No rank-16 physical finite-bosonic result has yet
been generated.
