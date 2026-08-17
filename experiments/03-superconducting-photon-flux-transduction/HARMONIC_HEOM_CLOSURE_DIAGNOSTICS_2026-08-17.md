# Experiment 03 — harmonic HEOM closure diagnostics — 2026-08-17

## Purpose

This checkpoint records the controlled closure work undertaken after the nonlinear
restricted-left-well raw HEOM hierarchy failed its predeclared depth-seven
convergence discriminator.

The harmonic problem is used only as an exact oracle because its reduced cold
state is independently known from quantum FDT.  Gate B itself remains passed on
the previously certified raw `Npade=4, depth=9, dim=8` calculation.  The work
below asks whether cheaper or more stable hierarchy closures are trustworthy
enough to use in nonlinear Gate C.1.

Current gate disposition:

```text
Gate A   PASS
Gate B   PASS — original harmonic full-state acceptance remains authoritative
Gate C.0 PASS — restricted left-well basis construction
Gate C.1 ACTIVE — raw nonlinear hierarchy rejected; alternate state/closure route active
Gate C.2 BLOCKED
Gate D   BLOCKED ON C
Gate E   BLOCKED
```

## 1. First-order diagonal-tail Schur terminator

The implemented closure follows the finite-dimensional Schur-complement form

```text
L_eff = L_TT - L_Tbar (L'_barbar)^(-1) L_barT,
```

where the discarded-space approximation `L'` keeps the diagonal hierarchy block
of each first omitted ADO.  The implementation is assembled directly from
QuTiP's own depth-`d+1` HEOM RHS, rather than re-deriving bath coefficients or ADO
scalings.

File:

```text
calculations/heom_schur_terminator_harmonic_probe.py
```

Implementation audit on every tested depth:

```text
max | extracted retained block - native QuTiP depth-d RHS | = 0
```

No state clipping, positivity projection, bath change, counterterm change, or
parameter refit is performed.

### Results

All cases are `dim=8`, `Npade=4`.  `maxFDT` is the maximum relative error in the
exact FDT widths.  Negative mass is the sum of the absolute values of negative
eigenvalues of the Hermitian part of the reduced state.

| retained depth | raw maxFDT | raw negative mass / eigmin | Schur maxFDT | Schur negative mass | Schur eigmin |
|---:|---:|---:|---:|---:|---:|
| 2 | 5.11e-4 | positive reduced state | 1.99e-4 | 2.24e-4 | not accepted |
| 3 | 1.988145e-4 | 2.243029e-4 / -1.075005e-4 | 1.554088e-5 | 1.033122e-4 | -6.713689e-5 |
| 4 | 1.553696e-5 | 1.033122e-4 / -6.713690e-5 | 1.081462e-5 | 1.281052e-6 | -6.930675e-7 |
| 5 | 1.081522e-5 | 1.281030e-6 / -6.930644e-7 | 2.624545e-6 | 1.727750e-6 | -6.775696e-7 |

The depth-four Schur result is a strong local improvement in full-state
physicality, but the depth-five negative mass reverses from `1.281e-6` to
`1.728e-6`.  Therefore the favorable depth-four tier cannot be selected as a
converged answer.

The closure also does not satisfy the harmonic full-state standards inherited
from Gate B:

```text
max relative FDT error < 1e-6
total negative mass    < 5e-8
```

## 2. One-effective-tier diagnosis

The first-order diagonal-tail Schur result tracks the next raw hierarchy tier
very closely:

```text
Schur d2 ~ raw d3
Schur d3 ~ raw d4
Schur d4 ~ raw d5
```

The historical Padé workflow provides the decisive d5/d6 comparison:

```text
workflow run 31982972155
raw p4,d6,dim8 job 95252934113
```

Raw depth six:

```text
max FDT error = 2.596516e-6
min eig(rho)  = -8.937236e-7
late drift    = 4.401769e-7
```

Schur depth five:

```text
max FDT error = 2.624545e-6
min eig(rho)  = -6.775696e-7
negative mass = 1.727750e-6
```

The FDT discrepancy differs by only about one percent.  This supports the
interpretation that the first-order diagonal-tail correction mainly supplies an
economical approximation to one additional raw tier.  It is useful, but it is
not presently evidence of a qualitatively stronger convergent closure.

## 3. Direct steady/nullspace diagnostic

A second question is relevant specifically to **cold-state preparation** in Gate
C.1: a finite HEOM generator can contain spurious growing modes while still
possessing a trace-normalized zero mode.  To separate stationary-state accuracy
from propagation stability, the finite raw HEOM nullspace was solved directly:

```text
L v = 0,
Tr(rho_top) = 1.
```

One redundant HEOM row is replaced by the physical trace constraint and the
resulting sparse system is solved directly.  No time propagation or state repair
is used.

File/workflow:

```text
calculations/heom_harmonic_steady_nullspace_probe.py
.github/workflows/experiment03-heom-harmonic-steady-nullspace.yml
run 31997818202
```

### Harmonic results

| raw depth | max FDT error | half nuclear discrepancy vs exact Gaussian | negative mass | eigmin | null residual |
|---:|---:|---:|---:|---:|---:|
| 3 | 1.988145e-4 | 8.836083e-4 | 2.243029e-4 | -1.075005e-4 | 1.21e-14 |
| 4 | 1.554311e-5 | 1.102927e-4 | 1.033122e-4 | -6.713689e-5 | 2.25e-14 |
| 5 | 1.083862e-5 | 4.005215e-5 | 1.281056e-6 | -6.930681e-7 | 5.399e-13 |

Depth-five details:

```text
trace             = 1.000000000000 + 2.72e-15 i
Hermiticity resid = 3.1714e-14
max FDT error     = 1.083862144657e-5
half nuclear      = 4.005215481503e-5
negative mass     = 1.281055574187e-6
min eig           = -6.930681421787e-7
null residual     = 5.399316902648e-13
```

The nullspace solver reproduces the same finite-depth stationary reduced state
seen in stable time propagation.  Thus the lower-depth positivity error is not
an ODE integration artifact and direct zero-mode solution does not itself cure
HEOM truncation.

However, the stationary state improves strongly from depth 3 to 5, and the
linear solve residuals are many orders below the physical discrepancies.  This
means the zero-mode route remains a legitimate **diagnostic/state-preparation
candidate** at deeper nonlinear tiers, provided its own physical state converges.
It does not validate finite-time dynamics and cannot be used to open Gate D.

## 4. Method disposition

### Rejected interpretations

```text
REJECT: choose the favorable Schur depth-four state because its moments look good.
REJECT: treat direct steady-state solution as a positivity repair.
REJECT: infer nonlinear convergence from dim8/dim9 raw depth-six moment agreement.
REJECT: continue raw nonlinear depth escalation after the frozen depth-seven failure.
```

### Active next question

The next falsifiable question for Gate C.1 is:

> Does the nonlinear finite hierarchy possess a trace-normalized stationary zero
> mode that remains physical and converges across hierarchy depth and system
> basis, even though the same finite generator contains spurious growing modes?

The test must first reproduce a known stable nonlinear raw tier as an
implementation control, then interrogate a depth at which propagation is known
to be unstable.  A physical stationary zero mode at one such tier is not enough:
adjacent-depth/system-basis convergence and the frozen Gate-C.1 physicality
thresholds remain mandatory.

If the stationary zero mode is also nonphysical or nonconvergent, the next method
step is a stronger tail treatment (finite-window/full-tail Schur or an independent
projection-based closure), not favorable-tier selection.
