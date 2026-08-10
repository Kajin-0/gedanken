# Current State — Experiment 02

**Checkpoint:** countably infinite bounded-port extension validated on real `main`.  
**Status:** **NARROWBAND TWO-ENDED INERTIA BOUND ESTABLISHED FOR FINITE OR COUNTABLY INFINITE BOUNDED-PORT MARKOV MODAL SECTORS; PASSIVE RECURRENCE AND PRIORITY REMAIN OPEN; NO MANUSCRIPT.**

## 1. Current theorem within the declared model

Let `omega_0` be the absolute carrier angular frequency and `nu` the complex-envelope detuning. Define

```math
\Gamma_{\rm coh}
=\frac1{2\pi}\int_{\mathcal B_\nu}
\operatorname{Tr}[T^\dagger(\nu)T(\nu)]\,d\nu.
```

For separated compact passive nonrelativistic linear-harmonic source and receiver systems in weak leading-quadrupolar wave-zone gravity, with finite or countably infinite **bounded-port Markov modal sectors**,

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

is the scalar second mass moment about the endpoint center of mass.

`Gamma_coh` has units `s^-1` and is a coherent-transfer spectral area, not an information capacity.

## 2. Proof spine

### A. Passive selected-port cut

```math
\Gamma_{\rm coh}
\le
\eta_{\max}
\min[
\operatorname{Tr}(K_{g,A}^\dagger K_{g,A}),
\operatorname{Tr}(K_{g,B}^\dagger K_{g,B})].
```

Finite-dimensional derivation:

`PASSIVE_SELECTED_PORT_CUT_DERIVATION.md`

Countably infinite bounded-port extension:

`INFINITE_DIMENSIONAL_BOUNDED_PORT_EXTENSION.md`

### B. Gravitational endpoint resource

```math
\kappa_{g,n}
=\frac{G\omega_n^4}{5c^5}
\frac{q_n:q_n}{\mu_n},
```

with

```math
\sum_n\frac{q_n:q_n}{\mu_n}
\le\frac{20}{3}I_2.
```

Thus in the narrow retained carrier sector

```math
\boxed{
\operatorname{Tr}(K_g^\dagger K_g)
\lesssim
\frac{4G}{3c^5}I_2\omega_0^4.
}
```

For a countable modal sector the finite trace makes the gravitational port Hilbert–Schmidt, supplying the regularity needed by the operator-valued `H2` proof.

Canonical derivation:

`GRAVITATIONAL_ENDPOINT_RESOURCE_DERIVATION.md`

### C. Compact TT propagation

Normalized STF TT radiation has

```math
\int d\Omega\,F_q=\frac{8\pi}{5}q^*:q,
\qquad
D_q\le\frac52.
```

Outgoing stationary phase gives

```math
\boxed{
\limsup_{kR\to\infty}
(kR)^2\|P_g\|_{\rm op}^2
\le\frac{25}{16}.
}
```

Canonical derivation:

`TT_PROPAGATION_BOUND_DERIVATION.md`

### D. Assembly

With `k_0=omega_0/c`, the three resources combine to

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

The filename is historical from the first proof stage; the passive cut has now been extended to countably infinite bounded-port modal sectors.

## 3. Infinite-dimensional bounded-port closure

Let `X` be separable and `T(t)` a passive contraction semigroup with bounded total Markov port `K`. For selected input `K_u`,

```math
P_u(\tau)=\int_0^\tau
T(t)K_u^\dagger K_uT^\dagger(t)dt
```

obeys

```math
\boxed{
0\le P_u(\tau)
\le I-T(\tau)T^\dagger(\tau)
\le I.
}
```

The monotone strong limit satisfies `0 <= P_u <= I`.

Stage B gives

```math
\operatorname{Tr}(K_g^\dagger K_g)<\infty,
```

so `K_g` is Hilbert–Schmidt. Consequently

```math
\int_0^\infty
\|K_gT(t)K_u^\dagger\|_{\rm HS}^2dt
\le
\operatorname{Tr}(K_g^\dagger K_g),
```

and Hilbert-space Plancherel gives the same frequency-domain cut.

This does **not** cover arbitrary unbounded PDE boundary ports or non-Markov continua; those require separate admissibility/domain analysis.

## 4. Narrowband and asymptotic discipline

The integrated variable is envelope detuning `nu`; `omega_0` is the absolute carrier. The theorem requires

```math
B/\omega_0\ll1.
```

See `NARROWBAND_NORMALIZATION_AUDIT.md`.

The `25/16` propagation statement is a leading wave-zone limsup coefficient. Experiment 02 does not assign the aligned plus-mode V7 even-power finite-distance correction to arbitrary complex quadrupole pairs.

## 5. Real validation record

```text
Stage A passive cut:
  run 31391304791, job 93463450929 — PASS

Stage B endpoint resource:
  run 31392339989, job 93466817164 — PASS

Stage C TT propagation:
  run 31393020114, job 93469060678 — PASS

Combined finite-dimensional theorem:
  commit 8fc8da7cf5d51e3a56d7e0b15434407c7e493ecb
  run 31393498572, job 93470648716 — PASS

Countably infinite bounded-port extension:
  commit 91566b4ccfb1488b54a403a79452b9dc67347181
  run 31394415776, job 93473679179 — PASS
```

Infinite-modal stress-test output:

```text
analytic infinite gravitational trace limit = 0.0789987925949
N=64 gravitational trace = 0.0787012072883
N=64 trace tail = 0.000297585306554
largest lambda_max(P_u) = 0.733694365996
worst H2/gravitational-resource ratio = 0.581912323912
modal-mixing resource error = 4.16333634234e-17
modal-mixing H2 error = 8.67361737988e-16
PASS: countably-infinite bounded-port truncation stress test
```

The truncation regression is a stress test. The operator semigroup/trace argument is the proof.

## 6. Historical boundary

Broad ingredients are established and are not novelty claims:

- passive `H2`/lossless-bounded-real machinery;
- infinite-dimensional `H2` realization/operator-Gramian methods;
- gravitational antenna eigenmode emission/reception;
- arbitrary-elastic-body multimode GW response;
- quadrupole radiation;
- TT projection and antenna directivity/reciprocity.

Current primary/system anchors include Guta–Yamamoto, Gough–Zhang, Hirakawa–Narihara–Fujimoto (1976), Lobo (1995), Baras–Brockett (1975), and Opmeer–Reis–Wollner (2013).

The exact historical status of the cumulative `20/3`/`4/3` resource and the complete two-ended closure remains **OPEN**. No priority language is permitted.

## 7. Current epistemic state

```text
passive selected-port cut, finite dimension:           ESTABLISHED WITHIN MODEL
countably infinite bounded-port passive extension:     ESTABLISHED WITHIN MODEL
20/3 modal quadrupole resource:                        ESTABLISHED WITHIN MODEL
4/3 gravitational endpoint trace resource:             ESTABLISHED WITHIN MODEL
passive internal modal-mixing trace invariance:        ESTABLISHED WITHIN MODEL
leading compact TT 25/16 propagation coefficient:      ESTABLISHED WITHIN MODEL
narrowband 25/12 two-ended bound:                      ESTABLISHED WITHIN MODEL
broad absolute-frequency version:                      NOT ESTABLISHED
passive two-endpoint recurrence:                       OPEN
unbounded PDE / non-Markov continuum extension:        OUTSIDE CURRENT CLAIM
complete historical prior-art boundary:                OPEN
publication significance / novelty:                    OPEN
manuscript:                                             NONE
```

## 8. Experiment 01 boundary

Experiment 01 / V7 remains frozen. No V7 physics has been modified by this reconstruction.

## 9. Next action — passive recurrence

The strongest remaining internal physical loophole is repeated source↔receiver gravitational scattering between the same two passive compact endpoints.

Next task:

1. write the exact two-endpoint multiple-scattering/feedback resolvent;
2. bound endpoint reflection blocks by passivity;
3. determine whether recurrence can change the retained leading `1/R^2` power ceiling;
4. distinguish an upper-bound asymptotic from an equality for actual transfer;
5. add a random contractive-matrix recurrence adversary and record real CI.

After recurrence, the dominant remaining question should be historical priority/significance rather than another internal generalization.
