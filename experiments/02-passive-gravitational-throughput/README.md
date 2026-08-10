# Experiment 02 — Passive Gravitational Coherent-Transfer Throughput

## Question

What frequency-integrated coherent transfer can a **direct passive gravitational link** support when both compact matter interfaces and the propagating TT channel are treated explicitly?

Experiment 01 / V7 is frozen. This branch develops a separate theorem and does not modify V7.

---

## Headline theorem

For compact passive nonrelativistic **linear bosonic** source and receiver networks in weak one-way quadrupolar wave-zone gravity,

```math
\Gamma_{\rm coh}
=\frac1{2\pi}\int_{\mathcal B}
\operatorname{Tr}[T^\dagger(\omega)T(\omega)]d\omega
```

obeys

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega^2}{12c^3R^2}
\min\!\left(\langle I_A\rangle,\langle I_B\rangle\right).
}
```

`I_A` and `I_B` are internal mass inertia moments about the endpoint centers of mass.

The final ceiling contains no endpoint quality factor, no assumed number of passive resonances, no internal coherent-mixing parameter, and no four-spoke-specific parameter. `Gamma_coh` is an integrated coherent-transfer quantity, **not itself a quantum capacity**.

---

## Proof skeleton

### Passive selected-port cut set

```math
\Gamma_{\rm coh}
\le
\eta_{\max}
\min\!\left[
\operatorname{Tr}(K_{g,A}^\dagger K_{g,A}),
\operatorname{Tr}(K_{g,B}^\dagger K_{g,B})
\right].
```

This follows from established completely passive H2/Gramian identities and allows arbitrary finite-dimensional passive coherent mode mixing and overlapping resonances.

### Cumulative quadrupole resource

```math
\operatorname{Tr}(K_g^\dagger K_g)
=\sum_n\kappa_{g,n}
\le
\frac{4G}{3c^5}\langle I\rangle\Omega^4.
```

This mass-quadrupole EWSR step closes the arbitrarily-many-passive-resonances loophole.

### Normalized propagation

```math
G_B^\dagger U_RG_A
=\Gamma_{g,B}^{1/2}P_g\Gamma_{g,A}^{1/2},
```

with

```math
\|P_g\|_{\rm op}^2
\le\frac{25}{16(kR)^2}
```

at leading wave-zone order.

---

## Historical normalization cross-check

The full Hirakawa–Narihara–Fujimoto 1976 compact-antenna formulas provide an independent classical normalization of the endpoint resource. Their mode effective area satisfies

```math
A_{Gn}=\frac{2q_n:q_n}{M\mu_n}.
```

Quantizing the same elastic normal coordinate gives

```math
Q^{01}:Q^{10}
=\frac{\hbar M A_{Gn}}{4\omega_n},
```

and therefore

```math
\boxed{
\kappa_{g,n}
=\frac{GMA_{Gn}\omega_n^4}{10c^5}.
}
```

Their historical Q-independent short-pulse response becomes

```math
\frac{E}{F(\nu_n)}
=\frac{\pi}{2}\frac{\kappa_{g,n}}{k_n^2}f_n(\hat n).
```

Thus the quantum linewidth used by Experiment 02 is exactly the quantized form of the historical compact-antenna oscillator-strength parameter. No factor-of-two or `2 pi` mismatch was found.

See `HIRAKAWA_EFFECTIVE_AREA_QUANTUM_LINEWIDTH_CROSSCHECK.md`.

---

## What is historical, not new

The prior-art audit now explicitly rejects novelty for

- complete gravitational generator--detector calculations and broad end-to-end limitations;
- compact mechanical gravitational antenna eigenmodes;
- quadrupole-controlled emission/reception oscillator strength;
- gravitational antenna reciprocity;
- Q-independent short-pulse / integrated gravitational response;
- the compact real-STF directivity functional and `D=5/2` maximum;
- passive H2/Gramian mathematics;
- continuous-time transducer efficiency-bandwidth/capacity metrics;
- generic source--receiver singular wave channels, squared connection-strength sums, and two-body response + Green-operator transfer bounds;
- the general methodology of using a physical sum rule to constrain an integrated passive scattering response.

Hirakawa Eq. (15) is algebraically the same real-STF directivity functional as

```math
D_q(\hat n)=\frac52\frac{q:\Lambda(\hat n):q}{q:q}.
```

Generic wave-channel precedents are documented in `GENERIC_WAVE_TRANSFER_COLLISION_AUDIT_2026-08-09.md`.

---

## Actual candidate contribution

The surviving candidate novelty is only the **gravity-specific cumulative endpoint closure**:

```text
established passive selected-port H2 integral
-> smaller source/receiver gravitational coupling trace
-> microscopic quadrupole identification of those traces
-> cumulative mass-quadrupole EWSR at BOTH endpoints
-> normalized compact separated TT propagation
-> explicit inertia-controlled many-mode end-to-end ceiling.
```

No inspected primary source has been found stating this exact theorem. That remains a **negative search result, not proof of priority**.

The manuscript must therefore stand on the usefulness and nontriviality of

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega^2}{12c^3R^2}
\min(\langle I_A\rangle,\langle I_B\rangle),
}
```

not on any of its individual ingredients.

---

## Exact resonator and pure-loss corollaries

For one source and receiver pole,

```math
\Gamma_{\rm EBP}
\le
\eta_{\rm prop}\min(\kappa_{g,A},\kappa_{g,B}).
```

For the symmetric lossless family,

```math
\kappa_{\rm in}=\kappa_{\rm out}=2\kappa_g,
\qquad
\Gamma_{\rm EBP}^{\rm max}
=\frac8{27}\eta_{\rm prop}\kappa_g.
```

For a stationary vacuum pure-loss realization,

```math
\eta_{\max}\le\frac12\Rightarrow Q_1=0,
```

and

```math
Q_2
\le
\frac{\Gamma_{\rm coh}}
{\ln2\,(1-\eta_{\max})}.
```

These are channel-specific corollaries, not universal quantum-capacity statements.

---

## Scope

The theorem is restricted to

- weak linearized gravity;
- direct one-way propagating wave-zone transfer;
- compact nonrelativistic quadrupole source and receiver matter;
- stable passive linear bosonic endpoint dynamics in narrow/band-local Markov sectors;
- no active gain, inversion, parametric drive, extended phased aperture, higher-multipole beaming, near-field exchange, or intermediate relay.

A general interacting/non-Markov susceptibility theorem is intentionally deferred.

---

## Validation

Physics regressions:

```text
run 31311724347
job 93240439026
PASS
```

Latest manuscript build after the historical-normalization and cross-field-prior-art revisions:

```text
run 31343168940
job 93320172594
LaTeX compile:             PASS
unresolved refs/citations: PASS
PDF artifact upload:       PASS
```

---

## Read next

1. `CURRENT_STATE.md`
2. `HIRAKAWA_EFFECTIVE_AREA_QUANTUM_LINEWIDTH_CROSSCHECK.md`
3. `HIRAKAWA_NARIHARA_FUJIMOTO_1976_COLLISION_AUDIT.md`
4. `GENERIC_WAVE_TRANSFER_COLLISION_AUDIT_2026-08-09.md`
5. `GRISHCHUK_SAZHIN_1975_COLLISION_AUDIT.md`
6. `THEOREM_SYNTHESIS.md`
7. `PASSIVE_NETWORK_CUTSET_THEOREM.md`
8. `GRAVITATIONAL_PORT_FACTORIZATION.md`
9. `MATERIAL_RESPONSE_BRIDGE.md`
10. `TT_PROPAGATION_BOUND.md`
11. `CAPACITY_COROLLARIES.md`
12. `ADVERSARIAL_THEOREM_AUDIT.md`

## Current status

**Physics theorem: closed within the stated passive compact linear-bosonic class.**

**Exact novelty: provisional only for the gravity-specific cumulative inertia closure.**

**Main remaining risk: publication significance, not a known algebraic defect.**

**Next step: hostile external-referee-style review. Do not broaden the theorem further for this paper.**
