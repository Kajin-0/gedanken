# Experiment 03 — Nonlinear HEOM Gate-C Pilot Checkpoint — 2026-08-16

## Purpose

This checkpoint records the first cold nonlinear/metastable open-system HEOM
pilot after harmonic Gate B passed.  It is intentionally an **intermediate
method-development record**, not a detector/capture result and not a Gate-C
acceptance declaration.

The objective is to combine:

1. the already accepted restricted-left-well phase-DVR Hamiltonian,
2. the already validated Gate-B direct-port Padé HEOM bath and physical
   Caldeira-Leggett counterterm,
3. the certified representative reduced point `delta=.212`,

and determine which numerical axes must be converged before a prospective
Gate-C.1 acceptance rule is frozen.

## Preconditions already closed

### Harmonic open-system Gate B

`HARMONIC_HEOM_GATE_B_FINAL_ACCEPTANCE_2026-08-16.md` records a full-state pass
against the exact Gaussian FDT reference.  That pass authorizes nonlinear method
validation only; it does not establish detector capture or dark-rate claims.

### Restricted left-well phase-DVR basis

The repaired shift-invert DVR solver with explicit eigenpair residual checks has
already passed across the safe `.212-.213` plateau.  At `.212`:

```text
r = 10.6229699624
C = 24.262211 pF
cold local plasma frequency = 1.984426717 GHz
hbar*omega_m/kB = 0.09523746 K
restricted-well dE01/kB = 0.094183653 K
DVR/harmonic spacing = 0.98893493
```

The accepted detector initialization remains a left-well conditioned/metastable
state, not the global tilted-double-well Gibbs state.

## Pilot implementation

Files:

```text
calculations/heom_nonlinear_leftwell_pilot.py
.github/workflows/experiment03-heom-nonlinear-leftwell-pilot.yml
```

Workflow:

```text
run 31985796103
head 1abbc4ed8c0d96afc2b5bc727da2c6fc8a1a5c3f
```

Physical/numerical choices:

```text
delta = .21200
T = 20 mK
restricted left-well Dirichlet wall = cold saddle
bath = same certified direct-port two-pole Padé bath as Gate B
coupling coordinate y = x-x_m
physical counterterm retained
initial state = bare restricted-well Gibbs state (control/initializer only)
```

The projected physical counterterm uses `P y^2 P`, not `(P y P)^2`, because
projection and squaring do not commute in a truncated eigenbasis.

The bare restricted Gibbs state is **not** treated as the exact stationary target
at finite coupling.  The true reduced stationary state is bath dressed (a
Hamiltonian-of-mean-force state in equilibrium language), so distance from bare
Gibbs is diagnostic rather than an acceptance failure.

## Completed pilot matrix

### 1. Large domain, dim=8, Npade=4, depth=4

```text
job 95260496282
xmin = -3.8
Ngrid = 2200
nexp = 6
ADO estimate = 210
max DVR residual = 3.751e-13 K

final trace = 1.000000000000 - 1.30e-17 i
anti-Hermitian residual = 1.297e-16
min eig(rho) = -8.969624e-05
negative mass = 1.284538e-04
<y> = +2.6116323581e-03
sigma_y = 4.0115076999e-02
bare-H0 energy units = 3.0440586300e-02
top retained population = +4.955744e-06
0.5 nuclear norm from bare restricted Gibbs = 3.526783e-02
late absolute drift = 4.479849e-07
runtime = 33.224 s
```

The trajectory is settled and trace/Hermiticity are excellent, but hierarchy
physicality is not converged at depth 4.

### 2. Large domain, dim=8, Npade=4, depth=5

```text
job 95260496205
nexp = 6
ADO estimate = 462

final trace = 1.000000000000 - 5.95e-17 i
anti-Hermitian residual = 1.189e-16
min eig(rho) = -9.253018e-07
negative mass = 9.968959e-07
<y> = +2.6118022031e-03
sigma_y = 4.0116252752e-02
bare-H0 energy units = 3.0467301249e-02
top retained population = -6.963007e-07
0.5 nuclear norm from bare restricted Gibbs = 3.515747e-02
late absolute drift = 4.367192e-07
runtime = 100.393 s
```

Depth 4 -> 5 reduces total negative mass by about a factor of 129.  This is the
same qualitative hierarchy-convergence pattern seen during harmonic Gate B.

### 3. Large domain, dim=8, Npade=5, depth=5

```text
job 95260496174
nexp = 7
ADO estimate = 792

final trace = 1.000000000000 - 5.83e-17 i
anti-Hermitian residual = 1.169e-16
min eig(rho) = -9.252822e-07
negative mass = 9.966114e-07
<y> = +2.6118012249e-03
sigma_y = 4.0116253141e-02
bare-H0 energy units = 3.0467544673e-02
top retained population = -6.963002e-07
0.5 nuclear norm from bare restricted Gibbs = 3.515774e-02
late absolute drift = 4.101027e-07
runtime = 255.504 s
```

At fixed dim/depth, `Npade=4` and `Npade=5` agree extremely closely:

```text
Delta min eig       = +1.96e-11
Delta negative mass = -2.845e-10
Delta <y>           = -9.782e-10
Delta sigma_y       = +3.89e-10
Delta bare-H0 E     = +2.434e-07
```

Thus Padé order is not the current limiting numerical axis.

### 4. Medium domain, dim=8, Npade=4, depth=5

```text
job 95260496287
xmin = -3.2
Ngrid = 1800

final trace = 1.000000000000 + 2.59e-17 i
anti-Hermitian residual = 2.372e-16
min eig(rho) = -9.252075e-07
negative mass = 9.964374e-07
<y> = +2.6118140183e-03
sigma_y = 4.0116137389e-02
bare-H0 energy units = 3.0467438577e-02
late absolute drift = 4.995008e-07
runtime = 80.071 s
```

Relative to the large-domain dim-8 depth-5 result, the domain change produces
only tiny shifts (approximately `9.4e-11` in minimum eigenvalue, `1.2e-8` in
mean coordinate, and `1.2e-7` in width).  Restricted-domain placement is not the
current limiting axis.

### 5. Large domain, dim=10, Npade=4, depth=5 — numerical instability

```text
job 95260496208
max DVR residual = 6.834e-14 K
```

The trajectory begins near the healthy dim-8 solution:

```text
tau=10:
  <y> = 3.1740977442e-03
  sigma_y = 3.9848960689e-02
  E = 4.0398077873e-02
  min eig = -3.927623e-06
  negative mass = 5.653137e-06

tau=20:
  <y> = 2.6519699716e-03
  sigma_y = 4.0061581639e-02
  E = 3.4214946027e-02
  min eig = -5.599206e-05
  negative mass = 7.421679e-05
```

It then develops a rapidly growing unstable mode:

```text
tau=40  min eig ~ -2.58e-02
tau=80  <y> ~ +4.37e+02, min eig ~ -2.59e+03
tau=120 <y> ~ +4.14e+07
tau=160 <y> ~ -1.29e+13
```

Final trace and negative mass are catastrophically invalid.  This result must
**not** be interpreted as evidence that `dim=8` is physically sufficient, nor as
a physical nonlinear instability.  The DVR eigensystem itself is well
converged; the failure arises only after open-system time propagation and must
be diagnosed as either an integration instability or a finite-tier HEOM
stability problem.

## Active dimension-stability discriminator

To resolve the dim-10 failure, the following diagnostic was added:

```text
calculations/heom_nonlinear_dim_stability.py
.github/workflows/experiment03-heom-nonlinear-dim-stability.yml
run 31986105536
head a05272bf184162d64ee76048aff1b88bfc403d02
```

Predeclared matrix:

```text
dim9,  Npade4, depth5, BDF unchanged
dim10, Npade4, depth4, BDF unchanged
dim10, Npade4, depth5, BDF max_step=0.1
dim10, Npade4, depth5, LSODA max_step=0.1
```

It also records spectral/Frobenius norms of the projected coupling coordinate,
projected physical `y^2`, system Hamiltonian span, and commutator scale.

Interpretation rule:

- if capped BDF and capped LSODA reproduce the same growth, classify the mode as
  a finite-tier HEOM generator instability rather than an ODE-step artifact;
- if both remove the growth and agree quantitatively, classify the original
  trajectory as an integration-step failure;
- dim9 and dim10/depth4 separate basis-threshold effects from hierarchy-depth
  effects.

Do not freeze final Gate-C.1 thresholds until this diagnostic is resolved.

## Current Gate disposition

```text
Gate A: PASS
Gate B: PASS — harmonic HEOM method validation
Gate C.0: PASS — phase-DVR / metastable-basis construction
Gate C.1: ACTIVE — cold nonlinear left-well open-system convergence
Gate C.2: BLOCKED — time-dependent fold passage / conditioned recapture
Gate D: BLOCKED ON C
Gate E: BLOCKED
```

No photon-capture or detector-efficiency claim is authorized by this checkpoint.
