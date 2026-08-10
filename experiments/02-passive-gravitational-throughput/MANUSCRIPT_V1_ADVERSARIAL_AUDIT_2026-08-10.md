# Manuscript V1 Adversarial Scope Audit — 2026-08-10

**Target:** `manuscript_v1/` on the real `main` branch after the first complete short-manuscript build.  
**Role:** hostile proof/scope reader.  
**Question:** does the manuscript state exactly the theorem that the repository derivations actually prove, without silently broadening the frequency or geometric class?

## Verdict

**PASS WITH REQUIRED SCOPE HARDENING.**

No defect was found in the recovered `25/12` coefficient or in the algebraic combination

```math
(25/16)\times(4/3)=25/12.
```

Three manuscript statements required tightening before the paper could be treated as an internally frozen statement of the proved result.

## 1. Retained modal-sector condition

### Problem

The endpoint resource is

```math
\sum_n\kappa_{g,n}
\le
\frac{4G}{3c^5}I_2\Omega^4,
```

for a retained sector whose physical modal frequencies satisfy `omega_n <= Omega`. The narrowband replacement

```math
Omega = omega_0[1+O(B/omega_0)]
```

therefore applies only to an effective modal sector whose gravitationally relevant physical frequencies are bounded at the carrier scale.

A generic narrowband transfer measurement can in principle contain off-resonant tails from modes with `omega_n >> omega_0`. Those modes are not controlled by replacing their `omega_n^4` gravitational rates with `omega_0^4` merely because the observed envelope bandwidth is small.

### Resolution

The theorem must explicitly refer to the **retained near-carrier Markov modal sector**. Higher-frequency off-resonant sectors are outside the simple `omega_0^4` closure unless their contribution is separately bounded.

This is a scope clarification, not a coefficient change.

## 2. Quantified compactness and wave-zone conditions

### Problem

The manuscript used the words `compact` and `wave zone`, but the TT derivation actually requires the endpoint sizes to be small relative to the carrier wavelength and the separation to be large relative to it.

### Resolution

Introduce characteristic endpoint radii `a_A,a_B` and state

```math
k_0 a_A \ll 1,
\qquad
k_0 a_B \ll 1,
\qquad
k_0R \gg 1,
\qquad
k_0=\omega_0/c.
```

The `25/16` coefficient is the retained leading compact-quadrupole separated-wave-zone coefficient under these conditions.

## 3. Band-limited metric versus full-line H2 norm

### Problem

The manuscript defines

```math
\Gamma_{\rm coh}
=\frac1{2\pi}\int_{\mathcal B_\nu}
\operatorname{Tr}(T^\dagger T)d\nu,
```

but derives the standard selected-port `H2` identity over the full real detuning line. The transition from the full-line identity to the band-limited theorem was correct but implicit.

### Resolution

State explicitly that the integrand is nonnegative, so the band integral is bounded by the full-line `H2` norm. Then use pointwise passivity/contractivity of the opposite endpoint and the propagation operator to obtain the source and receiver cuts.

This makes the proof chain explicit:

```math
\Gamma_{\rm coh}
\le \eta_{\max}\|H_A\|_2^2
\le \eta_{\max}\operatorname{Tr}(K_{g,A}^\dagger K_{g,A}),
```

and independently

```math
\Gamma_{\rm coh}
\le \eta_{\max}\|H_B\|_2^2
\le \eta_{\max}\operatorname{Tr}(K_{g,B}^\dagger K_{g,B}).
```

## 4. Items rechecked and retained

The audit rechecked the following manuscript claims against the repository proof spine:

- `Gamma_coh` is a complex-envelope spectral area with units `s^-1`, not a capacity;
- the finite-dimensional passive cut uses all physical loss/radiation ports in the passive dilation;
- the `20/3` Bessel resource and `4/3` gravitational trace coefficient are proof lemmas, not novelty claims;
- the compact TT directivity bound is `D <= 5/2` and yields the leading `25/16` propagation coefficient;
- the final coefficient is `25/12` after substituting `k_0=omega_0/c`;
- the infinite-dimensional extension remains restricted to separable bounded-port Markov modal sectors with a Hilbert-Schmidt gravitational port;
- the recurrence statement is an upper-bound statement only; destructive interference can lower actual recurrent transfer;
- added relays, external cavities, extended apertures, near-field transfer, active feedback, unbounded PDE ports, and genuinely non-Markov continua remain excluded;
- no priority claim is made for the complete closure.

No new theorem broadening is justified by this audit.

## 5. Publication posture after the required edits

If the scope-hardening edits compile and all existing Experiment-02 regressions remain green, the manuscript is technically consistent with the repository theorem to the level tested here.

The dominant remaining risk is then external significance/history review, not an identified internal coefficient or normalization failure.

## 6. Required recovery-state update

The repository recovery files were stale at the start of this audit: they still described Experiment 02 as Stage A / no manuscript even though the complete theorem, hostile prior-art audit, meta-referee, `manuscript_v1/`, and dedicated manuscript CI all existed on `main`.

Those recovery files must be synchronized with the actual remote state in the same scope-hardening checkpoint so future agents do not reconstruct from an obsolete stage.