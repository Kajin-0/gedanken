# Current State — Experiment 02

**Checkpoint:** hostile prior-art collision audit completed on real `main`.  
**Status:** **PHYSICS THEOREM ESTABLISHED WITHIN THE DECLARED BOUNDED-PORT NARROWBAND CLASS; SAME-ENDPOINT PASSIVE RECURRENCE CONTROLLED; STANDALONE INGREDIENT NOVELTY REJECTED; NO EXACT COLLISION FOUND FOR COMPLETE TWO-ENDED INERTIA CLOSURE; SIGNIFICANCE/PRIORITY IS NOW THE DOMINANT RISK; NO MANUSCRIPT YET.**

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

Files:

- `PASSIVE_SELECTED_PORT_CUT_DERIVATION.md`
- `INFINITE_DIMENSIONAL_BOUNDED_PORT_EXTENSION.md`

### B. Gravitational endpoint resource

```math
\kappa_{g,n}
=\frac{G\omega_n^4}{5c^5}
\frac{q_n:q_n}{\mu_n},
```

with

```math
\sum_n\frac{q_n:q_n}{\mu_n}
\le\frac{20}{3}I_2,
```

so in the narrow carrier sector

```math
\boxed{
\operatorname{Tr}(K_g^\dagger K_g)
\lesssim
\frac{4G}{3c^5}I_2\omega_0^4.
}
```

File:

`GRAVITATIONAL_ENDPOINT_RESOURCE_DERIVATION.md`

### C. Compact TT propagation

```math
D_q\le\frac52,
```

and outgoing stationary phase gives

```math
\boxed{
\limsup_{kR\to\infty}(kR)^2\|P_g\|_{\rm op}^2
\le\frac{25}{16}.
}
```

File:

`TT_PROPAGATION_BOUND_DERIVATION.md`

### D. Assembly

With `k_0=omega_0/c`, the three resources give

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega_0^2}{12c^3R^2}
\min(I_{2,A},I_{2,B}).
}
```

File:

`FINITE_TWO_ENDED_INERTIA_BOUND.md`

## 3. Countably infinite bounded-port closure

For a separable internal modal Hilbert space with bounded Markov port operator and passive contraction semigroup, the selected-input Gramian obeys

```math
0\le P_u(\tau)
\le I-T(\tau)T^\dagger(\tau)
\le I.
```

Stage B supplies

```math
\operatorname{Tr}(K_g^\dagger K_g)<\infty,
```

so the gravitational port is Hilbert–Schmidt and the operator-valued `H2` cut is finite.

This extends the theorem to countably infinite **bounded-port** modal sectors. It does not cover arbitrary unbounded PDE boundary-control ports or genuinely non-Markov continua.

## 4. Same-endpoint passive recurrence

Repeated passive returns between the same two separated compact endpoints obey

```math
P_{\rm eff}
=(I-P_+R_AP_-R_B)^{-1}P_+,
```

and

```math
\|P_{\rm eff}\|
\le\frac{p_+}{1-p_+p_-}.
```

For reciprocal one-hop power ceiling `eta=p^2`,

```math
\|P_{\rm eff}\|^2
\le\frac{\eta}{(1-\eta)^2}.
```

Therefore recurrence changes only subleading terms in the upper ceiling and

```math
\limsup_{kR\to\infty}(kR)^2\|P_{\rm eff}\|^2\le\frac{25}{16}.
```

The actual recurrent transfer may be smaller because of interference. The proof does not cover added relays, external mirrors/cavities, near-field exchange, or active feedback.

File:

`PASSIVE_TWO_ENDPOINT_RECURRENCE.md`

## 5. Narrowband/asymptotic discipline

The integrated variable is envelope detuning `nu`; `omega_0` is the absolute carrier. Required:

```math
B/\omega_0\ll1.
```

The `25/16` and `25/12` numbers are retained leading wave-zone coefficients, not universal exact finite-distance formulas.

File:

`NARROWBAND_NORMALIZATION_AUDIT.md`

## 6. Real validation record

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

## 7. Hostile prior-art verdict

Canonical audit:

`HOSTILE_PRIOR_ART_COLLISION_AUDIT.md`

The audit found strong historical collisions with nearly every individual ingredient:

```text
gravity antenna eigenmode theory:                  HISTORICAL
arbitrary-body multimode GW response:              HISTORICAL
integrated resonant-mass cross section:             HISTORICAL
mode-splitting finite integrated response:          HISTORICAL STRONG PRECEDENT
gravity material-response sum rules:                HISTORICAL
generator–receiver Hertz calculations:              HISTORICAL
generic wave-channel / coupling-limit mathematics:  HISTORICAL
generic response-plus-propagation bounds:           HISTORICAL
finite/infinite passive H2 machinery:                HISTORICAL
multiple-scattering recurrence:                     HISTORICAL
20/3 standalone novelty:                            DO NOT CLAIM
4/3 standalone novelty:                             DO NOT CLAIM
complete two-ended inertia-only closure:            NO EXACT COLLISION FOUND
priority claim:                                     NO
```

The most damaging near-collision is the old resonant-mass integrated-cross-section literature. Aguiar's review, citing Paik–Wagoner, explicitly notes that after adding a resonant transducer and producing two normal modes, the integrated cross section still retains a finite mass/material scaling. Thus the broad idea that extra passive resonances do not create unlimited integrated gravitational response is historical.

Rudenko's 2003 work is the strongest complete generator–receiver near-collision found: it optimizes an entire gravitational Hertz couple, but retains architecture-specific source/receiver/noise/geometry parameters rather than eliminating both endpoints into an inertia-only coherent spectral-area theorem.

Across the inspected sources, no exact statement of the complete closure

```text
passive selected-port spectral-area cut
-> gravitational trace at source and receiver
-> cumulative I_2 resource at BOTH endpoints
-> compact TT propagation ceiling
-> leading same-endpoint recurrence control
-> explicit min(I_2A,I_2B)/R^2 end-to-end ceiling
```

was found.

That is a **negative search result, not proof of priority**.

## 8. Current epistemic state

```text
physics theorem within declared model:                  GO
finite/countably infinite bounded-port modes:           GO
same-two-endpoint passive recurrence, leading order:    GO
broad-frequency theorem:                                NO CLAIM
unbounded PDE / non-Markov continuum extension:         NO CLAIM
added relays/cavities/near-field/active feedback:        NO CLAIM
standalone generic-method novelty:                       NO
standalone 20/3 or 4/3 novelty:                         NO
exact two-ended inertia closure as candidate result:     PROVISIONAL GO
exact historical priority:                               NOT ESTABLISHED
publication significance:                               OPEN / DOMINANT RISK
manuscript:                                              NONE
```

## 9. Experiment 01 boundary

Experiment 01 / V7 remains frozen. No V7 physics was modified by this reconstruction.

## 10. Next action — significance meta-referee

Do not broaden the theorem further merely because another extension is imaginable.

The next internally informative test is editorial/significance review:

> assuming the theorem is correct and the historical ingredients are fully credited, is the exact gravity-specific two-ended inertia closure sufficiently informative to justify a short specialist paper?

That review should decide `REJECT`, `MAJOR REVISION`, or `GO TO SHORT MANUSCRIPT`, and should penalize any presentation that makes the generic systems/modal machinery look new.
