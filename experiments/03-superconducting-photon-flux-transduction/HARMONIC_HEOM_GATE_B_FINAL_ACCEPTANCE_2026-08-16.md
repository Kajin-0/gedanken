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

## Gate disposition at rule-commit time

```text
Gate A: PASS
Gate B: ACTIVE — depth 9 pending
Gate C: BLOCKED ON B
Gate D: BLOCKED
Gate E: BLOCKED
```

## Post-result addendum — depth 9 completed

The predeclared raw-depth matrix completed successfully. The previously unknown
`N_Pade=4, depth=9, dim=8` result is:

```text
workflow run = 31983405446
job          = 95254099060
nexp         = 6
ADO estimate = 5005

rel sigma_x     = -3.417485e-09
rel sigma_u     = -5.033266e-07
max FDT error   =  5.033266e-07
late drift      =  4.768779e-07
trace           =  1.000000000000
min eig(rho)    = -9.172453e-09
top basis pop   = -8.416506e-09
runtime         = 713.786 s
```

Thus the raw hierarchy trend did **not** reverse:

```text
d7 min eig = -4.249847e-7
d8 min eig = -1.504870e-8
d9 min eig = -9.172453e-9
```

Depth 9 also remains inside the predeclared `1e-6` FDT-width tolerance. It
therefore earns the conditional full-state gate; it does **not** by itself pass
Gate B.

The final comparator is:

```text
calculations/heom_harmonic_final_state_gate.py
.github/workflows/experiment03-heom-final-state-gate.yml
run 31984071458
job 95255893597
```

That workflow reran the unmodified `N_Pade=4, depth=9, dim=8` HEOM state and
compared it directly against the exact finite-dimensional squeezed thermal FDT
state under the thresholds fixed above. No clipping or positivity repair was
performed.

## Post-result addendum — final full-state comparator passed

The final comparator completed successfully with workflow verdict
`PASS_GATE_B_HARMONIC`.

```text
exact reference:
  nbar                          = 2.868486916938e-02
  squeeze r                     = 2.564969052866e-01
  finite-basis width error      = 5.036745981981e-09

HEOM state:
  used bath exponents           = 6
  trace                         = 0.9999999999999999
  Hermiticity residual          = 0
  rel sigma_x                   = -5.031023973393e-07
  rel sigma_u                   = -4.821318535816e-07
  max FDT width error           = 5.031023973393e-07
  min eig(rho)                  = -9.172285230002e-09
  total negative mass           = 9.172285230002e-09
  ||rho_HEOM-rho_exact||_1      = 7.570074952352e-07
  0.5 nuclear-norm discrepancy = 3.785037476176e-07
```

The corresponding HEOM eigenvalue spectrum was:

```text
[ 9.72112713e-01,
  2.71159608e-02,
  7.50880084e-04,
  2.09235710e-05,
  6.06564864e-07,
 -4.31574376e-10,
 -6.28960329e-10,
 -8.11290953e-09 ]
```

All predeclared checks passed:

```text
basis error        5.04e-09 < 1.00e-07   PASS
FDT width error    5.03e-07 < 1.00e-06   PASS
0.5 nuclear norm   3.79e-07 < 5.00e-06   PASS
negative mass      9.17e-09 < 5.00e-08   PASS
trace residual                  <1e-10   PASS
Hermiticity residual            <1e-10   PASS
d8 -> d9 sign trend                       PASS
```

No acceptance threshold was changed after the depth-9 or full-state results were
known.

## Final Gate-B disposition

```text
Gate A: PASS
Gate B: PASS — harmonic open-system HEOM solver validated against exact FDT state
Gate C: AUTHORIZED — nonlinear/metastable validation may begin
Gate D: BLOCKED ON C
Gate E: BLOCKED
```

Scope discipline is essential: this Gate-B pass validates the harmonic
open-system numerical method for the certified two-pole bath representation. It
does **not** establish nonlinear metastable equilibrium, interwell escape,
photon-triggered capture, dark rate, or detector performance. Those remain Gate-C
and later questions.
