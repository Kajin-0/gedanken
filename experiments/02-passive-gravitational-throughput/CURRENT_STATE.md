# Current State — Experiment 02

**Checkpoint:** final manuscript freeze audit and bibliography polish.  
**Status:** **PHYSICS THEOREM ESTABLISHED WITHIN THE DECLARED RETAINED-SECTOR BOUNDED-PORT NARROWBAND CLASS; SCOPE-HARDENED MANUSCRIPT AND ALL SIX PHYSICS REGRESSIONS PASSED ON `3cfb62e3...`; FINAL POLISH CI PENDING; NO FURTHER THEOREM BROADENING.**

## 1. Current theorem

Use

```text
omega_0   absolute carrier angular frequency
nu        complex-envelope detuning
B         envelope bandwidth, B/omega_0 << 1
k_0       omega_0/c
a_A,a_B   endpoint radii, k_0 a_A,k_0 a_B << 1
R         separation, k_0 R >> 1
Omega     upper physical frequency of retained endpoint modal sector,
          Omega=omega_0[1+O(B/omega_0)]
I_2       int rho r^2 dV about endpoint COM
```

Define

```math
\Gamma_{\rm coh}
=\frac1{2\pi}\int_{\mathcal B_\nu}
\operatorname{Tr}[T^\dagger(\nu)T(\nu)]\,d\nu.
```

For separated compact passive nonrelativistic linear-harmonic endpoints in weak leading mass-quadrupole gravity, with finite or countably infinite bounded-port Markov retained modal sectors,

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega_0^2}{12c^3R^2}
\min(I_{2,A},I_{2,B}).
}
```

`Gamma_coh` has units `s^-1` and is a coherent-transfer spectral area, not an information capacity.

The carrier-scale resource does not automatically cover uncontrolled modes with `omega_n >> omega_0`; off-resonant higher-frequency sectors require a separate bound.

## 2. Proof spine

### Passive cut

```math
\Gamma_{\rm coh}
\le
\eta_{\max}
\min[
\operatorname{Tr}(K_{g,A}^\dagger K_{g,A}),
\operatorname{Tr}(K_{g,B}^\dagger K_{g,B})].
```

The band integral is bounded by the full-line selected-port `H2` norm because the integrand is nonnegative.

File: `PASSIVE_SELECTED_PORT_CUT_DERIVATION.md`.

### Endpoint resource

```math
\sum_n\frac{q_n:q_n}{\mu_n}\le\frac{20}{3}I_2,
```

and, for `omega_n <= Omega`,

```math
\operatorname{Tr}(K_g^\dagger K_g)
\le\frac{4G}{3c^5}I_2\Omega^4
\lesssim\frac{4G}{3c^5}I_2\omega_0^4.
```

File: `GRAVITATIONAL_ENDPOINT_RESOURCE_DERIVATION.md`.

### Compact TT propagation

```math
\limsup_{kR\to\infty}(kR)^2\|P_g\|_{\rm op}^2
\le\frac{25}{16}.
```

File: `TT_PROPAGATION_BOUND_DERIVATION.md`.

### Assembly

```math
(25/16)\times(4/3)=25/12,
```

with `k_0=omega_0/c`.

File: `FINITE_TWO_ENDED_INERTIA_BOUND.md`.

## 3. Infinite modal and recurrence closure

Countably infinite separable **bounded-port Markov** modal sectors are covered when the gravitational port is Hilbert--Schmidt; the retained endpoint resource gives the required finite trace.

File: `INFINITE_DIMENSIONAL_BOUNDED_PORT_EXTENSION.md`.

Same-two-endpoint passive recurrence obeys

```math
\|P_{\rm eff}\|^2\le\frac{\eta}{(1-\eta)^2},
```

so recurrence changes only subleading terms in the leading `1/R^2` upper ceiling. This is not equality for actual recurrent transfer.

File: `PASSIVE_TWO_ENDPOINT_RECURRENCE.md`.

## 4. Manuscript

Active source:

`manuscript_v1/`

Title:

**An Inertia-Controlled Throughput Bound for Passive Gravitational Transduction**

The first manuscript adversarial audit is:

`MANUSCRIPT_V1_ADVERSARIAL_AUDIT_2026-08-10.md`

It found no coefficient failure and required three scope hardenings now present in the manuscript:

1. retained carrier-scale endpoint modal sector;
2. explicit `k_0 a << 1` and `k_0 R >> 1` conditions;
3. explicit band-integral-to-full-line-`H2` positivity step.

The final freeze audit is:

`MANUSCRIPT_V1_FINAL_FREEZE_AUDIT_2026-08-10.md`

It found no new physics defect. It corrected two bibliography metadata entries and minor wording only. Fresh exact-head CI is required before the final freeze verdict is promoted to canonical.

## 5. Scope-hardening validation — exact real head

Scope-hardening commit:

```text
3cfb62e31dfb0905955050f963bdc2bf93706c9e
```

All seven Experiment-02 gates passed:

```text
passive cut        run 31429039197 — PASS
endpoint resource  run 31429039518 — PASS
TT propagation     run 31429039529 — PASS
combined bound     run 31429039256 — PASS
infinite modal     run 31429039819 — PASS
recurrence         run 31429039531 — PASS
manuscript         run 31429039874, job 93587616997 — PASS
```

The manuscript compiled to 10 pages with no unresolved references/citations after the final LaTeX pass.

Artifact:

```text
name: experiment02-manuscript-v1
artifact ID: 9078372416
ZIP SHA256: 9dac950d7f9136aaa8608e82eed819ed23544f5ce50cd9b927357540f8c39026
```

## 6. Historical / novelty boundary

Read:

- `HOSTILE_PRIOR_ART_COLLISION_AUDIT.md`
- `META_REFEREE_SIGNIFICANCE_AUDIT.md`
- `CLAIM_LEDGER.md`

Most ingredients are historical. No standalone novelty claim is made for resonant-mass integrated response, gravitational-antenna modal theory/directivity, arbitrary-body multimode response, material sum rules, generic passive `H2`, generic wave-channel bounds, multiple scattering, or the `20/3` and `4/3` lemmas.

No inspected source states the exact complete two-ended inertia closure. This is a negative search result, not proof of priority.

## 7. Exclusions

No claim is made for

- broad absolute-frequency operation with one carrier coefficient;
- uncontrolled higher-frequency off-resonant endpoint sectors;
- arbitrary unbounded PDE boundary-control ports;
- genuinely non-Markov continua;
- added relays, external mirrors/cavities, or extended phased apertures;
- reactive near-field exchange;
- active gain/pumping/feedback;
- higher-multipole-dominated, relativistic, nonlinear, or strong-field regimes.

## 8. Current research mode

Do not broaden the theorem further without a concrete defect.

Immediate sequence:

1. commit the final bibliography/wording polish and freeze audit;
2. require fresh manuscript plus all six physics workflows on that exact head;
3. if all pass, record a docs-only canonical freeze checkpoint;
4. reserve further technical changes for a concrete external specialist/journal objection.
