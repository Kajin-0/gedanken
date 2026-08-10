# Compact TT Propagation — Independent Stage-C Derivation

**Stage:** C  
**Status:** analytic derivation; automated validation to be run on the real repository head.  
**Method:** classical normalized TT angular modes + outgoing stationary phase. V7 is consulted only after the coefficient is derived.

## 1. Objective

Stages A and B have established, within their finite-dimensional/modal model,

```math
\Gamma_{\rm coh}
\le
\eta_{\max}
\min\left[
\operatorname{Tr}(K_{g,A}^\dagger K_{g,A}),
\operatorname{Tr}(K_{g,B}^\dagger K_{g,B})
\right]
```

and

```math
\operatorname{Tr}(K_g^\dagger K_g)
\le
\frac{4G}{3c^5}I_2\Omega^4.
```

Stage C independently determines the leading separated-wave-zone power norm `eta_max` for compact STF quadrupole radiation.

No `25/16` coefficient is assumed below.

## 2. TT projector and angular power pattern

Let

```math
P_{ij}(\hat n)=\delta_{ij}-n_in_j
```

and let `Lambda(n)` be the orthogonal projector from symmetric tensors to the two transverse-traceless polarizations perpendicular to `n`.

For a complex STF quadrupole amplitude `q_ij`, define

```math
F_q(\hat n)
\equiv
q^*:\Lambda(\hat n):q.
```

Because `Lambda` is an orthogonal projector,

```math
0\le F_q(\hat n)\le q^*:q.
```

For an STF tensor one convenient explicit form is

```math
F_q(\hat n)
=q^*:q
-2(q^*\hat n)\cdot(q\hat n)
+\frac12|\hat n\cdot q\hat n|^2.
```

This is proportional to the radiated power per solid angle; the dimensional prefactor cancels when the angular mode is normalized.

## 3. Full-sphere normalization

Use the isotropic angular moments

```math
\int d\Omega\,n_in_j
=\frac{4\pi}{3}\delta_{ij},
```

```math
\int d\Omega\,n_in_jn_kn_l
=\frac{4\pi}{15}
(\delta_{ij}\delta_{kl}
+\delta_{ik}\delta_{jl}
+\delta_{il}\delta_{jk}).
```

For traceless symmetric `q`, these give

```math
\int d\Omega\,(q^*\hat n)\cdot(q\hat n)
=\frac{4\pi}{3}q^*:q,
```

and

```math
\int d\Omega\,|\hat n\cdot q\hat n|^2
=\frac{8\pi}{15}q^*:q.
```

Therefore

```math
\boxed{
\int d\Omega\,F_q(\hat n)
=\frac{8\pi}{5}q^*:q.
}
```

Define the normalized angular radiation probability density

```math
w_q(\hat n)
\equiv
\frac{F_q(\hat n)}{(8\pi/5)q^*:q}.
```

Then

```math
\int d\Omega\,w_q=1.
```

Since `F_q <= q^*:q`,

```math
\boxed{
w_q(\hat n)\le\frac{5}{8\pi}.
}
```

Equivalently, the compact quadrupole directivity

```math
D_q(\hat n)=4\pi w_q(\hat n)
```

obeys

```math
\boxed{D_q\le\frac52.}
```

The bound is attainable: for propagation along `z`, a plus quadrupole proportional to `diag(1,-1,0)` is already TT and has `F_q=q^*:q`.

## 4. Normalized polarization amplitudes

Choose unit-norm TT polarization tensors `epsilon^lambda(n)`, `lambda=+ , x`, satisfying

```math
\epsilon^\lambda:\epsilon^{\lambda'}=\delta_{\lambda\lambda'}.
```

Define the normalized angular-mode amplitudes

```math
u_{q,\lambda}(\hat n)
=\frac{q:\epsilon^\lambda(\hat n)}
{\sqrt{(8\pi/5)q^*:q}}.
```

Then

```math
\sum_\lambda|u_{q,\lambda}(\hat n)|^2
=w_q(\hat n),
```

and

```math
\sum_\lambda\int d\Omega\,|u_{q,\lambda}|^2=1.
```

This normalization is classical: it is simply the total radiated power pattern divided by total power.

## 5. Separated translation and outgoing stationary phase

Place compact source `A` and receiver `B` a distance `R` apart along direction `Rhat`, with

```math
z=kR\gg1.
```

At fixed `k`, translating a plane-wave component by `R` contributes phase

```math
e^{ik\hat n\cdot\mathbf R}.
```

For an outgoing source mode and reciprocal incoming receiver mode, the retarded source-to-receiver contribution comes from the forward stationary point `n=Rhat`. The standard two-dimensional stationary-phase factor on the unit sphere is

```math
\frac{2\pi}{iz}e^{iz}.
```

Thus the leading directional mode-transfer amplitude is

```math
\boxed{
t_{BA}(\omega)
\sim
\frac{2\pi e^{ikR}}{ikR}
\sum_\lambda
u^*_{B,\lambda}(\hat R)
\nu_{A,\lambda}(\hat R).
}
```

Cauchy–Schwarz in polarization space gives

```math
\left|
\sum_\lambda
u^*_{B,\lambda}\nu_{A,\lambda}
\right|^2
\le w_B(\hat R)w_A(\hat R).
```

Using the compact-quadrupole angular-density bound,

```math
|t_{BA}|^2
\le
\frac{4\pi^2}{(kR)^2}
\left(\frac{5}{8\pi}\right)^2.
```

Therefore

```math
\boxed{
|t_{BA}|^2
\le
\frac{25}{16(kR)^2}
+O((kR)^{-4})
}
```

at the retained leading wave-zone power order.

For multiple compact quadrupolar endpoint modes, optimizing over normalized source and receiver superpositions cannot exceed this polarization/angular Cauchy–Schwarz maximum. Hence the normalized propagation operator obeys

```math
\boxed{
\|P_g(\omega)\|_{\rm op}^2
\le
\frac{25}{16[k(\omega)R]^2}
}
```

at leading separated-wave-zone order.

## 6. Directivity / reciprocal-area cross-check

The same coefficient follows from the generic reciprocal single-mode antenna relation

```math
A_e=\frac{\lambda^2D}{4\pi}.
```

A transmitter with directivity `D_A` produces directional flux `P_A D_A/(4 pi R^2)`. A reciprocal receiver with `D_B` captures effective area `lambda^2 D_B/(4 pi)`. Therefore

```math
\eta
= D_AD_B\left(\frac{\lambda}{4\pi R}\right)^2
=\frac{D_AD_B}{4(kR)^2}.
```

With `D_A,D_B <= 5/2`,

```math
\eta\le\frac{25}{16(kR)^2}.
```

This is a cross-check of the stationary-phase result rather than its starting assumption.

## 7. Post-derivation comparison with Experiment 01

Only after obtaining the coefficient above was Experiment 01's independent TT one-graviton audit consulted.

That real repository audit starts from canonical TT graviton modes, normalizes the one-graviton angular state, evaluates the full translated angular overlap, isolates the outgoing causal component, and finds

```math
t_{BA}^{\rm TT}(z)
\sim
-\frac{5i}{4}\frac{e^{iz}}{z},
```

so

```math
|t_{BA}^{\rm TT}|^2
\sim\frac{25}{16z^2}.
```

It also gives the exact finite-distance outgoing result

```math
|t_{BA}^{\rm TT}|^2
=\frac{25}{16z^2}
\left(
1-\frac{2}{z^2}
+\frac{3}{z^4}
-\frac{9}{z^6}
+\frac{9}{z^8}
\right).
```

Thus Stage C's classical angular/stationary-phase route independently reproduces the same leading coefficient before comparison with V7.

## 8. Prior-art boundary

Hirakawa, Narihara, and Fujimoto (1976) explicitly treat gravitational-antenna directivity within an eigenmode theory. Directivity as a concept is therefore historical here.

Stage C does not claim new antenna reciprocity, a new Friis law, or a new TT projector. The only role of this derivation is to establish the propagation normalization compatible with the Experiment-02 endpoint resource and spectral cut.

## 9. Scope

The result assumes:

- compact quadrupolar endpoints;
- free separated propagation in approximately flat spacetime;
- wave-zone `kR >> 1`;
- normalized reciprocal source/receiver gravitational modes;
- no extended phased aperture, relay, external cavity, or near-field coupling.

The displayed `25/16` is the leading power coefficient. The derivation does not claim the leading expression is exact at finite `kR`.

## 10. Required validation

`numerics/verify_tt_propagation_bound.py` should independently check:

1. the TT projector formula and `F_q <= q:q` for random complex STF tensors;
2. the sphere integral `int F dOmega = (8 pi/5) q:q` by numerical quadrature;
3. `D <= 5/2` and explicit saturation by an aligned plus quadrupole;
4. the polarization-overlap Cauchy–Schwarz bound for random source/receiver quadrupoles;
5. the resulting stationary-phase power prefactor `<=25/16`, with exact aligned saturation.

Only after real CI passes should the Experiment-02 `25/16` row be promoted.
