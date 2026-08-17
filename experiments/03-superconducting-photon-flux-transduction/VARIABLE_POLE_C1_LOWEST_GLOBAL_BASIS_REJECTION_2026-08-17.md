# Experiment 03 — rejection of the lowest-global nonlinear C.1 basis

**Date:** 2026-08-17  
**Scope:** static basis preflight only; no nonlinear open-system dynamics

## Provenance

```text
workflow: .github/workflows/experiment03-variable-pole-c1-nonlinear-basis-preflight.yml
run:      32040956598
job:      95420055640
head:     8669478bc94ea776eac088f096c14a657354cf74
artifact: experiment03-variable-pole-c1-nonlinear-basis-preflight
ID:       9291941015
sha256:   c8f6f4c3a98af2b523801bedeb058d7320d6309e17b86d661f8fef750d8864d3
```

The workflow itself passed its numerical/DVR residual guards.  The scientific
basis diagnostic is a rejection.

## Test

At the certified `.212` operating point, the validated restricted-left thermal
state was embedded into the unrestricted full phase grid.  The first

```text
12,16,24,32,48,64,80,96
```

**lowest-energy global eigenstates** of the tilted double well were then tested
for their ability to represent

1. the prepared left state;
2. its bath-coupling image `y |psi>` with `y=x-x_m`;
3. its counterterm image `y^2 |psi>`.

The basis was also tested against the left-basin projector.

## Result

Every tested global-low basis failed catastrophically.  Representative output:

```text
dim=12  prepLoss=1.000000000000  yLoss=1.000000000000  y2Loss=1.000000000000
dim=48  prepLoss=1.000000000000  yLoss=1.000000000000  y2Loss=1.000000000000
dim=96  prepLoss=1.000000000000  yLoss=1.000000000000  y2Loss=1.000000000000
```

The projected left-basin probability was only numerical roundoff,
approximately `1e-31` to `3e-30`.

Therefore increasing the number of **lowest global** eigenstates from 12 to 96
does not approach the metastable preparation at all.

## Physical interpretation

This is not an eigensolver failure.  It is the expected consequence of the
strongly tilted double well: the right well is energetically favored, so the
lowest global spectrum is populated by right-localized levels long before the
left metastable energy window is reached.

The result is the basis-space version of the already established statement

```text
global Gibbs != prepared detector state.
```

A low-energy global truncation would therefore delete the prepared detector
state before the bath is even attached.

## Decision

```text
LOWEST-GLOBAL-EIGENSTATE BASIS: REJECTED
```

Do not rescue this representation by merely increasing the same low-energy
cutoff post hoc.

The next static preflight shall target the **metastable left-well energy window**
in the unrestricted Hamiltonian using shift-invert around the left quasibound
energy.  The candidate basis must again demonstrate preparation, `y`, `y^2`, and
basin-projector closure before any nonlinear open-system dynamics are run.
