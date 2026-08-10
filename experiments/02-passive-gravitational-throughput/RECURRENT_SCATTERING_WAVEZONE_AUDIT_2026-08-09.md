# Recurrent Passive Wave-Zone Scattering Audit — 2026-08-09

## Purpose

Test the last major physical scope objection in the hostile referee report:

> The manuscript factors source -> one-pass propagation -> receiver. Could passive reciprocal backaction, repeated far-field returns, or common-bath multiple scattering invalidate the leading `25/16` propagation coefficient or the final `1/R^2` throughput ceiling?

The answer is favorable within the same compact far-zone class:

> **If each endpoint is passive and the single-hop gravitational propagation operator has norm `p<1`, all recurrent two-endpoint scattering can be summed exactly as a Redheffer/Born geometric series. Its effective forward propagation norm is at most `p/(1-p^2)`. Therefore the recurrent-scattering upper ceiling exceeds the one-hop power ceiling only by a relative `O(p^2)` and an absolute `O(p^4)`. Since compact TT propagation has `p=O((kR)^-1)`, repeated returns can increase the power ceiling only at `O((kR)^-4)`, beyond the retained leading `O((kR)^-2)` wave-zone term. The actual recurrent transfer can be smaller because of interference.**

Thus the leading `25/16` coefficient is not vulnerable to passive recurrent scattering between the same two compact endpoints.

---

## 1. Exact endpoint scattering blocks

At a fixed frequency, keep each endpoint internally exact. Write the source endpoint gravitational output as

```math
b_A^{\rm out}
=S_{Au}u+R_A b_A^{\rm in},
```

and the receiver endpoint as

```math
\begin{aligned}
b_B^{\rm out}&=R_B b_B^{\rm in},\\
v&=S_{Bv}b_B^{\rm in}.
\end{aligned}
```

Here

- `S_Au` is the exact local-input -> outgoing-gravitational block of endpoint A;
- `S_Bv` is the exact incoming-gravitational -> useful-output block of endpoint B;
- `R_A` and `R_B` are the exact gravitational reflection blocks, including all internal resonances and coherent mode mixing.

For passive endpoints, every scattering subblock is a contraction:

```math
\|R_A\|_{\rm op}\le1,
\qquad
\|R_B\|_{\rm op}\le1.
```

No weak-resonance approximation is made inside either endpoint.

---

## 2. Bidirectional free propagation

Let

```math
P_{BA}:\mathcal H_A^{\rm out}\to\mathcal H_B^{\rm in},
```

```math
P_{AB}:\mathcal H_B^{\rm out}\to\mathcal H_A^{\rm in}
```

be the two free wave-zone propagation operators.

Define

```math
p_+=\|P_{BA}\|_{\rm op},
\qquad
p_-=\|P_{AB}\|_{\rm op}.
```

For reciprocal separated propagation in the same compact channel class,

```math
p_+=p_-=p.
```

The normalized TT result gives, at leading order,

```math
p^2
\le
\eta
\equiv
\frac{25}{16(kR)^2}
+O((kR)^{-3}).
```

In the wave zone `kR >> 1`, so `p<1` by a wide margin.

---

## 3. Exact repeated-return series

The source-generated outgoing field in the absence of a returned gravitational wave is

```math
x=S_{Au}u.
```

Its first arrival at B is

```math
y_0=P_{BA}x.
```

After reflection at B, return to A, reflection at A, and another forward hop, the next contribution at B is

```math
y_1
=P_{BA}R_A P_{AB}R_B P_{BA}x.
```

Define the B-side round-trip loop operator

```math
L
=P_{BA}R_A P_{AB}R_B.
```

Then

```math
b_B^{\rm in}
=\sum_{m=0}^{\infty}L^mP_{BA}x.
```

This is the standard multiple-scattering / Redheffer feedback series. Since

```math
\|L\|_{\rm op}
\le p_+p_-,
```

the Neumann series converges whenever

```math
p_+p_-<1.
```

Hence

```math
\boxed{
b_B^{\rm in}
=(I-L)^{-1}P_{BA}S_{Au}u.
}
```

The exact end-to-end transfer is therefore

```math
\boxed{
T_{\rm rec}
=S_{Bv}(I-L)^{-1}P_{BA}S_{Au}.
}
```

This includes arbitrarily many reciprocal returns between the same two passive endpoints.

---

## 4. Operator-norm bound

From the Neumann resolvent bound,

```math
\|(I-L)^{-1}\|_{\rm op}
\le
\frac{1}{1-\|L\|_{\rm op}}
\le
\frac{1}{1-p_+p_-}.
```

Therefore the effective propagation factor obeys

```math
\boxed{
\|P_{\rm eff}\|_{\rm op}
\le
\frac{p_+}{1-p_+p_-}.
}
```

For reciprocal propagation,

```math
\boxed{
\|P_{\rm eff}\|_{\rm op}
\le
\frac{p}{1-p^2}.
}
```

Squaring,

```math
\boxed{
\eta_{\rm rec}
\le
\frac{\eta}{(1-\eta)^2},
\qquad
\eta=p^2.
}
```

This bound is independent of the detailed frequency dependence of `R_A` and `R_B`; endpoint resonances are already contained inside contraction-valued reflection blocks.

A high-Q endpoint cannot create a recurrent far-field pole unless the full round-trip loop reaches unit norm. In the compact wave zone,

```math
\|L\|\le\eta\ll1,
```

so passive repeated scattering cannot approach that condition.

---

## 5. Leading-order asymptotics

Expand the recurrent upper ceiling,

```math
\frac{\eta}{(1-\eta)^2}
=\eta+2\eta^2+3\eta^3+\cdots.
```

With

```math
\eta=O((kR)^{-2}),
```

we therefore have

```math
\boxed{
\eta_{\rm rec}
\le
\eta+O((kR)^{-4}).
}
```

This is an upper-bound statement. It does not assert that the actual recurrent transfer equals the one-hop transfer plus a positive `O((kR)^-4)` correction; interference can reduce the transfer. What is proved is exactly what the throughput theorem needs: recurrent scattering cannot increase the leading power-transfer ceiling at order `1/R^2`.

The current one-pass TT amplitude itself has omitted higher far-zone terms beginning at

```math
O((kR)^{-2})
```

in amplitude, which can generate power corrections at `O((kR)^-3)`. The possible recurrent enhancement of the upper ceiling is therefore parametrically **more subleading** than the first already-neglected one-pass propagation correction.

This is the central result of the audit.

---

## 6. Recurrent end-to-end H2 cut set

At each frequency,

```math
T_{\rm rec}
=S_{Bv}P_{\rm eff}S_{Au}.
```

Using the same Hilbert--Schmidt/operator-norm inequalities as the one-pass proof,

```math
\Gamma_{\rm coh}^{\rm rec}
\le
\eta_{\rm rec,max}
\min\!\left[
\|S_{Au}\|_2^2,
\|S_{Bv}\|_2^2
\right].
```

The passive endpoint theorem gives

```math
\|S_{Au}\|_2^2
\le\operatorname{Tr}(K_{g,A}^\dagger K_{g,A}),
```

```math
\|S_{Bv}\|_2^2
\le\operatorname{Tr}(K_{g,B}^\dagger K_{g,B}).
```

Therefore

```math
\boxed{
\Gamma_{\rm coh}^{\rm rec}
\le
\frac{\eta_{\max}}{(1-\eta_{\max})^2}
\min\!\left[
\operatorname{Tr}(K_{g,A}^\dagger K_{g,A}),
\operatorname{Tr}(K_{g,B}^\dagger K_{g,B})
\right].
}
```

Using the classical inertia resource,

```math
\boxed{
\Gamma_{\rm coh}^{\rm rec}
\le
\frac{\eta_{\max}}{(1-\eta_{\max})^2}
\frac{4G\Omega^4}{3c^5}
\min(I_A,I_B).
}
```

This is an exact passive recurrent-scattering upper bound within the two-endpoint scattering model.

---

## 7. Compact TT specialization

At leading compact wave-zone order,

```math
\eta_{\max}
\le
\frac{25}{16(kR)^2}.
```

Hence

```math
\Gamma_{\rm coh}^{\rm rec}
\le
\frac{
\frac{25}{16(kR)^2}
}{
\left[1-\frac{25}{16(kR)^2}\right]^2
}
\frac{4G\Omega^4}{3c^5}
\min(I_A,I_B),
```

provided the leading TT bound is used consistently in the denominator and `kR>5/4`.

In the narrowband wave zone, `Omega approx omega` and `k=omega/c`, so

```math
\boxed{
\Gamma_{\rm coh}^{\rm rec}
\lesssim
\frac{25G\omega^2}{12c^3R^2}
\min(I_A,I_B)
\left[1+O((kR)^{-2})\right].
}
```

Therefore the manuscript's headline coefficient is unchanged at retained order even if passive two-endpoint recurrent scattering is allowed.

---

## 8. Relation to common-bath language

A shared radiative continuum can be reorganized into endpoint scattering blocks plus propagation between the two spatially separated interaction regions. In this representation,

- local self-energy and internal endpoint resonance physics are already inside `S_Au`, `S_Bv`, `R_A`, and `R_B`;
- one propagation between interaction regions contributes one factor of `P`;
- collective return processes correspond to additional round trips and therefore additional factors of `P_AB P_BA`.

The present result does not construct a fully non-Markov common-bath master equation. It instead proves that, whenever the separated wave-zone scattering representation is valid, passive recurrent corrections cannot increase the leading `1/R^2` throughput ceiling.

That is the physically relevant question for the current asymptotic theorem.

---

## 9. What remains outside scope

This result still does not cover

- a third gravitational relay or mirror placed between A and B;
- an engineered extended cavity whose additional reflector is not part of the two compact endpoints;
- near-field reactive coupling;
- curved-background focusing;
- active gain or parametric feedback;
- spatially extended phased apertures;
- nonseparable strongly overlapping source/receiver regions.

Those architectures change the propagation problem rather than merely summing repeated returns between the same separated compact endpoints.

---

## 10. Prior-art status

The multiple-scattering algebra is standard. The appropriate historical language is the Redheffer star product / invariant-imbedding formalism for connecting scattering systems:

Raymond Redheffer, **"On the Relation of Transmission-Line Theory to Scattering and Transfer,"** Journal of Mathematics and Physics 41, 1--41 (1962), DOI `10.1002/sapm19624111`.

No novelty is claimed for the geometric-series or scattering-network mathematics.

The useful observation for Experiment 02 is only the asymptotic consequence:

```math
\boxed{
\text{possible passive recurrent increase of the power ceiling}
=O((kR)^{-4}),
}
```

so the gravity-specific leading `25/16` propagation coefficient and final `1/R^2` inertia ceiling survive the strongest two-endpoint recurrence objection.

---

## Verdict

```text
PASSIVE TWO-ENDPOINT RECURRENT SCATTERING:      BOUNDED
ROUND-TRIP LOOP NORM:                           <= p^2
EFFECTIVE FORWARD AMPLITUDE NORM:               <= p/(1-p^2)
EFFECTIVE POWER FACTOR:                         <= eta/(1-eta)^2
RECURRENT POWER-CEILING ENHANCEMENT:            O((kR)^-4)
ACTUAL RECURRENT TRANSFER EQUALS ONE-HOP+O(...): NOT CLAIMED
LEADING 25/16 COEFFICIENT:                      UNCHANGED AS UPPER CEILING
LEADING 1/R^2 HEADLINE THEOREM:                 UNCHANGED
EXTERNAL RELAYS / CAVITIES / NEAR FIELD:        NOT COVERED
```

The manuscript may safely replace the stronger phrase "one-pass only" by the more accurate statement that the displayed headline theorem is the **leading separated wave-zone upper ceiling**, with passive recurrent returns between the same two endpoints unable to increase it until beyond retained order.
