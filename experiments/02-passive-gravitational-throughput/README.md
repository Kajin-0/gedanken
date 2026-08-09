# Experiment 02 — Passive Gravitational Coherent-Transfer Throughput

## Research question

Can the speed–efficiency tradeoff exposed by Experiment 01 be promoted to a broad passive gravitational throughput bound that cannot be evaded by arbitrarily high Q, many resonances, or coherent mode mixing?

**Current answer:** yes for stable finite-dimensional passive linear Markov endpoint networks. The remaining hard step is extending the material-response bridge to completely general interacting/non-Markov passive susceptibilities.

Experiment 01 / V7 is frozen. This branch does not modify it.

---

## Main result — passive linear-network cut-set theorem

For a stable passive bosonic endpoint,

```math
A=-iH-\frac12K^\dagger K,
```

partition the external channels into useful local, gravitational, and ordinary-loss ports. Let

```math
P_g(\omega)
```

be the one-way gravitational propagation map between the source and receiver channel spaces, and define

```math
\eta_{\max}
=\sup_{\omega\in\mathcal B}
\|P_g(\omega)\|_{\rm op}^2
\le1.
```

For the complete useful source-to-receiver transfer matrix `T(omega)`, define

```math
\boxed{
\Gamma_{\rm coh}
=\frac1{2\pi}
\int_{\mathcal B}
\operatorname{Tr}[T^\dagger(\omega)T(\omega)]d\omega.
}
```

Then passivity gives

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

The proof uses the passive identity `A+A^dagger=-K^dagger K`, the fact that the complete-channel controllability Gramian is exactly the identity, and contraction of passive scattering subblocks.

This result allows arbitrary coherent internal mode mixing and overlapping resonances. It does **not** require independent scalar channels.

See `PASSIVE_NETWORK_CUTSET_THEOREM.md`.

---

## Single-pole specialization

For one source and one receiver resonance with explicit local input/output ports,

```math
\tau(\Omega)
=
\frac{
\eta_{\rm prop}
\kappa_{\rm in}\kappa_{g,A}\kappa_{g,B}\kappa_{\rm out}
}
{
[\Omega^2+(\kappa_A/2)^2]
[\Omega^2+(\kappa_B/2)^2]
},
```

and

```math
\boxed{
\Gamma_{\rm EBP}
\equiv
\frac1{2\pi}\int_{-\infty}^{\infty}\tau(\Omega)d\Omega
=
\frac{
4\eta_{\rm prop}
\kappa_{\rm in}\kappa_{g,A}\kappa_{g,B}\kappa_{\rm out}
}
{\kappa_A\kappa_B(\kappa_A+\kappa_B)}.
}
```

Therefore

```math
\boxed{
\Gamma_{\rm EBP}
\le
\eta_{\rm prop}\min(\kappa_{g,A},\kappa_{g,B}).
}
```

For symmetric intrinsic gravitational rates with no internal loss, the spectral-area optimum is overcoupled:

```math
\kappa_{\rm in}=\kappa_{\rm out}=2\kappa_g,
```

with

```math
\boxed{
\Gamma_{\rm EBP}^{\rm sym,max}
=\frac8{27}\eta_{\rm prop}\kappa_g.
}
```

See `TWO_PORT_SPECTRAL_BOUND.md`.

---

## Passive matter spectral resource

For a stationary passive nonrelativistic matter system, define the positive quadrupole spectral measure

```math
d\mu_Q(\omega)
=
\sum_{m<n,a}
(p_m-p_n)|Q^a_{mn}|^2
\delta(\omega-\omega_{nm})d\omega.
```

The energy-weighted quadrupole sum rule gives

```math
\int_0^\infty\omega\,d\mu_Q(\omega)
=\frac{10}{3}\hbar\langle I\rangle.
```

Hence the cumulative gravitational transition-rate weight below operating ceiling `Omega`,

```math
K_g(\Omega)
=
\frac{2G}{5\hbar c^5}
\int_0^\Omega\omega^5d\mu_Q(\omega),
```

obeys

```math
\boxed{
K_g(\Omega)
\le
\frac{4G}{3c^5}\langle I\rangle\Omega^4.
}
```

This controls the total passive gravitational oscillator-strength rate of arbitrarily many quadrupole transitions inside a finite operating band.

For passive linear mode networks whose gravitational Markov coupling matrix resolves that same positive spectral weight,

```math
\operatorname{Tr}(K_g^\dagger K_g)
\le K_g(\Omega),
```

and therefore

```math
\boxed{
\Gamma_{\rm coh}
\le
\eta_{\max}
\frac{4G\Omega^4}{3c^5}
\min\!\left(
\langle I_A\rangle,
\langle I_B\rangle
\right).
}
```

This is the current strongest material-level result. See `SPECTRAL_GENERALIZATION.md`.

---

## Pure-loss quantum-information corollaries

`Gamma_coh` is a physical coherent-transfer integral, **not** itself a capacity.

For a stationary vacuum pure-loss realization, every transmission eigenvalue satisfies

```math
\tau_n(\omega)\le\eta_{\max}.
```

Therefore, if

```math
\eta_{\max}\le1/2,
```

the unassisted pure-loss quantum capacity is identically zero:

```math
\boxed{Q_1=0.}
```

For `eta_max < 1`, the two-way-assisted capacity obeys

```math
\boxed{
Q_2
\le
\frac{\Gamma_{\rm coh}}
{\ln2\,(1-\eta_{\max})}.
}
```

Combining with the passive network and material bounds gives an explicit gravity-limited two-way entanglement-distribution rate ceiling within the pure-loss model.

See `CAPACITY_COROLLARIES.md`.

---

## Relation to the V7 aligned quadrupole

For the V7 aligned plus-quadrupole wave-zone channel,

```math
\eta_{\rm prop}
=\frac{25\mathcal O}{16(kR)^2}.
```

The narrowband passive matter result becomes

```math
\boxed{
\Gamma_{\rm EBP}
\lesssim
\frac{25\mathcal O}{24(kR)^2}
\omega
\min\!\left(
\mathcal C_A\beta_A^3,
\mathcal C_B\beta_B^3
\right).
}
```

For the inherited benchmark,

```math
\eta_{\rm prop}\kappa_g
=1.0734375\times10^{-27}\;\mathrm{s}^{-1},
```

whose inverse is about

```math
2.95\times10^{19}\;\mathrm{yr}.
```

This is a coherent-transfer cut-set timescale, not literally a one-qubit waiting time.

---

## What remains open

The key unresolved physics question is now narrower:

> Can the gravitational coupling-trace resource in the passive Markov theorem be replaced directly by a general matrix-valued mass-quadrupole susceptibility/spectral measure for arbitrary interacting passive matter, while retaining a rigorous TT propagation bound?

That is the next theorem target. Active/inverted matter, relativistic systems, nonstationary driving, thermal/noisy capacities, and resource-assisted escapes are later branches.

---

## Validation

Branch-only automated regression checks:

- exact two-pole spectral integral against direct quadrature;
- random passive two-pole rate sets;
- the symmetric `8/27` optimum;
- random multi-mode passive Gramians and endpoint H2 norms;
- direct quadrature of random source–propagation–receiver networks against the cut-set ceiling.

The first GitHub Actions run passed all checks.

---

## Novelty status

**Promising but unverified. Do not claim priority yet.**

A targeted current search has found nearby work on generic quantum-transducer capacity/efficiency-bandwidth limits and on gravitational detector coupling limits, but no inspected source yet combines passive mass-quadrupole spectral weight with an end-to-end gravitational transfer/capacity cut-set theorem.

Read next:

1. `CURRENT_STATE.md`
2. `PASSIVE_NETWORK_CUTSET_THEOREM.md`
3. `CAPACITY_COROLLARIES.md`
4. `TWO_PORT_SPECTRAL_BOUND.md`
5. `SPECTRAL_GENERALIZATION.md`
6. `SINGLE_RESONANCE_BOUND.md`
7. `LITERATURE_MAP.md`
8. `AGENTS.md`
