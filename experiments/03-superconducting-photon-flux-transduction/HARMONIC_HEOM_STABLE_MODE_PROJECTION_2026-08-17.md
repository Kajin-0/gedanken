# Experiment 03 — harmonic HEOM stable-mode projection validation — 2026-08-17

## Purpose

Validate unstable-mode projection on a deliberately unstable **harmonic** HEOM
representation before considering any projection in nonlinear Gate C/D.  This is
a controlled test because the harmonic reduced equilibrium state is independently
known from exact quantum FDT.

The test case is:

```text
dim=12
Npade=4
hierarchy depth=3
bath exponents=6
ADOs=84
full HEOM dimension=12,096
```

The same finite generator was previously shown to have right-half-plane modes.
The exact finite-dimensional Gaussian reference has basis-width error
`8.1046e-14`, so system-basis representation of the FDT oracle is not limiting.

## Method

Script/workflow:

```text
calculations/heom_harmonic_stable_mode_projection.py
.github/workflows/experiment03-heom-harmonic-stable-projection.yml
run 31999203526
job 95296249560
```

Right unstable eigenvectors `R` of `L` and matching left eigenvectors `W` of
`L^dagger` were computed and a biorthogonal spectral projector was formed:

```text
P = I - R (W^dagger R)^(-1) W^dagger.
```

Only modes with `Re(lambda)>1e-7` were removed.  The physical HEOM generator,
bath, counterterm, temperature, system Hamiltonian, and hierarchy were not
changed.  No density-matrix clipping or positivity repair was applied.

The projected initial HEOM vector was propagated with the original `L`; `P` was
reapplied only at output intervals to suppress numerical re-entry into the known
unstable invariant subspace.

## Projector audit

Twenty rightmost modes were requested on both `L` and `L^dagger`.  The returned
window extended safely into the left half-plane (`min Re ~ -0.120609`), and six
unstable modes were found as three conjugate pairs:

```text
+0.0581070887387 +/- 0.208333471937 i
+0.0209921716734 +/- 1.364831153263 i
+0.00238010739583 +/- 0.784845740635 i
```

Left/right eigenvalue matching errors were `<=6.21e-14`; eigenpair residuals were
of order `1e-13`.

Projector diagnostics:

```text
cond(W^dagger R)       = 1.296616
idempotence residual   = 2.082e-15
P annihilation of R    = 7.335e-17
left-subspace leakage  = 2.127e-15
```

The projection is therefore numerically well conditioned for this controlled
case.

## Initial-state invasiveness

Projection preserves the physical root trace to numerical precision but is not
identically zero on the factorized oscillator-ground HEOM initializer:

```text
root trace before       = 1
root trace after        = 1 + 9.48e-21 i
root half-nuclear change= 1.77350e-5
full HEOM relative change=1.46396e-2
```

The larger full-vector change mainly lives in auxiliary ADO components.  This is
one reason projection cannot be treated as innocuous without an oracle test.

## Time-domain result

At `tau=160` the unprojected finite hierarchy has clearly blown up:

```text
RAW
max FDT width error = 1.265838e-1
half nuclear discrepancy vs exact = 2.091937e-1
negative mass = 2.086658e-1
min eig(rho) = -9.614388e-2
```

The projected trajectory remains bounded and trace/Hermiticity preserving:

```text
PROJECTED
trace = 1 to numerical precision
anti-Hermitian relative norm = 1.105e-16
max FDT width error = 8.819886e-5
half nuclear discrepancy vs exact = 9.151817e-4
negative mass = 2.552939e-4
min eig(rho) = -1.145207e-4
```

Thus projection suppresses the exponential spectral instability by orders of
magnitude.

## Split verdict

### Stabilization

```text
trace                  PASS
Hermiticity            PASS
finite bounded state   PASS
no exponential blow-up PASS

STABILIZATION: PASS
```

### Exact open-system oracle

The same thresholds used to certify harmonic Gate B remain the standard:

```text
reference basis error  <1e-7      PASS
max FDT width error    <1e-6      FAIL (8.82e-5)
half nuclear error     <5e-6      FAIL (9.15e-4)
negative mass          <5e-8      FAIL (2.55e-4)

EXACT-ORACLE RECOVERY: FAIL
```

## Interpretation

This test cleanly separates two numerical problems:

1. **spectral pollution / unstable finite-generator modes**, and
2. **finite-hierarchy state error**.

Biorthogonal stable-mode projection solves (1) in this controlled harmonic case.
It does **not** solve (2).  Therefore projection alone is not authorized as a
production nonlinear HEOM method and cannot open Gate C or D.

The result is consistent with the known structure of the problem: deleting
spurious unstable modes does not supply the omitted hierarchy tail needed to
make the finite-depth stationary reduced state quantitatively exact.

## Related stationary-solver results

A direct trace-constrained sparse solve of the finite HEOM nullspace is a valid
way to identify the finite-depth stationary mode, but it likewise does not cure
hierarchy truncation.  The nonlinear dim8,p4,d7 direct LU attempt produced no
state because the hosted runner was externally canceled during factorization;
this is classified as a resource/infrastructure failure, not a physics result.

The attempted block-Jacobi LGMRES fallback is rejected as a solver: on the known
nonlinear dim8,p4,d5 control it stalled at 200 outer iterations with original
HEOM residual `0.525`, constrained residual `0.711`, and trace `0.289`.  It must
not be used for the depth-seven state.

## Gate disposition

```text
Gate A   PASS
Gate B   PASS — original p4,d9 harmonic full-state certification unchanged
Gate C.0 PASS
Gate C.1 ACTIVE — raw propagation rejected; projection stabilizes but is not an
                  exact-state repair; stationary/stronger-closure route unresolved
Gate C.2 BLOCKED
Gate D   BLOCKED ON C
Gate E   BLOCKED
```

No capture-efficiency or publication claim is authorized by this result.
