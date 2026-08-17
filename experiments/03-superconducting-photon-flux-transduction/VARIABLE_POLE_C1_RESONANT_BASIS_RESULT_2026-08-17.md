# Experiment 03 — metastable-window nonlinear C.1 basis result

**Date:** 2026-08-17  
**Scope:** static basis preflight only; no nonlinear open-system dynamics

## Provenance

```text
workflow: .github/workflows/experiment03-variable-pole-c1-resonant-basis-preflight.yml
run:      32041105285
job:      95420446671
head:     2c14d6026fea2faa781c1c369d19ef0921ee4b24
artifact: experiment03-variable-pole-c1-resonant-basis-preflight
ID:       9291966253
sha256:   984a45ccac2fde8e06855295c7cf5ba9bf4683ee47b67dd643d86c92a6899337
```

## Construction

The previously tested lowest-global eigenbasis was rejected because the deeper
right well consumes the low-energy spectrum before the prepared left metastable
state appears.

The replacement basis uses unrestricted full-double-well eigenstates selected
by shift-invert around the physical left quasibound energy

```math
E_{target}=U(x_m)+E_{0,L}.
```

This is still an unrestricted basis: the hard saddle wall is used only to define
the validated left preparation and its target energy.  The retained propagation
states are eigenstates of the full double-well Hamiltonian.

The diagnostic again tested closure of

```text
rho_L
y rho_L       with y=x-x_m
y^2 rho_L     for the directly projected counterterm
P_L           left-basin projector
```

before attaching the open-system bath.

## Result

```text
dim   prep loss       y-image loss     y^2-image loss    P_L
  8   8.82e-7         2.91e-4          2.16e-2           1.000000000000
 12   1.13e-9         6.98e-8          1.11e-5           1.000000000000
 16   8.93e-10        3.86e-9          2.47e-7           1.000000000000
 24   8.81e-10        1.89e-9          5.01e-9           1.000000000000
 32   8.81e-10        1.89e-9          4.96e-9           1.000000000000
 48   8.81e-10        1.89e-9          4.95e-9           1.000000000000
```

The cold projected width is already stable at

```text
sigma_y = 4.06896736e-2
```

from dim12 upward.

The decisive convergence axis is `y^2`, not the bare preparation itself.  A
12-state basis represents `rho_L` extremely well but still loses approximately
`1.1e-5` of the counterterm-applied norm.  At dim16 this drops by about 45x to
`2.47e-7`; at dim24 it drops by another ~49x to `5.01e-9`.

## Frozen detector-basis choice

Before any variable-pole nonlinear open-system result is generated:

```text
PRIMARY nonlinear detector basis = 16 metastable-window full eigenstates
ENLARGED basis control            = 24 metastable-window full eigenstates
```

This gives large static margin relative to the already frozen dynamic
rank16->rank24 detector-basis requirement

```text
0.5 ||rho_s^24-rho_s^16||_1 < 1e-4
|P_L^24-P_L^16|             < 1e-4.
```

Those dynamic thresholds remain unchanged and must still be tested.  Static
closure does not substitute for the open-system basis comparison.

## Decision

```text
LOWEST-GLOBAL BASIS       REJECTED
METASTABLE-WINDOW BASIS   ACCEPTED FOR FIRST C.1 NUMERICAL MATRIX
PRIMARY / CONTROL         16 / 24
```
