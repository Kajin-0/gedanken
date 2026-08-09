# Experiment 02 — Passive Gravitational Coherent-Transfer Throughput

## Research question

Can the speed–efficiency tradeoff exposed by Experiment 01 be promoted to a source-architecture-independent bound on coherent transfer through passive, compact, nonrelativistic matter coupled by propagating linearized gravity?

The target is **not** another detailed source model. The target is a hierarchy of increasingly general bounds:

1. exact single-resonance and two-port spectral bounds;
2. a many-resonance cumulative passive spectral-weight bound;
3. a fully coupled susceptibility / TT-scattering theorem;
4. only after the physical bound is secure, operational information-theory corollaries.

Experiment 01 / V7 is frozen. This experiment may reuse established V7 lemmas but must not modify V7 unless an actual defect is discovered.

---

## Result 1 — exact two-port spectral bound

Add explicit local input and output ports to the source and receiver resonators. For total linewidths

```math
\kappa_A
=\kappa_{\rm in}+\kappa_{g,A}+\kappa_{i,A},
```

```math
\kappa_B
=\kappa_{g,B}+\kappa_{\rm out}+\kappa_{i,B},
```

the weak one-way stationary transfer efficiency is

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
}.
```

Define the efficiency-bandwidth integral

```math
\boxed{
\Gamma_{\rm EBP}
\equiv
\frac{1}{2\pi}
\int_{-\infty}^{\infty}\tau(\Omega)d\Omega.
}
```

It evaluates exactly to

```math
\boxed{
\Gamma_{\rm EBP}
=
\frac{
4\eta_{\rm prop}
\kappa_{\rm in}\kappa_{g,A}\kappa_{g,B}\kappa_{\rm out}
}
{\kappa_A\kappa_B(\kappa_A+\kappa_B)}.
}
```

Passivity alone then gives

```math
\boxed{
\Gamma_{\rm EBP}
\le
\eta_{\rm prop}
\min(\kappa_{g,A},\kappa_{g,B}).
}
```

This is stronger than multiplying a chosen bandwidth by peak efficiency: the frequency integral is explicit and contains no bandwidth convention.

For symmetric gravitational linewidths, no internal loss, and symmetric external coupling, the EBP optimum occurs at

```math
\kappa_{\rm in}=\kappa_{\rm out}=2\kappa_g,
```

not at critical coupling, with

```math
\boxed{
\Gamma_{\rm EBP}^{\rm sym,max}
=\frac{8}{27}\eta_{\rm prop}\kappa_g.
}
```

See `TWO_PORT_SPECTRAL_BOUND.md`.

---

## Result 2 — passive matter corollary

For passive compact nonrelativistic matter in a selected narrow band, V7 established

```math
\kappa_{g,j}
\lesssim
\frac23\omega\mathcal C_j\beta_j^3,
```

where

```math
\mathcal C_j=\frac{2GM_j}{c^2L_j},
\qquad
\beta_j=\frac{\omega L_j}{c}.
```

Therefore

```math
\boxed{
\Gamma_{\rm EBP}
\lesssim
\frac23\eta_{\rm prop}\omega
\min\!\left(
\mathcal C_A\beta_A^3,
\mathcal C_B\beta_B^3
\right).
}
```

For the aligned plus-quadrupole wave-zone channel,

```math
\eta_{\rm prop}
=\frac{25\mathcal O}{16(kR)^2},
```

so

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

This is the first gravity-specific efficiency-bandwidth ceiling in the present research program.

---

## Result 3 — cumulative finite-band gravitational spectral weight

For a stationary passive nonrelativistic matter system, define the positive quadrupole spectral measure

```math
d\mu_Q(\omega)
=
\sum_{m<n,a}
(p_m-p_n)|Q^a_{mn}|^2
\delta(\omega-\omega_{nm})d\omega.
```

The EWSR gives

```math
\int_0^\infty\omega\,d\mu_Q(\omega)
=
\frac{10}{3}\hbar\langle I\rangle.
```

Define cumulative gravitational transition-rate weight below `Omega`:

```math
K_g(\Omega)
=
\frac{2G}{5\hbar c^5}
\int_0^\Omega\omega^5d\mu_Q(\omega).
```

Because `omega^5 <= Omega^4 omega` inside the selected band,

```math
\boxed{
K_g(\Omega)
\le
\frac{4G}{3c^5}
\langle I\rangle\Omega^4.
}
```

This is important because it controls the **sum of arbitrarily many passive quadrupole resonances below a finite operating frequency**. No literal ultraviolet cutoff is assumed; spectral weight above `Omega` is simply outside the selected operating band.

See `SPECTRAL_GENERALIZATION.md`.

---

## Current central conjecture

The remaining hard problem is to remove the assumption that the passive device decomposes into independent scalar resonances.

The desired architecture-independent statement is approximately:

> For arbitrary compact passive nonrelativistic source and receiver systems coupled through propagating linearized gravity, the frequency-integrated coherent transfer is bounded by the smaller positive quadrupole spectral resource of the two endpoints, further reduced by the TT propagation operator.

The correct general language should use matrix-valued quadrupole susceptibilities

```math
\chi_A^{ab}(\omega),
\qquad
\chi_B^{ab}(\omega),
```

and the TT propagation operator

```math
G_{\rm TT}^{ab}(\mathbf R,\omega).
```

The next mathematical target is a singular-value / trace inequality connecting passive `Im chi` sum rules to the integrated end-to-end transmission operator.

---

## Metric discipline

Do **not** call `Gamma_EBP` a quantum capacity.

It is a coherent-transfer efficiency-bandwidth integral with units of inverse time. Established continuous-time transducer theory defines genuine quantum capacities by integrating a per-frequency capacity over `d omega / 2 pi`.

For pure loss:

- unassisted one-way quantum capacity vanishes when `tau <= 1/2`;
- two-way-assisted capacity is positive for every `tau > 0`;
- in the weak-link limit,

```math
-\log_2(1-\tau)
=\frac{\tau}{\ln2}+O(\tau^2).
```

Thus a later rigorous EBP bound can generate a weak-link two-way entanglement-rate corollary, but capacity language comes **after** the physical response theorem.

---

## Validation

`numerics/verify_two_port_bound.py` checks

- the closed-form EBP against direct numerical frequency integration;
- random passive rate sets against the universal ceiling;
- the symmetric `8/27` optimum;
- the V7 benchmark rate scale.

Independent exploratory testing over 200,000 random passive rate sets found no violation and produced ratios arbitrarily close to the universal ceiling in strongly asymmetric cases.

---

## Current status

- V7 remains frozen at the submission-ready scientific state.
- Exact algebraic single-resonance bound: **proved**.
- Exact two-port spectral EBP bound: **proved within the stated cascaded Markov model**.
- Cumulative passive finite-band gravitational spectral-weight bound: **proved from the V7 EWSR**.
- Independent parallel-resonance cut-set extension: **derived, with the response-weight identification still to be formalized for general interacting/thermal systems**.
- Fully coupled susceptibility / TT-scattering theorem: **open**.
- Novelty status: **unknown; no priority claim**.

Read next:

1. `AGENTS.md`
2. `CURRENT_STATE.md`
3. `TWO_PORT_SPECTRAL_BOUND.md`
4. `SPECTRAL_GENERALIZATION.md`
5. `SINGLE_RESONANCE_BOUND.md`
6. `LITERATURE_MAP.md`
