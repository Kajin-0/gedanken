# AGENTS.md — Experiment 02 Recovery Protocol

## Scope

Experiment 02 studies a passive frequency-integrated throughput ceiling for direct propagating gravitational transduction.

It is separate from Experiment 01 / V7. **Do not modify V7 from this branch.** V7 is an inherited source of audited normalization/examples, not an active derivation target.

## Canonical current result

For compact passive nonrelativistic linear-harmonic endpoints in weak direct one-pass quadrupolar wave-zone gravity,

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
\min(I_A,I_B).
}
```

The headline physical bound is **classical** within this linear-harmonic class. Quantum theory supplies an equivalent one-graviton normalization and downstream pure-loss capacity/entanglement corollaries.

Canonical state:

`CURRENT_STATE.md`

Current manuscript:

`manuscript_v1/`

Current title:

**Passive Throughput Bounds for Propagating Gravitational Transduction**

## Proof skeleton

1. **Passive selected-port H2 cut set**

```math
\Gamma_{\rm coh}
\le
\eta_{\max}
\min[
\operatorname{Tr}(K_{g,A}^\dagger K_{g,A}),
\operatorname{Tr}(K_{g,B}^\dagger K_{g,B})].
```

2. **Classical quadrupole modal resource**

```math
\sum_{ijk}|(g^{ij})_k|^2
=\frac{20}{3}r^2,
```

```math
\sum_n\frac{q_n:q_n}{\mu_n}
\le\frac{20}{3}I,
```

and with Hirakawa's gravitational effective area,

```math
\sum_n M A_{Gn}\le\frac{40}{3}I.
```

For retained modes below `Omega`,

```math
\sum_n\kappa_{g,n}
\le\frac{4G}{3c^5}I\Omega^4.
```

3. **Normalized compact TT propagation**

```math
\|P_g\|_{\rm op}^2
\le\frac{25}{16(kR)^2}.
```

4. Combine the three results to obtain the headline inertia ceiling.

## Important interpretation corrections

Do not restore the superseded quantum-first framing.

The following are now explicit:

- the passive H2 inequality is classical linear-system algebra as well as quantum input-output algebra;
- modal participation / equivalent-modal-mass completeness is standard structural-dynamics methodology;
- `sum M A_G <= 40 I/3` is the gravity-specific STF quadrupole specialization of that completeness machinery;
- the quantum mass-quadrupole EWSR reproduces the same endpoint coefficient but is not needed to prove the present classical bound;
- the `25/16` wave-zone coefficient has a classical reciprocal-antenna interpretation as well as the normalized TT angular-mode derivation;
- quantum capacity statements are corollaries, not the headline theorem.

## Prior-art claim boundary

Do **not** claim novelty for

- gravitational generator--receiver calculations;
- compact gravitational antenna eigenmodes;
- gravitational reciprocity;
- `Q`-independent integrated gravitational response;
- compact real-STF directivity or `D=5/2`;
- gravitational material-response sum rules or quadrupole-commutator sum rules;
- passive H2/Gramian mathematics;
- generic singular source--receiver wave channels;
- generic two-body response + Green-operator transfer bounds;
- modal participation / effective-modal-mass completeness;
- generic use of sum rules to constrain integrated passive response.

The only surviving candidate publication contribution is the exact gravity-specific cumulative two-ended closure

```math
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega^2}{12c^3R^2}
\min(I_A,I_B)
```

and its simultaneous exclusion of passive escape via higher `Q`, more resonances, coherent bright-mode engineering, or compact quadrupole reorientation.

This remains a negative prior-art search result, **not a priority claim**.

## Closed scope clarifications

### Finite versus infinite modal sectors

The H2 theorem applies directly to finite retained band-local sectors. The modal resource bound is uniform in retained mode count. Any countably infinite extension requires the corresponding passive transfer operator to possess the usual trace-class limit.

### Propagation architecture

`P_g` is the direct retarded one-pass/Born wave-zone hop. Do not silently extend the theorem to recurrent source--receiver multiple scattering, strong common-bath hybridization, relays, near-field exchange, or curved-background focusing.

### Sharpness

The theorem is an upper bound. Do not claim the final coefficient is globally saturable. The explicit compact plus mode reaches the correct scaling, 30% of the endpoint material ceiling, and saturates compact TT geometry, but simultaneous saturation of the whole chain is open.

## Validation

Current complete physics regression checkpoint:

```text
run 31344642352
job 93324206747
PASS
```

Current complete manuscript checkpoint:

```text
run 31344642351
job 93324206692
PASS
```

The numerical suite includes the classical modal-sum regression in addition to the exact two-port, passive H2, TT propagation, and microscopic port-factorization checks.

## Canonical reading order

1. `CURRENT_STATE.md`
2. `README.md`
3. `HOSTILE_REFEREE_REPORT_2026-08-09.md`
4. `CLASSICAL_MODAL_SUM_RULE_AND_QUANTUM_SCOPE_AUDIT_2026-08-09.md`
5. `HIRAKAWA_EFFECTIVE_AREA_QUANTUM_LINEWIDTH_CROSSCHECK.md`
6. `HIRAKAWA_NARIHARA_FUJIMOTO_1976_COLLISION_AUDIT.md`
7. `SRIVASTAVA_WIDOM_PIZZELLA_2003_SUM_RULE_COLLISION_AUDIT.md`
8. `STRUCTURAL_DYNAMICS_MODAL_PARTICIPATION_COLLISION_AUDIT.md`
9. `GENERIC_WAVE_TRANSFER_COLLISION_AUDIT_2026-08-09.md`
10. `PASSIVE_NETWORK_CUTSET_THEOREM.md`
11. `GRAVITATIONAL_PORT_FACTORIZATION.md`
12. `TT_PROPAGATION_BOUND.md`
13. `manuscript_v1/`

## Hard stop

Do **not** broaden this paper internally to

- arbitrary interacting/non-Markov matter;
- active/inverted or parametrically driven systems;
- extended phased apertures;
- higher multipoles or relativistic beaming;
- near-field gravity;
- relay/repeater networks;
- curved backgrounds;
- recurrent multiple scattering;
- a universal gravitational quantum-capacity theorem.

Do not restart the old fully general susceptibility program unless an actual external referee objection makes it necessary.

## Next epistemic step

The next useful action is genuine external specialist review, aimed at

1. whether an equivalent inertia-closed two-ended gravitational theorem exists under older antenna, mutual-impedance, scattering, or network language;
2. whether the H2-to-gravitational-continuum / one-pass subsystem boundary hides a physical defect; and
3. whether the exact closure is significant enough for publication when its individual methods are prior art.

Canonical internal adversarial assessment:

`HOSTILE_REFEREE_REPORT_2026-08-09.md`

Absent a concrete external objection, further internal generalization is more likely to dilute the result than strengthen it.
