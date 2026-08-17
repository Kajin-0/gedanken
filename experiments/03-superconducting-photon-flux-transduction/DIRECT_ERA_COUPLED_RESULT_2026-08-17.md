# Experiment 03 — direct ERA coupled-realization result

Date: 2026-08-17

This result is evaluated against the criteria frozen in
`DIRECT_ERA_COUPLED_ACCEPTANCE_2026-08-17.md` at commit
`c39d17a4c657a8b223ede5c4fbb77965f1bc1982`, before the first ERA matrix was
run.

## Provenance

```text
workflow: .github/workflows/experiment03-direct-era-coupled-harmonic.yml
run:      32034976681
job:      95403163139
commit:   aaa5f4cab26441c939e903713eeec7a1251a358a
```

Automatic classification:

```text
ERA_ACCEPTANCE have_all=1 mandatory=1 monotone=0 finalpass=0 authorize_refined=0 failures=[]
DIRECT_ERA_FIRST_MATRIX_FAIL
```

The predeclared refined `dtau=.025, m=1024, ranks=24,32` matrix is therefore
**not authorized**.

## Implementation/oracle checks

The ERA implementation passed an exact three-exponential synthetic oracle:

```text
max off-grid relative error = 8.6744e-14
recovered max Re pole       = -0.31
```

The exact 10000-Matsubara direct-port sampler passed independent defining
quadrature:

```text
max relative error = 2.4453e-9
```

Thus the branch did not fail because of the ERA implementation or exact-data
sampler.

## Quasi-ERA fits

The direct nonphysical state-space fits are extremely accurate:

```text
rank    max |Delta C|/|C0|     spectral max abs / S0
12      1.621696e-6             1.466074e-7
16      9.572958e-7             1.043160e-7
24      9.054009e-7             1.033007e-7
```

The Hankel singular values are already near numerical rank saturation by r=16:

```text
sigma_r/sigma_1
r12 = 1.0434e-12
r16 = 5.7100e-16
r24 = 2.8311e-16
```

Therefore increasing raw ERA rank beyond ~16 is largely fitting numerical
subspace directions, not exposing substantial new exact-BCF information on the
frozen grid.

## Physicalized coupled models

The general non-diagonal coupled-Lindblad SDP succeeds and all physicality
checks pass:

```text
rank   rel SDP       Gamma_min       min scanned spectrum
12     1.699394e-4   +1.19682e-8     +1.85373e-10
16     1.240893e-4   +2.06478e-9     +5.73395e-11
24     1.251542e-4   +2.02032e-8     +3.18292e-10
```

Physicalized BCF error:

```text
rank   max |Delta C|/|C0|
12     8.598275e-5
16     6.265984e-5
24     6.320344e-5
```

The physical projection/SDP correction, not the raw ERA approximation, is now
the dominant bath error.

System-band detailed balance remains good near the detector mode.  For example:

```text
E_DB(x=1.0)
rank12 = 1.8962e-3
rank16 = 1.3721e-3
rank24 = 1.3827e-3
```

Again rank24 shows a slight reversal relative to rank16.

## Exact Gaussian harmonic state

All implementation/physicality checks remain at numerical precision:

- BCF real-drift identity: O(1e-13)
- auxiliary vacuum residual: O(1e-17)
- isolated system-frequency error: 1.764e-11
- full Gaussian drift max Re(lambda): about -6.0346e-2
- Lyapunov residual: O(1e-15)
- full minimum symplectic eigenvalue: 0.5
- normalized system q-p covariance: O(1e-14)

Reduced-system state:

```text
rank   max FDT width error      half nuclear discrepancy
12     2.005488e-5              1.957732e-5
16     1.451079e-5              1.416712e-5
24     1.462292e-5              1.427677e-5
```

The r16 -> r24 reversal is small but unambiguous and occurs in all three frozen
monotonic observables: physicalized BCF error, width error, and full-state
nuclear discrepancy.

## Why the refinement is not allowed

The predeclared refinement required, among other conditions:

1. monotonic r16 -> r24 state improvement;
2. r24 physicalized `max |Delta C|/|C0| < 5e-5`.

Neither is satisfied:

```text
r24 state errors are slightly worse than r16
r24 physicalized BCF error = 6.320344e-5 > 5e-5
```

Therefore no `dtau=.025, m=1024` ERA rerun is allowed.

## Scientific conclusion

The direct ERA branch demonstrates that the exact direct-port BCF itself is
very low-rank on the relevant time window and can be represented to ~1e-6 by a
small non-diagonal state-space model.  However forcing that unconstrained model
into the physical coupled-Lindblad cone introduces an O(1e-4) realization
correction that limits the harmonic state to O(1e-5) accuracy.

The bottleneck has therefore been localized more sharply:

**post-fit physicalization is the dominant error, not rational approximation of
the exact BCF.**

The next method should optimize the physical/positive-real realization directly
with the system-relevant spectrum/BCF weighting, rather than fit first and
project afterward.

Per the frozen ERA rule, the next authorized class is a
**frequency-weighted positive-real / coupled-Lindblad realization of the exact
physical spectrum**.

Do not reopen ERA by scanning ranks or grids post hoc.

## Gate status

```text
Gate A   PASS
Gate B   PASS
Gate C.1 ACTIVE / frequency-weighted physical realization next
Gate C.2 BLOCKED
Gate D   BLOCKED
Gate E   BLOCKED
Publication NO-GO
```
