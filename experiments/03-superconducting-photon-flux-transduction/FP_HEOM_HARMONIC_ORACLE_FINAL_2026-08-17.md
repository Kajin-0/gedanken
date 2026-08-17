# Experiment 03 — FP-HEOM harmonic-oracle final disposition

Date: 2026-08-17

## Purpose

This note closes the controlled Free-Pole HEOM (FP-HEOM) method branch opened in `FP_HEOM_HARMONIC_ORACLE_CHECKPOINT_2026-08-17.md`.

FP-HEOM was tested because conventional hard-cutoff HEOM developed explicit right-half-plane spectral pollution localized overwhelmingly on the terminal hierarchy tier.  The FP representation is a genuinely different finite hierarchy with independent forward/backward indices for each complex bath pole while preserving the same direct-port correlation function.

## Implementation validity

The sparse FP generator passed two independent analytic pure-dephasing audits:

```text
real exponential max relative error    = 1.7319251e-15
complex pole max relative error         = 4.7560688e-15
complex-pole max Hermiticity error      = 2.4532695e-18
```

Thus the branch is not rejected because of an unresolved sign, vectorization, conjugation, hierarchy-index, or complex-square-root implementation error.

## Harmonic exact-oracle depth sequence, dim=8, p4

Exact comparison standards remain the Gate-B standards:

```text
max FDT width error   < 1e-6
half nuclear error    < 5e-6
negative mass         < 5e-8
```

### FP depth 1

```text
nADO             = 13
RHP modes         = 0
max FDT           = 5.034059e-2
half nuclear      = 3.661088e-2
negative mass     = 1.335599e-2
eigmin            = -1.287812e-2
```

### FP depth 2

```text
nADO             = 91
RHP modes         = 0
max FDT           = 5.110901e-4
half nuclear      = 6.734458e-3
negative mass     = 0
eigmin            = +2.166128e-5
```

Depth 2 improved strongly and happened to be positive, but remained far outside the exact full-state oracle.

### FP depth 3

Workflow run `32001122799`, job `95301534222`:

```text
nADO             = 455
full dimension    = 29120
RHP modes         = 0
rightmost nonzero pair Re(lambda) = -6.0287004e-2
max FDT           = 1.987595e-4
half nuclear      = 8.837114e-4
negative mass     = 2.243029e-4
eigmin            = -1.075005e-4
null residual     = 1.812e-15
```

Independent stationary-only run `32001521748`, job `95302625337` reproduced the same state to logged precision.

The dominant nonzero FP mode at depth 3 has hierarchy weights

```text
tier 0 = 0.7849151
tier 1 = 0.1890141
tier 2 = 0.02288169
tier 3 = 0.00318921
```

## Predeclared discriminator outcome

The FP branch required coherent adjacent-depth improvement in both the full reduced state and physicality before any dim=12/deeper escalation.

Depth 2 -> depth 3 is **mixed, not coherent**:

```text
max FDT:       5.11e-4 -> 1.99e-4      improves
half nuclear:  6.73e-3 -> 8.84e-4      improves
negative mass: 0        -> 2.24e-4      reverses badly
eigmin:        +2.17e-5 -> -1.08e-4     reverses badly
```

Therefore the predeclared condition for further FP escalation is not met.

## System-basis discriminator already failed at FP depth 2

At dim=12, p4, FP depth 2:

```text
rightmost Re(lambda) = +9.9879648e-2
12/12 returned rightmost modes have positive real part
max FDT              = 1.042821e-4
half nuclear         = 6.734806e-3
negative mass        = 0
```

A positive stationary zero mode therefore coexists with a strongly unstable finite FP generator when the system basis is enlarged.

## Final disposition

**FP-HEOM is correctly implemented but is rejected as the immediate Gate-C.1 recovery solver.**

Specifically:

1. FP depth 3 is spectrally stable at dim 8 but its stationary reduced state is unphysical and fails the exact oracle.
2. FP depth 2 at dim 12 is stationary-positive but dynamically unstable.
3. The dim8 depth sequence is non-monotone in physicality.
4. No dim12 FP depth3 or deeper FP brute-force escalation is authorized.
5. No nonlinear FP-HEOM detector result is authorized from this branch.

This does **not** prove FP-HEOM cannot converge at much larger depth.  It establishes that, under the same falsification-first standard that rejected raw conventional hierarchy escalation, the tested FP sequence does not provide a controlled practical route to Gate C.1.

The independent non-hierarchy TEMPO/influence-functional route is now the active method-recovery candidate and must pass the same harmonic exact-oracle logic before any nonlinear use.

## Gate status

- Gate A direct-port bath correlation: PASS
- Gate B harmonic conventional HEOM: PASS at accepted dim8/p4/depth9 point
- Gate C.1 nonlinear cold/metastable state: ACTIVE / method recovery
- Gate C.2: BLOCKED
- Gate D: BLOCKED
- Gate E: BLOCKED
- Publication: NO-GO
