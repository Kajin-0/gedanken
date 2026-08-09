# TT Propagation Bound for Compact Quadrupole Channels

## 1. Purpose

The passive-network cut-set theorem contains an abstract propagation contraction

```math
\eta_{\max}(\omega)
=\|P_g(\omega)\|_{\rm op}^2.
```

V7 obtained

```math
\frac{25}{16(kR)^2}
```

for one aligned plus-quadrupole source and reciprocal receiver. This note asks a stronger question:

> Is that coefficient the largest possible wave-zone link between **any compact mass-quadrupole source and reciprocal compact quadrupole receiver** at the same frequency?

Within the stated compact, weak-field, quadrupole, reciprocal, one-way wave-zone class, the answer is yes.

---

## 2. General STF quadrupole radiation

Let

```math
Q_{ij}=Q_{ji},
\qquad
Q_{ii}=0
```

be an arbitrary possibly complex symmetric trace-free transition quadrupole at angular frequency `omega`.

For propagation direction `n`, define

```math
P_{ij}=\delta_{ij}-n_i n_j
```

and the transverse-traceless projector

```math
\boxed{
\Lambda_{ij,kl}(\hat n)
=
\frac12\left(
P_{ik}P_{jl}+P_{il}P_{jk}-P_{ij}P_{kl}
\right).
}
```

With polarization tensors normalized by

```math
\epsilon_{ij}^{(\lambda)}
\epsilon_{ij}^{(\lambda')}=\delta_{\lambda\lambda'},
```

the polarization completeness relation is

```math
\sum_\lambda
\epsilon_{ij}^{(\lambda)}
\epsilon_{kl}^{(\lambda)*}
=\Lambda_{ij,kl}.
```

Therefore

```math
\boxed{
\sum_\lambda
|Q_{ij}\epsilon_{ij}^{(\lambda)}|^2
=
Q_{ij}^*\Lambda_{ij,kl}Q_{kl}.
}
```

Because `Lambda` is an orthogonal projector on the five-dimensional STF tensor space,

```math
0\le Q^*:\Lambda:Q\le Q^*:Q.
```

---

## 3. Total quadrupole linewidth

The one-graviton angular rate is

```math
\frac{d\kappa_g}{d\Omega}
=
\frac{G\omega^5}{4\pi\hbar c^5}
Q^*:\Lambda(\hat n):Q.
```

Rotational invariance implies that the angular integral of `Lambda` over the sphere is proportional to the identity on STF tensor space:

```math
\int d\Omega\,\Lambda(\hat n)
=c\,I_{\rm STF}.
```

At every direction `Lambda` has rank two, so taking the trace on the five-dimensional STF space gives

```math
8\pi
=
\int d\Omega\,\operatorname{Tr}_{\rm STF}\Lambda
=5c.
```

Hence

```math
\boxed{
\int d\Omega\,\Lambda(\hat n)
=
\frac{8\pi}{5}I_{\rm STF}.
}
```

The total gravitational linewidth is therefore

```math
\boxed{
\kappa_g
=
\frac{2G\omega^5}{5\hbar c^5}
Q^*:Q.
}
```

This reproduces the V7 plus-mode normalization because for

```math
Q=q\,\operatorname{diag}(1,-1,0)
```

one has `Q*:Q=2|q|^2`.

---

## 4. Universal compact-quadrupole directivity ceiling

Define gravitational-wave directivity in the usual way,

```math
D_Q(\hat n)
\equiv
4\pi
\frac{d\kappa_g/d\Omega}{\kappa_g}.
```

Substituting the differential and total rates gives

```math
\boxed{
D_Q(\hat n)
=
\frac52
\frac{Q^*:\Lambda(\hat n):Q}{Q^*:Q}.
}
```

Because `Lambda` is a projector,

```math
\boxed{
D_Q(\hat n)\le\frac52.
}
```

### Equality condition

Equality holds exactly when

```math
\Lambda(\hat n)Q=Q,
```

that is, when the quadrupole tensor is already transverse-traceless with respect to the chosen propagation direction.

For `n = z`, both

```math
Q_+\propto\operatorname{diag}(1,-1,0)
```

and the corresponding cross tensor lie in that two-dimensional TT subspace. Thus the V7 aligned plus quadrupole already saturates the maximum possible compact-quadrupole directivity.

This is not a special property of the four-spoke source geometry; it is a property of the `l=2`, STF, TT radiation channel.

---

## 5. Reciprocal receiver gain

For a reciprocal compact quadrupole receiver coupled to the same radiation family, transmit and receive gain are equal channel by channel. Therefore the receiver gain obeys the same ceiling,

```math
\boxed{
G_B\le\frac52.
}
```

The corresponding maximum reciprocal effective area is

```math
A_e
=G_B\frac{\lambda^2}{4\pi}
\le
\frac52\frac{\lambda^2}{4\pi}
=
\frac{5\pi}{2k^2}.
```

The final equality uses `lambda = 2 pi / k` and reproduces the V7 reciprocal-absorption normalization.

---

## 6. Wave-zone source-to-receiver ceiling

For a weak one-way reciprocal far-field link, the Friis form is

```math
\eta_{BA}
=
G_A G_B
\left(\frac{\lambda}{4\pi R}\right)^2
\mathcal O,
```

where `0 <= O <= 1` contains residual polarization/tensor/orientation/temporal mismatch not already absorbed into the chosen singular channel.

Using

```math
G_A\le\frac52,
\qquad
G_B\le\frac52,
```

and

```math
\frac{\lambda}{4\pi R}
=\frac{1}{2kR},
```

gives

```math
\boxed{
\eta_{BA}
\le
\frac{25}{16(kR)^2}.
}
```

More generally,

```math
\boxed{
\eta_{BA}
\le
\frac{25\mathcal O}{16(kR)^2},
\qquad 0\le\mathcal O\le1.
}
```

The coefficient is saturated by an aligned reciprocal TT quadrupole pair with perfect polarization/tensor matching in the leading wave-zone limit.

---

## 7. Propagation-operator statement

Let `P_g(omega)` be the propagation map between normalized compact source and receiver quadrupole radiation-channel spaces. Its operator norm is the largest transfer amplitude over all normalized source and receiver superpositions. The gain argument above already maximizes over the STF source tensor and reciprocal receiver tensor, so

```math
\boxed{
\|P_g(\omega)\|_{\rm op}^2
\le
\frac{25}{16[k(\omega)R]^2}
}
```

in the weak one-way wave zone.

Therefore, over a declared operating band `B` lying entirely in the wave zone,

```math
\boxed{
\eta_{\max}
\equiv
\sup_{\omega\in\mathcal B}
\|P_g(\omega)\|_{\rm op}^2
\le
\sup_{\omega\in\mathcal B}
\frac{25}{16[k(\omega)R]^2}.
}
```

For a narrow band around carrier `omega_0`,

```math
\eta_{\max}
\lesssim
\frac{25}{16(k_0R)^2}
```

up to the declared fractional-bandwidth correction.

---

## 8. Closed material + geometry throughput theorem

Combining this propagation ceiling with the passive linear-network material theorem gives, for compact passive nonrelativistic linear bosonic endpoints whose retained frequencies satisfy `0 < omega <= Omega` and whose source-receiver separation is in the wave zone throughout the operating band,

```math
\Gamma_{\rm coh}
\le
\eta_{\max}
\frac{4G\Omega^4}{3c^5}
\min(\langle I_A\rangle,\langle I_B\rangle).
```

For a narrow band centered at `omega` with `k=omega/c`, this becomes

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25}{16(kR)^2}
\frac{4G\omega^4}{3c^5}
\min(\langle I_A\rangle,\langle I_B\rangle).
}
```

Equivalently,

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25}{24(kR)^2}
\omega
\min\!\left(
\mathcal C_A\beta_A^3,
\mathcal C_B\beta_B^3
\right).
}
```

This is now independent of the four-spoke construction. The four-spoke plus mode is an explicit source realization that saturates the compact-quadrupole directivity ceiling, not an assumption of the theorem.

---

## 9. Scope limitations

The `5/2` and `25/16` ceilings here are restricted to:

- compact mass-quadrupole (`l=2`) radiation;
- linearized weak-field gravity;
- nonrelativistic source/receiver matter;
- reciprocal compact quadrupole reception;
- weak one-way wave-zone propagation;
- no extended phased array whose physical aperture is large compared with the compact-source scale;
- no use of higher multipoles or relativistic beaming;
- no reactive near-field interpretation.

An extended distributed aperture can obtain larger directivity by using spatial phase across its size; that is a different architecture and must be bounded by its actual aperture rather than by the compact quadrupole theorem.

---

## 10. Claim discipline

Allowed:

> Any compact STF mass quadrupole has gravitational-wave directivity at most `5/2`. By reciprocity, the same ceiling applies to a compact quadrupole receiver, yielding a maximum one-way wave-zone quadrupole link factor `25/[16(kR)^2]`.

Not allowed:

- `25/16` is a universal bound for all gravitational antennas;
- the result covers extended arrays or higher multipoles;
- the result applies in the near field;
- the result is independent of reciprocity;
- the result is a fundamental bound of quantum gravity rather than a compact linearized-gravity quadrupole theorem.
