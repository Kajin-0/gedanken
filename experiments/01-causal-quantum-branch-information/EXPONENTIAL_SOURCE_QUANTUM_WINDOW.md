# Exponential Source Quantum-Capability Window

**Timestamp:** 2026-08-07 20:08 EDT  
**Status:** Source-specific analytic benchmark replacing the earlier universal-logarithmic-front picture. The result is exact within the narrowband exponential-wavepacket + Markov receiver model.

## 1. Why use a fixed source pulse

A real gravitational source emits one physical waveform. It does not re-optimize the incoming temporal mode separately for every possible receiver observation time.

To obtain a source-specific causal prediction, choose the simplest analytically soluble narrowband causal branch-difference wavepacket:

$$
\boxed{
f_S(t)
=\sqrt{\Gamma_S}
e^{-\Gamma_St/2}\Theta(t),
}
$$

with

$$
\int_0^\infty dt\,|f_S(t)|^2=1.
$$

In the narrowband regime

$$
\Gamma_S\ll\omega_0,
$$

this temporal graviton mode is produced approximately by a branch quadrupole history whose positive-frequency component has an exponentially decaying envelope,

$$
\Delta Q_{ij}^{(+)}(t)
\propto
q_{ij}e^{-i\omega_0t}e^{-\Gamma_St/2}\Theta(t).
$$

The exact graviton spectrum carries an additional $\omega^{5/2}$ weighting, but over a narrow bandwidth this is effectively constant, so the normalized emitted graviton temporal envelope follows the quadrupole envelope.

---

## 2. Receiver response

Let the receiver have total linewidth

$$
\kappa
$$

and useful coupling rate to the arriving source mode

$$
\kappa_\Delta(R).
$$

After the retarded arrival time $R/c$, define local receiver time

$$
t\equiv T-R/c\ge0.
$$

The stored source-mode amplitude is

$$
A(t)
=\sqrt{\kappa_\Delta}
\int_0^t ds\,
e^{-\kappa(t-s)/2}f_S(s).
$$

For $\Gamma_S\neq\kappa$,

$$
\boxed{
A(t)
=
\frac{2\sqrt{\kappa_\Delta\Gamma_S}}
{\kappa-\Gamma_S}
\left(
e^{-\Gamma_St/2}
-e^{-\kappa t/2}
\right).
}
$$

Therefore

$$
\boxed{
\tau(t)
=
\frac{4\kappa_\Delta\Gamma_S}
{(\kappa-\Gamma_S)^2}
\left(
e^{-\Gamma_St/2}
-e^{-\kappa t/2}
\right)^2.
}
$$

This is the exact coherent source-mode transmission into the receiver for the fixed exponential pulse.

---

## 3. Bandwidth-matched case

The cleanest benchmark is

$$
\boxed{
\Gamma_S=\kappa.
}
$$

Taking the limit gives

$$
\boxed{
A(t)
=\sqrt{\kappa_\Delta\kappa}\,
t\,e^{-\kappa t/2},
}
$$

and hence

$$
\boxed{
\tau(t)
=\frac{\kappa_\Delta}{\kappa}
x^2e^{-x},
\qquad
x\equiv\kappa t.
}
$$

The transfer probability begins quadratically,

$$
\tau(t)
\simeq
\kappa_\Delta\kappa t^2,
$$

reaches a maximum at

$$
x=2,
$$

and then decays as the finite source wavepacket passes and the receiver re-emits/loses its stored amplitude.

The maximum is

$$
\boxed{
\tau_{\max}
=\frac{4}{e^2}
\frac{\kappa_\Delta}{\kappa}
\simeq0.5413
\frac{\kappa_\Delta}{\kappa}.
}
$$

A decaying exponential is not the time reverse of the receiver ringdown, so it cannot achieve unit loading even when the source mode occupies the receiver's entire useful port.

---

## 4. Ground-state receiver with a stationary thermal bath

Prepare the receiver initially in its ground state,

$$
n_0=0.
$$

Let occupied bath channels inject thermal quanta at rate

$$
\Gamma_{\rm th}.
$$

The receiver vacuum-output occupation is

$$
\boxed{
m(t)
=\frac{\Gamma_{\rm th}}{\kappa}
(1-e^{-x}).
}
$$

The binary coherent theorem says the source-to-receiver channel is non-entanglement-breaking exactly when

$$
\tau(t)>m(t).
$$

Substituting the matched exponential pulse gives

$$
\frac{\kappa_\Delta}{\kappa}
x^2e^{-x}
>
\frac{\Gamma_{\rm th}}{\kappa}
(1-e^{-x}).
$$

Equivalently,

$$
\boxed{
h(x)
\equiv
\frac{x^2}{e^x-1}
>
r,
}
$$

where

$$
\boxed{
r
\equiv
\frac{\Gamma_{\rm th}}
{\kappa_\Delta}.
}
$$

This one dimensionless function determines the complete source-specific EB dynamics.

---

## 5. The channel has a finite quantum-capability window

The function

$$
h(x)=\frac{x^2}{e^x-1}
$$

obeys

$$
h(0)=0,
\qquad
h(\infty)=0,
$$

and has one positive maximum.

The stationary point satisfies

$$
2(e^x-1)=xe^x,
$$

or

$$
(2-x)e^x=2.
$$

Thus

$$
\boxed{
x_*
=2+W_0(-2e^{-2})
\simeq1.59362.
}
$$

Using the stationary-point identity,

$$
\boxed{
h_*
=h(x_*)
=x_*(2-x_*)
\simeq0.647610.
}
$$

Therefore a non-EB interval exists iff

$$
\boxed{
r<h_*,
}
$$

or

$$
\boxed{
\kappa_\Delta
>
\frac{1}{h_*}\Gamma_{\rm th}
\simeq1.54414\,\Gamma_{\rm th}.
}
$$

This source-specific threshold is stricter than the protocol-optimized envelope condition

$$
\kappa_\Delta>\Gamma_{\rm th}.
$$

---

## 6. Birth and death times

For

$$
0<r<h_*,
$$

the equation

$$
h(x)=r
$$

has two positive roots,

$$
\boxed{x_-(r)<x_*<x_+(r).}
$$

The gravitational receiver channel evolves as

$$
\boxed{
\mathrm{EB}
\quad\xrightarrow{x_-}\quad
\mathrm{non\!\!-EB}
\quad\xrightarrow{x_+}\quad
\mathrm{EB}.
}
$$

The spacetime boundaries are

$$
\boxed{
T_-(R)
=\frac Rc+
\frac{x_-[r(R)]}{\kappa},
}
$$

and

$$
\boxed{
T_+(R)
=\frac Rc+
\frac{x_+[r(R)]}{\kappa}.
}
$$

Thus one finite source pulse produces a **quantum-capability bubble/window** inside the ordinary future light cone rather than a permanently open quantum cone.

This is physically natural: the receiver is initially too noisy relative to the tiny accumulated signal; then the coherent pulse dominates; finally the pulse passes while environmental thermalization persists.

---

## 7. Insert the gravitational free-space coupling

For the aligned plus-quadrupole wave-zone link derived in Experiment 01,

$$
\boxed{
\kappa_\Delta(R)
=
\frac{25\mathcal O}{16(kR)^2}
\kappa_g,
}
$$

where

- $\kappa_g$ is the receiver's intrinsic graviton linewidth;
- $\mathcal O\le1$ is the remaining tensor/polarization/spatial mode overlap;
- $k=\omega_0/c$.

Therefore

$$
\boxed{
r(R)
=
\frac{16(kR)^2\Gamma_{\rm th}}
{25\mathcal O\kappa_g}.
}
$$

Define the earlier protocol-envelope radius

$$
R_{\rm env}
=\frac5{4k}
\sqrt{
\frac{\mathcal O\kappa_g}
{\Gamma_{\rm th}}
}.
$$

Then simply

$$
\boxed{
r(R)
=\left(
\frac{R}{R_{\rm env}}
\right)^2.
}
$$

---

## 8. Fixed-pulse maximum quantum range

The exponential source has a non-EB window only if

$$
r(R)<h_*.
$$

Hence

$$
\boxed{
R<R_{\rm exp},
}
$$

where

$$
\boxed{
R_{\rm exp}
=\sqrt{h_*}\,R_{\rm env}
\simeq0.804742\,R_{\rm env}.
}
$$

Explicitly,

$$
\boxed{
R_{\rm exp}
=
\frac5{4k}
\sqrt{
\frac{h_*\mathcal O\kappa_g}
{\Gamma_{\rm th}}
}.
}
$$

The finite pulse therefore reduces the maximum quantum reception distance relative to the unconstrained protocol-optimized temporal envelope.

---

## 9. Critical behavior is no longer logarithmic

As

$$
R\to R_{\rm exp}^{-},
$$

the two roots approach

$$
x_*,
$$

so the non-EB time window **shrinks to zero width at a finite post-arrival time**,

$$
\boxed{
T_*-R/c
=\frac{x_*}{\kappa}
\simeq
\frac{1.59362}{\kappa}.
}
$$

There is no logarithmic divergence.

Near the maximum, expand

$$
h(x)
=h_*
+\frac12h''(x_*)(x-x_*)^2+\cdots.
$$

Therefore

$$
\boxed{
|x_\pm-x_*|
\propto
\sqrt{h_*-r}.
}
$$

The birth and death fronts merge with square-root scaling.

This is a qualitatively different critical structure from the earlier stationary-receiver/protocol-envelope logarithm.

---

## 10. Stationary initial receiver gives a different fixed-pulse condition

If instead the receiver begins in its stationary thermal state,

$$
n_0
=\Gamma_{\rm th}/\kappa,
$$

then

$$
m(t)
=\Gamma_{\rm th}/\kappa
$$

is constant.

The matched exponential channel is non-EB when

$$
\frac{\kappa_\Delta}{\kappa}
x^2e^{-x}
>
\frac{\Gamma_{\rm th}}{\kappa},
$$

or

$$
\boxed{
x^2e^{-x}>r.}
$$

Since

$$
\max_{x>0}x^2e^{-x}
=\frac4{e^2}
$$

at $x=2$, the non-EB window exists iff

$$
\boxed{
\kappa_\Delta
>
\frac{e^2}{4}\Gamma_{\rm th}
\simeq1.84726\Gamma_{\rm th}.
}
$$

The fixed source waveform is therefore more demanding than the reoptimized Cauchy–Schwarz envelope for either receiver preparation.

---

## 11. Relation to Toccacelo et al. (2026)

Toccacelo et al.'s open gravitational-wave detector has

$$
\tau(t)
=e^{-\kappa t}\sin^2(\gamma_gt),
$$

$$
m(t)
=(1-e^{-\kappa t})\bar N.
$$

Its non-EB condition is

$$
e^{-\kappa t}\sin^2(\gamma_gt)
>(1-e^{-\kappa t})\bar N.
$$

That model exhibits the same qualitative finite-window phenomenon for an already-arrived single GW mode.

The present result differs by deriving the incoming temporal mode from a source-side branch wavepacket and inserting an explicit source-distance-dependent gravitational mode-overlap rate $\kappa_\Delta(R)$.

Thus the relevant candidate contribution is the **source-resolved spacetime window**, not the generic existence of a noisy GW receiver window.

---

## 12. Narrowband quadrupole interpretation

The normalized outgoing graviton spectrum for a source branch difference is proportional to

$$
F(\omega)
\propto
\omega^{5/2}\Delta\widetilde Q_{ij}(\omega).
$$

For

$$
\Delta Q_{ij}^{(+)}(t)
=q_{ij}e^{-i\omega_0t}g(t),
$$

with spectral width

$$
\Delta\omega\ll\omega_0,
$$

$$
\omega^{5/2}
\simeq
\omega_0^{5/2}
$$

throughout the pulse bandwidth. Hence

$$
F(\omega_0+\Omega)
\propto
\widetilde g(\Omega),
$$

so the normalized temporal graviton mode follows $g(t)$ up to narrowband corrections.

This justifies using the exponential $f_S(t)$ as the leading wave-zone branch-difference mode of an exponentially damped coherent quadrupole history.

---

## 13. Physical interpretation

> **A finite gravitational pulse does not permanently turn a distant receiver into a quantum channel. At first, too little of the coherent branch record has arrived. Then a window can open in which the stored branch signal exceeds the receiver's classicalizing thermal record. Finally the pulse passes and the receiver loses that quantum advantage. Distance weakens the useful mode overlap until the two boundaries meet and the quantum window disappears altogether.**

This is a more physical source-specific picture than the earlier universal logarithmic cone.

---

## 14. Strongest next step

The exponential pulse is an analytic benchmark, not yet the most realistic source.

Next:

1. use a **smooth finite conserved quadrupole pulse** with no sharp turn-on;
2. calculate its exact normalized graviton temporal mode from
   $$
   \omega^{5/2}\Delta\widetilde Q_{ij}(\omega);
   $$
3. compute the source-specific non-EB window numerically/analytically;
4. define finite experimental certification using **absolute negativity or absolute witness gap**, because normalized $\Lambda$ can remain finite even when the transmitted state weight tends to zero.

The source-specific window, not a universal logarithmic front, is now the strongest path.