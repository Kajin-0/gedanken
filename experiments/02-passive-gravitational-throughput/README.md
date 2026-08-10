# Experiment 02 — Passive Gravitational Throughput

## Question

What frequency-integrated coherent transfer can a **separated passive gravitational link** support when both compact matter interfaces and the propagating TT channel are treated explicitly?

Experiment 01 / V7 is frozen. This branch develops a separate theorem and does not modify V7.

---

## Headline theorem

For compact passive nonrelativistic linear-harmonic source and receiver networks in weak quadrupolar wave-zone gravity,

```math
\Gamma_{\rm coh}
=\frac1{2\pi}\int_{\mathcal B}
\operatorname{Tr}[T^\dagger(\omega)T(\omega)]d\omega
```

obeys, at leading separated-wave-zone order,

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega^2}{12c^3R^2}
\min(I_A,I_B).
}
```

The physical bound is **classical** within this linear-harmonic class. Quantum mechanics reproduces the same oscillator-strength normalization and gives later pure-loss channel/capacity corollaries.

The leading ceiling contains no endpoint quality factor, passive resonance count, coherent internal-mixing parameter, branching fraction, or four-spoke-specific quantity.

---

## Strongest-route upgrades

### Countably infinite passive modal sectors

The selected-port H2 theorem now holds directly for a separable bounded-port passive Markov modal Hilbert space. For the contraction semigroup `T(t)=exp(At)`,

```math
\boxed{
0\le P_u(\tau)
\le I-T(\tau)T^\dagger(\tau)
\le I.
}
```

If the gravitational port is Hilbert--Schmidt,

```math
\boxed{
\|S_{g\leftarrow u}\|_2^2
\le\operatorname{Tr}(K_g^\dagger K_g).
}
```

The gravitational inertia resource itself guarantees

```math
\operatorname{Tr}(K_g^\dagger K_g)<\infty,
```

so countably infinite passive resonance count is covered without a finite-mode loophole.

### Passive recurrent returns

For exact passive endpoint reflection blocks `R_A,R_B`, repeated separated propagation sums to

```math
\boxed{
P_{\rm eff}
=(I-P_{BA}R_AP_{AB}R_B)^{-1}P_{BA}.
}
```

For reciprocal propagation with one-hop power factor `eta`,

```math
\boxed{
\eta_{\rm rec}
\le\frac{\eta}{(1-\eta)^2}.
}
```

Since compact TT propagation has `eta = O((kR)^-2)`,

```math
\boxed{
\eta_{\rm rec}
=\eta+O((kR)^{-4}).
}
```

Thus arbitrarily many passive back-and-forth returns between the same two compact endpoints cannot change the retained leading `1/R^2` coefficient.

---

## Material resource

Historical resonant-mass theory already supplies the long-wavelength STF tidal-force fields and their projection onto elastic normal modes. Applying standard Bessel/Parseval completeness to those fields gives

```math
\boxed{
\sum_n\frac{q_n:q_n}{\mu_n}
\le\frac{20}{3}I.
}
```

Using Hirakawa's gravitational effective area,

```math
A_{Gn}=\frac{2q_n:q_n}{M\mu_n},
```

this becomes

```math
\boxed{
\sum_n M A_{Gn}\le\frac{40}{3}I.
}
```

and therefore

```math
\boxed{
\sum_n\kappa_{g,n}
=\operatorname{Tr}(K_g^\dagger K_g)
\le\frac{4G}{3c^5}I\Omega^4.
}
```

The `20/3` coefficient, tidal influence fields, and modal-completeness method are **not** presented as new mathematics. Lobo's arbitrary-body antenna formalism contains the historical STF tidal/modal ingredients; the exact `40/3` Hirakawa-effective-area sum has not been found explicitly in the inspected sources.

---

## Modern multimode stress test

Tobar, Pikovski, and Tobar's 2025 multimode graviton bar is an apparent many-mode challenge that instead illustrates the resource accounting. Its hybrid normal-mode absorption rates carry factors

```math
\Gamma_{{\rm stim},j}\propto P_{1j}^2 M h^2.
```

Orthogonality of the mass-weighted normal-mode transformation gives

```math
\boxed{
\sum_j|P_{1j}|^2=1.
}
```

so hybridization redistributes the gravitationally driven coordinate rather than creating independent copies of its coupling. The design can still improve readout transduction and spectral coverage substantially.

See `TOBAR_MULTIMODE_BAR_STRESS_TEST_2026-08-09.md`.

---

## Compact TT propagation

```math
\boxed{
\|P_g\|_{\rm op}^2
\le\frac{25}{16(kR)^2}
}
```

at leading wave-zone order.

The same coefficient has both a normalized TT angular-mode derivation and a classical reciprocal-antenna interpretation using `D_A=D_B=5/2`.

---

## Prior-art boundary

The audit explicitly rejects novelty for

- gravitational generator--receiver calculations;
- compact resonant-mass eigenmode and STF tidal-response theory;
- gravitational reciprocity and `D=5/2` directivity;
- `Q`-independent integrated gravitational response;
- gravitational response sum-rule methodology;
- modal participation/effective-mass completeness;
- passive finite/infinite-dimensional H2/Gramian machinery;
- generic singular wave channels and two-body Green-operator bounds;
- multiple-scattering/Redheffer composition.

The only surviving candidate contribution is the **complete gravity-specific two-ended inertia closure**:

```text
passive selected-port spectral-area cut
-> source/receiver gravitational traces
-> cumulative inertia resource at BOTH endpoints
-> compact TT propagation
-> passive recurrence subleading at retained order
-> explicit inertia-only end-to-end ceiling.
```

No inspected primary source has been found stating this exact theorem. That is a negative search result, not a priority claim.

---

## Scope

Included:

- weak linearized gravity;
- separated compact nonrelativistic quadrupolar matter;
- passive linear-harmonic endpoint dynamics;
- finite or countably infinite bounded-port Markov modal sectors;
- repeated passive returns between the same two endpoints at the stated wave-zone asymptotic order.

Excluded:

- active gain/inversion/parametric drive;
- extended phased apertures or additional gravitational relays/mirrors;
- engineered external cavities;
- near-field/reactive exchange;
- nonlinear/relativistic matter;
- unbounded PDE boundary ports without admissibility analysis;
- genuinely non-Markov continua;
- globally sharp/saturable optimality claims.

---

## Validation

The last fully validated pre-attribution checkpoint was

```text
physics:     run 31346367916, job 93328941553 — PASS
manuscript:  run 31346367918, job 93328941582 — PASS
```

The physics suite contains six layers:

1. two-port spectral bound;
2. passive H2 cut set;
3. classical modal sum rule;
4. recurrent passive scattering;
5. TT propagation;
6. microscopic port factorization.

A fresh manuscript build is required after the Lobo/Tobar citation edits before the final checkpoint is frozen.

---

## Read next

1. `CURRENT_STATE.md`
2. `HOSTILE_REFEREE_REPORT_2026-08-09.md`
3. `LOBO_SPHERICAL_MODAL_COMPLETENESS_COLLISION_AUDIT_2026-08-09.md`
4. `TOBAR_MULTIMODE_BAR_STRESS_TEST_2026-08-09.md`
5. `INFINITE_DIMENSIONAL_PASSIVE_H2_AUDIT_2026-08-09.md`
6. `RECURRENT_SCATTERING_WAVEZONE_AUDIT_2026-08-09.md`
7. `HIRAKAWA_EFFECTIVE_AREA_QUANTUM_LINEWIDTH_CROSSCHECK.md`
8. `GENERIC_WAVE_TRANSFER_COLLISION_AUDIT_2026-08-09.md`

## Current status

**Physics theorem: GO within the declared passive compact linear-harmonic separated-wave-zone class.**

**Exact novelty: provisional only for the final gravity-specific inertia closure.**

**Main remaining risk: publication significance/priority, not a known internal technical defect.**

**Next step: specialist external review; do not broaden the theorem further internally without a concrete objection.**
