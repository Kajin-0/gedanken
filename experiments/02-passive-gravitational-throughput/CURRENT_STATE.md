# Current State — Experiment 02

**Status:** **CLASSICAL PASSIVE THROUGHPUT THEOREM STRENGTHENED; COUNTABLY INFINITE BOUNDED-PORT MODAL SECTORS COVERED; TWO-ENDPOINT PASSIVE RECURRENCE CLOSED AT LEADING WAVE-ZONE ORDER; STANDALONE MODAL-SUM NOVELTY NARROWED BY HISTORICAL ANTENNA THEORY; FINAL TWO-ENDED INERTIA CLOSURE REMAINS THE ONLY CANDIDATE NOVELTY**

## 1. Headline physical theorem

For a separated narrowband link between compact passive nonrelativistic **linear-harmonic** source and receiver networks in weak quadrupolar wave-zone gravity, define

```math
\Gamma_{\rm coh}
=\frac1{2\pi}\int_{\mathcal B}
\operatorname{Tr}[T^\dagger(\omega)T(\omega)]d\omega.
```

The retained leading-order theorem is

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega^2}{12c^3R^2}
\min(I_A,I_B).
}
```

`I_A` and `I_B` are internal mass inertia moments about the endpoint centers of mass.

The ceiling is **classical** within the declared linear-harmonic class. It contains no endpoint quality factor, passive resonance count, internal coherent-mixing parameter, branching fraction, or four-spoke-specific parameter. Quantum theory reproduces the same oscillator-strength normalization and supplies downstream channel/capacity corollaries.

Experiment 01 / V7 remains frozen and is not modified by this branch.

---

## 2. Passive endpoint theorem — finite and countably infinite modal sectors

For an energy-normalized passive realization,

```math
A=-iH-\frac12K^\dagger K,
```

the selected-port cut set is

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

The finite-dimensional Gramian proof extends directly to a separable Hilbert-space modal sector with bounded Markov port operator `K`. If `T(t)=e^{At}` is the contraction semigroup,

```math
P_u(\tau)
=\int_0^\tau
T(t)K_u^\dagger K_uT^\dagger(t)dt
```

obeys

```math
\boxed{
0\le P_u(\tau)
\le I-T(\tau)T^\dagger(\tau)
\le I.
}
```

The monotone strong limit gives `0 <= P_u <= I`. If `K_g` is Hilbert--Schmidt, operator-valued Plancherel yields the same H2 inequality,

```math
\boxed{
\|S_{g\leftarrow u}\|_2^2
\le\operatorname{Tr}(K_g^\dagger K_g).
}
```

The gravitational material theorem below guarantees precisely this Hilbert--Schmidt regularity in the retained band.

Therefore **countably infinite passive resonance count is covered directly** for the bounded-port Markov modal class. The theorem does not claim arbitrary unbounded PDE boundary ports or genuinely non-Markov matter continua.

Canonical file:

- `INFINITE_DIMENSIONAL_PASSIVE_H2_AUDIT_2026-08-09.md`

---

## 3. Microscopic gravitational-port factorization

For narrowband matter-to-radiation coupling,

```math
G=V\Gamma_g^{1/2},
\qquad
\Gamma_g=G^\dagger G,
```

so

```math
\boxed{
G_B^\dagger U_RG_A
=\Gamma_{g,B}^{1/2}P_g\Gamma_{g,A}^{1/2},
\qquad
P_g=V_B^\dagger U_RV_A.
}
```

This separates endpoint coupling magnitude from normalized propagation geometry and retains nonorthogonal radiation patterns through the gravitational damping Gram operator.

Canonical file:

- `GRAVITATIONAL_PORT_FACTORIZATION.md`

---

## 4. Classical cumulative quadrupole resource

For mass-weighted elastic normal modes `w_n` with modal masses `mu_n`, define

```math
q_{n,ij}
=\int\rho\left(
 w_{n,i}x_j+w_{n,j}x_i
-\frac23\delta_{ij}w_n\cdot x
\right)dV.
```

The corresponding STF influence-field norm is

```math
\boxed{
\sum_{ijk}|(g^{ij})_k|^2
=\frac{20}{3}r^2.
}
```

Bessel completeness gives

```math
\boxed{
\sum_n\frac{q_n:q_n}{\mu_n}
\le\frac{20}{3}I.
}
```

Using Hirakawa's historical gravitational effective area,

```math
A_{Gn}=\frac{2q_n:q_n}{M\mu_n},
```

this becomes

```math
\boxed{
\sum_n M A_{Gn}\le\frac{40}{3}I.
}
```

Hirakawa's emitted-power normalization then gives

```math
\boxed{
\kappa_{g,n}
=\frac{GMA_{Gn}\omega_n^4}{10c^5},
}
```

and for retained modes with `omega_n <= Omega`,

```math
\boxed{
\sum_n\kappa_{g,n}
=\operatorname{Tr}(K_g^\dagger K_g)
\le\frac{4G}{3c^5}I\Omega^4.
}
```

This both bounds the endpoint gravitational resource and proves `K_g` is Hilbert--Schmidt for the countably infinite retained modal sector.

### Historical narrowing of this intermediate result

The standalone modal construction is **not** a strong novelty claim.

Lobo's arbitrary-body resonant-mass formalism already contains

- the long-wavelength GW tidal fields proportional to `rho E_ij x_j`;
- projection of those fields onto mass-orthogonal elastic eigenmodes; and
- completeness of the five-dimensional STF tensor basis.

For an STF tensor `E`,

```math
E:q_n
=2\int\rho\,w_{n,i}E_{ij}x_j\,dV,
```

so Lobo's historical modal drive coefficients are directional projections of the same dynamic quadrupole. Combining that established framework with standard modal Bessel/Parseval completeness produces the `20/3` coefficient in a short derivation.

A spherical-detector literature precedent also sums the five quadrupole components using spherical-harmonic completeness to obtain an equivalent modal mass.

Accordingly:

```text
GW tidal influence fields:                 HISTORICAL
arbitrary-body modal projection:            HISTORICAL
STF completeness:                           HISTORICAL
modal-participation mathematics:            HISTORICAL
20/3 coefficient as new mathematics:        NO-GO
40/3 A_G formula explicitly found:          NO
use at both endpoints in final H2/TT link:   NOT FOUND
```

Canonical audits:

- `LOBO_SPHERICAL_MODAL_COMPLETENESS_COLLISION_AUDIT_2026-08-09.md`
- `CLASSICAL_MODAL_SUM_RULE_AND_QUANTUM_SCOPE_AUDIT_2026-08-09.md`
- `HIRAKAWA_EFFECTIVE_AREA_QUANTUM_LINEWIDTH_CROSSCHECK.md`

---

## 5. Modern multimode-bar stress test

Tobar, Pikovski, and Tobar (2025) provide a useful adversarial example. Their strongly hybridized multimode bar lets several normal modes inherit substantial coupling from one massive GW-driven element while the readout occurs through a much smaller end mass.

Their normal-mode interaction has a participation factor `P_1j` and the stimulated absorption rate of mode `j` is proportional to

```math
\Gamma_{{\rm stim},j}\propto P_{1j}^2 M h^2.
```

Because the mass-weighted normal-mode transformation is orthogonal,

```math
\boxed{
\sum_j|P_{1j}|^2=1.
}
```

Thus hybridization redistributes the driven-coordinate norm rather than producing `N` independent copies of it. The design can substantially improve readout transduction and spectral coverage without violating the fixed cumulative external gravitational resource.

This is a concrete modern illustration of the trace invariance

```math
\operatorname{Tr}[(GU)^\dagger(GU)]
=\operatorname{Tr}(G^\dagger G).
```

Canonical file:

- `TOBAR_MULTIMODE_BAR_STRESS_TEST_2026-08-09.md`

---

## 6. Equivalent quantum representation

Quantizing the same elastic mode gives

```math
Q^{01}:Q^{10}
=\frac{\hbar M A_{Gn}}{4\omega_n}
```

and hence

```math
\boxed{
\kappa_{g,n}
=\frac{2G\omega_n^5}{5\hbar c^5}Q^{01}:Q^{10}
=\frac{GMA_{Gn}\omega_n^4}{10c^5}.
}
```

The mass-quadrupole EWSR reproduces the same endpoint ceiling. In the linear-harmonic class it is an equivalent quantum representation of the classical modal-completeness constraint rather than the origin of the physical ceiling.

---

## 7. Compact TT propagation and passive recurrence

For compact STF quadrupoles,

```math
\boxed{
\|P_g(\omega)\|_{\rm op}^2
\le\frac{25}{16[k(\omega)R]^2}
}
```

at leading wave-zone order.

The same coefficient follows from

- normalized TT angular modes; and
- classical reciprocal compact-antenna transfer with `D_A=D_B=5/2`.

### Arbitrarily many passive returns between the same endpoints

Let `R_A,R_B` be the exact gravitational reflection blocks of the two passive endpoints and `P_BA,P_AB` the forward/reverse separated propagation operators. The exact repeated-return propagation is

```math
\boxed{
P_{\rm eff}
=(I-P_{BA}R_AP_{AB}R_B)^{-1}P_{BA}.
}
```

If

```math
p_+=\|P_{BA}\|,
\qquad
p_-=\|P_{AB}\|,
```

then passivity gives

```math
\boxed{
\|P_{\rm eff}\|
\le\frac{p_+}{1-p_+p_-}.
}
```

For reciprocal propagation, `p_+=p_-=p` and `eta=p^2`,

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

Therefore arbitrary passive back-and-forth returns between the same two separated compact endpoints cannot change the retained leading `1/R^2` power coefficient.

This does not cover added relays or mirrors, engineered extended cavities, near-field exchange, active gain, or nonseparable overlapping interaction regions.

Canonical files:

- `RECURRENT_SCATTERING_WAVEZONE_AUDIT_2026-08-09.md`
- `numerics/verify_recurrent_scattering_bound.py`
- `TT_PROPAGATION_BOUND.md`
- `INDEPENDENT_TT_COEFFICIENT_CHECK.md`

---

## 8. Exact resonator specialization and quantum corollaries

For one source and receiver pole,

```math
\Gamma_{\rm EBP}
=\frac{4\eta_{\rm prop}
\kappa_{\rm in}\kappa_{g,A}\kappa_{g,B}\kappa_{\rm out}}
{\kappa_A\kappa_B(\kappa_A+\kappa_B)}
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

For the stationary vacuum pure-loss realization,

```math
\eta_{\max}\le\frac12
\Rightarrow Q_1=0,
```

while

```math
Q_2
\le
\frac{\Gamma_{\rm coh}}
{\ln2(1-\eta_{\max})}.
```

These are downstream channel-specific quantum consequences, not the foundation of the classical theorem.

---

## 9. Prior-art boundary

The following are explicitly **historical / established**, not novelty claims:

- gravitational generator--receiver calculations;
- compact gravitational resonant-mass eigenmode theory;
- long-wavelength STF tidal-force/modal projection formalism;
- quadrupole-controlled emission/reception oscillator strength;
- gravitational reciprocity;
- `Q`-independent short-pulse / integrated response;
- compact real-STF directivity and `D=5/2`;
- gravitational material-response sum-rule methodology;
- modal participation / effective modal mass / STF completeness;
- passive H2/Gramian and infinite-dimensional realization machinery;
- generic singular source--receiver wave channels;
- two-body response + Green-operator transfer bounds;
- Redheffer/multiple-scattering composition.

### Surviving candidate contribution

No inspected primary source has been found to state the exact gravity-specific closure

```text
passive selected-port spectral-area cut set
-> smaller source/receiver gravitational coupling trace
-> historical STF tidal/modal coupling + cumulative inertia resource
-> resource bound at BOTH endpoints
-> compact separated TT propagation
-> passive two-endpoint recurrence cannot change leading order
-> explicit inertia-only many-mode end-to-end ceiling.
```

The candidate publication result remains

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega^2}{12c^3R^2}
\min(I_A,I_B).
}
```

This is a **negative prior-art search result, not proof of priority**.

The dimensional-fingerprint search for an older equivalent scaling proportional to `G omega^2 I/(c^3 R^2)` did not reveal an exact two-ended theorem in the inspected primary literature.

---

## 10. Validation — frozen strongest-route checkpoint

Final manuscript validation after the Lobo/Tobar attribution and strongest-route theorem edits:

```text
run: 31346901851
job: 93330404771
PASS
```

- LaTeX compile: **PASS**
- unresolved citation/reference scan: **PASS**
- PDF artifact upload: **PASS**

Final-head physics regression:

```text
run: 31347058681
job: 93330821747
PASS
```

All six physics layers passed:

1. exact two-port spectral bound;
2. passive-network H2 cut set;
3. classical modal sum rule;
4. recurrent passive scattering;
5. TT propagation;
6. microscopic gravitational-port factorization.

The earlier physics run at the exact Lobo/Tobar manuscript commit also passed (`31346901841`, job `93330404759`). The later final-head run confirms that the synchronized repository state retains all six passing regressions.

---

## 11. Publication decision

```text
PHYSICS THEOREM:                              GO
COUNTABLY INFINITE BOUNDED-PORT MODES:        GO
TWO-ENDPOINT PASSIVE RECURRENCE, LEADING:     GO
MICROSCOPIC / A_G NORMALIZATION:              GO
TT NORMALIZATION:                             GO
MODERN MULTIMODE STRESS TEST:                 PASS
STANDALONE MODAL-SUM NOVELTY:                 STRONGLY NARROWED
GENERIC METHOD NOVELTY:                       NO
EXACT INERTIA-CLOSED TWO-ENDED THEOREM:       PROVISIONAL GO
PUBLICATION SIGNIFICANCE:                     DOMINANT EXTERNAL-REVIEW RISK
PRIORITY CLAIM:                               NO
V7 MODIFICATION:                              NO
FURTHER INTERNAL BROADENING:                  NO
```

The dominant remaining risk is **priority/significance**, not a known correctness defect.

---

## 12. Hard stop / next epistemic step

Do not broaden the internal theorem further without a concrete external objection.

The next genuinely informative test is specialist review aimed at either

1. identifying an older theorem equivalent to the complete inertia-closed two-ended result under historical antenna/network notation; or
2. identifying a hidden failure of the bounded-port separated-scattering representation.

Absent such a collision, additional internal generalization is more likely to dilute the result than strengthen it.

### Forbidden claims

- first gravitational efficiency-bandwidth bound;
- new `Q`-independent gravitational response law;
- first gravitational source--receiver calculation;
- new gravitational reciprocity/directivity;
- new tidal influence fields or modal-completeness mathematics;
- new gravitational response sum-rule methodology;
- new generic H2/singular-channel/scattering-network formalism;
- universal gravitational quantum-capacity limit;
- all passive matter;
- globally optimal/saturable coefficient;
- first/unique/unprecedented language without substantially stronger external evidence.
