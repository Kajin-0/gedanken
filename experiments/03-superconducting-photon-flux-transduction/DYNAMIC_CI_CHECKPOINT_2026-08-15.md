# Experiment 03 — Dynamic CI Checkpoint — 2026-08-15

## Purpose

Record the first fully green automated regression checkpoint for the current nonadiabatic Experiment-03 theory stack.

Validated exact science/code head:

```text
8254aa21681a838cefb43707b44fca5576f5e6ca
```

GitHub Actions workflow:

```text
.github/workflows/experiment03-dynamic-rfsquid.yml
```

Validated run:

```text
run ID: 31904479258
job ID: 95060060655
conclusion: SUCCESS
```

## Pinned environment

```text
Python 3.12.13
NumPy 2.5.1
SciPy 1.18.0
```

Dependency file:

```text
calculations/requirements.txt
```

## Passing gates on exact head

All current workflow steps passed:

```text
full nonlinear CPR-RCSJ numerical smoke        PASS
sudden-quench threshold regression             PASS
dark-capture / capacitance elimination         PASS
exact scalar-R damping-window regression       PASS
local saddle-node ghost sensitivity regression PASS
```

The dynamic smoke deliberately guards numerical/structural invariants rather than exact fine-grid capture boundaries. Full-resolution boundary values remain scientific checkpoint outputs.

## Regression history and corrections

The first workflow versions failed for two distinct reasons.

### 1. Test-design error

The initial smoke test asked a deliberately coarse CPR grid to reproduce narrow fine-grid capture-resistance brackets.

That was too brittle and was corrected by separating:

```text
CI numerical invariants
from
full-resolution bifurcation/capture values.
```

This did **not** change the scientific model.

### 2. NumPy 2.5 scalar-conversion compatibility defect

The full solver called `float(...)` on spline return objects that were one-element arrays under the pinned NumPy/SciPy stack. NumPy 2.5 rejected this with

```text
TypeError: only 0-dimensional arrays can be converted to Python scalars
```

The solver now extracts spline scalars explicitly with a robust helper.

After this correction, the full dynamic smoke, sudden-quench and dark-capture regressions passed.

### 3. Critical-damping floating-point cusp

The exact scalar-R damping regression then exposed a numerical issue at

```math
R/R_*=1.
```

Roundoff placed the computed value infinitesimally on the overdamped side, where the square-root formula has a cusp, producing a small amplified error in the regression identity.

The exact critical-damping limit

```math
\tau=1/\omega_0
```

is now handled explicitly. The analytic damping-window result was unchanged.

## Current validation boundary

This green workflow validates implementation consistency of the **current model stack**. It does not validate the model assumptions themselves.

Still provisional/unvalidated physics includes:

```text
shape-only graphene/MoRe interface stress
conditional Huang thermal coefficient mapping
scalar frequency-independent damping R
provisional cubic-MQT rate / Cmin,Q
deterministic rather than stochastic capture
spatially uniform electronic temperature in the full RCSJ solver
absence of readout/backaction and detailed optical absorptance.
```

Therefore this checkpoint must not be described as a validated detector design.

## Change control

Any future change to

```text
full_dynamic_rfsquid.py
quench_energy_bound.py
eliminated_dark_capture_closure.py
rcsj_damping_window.py
dynamic_fold_ghost.py
or their shared physical assumptions
```

must obtain a fresh green run before the resulting numerical state is called a validated Experiment-03 code checkpoint.

## Status

**NUMERICAL REGRESSION STACK: PASS at `8254aa21681a...`.**

**SCIENTIFIC PROGRAM: GO for continued theory. NO-GO for manuscript.**
