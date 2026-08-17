# Experiment 03 — MPDO nonzero-cutoff refinement result

**Date:** 2026-08-17  
**Status:** **PASS / TWO-SITE TDVP RETAINED / PRODUCTION CUTOFFS FROZEN**

## Workflow

```text
run:  32062630697
job:  95487188001
head: ce357cd97d7a9f9ab10e470f5b0c03da351ef9a1
status: SUCCESS
```

The calculation used only the frozen three-site dense implementation oracle. No
accepted rank-16 finite-bosonic physical propagation and no nonlinear C.1 state
was generated.

## Frozen refinement matrix

All points used `tau=.001`, `dt=1e-5`, standard two-site TDVP,
`reverse_step=true`, order 2, `maxdim=64`, no normalization, and the unchanged
local Krylov controls.

| cutoff | half trace | trace error | vector relative error | bond | oracle |
|---:|---:|---:|---:|---:|:---:|
| 1e-20 | 3.340240613677e-9 | 6.680473285670e-9 | 5.010562901092e-9 | 4 | FAIL |
| 1e-21 | 1.382256040155e-9 | 2.764506290553e-9 | 2.513656962183e-9 | 4 | FAIL |
| 1e-22 | 1.383981576321e-10 | 2.767904794254e-10 | 2.517549848580e-10 | 4 | FAIL |
| **1e-23** | **1.429100627806e-11** | **2.857625247543e-11** | **2.581395249792e-11** | **4** | **PASS** |
| 1e-24 | 1.623931975569e-12 | 3.242073276510e-12 | 2.636573627300e-12 | 4 | PASS |
| 1e-25 | 2.014472077108e-13 | 3.970157536060e-13 | 3.999386867840e-13 | 4 | PASS |
| 1e-26 | 5.145094523139e-14 | 9.714451465470e-14 | 1.000238898279e-13 | 4 | PASS |
| 1e-27 | 1.457861865713e-15 | 2.886579864025e-15 | 2.886719875372e-15 | 4 | PASS |
| 1e-28 | 1.457861865713e-15 | 2.886579864025e-15 | 2.886719875372e-15 | 4 | PASS |
| 1e-29 | 1.457861865713e-15 | 2.886579864025e-15 | 2.886719875372e-15 | 4 | PASS |
| 1e-30 | 1.457861865713e-15 | 2.886579864025e-15 | 2.886719875372e-15 | 4 | PASS |
| 0 | 1.457861865713e-15 | 2.886579864025e-15 | 2.886719875372e-15 | 4 | PASS |

The anti-Hermitian norm remains far below `1e-10` throughout the passing region.
The independently assembled MPO/dense generator discrepancy is

```text
1.7388895832145421e-16.
```

## Mechanical selection

The predeclared rule defines

```text
epsilon_star = largest tested nonzero passing cutoff.
```

Therefore

```text
epsilon_star = 1e-23.
```

Because

```text
epsilon_star >= 1e-26,
```

adaptive two-site TDVP remains eligible for the physical finite-bosonic gate.

The predeclared production rule now fixes

```text
PRIMARY cutoff = epsilon_star * 1e-2 = 1e-25
TIGHT cutoff   = epsilon_star * 1e-4 = 1e-27.
```

These replace the withdrawn provisional `1e-10/1e-12` values in all subsequent
Experiment-03 MPDO calculations.

All other already frozen controls remain unchanged:

```text
PRIMARY: dt=.02, maxdim=128, Krylov tol=1e-11
TIGHT:   dt=.01, maxdim=256, Krylov tol=1e-13
```

## Interpretation

The solver-selection question is now closed at the small dense-oracle level:

```text
MPO generator mapping                 PASS
non-Hermitian Krylov local evolution  PASS
standard two-site TDVP                PASS when SVD cutoff is adequate
one-site TDVP                         retained as fallback only
production PRIMARY cutoff             1e-25
production TIGHT cutoff               1e-27
```

The extremely small cutoff numbers are not equivalent to `1e-25` amplitude
errors: ITensor interprets cutoff as discarded **squared singular weight**.
External convergence and physicality remain mandatory; the small oracle does not
waive the finite-bosonic harmonic matrix.

## Next gate

The already frozen physical rank-16 harmonic matrix is now authorized:

```text
H0 PRIMARY Fock + PRIMARY tensor
H1 PRIMARY Fock + TIGHT tensor
H2 HIGH Fock    + TIGHT tensor
```

with independent exact-FDT comparison, physicality, late stationarity and
H0/H1/H2 external convergence.  No nonlinear Hamiltonian is authorized until
that complete matrix passes.
