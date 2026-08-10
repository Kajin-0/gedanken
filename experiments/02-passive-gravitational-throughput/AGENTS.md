# AGENTS.md — Experiment 02 Recovery Protocol

## Scope

Experiment 02 studies a frequency-integrated passive throughput ceiling for **separated propagating gravitational transduction**.

It is separate from Experiment 01 / V7. **Do not modify V7 from this branch.** V7 is an inherited source of audited normalization/examples, not an active derivation target.

## Canonical current result

For compact passive nonrelativistic linear-harmonic endpoints in weak quadrupolar wave-zone gravity,

```math
\Gamma_{\rm coh}
=\frac1{2\pi}\int_{\mathcal B}
\operatorname{Tr}[T^\dagger(\omega)T(\omega)]d\omega
```

obeys at leading separated-wave-zone order

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega^2}{12c^3R^2}
\min(I_A,I_B).
}
```

The headline physical bound is **classical**. Quantum theory supplies an equivalent one-graviton normalization and downstream pure-loss capacity/entanglement corollaries.

Canonical state: `CURRENT_STATE.md`.

Current manuscript: `manuscript_v1/`.

Current title: **Passive Throughput Bounds for Propagating Gravitational Transduction**.

## Proof skeleton

1. Passive selected-port H2 cut set:

```math
\Gamma_{\rm coh}
\le
\eta_{\max}
\min[
\operatorname{Tr}(K_{g,A}^\dagger K_{g,A}),
\operatorname{Tr}(K_{g,B}^\dagger K_{g,B})].
```

2. Historical STF tidal fields + standard modal completeness:

```math
\sum_n\frac{q_n:q_n}{\mu_n}
\le\frac{20}{3}I,
\qquad
\sum_n M A_{Gn}\le\frac{40}{3}I.
```

3. Hirakawa normalization:

```math
\kappa_{g,n}
=\frac{GMA_{Gn}\omega_n^4}{10c^5},
```

hence

```math
\operatorname{Tr}(K_g^\dagger K_g)
=\sum_n\kappa_{g,n}
\le\frac{4G}{3c^5}I\Omega^4.
```

4. Compact TT propagation:

```math
\|P_g\|_{\rm op}^2
\le\frac{25}{16(kR)^2}.
```

5. Combine the endpoint resources and propagation factor to obtain the inertia-only ceiling.

## Strongest-route closures — do not reopen without a concrete defect

### Countably infinite bounded-port modal sectors

Finite internal dimension is **not** required in the bounded-port Markov modal class.

For the contraction semigroup `T(t)=exp(At)`,

```math
\boxed{
0\le P_u(\tau)
\le I-T(\tau)T^\dagger(\tau)
\le I.
}
```

If `K_g` is Hilbert--Schmidt, operator-valued Plancherel gives the same H2 endpoint bound. The material theorem guarantees

```math
\operatorname{Tr}(K_g^\dagger K_g)<\infty,
```

so `K_g` is Hilbert--Schmidt in the retained band.

Do not revert to the statement that "arbitrarily many modes" means only every finite truncation.

Still excluded: unbounded PDE boundary ports and genuinely non-Markov continua without additional admissibility analysis.

Canonical audit: `INFINITE_DIMENSIONAL_PASSIVE_H2_AUDIT_2026-08-09.md`.

### Passive repeated returns between the same two endpoints

The exact separated repeated-return propagator is

```math
P_{\rm eff}
=(I-P_{BA}R_AP_{AB}R_B)^{-1}P_{BA}.
```

For reciprocal propagation with one-hop power factor `eta`,

```math
\boxed{
\eta_{\rm rec}
\le\frac{\eta}{(1-\eta)^2}
=\eta+O((kR)^{-4}).
}
```

Since the headline propagation factor is `O((kR)^-2)`, passive recurrence between the same two compact endpoints cannot change the retained leading coefficient.

Do not restore the statement that all recurrent scattering is excluded. Instead say that **two-endpoint passive recurrence is controlled and subleading at retained wave-zone order**.

Still excluded: added relays/mirrors, engineered extended cavities, near-field exchange, active feedback, and nonseparable overlapping interaction regions.

Canonical audit: `RECURRENT_SCATTERING_WAVEZONE_AUDIT_2026-08-09.md`.

## Historical interpretation corrections

Do not restore the quantum-first framing or overclaim the modal sum.

The following are explicit:

- the passive H2 inequality is classical linear-system algebra as well as quantum input-output algebra;
- infinite-dimensional H2/Gramian machinery is established systems theory;
- Lobo's arbitrary-body resonant-mass formalism already contains the long-wavelength STF tidal fields and their projection onto mass-orthogonal elastic modes;
- modal participation / equivalent-modal-mass completeness is standard structural dynamics;
- STF tensor completeness is historical gravitational-antenna machinery;
- the `20/3` coefficient is a short consequence of those ingredients and is **not** to be presented as new mathematics;
- the exact `sum M A_G <= 40 I/3` form has not been found explicitly, but its role is an intermediate closure rather than the primary novelty claim;
- the quantum EWSR reproduces the same endpoint coefficient but is not needed for the classical theorem;
- the `25/16` coefficient has both normalized TT and classical reciprocal-antenna derivations;
- Redheffer/multiple-scattering composition is prior art;
- quantum capacity statements are corollaries.

Canonical historical audit: `LOBO_SPHERICAL_MODAL_COMPLETENESS_COLLISION_AUDIT_2026-08-09.md`.

## Modern multimode stress test

Tobar--Pikovski--Tobar (2025) is a useful apparent counterexample and should be interpreted correctly.

Their hybrid normal-mode absorption rates contain

```math
\Gamma_{{\rm stim},j}\propto P_{1j}^2Mh^2.
```

Mass-weighted normal-mode orthogonality gives

```math
\sum_j|P_{1j}|^2=1.
```

Therefore passive hybridization redistributes the gravitationally driven coordinate; it does not create `N` copies of its oscillator strength. Their design improves readout transduction and spectral coverage, which Experiment 02 does not prohibit.

Canonical audit: `TOBAR_MULTIMODE_BAR_STRESS_TEST_2026-08-09.md`.

## Prior-art claim boundary

Do **not** claim novelty for

- gravitational generator--receiver calculations;
- compact gravitational antenna eigenmodes;
- long-wavelength STF tidal-force/modal theory;
- gravitational reciprocity;
- `Q`-independent integrated gravitational response;
- compact real-STF directivity or `D=5/2`;
- gravitational material-response or quadrupole-commutator sum-rule methods;
- passive finite/infinite-dimensional H2/Gramian mathematics;
- generic singular source--receiver wave channels;
- generic two-body response + Green-operator bounds;
- modal participation / effective-modal-mass completeness;
- multiple-scattering / Redheffer composition;
- generic use of sum rules to constrain integrated passive response.

The only surviving candidate publication contribution is the exact gravity-specific cumulative two-ended closure

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega^2}{12c^3R^2}
\min(I_A,I_B).
}
```

Its physical value is simultaneous exclusion of passive escape via

```text
higher Q
finite or countably infinite resonances
coherent bright-mode engineering
compact quadrupole reorientation
passive repeated returns between the same endpoints.
```

This remains a negative prior-art search result, **not a priority claim**.

## Sharpness

The theorem is an upper bound. Do not claim the final coefficient is globally saturable. The explicit compact plus mode reaches the correct scaling, 30% of the endpoint material ceiling, and saturates compact TT geometry, but simultaneous saturation of the whole chain is open.

## Validation

Canonical strongest-route validation:

```text
manuscript:  run 31346901851, job 93330404771 — PASS
physics:     run 31347058681, job 93330821747 — PASS
```

The manuscript compile, unresolved citation/reference scan, and PDF upload passed after the Lobo/Tobar attribution edits.

Physics CI contains six passing regressions:

1. exact two-port spectral bound;
2. passive H2 cut set;
3. classical modal resource;
4. recurrent passive scattering;
5. TT propagation;
6. microscopic port factorization.

Use these runs as the canonical validation for this frozen checkpoint unless the manuscript or physics code changes afterward.

## Canonical reading order

1. `CURRENT_STATE.md`
2. `README.md`
3. `HOSTILE_REFEREE_REPORT_2026-08-09.md`
4. `LOBO_SPHERICAL_MODAL_COMPLETENESS_COLLISION_AUDIT_2026-08-09.md`
5. `TOBAR_MULTIMODE_BAR_STRESS_TEST_2026-08-09.md`
6. `INFINITE_DIMENSIONAL_PASSIVE_H2_AUDIT_2026-08-09.md`
7. `RECURRENT_SCATTERING_WAVEZONE_AUDIT_2026-08-09.md`
8. `CLASSICAL_MODAL_SUM_RULE_AND_QUANTUM_SCOPE_AUDIT_2026-08-09.md`
9. `HIRAKAWA_EFFECTIVE_AREA_QUANTUM_LINEWIDTH_CROSSCHECK.md`
10. `GENERIC_WAVE_TRANSFER_COLLISION_AUDIT_2026-08-09.md`
11. `manuscript_v1/`

## Hard stop

Do **not** broaden this paper internally to

- arbitrary interacting/non-Markov matter;
- unbounded PDE boundary control without necessity;
- active/inverted or parametrically driven systems;
- extended phased apertures;
- higher multipoles or relativistic beaming;
- near-field gravity;
- relay/repeater networks or external cavities;
- curved backgrounds;
- a universal gravitational quantum-capacity theorem.

Do not restart the old fully general susceptibility program unless an actual external referee objection makes it necessary.

## Next epistemic step

The next useful action is genuine external specialist review aimed at

1. whether an equivalent inertia-closed two-ended gravitational theorem exists under older antenna, mutual-impedance, cross-section, or network language;
2. whether the bounded-port separated-scattering representation hides a physical defect outside the already closed recurrence problem; and
3. whether the exact closure is significant enough for publication when its individual methods are prior art.

Absent a concrete external objection, further internal generalization is more likely to dilute the result than strengthen it.
