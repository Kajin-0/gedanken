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

For ordinary compact nonrelativistic linear matter, the mass-quadrupole EWSR gives

```math
\operatorname{Tr}(K_g^\dagger K_g)
\le
\frac{4G\omega^4}{3c^5}\langle I\rangle
```

in the retained narrow band.

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

The V7 plus mode saturates this geometry ceiling, but the theorem itself no longer depends on that source construction.

---

## What is actually new here — if the remaining prior-art audit holds

The easy novelty story is **not allowed**.

Historical resonant-mass gravitational-wave antenna theory already uses integrated absorption cross sections. The cancellation between increased resonant peak and reduced bandwidth at high Q is therefore not a new discovery here. Gravitational absorption written in material-susceptibility language is also established, as are passive quantum-network Gramian identities and generic quantum-transducer efficiency-bandwidth/capacity metrics.

The candidate contribution is narrower:

```text
historical one-sided gravitational response
+ established passive network identities
-> source gravitational resource cut set
-> normalized propagating TT channel
-> receiver gravitational resource cut set
-> end-to-end integrated coherent-transfer ceiling
-> pure-loss quantum-information corollaries.
```

A targeted search has not yet found this same two-ended passive far-field closure. That is a negative search result, not proof of priority.

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

Automated branch regression checks:

- exact two-pole spectral area against direct integration;
- random passive rate sets;
- random multi-mode passive Gramians and end-to-end cascades;
- random complex STF tensors against the `D <= 5/2` TT ceiling;
- TT angular normalization and the `25/16` propagation coefficient.

GitHub Actions run `31310582891`, job `93237694140`, passed all current regression stages.

---

## Read next

1. `CURRENT_STATE.md`
2. `THEOREM_SYNTHESIS.md`
3. `PASSIVE_NETWORK_CUTSET_THEOREM.md`
4. `GRAVITATIONAL_PORT_FACTORIZATION.md`
5. `MATERIAL_RESPONSE_BRIDGE.md`
6. `TT_PROPAGATION_BOUND.md`
7. `CAPACITY_COROLLARIES.md`
8. `ADVERSARIAL_THEOREM_AUDIT.md`
9. `INITIAL_NOVELTY_SWEEP.md`
10. `LITERATURE_MAP.md`
11. `MANUSCRIPT_OUTLINE.md`
12. `AGENTS.md`

## Current status

**Physics theorem: closed within the stated passive compact linear-bosonic class.**

**Publication novelty: promising but not yet established.**

The next step is a theorem-first manuscript hardening pass, not further broadening of the physics.
