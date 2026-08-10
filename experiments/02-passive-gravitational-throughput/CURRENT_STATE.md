# Current State — Experiment 02

**Checkpoint:** passive recurrence validated on real `main`.  
**Status:** **NARROWBAND TWO-ENDED INERTIA BOUND ESTABLISHED FOR FINITE OR COUNTABLY INFINITE BOUNDED-PORT MARKOV MODAL SECTORS; SAME-ENDPOINT PASSIVE RECURRENCE DOES NOT CHANGE THE LEADING COEFFICIENT; PRIORITY/SIGNIFICANCE NOW DOMINANT; NO MANUSCRIPT.**

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

is the scalar second mass moment about each endpoint center of mass.

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

The finite trace makes the countable gravitational port Hilbert–Schmidt, which is exactly the regularity used by the infinite-dimensional `H2` proof.

Canonical derivation:

`GRAVITATIONAL_ENDPOINT_RESOURCE_DERIVATION.md`

### C. Compact TT propagation

Normalized STF TT radiation gives

```math
D_q\le\frac52
```

and outgoing stationary phase gives

```math
\boxed{
\limsup_{kR\to\infty}(kR)^2\|P_g\|_{\rm op}^2
\le\frac{25}{16}.
}
```

Canonical derivation:

`TT_PROPAGATION_BOUND_DERIVATION.md`

### D. Two-ended assembly

With `k_0=omega_0/c`, Stages A–C give

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

The filename reflects the first proof stage; the endpoint cut is now also established for countably infinite bounded-port modal sectors.

## 3. Same-endpoint passive recurrence

Let `P_+` and `P_-` be forward/reverse separated gravitational propagation and `R_A,R_B` the gravitational reflection blocks of the passive endpoints. The exact repeated-return propagation is

```math
\boxed{
P_{\rm eff}
=(I-P_+R_AP_-R_B)^{-1}P_+.
}
```

Passivity gives `||R_A||,||R_B|| <= 1`. If

```math
p_+=\|P_+\|,
\qquad
p_-=\|P_-\|,
```

then

```math
\boxed{
\|P_{\rm eff}\|
\le\frac{p_+}{1-p_+p_-}.
}
```

For reciprocal one-hop power ceiling `eta=p^2`,

```math
\boxed{
\|P_{\rm eff}\|^2
\le\frac{\eta}{(1-\eta)^2}.
}
```

Since `eta=O((kR)^-2)`, the correction to the **upper ceiling** begins at `O((kR)^-4)` in power. Therefore

```math
\boxed{
\limsup_{kR\to\infty}(kR)^2\|P_{\rm eff}\|^2
\le\frac{25}{16}.
}
```

The actual recurrent transfer need not equal the one-hop transfer plus a positive correction; destructive interference can make it smaller.

Canonical derivation:

`PASSIVE_TWO_ENDPOINT_RECURRENCE.md`

This does not cover added relays, external mirrors/cavities, active feedback, near-field exchange, or a changed propagation architecture.

## 4. Narrowband and asymptotic discipline

The integrated variable is envelope detuning `nu`; `omega_0` is the absolute carrier. Required:

```math
B/\omega_0\ll1.
```

See `NARROWBAND_NORMALIZATION_AUDIT.md`.

The `25/16` and final `25/12` coefficients are retained leading wave-zone coefficients, not universal exact finite-distance formulas.

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

Passive same-endpoint recurrence:
  commit e040fcaf2f6023fafd02bef1f11846d0a9236d0e
  run 31394879241, job 93475219560 — PASS
```

Recurrence adversary output:

```text
worst random ||P_eff|| / resolvent ceiling ratio = 0.999994469265
largest random z^2 ||P_eff||^2 = 1.64372328603
largest scalar saturation absolute error = 2.77555756156e-17
scalar z=160 scaled power = 1.56269075233
target leading coefficient 25/16 = 1.5625
z=160 leading-coefficient absolute error = 0.000190752327001
recurrence ceiling correction / eta^2 at z=160 = 2.00018312037
PASS: passive two-endpoint recurrence leaves leading 25/16 coefficient unchanged
```

The finite-`z` scaled recurrent power may exceed `25/16`; that is the expected subleading recurrence correction, not a violation of the asymptotic coefficient.

## 6. Historical boundary

Broad ingredients are established and are not novelty claims:

- passive finite/infinite-dimensional `H2` machinery;
- elastic gravitational-antenna eigenmode theory;
- arbitrary-body multimode gravitational response;
- quadrupole radiation;
- TT directivity/reciprocity;
- multiple-scattering/network composition.

Primary/system anchors currently include Guta–Yamamoto, Gough–Zhang, Hirakawa–Narihara–Fujimoto (1976), Lobo (1995), Baras–Brockett (1975), Opmeer–Reis–Wollner (2013), and Redheffer (1962).

The exact historical status of the `20/3`/`4/3` cumulative resource and the complete two-ended inertia closure remains **OPEN**. A negative search is not proof of priority.

## 7. Current epistemic state

```text
passive selected-port cut:                             ESTABLISHED WITHIN MODEL
countably infinite bounded-port passive extension:     ESTABLISHED WITHIN MODEL
20/3 modal quadrupole resource:                        ESTABLISHED WITHIN MODEL
4/3 gravitational endpoint trace resource:             ESTABLISHED WITHIN MODEL
passive internal modal-mixing trace invariance:        ESTABLISHED WITHIN MODEL
leading compact TT 25/16 propagation coefficient:      ESTABLISHED WITHIN MODEL
narrowband 25/12 two-ended bound:                      ESTABLISHED WITHIN MODEL
same-two-endpoint passive recurrence, leading order:   ESTABLISHED WITHIN MODEL
broad absolute-frequency version:                      NOT ESTABLISHED
unbounded PDE / non-Markov continuum extension:        OUTSIDE CURRENT CLAIM
added relays/cavities/near-field/active feedback:       OUTSIDE CURRENT CLAIM
complete historical prior-art boundary:                OPEN
publication significance / novelty:                    OPEN
manuscript:                                             NONE
```

## 8. Experiment 01 boundary

Experiment 01 / V7 remains frozen. No V7 physics was modified by this reconstruction.

## 9. Next action — hostile prior-art collision

There is no longer an obvious internal finite/countable-mode or same-endpoint recurrence loophole inside the declared class.

The dominant next question is:

> Does older gravitational-antenna, resonant-mass, generator–receiver, oscillator-strength, absorption-cross-section, or generic wave-channel literature already contain an equivalent complete two-ended inertia closure, perhaps under different notation?

The next pass must assume the answer is yes and try to find the collision. Only after that audit should manuscript/significance work begin.
