# Experiment 03 — Harmonic HEOM Gate B Final Acceptance Rule — 2026-08-16

## Purpose

This file fixes the final Gate-B acceptance rule **before** the pending
`N_Pade=4, depth=9` result is read. It exists to prevent post-hoc relaxation of
the harmonic open-system validation criteria.

This is method validation only. It does not authorize nonlinear detector HEOM.

## State when this rule was fixed

Final raw-depth workflow:

```text
.github/workflows/experiment03-heom-pade-final-depth.yml
run 31983405446
```

Results already known when this rule was written:

```text
N_Pade=4, depth=7, dim=8:
  max FDT width error = 6.558955e-7
  min eig(rho)        = -4.249847e-7

N_Pade=5, depth=7, dim=8:
  max FDT width error = 2.637383e-7
  min eig(rho)        = -4.249855e-7

N_Pade=4, depth=8, dim=8:
  max FDT width error = 6.047563e-7
  min eig(rho)        = -1.504870e-8
```

The `N_Pade=4, depth=9` job was still running and its numerical result was not
available when this file was committed.

The depth-7 Padé-order agreement shows that the hierarchy trend is independent
of using four versus five thermal Padé poles. The depth-8 result is the first
adjacent-depth point to reduce the negative tail by another large factor, but it
is not accepted by itself.

## Final raw-depth decision rule

The depth-9 result must continue a stable approach toward the exact positive
Gaussian state. A single accidentally positive tier is not sufficient.

No raw hierarchy depth greater than 9 is authorized for this gate.

If depth 9 materially reverses the depth-8 sign-convergence trend, Gate B stays
open and the next method must be an independent physical embedding or controlled
alternate open-system solver using the same physical admittance `Y(omega)`.

## Conditional full-state gate

Only if the depth-9 result continues the depth-8 trend, rerun the final retained
HEOM state and compare it directly against the exact finite-dimensional squeezed
thermal Gaussian reference constructed from the exact FDT covariance.

The final full-state comparator must satisfy all of the following predeclared
criteria:

```text
exact-reference finite-basis width error  < 1.0e-7
HEOM max relative FDT width error          < 1.0e-6
full-state nuclear-norm discrepancy        < 5.0e-6
total negative eigenvalue mass             < 5.0e-8
```

In addition, the negative-mass/sign behavior must not reverse the established
depth-8 convergence trend.

`0.5 ||rho_HEOM-rho_exact||_1` may be reported as a nuclear-norm discrepancy if
the HEOM state retains any tiny negative eigenvalue. Do not call it a trace
distance unless both compared matrices are valid density operators.

Do not clip, project, renormalize away negative eigenvalues, or otherwise repair
the HEOM reduced state before comparison.

## Gate disposition at commit time

```text
Gate A: PASS
Gate B: ACTIVE — depth 9 pending
Gate C: BLOCKED ON B
Gate D: BLOCKED
Gate E: BLOCKED
```
