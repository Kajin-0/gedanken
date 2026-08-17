# Experiment 03 — TEMPO method-recovery checkpoint

Date: 2026-08-17

## Scope

This checkpoint records the independent influence-functional/TEMPO recovery program for nonlinear Gate C.1 after the conventional finite HEOM hierarchy, stable-mode projection, diagonal NZ/Schur termination, and tested Free-Pole HEOM sequence all failed to provide a controlled nonlinear solver path.

It does **not** promote nonlinear Gate C.1.  Gate C.2, photon-pulse Gate D, and exact-open-vs-TWA Gate E remain blocked.

## Why TEMPO is the active route

The conventional nonlinear HEOM generator has directly resolved right-half-plane spectral pollution.  The dominant unstable mode is overwhelmingly localized at the terminal hierarchy tier and, in the nonlinear high-basis case, also near the retained Hilbert-space boundary.  Projection removes growth but not state error; the diagonal NZ/Schur terminator acts approximately as one effective extra hierarchy tier; the tested FP-HEOM depth sequence is non-monotone in physicality.

TEMPO/PT-TEMPO uses the Feynman-Vernon influence functional directly from the bath correlation and therefore does not rely on a finite HEOM generator spectrum.  OQuPy 0.5 exposes `CustomCorrelations`, so the already validated direct-port correlation can be supplied without refitting a spectral density.

## Frozen TEMPO acceptance rule

See `TEMPO_HARMONIC_ACCEPTANCE_RULE_2026-08-17.md`.

Before any nonlinear use, the actual harmonic direct-port problem must satisfy the existing Gate-B state standards:

```text
finite-basis exact-reference width error < 1e-7
max FDT width error                      < 1e-6
0.5 ||rho_TEMPO-rho_exact||_1            < 5e-6
negative eigenvalue mass                 < 5e-8
trace error                              < 1e-8
relative anti-Hermitian norm             < 1e-8
```

and independent convergence in timestep, memory cutoff, tensor tolerance, bath order, Hilbert basis, late-time equilibration, and initial-state independence.

The thresholds were committed before reading the actual direct-port pilot result.

## Analytic TEMPO interface audits

Two independent pure-dephasing tests validate the OQuPy explicit-correlation convention.

### Real exponential

Corrected workflow run `32001891440`, job `95303666691`:

```text
dt=.10 max relative analytic error = 6.8106978e-14
dt=.05 max relative analytic error = 2.1067632e-13
trace/Hermiticity errors           ~ 1e-13
PASS_TEMPO_IMPLEMENTATION_AUDIT
```

Both grids are below the declared numerical floor, so non-monotonic ordering at ~1e-13 is roundoff/tensor-contraction noise rather than a convergence failure.

### Complex exponential

Workflow run `32001960904`, job `95303850663`:

```text
dt=.10 max relative analytic error = 7.2879212e-14
dt=.05 max relative analytic error = 2.9926655e-13
trace/Hermiticity errors           ~ 1e-13
PASS_TEMPO_COMPLEX_IMPLEMENTATION_AUDIT
```

Thus the positive/negative-time conjugation convention required by the complex direct-port circuit poles is independently validated.

## First finite-system TEMPO-vs-HEOM mapping test

Script:

`calculations/tempo_vs_heom_dim2_mapping.py`

Workflow run `32002662916`, job `95305883162`.

This fixes a tiny dim=2 harmonic system and compares two independent solvers for the same finite open-system problem:

- conventional p4 HEOM depth 6 stationary nullspace;
- direct OQuPy TEMPO with `dt=.2`, `tcut=8`, `tend=32`, `epsrel=1e-8`.

### HEOM reference

```text
nADO          = 924
null residual = 8.265e-14
rho_HEOM      = diag(0.9662706604731, 0.03372933952688)
eigmin        = +0.03372933952688
```

### TEMPO trajectory relative to HEOM

```text
tau=8   half trace distance = 4.7083184e-3
tau=16                       = 2.5105076e-3
tau=24                       = 1.8268709e-3
tau=32                       = 1.6145791e-3
```

The state moves monotonically toward the HEOM stationary state.

At `tau=32`:

```text
late half-distance tau24->32 = 2.1230384e-4
eigmin                       = +0.03534226827411
trace error                   = 3.30029998e-6
relative anti-Hermitian norm  = 5.71979274e-6
```

The job failed the strict mapping guard because trace/Hermiticity were outside `1e-8`.  This is currently classified as a **tensor-accuracy/equilibration diagnostic**, not a bath-mapping falsification, because:

1. the state is positive;
2. it moves monotonically toward the HEOM stationary state;
3. the final solver-to-solver half distance is only `1.61e-3`, well below the gross-disagreement guard `0.02`;
4. the trajectory has not equilibrated by tau=32.

Do not call this mapping PASS until the refinement matrix resolves the numerical and late-time errors.

## Active dim=2 refinement matrix

Script:

`calculations/tempo_vs_heom_dim2_refine.py`

Workflow run `32003044791`:

```text
tol32:   dt=.2, tcut=8,  tend=32, epsrel=1e-10
long64:  dt=.2, tcut=8,  tend=64, epsrel=1e-10
mem64:   dt=.2, tcut=12, tend=64, epsrel=1e-10
```

Current job IDs:

```text
tol32   95306962998
long64  95306962896
mem64   95306963004
```

All were still in progress at this checkpoint.

Interpretation is fixed:

- `tol32` isolates tensor truncation accuracy;
- `long64` tests equilibration at fixed memory;
- `mem64` tests memory-cutoff sensitivity after extending the trajectory.

If the refined TEMPO state plateaus materially away from the HEOM finite-system state, the direct-port mapping/counterterm/interface must be re-examined before any higher-dimensional TEMPO claim.

## Direct-port dim=4 pilots

### Fine pilot

`calculations/tempo_harmonic_direct_port_pilot.py`

Corrected run after the NumPy-1.26 compatibility shim:

```text
run 32002191596
job 95304510522
```

Parameters:

```text
dim=4 bare basis
p4
dt=.20
tcut=8
tend=32
epsrel=1e-8
```

Still in progress at this checkpoint.

### Coarse same-memory control

`calculations/tempo_harmonic_direct_port_coarse.py`

```text
run 32002574182
job 95305627266
```

Parameters:

```text
dim=4 bare basis
p4
dt=.40
tcut=8
tend=24
epsrel=1e-7
```

Still in progress at this checkpoint.

These are only mapping/viability pilots.  Bare dim=4 has finite-reference width error of order `3e-4`, so neither run can pass the harmonic method gate.

At `tcut=8`, the p4 correlation magnitude remains of order 1% of its zero-time value, so memory refinement is mandatory even if the pilots look favorable.

## Harmonic basis optimization

### Covariance-adapted equilibrium basis

`calculations/harmonic_squeezed_basis_audit.py`

Run `32002936662`, job `95306649814`: PASS.

Using the exact equilibrium squeeze `r_eq=0.03329044903832`, the exact reduced state is represented very compactly:

```text
dim3 basis width error = 1.134388e-3
dim4                   = 4.215045e-5
dim5                   = 1.469100e-6
dim6                   = 4.915644e-8
dim7                   = 1.599099e-9
dim8                   = 5.095835e-11
```

At dim6:

```text
top equilibrium population = 1.638548e-8
```

The explicit high-basis unitary squeeze matches the canonical transformed `H,x,u` at ~`2e-16` relative error.

However, a small hard truncation in this basis distorts higher isolated-system levels because the transformed system Hamiltonian is not diagonal in the truncated basis.  Therefore dim6 is **not** promoted as the final dynamical TEMPO basis despite passing the equilibrium-state width criterion.

### Preferred counterterm-renormalized system-normal-mode basis

`calculations/harmonic_system_mode_basis_audit.py`

Run `32003163659`, job `95307305843`: PASS.

For the quadratic system Hamiltonian including the physical counterterm:

```text
Omega_s/omega_c = 1.131080565620
r_sys            = 0.06158671428343
r_eff=r_eq-r_sys = -0.02829626524511
k_ct              = 43.39591671482
```

In this basis:

```text
H = Omega_s (b^dag b + 1/2)
x = sigma0 exp(-r_sys)(b+b^dag)
u = i sigma0 exp(+r_sys)(b^dag-b)
rho_exact = S(r_eff) thermal(nbar) S(r_eff)^dag
```

The system Hamiltonian is exactly diagonal at every retained dimension.

Finite-reference width errors:

```text
dim3  = 3.8571556e-3
dim4  = 2.4430703e-4
dim5  = 1.4707689e-5
dim6  = 8.6684821e-7
dim7  = 5.0661193e-8
dim8  = 2.9509162e-9
dim10 = 9.9700e-12
```

At dim7:

```text
rho eigmin            = +4.5688541e-10
top diagonal population = 6.8504435e-9
H diagonal error      < 9e-16
```

Explicit high-basis unitary transformation:

```text
rel_x = 2.549e-16
rel_u = 2.541e-16
rel_H = 2.437e-16
```

Therefore **system-mode dim7 is the preferred minimum harmonic TEMPO acceptance basis**, with dim8 as the larger-basis control.  This is a representation change only; the physical Hamiltonian and bath are unchanged.

## Conventional dim12/depth5 resource-side partial result

The old conventional harmonic `dim12,p4,depth5` diagnostic run `31999375599`, job `95296719069`, completed its spectrum before an external cancellation during the sparse stationary solve.

Spectrum:

```text
no returned RHP modes
first nonzero pair Re(lambda) = -1.543436197e-2
```

No stationary state was produced.  Do not rerun; it is a nonblocking resource-side partial result and does not alter the already-passed harmonic Gate B.

## Current method disposition

Established:

1. TEMPO real and complex explicit-correlation interfaces pass analytic tests to ~1e-13.
2. First dim2 TEMPO trajectory moves toward the independent HEOM stationary state but is not yet converged and violates strict trace/Hermiticity at `epsrel=1e-8`.
3. A controlled dim2 tolerance/time/memory refinement is in progress.
4. Bare dim4 pilots are in progress and are sanity tests only.
5. A counterterm-renormalized system-normal-mode basis provides an exact diagonal system Hamiltonian and meets the frozen finite-reference criterion at dim7.
6. No nonlinear TEMPO calculation is authorized yet.

Not established:

- TEMPO-vs-HEOM finite-system mapping at controlled tensor/memory/time settings;
- harmonic direct-port exact-state convergence under the frozen matrix;
- p4 vs p5 TEMPO convergence;
- dim7 vs dim8 TEMPO basis convergence;
- initial-state independence;
- nonlinear cold/metastable TEMPO state;
- finite-pulse open-system capture.

## Gate status

- Gate A direct-port bath correlation: PASS
- Gate B harmonic conventional HEOM: PASS
- Gate C.1 nonlinear cold/metastable state: ACTIVE / TEMPO method recovery
- Gate C.2: BLOCKED
- Gate D: BLOCKED
- Gate E: BLOCKED
- Publication: NO-GO
