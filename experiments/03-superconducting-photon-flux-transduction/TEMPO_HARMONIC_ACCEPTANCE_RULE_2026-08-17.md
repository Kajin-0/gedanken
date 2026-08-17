# Experiment 03 — TEMPO harmonic acceptance rule

Date: 2026-08-17

## Purpose

This document freezes the acceptance criteria for using an influence-functional / TEMPO solver as the independent open-system method for nonlinear Gate C.1.  It is committed before the first actual direct-port harmonic TEMPO pilot result is read.

A successful small pilot is **not** a pass.  TEMPO may be promoted to nonlinear use only after the actual direct-port harmonic problem reproduces the independently known exact FDT/Gaussian reduced equilibrium under a controlled convergence matrix.

## Physics that must remain fixed

The harmonic validation must use:

- the same `.212` compensated electrical operating point;
- the same direct-port positive-real environment;
- the same physical Caldeira-Leggett counterterm used in harmonic Gate B;
- the same exact FDT covariance oracle;
- the same dimensionless `tau = omega_c t` convention;
- no clipping, positivity repair, or post-selected spectral projection.

The TEMPO initial state is factorized system x bath.  Therefore initial slip is allowed and the coupled FDT state is an **asymptotic reduced-state oracle**, not a t=0 oracle.

## Analytic implementation prerequisites

Before interpreting the direct-port harmonic result, TEMPO must pass:

1. real-exponential pure-dephasing analytic test;
2. genuinely complex-pole pure-dephasing analytic test;
3. trace and Hermiticity preservation in both tests.

These tests validate the explicit-correlation interface and conjugation convention only.

## Exact-state acceptance thresholds

The final converged harmonic TEMPO state must meet the existing Gate-B full-state standards:

```text
finite-basis exact-reference width error  < 1e-7
max relative FDT width error              < 1e-6
0.5 * nuclear norm(rho_TEMPO-rho_exact)   < 5e-6
negative eigenvalue mass                  < 5e-8
trace error                               < 1e-8
relative anti-Hermitian Frobenius norm    < 1e-8
```

These thresholds are not to be relaxed after seeing TEMPO results.

## Required convergence axes

A single favorable parameter set is insufficient.  Before nonlinear promotion, the following axes must be controlled.

### 1. Time step

At fixed memory and tensor tolerance, two finest practical time steps must give

```text
0.5 * ||rho_dt1 - rho_dt2||_1 < 5e-6
```

and both must satisfy the exact-state thresholds above.

### 2. Memory cutoff

At fixed fine time step, increasing `tcut` must give

```text
0.5 * ||rho_tcut1 - rho_tcut2||_1 < 5e-6
```

with no reversal in exact-state accuracy.

### 3. Tensor SVD tolerance

Tightening `epsrel` by at least two orders of magnitude must change the late reduced state by

```text
0.5 * ||rho_eps1 - rho_eps2||_1 < 5e-6.
```

### 4. Bath expansion order

The direct-port thermal decomposition must be checked at adjacent already-validated Padé orders, nominally N=4 and N=5.  Their converged late reduced states must differ by

```text
0.5 * ||rho_p4 - rho_p5||_1 < 5e-6.
```

This is a bath-representation control, not a refit.

### 5. Hilbert basis

The final acceptance basis must itself reproduce the exact Gaussian widths to <1e-7.  At least one larger system basis must be checked for reduced-state stability where computationally feasible; a basis-edge population/localization diagnostic must accompany the nonlinear transition later.

### 6. Late-time equilibration

The result must be stationary on the same state norm used for the oracle comparison.  Over a late-time interval at least several bath-memory times long,

```text
0.5 * ||rho(t_final)-rho(t_late)||_1 < 5e-6.
```

The comparison point must not be chosen from a transient minimum in the oracle error.

### 7. Initial-state independence

At the final harmonic configuration, two materially different factorized system initial states must converge to late reduced states satisfying

```text
0.5 * ||rho_final,A-rho_final,B||_1 < 5e-6.
```

This guards against mistaking an unequilibrated trajectory for the coupled stationary state.

## Pilot rule

A low-dimensional pilot may use looser sanity guards only to answer:

- is the direct-port correlation/counterterm/unit mapping grossly correct?
- is TEMPO computationally viable for this bath?
- does relaxation move toward the exact FDT state rather than away from it?

A pilot cannot pass the harmonic method gate because its finite Hilbert basis may itself fail the <1e-7 reference criterion.

## Promotion rule

Only after **all** exact-state and convergence requirements above are satisfied may TEMPO be called a validated independent harmonic solver for this direct-port problem and be considered for nonlinear Gate C.1.

Even then, nonlinear Gate C.1 requires its own convergence in:

- restricted-well Hilbert basis/domain;
- TEMPO timestep and memory;
- tensor tolerance;
- bath order;
- metastable-state conditioning/preparation.

No photon-pulse Gate D calculation is authorized before nonlinear cold-state Gate C.1 closes.

## Current gate status at predeclaration

- Gate A: PASS
- Gate B conventional harmonic HEOM: PASS
- Gate C.1: ACTIVE / method recovery
- Gate C.2: BLOCKED
- Gate D: BLOCKED
- Gate E: BLOCKED
- Publication: NO-GO
