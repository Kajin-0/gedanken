# Experiment 03 — HEOM boundary localization and harmonic dim12 depth map — 2026-08-17

## Status

```text
Gate A   PASS
Gate B   PASS — harmonic full-state certification unchanged
Gate C.0 PASS
Gate C.1 ACTIVE
Gate C.2 BLOCKED
Gate D   BLOCKED ON C
Gate E   BLOCKED
```

No nonlinear capture or efficiency claim is authorized here.

## 1. Dominant unstable-mode localization

Workflow:

```text
.github/workflows/experiment03-heom-unstable-mode-localization.yml
run 31999615135
script calculations/heom_unstable_mode_localization.py
```

The diagnostic normalizes the dominant right-half-plane eigenvector of the
finite HEOM generator and resolves its squared norm by hierarchy tier and by
retained system energy level.

### Harmonic exact-oracle case: dim12, p4, depth3

Dominant mode:

```text
Re(lambda) = +5.810709e-2 per tau
root/physical ADO weight = 9.205761e-7
terminal hierarchy tier weight = 9.891512e-1
```

System-level localization is comparatively broad:

```text
top retained level weight       = 5.726596e-2
top two levels cumulative       = 1.737370e-1
top three levels cumulative     = 2.716619e-1
mean retained level             = 6.403702 of max 11
```

Thus the harmonic unstable mode is overwhelmingly a **hard hierarchy-boundary
mode**, not primarily a Hilbert-space-edge mode.  More than 98.9% of its norm is
on the terminal hierarchy tier while the physical/root ADO carries less than
1e-6 of the mode norm.

### Nonlinear detector case: dim10, p4, depth5

Dominant mode:

```text
lambda = +0.2926689050665 + 0.8857378759102 i
right-eigenpair residual = 5.042e-13
root/physical ADO weight = 9.509037e-12
terminal hierarchy tier weight = 9.948761e-1
```

Hierarchy-tier weights:

```text
tier0 = 9.5090e-12
tier1 = 9.6147e-10
tier2 = 1.1935e-7
tier3 = 2.2340e-5
tier4 = 5.1014e-3
tier5 = 9.948761e-1
```

Unlike the harmonic oracle, the nonlinear unstable mode is also strongly
localized near the **system-basis boundary**:

```text
top level weight              = 2.170494e-1
top two levels cumulative     = 6.414085e-1
top three levels cumulative   = 8.878851e-1
mean retained level           = 7.712624 of max 9
```

Interpretation:

```text
nonlinear spectral pathology = coupled hierarchy-boundary x Hilbert-boundary mode
```

The hierarchy cutoff is the dominant structural location, but system-basis
resolution is also materially involved.  This explains why enlarging the
retained system basis can reveal a much stronger unstable mode even when
low-order observables at a smaller basis appear converged.

## 2. Harmonic dim12 depth map

Workflow:

```text
.github/workflows/experiment03-heom-harmonic-dim12-depth-map.yml
run 31999375599
```

The purpose is to find whether there exists a finite depth at which the
stationary reduced state is already exact-oracle accurate while the finite
generator remains spectrally unstable.  Such an overlap would be the strongest
possible controlled test bed for stable-mode projection.

### Depth 3 — previously established

```text
rightmost Re(lambda) = +5.810709e-2
finite generator spectrally unstable
stable-mode projection removes blow-up
projected state still fails exact FDT/full-state oracle
```

### Depth 4 — completed here

Job `95296719037`:

```text
dim=12, Npade=4, depth=4
ADOs=210
full HEOM dimension=30,240
```

Spectrum:

```text
rightmost eigenvalue = approximately 0
positive-real returned modes = 0
next relevant pairs all have Re(lambda)<0
returned window reaches Re(lambda)=-9.3084e-2
```

Thus the raw finite generator is already spectrally stable at depth 4.

Direct trace-constrained zero mode:

```text
null residual = 1.29449e-13
trace = 1 to numerical precision
max FDT width error = 3.217545e-6
half nuclear discrepancy vs exact Gaussian = 1.859803e-4
negative mass = 1.033279e-4
min eig(rho) = -6.705718e-5
```

Exact-oracle verdict:

```text
spectral stability: PASS
FDT <1e-6: FAIL
half nuclear <5e-6: FAIL
negative mass <5e-8: FAIL
```

Therefore **spectral stability occurs before physical state convergence**.  This
is an important separation: absence of right-half-plane modes is not a sufficient
HEOM convergence criterion.

It also closes the hoped-for projection overlap at depth 4.  The hierarchy no
longer needs projection for stability, yet its stationary reduced state is still
far outside the accepted harmonic full-state standards.

### Depth 5

At checkpoint commit time the depth-5 job `95296719069` is still running.  Do not
infer its result from runtime.  Record the numerical output before drawing any
additional conclusion.

## 3. Stable-mode projection disposition

The already-completed harmonic dim12,p4,d3 projection test remains:

```text
spectral stabilization: PASS
exact FDT/full-state recovery: FAIL
```

The new depth-4 result explains why: projection removes a shallow-depth spectral
artifact but does not supply the hierarchy tail needed for the correct reduced
state.  By the next raw tier the unstable spectrum is already gone while the
state remains quantitatively wrong.

Therefore:

```text
DO NOT authorize projection alone for nonlinear production dynamics.
DO NOT use spectral stability as a proxy for full-state convergence.
DO NOT cure the nonlinear problem by system-basis enlargement alone.
```

## 4. Published-terminator route

The active diagonal Schur/Nakajima-Zwanzig terminator is structurally the same
class as the diagonal hierarchy terminator derived from Zwanzig projection by
Fay (JCP 157, 054108, 2022): the omitted-ADO resolvent retains the system
Liouvillian rather than replacing it with a scalar fast-modulation rate.

A dedicated exact-oracle test on the unstable harmonic dim12,p4,d3 case is
running as:

```text
script calculations/heom_harmonic_dim12_schur_oracle.py
workflow .github/workflows/experiment03-heom-harmonic-dim12-schur-oracle.yml
run 31999787431
```

The predeclared distinction is:

```text
removing positive spectrum = stability result only
improving/passing exact FDT + full-state metrics = physical closure evidence
```

## Current method conclusion

The strongest current diagnosis is:

1. the raw nonlinear HEOM failure is a genuine finite-generator spectral
   pathology, directly resolved in its eigenvalues;
2. the dominant bad modes are overwhelmingly localized at the hard hierarchy
   boundary;
3. in the nonlinear problem they are also strongly concentrated near the
   retained Hilbert-space boundary;
4. projecting unstable modes can suppress exponential blow-up but does not cure
   finite-hierarchy state error;
5. spectral stability itself can occur one or more depths before the reduced
   state satisfies the exact open-system oracle.

Gate C.1 therefore remains ACTIVE.  The required next method must control both
hierarchy-tail convergence and system-basis convergence; mere spectral
stabilization is insufficient.
