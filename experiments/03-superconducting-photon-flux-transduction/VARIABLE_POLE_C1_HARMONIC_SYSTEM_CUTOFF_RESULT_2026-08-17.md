# Experiment 03 — variable-pole C1 harmonic system cutoff result

**Date:** 2026-08-17  
**Status:** **PASS / NUMERICAL CHOICES FROZEN BEFORE FINITE-BOSONIC HARMONIC EVOLUTION**

## Purpose

Choose the harmonic detector-site local Fock dimension and asymptotic harmonic
regression horizon using only the already accepted infinite-bosonic Gaussian
rank-16 model.  No nonlinear C.1 state, basin probability, or driven result is
used in this checkpoint.

Workflow:

```text
run:      32061326513
job:      95483042670
artifact: 9298284642
status:   SUCCESS
```

The first workflow attempt failed before Python execution because of a nonexistent
requirements-file path.  The corrected run above reused the exact dependency
installation used by the earlier successful deterministic bath preflight; no
physics input or threshold was changed.

## Exact harmonic reduced state

The accepted rank-16 Gaussian covariance gives

```text
nbar(system)              = 2.985563884985e-02
symplectic nu             = 5.286833671183e-01
normalized q-p covariance = 9.228716704142e-15
Vqq                        = 4.946292942565e-01
Vpp                        = 5.650819834432e-01
Vqp                        = -4.879069021327e-15
Gaussian rho reconstruction error = 2.090715785322e-15
```

## Bare-system Fock tails

The exact Gaussian reduced density matrix was reconstructed in a 96-state bare
harmonic Fock basis.  The probability above candidate local cutoffs is

| retained dimension `d_s` | omitted probability |
|---:|---:|
| 4 | 3.736346965599e-06 |
| 6 | 1.155292395083e-08 |
| 8 | 3.762568034915e-11 |
| 10 | 1.263433802023e-13 |
| 12 | 6.661338147751e-16 |

The finite-bosonic harmonic acceptance thresholds are `1e-5` in maximum relative
width error and `2e-5` in half trace distance.  A `d_s=6` exact reduced-state tail
is therefore already more than three orders below the trace-distance gate scale,
while `d_s=8` supplies a further ~300-fold tail reduction.

Freeze:

```text
HARMONIC SYSTEM PRIMARY local dimension = 6
HARMONIC SYSTEM HIGH control dimension  = 8
```

These are system-site cutoffs only.  The previously frozen auxiliary cutoffs
remain unchanged:

```text
bath PRIMARY: mode0 d=6, modes1..15 d=4
bath HIGH:    mode0 d=8, modes1..15 d=6
```

## Harmonic equilibration horizon

The accepted enlarged-system harmonic drift has

```text
max Re(lambda_drift) = -6.034486723578e-02
gap                  =  6.034486723578e-02
```

The horizon was selected before finite-bosonic propagation as

```text
tau_final = 240
```

for which the slowest linear first-moment exponential factor is

```text
exp(-gap*tau_final) = 5.131138243379e-07.
```

The finite-bosonic regression must still verify explicit late-time stationarity;
this gap estimate is not substituted for that numerical check.

## Disposition

```text
HARMONIC SYSTEM FOCK PREFLIGHT: PASS
system primary/high: 6 / 8
harmonic final horizon: tau=240
```

No full-rank finite-bosonic harmonic result has been generated yet.  The MPDO
propagator implementation oracle remains a separate blocking gate.
