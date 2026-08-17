# Experiment 03 — MPDO cutoff-semantics audit freeze

**Date:** 2026-08-17  
**Status:** **FROZEN BEFORE CUTOFF-AUDIT RESULTS**  
**Scope:** small dense implementation oracle only

## Trigger

The exact toy dense oracle at `tau=.001` has nonzero fourth Schmidt components
across its MPS cuts.  Across the first cut, a direct dense SVD gives approximately

```text
s1 = 9.99999966e-01
s2 = 1.83837025e-04
s3 = 1.83837025e-04
s4 = 3.37960529e-08
```

while the original two-site TDVP calculation finishes with bond dimension 3 and
trace error `3.37986635e-08`.

ITensor SVD truncation uses `cutoff` as a bound on the **discarded squared
singular weight** (relative by default).  Thus

```text
s4^2 ~= 1.142e-15 < original cutoff 1e-14,
```

so the observed bond-4 -> bond-3 truncation is consistent with the documented
cutoff rule.  This audit tests that mechanism without changing the physical
model, timestep, TDVP splitting, or oracle thresholds.

## Frozen calculation

Reuse the exact same three-site toy Liouvillian, OpSum/MPO, exact dense reference,
and four-vector globally expanded initial MPDO.

Fix

```text
tau_test      = .001
dt            = 1e-5
nsite         = 2
reverse_step  = true
TDVP order    = 2
maxdim        = 64
normalize     = false
local Krylov tolerance = 1e-13
local Krylov dimension = 30
```

Run the cutoff sequence

```text
1e-12
1e-14
1e-16
1e-18
1e-20
0.0
```

`cutoff=0` is an oracle control, not a proposed production setting.

For the exact dense state at `tau=.001`, report the full Schmidt singular spectrum
for both cuts and the corresponding squared discarded weights.

## Unchanged oracle requirements

```text
half trace distance < 1e-9
trace error         < 1e-10
anti-Hermitian norm < 1e-10
```

## Decision rule

If the oracle failure disappears once the cutoff is below the exact fourth
Schmidt weight while all other settings are unchanged, classify the previous
failure as **tensor truncation semantics**, not a TDVP/non-Hermitian propagation
failure.

A passing cutoff audit does not automatically restore the original production
`cutoff=1e-10/1e-12` settings.  Those settings would be closed as inconsistent
with the required C.1 density-matrix accuracy, and new production cutoffs must be
frozen from this oracle plus the already fixed external physicality/convergence
tolerances before any accepted rank-16 finite-bosonic harmonic run.

If even `cutoff=0` fails the existing oracle thresholds, the cutoff hypothesis is
rejected and the TDVP discriminator remains controlling.

No accepted rank-16 physical harmonic state and no nonlinear C.1 state are used
in this audit.
