# Experiment 03 — frequency-weighted physical-cone fit result

Date: 2026-08-17

This result is evaluated against the rule frozen in
`FREQUENCY_WEIGHTED_PHYSICAL_ACCEPTANCE_2026-08-17.md` at commit
`cb99531bf7780991ee5ff5957984e16499f0a3d8`, before the weighted fit was run.

## Provenance

```text
workflow: .github/workflows/experiment03-frequency-weighted-physical-fit.yml
run:      32035734532
job:      95405614946
commit:   9faab09823c8872794776c8b837e7d9b1fe18be5
```

Automatic classification:

```text
WEIGHTED_ACCEPTANCE mandatory=1 primary_pass=0 control_ok=0 finalpass=0
FREQUENCY_WEIGHTED_PHYSICAL_FAIL
```

Per the frozen stopping rule there is no second weighting choice and no further
fixed-ERA rank/grid scan.

## Objective definition actually used

The fixed convex objective was

```text
J = J_time + J_x + J_u
```

with:

- exact `C(0)` enforced as an affine equality;
- 121 uniform time points on `0<=tau<=24`;
- 241 positive-frequency points on `0.02<=omega/omega_c<=4`;
- `J_x` weighted by the exact harmonic `|chi|^2` sensitivity;
- `J_u` weighted by `x^2 |chi|^2`;
- each spectral sensitivity array normalized to unit sum;
- equal coefficient for all three terms.

The susceptibility weight peaks at

```text
omega/omega_c ~= 1.16425
```

close to the accepted renormalized system mode.

## Mandatory physicality

All optimized ranks remained comfortably physical and numerically controlled.
For example:

```text
rank   Y_min       Q_min        Gamma_min       min scanned S
12     1.2553e-1   5.8362e-5    3.4761e-5       1.7100e-8
16     1.1440e-1   3.0406e-7    2.1451e-7       1.3043e-8
24     1.1735e-1   1.5875e-7    1.1230e-7       1.1452e-8
```

The exact equal-time constraint was satisfied to machine precision.
All real-drift BCF, auxiliary-vacuum, system-frequency, Hurwitz, Lyapunov,
symplectic-uncertainty, and Gaussian-reconstruction checks passed.

Thus the failure is not a convention or complete-positivity failure.

## Coefficient-projection baseline

Before weighted optimization:

```text
rank   max |Delta C|/C0   max FDT width error   half nuclear
12     8.5983e-5          2.0055e-5             1.9577e-5
16     6.2660e-5          1.4511e-5             1.4167e-5
24     6.3203e-5          1.4623e-5             1.4277e-5
```

## Frequency-weighted physical fit

After the predeclared convex optimization:

```text
rank   max |Delta C|/C0   max FDT width error   half nuclear
12     7.7154e-4          5.3961e-5             4.1847e-5
16     5.0380e-4          1.9877e-5             1.4279e-5
24     4.4929e-4          1.2414e-5             8.5501e-6
```

The fit strongly improves detailed balance in the central system band.  For
example at `omega=omega_c`:

```text
coefficient projection E_DB:
rank16 1.3721e-3
rank24 1.3827e-3

weighted physical E_DB:
rank16 2.5538e-4
rank24 6.5298e-5
```

At rank24 the system-state discrepancy also improves materially relative to the
coefficient-projection model.  However the full BCF error becomes much larger
because the fixed objective intentionally spends approximation freedom in the
FDT-sensitive band.

## Why the branch fails

Rank 16 was predeclared as the primary model because the ERA Hankel spectrum had
already saturated by that rank.

Required primary thresholds:

```text
max FDT width error < 1e-6
half nuclear        < 5e-6
```

Observed rank16:

```text
max FDT width error = 1.98774e-5
half nuclear        = 1.42790e-5
```

The nearby rank24 robustness control also fails its predeclared agreement test:

```text
0.5 ||rho_24-rho_16||_1 = 5.87463e-6
required                  < 5e-6
```

Therefore the fixed-state-matrix frequency-weighted route is closed even though
rank24 happened to be better than rank16 on the final state metrics.

## Scientific conclusion

Two distinct fixed-A physicalizations have now failed under predeclared rules:

1. coefficient-space projection `min ||l-Yr||`;
2. direct time/FDT-weighted fitting over `Y` inside the physical cone.

The second method shows that moving the positive-real metric alone can trade
error productively—especially in central detailed balance—but cannot close the
remaining harmonic state gap while retaining global BCF accuracy.

The remaining degree of freedom is therefore the stable realization itself:
**the poles/state matrix must move while passivity is enforced**, rather than
holding the ERA `A` fixed.

The next method class is a genuinely passive rational interpolation/vector-
fitting/network-synthesis realization of the exact positive-real transfer
function, followed by the same exact Gaussian harmonic gate.

Do not reweight this fixed-A objective or reopen ERA ranks/grids.

## Gate status

```text
Gate A   PASS
Gate B   PASS
Gate C.1 ACTIVE / variable-pole passive realization next
Gate C.2 BLOCKED
Gate D   BLOCKED
Gate E   BLOCKED
Publication NO-GO
```
