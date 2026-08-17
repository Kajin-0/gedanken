# Experiment 03 — frequency-weighted physical-realization acceptance

Date: 2026-08-17

## Scope

The direct-ERA branch showed that the exact BCF can already be approximated at
~1e-6 by a low-rank unconstrained realization, while post-fit coupled-Lindblad
physicalization introduces ~6e-5 BCF error and ~1.4e-5 harmonic-state error.

This test retains the fixed stable ERA state matrix but changes the optimization
itself: the model is fitted **inside the physical coupled-Lindblad cone**.

No nonlinear detector dynamics are authorized by this test.

## Fixed realization data

Use exactly the first-matrix ERA setup already frozen and validated:

```text
exact BCF: 2 circuit poles + 10000 Matsubara terms
delta_tau = 0.05
Hankel m  = 512
training horizon = 51.15 tau
ranks = 12, 16, 24
```

No new ERA grid or rank search is permitted.

The ERA audit established

```text
sigma_16/sigma_1 = 5.70998e-16
sigma_24/sigma_1 = 2.83113e-16
```

so rank 16 is predeclared as the **primary model**.  Rank 12 is an under-order
control and rank 24 an over-order/numerical-subspace control.  Final promotion
will not switch post hoc to whichever rank happens to look best.

## Physical-cone optimization

For fixed stable continuous ERA matrix `A` and balanced input vector `r`, define

```text
Lambda = i A
C_Y(tau) = r^dag Y exp(A tau) r
```

and require

```text
Y >= 1e-9 I
Q(Y) = i(Y Lambda - Lambda^dag Y) >= 0.
```

These are exactly the coupled-Lindblad physicality constraints used previously.
After solving, factor `Y=X^dag X` and construct

```text
K = X Lambda X^-1
g = X r
H = (K+K^dag)/2
Gamma = (K^dag-K)/(2i).
```

The optimization variable is `Y`; therefore both the time-domain BCF and the
frequency-domain spectrum are affine functions of the optimization variable.
This is a convex SDP/QCQP, not nonlinear pseudomode fitting.

## Exact equal-time constraint

Enforce the exact bath variance as an affine equality:

```text
r^dag Y r = C_exact(0)
```

in the same dimensionless Gate-B coupling convention.  This is physically
natural because a vacuum coupled-Lindblad realization has
`C(0)=g^dag g=r^dag Y r`.

No tolerance/weight tuning of C(0) is allowed.

## Fixed objective

The objective has three equally weighted, separately normalized components:

```text
J = J_time + J_x + J_u.
```

### Time-domain term

Use 121 uniformly spaced points over

```text
0 <= tau <= 24
```

and minimize the mean squared complex BCF error normalized by `|C_exact(0)|^2`:

```text
J_time = mean |C_Y(tau)-C_exact(tau)|^2 / |C_exact(0)|^2.
```

### Physics-derived spectral weights

For positive `x=omega/omega_c`, use 241 uniformly spaced points over

```text
0.02 <= x <= 4.0.
```

The accepted harmonic FDT susceptibility is

```text
chi(omega) = 1 / [K-C omega^2+i omega Y_port(omega)].
```

In dimensionless form the common multiplicative scale is irrelevant.  Define

```text
W_x(x) = |chi(x)|^2
W_u(x) = x^2 |chi(x)|^2
```

and normalize each weight array to unit sum.

For each positive x compare the **symmetrized** spectrum

```text
S_sym(x) = [S(+x)+S(-x)]/2
```

to the exact physical bath.  Let `S0=S_exact(0)`.

```text
J_x = sum W_x_norm(x) [Delta S_sym(x)/S0]^2
J_u = sum W_u_norm(x) [Delta S_sym(x)/S0]^2.
```

Thus the spectral part is weighted directly by the exact sensitivity kernels of
the harmonic position and velocity variances.  There are no empirically tuned
frequency weights.

The three terms enter with equal coefficient 1.  No post-result reweighting is
allowed.

## Solver rule

Use CLARABEL first with tight feasibility/gap tolerances.  If and only if the
returned `Y` or `Q` violates the stated constraints by more than `1e-9`, SCS may
re-solve the **same objective and constraints**.  Do not change the weights,
rank, equality constraint, or physicality floor to obtain feasibility.

## Required reporting

For ranks 12, 16, 24 report:

- optimization status and objective components `J_time,J_x,J_u`;
- `Y_min`, `Q_min`, `Gamma_min`, wide scanned spectrum minimum;
- max/RMS exact BCF error over the prior independent ERA audit grid;
- normalized exact spectrum error over `-4<=x<=6`;
- detailed-balance log error at x=0.5,1.0,1.13,1.5,2.0;
- exact Gaussian harmonic state metrics under the unchanged oracle.

Also report the previous coefficient-projection physical model at each rank as a
baseline, but do not use the baseline to change acceptance.

## Mandatory numerical/physicality conditions

For all three optimized ranks:

```text
Y_min > 0
Q_min >= -1e-9
Gamma_min >= -1e-9
wide scanned spectrum >= -1e-9
BCF real-drift identity < 1e-10
aux vacuum residual < 1e-12
isolated system frequency rel error < 2e-9
full drift max Re(lambda) < -1e-8
Lyapunov residual < 1e-10
minimum full symplectic nu >= 0.5-1e-9
system Gaussian reconstruction error < 1e-7
```

Any violation is a method/implementation failure.

## Primary-model acceptance

Rank 16 is the predeclared primary model.  It passes the independent harmonic
solver gate only if

```text
max relative FDT width error < 1e-6
half nuclear discrepancy     < 5e-6
normalized q-p covariance    < 1e-5
```

with the exact reference basis width error `<1e-7`.

Rank 24 is an over-order control and must satisfy

```text
half nuclear distance(rho_24,rho_16) < 5e-6
```

and must not violate any mandatory physicality condition.  This prevents a
single finely tuned rank-16 result from being accepted without a nearby
higher-order robustness check.

Rank 12 is diagnostic and need not pass the final state thresholds.

## Stopping rule

There is **no second weight choice** and no further fixed-ERA rank/grid scan.

If the primary rank-16 model fails the final harmonic state thresholds, this
fixed-state-matrix frequency-weighted branch is closed, regardless of whether it
improves substantially over the coefficient-projection baseline.

The next method would then need to optimize the stable state matrix/poles as well
as the positive-real metric—e.g. a genuinely passive vector-fitting/network-
synthesis realization—with a new predeclared test.

## Gate status at freeze

```text
Gate A   PASS
Gate B   PASS
Gate C.1 ACTIVE / frequency-weighted physical-cone fit
Gate C.2 BLOCKED
Gate D   BLOCKED
Gate E   BLOCKED
Publication NO-GO
```
