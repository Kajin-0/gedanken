# Experiment 03 — variable-pole nonlinear C.1 coupling clarification

**Date:** 2026-08-17  
**Timing:** committed before any variable-pole nonlinear open-system C.1 result

## Purpose

`VARIABLE_POLE_NONLINEAR_C1_ACCEPTANCE_2026-08-17.md` froze the physical
acceptance metrics and required the nonlinear implementation to preserve the
accepted harmonic coupling/counterterm normalization. Repository recovery of the
later nonlinear HEOM implementation exposes one convention that should be made
explicit before the new solver is written.

This clarification changes no acceptance threshold and is not based on a new
nonlinear result.

## Centered system coordinate

The existing nonlinear implementation

`calculations/heom_nonlinear_leftwell_pilot.py`

uses the centered phase displacement

```math
y=x-x_m,
```

where `x_m` is the cold metastable left minimum.

That is the nonlinear continuation of the local harmonic Gate-B coordinate. A
constant shift of the bath-coupled coordinate corresponds to a bath displacement;
using `y` keeps the nonlinear and harmonic counterterm conventions aligned.

Therefore the variable-pole nonlinear C.1 implementation shall use

```text
system-bath coordinate = y = x - x_m
```

rather than absolute phase `x`.

## Counterterm projection

For a truncated nonlinear system basis with projector `P`, the physical
Caldeira-Leggett counterterm is constructed from the directly projected
multiplicative operator

```math
P y^2 P,
```

not from

```math
(P y P)^2.
```

Projection and squaring do not commute. This distinction is already explicit in
the historical nonlinear HEOM code and is retained here independently of the
failed HEOM hierarchy machinery.

The physical coefficient remains the same direct-port value used throughout the
harmonic validation,

```math
\lambda_{ct}
=\frac{1}{\omega_c}
\frac{\bar\Phi^2}{\hbar}
\frac{G\omega_D}{2\sqrt{2}},
```

in the repository's dimensionless `tau=omega_c t` convention.

## Bath realization

No change is made to the accepted variable-pole bath:

```text
rank 16 = primary
rank 24 = bath-order control
C(tau) = g^dag exp[(-i H_b-Gamma) tau] g
Gamma > 0
```

Only the system operator attached to the accepted bath is clarified as the
centered nonlinear coordinate `y` with the directly projected `y^2`
counterterm.

## Disposition

```text
COUPLING CONVENTION CLARIFIED BEFORE NONLINEAR OPEN-SYSTEM RUN
```
