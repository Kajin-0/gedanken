# Experiment 03 — nonlinear HEOM numerical spectrum check — 2026-08-17

## Purpose

Directly test whether the late-time failure of the finite nonlinear HEOM is
associated with right-half-plane eigenmodes of the finite generator.

Workflow:

```text
run 31998632980
head da17a8c65999d9657b553b0d3f3ed068cb06dcd2
script calculations/heom_nonlinear_rightmost_spectrum.py
```

Both cases use the same physical model, direct-port Padé bath, counterterm,
restricted-left-well construction, and `Npade=4`, `depth=5`.

## Stable time-domain control: dim=8

Job `95294726951`:

```text
full HEOM dimension = 29,568
ARPACK runtime       = 58.800 s

lambda0 = +3.545076e-15 - 3.604528e-15 i
lambda1 = -6.277544647e-2 - 1.150992811 i
lambda2 = -6.277544647e-2 + 1.150992811 i
lambda3 = -1.024990573e-1 - 0.786211622 i
lambda4 = -1.024990573e-1 + 0.786211622 i
lambda5 = -1.241205572e-1
```

No returned mode has positive real part.  There is one stationary zero mode and
the remaining returned modes decay.  This agrees with the previously settled
dim8/depth5 time-domain trajectory.

## Failing time-domain case: dim=10

Job `95294727056`:

```text
full HEOM dimension = 46,200
ARPACK runtime       = 178.956 s
```

The rightmost modes are

```text
lambda1,2 = +0.2926689051 +/- 0.8857378759 i
lambda3,4 = +0.0022946101 +/- 2.4643203731 i
lambda0   = approximately 0
```

The four positive-real eigenpairs have numerical residuals of order `1e-13`.
Thus the finite dim10/depth5 generator itself contains two right-half-plane
conjugate pairs; the time-domain blow-up is not an adaptive-step artifact.

Before reading the dim10 spectrum, the already-recorded negative-mass trajectory
implied transient growth exponents

```text
20 -> 40: 0.32032 per tau
40 -> 50: 0.30089 per tau
```

The directly computed dominant spectral exponent `0.29267 per tau` is close to
this transient estimate.  The difference is not forced to vanish because
negative mass is a nonlinear reduced-state diagnostic and the finite HEOM is
nonnormal/multimode.

## Interpretation

This calculation upgrades the previous classification from an inference to a
direct generator diagnosis:

```text
finite nonlinear hard-cutoff HEOM spectral pathology: DIRECTLY DEMONSTRATED
```

The pathology depends on the finite representation: the dim8/depth5 control has
no positive-real returned mode, whereas dim10/depth5 has four.

This result does **not** authorize deletion or projection of those modes for
production dynamics.  Any stable-mode projection or alternate terminator must
be validated independently before it can be used for Gate C or D.

Current gate status is unchanged:

```text
Gate A   PASS
Gate B   PASS
Gate C.0 PASS
Gate C.1 ACTIVE
Gate C.2 BLOCKED
Gate D   BLOCKED ON C
Gate E   BLOCKED
```
