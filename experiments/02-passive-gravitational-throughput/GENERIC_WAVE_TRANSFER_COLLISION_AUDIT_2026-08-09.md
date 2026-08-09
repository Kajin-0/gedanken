# Generic Wave-Transfer Structural Prior-Art Audit — 2026-08-09

## Purpose

Test whether the remaining structural ingredients of Experiment 02 are already established in generic wave physics even if the exact gravity-specific theorem is not.

This audit is about **significance and claim boundaries**, not an identified physics defect.

---

## 1. Collision target

After the gravitational-antenna historical audits, the Experiment 02 chain is

```text
passive selected-port H2 cut set
-> source gravitational coupling trace
-> normalized separated propagation operator
-> receiver gravitational coupling trace
-> cumulative quadrupole EWSR closure at both endpoints
-> frequency-integrated end-to-end coherent-transfer ceiling.
```

The question is whether the middle operator/singular-channel structure is itself a new conceptual construction.

---

## 2. Miller 2000: spatial communication channels between two volumes

David A. B. Miller, **“Communicating with waves between volumes: evaluating orthogonal spatial channels and limits on coupling strengths,”** *Applied Optics* **39**, 1681–1699 (2000), DOI `10.1364/AO.39.001681`.

Miller develops an exact source-to-receiver wave communication problem between two arbitrary volumes. The key established ingredients include

```text
source volume
-> propagation operator
-> receiver volume
-> singular/eigen communication channels
-> connection strengths
-> sum rule for the squared connection strengths.
```

Thus the following generic ideas are historical:

- identifying the best-connected source/receiver spatial modes by singular/eigen channels;
- interpreting squared singular values as connection strengths;
- summing those squared connection strengths as an overall coupling measure;
- bounding/relating that sum to a simple operator/volume integral.

Experiment 02's use of `Tr[T^dagger T]` as the sum of squared transmission singular values must therefore not be presented as a novel wave-communication concept.

Miller's result is primarily a fixed-frequency spatial-channel theorem. It does not provide the Experiment 02 frequency-integrated passive endpoint resource closure.

---

## 3. Miller–Johnson–Rodriguez 2015: two material resources plus free-space Green function

O. D. Miller, S. G. Johnson, and A. W. Rodriguez, **“Shape-Independent Limits to Near-Field Radiative Heat Transfer,”** *Physical Review Letters* **115**, 204302 (2015), DOI `10.1103/PhysRevLett.115.204302`.

Their spectral two-body bound is obtained by

```text
response limit of body 1
+ free-space Green-function coupling
+ response limit of body 2
-> bound on spectral power transfer.
```

In particular, their bound has the schematic structure

```math
\Phi(\omega)
\lesssim
R_1(\omega)R_2(\omega)
\int_{V_1}\int_{V_2}\|G_0\|_F^2,
```

where each material factor is bounded separately using passivity/energy conservation and reciprocity.

This is a clear generic-wave precedent for a **two-ended material-resource + propagation-operator** bound.

It is not the same mathematical resource as Experiment 02: the electromagnetic resources depend on susceptibility and dissipation, whereas Experiment 02 ultimately uses a cumulative gravitational quadrupole oscillator-strength trace constrained by an EWSR.

---

## 4. Molesky–Venkataram–Jin–Rodriguez 2020: operator transmission formulation

S. Molesky, P. S. Venkataram, W. Jin, and A. W. Rodriguez, **“Fundamental limits to radiative heat transfer: Theory,”** *Physical Review B* **101**, 035408 (2020), DOI `10.1103/PhysRevB.101.035408`.

This work is structurally even closer. For two bodies A and B, the heat-transfer spectrum is written in operator form with the bodies treated symmetrically and connected by the vacuum Green operator.

They write the spectrum as a Frobenius norm of an operator product and alternatively in terms of a transmission operator whose singular values obey channel bounds. Schematically,

```text
body-A response
-> vacuum Green operator
-> body-B response
-> Frobenius trace / transmission singular values.
```

Thus these concepts are generic prior art:

- a two-body operator resource sandwich;
- a free-space propagation/Green operator between independently constrained endpoint responses;
- Frobenius traces as total spectral transfer;
- singular-value channel bounds;
- separating material limitations from propagation geometry.

Experiment 02 should therefore not imply that this abstract architecture is itself new.

---

## 5. Precise distinction from Experiment 02

The generic electromagnetic literature above differs in several load-bearing respects.

### Different endpoint resource

The electromagnetic bounds use susceptibility/dissipation response factors at a fixed frequency. Experiment 02 uses

```math
\operatorname{Tr}\Gamma_g
=\sum_n\kappa_{g,n}
```

and closes the **cumulative** retained resource using the mass-quadrupole EWSR,

```math
\operatorname{Tr}\Gamma_g
\le
\frac{4G}{3c^5}\langle I\rangle\Omega^4.
```

### Frequency-integrated local-port transfer

Experiment 02's primary object is

```math
\Gamma_{\rm coh}
=\frac1{2\pi}\int d\omega\,
\operatorname{Tr}[T^\dagger T],
```

and the passive H2 identity converts that frequency integral into an endpoint coupling-trace cut set.

The cited generic wave-transfer papers primarily establish spatial/spectral channel bounds at fixed frequency or thermally weighted frequency integrals, rather than this particular H2 endpoint resource theorem.

### Gravitational microscopic closure

Experiment 02 identifies the abstract endpoint trace with the one-quantum mass-quadrupole gravitational linewidth resource and uses the coordinate quadrupole EWSR to eliminate the internal passive mode count.

### Final inertia-only ceiling

The resulting gravity-specific narrowband theorem

```math
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega^2}{12c^3R^2}
\min(\langle I_A\rangle,\langle I_B\rangle)
```

is not present in the inspected generic-wave literature.

---

## 6. Claim correction forced by this audit

The manuscript should **not** claim conceptual novelty for

```text
source/receiver singular channels
Tr[T^dagger T] as a sum of squared channel strengths
a two-ended response-resource sandwich
separating endpoint response from a free-space Green/propagation operator
using singular values to bound wave transfer.
```

Those structures are established across wave physics.

The surviving candidate contribution is narrower still:

> **A gravity-specific cumulative passive closure:** a selected-port H2 integral is bounded by the smaller gravitational endpoint coupling trace; both traces are closed by the mass-quadrupole EWSR; and the compact TT propagation operator supplies the separated wave-zone geometry factor, yielding an inertia-controlled many-mode end-to-end bound.

---

## 7. Publication-significance implication

The strongest hostile referee can now say:

> The paper combines a historical gravitational antenna oscillator-strength normalization with standard wave-channel/singular-value transfer theory, standard passive H2 identities, and a quadrupole sum rule.

That is a serious significance objection.

The response must be substantive rather than rhetorical:

- the **final gravity-specific cumulative bound** removes endpoint `Q`, passive mode count, coherent internal mixing, and compact orientation in one closed inequality;
- the cumulative EWSR step prevents passive parallelization from evading the ceiling;
- both material interfaces are bounded by the same microscopic gravitational resource rather than by phenomenological susceptibility figures of merit;
- the resulting coefficient and scaling are explicit in `G`, `c`, `omega`, `R`, and endpoint inertia.

Whether that synthesis is publication-level significant remains an external-review question.

---

## 8. Updated novelty hierarchy

```text
GENERIC SINGULAR WAVE CHANNELS:             HISTORICAL
GENERIC TWO-BODY RESOURCE + GREEN OPERATOR: HISTORICAL
GENERIC FROBENIUS/TRACE TRANSFER METRIC:    HISTORICAL
GRAVITATIONAL SINGLE-MODE OSCILLATOR STRENGTH:
                                            HISTORICAL
GRAVITATIONAL RECIPROCITY / DIRECTIVITY:    HISTORICAL
PASSIVE H2 SELECTED-PORT CUT SET:           ESTABLISHED MATHEMATICS
CUMULATIVE GRAVITATIONAL EWSR AT BOTH ENDS: NO EXACT COLLISION FOUND
FINAL INERTIA-CLOSED MANY-MODE GRAVITY BOUND:
                                            NO EXACT COLLISION FOUND
PRIORITY CLAIM:                             NO
```

---

## 9. Decision

```text
PHYSICS DEFECT:                  NONE IDENTIFIED
GENERIC STRUCTURAL NOVELTY:      NO
GRAVITY-SPECIFIC CUMULATIVE CLOSURE:
                                 PROVISIONAL GO
PUBLICATION SIGNIFICANCE RISK:   HIGHER THAN BEFORE THIS AUDIT
THEOREM BROADENING:              DO NOT DO
NEXT STEP:                       EXTERNAL SPECIALIST SIGNIFICANCE/PRIOR-ART REVIEW
```
