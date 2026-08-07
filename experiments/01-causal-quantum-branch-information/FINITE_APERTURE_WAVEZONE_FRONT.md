# Finite-Aperture Wave-Zone Quantum Front

**Timestamp:** 2026-08-07 17:20 EDT  
**Status:** Ideal mode-matched spherical-cap receiver geometry for the plus-type quadrupole difference mode.

## 1. Purpose

The exact causal-front theorem contains the useful source-mode coupling

$$
\kappa_\Delta
=\mathcal O_{SB}\kappa_g.
$$

For an ideal enclosing receiver, $\mathcal O_{SB}$ can approach unity. A finite receiver has limited angular access to the outgoing gravitational difference mode.

This note calculates the exact angular-access fraction for the same plus-type STF source quadrupole used throughout Experiment 01 and converts it into a maximum wave-zone quantum-reception range.

The receiver is an idealized coherent array distributed over a spherical cap and mode matched within that aperture. This is **not** the same as the previously analyzed pointlike/local tidal receiver.

---

## 2. Plus-type quadrupole radiation pattern

Take the source difference quadrupole tensor

$$
Q_{ij}=q\,\operatorname{diag}(1,-1,0).
$$

For propagation direction

$$
\hat{\mathbf n}
=(\sin\theta\cos\phi,
\sin\theta\sin\phi,
\cos\theta),
$$

the polarization-summed TT mode weight is

$$
\mathcal F(\theta,\phi)
=Q_{ij}\Lambda_{ij,kl}(\hat{\mathbf n})Q_{kl}^*.
$$

Direct contraction gives

$$
\boxed{
\mathcal F(\theta,\phi)
=2\cos^2\theta
+\frac12\sin^4\theta\cos^2(2\phi).
}
$$

Azimuthal integration yields

$$
\boxed{
\int_0^{2\pi}d\phi\,\mathcal F
=\frac\pi2
\left(1+6\cos^2\theta+\cos^4\theta\right).
}
$$

The full-sphere normalization is

$$
\int d\Omega\,\mathcal F
=\frac{16\pi}{5},
$$

consistent with the standard STF angular TT identity

$$
\int d\Omega\,
\Lambda_{ij,kl}Q_{ij}Q_{kl}^*
=\frac{8\pi}{5}Q_{ij}Q_{ij}^*.
$$

---

## 3. Exact spherical-cap access fraction

Let the ideal receiver coherently cover the polar cap

$$
0\le\theta\le\theta_0
$$

around the $+z$ axis.

Define

$$
\beta_{\rm cap}(\theta_0)
=
\frac{
\int_0^{\theta_0}d\theta\sin\theta
\int_0^{2\pi}d\phi\,\mathcal F
}
{
\int d\Omega\,\mathcal F
}.
$$

Writing

$$
c=\cos\theta_0,
$$

integration gives

$$
\boxed{
\beta_{\rm cap}(\theta_0)
=
\frac12
-
\frac{5c+10c^3+c^5}{32}.
}
$$

Checks:

$$
\theta_0=0\Rightarrow\beta_{\rm cap}=0,
$$

$$
\theta_0=\pi/2\Rightarrow\beta_{\rm cap}=1/2,
$$

$$
\theta_0=\pi\Rightarrow\beta_{\rm cap}=1.
$$

Thus a full hemisphere contains exactly half of the branch-difference mode norm for this symmetric source.

---

## 4. Small-aperture limit

For

$$
\theta_0\ll1,
$$

$$
\boxed{
\beta_{\rm cap}
=\frac58\theta_0^2+O(\theta_0^4).
}
$$

For a circular receiver array of radius $a_R$ at distance $R$,

$$
\theta_0\simeq\frac{a_R}{R},
$$

so

$$
\boxed{
\beta_{\rm cap}
\simeq
\frac58\frac{a_R^2}{R^2}.
}
$$

Equivalently, using aperture area $A_R=\pi a_R^2$,

$$
\boxed{
\beta_{\rm cap}
\simeq
\frac{5A_R}{8\pi R^2}.
}
$$

This is a geometry/mode-overlap limitation, separate from the intrinsic gravitational transition rate of the receiver elements.

---

## 5. Useful coupling rate

Let

- $\kappa_g$ be the total gravitational linewidth of the optimally collective receiver mode;
- $\mathcal O_Q$ be source-receiver quadrupole-tensor overlap;
- $\mathcal O_t$ be temporal/spectral overlap;
- $\mathcal O_{\rm other}$ collect any remaining normalized matching factors.

Then the useful difference-mode rate is bounded by

$$
\boxed{
\kappa_\Delta(R)
=\beta_{\rm cap}(R)
\mathcal O_Q\mathcal O_t\mathcal O_{\rm other}\,
\kappa_g.
}
$$

For the small-aperture limit, define

$$
\mathcal O=\mathcal O_Q\mathcal O_t\mathcal O_{\rm other},
$$

and obtain

$$
\boxed{
\kappa_\Delta(R)
\simeq
\frac58
\frac{a_R^2}{R^2}
\mathcal O\,\kappa_g.
}
$$

---

## 6. Maximum NPT reception range

For a stationary passive thermal receiver, the exact finite-cat theorem requires

$$
\kappa_\Delta(R)>\Gamma_{\rm th}.
$$

In the small-aperture limit this gives

$$
\frac58
\frac{a_R^2}{R^2}
\mathcal O\kappa_g
>\Gamma_{\rm th}.
$$

Therefore

$$
\boxed{
R<R_{\rm NPT}^{\max}
\simeq
 a_R
\sqrt{
\frac{5\mathcal O\kappa_g}
{8\Gamma_{\rm th}}
}.
}
$$

This is the **maximum quantum-reception range** of the ideal finite-aperture wave-zone receiver within the stated model.

It is a strict channel-quality range, not a classical signal-to-noise range.

---

## 7. Finite-certification range

The exact finite-strength witness requires

$$
\kappa_\Delta
>
\Gamma_{\rm th}
\left(1+\frac{\Lambda_{\rm req}}{N_\Delta}\right).
$$

Thus

$$
\boxed{
R<R_\Lambda^{\max}
\simeq
 a_R
\sqrt{
\frac{5\mathcal O\kappa_g}
{8\Gamma_{\rm th}
(1+\Lambda_{\rm req}/N_\Delta)}
}.
}
$$

The finite-certification range is smaller than the mathematical NPT range and shrinks rapidly for weak branch sources.

---

## 8. Wave-zone compatibility condition

To interpret the propagating mode cleanly as wave-zone radiation, require schematically

$$
R\gtrsim\zeta\frac{c}{\omega},
$$

where $\zeta$ is an order-unity or larger criterion specifying how deep into the radiation zone one wishes to operate.

A finite-aperture NPT experiment therefore requires a nonempty interval

$$
\zeta\frac{c}{\omega}
\lesssim R<R_{\rm NPT}^{\max}.
$$

A necessary geometry/receiver condition is

$$
\boxed{
 a_R
\sqrt{
\frac{5\mathcal O\kappa_g}
{8\Gamma_{\rm th}}
}
\gtrsim
\zeta\frac{c}{\omega}.
}
$$

Equivalently,

$$
\boxed{
\frac{a_R\omega}{c}
\sqrt{
\frac{5\mathcal O\kappa_g}
{8\Gamma_{\rm th}}
}
\gtrsim\zeta.
}
$$

This makes the wave-zone dilemma quantitative: a receiver must be large enough in wavelength units and quantum-efficient enough to catch the branch mode before thermal classicalization.

---

## 9. Full-cap formula for exact range

For a receiver with non-negligible angular radius, avoid the small-cap approximation. The exact condition is

$$
\boxed{
\beta_{\rm cap}(\theta_0)
\mathcal O\kappa_g
>\Gamma_{\rm th},
}
$$

with

$$
\theta_0=\arctan(a_R/R)
$$

for the simplest disk-like geometry and

$$
\beta_{\rm cap}
=\frac12-rac{5c+10c^3+c^5}{32}.
$$

This implicit equation determines the exact idealized quantum-reception range.

---

## 10. Interpretation

> **A classical gravitational wave can be detected from arbitrarily far away in principle if one integrates long enough and has enough classical sensitivity. Coherent quantum reception is stricter. A finite receiver must capture enough of the specific branch-difference wave mode before its own uncontrolled channels create an equivalent classical record. For a fixed physical aperture, the useful mode fraction falls as $R^{-2}$ in the far field, creating a genuine maximum range for NPT transfer at nonzero thermal noise.**

This is not a universal limit on quantum gravity. It is a receiver-channel bound under finite angular access, linear coherent mode matching, and stationary thermal noise.

---

## 11. Next step

Combine

$$
R_{\rm NPT}^{\max},
\qquad
R_\Lambda^{\max},
\qquad
T_{\rm NPT}^{\min}(R),
\qquad
T_\Lambda^{\min}(R)
$$

into one spacetime **quantum reception cone** and determine its asymptotic shape for a finite physical receiver.