# Current State — Experiment 02

**Checkpoint:** manuscript-v1 adversarial scope hardening on real `main`.  
**Status:** **PHYSICS THEOREM ESTABLISHED WITHIN THE DECLARED RETAINED-SECTOR BOUNDED-PORT NARROWBAND CLASS; SHORT MANUSCRIPT ACTIVE; SCOPE-HARDENING CI PENDING ON THIS CHECKPOINT; SIGNIFICANCE/PRIORITY REMAINS THE DOMINANT EXTERNAL RISK.**

## 1. Current theorem

Let `omega_0` be the absolute carrier angular frequency, `nu` the complex-envelope detuning, and `B/omega_0 << 1`. Let `a_A,a_B` be characteristic endpoint radii and require

```math
k_0 a_A \ll 1,
\qquad
k_0 a_B \ll 1,
\qquad
k_0 R \gg 1,
\qquad
k_0=\omega_0/c.
```

Define

```math
\Gamma_{\rm coh}
=\frac1{2\pi}\int_{\mathcal B_\nu}
\operatorname{Tr}[T^\dagger(\nu)T(\nu)]\,d\nu.
```

At each endpoint the current theorem applies to a finite or countably infinite bounded-port Markov modal sector whose retained physical modal frequencies satisfy

```math
\omega_n\le\Omega,
\qquad
\Omega=\omega_0[1+O(B/\omega_0)].
```

For separated compact passive nonrelativistic linear-harmonic endpoints in weak leading mass-quadrupole gravity,

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega_0^2}{12c^3R^2}
\min(I_{2,A},I_{2,B}),
}
```

with

```math
I_2=\int\rho r^2d^3x
```

about each endpoint center of mass.

`Gamma_coh` has units `s^-1` and is a coherent-transfer spectral area, not an information capacity.

## 2. Proof spine

### A. Passive selected-port cut

For passive Markov endpoints,

```math
\Gamma_{\rm coh}
\le
\eta_{\max}
\min[
\operatorname{Tr}(K_{g,A}^\dagger K_{g,A}),
\operatorname{Tr}(K_{g,B}^\dagger K_{g,B})].
```

The band-limited `Gamma_coh` is no larger than the corresponding full-line `H2` integral because the integrand is nonnegative. The source and receiver cuts then follow by pointwise contractivity of the opposite endpoint and the propagation operator.

Files:

- `PASSIVE_SELECTED_PORT_CUT_DERIVATION.md`
- `INFINITE_DIMENSIONAL_BOUNDED_PORT_EXTENSION.md`

### B. Gravitational endpoint resource

```math
\kappa_{g,n}
=\frac{G\omega_n^4}{5c^5}
\frac{q_n:q_n}{\mu_n},
```

and

```math
\sum_n\frac{q_n:q_n}{\mu_n}
\le\frac{20}{3}I_2.
```

Therefore, for the retained sector with `omega_n <= Omega`,

```math
\operatorname{Tr}(K_g^\dagger K_g)
\le
\frac{4G}{3c^5}I_2\Omega^4
\lesssim
\frac{4G}{3c^5}I_2\omega_0^4.
```

The final carrier replacement is not a bound on uncontrolled modes with `omega_n >> omega_0`. Such higher-frequency off-resonant sectors require separate treatment.

File:

`GRAVITATIONAL_ENDPOINT_RESOURCE_DERIVATION.md`

### C. Compact TT propagation

For compact quadrupoles,

```math
D_q\le\frac52,
```

and outgoing stationary phase in the separated wave zone gives

```math
\limsup_{kR\to\infty}(kR)^2\|P_g\|_{\rm op}^2
\le\frac{25}{16}.
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

For a separable internal modal Hilbert space with bounded Markov port operator and passive contraction semigroup,

```math
0\le P_u(\tau)
\le I-\mathcal T(\tau)\mathcal T^\dagger(\tau)
\le I.
```

The retained gravitational resource gives

```math
\operatorname{Tr}(K_g^\dagger K_g)<\infty,
```

so the gravitational port is Hilbert--Schmidt and the operator-valued `H2` cut is finite.

This does not cover arbitrary unbounded PDE boundary-control ports or genuinely non-Markov continua.

## 4. Same-endpoint passive recurrence

Repeated passive returns between the same two separated compact endpoints obey

```math
P_{\rm eff}
=(I-P_+R_AP_-R_B)^{-1}P_+,
```

with

```math
\|P_{\rm eff}\|
\le\frac{p_+}{1-p_+p_-}.
```

For reciprocal one-hop power ceiling `eta=p^2`,

```math
\|P_{\rm eff}\|^2
\le\frac{\eta}{(1-\eta)^2}.
```

Since `eta=O[(kR)^-2]`, recurrence changes only subleading terms in the upper ceiling. This is not an equality for actual recurrent transfer.

File:

`PASSIVE_TWO_ENDPOINT_RECURRENCE.md`

## 5. Manuscript

Active source:

`manuscript_v1/`

Title:

**An Inertia-Controlled Throughput Bound for Passive Gravitational Transduction**

The meta-referee decision was `GO TO A SHORT SPECIALIST MANUSCRIPT`; that manuscript now exists on `main`.

First manuscript adversarial scope audit:

`MANUSCRIPT_V1_ADVERSARIAL_AUDIT_2026-08-10.md`

The audit found no coefficient failure, but required three hardenings:

1. explicitly constrain the retained endpoint modal sector at the carrier scale;
2. quantify compactness and wave-zone conditions;
3. make the band-integral-to-full-line-`H2` step explicit.

These edits are part of the current checkpoint and require fresh CI before freeze.

## 6. Validation record before this scope-hardening checkpoint

```text
Stage A passive cut:
  run 31391304791, job 93463450929 — PASS

Stage B endpoint resource:
  run 31392339989, job 93466817164 — PASS

Stage C TT propagation:
  run 31393020114, job 93469060678 — PASS

Combined finite-dimensional theorem:
  run 31393498572, job 93470648716 — PASS

Countably infinite bounded-port extension:
  run 31394415776, job 93473679179 — PASS

Passive same-endpoint recurrence:
  run 31394879241, job 93475219560 — PASS

Pre-hardening manuscript head:
  commit 87732887b9139f286e025e470810cdf207706116
  manuscript run 31397765390 — PASS
  combined-bound run 31397765584 — PASS
  infinite-modal run 31397765773 — PASS
  recurrence run 31397765372 — PASS
```

## 7. Historical / novelty boundary

Canonical files:

- `HOSTILE_PRIOR_ART_COLLISION_AUDIT.md`
- `META_REFEREE_SIGNIFICANCE_AUDIT.md`
- `CLAIM_LEDGER.md`

Nearly every ingredient has strong historical precedent. No standalone novelty claim is made for gravitational-antenna eigenmodes, integrated resonant response, the `20/3` or `4/3` lemmas, generic `H2` machinery, directivity, generic wave-channel bounds, or multiple-scattering composition.

No inspected source states the exact complete two-ended inertia closure. That is a negative search result, not proof of priority.

## 8. Current exclusions

No claim is made for

- broad absolute-frequency operation with one carrier coefficient;
- uncontrolled higher-frequency off-resonant endpoint sectors;
- arbitrary unbounded PDE boundary-control ports;
- genuinely non-Markov continua;
- added relays, external mirrors/cavities, or extended phased apertures;
- reactive near-field exchange;
- active gain/pumping/feedback;
- higher-multipole-dominated, relativistic, nonlinear, or strong-field regimes.

## 9. Current research mode

Do not broaden the theorem further without a concrete defect.

Immediate tasks:

1. validate the manuscript scope-hardening checkpoint on the exact `main` head;
2. synchronize all recovery files with that validated head;
3. perform one final manuscript claim/citation/normalization audit;
4. then freeze internal theory and reserve human specialists/journal referees for the external boundary.
