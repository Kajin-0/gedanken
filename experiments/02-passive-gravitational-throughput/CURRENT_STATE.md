# Current State — Experiment 02

**Status:** **CLASSICAL PASSIVE THROUGHPUT THEOREM CHECKPOINT CLOSED; FULL PRIOR-ART CLAIM NARROWING COMPLETED; QUANTUM RESULTS RETAINED AS COROLLARIES; FURTHER INTERNAL BROADENING STOPPED**

## 1. Headline physical theorem

For a direct narrowband link between compact passive nonrelativistic **linear-harmonic** source and receiver networks in weak one-way quadrupolar wave-zone gravity, define

```math
\Gamma_{\rm coh}
=\frac1{2\pi}\int_{\mathcal B}
\operatorname{Tr}[T^\dagger(\omega)T(\omega)]d\omega.
```

The current theorem is

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega^2}{12c^3R^2}
\min(I_A,I_B).
}
```

`I_A` and `I_B` are internal mass inertia moments about the endpoint centers of mass.

The physical ceiling is **classical** within the declared linear-harmonic class. It contains no endpoint quality factor, passive resonance count, internal coherent-mixing parameter, branching fraction, or four-spoke-specific parameter. Quantum theory reproduces the same oscillator-strength normalization and supplies downstream channel/capacity corollaries.

Experiment 01 / V7 remains frozen and is not modified by this branch.

---

## 2. Proof chain

### A. Passive selected-port H2 cut set

For an energy-normalized stable passive linear realization,

```math
A=-iH-\frac12K^\dagger K,
```

standard passive Gramian identities imply

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

The same algebra applies to classical energy-normalized temporal coupled modes. The H2/Gramian machinery is established prior art.

Canonical file: `PASSIVE_NETWORK_CUTSET_THEOREM.md`.

### B. Microscopic / radiative-port factorization

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

This separates endpoint coupling magnitude from normalized radiation geometry and retains overlapping radiation patterns through the gravitational Gram matrix.

Canonical file: `GRAVITATIONAL_PORT_FACTORIZATION.md`.

### C. Classical quadrupole modal-completeness resource

For mass-weighted elastic normal modes `w_n` with modal masses `mu_n`, define the linear STF quadrupole influence fields

```math
(g^{ij})_k
=\delta_{ik}x_j+\delta_{jk}x_i
-\frac23\delta_{ij}x_k
```

and modal quadrupoles

```math
q_{n,ij}=\langle w_n,g^{ij}\rangle_\rho.
```

The exact pointwise tensor identity is

```math
\boxed{
\sum_{ijk}|(g^{ij})_k|^2
=\frac{20}{3}r^2.
}
```

Bessel completeness therefore gives

```math
\boxed{
\sum_n\frac{q_n:q_n}{\mu_n}
\le\frac{20}{3}I.
}
```

Using the historical Hirakawa gravitational effective area

```math
A_{Gn}=\frac{2q_n:q_n}{M\mu_n},
```

this becomes

```math
\boxed{
\sum_n M A_{Gn}\le\frac{40}{3}I.
}
```

The Bessel/Parseval modal-participation method is standard structural dynamics. The gravity-specific specialization is the STF quadrupole influence field and its `20/3` norm.

Hirakawa's emitted-power normalization gives the classical gravitational energy-decay rate

```math
\boxed{
\kappa_{g,n}
=\frac{GMA_{Gn}\omega_n^4}{10c^5}.
}
```

Therefore, for retained modes with `omega_n <= Omega`,

```math
\boxed{
\sum_n\kappa_{g,n}
\le\frac{4G}{3c^5}I\Omega^4.
}
```

Canonical files:

- `CLASSICAL_MODAL_SUM_RULE_AND_QUANTUM_SCOPE_AUDIT_2026-08-09.md`
- `HIRAKAWA_EFFECTIVE_AREA_QUANTUM_LINEWIDTH_CROSSCHECK.md`
- `numerics/verify_classical_modal_sum_rule.py`

### D. Equivalent quantum representation

Quantizing the same elastic coordinate gives

```math
Q^{01}:Q^{10}
=\frac{\hbar M A_{Gn}}{4\omega_n},
```

and therefore

```math
\kappa_{g,n}
=\frac{2G\omega_n^5}{5\hbar c^5}Q^{01}:Q^{10}
=\frac{GMA_{Gn}\omega_n^4}{10c^5}.
```

The mass-quadrupole EWSR reproduces the same `4G I Omega^4/(3c^5)` endpoint ceiling. In the linear-harmonic class it is an equivalent quantum representation of the classical modal-completeness bound rather than the origin of the physical ceiling.

### E. Compact TT propagation

For compact STF quadrupoles,

```math
\boxed{
\|P_g(\omega)\|_{\rm op}^2
\le\frac{25}{16[k(\omega)R]^2}
}
```

at leading wave-zone order.

The same coefficient has both

- a normalized TT angular-mode derivation; and
- a classical reciprocal antenna interpretation using `D_A=D_B=5/2` and `D_A D_B (lambda/4 pi R)^2`.

The compact real-STF directivity functional and its `5/2` maximum are historical gravitational-antenna physics.

Canonical files:

- `TT_PROPAGATION_BOUND.md`
- `INDEPENDENT_TT_COEFFICIENT_CHECK.md`
- `HIRAKAWA_NARIHARA_FUJIMOTO_1976_COLLISION_AUDIT.md`

---

## 3. Exact resonator specialization

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
```

and

```math
\boxed{
\Gamma_{\rm EBP}^{\rm max}
=\frac8{27}\eta_{\rm prop}\kappa_g.
}
```

Peak-optimal critical coupling and spectral-area-optimal coupling are therefore different objectives.

---

## 4. Quantum-information corollaries

The throughput theorem itself is classical. For the stationary vacuum pure-loss quantum realization,

```math
\eta_{\max}\le\frac12
\Rightarrow Q_1=0,
```

while

```math
\boxed{
Q_2
\le
\frac{\Gamma_{\rm coh}}
{\ln2\,(1-\eta_{\max})}.
}
```

These are channel-specific operational consequences, not the foundation of the physical bound.

---

## 5. Scope clarifications closed at this checkpoint

### Finite H2 model versus infinite elastic spectrum

The H2 theorem applies directly to any finite retained band-local modal sector. The classical modal bound is uniform in the retained mode count. For a countably infinite retained spectrum, the nonnegative cumulative resource has a finite monotone limit; extending the H2 statement requires the corresponding passive transfer operator to possess the usual well-defined trace-class limit. No stronger infinite-dimensional claim is required.

### One-way propagation

`P_g` is the direct retarded one-pass/Born wave-zone hop. The theorem does not claim to bound recurrent multiple scattering, strong common-bath hybridization, repeated coherent backaction, relays, near-field exchange, or curved-background focusing.

### Sharpness

The final coefficient is an upper bound, not a globally proven optimum. The explicit long-wavelength plus mode reaches 30% of the endpoint material ceiling and saturates the compact TT geometry ceiling, but simultaneous saturation of the full chain is unproved.

---

## 6. Prior-art boundary after the full audit

The following are explicitly **historical / established**, not novelty claims:

- gravitational generator--receiver calculations and broad end-to-end limitations;
- compact gravitational antenna eigenmode theory;
- quadrupole-controlled gravitational emission/reception oscillator strength;
- gravitational reciprocity;
- `Q`-independent short-pulse / integrated gravitational response;
- compact real-STF directivity and `D=5/2`;
- gravitational material-response dispersion/sum-rule methodology;
- quadrupole-commutator evaluation of gravitational response sum rules;
- generic passive H2/Gramian identities;
- generic source--receiver singular wave channels and Frobenius/trace transfer metrics;
- generic two-body response + Green-operator transfer bounds;
- modal participation / equivalent-modal-mass completeness;
- generic use of physical sum rules to constrain integrated passive response.

Canonical collision audits:

- `GRISHCHUK_SAZHIN_1975_COLLISION_AUDIT.md`
- `HIRAKAWA_NARIHARA_FUJIMOTO_1976_COLLISION_AUDIT.md`
- `SRIVASTAVA_WIDOM_PIZZELLA_2003_SUM_RULE_COLLISION_AUDIT.md`
- `GENERIC_WAVE_TRANSFER_COLLISION_AUDIT_2026-08-09.md`
- `STRUCTURAL_DYNAMICS_MODAL_PARTICIPATION_COLLISION_AUDIT.md`

### Surviving candidate contribution

No inspected source has been found to state the exact gravity-specific closure

```text
passive selected-port spectral-area cut set
-> smaller source/receiver gravitational coupling resource
-> STF quadrupole modal-participation specialization
-> cumulative effective-area/inertia ceiling at BOTH endpoints
-> normalized compact TT one-pass propagation
-> explicit inertia-only many-mode end-to-end bound.
```

The candidate publication contribution is therefore specifically

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega^2}{12c^3R^2}
\min(I_A,I_B),
}
```

and the simultaneous exclusion of passive escape by higher `Q`, more resonances, coherent bright-mode engineering, and compact quadrupole orientation.

This remains a **negative prior-art search result, not proof of priority**.

---

## 7. Validation checkpoint

Latest complete physics regression:

```text
GitHub Actions run: 31344642352
job:               93324206747
```

All stages passed:

1. exact two-port spectral bound;
2. passive-network cut-set bound;
3. classical modal sum-rule regression;
4. TT quadrupole propagation bound;
5. microscopic gravitational port factorization.

Latest complete manuscript validation:

```text
GitHub Actions run: 31344642351
job:               93324206692
```

- LaTeX compile: **PASS**
- unresolved citation/reference scan: **PASS**
- PDF artifact upload: **PASS**

The new modal regression independently checks the `20/3` identity, Bessel/Parseval resource bound, `sum M A_G <= 40 I/3`, center-of-mass translation orthogonality, and exact `A_G <-> kappa_g` normalization.

---

## 8. Manuscript identity

Current title:

**Passive Throughput Bounds for Propagating Gravitational Transduction**

The main theorem is presented as classical. Quantum-channel material is explicitly downstream.

The manuscript now credits all known ingredient-level prior art and does not claim novelty for the mathematical methods themselves.

---

## 9. Publication decision

```text
PHYSICS THEOREM:                         GO
CLASSICAL MODAL COMPLETENESS:            GO
MICROSCOPIC / A_G NORMALIZATION:         GO
TT NORMALIZATION:                        GO
NUMERICAL VALIDATION:                    GO
MANUSCRIPT:                              GO
QUANTUM STATUS OF HEADLINE BOUND:        CLASSICAL, NOT QUANTUM
GENERIC METHOD NOVELTY:                  NO
GRAVITATIONAL INGREDIENT NOVELTY:        NO
EXACT INERTIA-CLOSED TWO-ENDED THEOREM:  PROVISIONAL GO
PUBLICATION SIGNIFICANCE:                MATERIAL EXTERNAL-REVIEW RISK
PRIORITY CLAIM:                          NO
V7 MODIFICATION:                         NO
THEOREM BROADENING:                      NO
```

The dominant risk is now **significance, not a known correctness defect**.

---

## 10. Hard stop / next epistemic step

The internal derivation program should stop here.

Canonical hostile review:

`HOSTILE_REFEREE_REPORT_2026-08-09.md`

The next useful test is an actual gravitational-antenna / passive-wave specialist asking whether

1. an equivalent inertia-closed two-ended theorem already exists under older antenna, mutual-impedance, network, or scattering language; or
2. the H2-to-gravitational-continuum / one-pass subsystem boundary hides a physical defect.

Absent a concrete objection of that type, further internal generalization is more likely to dilute the result than strengthen it.

### Forbidden claims

- first gravitational efficiency-bandwidth bound;
- new `Q`-independent gravitational response law;
- first gravitational source--receiver/end-to-end bound;
- new gravitational antenna reciprocity/directivity;
- new gravitational response sum-rule methodology;
- new modal-completeness/effective-mass method;
- new generic singular-channel wave-transfer formalism;
- universal gravitational quantum-capacity limit;
- all passive matter;
- globally optimal/saturable coefficient;
- first/unique/unprecedented language without substantially stronger external evidence.
