# Experiment 02 — Passive Gravitational Coherent-Transfer Throughput

## Research question

Can the speed–efficiency tradeoff exposed by Experiment 01 be promoted to a source-architecture-independent bound on coherent transfer through passive, compact, nonrelativistic matter coupled by propagating linearized gravity?

The target is **not** another detailed source model. The target is a hierarchy of increasingly general bounds:

1. an exact algebraic single-resonance bound;
2. a frequency-domain passive linear-response formulation;
3. an integrated spectral bound using positive quadrupole spectral weight and the energy-weighted sum rule;
4. only after the physical bound is secure, operational information-theory corollaries.

Experiment 01 / V7 is frozen. This experiment may reuse established V7 lemmas but must not modify V7 unless an actual defect is discovered.

---

## Stage 1 target

For the V7 narrowband Markov link,

```math
\tau_c(t)=
\eta_{\rm prop}\,
\frac{\kappa_{g,A}}{\kappa_A}
\frac{\kappa_{g,B}}{\kappa_B}
\mathcal T_f(t),
\qquad 0\le\mathcal T_f\le1,
```

define the linewidth scale

```math
B_\kappa\equiv\min(\kappa_A,\kappa_B)
```

and the linewidth-weighted coherent-transfer scale

```math
\Gamma_\kappa
\equiv
B_\kappa\sup_t\tau_c(t).
```

The first theorem candidate is

```math
\boxed{
\Gamma_\kappa
\le
\eta_{\rm prop}
\min(\kappa_{g,A},\kappa_{g,B}).
}
```

This removes the apparent high-Q loophole: reducing ordinary damping can make each gravitational branching fraction approach unity, but the available linewidth then approaches the intrinsically tiny gravitational linewidth.

For the aligned single-quadrupole wave-zone specialization,

```math
\eta_{\rm prop}=\frac{25\mathcal O}{16(kR)^2},
```

and the passive V7 sum-rule bound

```math
\frac{\kappa_{g,j}}{\omega}
\lesssim
\frac23\mathcal C_j\beta_j^3
```

implies the candidate corollary

```math
\boxed{
\Gamma_\kappa
\lesssim
\frac{25\mathcal O}{24(kR)^2}
\omega
\min\!\left(
\mathcal C_A\beta_A^3,
\mathcal C_B\beta_B^3
\right).
}
```

The single-resonance result is only the entry point. A true architecture-independent theorem must replace the scalar linewidths by total positive quadrupole spectral weight so that many parallel resonances cannot evade the bound.

---

## Metric discipline

Do **not** call `Gamma_kappa` a quantum capacity.

`Gamma_kappa` is a coherent-transfer rate scale with units of inverse time. A genuine continuous-time quantum-capacity statement requires a frequency-dependent channel and an explicit capacity integral. For pure loss, one-way capacity vanishes below 50% transmissivity even though coherent branch dependence and two-way-assisted entanglement distribution can remain nonzero.

The eventual preferred broadband object is expected to have the form

```math
\Gamma_{\rm coh}
=\frac{1}{2\pi}
\int_{\mathcal B} d\Omega\,\tau(\Omega),
```

or a closely related response integral. This eliminates arbitrary bandwidth conventions and hidden factors of `2 pi`.

---

## Stage 2 target — arbitrary passive spectra

For each endpoint define the positive quadrupole spectral measure schematically by

```math
d\mu_Q(\omega)
=
\sum_{m<n,A}
(p_m-p_n)
|Q^A_{mn}|^2
\delta(\omega-\omega_{nm})\,d\omega.
```

The V7 energy-weighted sum rule gives

```math
\int_0^\infty \omega\,d\mu_Q(\omega)
=
\frac{10}{3}\hbar\langle I\rangle.
```

Gravitational transition weight scales as `omega^5 dmu_Q`. Therefore the EWSR alone does **not** control an unrestricted ultraviolet spectrum. The nonrelativistic compact regime must enter explicitly, for example through a validity cutoff `omega_max L / c << 1`, higher spectral moments, or a stronger response theorem.

This ultraviolet issue is a central research problem, not a detail to hide.

---

## Stage 3 target — TT propagation operator

The scalar `25/16` factor is not universal for arbitrary source/receiver tensors. The general theory should use the transverse-traceless propagation operator

```math
G_{\rm TT}^{ijkl}(\mathbf R,\omega)
```

between source and receiver quadrupole response tensors. The aligned plus-quadrupole result should emerge as a singular-channel/single-mode specialization rather than being assumed at the outset.

---

## Stage 4 — information-theory corollaries

Only after the physical spectral bound is proved should it be mapped to operational quantities such as

- continuous-time two-way-assisted pure-loss capacity;
- weak-link entanglement-distribution rate;
- noisy thermal-loss upper/lower bounds.

The primary theorem should remain a passive gravitational response bound, not depend on a particular coding theorem.

---

## Current status

- V7 source-resolved link and passive EWSR are inherited as established inputs, not rederived here.
- The single-resonance inequality has a short exact proof; see `SINGLE_RESONANCE_BOUND.md`.
- The broadband susceptibility theorem is **not yet proved**.
- No novelty claim is made yet.

Read next:

1. `AGENTS.md`
2. `CURRENT_STATE.md`
3. `SINGLE_RESONANCE_BOUND.md`
4. `SPECTRAL_GENERALIZATION.md`
5. `LITERATURE_MAP.md`
