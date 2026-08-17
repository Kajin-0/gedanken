# Experiment 03 — physical rank-16 MPDO zero-time/derivative smoke result

**Date:** 2026-08-17  
**Status:** **PASS**

## Scope

This checkpoint tests vectorization, custom MPDO state definitions, full/reduced
trace contractions, Hermiticity preservation, and one exact application of the
accepted rank-16 finite-bosonic harmonic Liouvillian. It performs no TDVP time
evolution, no equilibrium/FDT comparison, and no nonlinear C.1 calculation.

Workflow:

```text
run: 32064102054
job: 95491905891
status: SUCCESS
```

An earlier attempt failed before the smoke identities because custom Qudit state
methods used the operator-style integer-dimension dispatch rather than the
`Index` dispatch used by ITensor state construction. That API defect was fixed
without changing any physical matrix, Fock dimension, or threshold.

## Result

For the PRIMARY frozen local Fock class and bare-vacuum product MPDO:

```text
initial full trace           = 1.0
initial reduced-state error  = 0
initial anti-Hermitian norm  = 0
```

After one **exact MPO application**

```math
|\dot\rho\rangle = \mathcal L |\rho\rangle
```

with no TDVP and no SVD time stepping:

```text
Tr_full(L rho) = 0 + 0 i
Tr_sys (L rho) = 0 + 0 i
reduced derivative anti-Hermitian norm = 0
MPO max link reported in smoke = 31
derivative MPS max bond        = 30
```

The separately completed construction workflow reports max MPO link 30 for both
frozen Fock classes. The one-link difference in the smoke diagnostic is not a
physics discrepancy and does not affect the predeclared feasibility conclusion;
the exact derivative state itself has max bond 30. If needed for internal
bookkeeping, the link-dimension diagnostic can be made immutable before `apply`,
but no acceptance gate depends on 30 versus 31 because both are far below the
frozen ceiling of 1024.

Disposition:

```text
VARIABLE_POLE_C1_HARMONIC_MPDO_SMOKE_PASS
```

## Interpretation

The physical rank-16 finite-bosonic implementation now separately verifies:

```text
accepted bath regeneration             PASS
exact physical Liouvillian MPO build   PASS
full dense Gamma retained              PASS
MPDO vacuum construction               PASS
full trace functional                  PASS
reduced partial trace                  PASS
Liouvillian trace preservation         PASS
Liouvillian Hermiticity preservation   PASS
```

The remaining pre-matrix implementation gate is the already frozen single H0
production-setting TDVP step at `tau=.02`.  A pass authorizes the full H0/H1/H2
harmonic relaxation matrix; it does not itself establish equilibrium accuracy.
