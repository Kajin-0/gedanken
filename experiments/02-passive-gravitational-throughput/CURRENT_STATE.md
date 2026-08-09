# Current State — Experiment 02

**Status:** **COMPACT PASSIVE LINEAR-BOSONIC THROUGHPUT THEOREM CLOSED; NOVELTY NARROWED TO TWO-ENDED GRAVITATIONAL QUANTUM CUT SET; MANUSCRIPT HARDENING NEXT**

## 1. Research question

Can the speed–efficiency tradeoff exposed by Experiment 01 be promoted to an end-to-end passive gravitational throughput bound that cannot be evaded by arbitrarily high Q, many resonances, coherent mode mixing, or a different compact quadrupole orientation?

Current answer:

> **Yes for stable passive linear bosonic matter networks coupled through compact quadrupole radiation in the weak one-way wave zone.**

Experiment 01 / V7 remains frozen and is not modified by this branch.

---

## 2. Physical throughput metric

For the stationary source-to-receiver transfer matrix `T(omega)`, define

```math
\boxed{
\Gamma_{\rm coh}
=\frac1{2\pi}
\int_{\mathcal B}
\operatorname{Tr}[T^\dagger(\omega)T(\omega)]d\omega.
}
```

`Gamma_coh` has units of inverse time. It is a frequency-integrated coherent-transfer / efficiency-bandwidth quantity, **not itself a quantum capacity**.

---

## 3. Passive-network cut set

For a stable completely passive endpoint,

```math
A=-iH-\frac12K^\dagger K.
```

Established passive-system theory gives the full-channel Gramian identity `P=I`. Selecting the useful local ports and gravitational ports then yields

```math
\boxed{
\|S_{g\leftarrow u}\|_2^2
\le
\operatorname{Tr}(K_g^\dagger K_g).
}
```

For source and receiver connected by one-way gravitational propagation `P_g(omega)`, define

```math
\eta_{\max}
=\sup_{\omega\in\mathcal B}\|P_g(\omega)\|_{\rm op}^2.
```

Then

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

This permits arbitrary finite-dimensional passive coherent mode mixing and overlapping resonances. The Gramian/H2 mathematics is **not claimed new**; the candidate contribution is its gravitational end-to-end closure.

Canonical derivation: `PASSIVE_NETWORK_CUTSET_THEOREM.md`.

---

## 4. Microscopic gravitational-port factorization

For a narrow frequency sector, let the microscopic matter-to-graviton coupling be

```math
G=V\Gamma_g^{1/2},
\qquad
\Gamma_g=G^\dagger G.
```

Then free graviton propagation `U_R` produces the normalized interface map

```math
P_g=V_B^\dagger U_RV_A,
```

and the complete matter-to-matter gravitational coupling factorizes as

```math
\boxed{
G_B^\dagger U_RG_A
=
\Gamma_{g,B}^{1/2}
P_g
\Gamma_{g,A}^{1/2}.
}
```

This separates endpoint oscillator-strength/linewidth magnitude from normalized angular-polarization propagation and prevents double counting.

Canonical derivation: `GRAVITATIONAL_PORT_FACTORIZATION.md`.

---

## 5. Material resource — closed for passive linear bosonic matter

Diagonalizing the isolated linear matter Hamiltonian gives

```math
\boxed{
\operatorname{Tr}(K_g^\dagger K_g)
=\sum_n\kappa_{g,n}.
}
```

For a one-quantum compact quadrupole transition,

```math
\kappa_{g,n}
=
\frac{2G\omega_n^5}{5\hbar c^5}
Q_{ij}^{0n}Q_{ij}^{n0}.
```

The internal inertia moment is defined about each endpoint center of mass,

```math
I=\sum_a m_a|\mathbf r_a-\mathbf R_{\rm CM}|^2.
```

For retained quadrupole-active modes below operating ceiling `Omega`, the EWSR gives

```math
\boxed{
\operatorname{Tr}(K_g^\dagger K_g)
\le
\frac{4G}{3c^5}\langle I\rangle\Omega^4.
}
```

Therefore

```math
\boxed{
\Gamma_{\rm coh}
\le
\eta_{\max}
\frac{4G\Omega^4}{3c^5}
\min(\langle I_A\rangle,\langle I_B\rangle).
}
```

Canonical derivations: `MATERIAL_RESPONSE_BRIDGE.md`, `SPECTRAL_GENERALIZATION.md`.

---

## 6. TT geometry — closed for compact quadrupole wave-zone channels

For arbitrary complex STF quadrupole `Q`,

```math
D_Q(\hat n)
=
\frac52
\frac{Q^*:\Lambda(\hat n):Q}{Q^*:Q}
\le\frac52.
```

The direct normalized one-graviton stationary-phase overlap gives

```math
\boxed{
t_{BA}^{\rm TT}
=
-\frac{5i}{4kR}e^{ikR}
\frac{Q_B^*:\Lambda(\hat R):Q_A}
{\sqrt{Q_A^*:Q_A}\sqrt{Q_B^*:Q_B}}
+O((kR)^{-2}).
}
```

Hence

```math
\boxed{
\|P_g(\omega)\|_{\rm op}^2
\le
\frac{25}{16[k(\omega)R]^2}
}
```

at leading wave-zone order. Matched line-of-sight TT quadrupoles saturate the projector inequality.

Canonical derivation: `TT_PROPAGATION_BOUND.md`.

---

## 7. Headline narrowband theorem

Combining the endpoint material resource and compact TT propagation ceiling gives

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25}{16(kR)^2}
\frac{4G\omega^4}{3c^5}
\min(\langle I_A\rangle,\langle I_B\rangle).
}
```

Since `k=omega/c`,

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega^2}{12c^3R^2}
\min(\langle I_A\rangle,\langle I_B\rangle).
}
```

This expression contains no endpoint Q, no number of passive internal modes, and no four-spoke-specific parameter.

The theorem is restricted to direct compact nonrelativistic quadrupole links in weak linearized gravity, with stable passive linear bosonic endpoints and narrowband/band-local Markov dynamics.

Canonical synthesis: `THEOREM_SYNTHESIS.md`.

---

## 8. Exact single-pole checkpoint

For one source and receiver pole with explicit local input/output ports,

```math
\boxed{
\Gamma_{\rm EBP}
=
\frac{4\eta_{\rm prop}
\kappa_{\rm in}\kappa_{g,A}\kappa_{g,B}\kappa_{\rm out}}
{\kappa_A\kappa_B(\kappa_A+\kappa_B)}
\le
\eta_{\rm prop}\min(\kappa_{g,A},\kappa_{g,B}).
}
```

For symmetric intrinsic gravitational rates and no internal loss,

```math
\kappa_{\rm in}=\kappa_{\rm out}=2\kappa_g
```

maximizes the integrated area, giving

```math
\boxed{
\Gamma_{\rm EBP}^{\rm sym,max}
=\frac8{27}\eta_{\rm prop}\kappa_g.
}
```

Canonical derivation: `TWO_PORT_SPECTRAL_BOUND.md`.

---

## 9. Capacity corollaries

For a stationary vacuum pure-loss realization, each transmission eigenvalue satisfies

```math
\tau_n(\omega)\le\eta_{\max}.
```

If `eta_max <= 1/2`, the unassisted continuous-time pure-loss quantum capacity is

```math
\boxed{Q_1=0.}
```

For `eta_max < 1`, the two-way-assisted rate obeys

```math
\boxed{
Q_2
\le
\frac{\Gamma_{\rm coh}}
{\ln2\,(1-\eta_{\max})}.
}
```

These are operational corollaries, not the definition of `Gamma_coh` and not universal noisy-gravity capacity statements.

Canonical derivation: `CAPACITY_COROLLARIES.md`.

---

## 10. Explicit V7 realization vs theorem ceiling

In the long-wavelength V7 source,

```math
\kappa_g^{\rm V7}
\to
\frac{8G\mu L^2\omega^4}{5c^5},
```

while the endpoint-only EWSR ceiling for `I=4 mu L^2` is

```math
\kappa_{g,\rm EWSR}^{\max}
=\frac{16G\mu L^2\omega^4}{3c^5}.
```

Therefore

```math
\frac{\kappa_{g,\rm EWSR}^{\max}}
{\kappa_g^{\rm V7}}
=\frac{10}{3}.
```

The explicit mode carries 30% of the endpoint-only material ceiling and its plus tensor saturates the compact TT geometry ceiling. The final end-to-end theorem is not claimed globally sharp.

See `BENCHMARK_THEOREM_COMPARISON.md`.

---

## 11. Critical prior-art update

The easy novelty story is no longer allowed.

Historical resonant-mass gravitational-wave antenna theory already computes absorption cross sections and their frequency integrals. In that literature, increasing Q raises the resonant peak while reducing bandwidth, leaving an integrated response governed by oscillator strength/material parameters rather than by Q alone.

Material-susceptibility descriptions of gravitational absorption are also established, including Kubo/elastic-response treatments of metallic antennas.

Therefore the following are **not** Experiment 02 novelty claims:

- Q-independent integrated gravitational response;
- integrated gravitational absorption cross sections;
- gravitational absorption written in susceptibility language;
- passive Gramian/H2 theory;
- generic efficiency-bandwidth quantum-transducer bounds.

The potential contribution is narrower:

```text
historical one-sided gravitational response
+ known passive network identities
-> two-ended gravitational interface cut set
-> source and receiver quadrupole spectral resources
-> normalized propagating TT channel
-> end-to-end integrated coherent-transfer ceiling
-> capacity corollary.
```

A targeted search has also found near-field laboratory transmitter–receiver gravitational coupling and active electromagnetic GW emission/reception proposals. These are important neighboring architectures but lie outside the present direct passive far-field compact-quadrupole class.

No inspected source yet states the same two-ended passive far-field theorem. This is a negative search result, not proof of priority.

See `LITERATURE_MAP.md` and `INITIAL_NOVELTY_SWEEP.md`.

---

## 12. Validation

Automated branch regression covers:

1. exact two-pole spectral integral and random passive rate sets;
2. random multi-mode passive Gramians, endpoint H2 bounds, and directly integrated cascades;
3. random complex STF quadrupoles, TT directivity, angular normalization, and the `25/16` wave-zone coefficient.

GitHub Actions run `31310582891`, job `93237694140`, completed successfully with all three regression stages passing.

An adversarial theorem audit found no fatal internal gap within the declared class and identified the correct remaining risks as novelty collision, scope creep, and global sharpness.

See `ADVERSARIAL_THEOREM_AUDIT.md`.

---

## 13. Strongest next step

Do **not** broaden to arbitrary interacting matter yet.

The next work should be publication hardening:

1. finish the targeted historical two-antenna / reciprocity / scattering collision search;
2. independently rederive the TT stationary-phase coefficient and gravitational-port factorization in manuscript notation;
3. write a short theorem-first manuscript outline centered on the two-ended closure, explicitly crediting historical integrated resonant-mass response;
4. keep the V7 four-spoke source only as a concrete near-ceiling example;
5. only after that decide whether a full manuscript is justified.

### Forbidden for now

- “first gravitational efficiency-bandwidth bound”;
- “new Q-independent gravitational response law”;
- “universal gravitational quantum capacity bound”;
- “all passive matter”;
- first/unique/unprecedented claims;
- applying `25/16` to extended arrays, higher multipoles, or the near field;
- merging Experiment 02 into V7.
