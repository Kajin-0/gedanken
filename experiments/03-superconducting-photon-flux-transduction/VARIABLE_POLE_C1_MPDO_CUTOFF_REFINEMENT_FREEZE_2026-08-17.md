# Experiment 03 — MPDO nonzero-cutoff refinement freeze

**Date:** 2026-08-17  
**Status:** **FROZEN BEFORE REFINEMENT RESULTS**  
**Scope:** small dense implementation oracle only

## Purpose

The previous cutoff audit proved that standard two-site TDVP becomes essentially
exact when SVD truncation is disabled, while `cutoff=1e-20` remains too loose for
the frozen density-matrix oracle.  This refinement locates the largest practical
**nonzero** ITensor squared-weight cutoff that satisfies the existing oracle.

No accepted rank-16 physical harmonic state and no nonlinear C.1 state are used.

## Fixed calculation

Reuse exactly the same three-site toy Liouvillian, independently assembled MPO,
global-Krylov-expanded initial MPDO, and dense `exp(L*t)` reference.

Freeze

```text
tau_test      = 0.001
dt            = 1e-5
nsite         = 2
reverse_step  = true
TDVP order    = 2
maxdim        = 64
normalize     = false
local Krylov tolerance = 1e-13
local Krylov dimension = 30
```

Run

```text
cutoff = 1e-20, 1e-21, 1e-22, 1e-23, 1e-24, 1e-25,
         1e-26, 1e-27, 1e-28, 1e-29, 1e-30, 0
```

The `0` point is a regression control only.

## Unchanged oracle thresholds

A point passes only if all hold:

```text
half trace distance < 1e-9
trace error         < 1e-10
anti-Hermitian norm < 1e-10
```

Report vector relative error and final maximum bond as diagnostics.

## Predeclared production-selection rule

Let `epsilon_star` be the **largest tested nonzero cutoff** that passes all three
oracle thresholds.

### Two-site production remains eligible only if

```text
epsilon_star >= 1e-26.
```

This prevents selecting a two-site scheme whose required SVD threshold is already
so close to floating-point singular-value resolution that long-run robustness is
questionable before the physical calculation begins.

If eligible, freeze the later physical MPDO cutoffs as

```text
PRIMARY cutoff = epsilon_star * 1e-2
TIGHT cutoff   = epsilon_star * 1e-4.
```

Thus the physical primary run is two decades tighter in discarded squared weight
than the largest toy-oracle pass, and the solver-control run is another two
decades tighter.  `maxdim`, timestep and Krylov controls remain those already
predeclared; only the invalid old cutoff values are replaced.

These cutoffs do **not** guarantee the long rank-16 physical calculation.  The
already frozen finite-bosonic harmonic FDT regression and PRIMARY/TIGHT external
convergence test remain decisive.  Failure there blocks C.1 rather than causing
post-hoc cutoff retuning.

### If no nonzero point passes, or epsilon_star < 1e-26

standard adaptive two-site TDVP is closed for the production C.1 solver.  The
already demonstrated one-site TDVP candidate becomes the next route, but it must
receive a separate pre-result deterministic re-expansion schedule before any
accepted rank-16 propagation.

## Claim boundary

This refinement chooses a numerical truncation regime only.  It does not change
bath physics, system physics, Fock dimensions, C.1 acceptance thresholds, or the
photon/capture gate.
