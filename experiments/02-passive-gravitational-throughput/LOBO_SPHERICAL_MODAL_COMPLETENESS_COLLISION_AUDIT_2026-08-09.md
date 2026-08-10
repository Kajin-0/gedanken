# Lobo / Spherical Modal-Completeness Collision Audit — 2026-08-09

## Purpose

Test whether the classical material identity

```math
\sum_n M A_{Gn}\le\frac{40}{3}I
```

is genuinely new as a standalone result, or whether it is already implicit in established gravitational resonant-mass antenna theory.

## Verdict

> **The exact `40/3` gravitational-effective-area statement has not been found explicitly in the inspected literature, but its mathematical content is much closer to historical gravitational-antenna formalism than previously stated. In particular, Lobo's arbitrary-body GW-response formalism already contains the STF tidal influence fields, mass-orthonormal elastic eigenmodes, and STF tensor completeness needed to derive the `20/3` modal identity in a few lines. Spherical-detector literature also contains explicit quadrupole-mode effective-mass summations based on spherical-harmonic completeness.**

Therefore the paper should **not** present the modal sum as an independently deep or methodologically novel theorem. Its main value is as the material closure required by the two-ended throughput result.

---

## 1. Lobo's arbitrary-body formalism already contains the needed force fields

J. Alberto Lobo, *What can we learn about GW Physics with an elastic spherical antenna?*, Phys. Rev. D 52, 591 (1995), arXiv:`gr-qc/0006102`, sets up a response theory for an **arbitrarily shaped isotropic elastic solid** in the long-wavelength linear regime.

The normal modes `u_N` are mass-orthonormalized as

```math
\int \rho\,u_{N'}^*\cdot u_N\,d^3x
=M\delta_{N'N}.
```

The GW tidal force is decomposed into STF quadrupole components whose spatial fields are

```math
f_i^{(m)}(x)=\rho E_{ij}^{(m)}x_j,
```

with modal projection coefficient

```math
f_N^{(m)}
=\frac1M\int u_N^*(x)\cdot f^{(m)}(x)\,d^3x.
```

Lobo also gives orthogonality and completeness relations for the five STF `E^(m)` tensors.

These are already the ingredients used in the present manuscript's mass-weighted quadrupole influence-field construction.

---

## 2. Exact map from Lobo's modal coefficient to the manuscript quadrupole

Define the linearized STF mass quadrupole of mode `N` as

```math
q_{N,ij}
=\int\rho\left(
 u_{N,i}x_j+u_{N,j}x_i
-\frac23\delta_{ij}\,u_N\cdot x
\right)d^3x.
```

For any symmetric trace-free tensor `E`,

```math
E:q_N
=2\int\rho\,u_{N,i}E_{ij}x_j\,d^3x.
```

Therefore, for Lobo's STF basis,

```math
\boxed{
E^{(m)}:q_N
=2M f_N^{(m)}
}
```

(up to complex conjugation convention for the mode coefficient).

Thus Lobo's gravitational driving amplitudes are precisely directional STF projections of the same dynamic quadrupole tensor used in Experiment 02.

This materially narrows the originality of the intermediate material construction: the quadrupole influence fields are not a new physical object.

---

## 3. Lobo's STF completeness almost immediately gives the `20/3` coefficient

Let `T_a`, `a=1,...,5`, be an orthonormal STF tensor basis,

```math
T_a:T_b=\delta_{ab}.
```

Lobo's `E^(m)` basis is the same five-dimensional STF space with a different normalization. STF completeness is

```math
\sum_{a=1}^5
(T_a)_{ij}(T_a)_{kl}
=
\frac12(\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk})
-\frac13\delta_{ij}\delta_{kl}.
```

Contracting the first and third tensor indices gives

```math
\sum_a |T_a x|^2
=\frac53 r^2.
```

The manuscript's quadrupole influence vector associated with `T_a` is

```math
g_a(x)=2T_a x,
```

because the trace subtraction vanishes after contraction with an STF tensor. Hence

```math
\boxed{
\sum_a|g_a(x)|^2
=4\sum_a|T_a x|^2
=\frac{20}{3}r^2.
}
```

This is exactly the coefficient used in Experiment 02.

So once Lobo's tidal-force decomposition and STF completeness are combined with standard modal Parseval/Bessel theory, the central algebraic coefficient is essentially immediate.

---

## 4. Modal Bessel step in Lobo normalization

With Lobo's normalization

```math
\int\rho\,u_{N'}^*\cdot u_N\,d^3x
=M\delta_{N'N},
```

the normalized displacement vectors are

```math
e_N=u_N/\sqrt M.
```

For each STF influence field `g_a`, Bessel's inequality gives

```math
\sum_N
|\langle e_N,g_a\rangle_\rho|^2
\le
\|g_a\|_\rho^2.
```

Summing over the five STF components therefore yields

```math
\boxed{
\sum_N\frac{q_N:q_N}{M}
\le
\frac{20}{3}I.
}
```

For general modal masses `mu_N` this is the manuscript form

```math
\boxed{
\sum_N\frac{q_N:q_N}{\mu_N}
\le
\frac{20}{3}I.
}
```

The mathematics is standard orthogonal-mode completeness applied to Lobo's already-established GW tidal influence fields.

---

## 5. What Lobo does and does not state

Lobo explicitly states that, for a nonsymmetric body, many modes can carry monopole/quadrupole moments, while the sphere concentrates GW coupling into one monopole series and one fivefold-degenerate quadrupole series. He argues qualitatively that concentrating the absorbed GW energy into fewer coupled modes explains the sphere's high efficiency.

He also derives mode-dependent absorption cross sections for the sphere,

```math
\sigma_{\rm abs}(\omega_{n2})
\propto
\frac{GMv_t^2}{c^3}(k_{n2}b_n)^2,
```

and shows the higher-mode scaling.

However, in the inspected full text I did **not** find an explicit statement equivalent to

```math
\sum_N\frac{q_N:q_N}{\mu_N}\le\frac{20}{3}I
```

or

```math
\sum_N M A_{GN}\le\frac{40}{3}I.
```

Nor does the paper form a source--propagation--receiver throughput cut set.

The priority conclusion is therefore:

```text
GW tidal influence fields:                 HISTORICAL
arbitrary-body modal projection:            HISTORICAL
STF tensor completeness:                    HISTORICAL
qualitative oscillator-strength sharing:    HISTORICAL
20/3 global inertia contraction:            NOT FOUND EXPLICITLY
40/3 Hirakawa effective-area sum:            NOT FOUND EXPLICITLY
use at both endpoints in H2/TT link:         NOT FOUND
```

---

## 6. Spherical effective-mass sum precedent

A modern Schenberg resonant-sphere analysis, V. Liccardo et al., *The Design Strain Sensitivity of the Schenberg Spherical Resonant Antenna for Gravitational Waves*, arXiv:`2302.01232` (2023), contains an explicit five-quadrupole-mode equivalent-mass sum.

For a surface transducer, it derives

```math
\frac{M_S}{\alpha^2}
\sum_{m=-2}^{2}\frac1{M_m}
=
\sum_{m=-2}^{2}Y_{2m}^2(\theta,\phi),
```

then uses

```math
\sum_{m=-2}^{2}Y_{2m}^2(\theta,\phi)
=\frac5{4\pi}
```

to obtain a direction-independent equivalent mass.

The paper attributes the underlying effective-mass concept to C. Z. Zhou and P. F. Michelson, *Spherical resonant-mass gravitational wave detectors*, Phys. Rev. D 51, 2517 (1995).

This is **not** the Experiment 02 sum rule:

- it is a transducer-facing surface effective mass;
- it sums the five `m` components of a spherical quadrupole multiplet rather than all quadrupole-active elastic modes/overtones;
- it does not use Hirakawa gravitational effective area `A_G`;
- it does not produce an inertia-only total gravitational damping trace;
- it does not enter a two-ended propagation theorem.

But it is a clear gravitational-antenna precedent for using quadrupole harmonic completeness to collapse multiple modal degrees of freedom into one effective resource.

---

## 7. Consequence for manuscript novelty language

The manuscript should no longer describe the `20/3` or `40/3` relation as though the **method** or the underlying influence-field construction were independently novel.

The safest description is:

> Applying standard modal completeness to the historical STF tidal-force fields of gravitational resonant-mass antenna theory gives the compact relation `sum_n M A_Gn <= (40/3) I`. We use this relation at both endpoints to close the passive end-to-end throughput bound.

The potentially publishable content is therefore pushed even more strongly toward the final composition:

```text
historical arbitrary-body GW modal response
+ historical Hirakawa gravitational effective area
+ standard modal completeness
+ passive endpoint H2 cut
+ compact TT propagation
+ both endpoint resources eliminated by inertia
= final two-ended throughput ceiling.
```

---

## 8. Collision severity

```text
STANDALONE MODAL-SUM NOVELTY:              STRONGLY NARROWED
20/3 COEFFICIENT AS NEW MATHEMATICS:        NO-GO
QUADRUPOLE INFLUENCE FIELD AS NEW OBJECT:   NO-GO
40/3 A_G FORMULA EXPLICITLY FOUND:          NO
TWO-ENDED INERTIA CLOSURE FOUND:            NO
PHYSICS CORRECTNESS IMPACT:                 NONE
PUBLICATION SIGNIFICANCE IMPACT:            MODERATE NEGATIVE
PRIORITY CONFIDENCE OF FINAL THEOREM:        STILL PROVISIONAL
```

## Bottom line

The material sum is **useful and apparently unstated in this exact form, but it is not conceptually distant from the historical theory**. A hostile referee can plausibly reconstruct it from Lobo + standard completeness + Hirakawa in a short derivation.

That makes the final two-ended inertia-controlled throughput theorem—not the material sum alone—the only defensible novelty center of Experiment 02.
