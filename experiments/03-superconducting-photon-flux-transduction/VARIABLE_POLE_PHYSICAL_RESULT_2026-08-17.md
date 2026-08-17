# Experiment 03 — variable-pole physical coupled-mode result

Date: 2026-08-17

This result is evaluated against the protocol frozen in
`VARIABLE_POLE_PHYSICAL_ACCEPTANCE_2026-08-17.md` at commit
`a5a17a94d89e53c501e600152beccf1f243612ec`, with the exact-C0 initializer
normalization clarified before the run in
`VARIABLE_POLE_INITIALIZER_CLARIFICATION_2026-08-17.md` at commit
`fe758be216bb95e238d40aa25c66d199fadc66a0`.

## Provenance

```text
workflow: .github/workflows/experiment03-variable-pole-physical-opt.yml
run:      32036642965
job:      95408364643
commit:   7e6dfd26bad26c55950062f94e78de63e29754bd
PyTorch:  2.12.1+cpu
```

Automatic classification:

```text
VARIABLE_ACCEPTANCE mandatory=1 primary_pass=1 control_ok=1 finalpass=1
VARIABLE_POLE_PHYSICAL_PASS
```

This is the first independent physical coupled-mode solver in this recovery
program to pass the unchanged harmonic Gate-B full-state thresholds under a
predeclared primary model and over-order robustness control.

## Implementation oracle

The synthetic four-mode implementation oracle passed:

```text
pack/unpack H relative error       = 0
pack/unpack Gamma relative error   = 0
PyTorch vs NumPy transfer error    = 2.90294e-16
autograd derivative               = +4.132914835879e-1
finite-difference derivative       = +4.132914835841e-1
relative gradient discrepancy      = 9.24260e-12
```

The exact 10000-Matsubara direct-port sampler again agreed with independent
quadrature to maximum relative error `2.44531e-9`.

## Exact-C0 initializer normalization

The unique positive coupling rescale required by the frozen exact-C0 gauge was
small:

```text
rank12 scale = 0.9999522400219
rank16 scale = 0.9999653075065
rank24 scale = 0.9999650382295
```

After normalization and full-reorthogonalized Hermitian Lanczos, all gauge
identities were at numerical precision.  For rank16:

```text
||U^dag U-I||_F                     = 8.09e-16
relative H tridiagonalization error = 4.12e-16
relative g alignment error          = 2.65e-17
relative Gamma factorization error  = 1.12e-16
BCF gauge-invariance error           = 3.88e-12
```

No Gamma diagonal shift was required at any tested rank.

## Frozen optimizer behavior

The fixed Adam -> LBFGS schedule strongly reduced the predeclared complex
transfer objective at every rank.  The best iterates occurred during the fixed
LBFGS stage.

```text
rank   J_initial          J_best             objective gain
12     7.29781e-9         2.80258e-11        2.604e2
16     3.84987e-9         2.70104e-11        1.425e2
24     3.90952e-9         2.94718e-11        1.327e2
```

No random restart, schedule change, reweighting, or post-result rank selection
was used.

## Primary rank-16 result

The predeclared primary model passes the unchanged harmonic state gate:

```text
max relative FDT width error = 1.273961081072e-7
half nuclear discrepancy     = 8.540804931657e-8
normalized q-p covariance    = 9.23e-15
```

The individual width errors are

```text
sigma_x relative error = -9.580151760780e-8
sigma_u relative error = +1.273961081072e-7
```

versus the required

```text
max width error < 1e-6
half nuclear    < 5e-6
q-p covariance  < 1e-5.
```

The optimized physical bath remains stable and positive:

```text
Gamma_min                    = +2.057294254587e-9
auxiliary drift max Re       = -6.358215135153e-1
full system drift max Re     = about -6.03449e-2
wide scanned spectrum min    = +1.257503766172e-10
full minimum symplectic nu   = 0.5
```

The exact Gaussian implementation checks remain at numerical precision:

```text
real-drift BCF identity      = 3.21e-13
aux vacuum residual          = 3.79e-17
isolated system-frequency err= 1.76e-11
steady Lyapunov residual     = 3.11e-15
Gaussian rho reconstruction  = 2.09e-15
```

## Independent holdout bath diagnostics

The optimized rank16 model was trained on the frozen complex transfer grids, not
on the time-domain holdout BCF or reduced harmonic density matrix.

Independent holdout:

```text
max |Delta C|/C0             = 2.760192648988e-5
RMS |Delta C|/C0             = 1.853612430847e-6
max normalized spectral error= 1.086127558861e-5
RMS normalized spectral error= 5.093647426375e-6
```

System-band detailed-balance log errors:

```text
x=.50  6.37486e-6
x=1.00 2.68814e-4
x=1.13 2.14308e-5
x=1.50 3.44975e-3
x=2.00 2.42720e-1
```

The residual high-frequency negative-side detailed-balance error remains
explicit; the pass is a harmonic-state validation of this physical
approximation, not a claim of uniformly exact bath representation at all
frequencies.

## Under-order and over-order controls

Rank12 also lands inside the harmonic state thresholds:

```text
max width error = 5.132815610320e-7
half nuclear    = 4.067638117837e-7
```

Rank24:

```text
max width error = 1.985050877007e-7
half nuclear    = 1.293705605882e-7
```

Most importantly, the predeclared rank24 robustness comparison is

```text
0.5 ||rho_24-rho_16||_1 = 6.322825015365e-8
```

versus the required `<5e-6`.

Thus the primary rank16 result is not an isolated order-specific cancellation.

## Scientific interpretation

The preceding recovery sequence localized the controlling representation error:

- raw direct ERA represented the exact BCF extremely accurately but was not
  physical;
- post-fit physical projection imposed an O(1e-5) harmonic-state floor;
- optimizing only the positive-real metric Y with fixed ERA poles did not close
  that floor;
- allowing the physical H/Gamma realization itself to move reduced the primary
  harmonic state error by roughly two orders of magnitude while maintaining
  complete positivity at every iterate.

The variable-pole physical coupled-mode representation is therefore accepted as
an **independent harmonic open-system solver/backend** for the direct-port bath
under the frozen tests.

This does not by itself validate nonlinear detector dynamics.

## Next authorized stage

Gate C may now leave harmonic-method recovery and proceed to the nonlinear cold
metastable-state problem.

Required next actions:

1. recover the later exact nonlinear phase-DVR/full-CPR Hamiltonian code from the
   repository; do **not** use legacy `quantum_initial_capture.py` as the prepared
   quantum state;
2. construct/validate a left-well-conditioned metastable cold state; global
   Gibbs remains invalid as the prepared detector state;
3. couple the nonlinear system to the accepted physical rank16 bath, with rank24
   as the predeclared bath-order control;
4. reintroduce explicit auxiliary local/Fock truncation convergence, because the
   exact Gaussian infinite-bosonic solution used here is no longer available
   once the system is nonlinear;
5. only after the nonlinear cold state is physical, stable, and converged may a
   photon pulse/capture calculation begin.

## Gate status

```text
Gate A   PASS
Gate B   PASS
Harmonic independent-solver recovery   PASS
Gate C.1 nonlinear cold/metastable      ACTIVE
Gate C.2 nonlinear pulse/capture        BLOCKED
Gate D/E downstream comparisons         BLOCKED
Publication                             NO-GO
```
