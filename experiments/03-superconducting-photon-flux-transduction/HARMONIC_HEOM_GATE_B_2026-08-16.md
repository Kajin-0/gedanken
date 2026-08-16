# Experiment 03 — Harmonic Direct-Port HEOM Gate B — 2026-08-16

## Purpose

Validate the selected UV-regular direct-port HEOM mapping against the independently known exact cold quantum-FDT covariance **before** applying HEOM to the nonlinear metastable latch.

This is a method-validation checkpoint, not a detector-efficiency result.

## 1. Exact benchmark and model held fixed

Certified `.212` electrical point:

```text
delta       = .212
C           = 24.262211 pF
R           = 7.5308506 ohm
fc          = 1.984426698 GHz
alpha       = omega_D/omega_c = .90
```

Direct port:

```text
Re Y(omega) = (1/R) / [1 + (omega/omega_D)^4]
```

The phase bath correlation is UV regular and has the already-validated two-circuit-pole plus Matsubara decomposition used here.

Exact cold FDT targets:

```text
sigma_x = 3.9899698572e-2
sigma_u = 4.2646690208e-2
```

The Caldeira-Leggett quadratic counterterm is retained so the experimentally defined static phase potential remains unrenormalized. In the dimensionless harmonic solver,

```text
counterterm / omega_c = 43.395916715
```

## 2. Original steady-state implementation — COMPUTATIONALLY REJECTED

The first Gate-B implementation used `HEOMSolver.steady_state()` for a matrix of hierarchy/Matsubara cases.

Workflow:

```text
experiment03-heom-harmonic-port.yml
run 31973895654
job 95230380971
```

The job spent its entire 45-minute CI budget inside the first sparse steady-state solve and was cancelled before producing a physical result.

Disposition:

```text
REJECT steady_state() factorization as the CI strategy.
DO NOT interpret this timeout as a physical HEOM failure.
```

## 3. Staged time-domain replacement

The replacement evolves the HEOM to `tau=120` in units of `omega_c^-1`, more than ten cold phase-amplitude decay times, with late-time drift monitored explicitly. Each convergence axis is an independent CI job.

Primary staged workflow:

```text
experiment03-heom-harmonic-probe.yml
run 31979252567
```

### Results

| dim | N_Mats | depth | CT | rel sigma_x | rel sigma_u | max width err | late drift | min eig(rho) |
|---:|---:|---:|:---:|---:|---:|---:|---:|---:|
| 6 | 8 | 2 | yes | -9.115864e-4 | -1.137463e-3 | 1.137463e-3 | 2.834851e-7 | +2.044258e-4 |
| 6 | 4 | 3 | yes | +1.290002e-3 | +1.541861e-3 | 1.541861e-3 | small | -1.332885e-4 |
| 8 | 4 | 2 | yes | +5.323017e-4 | +5.499520e-4 | 5.499520e-4 | small | +2.197410e-5 |
| 6 | 8 | 3 | yes | +4.839710e-4 | +6.405204e-4 | 6.405204e-4 | small | -1.332862e-4 |
| 6 | 4 | 2 | **no** | +9.161665e-2 | -5.835390e-2 | 9.161665e-2 | small | positive |

The no-counterterm control misses the exact FDT widths by up to 9.16%, whereas the counterterm cases are already sub-0.16%. This is a nontrivial physical discrimination in favor of the intended counterterm convention.

## 4. Combined higher-order point

Workflow:

```text
experiment03-heom-harmonic-final.yml
run 31979346519
```

At `dim=8`, `N_Mats=8`, `depth=3`:

```text
rel sigma_x     = -2.981414e-4
rel sigma_u     = -3.643696e-4
max width error = 3.643696e-4
late drift      = 3.140627e-7
trace           = 1
min eig(rho)    = -1.066899e-4
```

Observable covariance agreement is excellent, but the reduced density matrix is not strictly positive at this truncation.

## 5. Hilbert-basis sweep — positivity defect is not a simple system-basis artifact

Workflow:

```text
experiment03-heom-harmonic-basis-sweep.yml
run 31979429478
```

Fixed `N_Mats=8`, `depth=3`:

```text
dim=8:  min eig(rho) = -1.066899e-4
dim=10: min eig(rho) = -1.152782e-4
```

For `dim=10`:

```text
rel sigma_x     = -2.086396e-4
rel sigma_u     = -3.118642e-4
max width error = 3.118642e-4
runtime         = 18.6 s
```

At `dim=12` the high-energy sector becomes dynamically unstable by the end of the time window:

```text
rel sigma_x  ~ +0.2368
rel sigma_u  ~ +0.7149
min eig(rho) = -6.325389e-3
```

Therefore simply enlarging the oscillator basis does not repair Gate B.

## 6. Independent HEOM/bath-truncation sweep

Workflow:

```text
experiment03-heom-harmonic-truncation-sweep.yml
run 31979513933
```

### `N_Mats=8`, depth 4, dim 10

```text
rel sigma_x     = +1.485187e-4
rel sigma_u     = +1.666663e-4
max width error = 1.666663e-4
late drift      = 2.188050e-7
min eig(rho)    = -6.677187e-5
```

Increasing hierarchy depth improves both covariance and negativity magnitude, but does not restore positivity.

### `N_Mats=16`, depth 2, dim 10

```text
rel sigma_x     = -1.379920e-4
rel sigma_u     = -1.995830e-4
max width error = 1.995830e-4
late drift      = 2.465110e-7
min eig(rho)    = +4.003324e-6
```

This case is positive and accurately reproduces FDT.

### `N_Mats=16`, depth 3, dim 10

```text
nexp            = 18
estimated ADOs  = 1330
rel sigma_x     = -6.639225e-5
rel sigma_u     = -4.659999e-5
max width error = 6.639225e-5
late drift      = 2.095774e-7
trace           = 1
min eig(rho)    = -1.147540e-4
runtime         = 124.148 s
```

The exact-FDT observable widths converge to the `~7e-5` relative level, but the depth-3 reduced state again has a small negative eigenvalue. Thus the positive `N16,d2` result cannot by itself certify the hierarchy.

## 7. Current controlling test — ACTIVE

A pure hierarchy-depth test is running with the same validated bath decomposition and counterterm:

```text
workflow: experiment03-heom-n16d4.yml
run:      31979681514
N_Mats:   16
depth:    4
dim:      8 and 10 in independent jobs
```

Final Gate-B disposition is intentionally withheld until this run completes.

### Acceptance logic

Gate B may be promoted only if the higher hierarchy preserves the already excellent FDT covariance convergence and demonstrates a controlled density-matrix positivity trend across the relevant Hilbert dimensions.

Do **not** weaken the positivity criterion merely because second moments agree.

## 8. If depth 4 does not close positivity

The next repair is the omitted-correlation-tail/terminator problem, not another arbitrary basis increase.

For a finite exponential bath approximation, QuTiP's documented terminator represents the omitted fast correlation by a Markovian double-commutator Liouvillian. For this custom two-pole spectrum, the discrepancy coefficient must be derived from the **actual omitted Matsubara coefficients of this bath** rather than copied from a Drude-Lorentz model.

The corresponding next gate is:

```text
1. compute the custom Matsubara approximation discrepancy from the exact correlation sum rule;
2. add the resulting system terminator while keeping the direct-port spectral density fixed;
3. repeat the harmonic FDT/positivity convergence matrix;
4. only then authorize nonlinear metastable HEOM.
```

## 9. Current disposition

```text
Gate A: direct-port bath correlation             PASS
Gate B: harmonic HEOM versus exact cold FDT      ACTIVE / NOT YET PASSED
Gate C: nonlinear cold/metastable HEOM           BLOCKED ON B
Gate D: finite-pulse nonlinear HEOM              BLOCKED
Gate E: exact/open versus N=8192 TWA             BLOCKED
```

The present evidence is stronger than a simple failure: the HEOM observable covariance is highly accurate and the counterterm is decisively validated, but strict reduced-state physicality has not yet converged. That distinction must be preserved.
