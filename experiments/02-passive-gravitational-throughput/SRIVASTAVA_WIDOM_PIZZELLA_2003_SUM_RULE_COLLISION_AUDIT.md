# Srivastava–Widom–Pizzella 2003 Sum-Rule Collision Audit

## Source

Y. N. Srivastava, A. Widom, and G. Pizzella, **“Electronic Enhancements in the Detection of Gravitational Waves by Metallic Antennae,”** arXiv:gr-qc/0302024 (2003).

Primary arXiv full text inspected.

---

## 1. Why this source matters

The Experiment 02 literature map already treated this work as prior art for susceptibility/Kubo descriptions of gravitational absorption. Full-text inspection shows a stronger collision:

> **The paper contains an explicit section titled “Dispersion Relations and Sum Rules,” derives a frequency-integrated gravitational-antenna response sum rule, and evaluates it microscopically using an equal-time mass-quadrupole commutator.**

Therefore Experiment 02 must not claim novelty for

- applying a dispersion relation to gravitational antenna response;
- deriving a gravitational material-response sum rule;
- evaluating such a sum rule through quadrupole commutators;
- connecting integrated gravitational absorption to microscopic material resources.

Those ideas are historical.

---

## 2. Their gravitational absorption response

In the mass-quadrupole limit, Srivastava et al. write the gravitational absorption cross section in terms of the imaginary part of a transverse dynamical elastic Lamé coefficient `mu(omega)` and equivalently the real part of the viscosity `eta(omega)`.

Schematically,

```math
\sigma(\omega)
\propto
-\frac{1}{\omega}\operatorname{Im}\mu(\omega)
\propto
\operatorname{Re}\eta(\omega).
```

Thus their endpoint object is a genuine frequency-dependent gravitational material response, not merely a single resonant-mode parameter.

---

## 3. Their explicit sum rule

Their Sec. 6 gives the dispersion relation

```math
\eta(\zeta)
=-\frac{2i\zeta}{\pi}
\int_0^\infty
\frac{\operatorname{Re}\eta(\omega+i0^+)}
{\omega^2-\zeta^2}\,d\omega,
```

and obtains

```math
\boxed{
\frac{2}{\pi}
\int_0^\infty
\operatorname{Re}\eta(\omega+i0^+)\,d\omega
=
\mu(\infty)-\mu(0).
}
```

They explicitly call this a **sum rule**.

They then evaluate the right-hand side microscopically through an equal-time commutator involving time derivatives of the mass quadrupole operator. For a nonrelativistic many-particle Hamiltonian they reduce the result to kinetic- and interaction-energy expectation values; for Coulomb matter they further simplify it using the virial theorem.

Therefore the general strategy

```text
causal gravitational response
-> dispersion relation
-> frequency-integrated response
-> quadrupole commutator / microscopic resource
```

is historical prior art.

---

## 4. Relation to the Experiment 02 classical modal sum rule

The newly derived Experiment 02 identity is different:

```math
\boxed{
\sum_n M A_{Gn}\le\frac{40}{3}I,
}
```

where `A_Gn` is the compact elastic-mode gravitational effective area and `I` is the total internal mass inertia moment about the center of mass.

The proof is a mass-weighted normal-mode Bessel/completeness inequality rather than a viscosity dispersion relation:

```math
\sum_n\frac{q_n:q_n}{\mu_n}
\le\frac{20}{3}I.
```

Combined with

```math
\kappa_{g,n}
=\frac{GMA_{Gn}\omega_n^4}{10c^5}
```

and a retained-band ceiling `omega_n <= Omega`, it yields

```math
\boxed{
\sum_n\kappa_{g,n}
\le\frac{4G}{3c^5}I\Omega^4.
}
```

No inspected equation in Srivastava et al. was found to state this inertia-based modal effective-area completeness bound.

---

## 5. Important conceptual distinction

### Srivastava–Widom–Pizzella

Their sum rule constrains an **integrated absorptive material response** in terms of differences between high- and low-frequency elastic moduli and, microscopically, kinetic/interparticle interaction energies.

### Experiment 02 classical modal sum

The new compact relation constrains the **total squared quadrupole coupling carried by an orthogonal elastic mode basis** directly by the geometry/mass resource

```math
I=\int\rho r^2dV.
```

It is a completeness/Bessel theorem for the linearized STF quadrupole map.

The two statements are related in spirit but are not algebraically the same resource identity.

---

## 6. Novelty consequence

The phrase “mass-quadrupole sum rule” by itself is far too broad to support novelty.

The surviving candidate contribution must be described precisely as

> **a compact elastic-mode gravitational effective-area completeness bound, `sum_n M A_Gn <= (40/3) I`, and its use at both endpoints of a passive source-to-receiver throughput cut set.**

Even this remains a negative-search novelty claim until broader antenna/modal-analysis literature is exhausted.

The final two-ended bound remains

```math
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega^2}{12c^3R^2}
\min(I_A,I_B).
```

No equivalent two-ended inertia closure was found in this source.

---

## 7. Publication significance after this collision

A hostile referee can now accurately say that essentially every **methodological ingredient** has precedent:

```text
compact gravitational antenna modes             historical
emission/reception reciprocity                   historical
Q-independent integrated response                historical
gravity-specific response sum rule               historical
quadrupole commutator evaluation                 historical
generic H2/passive-system identities             historical
generic singular-channel wave transfer           historical
```

The paper therefore stands only on the compact modal completeness relation and its architecture-independent two-ended closure.

That is a narrower claim, but also a much cleaner one.

---

## 8. Verdict

```text
GRAVITATIONAL MATERIAL SUM-RULE METHODOLOGY:  HISTORICAL
QUADRUPOLE-COMMUTATOR SUM RULE:               HISTORICAL
INTEGRATED ABSORPTIVE RESPONSE SUM RULE:      HISTORICAL
sum_n M A_Gn <= (40/3) I:                     NO EXACT COLLISION FOUND HERE
TWO-ENDED INERTIA-CLOSED THROUGHPUT THEOREM:  NO EXACT COLLISION FOUND HERE
PHYSICS DEFECT:                               NONE IDENTIFIED
NOVELTY BOUNDARY:                             NARROWER
```
