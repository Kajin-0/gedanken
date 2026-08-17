# Experiment 03 — variable-pole C1 current recovery state

**Date:** 2026-08-17  
**Branch:** `agent/nonlinear-c1-preflight-2026-08-17`  
**Authority:** later than the direct-TEMPO-era `OPEN_SYSTEM_CURRENT_STATE_2026-08-17.md`

## Scientific frontier

The accepted variable-pole physical coupled-mode realization has already closed
the independent harmonic open-system recovery gate.  The active question is now
**finite-bosonic implementation validation before nonlinear Gate C.1**.

```text
Gate A                              PASS
Gate B                              PASS
variable-pole physical rank16 bath PASS
rank24 bath-order control           PASS
small dense Lindblad oracle         PASS
small MPDO/MPO mapping oracle       PASS
adaptive-SVD cutoff calibration     PASS
rank16 finite-bosonic harmonic gate ACTIVE
nonlinear C.1                       BLOCKED
photon/capture C.2                  BLOCKED
publication                         NO-GO
```

Do not reopen conventional HEOM, direct TEMPO, ERA physicalization, independent
Lorentzian pseudomodes or bath fitting unless the accepted variable-pole
representation itself fails the frozen nonlinear criteria.

## Fixed operating point

```text
delta=.21200
r_Gamma=10.6229699624
L=111.5 pH
C≈24.262211 pF
T0=20 mK
BETA_COLD=.80
LAMBDA_MIX=.590
```

## Accepted bath

```math
C(\tau)=g^\dagger e^{(-iH_b-\Gamma)\tau}g,
\quad H_b=H_b^\dagger,
\quad \Gamma>0.
```

Primary rank 16, control rank 24.

Rank-16 structure:

```text
H_b is exactly tridiagonal in accepted chain gauge
g couples numerically only to mode 0: ||g[1:]||/||g||≈2.47e-17
Gamma is materially dense:
  off-diagonal fraction ≈ .6445
  beyond-nearest fraction ≈ .5086
```

Therefore the full accepted `Gamma` must be retained.

## Nonlinear system basis already frozen

The lowest global double-well eigenstates are rejected: even 96 such states miss
the prepared metastable-left state essentially completely.

Use unrestricted full-double-well **metastable-window** eigenstates centered on
`U(x_m)+E_0,L`:

```text
PRIMARY nonlinear system basis = 16 states
CONTROL nonlinear system basis = 24 states
```

At 16 states:

```text
preparation loss 8.93e-10
y-image loss     3.86e-9
y^2-image loss   2.47e-7
```

At 24 states the `y^2` loss falls to about `5.01e-9`.

Bath coupling uses

```text
y=x-x_m
```

and the counterterm uses direct projected `P y^2 P`, not `(P y P)^2`.

## Explicit finite-bosonic local dimensions

Bath PRIMARY:

```text
mode 0 d=6
modes 1..15 d=4
```

Bath HIGH:

```text
mode 0 d=8
modes 1..15 d=6
```

Harmonic system PRIMARY/HIGH:

```text
d_s=6 / 8
```

The exact rank-16 harmonic system tails are approximately

```text
d_s=6: 1.1553e-8
d_s=8: 3.7626e-11.
```

## Lindblad convention

With `Gamma=L L^dagger`, collective collapse operators are

```math
c_\mu=\sqrt2\sum_jL^*_{j\mu}b_j,
```

which reproduces

```math
\dot b=(-iH_b-\Gamma)b.
```

Dense oracle errors were `~1e-16` in Kossakowski/first-moment mapping and
`~4.6e-14` in direct propagation.

## MPDO solver selection

Pinned implementation:

```text
Julia 1.11
ITensorMPS 0.4.1
ITensors 0.9.30
vectorized density operator as MPS/MPDO
Liouvillian as MPO
```

The MPO toy generator agrees with independent dense assembly at `~1.7e-16`.

A key numerical finding is that ITensor `cutoff` controls discarded **squared
singular weight**.  The provisional `1e-10/1e-12` production cutoffs are
withdrawn.

Frozen nonzero-cutoff refinement:

```text
largest nonzero toy-oracle pass epsilon_star = 1e-23
PRIMARY production cutoff = 1e-25
TIGHT production cutoff   = 1e-27
```

At `1e-23` the toy oracle gives approximately

```text
half trace = 1.43e-11
trace error= 2.86e-11.
```

At zero SVD truncation standard two-site TDVP is exact to `~1e-15`, proving the
previous failure was truncation rather than a Liouvillian/TDVP defect.

Other controls remain

```text
PRIMARY: dt=.02, maxdim=128, local Krylov tol=1e-11
TIGHT:   dt=.01, maxdim=256, local Krylov tol=1e-13
```

One-site TDVP reproduced the small dense oracle at `~1e-13` and is retained only
as a fallback; no re-expansion schedule has been authorized because adaptive
two-site TDVP remains eligible.

## Harmonic finite-bosonic gate now frozen

File:

`VARIABLE_POLE_C1_FINITE_BOSONIC_HARMONIC_ACCEPTANCE_2026-08-17.md`

Run exactly:

```text
H0 PRIMARY Fock + PRIMARY tensor
H1 PRIMARY Fock + TIGHT tensor
H2 HIGH Fock    + TIGHT tensor
```

from bare vacuum to `tau=240`, reporting `160,200,220,240`.

Each must independently pass:

```text
max relative width error vs exact FDT <1e-5
half trace distance to exact FDT rho  <2e-5
normalized q-p covariance             <2e-5
reduced/full trace physicality gates
late-time stationarity gates
```

and the completed matrix must pass H0/H1 tensor convergence and H1/H2 Fock
convergence.

## Solver-neutral accepted input

Workflow `32062854320` regenerated and exported the accepted rank-16 matrices and
independent FDT target.

```text
artifact: 9298821858
wc      = 1.246852066949e10 s^-1
sigma0  = 4.011572619770e-2
lambda  = 43.39591671482
accepted infinite-Gaussian max width = 1.273961081072e-7
accepted infinite-Gaussian half trace= 8.540804931657e-8
```

The artifact contains plain solver-neutral `H16`, `Gamma16`, `g16`, exact-FDT
rho/covariance and scalar metadata.

## Immediate next operation

The full 17-site physical Liouvillian MPO construction preflight is active.  It
uses the exact accepted rank-16 matrices and both frozen local-Fock classes but
performs no time propagation.

If that construction passes its feasibility check, launch the already frozen
H0/H1/H2 finite-bosonic harmonic matrix.  **Do not enable the nonlinear phase
Hamiltonian until the complete matrix passes.**
