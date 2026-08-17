# Experiment 03 — direct ERA coupled-realization acceptance

Date: 2026-08-17

## Motivation and scope

The Padé-coordinate coupled-Lindblad route was closed by the predeclared p32
stopping rule in `COUPLED_LINDBLAD_HARMONIC_FINAL_RESULT_2026-08-17.md`.

The coupled-Lindblad physicalization and exact Gaussian system solver themselves
were well behaved.  This new branch therefore changes **only the rational
realization coordinates**.

A compact non-diagonal state-space realization is constructed directly from the
exact direct-port BCF by the Eigensystem Realization Algorithm (ERA), then fed
to the same coupled-Lindblad feasibility SDP.

No nonlinear detector dynamics are authorized by this branch.

## Fixed exact-data source

Use the repository's accepted direct-port correlation
`direct_port_bath_correlation.py` with:

```text
2 exact circuit-pole residues
10000 ordinary Matsubara terms
```

and the same coupling/time normalization used by harmonic Gate B:

```text
tau = omega_c t
C_dim(tau) = C_I(tau/omega_c) (Phi_bar/hbar)^2 / omega_c^2.
```

Before ERA, the 10000-term sampler must agree with the independent defining
quadrature at selected times including tau=0 to maximum relative error `<2e-6`.

## Fixed ERA grid

No grid search is allowed in this first matrix.

```text
delta_tau = 0.05
Hankel size m = 512
samples n = 0,...,1023
training horizon = 51.15 tau
```

Construct scalar complex Hankel matrices

```text
H0[i,j] = C((i+j) delta_tau)
H1[i,j] = C((i+j+1) delta_tau)
```

and the standard balanced ERA realization from the SVD of H0.

The tested retained ranks are fixed in advance:

```text
r = 12, 16, 24
```

No r=20/28 or pole hand-editing is allowed after results are seen.

## Mandatory ERA implementation self-test

Before the physical bath, apply the same implementation to a synthetic stable
three-exponential complex correlation with known coefficients/rates.

At exact rank 3 require:

```text
max off-grid relative correlation error < 1e-10
all recovered continuous poles stable
```

A failure is an implementation failure, not a detector result.

## Quasi-realization checks

For each retained rank:

1. discrete ERA eigenvalues must map to continuous rates with
   `max Re(lambda_A) < 0` under the principal matrix logarithm;
2. continuous off-grid BCF comparison is evaluated on a fixed independent
   midpoint/dense grid over `0 <= tau <= 51.15`;
3. report normalized max absolute and RMS BCF errors using exact `|C(0)|`;
4. report exact-spectrum errors over `-4 <= omega/omega_c <= 6` normalized by
   `S_exact(0)`;
5. report detailed-balance log error at x=0.5,1.0,1.13,1.5,2.0.

No quasi-Lindblad representation is promoted directly to system dynamics.

## General coupled-Lindblad SDP

Write the ERA realization as

```text
C_q(tau) = l^dag exp(-i Lambda tau) r
```

with general, non-diagonal `Lambda`.

Use the published coupled-Lindblad feasibility SDP

```text
min ||l-Yr||_2^2
Y > 0
Q(Y)=i(Y Lambda-Lambda^dag Y) >= 0.
```

The scalar input/output gauge must be balanced before the SDP so
`||l||_2 = ||r||_2`; no post-result gauge search is allowed.

For numerical feasibility use the same objective, `Y >= 1e-9 I`, and `Q>=0`.
If CLARABEL returns a constraint violation larger than numerical tolerance, a
predeclared SCS re-solve of the **same SDP** is allowed.  Do not modify poles,
weights, or constraints to force physicality.

Mandatory physicality for an accepted rank:

```text
Y_min       > 0
Q_min       >= -1e-9
Gamma_min   >= -1e-9
wide scanned physical spectrum >= -1e-9
```

## Harmonic-state test

Physicalized ranks 12, 16, and 24 are evaluated with the already validated exact
real-quadrature Gaussian/Lyapunov solver and the exact direct-port FDT reference.

Mandatory convention/numerical checks remain those in
`COUPLED_LINDBLAD_HARMONIC_ACCEPTANCE_2026-08-17.md`:

```text
BCF drift identity < 1e-10
aux vacuum residual < 1e-12
isolated system frequency rel error < 2e-9
full drift max Re(lambda) < -1e-8
steady Lyapunov residual < 1e-10
minimum full symplectic nu >= 0.5-1e-9
system Gaussian reconstruction error < 1e-7
```

## Convergence and final acceptance

Ranks 12 -> 16 -> 24 must improve monotonically in:

```text
physicalized max |Delta C|/|C(0)|
max system FDT width error
half nuclear-norm discrepancy
```

Final harmonic promotion at rank 24 uses the unchanged Gate-B standards:

```text
exact reference basis width error < 1e-7
max relative FDT width error      < 1e-6
half nuclear discrepancy          < 5e-6
normalized system q-p covariance  < 1e-5
```

No threshold may be relaxed.

## One possible refinement, frozen now

If rank 24 does not pass the final state gate but all of the following hold:

1. mandatory implementation/physicality checks pass at ranks 16 and 24;
2. rank 24 improves both state errors over rank 16;
3. rank-24 max width error and half nuclear discrepancy are each `<2e-5`;
4. rank-24 physicalized max `|Delta C|/|C(0)| < 5e-5`;

then one **final grid-refined ERA matrix** is authorized in advance:

```text
delta_tau = 0.025
m = 1024
ranks = 24, 32
```

The final thresholds remain unchanged.

If the first matrix misses those refinement-authorizing conditions, or the
refined matrix misses the final state gate, close direct ERA and move to a
frequency-weighted positive-real realization rather than tuning ERA ranks or
sampling grids post hoc.

## Gate status at freeze

```text
Gate A   PASS
Gate B   PASS
Gate C.1 ACTIVE / direct ERA coupled realization
Gate C.2 BLOCKED
Gate D   BLOCKED
Gate E   BLOCKED
Publication NO-GO
```
