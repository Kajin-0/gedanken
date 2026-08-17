# Experiment 03 — predeclared dim2 TEMPO memory-bias diagnostic

Date: 2026-08-17

This note is committed before the `tcut=12` direct-TEMPO dim2 results are read.
It is a diagnostic prediction only, not an acceptance criterion or theorem.

## Existing tcut=8 trajectory

For direct TEMPO at

```text
dim=2
p4
dt=.2
tcut=8
epsrel=1e-10
```

the half trace-distance to the independently depth/order-converged conventional-HEOM stationary state is

```text
tau=8   4.712920068e-3
tau=16  2.516985657e-3
tau=24  1.837290172e-3
tau=32  1.625898869e-3
```

A three-parameter descriptive fit

```text
D(t)=D_inf + A exp(-k t)
```

gives approximately

```text
D_inf = 1.532e-3
k     = 0.1465 per tau.
```

This fit is not used as an acceptance model; it only predicts where the fixed-memory trajectory is heading if its late behavior remains single-exponential plus offset.

## Exact direct-port memory-tail fractions

The validated p4 exponential correlation gives

```text
tcut   |integrated signed tail| / |full integral|
8      6.67319e-3
12     5.52458e-4
16     4.46652e-5
20     3.41131e-6
```

The p5 values agree at displayed precision.

## Diagnostic memory-scaling prediction

If the late reduced-state bias is dominated by omitted bath memory and is approximately linear in the small integrated-tail amplitude over this range, then scaling the fitted `tcut=8` plateau by the tail ratios gives rough predictions

```text
tcut=12:  D_inf ~ 1.27e-4
tcut=16:  D_inf ~ 1.03e-5
tcut=20:  D_inf ~ 7.8e-7
```

These numbers are **not** acceptance thresholds and must not be used to force-fit the TEMPO result.  Their only purpose is falsification:

- a `tcut=12` late state near order `1e-4` would support finite-memory bias as the dominant explanation of the `tcut=8` plateau;
- a `tcut=12` late state remaining near `1e-3` would substantially weaken that explanation and require re-examination of mapping/counterterm/interface or other TEMPO systematics;
- regardless of agreement, the frozen full TEMPO harmonic convergence criteria remain unchanged.

Pending direct tests at the time of this note:

```text
mem32: tcut=12, tend=32, run 32004405379
mem64: tcut=12, tend=64, run 32003044791
long64: tcut=8,  tend=64, run 32003044791
```
