# Current State — Experiment 02

**Checkpoint:** finite-dimensional narrowband inertia theorem assembled and validated on real `main`.  
**Status:** **FINITE-DIMENSIONAL NARROWBAND TWO-ENDED INERTIA BOUND ESTABLISHED WITHIN MODEL; INFINITE-MODAL EXTENSION, PASSIVE RECURRENCE, AND PRIORITY REMAIN OPEN; NO MANUSCRIPT.**

## 1. Current established theorem within model

Let `omega_0` be the absolute carrier angular frequency and `nu` the complex-envelope detuning. Define

```math
\Gamma_{\rm coh}
=\frac1{2\pi}\int_{\mathcal B_\nu}
\operatorname{Tr}[T^\dagger(\nu)T(\nu)]\,d\nu.
```

For separated compact passive nonrelativistic linear-harmonic source and receiver systems, under the current **finite-dimensional Markov, narrowband, leading quadrupolar wave-zone** assumptions,

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega_0^2}{12c^3R^2}
\min(I_{2,A},I_{2,B}),
}
```

where

```math
I_2=\int\rho r^2d^3x
```

is the scalar second mass moment about each endpoint center of mass.

This is a frequency-integrated coherent-transfer area with units `s^-1`, not an information capacity.

The theorem has been reconstructed from scratch in the actual repository. It is not inherited from the earlier conversation-only Experiment 02 state.

## 2. Proof spine

### A. Passive selected-port cut

For a finite-dimensional passive Markov realization,

```math
\boxed{
\Gamma_{\rm coh}
\le
\eta_{\max}
\min\!\left[
\operatorname{Tr}(K_{g,A}^\dagger K_{g,A}),
\operatorname{Tr}(K_{g,B}^\dagger K_{g,B})
\right].
}
```

Canonical derivation:

`PASSIVE_SELECTED_PORT_CUT_DERIVATION.md`

### B. Gravitational endpoint resource

For mass-orthogonal compact quadrupolar modes,

```math
\kappa_{g,n}
=\frac{G\omega_n^4}{5c^5}
\frac{q_n:q_n}{\mu_n}.
```

The STF influence-field identity and Bessel inequality give

```math
\sum_n\frac{q_n:q_n}{\mu_n}
\le\frac{20}{3}I_2,
```

hence in the narrow retained carrier sector

```math
\boxed{
\operatorname{Tr}(K_g^\dagger K_g)
\lesssim
\frac{4G}{3c^5}I_2\omega_0^4.
}
```

Canonical derivation:

`GRAVITATIONAL_ENDPOINT_RESOURCE_DERIVATION.md`

### C. Compact TT propagation

Independent classical normalized-TT angular-mode analysis gives

```math
\int d\Omega\,F_q
=\frac{8\pi}{5}q^*:q,
```

and compact quadrupole directivity

```math
D_q\le\frac52.
```

Outgoing stationary phase then gives

```math
\boxed{
\limsup_{kR\to\infty}
(kR)^2\|P_g\|_{\rm op}^2
\le\frac{25}{16}.
}
```

Canonical derivation:

`TT_PROPAGATION_BOUND_DERIVATION.md`

This was derived before comparing with Experiment 01. The real V7 one-graviton audit then supplied an independent cross-check of the same leading `25/16` coefficient.

### D. Assembly

Using `k_0=omega_0/c`, Stages A–C give

```math
\Gamma_{\rm coh}
\lesssim
\frac{25}{16(k_0R)^2}
\frac{4G\omega_0^4}{3c^5}
\min(I_{2,A},I_{2,B})
```

and therefore

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega_0^2}{12c^3R^2}
\min(I_{2,A},I_{2,B}).
}
```

Canonical assembly:

`FINITE_TWO_ENDED_INERTIA_BOUND.md`

## 3. Narrowband normalization correction

A subtle notation issue was caught before theorem promotion: Stage A integrates **envelope detuning** `nu`, whereas Stages B/C use the **absolute carrier** `omega_0`.

The active theorem therefore requires

```math
B/\omega_0\ll1.
```

A broad absolute-frequency theorem with the same simple coefficient has not been proved.

Canonical audit:

`NARROWBAND_NORMALIZATION_AUDIT.md`

## 4. Stage-C asymptotic correction

The initial Stage-C draft was stronger than justified when it assigned a universal `O((kR)^-4)` power correction to arbitrary complex source/receiver quadrupoles.

The corrected statement is only the leading limsup coefficient

```math
\limsup_{kR\to\infty}(kR)^2\|P_g\|_{\rm op}^2\le25/16.
```

The aligned plus-mode V7 specialization has an even-power finite-distance correction series, but Experiment 02 does not generalize that subleading structure without proof.

## 5. Real validation record

### Stage A

```text
workflow: .github/workflows/experiment02-passive-cut.yml
first canonical run: 31391304791
job: 93463450929
PASS
```

It reran successfully on the assembled theorem commit as run `31393498735`.

### Stage B

```text
workflow: .github/workflows/experiment02-endpoint-resource.yml
first canonical run: 31392339989
job: 93466817164
PASS
```

It reran successfully on the assembled theorem commit.

### Stage C

```text
workflow: .github/workflows/experiment02-tt-propagation.yml
first canonical run: 31393020114
job: 93469060678
PASS
```

Key output:

```text
aligned directivity saturation = 2.5
aligned amplitude prefactor = 1.25
aligned power prefactor = 1.5625
PASS: compact TT propagation 25/16 bound
```

It reran successfully on the assembled theorem commit.

### Combined theorem adversary

```text
workflow: .github/workflows/experiment02-combined-bound.yml
commit: 8fc8da7cf5d51e3a56d7e0b15434407c7e493ecb
run: 31393498572
job: 93470648716
PASS
```

Actual output:

```text
worst actual Gamma/(25 min(I2)/(12 R^2)) ratio = 0.0630906707807
largest endpoint resource/budget fraction = 0.99023971892
largest propagation/TT-ceiling fraction = 0.972827931667
PASS: finite-dimensional narrowband two-ended 25/12 inertia bound
```

The numerical regressions support the analytic proof; they do not replace it.

## 6. Historical boundary

Broad ingredients are already established:

- passive `H2`/lossless-bounded-real machinery;
- gravitational antenna eigenmode emission/reception;
- arbitrary-elastic-body multimode GW response;
- quadrupole radiation;
- TT projection and antenna directivity/reciprocity.

Current primary anchors include Guta–Yamamoto, Gough–Zhang, Hirakawa–Narihara–Fujimoto (1976), and Lobo (1995).

The historical status of the exact cumulative `20/3`/`4/3` resource and the complete two-ended inertia closure is still **OPEN**. A negative search is not proof of priority.

## 7. Current epistemic state

```text
finite-dimensional passive selected-port cut:         ESTABLISHED WITHIN MODEL
20/3 modal quadrupole resource:                        ESTABLISHED WITHIN MODEL
4/3 gravitational endpoint trace resource:             ESTABLISHED WITHIN MODEL
passive internal modal-mixing trace invariance:        ESTABLISHED WITHIN MODEL
leading compact TT 25/16 propagation coefficient:      ESTABLISHED WITHIN MODEL
finite-dimensional narrowband 25/12 two-ended bound:   ESTABLISHED WITHIN MODEL
broad absolute-frequency version:                      NOT ESTABLISHED
countably infinite bounded-port modal extension:       OPEN
passive two-endpoint recurrence:                       OPEN
unbounded PDE / non-Markov continuum extension:        OUTSIDE CURRENT CLAIM
complete historical prior-art boundary:                OPEN
publication significance / novelty:                    OPEN
manuscript:                                             NONE
```

## 8. Experiment 01 boundary

`../01-causal-quantum-branch-information/` remains the frozen V7 publication project. No Experiment 01 physics was modified during this reconstruction.

## 9. Next action — strongest loophole

The next mathematical task is to test whether the Stage-A passive cut survives a **countably infinite separable modal Hilbert space with bounded Markov port operators**.

The desired route is not finite truncation extrapolation alone. It should prove, in operator form, that for a contraction semigroup `T(t)` and selected bounded port `K_u`,

```math
P_u(\tau)=\int_0^\tau
T(t)K_u^\dagger K_uT^\dagger(t)dt
```

obeys a positive-operator ceiling `P_u <= I`, and then use the Stage-B trace bound to show the gravitational port is Hilbert–Schmidt so the operator-valued `H2` norm is finite.

Only after that proof and an independent truncation stress test should the theorem be extended beyond finite-dimensional endpoints.
