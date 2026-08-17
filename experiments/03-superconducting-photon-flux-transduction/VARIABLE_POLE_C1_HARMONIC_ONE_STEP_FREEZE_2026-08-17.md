# Experiment 03 — physical rank-16 one-step TDVP smoke freeze

**Date:** 2026-08-17  
**Status:** **FROZEN BEFORE ONE-STEP RESULT**  
**Scope:** implementation/performance smoke only; not the finite-bosonic harmonic acceptance result

## Purpose

Before launching the 12,000-24,000-sweep H0/H1/H2 harmonic relaxation matrix,
exercise one actual production-setting two-site TDVP step on the exact accepted
17-site rank-16 Liouvillian.  This catches production-only state-dispatch,
partial-trace, local-Krylov, or adaptive-SVD defects without inspecting an
equilibrium/FDT result.

This smoke is authorized only after the zero-time trace/derivative smoke passes.

## Fixed model

Use the exact solver-neutral accepted rank-16 `H_b`, full `Gamma`, and `g` and the
PRIMARY frozen local Fock class:

```text
system d=6
bath0 d=6
bath1..15 d=4
```

Initialize every site in bare vacuum.

## Fixed propagation

Use exactly the already frozen H0 production controls:

```text
tau = 0 -> .02
one TDVP step
nsite = 2
reverse_step = true
order = 2
dt = .02
maxdim = 128
SVD cutoff = 1e-25
normalize = false
local Krylov tolerance = 1e-11
local Krylov dimension = 30
```

No parameter may be changed based on the result.

## Required checks

At `tau=.02`, report:

```text
full MPDO trace error
reduced system trace error
reduced anti-Hermitian Frobenius norm
reduced negative eigenvalue mass
maximum MPS bond
system highest retained Fock population
maximum bath highest retained Fock population
```

Pass only if

```text
|Tr rho_full - 1| < 1e-9
|Tr rho_s    - 1| < 1e-9
anti-Hermitian norm < 1e-9
negative eigenvalue mass < 5e-9
max MPS bond <= 128
```

The highest-level populations are diagnostics only in this single short step;
the frozen H0/H1/H2 equilibrium matrix remains controlling for Fock convergence.

## Explicit non-claims

Do **not** compare the `tau=.02` state to equilibrium FDT and do not interpret its
system widths, occupation, or entropy physically.  At one short step the system
is deliberately still in a transient from the bare-vacuum initializer.

A pass authorizes launching the already frozen H0/H1/H2 harmonic matrix.  A fail
blocks that matrix and must be diagnosed as an implementation failure; no H0
setting is retuned post hoc.
