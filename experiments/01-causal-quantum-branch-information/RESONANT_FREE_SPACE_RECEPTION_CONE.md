# Resonant Free-Space Gravitational Quantum Reception Cone

**Timestamp:** 2026-08-07 17:25 EDT  
**Status:** Far-zone aligned-plus-quadrupole result obtained by matching the exact retarded Green coupling to a cascaded input-output channel. This supersedes the geometric-aperture cone as the cleaner model for a compact resonant receiver.

## 1. Starting point: normalized retarded cross response

For resonant aligned plus-type quadrupole transitions $A$ and $B$, the exact retarded source-receiver coefficient is

$$
\Sigma_{AB}^{R}(\omega,R)
=\frac54
\sqrt{\kappa_{g,A}\kappa_{g,B}}
\frac{P(\epsilon)e^{i\epsilon}}{\epsilon^5},
\qquad
\epsilon=kR=\frac{\omega R}{c}.
$$

In the wave zone,

$$
\boxed{
\Sigma_{AB}^{R}
\simeq
\frac54
\frac{e^{ikR}}{kR}
\sqrt{\kappa_{g,A}\kappa_{g,B}}.
}
$$

See `NORMALIZED_GRAVITATIONAL_CROSS_RESPONSE.md`.

---

## 2. Match to a cascaded source-to-receiver channel

For a source oscillator radiating into a normalized outgoing mode that reaches receiver $B$ with propagation efficiency $\eta_{\rm ff}$, the standard one-way cascaded drive has magnitude

$$
\sqrt{\eta_{\rm ff}\kappa_{g,A}\kappa_{g,B}}.
$$

Matching this to the far-zone retarded cross response gives

$$
\sqrt{\eta_{\rm ff}}
=\frac{5}{4kR},
$$

and therefore

$$
\boxed{
\eta_{\rm ff}(R)
=\frac{25}{16(kR)^2}.
}
$$

This interpretation is restricted to the wave zone where

$$
kR\gg1
$$

and therefore $\eta_{\rm ff}\ll1$. The full near-zone retarded coefficient can exceed the bounds appropriate to a propagating loss channel because there the interaction contains large reactive/virtual-field contributions and should not be interpreted as a transmissivity.

The numerical coefficient applies to the aligned plus-quadrupole geometry and the stated input-output normalization. General source/receiver tensor and temporal mismatch should multiply this by a normalized factor

$$
0\le\mathcal O\le1.
$$

Thus more generally

$$
\boxed{
\eta_{\rm ff}(R)
=\frac{25\mathcal O}{16(kR)^2}
}
$$

in the far zone.

---

## 3. Effective coherent cross-section

If one formally writes

$$
\eta_{\rm ff}
=\frac{A_{\rm eff}}{4\pi R^2},
$$

then

$$
\boxed{
A_{\rm eff}
=\frac{25\pi\mathcal O}{4k^2}.
}
$$

This is of order the gravitational wavelength squared and can be much larger than the receiver's material area when

$$
kL_B\ll1.
$$

Therefore a resonant quantum receiver cannot generally be bounded by the literal geometric area $\pi L_B^2$.

This is the key correction to the earlier $\beta_B^5$ geometric-aperture argument.

---

## 4. Receiver bath decomposition

The receiver's total spontaneous graviton linewidth

$$
\kappa_{g,B}
$$

is an intrinsic property of the receiver and does **not** depend on the source distance.

The incoming source branch mode occupies only a fraction of the receiver's gravitational bath. Define

$$
\boxed{
\kappa_\Delta(R)
=\eta_{\rm ff}(R)\kappa_{g,B}.
}
$$

The orthogonal gravitational vacuum channels contribute

$$
\kappa_{g,\perp}
=\kappa_{g,B}-\kappa_\Delta.
$$

Hence, with fixed internal damping $\kappa_i$ and any other fixed passive ports,

$$
\boxed{
\kappa_{\rm tot}
=\kappa_{g,B}+\kappa_i+\cdots
}
$$

is distance independent.

Vacuum gravitational ports broaden the receiver but do not contribute thermal occupation to

$$
\Gamma_{\rm th}
=\sum_a\bar n_a\kappa_a
$$

when their occupation is zero.

---

## 5. Exact finite-cat NPT condition

For a stationary thermal receiver, the exact binary-coherent Gaussian theorem gives the capability condition

$$
\boxed{
\kappa_\Delta(R)>\Gamma_{\rm th}.
}
$$

Using the far-zone propagation efficiency,

$$
\frac{25\mathcal O}{16(kR)^2}
\kappa_{g,B}
>\Gamma_{\rm th}.
$$

Define the resonant quantum-reception radius

$$
\boxed{
R_Q^{\rm res}
=\frac{5}{4k}
\sqrt{
\frac{\mathcal O\kappa_{g,B}}
{\Gamma_{\rm th}}
}.
}
$$

Then the mathematical NPT front exists iff

$$
\boxed{R<R_Q^{\rm res}.}
$$

At exactly zero thermal injection, $R_Q^{\rm res}\to\infty$ as expected for a pure-loss channel: entanglement survives at arbitrarily small nonzero transmissivity, although its magnitude vanishes with distance.

---

## 6. Exact waveform-optimal spacetime front

For any normalized incoming temporal difference-mode waveform,

$$
\tau_f(t)
\le
\frac{\kappa_\Delta(R)}{\kappa_{\rm tot}}
\left(1-e^{-\kappa_{\rm tot}(t-R/c)}\right).
$$

The time-reversed receiver ringdown saturates this ceiling.

Using

$$
\frac{\Gamma_{\rm th}}
{\kappa_\Delta(R)}
=\left(\frac{R}{R_Q^{\rm res}}\right)^2,
$$

the exact optimal finite-cat NPT front is

$$
\boxed{
T_{\rm NPT}^{\min}(R)
=
\frac Rc
-
\frac1{\kappa_{\rm tot}}
\ln\left[
1-\left(\frac{R}{R_Q^{\rm res}}\right)^2
\right],
\qquad
R<R_Q^{\rm res}.
}
$$

No NPT front exists for

$$
R\ge R_Q^{\rm res}
$$

within the stationary thermal model.

This corrects the earlier geometric-cone denominator: the intrinsic receiver linewidth is fixed rather than decaying with source-mode overlap.

---

## 7. Front asymptotics

### Well inside the quantum range

For

$$
R\ll R_Q^{\rm res}
$$

while remaining in the wave zone,

$$
-\ln(1-x^2)\simeq x^2,
$$

so

$$
\boxed{
T_{\rm NPT}^{\min}-R/c
\simeq
\frac1{\kappa_{\rm tot}}
\left(\frac{R}{R_Q^{\rm res}}\right)^2.
}
$$

Thus the post-light-cone quantum build delay scales as

$$
\boxed{R^2}
$$

for a resonant far-zone receiver.

### Near the thermal quantum range

Let

$$
R=R_Q^{\rm res}(1-\epsilon),
\qquad
0<\epsilon\ll1.
$$

Then

$$
\boxed{
T_{\rm NPT}^{\min}-R/c
\simeq
\frac1{\kappa_{\rm tot}}
\ln\frac1{2\epsilon}.
}
$$

The NPT front still has a vertical logarithmic asymptote at the finite thermal range.

---

## 8. Wave-zone existence condition

Demand

$$
kR\ge\zeta
$$

for some chosen wave-zone criterion $\zeta\gtrsim1$.

A nonempty resonant wave-zone NPT interval requires

$$
kR_Q^{\rm res}>\zeta.
$$

Therefore

$$
\boxed{
\frac{25\mathcal O}{16}
\frac{\kappa_{g,B}}
{\Gamma_{\rm th}}
>\zeta^2.
}
$$

Equivalently,

$$
\boxed{
\frac{\kappa_{g,B}}
{\Gamma_{\rm th}}
>
\frac{16}{25\mathcal O}\zeta^2.
}
$$

This is the clean resonant receiver criterion. It contains no additional geometric $\beta_B^2$ unless a physical-aperture limit is imposed separately.

---

## 9. Combine with passive nonrelativistic oscillator-strength ceiling

For one dominant thermal internal bath,

$$
\Gamma_{\rm th}
=\bar n_B\frac{\omega_B}{Q_B}.
$$

The passive nonrelativistic sum-rule ceiling gives

$$
\frac{\kappa_{g,B}}
{\Gamma_{\rm th}}
\le
\frac23
\frac{Q_B\mathcal C_B\beta_B^3}
{\bar n_B}.
$$

Therefore a necessary condition for a passive nonrelativistic **resonant** wave-zone receiver is

$$
\boxed{
\frac{25\mathcal O}{24}
\frac{Q_B\mathcal C_B\beta_B^3}
{\bar n_B}
>\zeta^2.
}
$$

This replaces the earlier $\beta_B^5$ condition for resonant reception.

The difficulty remains severe because

$$
\mathcal C_B\ll1,
\qquad
\beta_B\ll1
$$

for ordinary material systems, but the additional geometric $\beta_B^2$ suppression is not fundamental.

---

## 10. Finite-strength certification cone

The exact three-element witness margin is

$$
\Lambda
=\frac{N_\Delta}{m}(\tau-m).
$$

For stationary receiver noise, requiring

$$
\Lambda\ge\Lambda_{\rm req}>0
$$

is equivalent to replacing

$$
\Gamma_{\rm th}
\rightarrow
\Gamma_{\rm th}
\left(1+\frac{\Lambda_{\rm req}}{N_\Delta}\right).
$$

Therefore

$$
\boxed{
R_\Lambda^{\rm res}
=
\frac{R_Q^{\rm res}}
{\sqrt{1+\Lambda_{\rm req}/N_\Delta}}.
}
$$

The finite-certification front is

$$
\boxed{
T_\Lambda^{\min}(R)
=
\frac Rc-
\frac1{\kappa_{\rm tot}}
\ln\left[
1-\left(\frac{R}{R_\Lambda^{\rm res}}\right)^2
\right],
\qquad
R<R_\Lambda^{\rm res}.
}
$$

---

## 11. Relation to the geometric-cap model

Two different receiver architectures should now be kept separate.

### Resonant compact receiver

$$
\eta_{\rm ff}\sim(kR)^{-2}.
$$

Its effective cross-section is of order wavelength squared and its front is described by this note.

### Literal enclosing/absorbing cap

$$
\eta_{\rm cap}\sim(a_R/R)^2.
$$

Its capture is determined by physical angular coverage around the source and is described by `FINITE_APERTURE_WAVEZONE_FRONT.md`.

The cap model is useful as an ideal geometric receiver; it should not be used as a universal bound on resonant matter.

---

## 12. Strongest next step

Independently derive the far-zone coefficient $25/16$ from a common-bath / Green-tensor master equation or from the gravitational resonant absorption cross-section. That will verify the cascaded-channel normalization and separate the coherent exchange and collective-damping pieces of the complex retarded kernel.
