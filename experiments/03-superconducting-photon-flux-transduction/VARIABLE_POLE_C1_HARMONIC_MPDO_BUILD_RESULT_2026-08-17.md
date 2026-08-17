# Experiment 03 — physical rank-16 harmonic MPDO construction result

**Date:** 2026-08-17  
**Status:** **PASS / EXACT 17-SITE LIOUVILLIAN MPO TRACTABLE**

## Scope

This checkpoint validates construction and tensor-network structure of the exact
accepted rank-16 finite-bosonic harmonic Liouvillian in both frozen Fock classes.
It performs **no time evolution**, no nonlinear C.1 calculation, and no photon
calculation.

Workflow:

```text
run: 32064003668
prepare: PASS
primary build job: 95491999179 PASS
high build job:    95491999038 PASS
```

The first two workflow attempts exposed only language/interchange defects before
MPO construction (complex CSV parsing and Julia Hermitian eigensolver naming).
Those were repaired without changing any physical matrix, local dimension,
threshold, or acceptance rule.

## PRIMARY Fock construction

Frozen Hilbert dimensions:

```text
system = 6
bath mode 0 = 6
bath modes 1..15 = 4
```

Corresponding local Liouville dimensions:

```text
36,36,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16
```

The exact OpSum/MPO built with all accepted `H_b`, `Gamma`, and `g` entries has
link dimensions

```text
4,6,10,14,18,22,26,28,30,30,26,22,18,14,10,6
```

therefore

```text
max MPO bond = 30.
```

Structural checks:

```text
||H_b-H_b^dag|| / ||H_b|| = 0
||Gamma-Gamma^dag|| / ||Gamma|| = 0
min eig(Gamma) = 2.994750927889e-9
||g[1:]||/||g|| = 2.992277719973e-17
sigma0 = 0.040115726197698695
lambda = 43.395916714820736
```

Disposition:

```text
VARIABLE_POLE_C1_HARMONIC_MPDO_BUILD_PASS
```

## HIGH Fock construction

Frozen Hilbert dimensions:

```text
system = 8
bath mode 0 = 8
bath modes 1..15 = 6
```

Local Liouville dimensions:

```text
64,64,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36
```

Despite the larger local dimensions, the exact operator graph produces the same
MPO links:

```text
4,6,10,14,18,22,26,28,30,30,26,22,18,14,10,6
max MPO bond = 30.
```

Structural checks:

```text
H_b Hermiticity error = 0
Gamma Hermiticity error = 0
min eig(Gamma) = 2.994750923627e-9
g-tail ratio = 2.992277719973e-17
```

Disposition:

```text
VARIABLE_POLE_C1_HARMONIC_MPDO_BUILD_PASS
```

## Interpretation

The full dense accepted damping matrix is **not** a prohibitive MPO-structure
bottleneck.  The predeclared construction feasibility ceiling was `max bond <=
1024`; the exact physical Liouvillian is more than thirty-fold below that ceiling
at bond 30 in both Fock classes.

No damping localization, Gamma diagonalization, coefficient pruning, bath refit,
or nearest-neighbor approximation is needed or authorized.

## Next gate

A separate zero-time physical trace/derivative smoke test must pass on the exact
rank-16 generator.  After that, one production-setting TDVP step may be used as
an implementation/performance smoke test.  The already frozen H0/H1/H2
finite-bosonic harmonic matrix remains the decisive physics gate.
