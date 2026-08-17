# Experiment 03 — harmonic dim12 diagonal NZ/Schur terminator oracle — 2026-08-17

## Test

The deliberately unstable harmonic exact-oracle case was used:

```text
dim=12
Npade=4
raw retained depth=3
retained ADOs=84
omitted first tier=126 ADOs
```

The terminator is the already-audited first-omitted-tier Schur/Nakajima-Zwanzig
correction assembled directly from QuTiP's depth-4 HEOM blocks:

```text
L_eff = L_TT - L_Tbar (L'_barbar)^(-1) L_barT
```

with `L'_barbar` retaining the omitted-ADO diagonal blocks, including the system
Liouvillian.  The extracted retained block agrees exactly with the native raw
depth-3 generator (`max difference = 0`).

Workflow:

```text
run 31999787431
job 95297816832
script calculations/heom_harmonic_dim12_schur_oracle.py
```

## Raw depth-3 reference

Spectrum:

```text
6 resolved right-half-plane modes
rightmost pair = +0.0581070887387 +/- 0.208333471937 i
```

Direct stationary state:

```text
max FDT width error = 9.364570e-5
half nuclear discrepancy = 9.103575e-4
negative mass = 2.506610e-4
min eig = -1.124204e-4
```

## Diagonal NZ/Schur terminated depth-3 generator

Spectrum:

```text
4 resolved right-half-plane modes
rightmost pair = +0.0209170221735 +/- 0.874129675358 i
second unstable pair = +0.00219183448542 +/- 2.09057704641 i
stationary zero mode also resolved
```

Thus the published-form diagonal hierarchy terminator **reduces** spectral
pollution but does not eliminate it at this shallow depth:

```text
unstable mode count: 6 -> 4
dominant Re(lambda): 0.0581071 -> 0.0209170
```

Stationary reduced state:

```text
null residual = 4.11224e-14
max FDT width error = 3.217545e-6
half nuclear discrepancy = 1.859803e-4
negative mass = 1.033279e-4
min eig = -6.705718e-5
```

These stationary numbers agree with the independently computed **raw depth-4**
stationary state to numerical precision.  This confirms the earlier
one-effective-tier interpretation for the zero-frequency state.

## Verdict

```text
spectral improvement: PASS
complete spectral stabilization: FAIL
exact-oracle reduced-state recovery: FAIL
```

The diagonal Nakajima-Zwanzig/Schur terminator is therefore retained as a
controlled, literature-grounded acceleration/termination device, but it is not
sufficient to open nonlinear Gate C.1.

The result also strengthens the conceptual split:

1. removing or shifting unstable modes is a spectral-stability problem;
2. recovering the exact reduced state is a hierarchy-tail convergence problem.

A one-tier diagonal tail approximation helps both, but does not solve either to
the required standard in the deliberately difficult dim12/depth3 oracle case.

## Gate status

```text
Gate A   PASS
Gate B   PASS
Gate C.0 PASS
Gate C.1 ACTIVE
Gate C.2 BLOCKED
Gate D   BLOCKED ON C
Gate E   BLOCKED
```
