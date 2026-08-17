# Experiment 03 — FP-HEOM harmonic-oracle checkpoint

Date: 2026-08-17

## Scope

This checkpoint records the first controlled Free-Pole HEOM (FP-HEOM) investigation for Gate C.1 method recovery after conventional hard-cutoff HEOM exhibited explicit right-half-plane spectral pollution.  It is a method-validation checkpoint only.  It does **not** promote nonlinear Gate C.1, Gate C.2, or photon-capture Gate D.

The physical bath is unchanged: the same direct-port positive-real environment, the same two exact circuit poles, the same N=4 Bose-Padé thermal terms, the same physical Caldeira-Leggett counterterm, and the same harmonic exact-FDT/Gaussian oracle used to close Gate B.

## Why FP-HEOM was tested

The conventional finite hierarchy showed non-monotone instability with depth and system-basis size.  Direct eigenvector localization then showed that the unstable modes are overwhelmingly concentrated on the terminal hierarchy tier.  The nonlinear detector instability is additionally concentrated at the top retained system levels.

FP-HEOM uses independent forward/backward hierarchy indices for each complex bath pole rather than the conventional folded real/imaginary ADO representation.  It therefore supplies a genuinely different finite hierarchy geometry while preserving the same bath correlation function.

Implementation:

- `calculations/heom_fp_harmonic_oracle.py`
- workflow `.github/workflows/experiment03-fpheom-harmonic-oracle.yml`
- initial workflow run `32001122799`

## Independent implementation audits

Two analytic pure-dephasing tests were added before interpreting the physical FP results.

### Real exponential audit

For

```text
C(t) = d exp(-Gamma t), d=0.2, Gamma=1
```

and `H=0`, `q=diag(0,1)`, the exact coherence is

```text
rho01(t) = rho01(0) exp[-d/Gamma^2 (Gamma t - 1 + exp(-Gamma t))].
```

Workflow run `32001180400`, job `95301689099`:

```text
max relative coherence error = 1.7319251e-15
trace = 1 to displayed precision
PASS_FP_IMPLEMENTATION_AUDIT
```

### Complex-pole audit

A second audit exercised the conjugate forward/backward branches and complex square roots using

```text
d = 0.20 + 0.07 i
z = 1.10 + 0.40 i
```

For `q=diag(0,1)`, the exact `rho01` contains the conjugate influence integral.

Workflow run `32001380919`, job `95302237517`:

```text
max relative coherence error = 4.7560688e-15
max Hermiticity error        = 2.4532695e-18
PASS_FP_COMPLEX_IMPLEMENTATION_AUDIT
```

Therefore the present FP sparse generator has independently validated hierarchy indexing, vectorization convention, forward/backward signs, complex conjugation and square-root normalization.  A physical FP instability should not be dismissed as an untested complex-pole implementation path.

## Harmonic exact-oracle results available so far

Exact reference:

```text
sigma_x = 3.989969857213e-2
sigma_u = 4.264669020793e-2
```

Gate-B comparison standards retained unchanged:

```text
reference basis width error < 1e-7
HEOM max FDT width error     < 1e-6
half nuclear discrepancy    < 5e-6
negative eigenvalue mass    < 5e-8
```

No clipping or positivity repair is applied.

### dim=8, p4, FP depth 1

```text
ncoord = 12
nADO   = 13
rightmost spectrum: zero mode, no resolved positive-real mode
max FDT error       = 5.0340590e-2
half nuclear error  = 3.6610879e-2
negative mass       = 1.3355993e-2
eigmin              = -1.2878121e-2
```

As expected, the shallow hierarchy is physically poor.

### dim=8, p4, FP depth 2

```text
nADO                = 91
rightmost spectrum: zero mode, no resolved positive-real mode
max FDT error       = 5.1109014e-4
half nuclear error  = 6.7344576e-3
negative mass       = 0
eigmin              = +2.1661276e-5
```

Depth 2 gives a major improvement over depth 1 and yields an exactly positive reduced stationary state at numerical precision, but it remains far outside the full-state oracle standard.

Dominant nonzero-mode hierarchy weights:

```text
tier 0 = 0.786817
tier 1 = 0.190507
tier 2 = 0.0226764
```

### dim=12, p4, FP depth 2

The job ended with the predeclared spectral-window guard because all 12 returned rightmost modes remained in the right half plane.  This is a scientific result, not a setup failure.

```text
nADO               = 91
rightmost Re(lambda) = +9.9879648e-2
positive returned modes = 12
min returned Re(lambda) = +3.0905973e-2
max FDT error       = 1.0428209e-4
half nuclear error  = 6.7348060e-3
negative mass       = 0
eigmin              = +9.6694478e-7
null residual       = 6.15e-16
```

Thus the FP depth-2 stationary state is positive while the same finite generator is dynamically unstable once the harmonic system basis is enlarged from 8 to 12 states.

This independently reinforces an earlier methodological result:

> stationary-state positivity and transient spectral stability are separate convergence axes.

A positive trace-normalized zero mode is not sufficient to certify a finite hierarchy for dynamics.

## Current interpretation

FP-HEOM is **implemented correctly but not yet validated as a replacement solver**.

Established:

1. The FP generator passes independent real and complex pure-dephasing analytic audits at ~1e-15 relative accuracy.
2. dim8 depth1 -> depth2 shows strong state improvement.
3. dim8 depth2 is spectrally stable and positive, but full-state inaccurate.
4. dim12 depth2 is stationary-positive but has a strong right-half-plane spectrum.
5. Therefore FP-HEOM does not automatically remove truncation instability under system-basis enlargement.

Not established:

- convergence of dim8 FP depth3;
- whether FP depth can move the dim12 RHP spectrum left while converging the exact state;
- nonlinear FP-HEOM validity;
- any Gate C.1 promotion.

## Pending jobs at this checkpoint

### FP dim8 p4 depth3

Workflow run `32001122799`, job `95301534222` — still in progress when this checkpoint was written.

This is the immediate discriminator.  Do not launch dim12 FP depth3 unless the dim8 depth sequence remains coherent in **both** spectrum and exact-state metrics.

### Conventional harmonic dim12 p4 depth5

Workflow run `31999375599`, job `95296719069` — still in progress when this checkpoint was written.

Do not infer anything from its runtime.

## Gate status

- Gate A direct-port bath correlation: PASS
- Gate B harmonic conventional HEOM: PASS at the already accepted converged dim8/p4/depth9 point
- Gate C.1 nonlinear cold/metastable state: ACTIVE
- Gate C.2: BLOCKED
- Gate D finite-pulse nonlinear capture: BLOCKED
- Gate E exact-open vs TWA: BLOCKED
- Publication: NO-GO
