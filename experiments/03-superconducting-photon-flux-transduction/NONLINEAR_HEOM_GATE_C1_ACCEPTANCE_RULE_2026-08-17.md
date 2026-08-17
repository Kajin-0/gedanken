# Experiment 03 — Nonlinear HEOM Gate C.1 acceptance rule — 2026-08-17

## Purpose

This file freezes the acceptance rule for the **cold restricted-left-well nonlinear
HEOM state** before the pending depth-seven basis discriminator is read.

The pending run is:

```text
workflow 31996495432
head     b5f4211e2dd7b6bdfa9c752fefa4c0968de4f24a
cases    dim9_p4d7, dim10_p4d7
```

At the time this rule is committed, both jobs are still in progress and no
numerical depth-seven result has been read.

This rule exists to prevent post-hoc acceptance of a visually plausible stable
trajectory.  Gate C.1 is method/state validation only; it authorizes neither
photon-triggered capture nor detector-efficiency claims.

## Numerical axes already screened

The pilot has already shown that, within the tested range:

```text
Padé order:  Npade 4 -> 5 at dim8/depth5 gives negligible change
DVR domain:  xmin -3.8 -> -3.2 at dim8/depth5 gives negligible change
DVR residuals: O(1e-13 K) or smaller for the relevant retained states
ODE step: dim10/depth5 remains unstable with BDF max_step=0.1
```

The unresolved coupled axes are **system-basis dimension** and **hierarchy
closure depth**.

## Depth-seven discriminator is not itself an acceptance run

The pending depth-seven matrix has three possible dispositions.

### A. dim10 remains unstable

If dim9 is stable but dim10 develops a growing nonphysical mode, or if both are
unstable, Gate C.1 remains ACTIVE and **no depth-eight brute-force run is
authorized**.  The next method step must be a controlled hierarchy
closure/terminator benchmark, first against the exact harmonic FDT oracle.

### B. dim10 is stationary but materially nonpositive

If the dim10 trajectory no longer grows but its final negative mass exceeds the
physicality threshold below, depth seven is classified as a successful
**stability discriminator** but not a Gate-C.1 pass.  One final adjacent-depth
confirmation at dim10/depth8 may be authorized only if the trajectory is
stationary and its observables agree with dim9/depth7 within the provisional
cross-basis thresholds below.

### C. dim9 and dim10 are stationary and mutually consistent

A single final comparator may then be run using dim10/depth8 as the candidate
state.  Gate C.1 can pass only through that comparator; depth seven alone cannot
pass C.1 because dim10/depth6 was unstable and therefore provides no valid
adjacent-depth convergence pair.

## Hard physicality and stationarity thresholds

The candidate final reduced state must satisfy, without eigenvalue clipping,
projection, positivity repair, or post-processing:

```text
|Tr(rho)-1|                         < 1.0e-10
Hermiticity residual                < 1.0e-10
total negative eigenvalue mass      < 5.0e-8
late absolute drift                 < 1.0e-6
|top retained basis population|     < 1.0e-6
```

The negative-mass threshold is deliberately retained from the harmonic Gate-B
full-state acceptance rule rather than relaxed for the nonlinear problem.

`late absolute drift` is the maximum absolute change between the final two
reported times in `<y>`, `sigma_y`, and bare-H0 energy units.

## Cross-basis prerequisite for a final dim10/depth8 run

Before dim10/depth8 is authorized, the stationary depth-seven dim9 and dim10
results must satisfy:

```text
|Delta <y>|                         < 1.0e-5
|Delta sigma_y|                     < 1.0e-5
|Delta bare-H0 energy|              < 1.0e-4
```

These are permissive discriminator thresholds, not final convergence claims.
Their purpose is to ensure that a depth-eight calculation is testing a nearby
candidate solution rather than chasing a qualitatively different branch.

## Final C.1 comparator

If authorized, the final comparator must retain and compare the complete reduced
states for:

```text
reference/control: dim9,  Npade4, depth7
candidate:         dim10, Npade4, depth8
```

The system eigenvectors must be reconstructed on the same DVR grid.  Let `V9`
and `V10` be the common-grid retained eigenvector matrices and

```text
S = V10^dagger V9
rho9_in_10 = S rho9 S^dagger
```

so the dim9 state is embedded into the dim10 physical subspace without relying
on arbitrary eigenvector phase conventions.  The comparator must also report
`||S^dagger S-I||` to verify that the dim9 physical subspace is contained in the
dim10 subspace to numerical accuracy.

The final cross-basis state criteria are:

```text
0.5 ||rho10_d8 - rho9_d7_in_10||_1 < 5.0e-5
|Delta <y>|                         < 5.0e-6
|Delta sigma_y|                     < 5.0e-6
|Delta bare-H0 energy|              < 5.0e-5
subspace isometry residual          < 1.0e-8
```

In addition, the dim10/depth8 candidate itself must satisfy every hard
physicality/stationarity threshold above.

Because dim10/depth6 is invalid, no formal adjacent-depth state norm can be
formed across depths 6 and 7.  The final comparator therefore couples a
hierarchy-refined dim10 candidate to an independently hierarchy-stable lower
system-basis control.  This is intentionally stricter than accepting converged
low-order moments alone.

## Failure rule

Any of the following keeps Gate C.1 open:

- delayed exponential growth at depth seven or eight;
- negative mass above `5e-8` in the candidate final state;
- failure of the common-grid subspace embedding;
- cross-basis full-state discrepancy above `5e-5`;
- nonstationary late-time observables;
- need to alter the bath, counterterm, temperature, restricted-well definition,
  or acceptance thresholds to obtain a pass.

If the raw hierarchy fails this rule, the next path is a controlled hierarchy
closure/terminator.  Do not continue increasing raw hierarchy depth solely until
a desired answer appears.

## Gate disposition at rule-commit time

```text
Gate A: PASS
Gate B: PASS — harmonic HEOM method validation
Gate C.0: PASS — restricted left-well phase-DVR construction
Gate C.1: ACTIVE — depth-seven discriminator pending
Gate C.2: BLOCKED
Gate D: BLOCKED ON C
Gate E: BLOCKED
```
