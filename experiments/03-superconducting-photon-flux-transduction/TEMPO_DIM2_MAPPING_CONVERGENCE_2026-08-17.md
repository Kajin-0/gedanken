# Experiment 03 — direct-TEMPO dim2 mapping convergence

Date: 2026-08-17

## Purpose

This checkpoint records the decisive finite-system validation of the direct OQuPy TEMPO mapping for the Experiment-03 direct-port bath.

It closes the main ambiguity between

1. a wrong bath/counterterm/unit convention, and
2. controllable TEMPO numerical errors from finite timestep, finite memory, and tensor truncation.

The result is **not** a nonlinear Gate-C.1 pass.  It validates only the direct-TEMPO mapping on a tiny dim=2 harmonic finite system against an independently depth/order-converged conventional HEOM reference.

## Independently converged finite-system reference

The conventional p4 HEOM stationary state was separately converged in hierarchy depth through d9 and checked against p5.  The canonical dim2 stationary reference is

```text
rho_ref = diag(0.9662704692933118,
               0.03372953070668817)
```

with p4 d8->d9 population change `6.84e-10` and p5 d8 - p4 d9 change `2.61e-7`.

Therefore HEOM-reference uncertainty is negligible compared with the TEMPO errors discussed below.

## 1. Fixed-memory long-time behavior: tcut=8 reaches a biased stationary state

Direct TEMPO at

```text
dt=.2
tcut=8
tend=64
epsrel=1e-10
```

workflow run `32003044791`, job `95306962896`:

```text
tau=16  half-distance to HEOM = 2.516990606e-3
tau=32                        = 1.625895285e-3
tau=48                        = 1.539715932e-3
tau=64                        = 1.531374503e-3
late drift tau48->64          = 8.341431e-6
```

Numerical physicality at tau64:

```text
trace error = 7.456e-8
anti-Hermitian relative norm = 1.168e-8
eigmin = +3.526068e-2
```

The job is marked failure only because the deliberately strict trace/Hermiticity guard was `1e-8`.

Before this result was read, `TEMPO_DIM2_MEMORY_PREDICTION_2026-08-17.md` fit the earlier tcut8 trajectory to

```text
D(t)=D_inf + A exp(-k t)
D_inf ~ 1.532e-3
k ~ 0.1465/tau.
```

The actual tau64 result `1.5313745e-3` lands essentially exactly on that predeclared plateau.

**Conclusion:** increasing propagation time at fixed `tcut=8` does not remove the discrepancy.  The finite-memory trajectory converges to a biased stationary state.

## 2. Independent HEOM transient relaxation reference

Workflow run `32005167199`, job `95313028293`, conventional p4/depth9 HEOM from the same factorized initial state `|0><0|`:

```text
tau=1   half_to_stationary = 2.66681e-3
tau=2                      = 2.61493e-2
tau=4                      = 7.14137e-3
tau=8                      = 4.50622e-3
tau=16                     = 1.45148e-3
tau=24                     = 4.53258e-4
tau=32                     = 1.41814e-4
tau=48                     = 1.38884e-5
tau=64                     = 1.36535e-6
```

At tau8, before a `tcut=8` TEMPO calculation has discarded any history, direct TEMPO gives `4.7129e-3` to the same stationary state, only ~`2.1e-4` away from HEOM.  After the cutoff begins discarding bath history, the stationary curves separate by order `1e-3`.

This already indicated two different numerical errors: finite timestep before the cutoff acts, and finite-memory bias afterward.

## 3. Full-history TEMPO-vs-HEOM transient mapping

A stronger test compares the entire reduced state directly, with both solvers starting from the same factorized initial state and TEMPO retaining **all** bath history within the simulated interval.

For `tcut=tend=4`, no influence term in `0<=tau<=4` is discarded.

### dt=.20

Workflow run `32005104955`, job `95312854136`:

```text
max 0.5||rho_TEMPO-rho_HEOM||_1 = 4.022613e-4
location                          tau ~1.6
final tau4 distance               2.151731e-4
max trace error                   2.608e-9
max anti-Hermitian norm           1.756e-8
```

The predeclared `2e-4` transient mapping guard was therefore failed at dt=.2.

This did **not** by itself imply a mapping failure because the finite dim2 Hamiltonian does not commute with the bath coupling, unlike the exactly soluble pure-dephasing implementation audits.  A finite Trotter/time-discretization error is therefore expected.

## 4. Timestep refinement shows essentially exact second-order convergence

Script:

`calculations/tempo_vs_heom_dim2_transient_dt.py`

Workflow run `32005259082`.

Holding

```text
tcut=tend=4
p4
dim=2
HEOM depth=9
TEMPO epsrel=1e-10
```

fixed and changing only the timestep gives

```text
dt=.20:
  max half-distance = 4.022613e-4

dt=.10:
  max half-distance = 1.004917015e-4
  final tau4        = 5.370780085e-5
  max trace error   = 4.679e-9
  max anti-Herm     = 2.834e-8

dt=.05:
  max half-distance = 2.510405440e-5
  final tau4        = 1.429496111e-5
  max trace error   = 1.212e-8
  max anti-Herm     = 2.234e-7
```

Successive error ratios are

```text
E(.20)/E(.10) ~ 4.003
E(.10)/E(.05) ~ 4.003
```

Thus the full-history TEMPO-vs-HEOM discrepancy obeys essentially exact

```text
E(dt) proportional to dt^2
```

scaling over two successive halvings.

**This is strong evidence that the direct-port bath, counterterm, coupling normalization, correlation convention, and dimensionless-time mapping are correct.**  A convention mismatch would not naturally collapse with clean second-order timestep refinement over the complete reduced-state trajectory.

## 5. Fine-step tensor truncation is independently controllable

At dt=.05, keeping `epsrel=1e-10` caused accumulated tensor truncation to violate the numerical physicality guard after 80 steps even though the TEMPO-vs-HEOM state discrepancy continued its second-order trend.

Tensor-only refinement was therefore performed at fixed

```text
dt=.05
tcut=tend=4
```

using `calculations/tempo_vs_heom_dim2_transient_eps.py`, workflow run `32005423739`.

### epsrel=1e-11

Job `95313783697`:

```text
max half-distance = 2.509636960e-5
final tau4        = 1.353104753e-5
max trace error   = 1.317e-9
max anti-Herm     = 2.334e-8
```

The physicality guard still narrowly fails because anti-Hermiticity remains above `1e-8`.

### epsrel=1e-12

Job `95313783521`:

```text
max half-distance = 2.509645544e-5
final tau4        = 1.339266590e-5
max trace error   = 2.290e-10
max anti-Herm     = 7.736e-9
PASS_FINE_TEMPO_TENSOR_PHYSICALITY
```

The TEMPO-vs-HEOM discrepancy is unchanged to ~`1e-8` absolute while trace/Hermiticity improve strongly.

Therefore:

1. the ~`2.51e-5` dt=.05 full-history discrepancy is the timestep-discretization floor at this dt, not tensor truncation;
2. tensor numerical physicality is independently controllable by tightening `epsrel`;
3. the timestep and tensor-error axes are successfully separated.

## 6. Finite-memory bias is independently visible

The exact direct-port integrated correlation tail is

```text
tcut=8   |I_tail|/|I_total| = 6.67319e-3
tcut=12                    = 5.52458e-4
tcut=16                    = 4.46652e-5
tcut=20                    = 3.41131e-6
tcut=24                    = 2.53454e-7
```

These are bath-memory diagnostics, not reduced-state error bounds.

A matched exploratory coarse-grid pair at `dt=.4, tend=64, epsrel=1e-8` gives:

### tcut=8

```text
half-distance tau64 = 2.088416e-3
late drift          = 8.81e-6
```

### tcut=20

```text
half-distance tau16 = 1.094716e-3
half-distance tau32 = 6.802954e-4
half-distance tau48 = 6.531108e-4
half-distance tau64 = 6.364183e-4
late drift          = 2.373e-5
```

At the identical coarse timestep, increasing memory from 8 to 20 improves the late state by a factor about `3.28`.

These exploratory jobs use loose tensor tolerance and fail strict trace/Hermiticity guards, so the absolute values are not acceptance results.  The same-grid differential nevertheless demonstrates that memory extension materially removes the late stationary bias.

## 7. Current error decomposition

The dim2 direct-TEMPO data now support a controlled two-error picture:

### Time discretization

With full bath history retained,

```text
TEMPO-vs-HEOM state error proportional to dt^2
```

with max half-distance

```text
4.02e-4 at dt=.2
1.00e-4 at dt=.1
2.51e-5 at dt=.05.
```

### Finite memory

At fixed `tcut=8`, extending time to tau64 converges to a biased state

```text
half-distance ~1.531e-3,
```

while increasing memory to `tcut=20` at a common coarse grid moves the stationary state substantially toward the HEOM reference.

### Tensor truncation

At fixed dt=.05, tightening `epsrel` to `1e-12` restores the strict numerical physicality guard without changing the state-mapping discrepancy.

The three main TEMPO numerical axes are therefore empirically separable.

## Direct-TEMPO mapping disposition

**The direct-TEMPO mapping is validated at the finite dim2 level.**

This statement is intentionally narrow:

- analytic real and complex pure-dephasing interfaces passed at the ~1e-13 numerical floor;
- a noncommuting finite-system full-history trajectory converges to independent HEOM as `O(dt^2)`;
- tensor physicality can be tightened independently;
- late fixed-memory bias is demonstrably sensitive to `tcut` and not removed by longer propagation alone.

This does **not** mean the final harmonic TEMPO gate has passed.

## Next controlled calculation

The next direct-TEMPO task is a **combined** dim2 convergence point using simultaneously:

- fine timestep;
- tensor tolerance strong enough to satisfy numerical physicality;
- long enough memory that the exact direct-port integrated tail is on the required scale;
- enough propagation time to demonstrate late stationarity.

The current evidence suggests `tcut≈20` is the first physically justified long-memory target because its signed integrated tail is `3.4e-6`.  Timestep and tensor settings must be chosen from the demonstrated convergence data rather than guessed.

Only after the combined dim2 state is converged should the method move to the preferred harmonic system-normal-mode basis:

```text
dim7 acceptance basis
finite exact-reference width error = 5.066e-8
```

with dim8 as the larger-basis control.

## Gate status

- Gate A direct-port correlation: PASS
- Gate B conventional harmonic HEOM: PASS
- direct-TEMPO dim2 mapping: VALIDATED
- direct-TEMPO final harmonic exact-state gate: NOT YET PASSED
- Gate C.1 nonlinear cold/metastable state: ACTIVE / blocked on final harmonic TEMPO validation
- Gate C.2: BLOCKED
- Gate D: BLOCKED
- Gate E: BLOCKED
- Publication: NO-GO
