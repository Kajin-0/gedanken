# Experiment 03 — variable-pole physical coupled-mode acceptance

Date: 2026-08-17

## Purpose

The fixed-ERA physicalization branches are closed under predeclared rules:

1. coefficient projection into the coupled-Lindblad cone;
2. frequency/FDT-weighted optimization over the positive-real metric `Y` with
   the ERA state matrix held fixed.

Both remained physical, but neither met the independent harmonic Gate-B state
thresholds.  The remaining realization degree of freedom is therefore the
stable pole/state matrix itself.

This file freezes the first **variable-pole physical-by-construction** test
before implementation or optimization results are seen.

No nonlinear detector dynamics are authorized by this file.

## Physical parameterization

Use the scalar coupled-Lindblad representation

```text
C(tau) = g^dag exp[(-i H-Gamma) tau] g,
H = H^dag,
Gamma >= 0.
```

For each tested order, fix the unitary gauge by Hermitian Lanczos with starting
vector `g/||g||` so that

```text
g = sqrt(C_exact(0)) e1,
H = real symmetric tridiagonal,
```

with positive Lanczos off-diagonal entries.

Parameterize

```text
H_ii          = unrestricted real parameters,
H_i,i+1       = H_i+1,i = exp(b_i) > 0,
Gamma         = L L^dag,
```

where `L` is complex lower triangular with positive real diagonal
`L_ii=exp(d_i)` and unrestricted complex strict-lower-triangular entries.

This makes `Gamma` positive definite and therefore complete positivity automatic
at every optimizer iterate.  No post-fit passivity projection is used.

`g` is fixed, so

```text
C_model(0)=g^dag g=C_exact(0)
```

exactly throughout optimization.

## Predeclared orders

Use the same validated ERA data source and ranks:

```text
rank 12  under-order diagnostic
rank 16  PRIMARY MODEL
rank 24  over-order robustness control
```

Rank 16 is primary because the direct-ERA audit found

```text
sigma_16/sigma_1 = 5.70998e-16,
sigma_24/sigma_1 = 2.83113e-16,
```

so the sampled exact BCF is already numerically rank-saturated by approximately
16 states on the validated grid.

Acceptance will not switch post hoc to whichever order looks best.

## Deterministic physical initializer

For each order:

1. reconstruct the frozen direct ERA realization (`dtau=.05`, `m=512`);
2. solve the already validated coefficient-projection coupled-Lindblad SDP;
3. reconstruct its physical `(H,Gamma,g)` model;
4. apply full-reorthogonalized Hermitian Lanczos to `H` starting from
   `g/||g||`;
5. transform `Gamma` by the same unitary;
6. factor transformed `Gamma` by complex Cholesky.

Before optimization require:

```text
||U^dag U-I||_F                         < 1e-10
||U^dag H U-H_tridiag||_F / ||H||_F    < 1e-10
||U^dag g-sqrt(C0)e1|| / sqrt(C0)       < 1e-10
||U^dag Gamma U-L L^dag||_F/||Gamma||_F < 1e-10
```

and require the gauge-fixed initializer to reproduce the pre-Lanczos physical
BCF on the independent audit grid to maximum relative error `<1e-10`.

If a transformed `Gamma` has a tiny nonpositive eigenvalue from roundoff larger
than `-1e-12`, add only the minimum diagonal shift required to reach
`lambda_min=1e-12` and report it.  Any more negative value is an implementation
failure and blocks that order.

## Exact transfer target

Use the accepted exact direct-port BCF with two circuit poles plus 10000
Matsubara terms in the Gate-B dimensionless coupling convention.

For dimensionless frequency `x=omega/omega_c`, fit the full causal one-sided
transfer

```text
F_exact(x) = integral_0^inf exp(+i x tau) C_exact(tau) d tau
           = sum_k d_k/(z_k-i x).
```

For the physical model

```text
F_model(x) = g^dag [Gamma+i H-i x I]^-1 g.
```

The corresponding unsymmetrized spectrum is `S(x)=2 Re F(x)`.

The full complex transfer is fitted, not spectrum alone, so both dissipative and
causal/dispersive information are constrained.

## Frozen optimization grids and objective

No grid or weight search is allowed.

### Uniform transfer grid

```text
401 uniformly spaced points on -4 <= x <= 6.
```

Define

```text
J_uniform = mean |F_model-F_exact|^2 / |F_exact(0)|^2.
```

### Harmonic sensitivity grids

Use the same accepted exact harmonic susceptibility from the FDT calculation.
On

```text
241 uniformly spaced positive points on 0.02 <= x <= 4,
```

define unit-sum weights

```text
W_x proportional to |chi(x)|^2,
W_u proportional to x^2 |chi(x)|^2.
```

At every positive grid point include both `+x` and `-x` **complex transfer**
errors:

```text
E_pair(x) = [|Delta F(+x)|^2+|Delta F(-x)|^2] /(2 |F_exact(0)|^2),
J_x = sum W_x E_pair,
J_u = sum W_u E_pair.
```

Final objective:

```text
J = J_uniform + J_x + J_u.
```

The optimizer may minimize `1e8 J` for numerical scaling; that constant does not
change the optimum.  Report the unscaled components.

There is no time-domain training term.  Time-domain BCF is an independent
holdout diagnostic after optimization.

## Frozen optimizer

Use CPU PyTorch `torch==2.12.1` with `torch.float64/complex128`.  Complex
PyTorch autograd is supported for complex floating tensors; optimization is
performed on explicit real parameter tensors.

For each order use exactly one deterministic start: the physical initializer
above.  No random restarts.

Optimizer schedule:

```text
Adam:
  steps = 1500
  learning rate = 2e-3
  betas = (0.9,0.999)
  eps = 1e-8

then LBFGS:
  max_iter = 500
  history_size = 100
  tolerance_grad = 1e-12
  tolerance_change = 1e-14
  line_search_fn = strong_wolfe
```

Set `torch.manual_seed(0)` and CPU thread count to 1 for deterministic execution.
No learning-rate schedule, clipping, regularization, early stopping rule, or
parameter bounds may be added after results are seen.

All iterates are physical by construction.  Retain the iterate with the lowest
predeclared objective `J` encountered over the fixed Adam+LBFGS schedule and use
that single best-objective iterate for all holdout and harmonic-state tests.

## Mandatory implementation oracle

Before detector-bath optimization, run a deterministic four-mode synthetic
physical model and verify:

1. pack/unpack reconstruction of `H` and `Gamma` relative Frobenius error
   `<1e-12`;
2. PyTorch and NumPy transfer functions agree to relative error `<1e-11` on the
   frozen frequency grid;
3. one central finite-difference derivative of the scaled objective with respect
   to a predeclared Hamiltonian diagonal parameter agrees with autograd to
   relative error `<2e-5` (or absolute error `<1e-8` if the derivative magnitude
   is below `1e-6`).

Failure is an implementation failure, not a detector result.

## Mandatory holdout reporting

For baseline and optimized models at ranks 12,16,24 report:

- `J_uniform,J_x,J_u,J`;
- eigenvalue ranges of `H` and `Gamma`;
- `Gamma_min`;
- full drift spectral abscissa;
- independent exact BCF error on the prior off-grid midpoint set spanning
  `0<=tau<=51.15`;
- exact spectrum errors on `-4<=x<=6`;
- detailed-balance log error at x=.5,1.0,1.13,1.5,2.0;
- exact Gaussian harmonic state widths, normalized q-p covariance, and half
  nuclear distance to the exact FDT Gaussian state.

The independent holdout BCF and harmonic state are not used in the optimization
objective.

## Mandatory physical/numerical conditions

For every optimized order:

```text
Gamma_min > 0
wide scanned physical spectrum >= -1e-10
BCF real-drift identity < 1e-10
aux vacuum residual < 1e-12
isolated system frequency rel error < 2e-9
full drift max Re(lambda) < -1e-8
steady Lyapunov residual < 1e-10
minimum full symplectic nu >= 0.5-1e-9
system Gaussian reconstruction error < 1e-7
```

Any failure blocks the method.

## Primary harmonic acceptance

Rank 16 is accepted only if

```text
exact reference basis width error < 1e-7
max relative FDT width error      < 1e-6
half nuclear discrepancy          < 5e-6
normalized q-p covariance         < 1e-5
```

and optimization must improve the rank-16 objective relative to its initializer.

## Over-order robustness control

Rank 24 must pass all physical/numerical conditions and satisfy

```text
0.5 ||rho_24-rho_16||_1 < 5e-6.
```

Rank 12 is diagnostic and need not pass the final harmonic thresholds.

## Stopping rule

There is no second optimizer schedule, no second objective weighting, no random
restart, and no post-hoc rank scan.

If the rank-16 primary model misses the unchanged harmonic thresholds, or the
rank-24 robustness control fails, this variable-pole chain-gauge realization is
closed even if it materially improves earlier physical fits.

The next method would require a different exact/passive representation class,
not retuning this optimizer.

## Gate status at freeze

```text
Gate A   PASS
Gate B   PASS
Gate C.1 ACTIVE / variable-pole physical coupled-mode optimization
Gate C.2 BLOCKED
Gate D   BLOCKED
Gate E   BLOCKED
Publication NO-GO
```
