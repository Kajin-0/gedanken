# Experiment 02 — Passive Gravitational Coherent-Transfer Throughput

## Question

What frequency-integrated coherent transfer can a **direct passive gravitational link** support when both compact matter interfaces and the propagating TT channel are treated explicitly?

Experiment 01 / V7 is frozen. This branch develops a separate theorem and does not modify V7.

---

## Headline theorem

For compact passive nonrelativistic **linear bosonic** source and receiver networks coupled by quadrupolar linearized gravity in the weak one-way wave zone, define

```math
\Gamma_{\rm coh}
=\frac1{2\pi}
\int_{\mathcal B}
\operatorname{Tr}[T^\dagger(\omega)T(\omega)]d\omega.
```

For a narrow band centered at `omega`, the current theorem gives

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega^2}{12c^3R^2}
\min\!\left(
\langle I_A\rangle,
\langle I_B\rangle
\right).
}
```

Here `I_A` and `I_B` are internal mass inertia moments about each endpoint center of mass.

The result contains no endpoint quality factor, no assumed number of passive modes, and no four-spoke-specific parameter.

`Gamma_coh` is a physical integrated coherent-transfer / efficiency-bandwidth quantity, **not itself a quantum capacity**.

---

## Why the theorem survives obvious passive escape routes

### High Q

For one source and receiver pole,

```math
\Gamma_{\rm EBP}
=\frac1{2\pi}\int\tau(\Omega)d\Omega
\le
\eta_{\rm prop}\min(\kappa_{g,A},\kappa_{g,B}).
```

Removing ordinary loss can raise peak gravitational branching, but the spectral response narrows toward the intrinsic gravitational linewidth.

The general fact that integrated resonant gravitational response is `Q`-independent is historical antenna physics; the present result extends the resource ceiling to arbitrary passive local-port matching and many-mode coherent endpoint dynamics.

### Many modes / coherent mixing

Established completely passive linear-system identities imply the endpoint cut set

```math
\Gamma_{\rm coh}
\le
\eta_{\max}
\min\!\left[
\operatorname{Tr}(K_{g,A}^\dagger K_{g,A}),
\operatorname{Tr}(K_{g,B}^\dagger K_{g,B})
\right].
```

Internal coherent mixing cannot increase the basis-invariant gravitational coupling trace.

### More passive quadrupole oscillator strength

For ordinary compact nonrelativistic linear matter, the cumulative mass-quadrupole EWSR gives

```math
\operatorname{Tr}(K_g^\dagger K_g)
\le
\frac{4G\omega^4}{3c^5}\langle I\rangle
```

in the retained narrow band.

This is the step that closes the arbitrarily-many-passive-resonances loophole.

### Better compact quadrupole orientation

For any compact STF mass quadrupole,

```math
D_Q(\hat n)\le\frac52,
```

and the normalized TT one-graviton propagation map obeys

```math
\|P_g\|_{\rm op}^2
\le
\frac{25}{16(kR)^2}
```

at leading wave-zone order.

**Prior-art correction:** Hirakawa, Narihara, and Fujimoto (1976) already derived the same real-STF directivity functional in equivalent component form, including the `5/2` maximum. The candidate contribution is not the directivity law; it is the use of the normalized inter-endpoint TT propagation operator inside the two-ended resource cut set.

---

## Prior art and the actual candidate contribution

The easy novelty story is **not allowed**.

Full-text historical audits now establish that all of the following are old:

- complete gravitational generator--detector calculations and architecture-specific end-to-end limitations;
- compact mechanical gravitational antenna eigenmodes;
- one quadrupole-derived oscillator-strength parameter governing emission and reception;
- gravitational antenna reciprocity;
- `Q`-independent short-pulse / integrated gravitational response;
- the compact real-STF directivity functional and its `D=5/2` maximum;
- integrated resonant-mass absorption, susceptibility/Kubo gravitational response, passive Gramian/H2 mathematics, and generic quantum-transducer efficiency-bandwidth/capacity metrics.

The candidate contribution is therefore only the **many-mode two-ended passive resource closure**:

```text
historical compact gravitational antenna oscillator-strength / reciprocity / directivity
+ established passive selected-port H2 machinery
-> source gravitational coupling trace
-> normalized separated TT propagation operator
-> receiver gravitational coupling trace
-> cumulative mass-quadrupole EWSR closure of BOTH endpoint traces
-> end-to-end frequency-integrated coherent-transfer ceiling
-> channel-specific pure-loss corollaries.
```

No equivalent theorem has been found in the inspected primary sources, including the full Hirakawa–Narihara–Fujimoto 1976 and Grishchuk–Sazhin 1975 papers. That is a **negative search result, not proof of priority**.

Canonical audits:

- `TARGETED_TWO_ENDED_NOVELTY_SWEEP_2026-08-09.md`
- `SPECIALIST_PRIOR_ART_STRESS_TEST_2026-08-09.md`
- `GRISHCHUK_SAZHIN_1975_COLLISION_AUDIT.md`
- `HIRAKAWA_NARIHARA_FUJIMOTO_1976_COLLISION_AUDIT.md`

---

## Pure-loss corollaries

For a stationary vacuum pure-loss realization, every transmission eigenvalue obeys

```math
\tau_n(\omega)\le\eta_{\max}.
```

If `eta_max <= 1/2`,

```math
\boxed{Q_1=0}
```

for unassisted asymptotic pure-loss quantum capacity.

For `eta_max < 1`,

```math
\boxed{
Q_2
\le
\frac{\Gamma_{\rm coh}}
{\ln2\,(1-\eta_{\max})}
}
```

for the two-way-assisted pure-loss rate.

These are channel-specific corollaries, not universal statements about gravity.

---

## Explicit realization

The frozen V7 long-wavelength mode reaches 30% of the endpoint-only EWSR gravitational-linewidth ceiling and saturates the compact TT geometry ceiling. This shows that the theorem has the correct physical scale, but the complete end-to-end coefficient is not claimed globally sharp.

See `BENCHMARK_THEOREM_COMPARISON.md`.

---

## Scope

The current theorem is restricted to:

- weak linearized gravity;
- direct propagating one-way wave-zone transfer;
- compact nonrelativistic quadrupole source and receiver matter;
- stable passive linear bosonic endpoint dynamics in a narrow/band-local Markov description;
- no active gain, inversion, parametric drive, extended phased aperture, higher-multipole beaming, near-field exchange, or intermediate relay.

A general interacting/non-Markov susceptibility theorem is **not required for the current result** and is intentionally deferred.

---

## Validation

Physics regression checks include:

- exact two-pole spectral area against direct integration;
- random passive rate sets;
- random multi-mode passive Gramians and end-to-end cascades;
- random complex STF tensors against the TT ceiling;
- TT angular normalization and the `25/16` propagation coefficient;
- microscopic gravitational-port factorization with overlapping radiation patterns.

The post-Hirakawa manuscript framing also passed branch CI:

- workflow run `31342625802`;
- job `93318795190`;
- LaTeX compile: **PASS**;
- unresolved citation/reference scan: **PASS**;
- PDF upload: **PASS**;
- rendered manuscript: **14 pages**, visual QA **PASS**.

---

## Read next

1. `CURRENT_STATE.md`
2. `HIRAKAWA_NARIHARA_FUJIMOTO_1976_COLLISION_AUDIT.md`
3. `GRISHCHUK_SAZHIN_1975_COLLISION_AUDIT.md`
4. `THEOREM_SYNTHESIS.md`
5. `PASSIVE_NETWORK_CUTSET_THEOREM.md`
6. `GRAVITATIONAL_PORT_FACTORIZATION.md`
7. `MATERIAL_RESPONSE_BRIDGE.md`
8. `TT_PROPAGATION_BOUND.md`
9. `CAPACITY_COROLLARIES.md`
10. `ADVERSARIAL_THEOREM_AUDIT.md`
11. `LITERATURE_MAP.md`
12. `AGENTS.md`

## Current status

**Physics theorem: closed within the stated passive compact linear-bosonic class.**

**Exact publication novelty: provisional; no inspected full-theorem collision found, but broad ingredient-level novelty is explicitly rejected.**

**Next step: external specialist/referee-style review of the exact resource closure and its significance. Do not broaden the theorem further for this paper.**
