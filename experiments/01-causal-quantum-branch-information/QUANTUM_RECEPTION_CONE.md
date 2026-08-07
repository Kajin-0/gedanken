# Quantum Reception Cone for a Finite Wave-Zone Receiver

**Timestamp:** 2026-08-07 17:24 EDT  
**Status:** Exact asymptotic front within the small-aperture, stationary passive Markov receiver model.

## 1. Setup

For the plus-quadrupole difference mode, a small ideal coherent receiver aperture of radius $a_R$ at distance $R$ has accessible branch-mode fraction

$$
\beta_{\rm cap}
\simeq
\frac58\frac{a_R^2}{R^2}.
$$

Let

$$
\mathcal O
=\mathcal O_Q\mathcal O_t\mathcal O_{\rm other}
$$

be the remaining normalized source-receiver mode overlap and let $\kappa_g$ be the receiver's total gravitational linewidth.

Define

$$
\boxed{
K
=\frac58a_R^2\mathcal O\kappa_g.
}
$$

Then the useful branch-mode coupling is

$$
\boxed{
\kappa_\Delta(R)=\frac{K}{R^2}.
}
$$

Let the receiver have distance-independent uncontrolled damping

$$
\kappa_0=\sum_a\kappa_a
$$

and stationary thermal injection

$$
\Gamma_{\rm th}=\sum_a\bar n_a\kappa_a.
$$

Thus

$$
\boxed{
\kappa_{\rm tot}(R)
=\kappa_0+\frac{K}{R^2}.
}
$$

---

## 2. Maximum quantum-reception distance

The exact finite-cat NPT condition requires

$$
\kappa_\Delta(R)>\Gamma_{\rm th}.
$$

Therefore define

$$
\boxed{
R_Q
=\sqrt{\frac{K}{\Gamma_{\rm th}}}
=
 a_R
\sqrt{
\frac{5\mathcal O\kappa_g}
{8\Gamma_{\rm th}}
}.
}
$$

Then

$$
\boxed{
R<R_Q
}
$$

is necessary and sufficient for the existence of an NPT front in the ideal small-aperture model.

For

$$
R\ge R_Q,
$$

no finite binary coherent source branch encoding can become NPT with the stationary receiver, regardless of integration time or cat amplitude.

---

## 3. Exact NPT spacetime front

The exact waveform-optimal front theorem gives

$$
T_{\rm NPT}^{\min}(R)
=
\frac Rc+
\frac1{\kappa_{\rm tot}(R)}
\ln\left[
\frac{\kappa_\Delta(R)}
{\kappa_\Delta(R)-\Gamma_{\rm th}}
\right].
$$

Using

$$
\frac{\Gamma_{\rm th}}{\kappa_\Delta(R)}
=\frac{R^2}{R_Q^2},
$$

we obtain the compact result

$$
\boxed{
T_{\rm NPT}^{\min}(R)
=
\frac Rc
-
\frac{1}
{\kappa_0+K/R^2}
\ln\left[
1-\left(\frac{R}{R_Q}\right)^2
\right],
\qquad
0<R<R_Q.
}
$$

This is the idealized **quantum reception cone boundary**.

The region

$$
T>T_{\rm NPT}^{\min}(R),
\qquad R<R_Q,
$$

is the spacetime region in which an optimally shaped incoming branch mode can have generated source-receiver NPT entanglement.

---

## 4. Dimensionless universal shape

Define

$$
x=\frac{R}{R_Q},
$$

and

$$
\rho=\frac{\kappa_0}{\Gamma_{\rm th}}.
$$

The build time beyond the ordinary light cone is

$$
\tau_Q(R)
=T_{\rm NPT}^{\min}(R)-R/c.
$$

Then

$$
\boxed{
\Gamma_{\rm th}\tau_Q
=
-\frac{x^2}{1+\rho x^2}
\ln(1-x^2),
\qquad 0<x<1.
}
$$

Apart from the ordinary propagation term $R/c$, the entire front shape is controlled by one dimensionless receiver parameter $\rho$.

---

## 5. Near-source asymptotic

For

$$
x\ll1,
$$

$$
-\ln(1-x^2)
=x^2+O(x^4).
$$

Therefore

$$
\boxed{
\tau_Q
\simeq
\frac{x^4}{\Gamma_{\rm th}}
=
\frac{\Gamma_{\rm th}R^4}{K^2}
}
$$

when the useful branch-mode coupling dominates the uncontrolled linewidth.

Thus the quantum build delay falls extremely rapidly at short range:

$$
\tau_Q\propto R^4.
$$

The front approaches the ordinary light cone,

$$
T_{\rm NPT}\to R/c,
$$

although the small-aperture far-field approximation itself should not be extrapolated into the true near zone.

---

## 6. Range-boundary asymptotic

Let

$$
x=1-\epsilon,
\qquad
0<\epsilon\ll1.
$$

Then

$$
1-x^2\simeq2\epsilon.
$$

The useful coupling approaches the thermal threshold,

$$
\kappa_\Delta\to\Gamma_{\rm th},
$$

and

$$
\boxed{
\tau_Q
\simeq
\frac1{\kappa_0+\Gamma_{\rm th}}
\ln\frac1{2\epsilon}.
}
$$

Hence

$$
\boxed{
T_{\rm NPT}^{\min}(R)\to\infty
\quad\text{as}\quad
R\to R_Q^-.
}
$$

The quantum front therefore has a **vertical logarithmic asymptote** at a finite spatial range.

This is the spacetime version of the entanglement-breaking critical slowing derived earlier.

---

## 7. Finite-certification cone

For exact three-element witness margin

$$
\Lambda\ge\Lambda_{\rm req}>0,
$$

define the effective required record-formation rate

$$
\Gamma_\Lambda
=\Gamma_{\rm th}
\left(1+\frac{\Lambda_{\rm req}}{N_\Delta}\right).
$$

Then the maximum certification distance is

$$
\boxed{
R_\Lambda
=\sqrt{\frac{K}{\Gamma_\Lambda}}
=
\frac{R_Q}
{\sqrt{1+\Lambda_{\rm req}/N_\Delta}}.
}
$$

The corresponding exact optimal front is

$$
\boxed{
T_\Lambda^{\min}(R)
=
\frac Rc
-
\frac1{\kappa_0+K/R^2}
\ln\left[
1-\left(\frac{R}{R_\Lambda}\right)^2
\right],
\qquad R<R_\Lambda.
}
$$

Thus there is a nested family of causal quantum reception cones:

$$
R_\Lambda<R_Q
$$

for every finite positive witness requirement.

---

## 8. Source dependence

The mathematical NPT cone depends only on channel quality, but the finite-certification cone depends explicitly on source branch strength through

$$
N_\Delta
=\frac{G}{5\pi\hbar c^5}
\int_0^\infty d\omega\,\omega^5
|\Delta\widetilde Q_{ij}(\omega)|^2.
$$

For a narrow-band plus quadrupole,

$$
N_\Delta
\simeq
\frac{Gq_0^2\omega_0^5T_f}{5\hbar c^5}.
$$

Therefore stronger/faster/longer source branch motion expands the finite-certification cone toward the limiting NPT cone but can never push it beyond $R_Q$.

---

## 9. Wave-zone lower boundary

The wave-zone description also requires

$$
R\gtrsim R_{\rm WZ}
\equiv\zeta c/\omega.
$$

Thus a genuine wave-zone quantum reception region exists only if

$$
\boxed{
R_Q>R_{\rm WZ}.
}
$$

For finite certification,

$$
\boxed{
R_\Lambda>R_{\rm WZ}.
}
$$

This creates a spatial window

$$
R_{\rm WZ}\lesssim R<R_Q
$$

for mathematical NPT transfer and a smaller window for finite witness strength.

---

## 10. Conceptual interpretation

> **The ordinary light cone says when the gravitational disturbance is allowed to arrive. The quantum reception cone says where and when that arriving disturbance can still carry entanglement into a finite noisy receiver. At nonzero receiver temperature, the quantum cone can terminate at a finite radius even though the classical gravitational wave continues indefinitely. As the receiver approaches that radius, the quantum front retreats logarithmically into the future.**

This is a receiver-channel statement, not a modification of spacetime causality and not a fundamental range limit on the gravitational field itself.

---

## 11. Potential paper figure

A natural spacetime figure would plot

1. the light cone $T=R/c$;
2. the NPT front $T_{\rm NPT}^{\min}(R)$;
3. one or more finite-certification fronts $T_\Lambda^{\min}(R)$;
4. the vertical asymptotes $R_Q$ and $R_\Lambda$;
5. the wave-zone lower radius $R_{\rm WZ}$.

This would visually distinguish **causal propagation**, **quantum-capability latency**, and **finite-certification latency**.

## 12. Strongest next step

Determine whether this finite-range/logarithmic-front structure has a known analogue in quantum communication theory and then insert realistic/idealized gravitational receiver parameters to quantify how extreme the wave-zone requirements are.