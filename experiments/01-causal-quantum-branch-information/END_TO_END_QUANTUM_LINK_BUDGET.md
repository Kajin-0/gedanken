# End-to-End Quantum Link Budget

**Date:** 2026-08-08  
**Status:** **CANONICAL FACTORIZATION — RECOMMENDED QUANTITATIVE CENTERPIECE FOR THE GRAVITY MANUSCRIPT**

## 1. Why this is the right organizing equation

The repository has accumulated several source waveforms and receiver formulas:

- passive exponential emission;
- finite local-encoder precursor + exponential tail;
- actively shaped \(\sin^4\) pulses;
- target-time-optimized rising exponentials.

The individual waveform coefficients are useful, but none is the fundamental quantity.

The physically invariant structure is the serial link

$$
\boxed{
\text{source branch information}
\to
\text{gravitational source port}
\to
\text{free-space source mode}
\to
\text{receiver gravitational port}
\to
\text{receiver memory}.
}
$$

In the vacuum-source, linear one-way Markov model, every stage factors cleanly.

The result is

$$
\boxed{
\tau_{A\to B}(t)
=
\beta_{g,A}
\eta_{\rm store}(R)
\beta_{g,B}
\mathcal T_f(t).}
$$

This should replace the special \(4e^{-2}\) passive coefficient as the manuscript's main link-budget equation.

---

# 2. Source gravitational branching

Let the source total linewidth be

$$
\kappa_A
=\kappa_{g,A}+\kappa_{\ell,A}.
$$

For vacuum nongravitational loss ports, the fraction of the source-mode branch amplitude power reaching gravity is

$$
\boxed{
\beta_{g,A}
\equiv
\frac{\kappa_{g,A}}{\kappa_A}.}
$$

Equivalently, tracing the other source ports produces a pure-loss channel

$$
\mathcal L_{\beta_{g,A}}
$$

from the virtual source branch mode to the normalized outgoing gravitational mode.

For a controlled source pulse, the same factor appears from the exact branch-distance partition

$$
\frac{N_{\Delta,g}}
{N_{\Delta,{\rm total}}}
=\beta_{g,A}.
$$

Thus the source branching factor is independent of waveform shape.

---

# 3. Free-space source-mode storage

For the aligned plus-quadrupole compact-source wave-zone geometry,

$$
\boxed{
\eta_{\rm store}(R)
=\frac{25\mathcal O}{16(kR)^2},
}
$$

where

$$
0\le\mathcal O\le1
$$

contains normalized tensor, polarization, spatial, and any residual mode-overlap factors not already absorbed into the chosen travelling source mode.

This coefficient should be presented as a normalized source→receiver interface consistent with standard directivity and critical-coupling absorption physics, not as a new universal absorption cross section.

---

# 4. Receiver gravitational branching

Let the receiver intrinsic total gravitational linewidth be

$$
\kappa_{g,B}
$$

and its total linewidth be

$$
\kappa_B.
$$

Define

$$
\boxed{
\beta_{g,B}
\equiv
\frac{\kappa_{g,B}}{\kappa_B}.}
$$

The useful source-mode loading rate is

$$
\boxed{
\kappa_\Delta
=\eta_{\rm store}\kappa_{g,B}
=\eta_{\rm store}\beta_{g,B}\kappa_B.}
$$

This separates

- total matter-gravity coupling of the receiver;
- normalized overlap with the particular incoming source mode;
- total receiver damping.

---

# 5. Dimensionless temporal loading factor

For a normalized incident gravitational waveform

$$
\int_0^\infty|f(s)|^2ds=1,
$$

define

$$
\boxed{
\mathcal T_f(t)
\equiv
\kappa_B
\left|
\int_0^t ds\,
e^{-\kappa_B(t-s)/2}f(s)
\right|^2.}
$$

The ordinary receiver coherent parameter is

$$
\tau_f(t)
=\kappa_\Delta
\left|
\int_0^t ds\,
e^{-\kappa_B(t-s)/2}f(s)
\right|^2.
$$

Using

$$
\kappa_\Delta
=\eta_{\rm store}\beta_{g,B}\kappa_B,
$$

we obtain

$$
\boxed{
\tau_f(t)
=\eta_{\rm store}\beta_{g,B}\mathcal T_f(t).}
$$

Cauchy–Schwarz gives

$$
\boxed{
0\le\mathcal T_f(t)
\le1-e^{-\kappa_Bt}
\le1.}
$$

Thus

$$
\mathcal T_f
$$

contains **all pure temporal waveform matching** and nothing else.

---

# 6. Exact vacuum-source link factorization

Compose the source pure-loss stage with the receiver:

$$
\boxed{
\tau_{A\to B}(t)
=\beta_{g,A}\tau_f(t).}
$$

Therefore

$$
\boxed{
\tau_{A\to B}(t)
=
\beta_{g,A}
\eta_{\rm store}
\beta_{g,B}
\mathcal T_f(t).}
$$

Define the **gravitational quantum link ceiling**

$$
\boxed{
\eta_Q^{\rm link}(R)
\equiv
\beta_{g,A}
\eta_{\rm store}(R)
\beta_{g,B}.}
$$

Then

$$
\boxed{
\tau_{A\to B}(t)
=\eta_Q^{\rm link}(R)\mathcal T_f(t),
\qquad
0\le\mathcal T_f(t)\le1.}
$$

The absolute coherent-transfer ceiling of the architecture is therefore

$$
\boxed{
\tau_{A\to B}(t)
\le
\eta_Q^{\rm link}(R).}
$$

This is the cleanest link-budget statement in the repository.

---

# 7. Where every previously derived waveform fits

## Matched passive exponential

For

$$
\kappa_A=\kappa_B
$$

and a passive exponential source,

$$
\boxed{
\mathcal T_{\exp}^{\max}
=4e^{-2}
\simeq0.541341.}
$$

Thus

$$
\boxed{
\tau_{A\to B}^{\max}
=4e^{-2}\eta_Q^{\rm link}.}
$$

This is a special temporal penalty, not the fundamental link ceiling.

## Full finite-\(g\) local encoder + passive tail

For the matched local encoder model,

$$
\boxed{
\mathcal T_{\rm full}^{\max}
=
4e^{-2}
\exp\left[
\epsilon e^{-y/4}
-\frac y2
+\frac{\epsilon^2}{2}
\right],}
$$

with

$$
\epsilon=\kappa/g,
\qquad
y=\kappa T_*.
$$

For

$$
\epsilon\ll1,
$$

$$
\boxed{
\mathcal T_{\rm full}^{\max}
=4e^{-2}
\left[
1+\left(1-\frac\pi4\right)\frac\kappa g
+O((\kappa/g)^2)
\right].}
$$

## \(\sin^4\) active source pulse

For the fixed mechanically smooth \(\sin^4\) pulse, the optimized vacuum temporal loading factor is

$$
\boxed{
\mathcal T_{\sin^4}^{\max}
=S_{4,*}
\simeq0.7980213.}
$$

Thus

$$
\boxed{
\tau_{A\to B}^{\max}
\simeq0.7980213\,
\eta_Q^{\rm link}.}
$$

provided the source branching stage appropriate to that controlled source is included.

## Target-time-optimized coherent shaping

The Cauchy-saturating rising exponential gives

$$
\boxed{
\mathcal T_{\rm opt}(t)
=1-e^{-\kappa_Bt}.}
$$

Hence

$$
\boxed{
\mathcal T_{\rm opt}(t)\to1
}
$$

as the target time becomes long compared with the receiver lifetime.

This saturates, but never exceeds, the link ceiling

$$
\eta_Q^{\rm link}.
$$

---

# 8. Why waveform engineering is secondary

The available temporal coefficients are all order unity:

$$
0.5413
\quad\text{(matched passive exponential)},
$$

$$
0.7980
\quad\text{(optimized \(\sin^4\) pulse)},
$$

$$
1
\quad\text{(ideal target-time matched envelope)}.
$$

Therefore, once the physical branch fractions are fixed, waveform engineering can improve the absolute transmissivity by at most an order-unity factor.

The severe suppressions reside in

$$
\boxed{
\beta_{g,A},
\qquad
\eta_{\rm store},
\qquad
\beta_{g,B}.}
$$

This is the principal physical lesson of the end-to-end analysis.

---

# 9. Thermal source extension as a quantum-excess budget

Let the source-to-gravitational-mode stage have Gaussian parameters

$$
\Phi_A=\Phi_{\beta_{g,A},m_A}.
$$

Pure free-space propagation adds no occupation in the ideal vacuum model.

The receiver coherent parameter after propagation is

$$
\boxed{
\tau_{G\to B}(t)
=\eta_{\rm store}\beta_{g,B}\mathcal T_f(t).}
$$

Gaussian channel composition gives

$$
\boxed{
\tau_{A\to B}(t)
=\beta_{g,A}
\eta_{\rm store}
\beta_{g,B}
\mathcal T_f(t),}
$$

and

$$
\boxed{
m_{A\to B}(t)
=m_B(t)
+\eta_{\rm store}\beta_{g,B}
\mathcal T_f(t)m_A.}
$$

Therefore the complete channel is non-entanglement-breaking iff

$$
\boxed{
\eta_{\rm store}\beta_{g,B}\mathcal T_f(t)
[\beta_{g,A}-m_A]
>m_B(t).}
$$

Define the source quantum excess

$$
\boxed{
\Delta_A
\equiv
\beta_{g,A}-m_A.}
$$

Then

$$
\boxed{
\eta_{\rm store}\beta_{g,B}\mathcal T_f(t)
\Delta_A
>m_B(t).}
$$

For the passive thermal source model,

$$
m_A
=\beta_{g,A}
\frac{\Gamma_{{\rm th},A}}{\kappa_A},
$$

so

$$
\boxed{
\Delta_A
=\beta_{g,A}
\left(1-rac{\Gamma_{{\rm th},A}}{\kappa_A}\right).}
$$

The finite local encoder adds the controlled correction already bounded in

`ENCODER_THERMAL_NOISE_BOUND.md`.

---

# 10. Receiver thermal noise

The receiver occupation is

$$
\boxed{
m_B(t)
=n_0e^{-\kappa_Bt}
+\frac{\Gamma_{{\rm th},B}}{\kappa_B}
(1-e^{-\kappa_Bt}).}
$$

Thus the full source-resolved non-EB criterion is a literal link budget:

$$
\boxed{
\text{source quantum excess}
\times
\text{propagation overlap}
\times
\text{receiver branching}
\times
\text{temporal loading}
>
\text{receiver noise}.}
$$

No single waveform coefficient should obscure this structure.

---

# 11. Aggressive benchmark under the link-budget view

For the historical benchmark

$$
M_e=4\,\mathrm{kg},
\quad
L=1\,\mathrm m,
\quad
f=1\,\mathrm{MHz},
\quad
Q=10^{12},
\quad
kR=10,
\quad
\mathcal O=1,
$$

the explicit V5 source/receiver mode has

$$
\boxed{
\beta_g
\simeq1.09386\times10^{-20}.}
$$

Also

$$
\boxed{
\eta_{\rm store}=1.5625\times10^{-2}.}
$$

If both source and receiver have this ordinary branching fraction,

$$
\boxed{
\eta_Q^{\rm link}
=\eta_{\rm store}\beta_g^2
\simeq1.87\times10^{-42}.}
$$

The matched passive exponential gives

$$
\boxed{
\tau_{\rm pass}^{\max}
=4e^{-2}\eta_Q^{\rm link}
\simeq1.01\times10^{-42}.}
$$

The optimized \(\sin^4\) temporal factor would give approximately

$$
\boxed{
\tau_{\sin^4}^{\max}
\simeq1.49\times10^{-42}.}
$$

An ideal target-time waveform cannot exceed

$$
\boxed{
1.87\times10^{-42}.}
$$

Thus no temporal waveform can repair the ordinary two-ended branching weakness.

---

# 12. Why the old \(10^{-22}\) number was not wrong

The old optimized receiver-local calculation found a scale around

$$
10^{-22}.
$$

That calculation began with a **normalized incoming gravitational wavepacket**.

In link-budget language it evaluated approximately

$$
\eta_{\rm store}\beta_{g,B}\mathcal T_f,
$$

without a mechanical source branching stage.

For the benchmark,

$$
\eta_{\rm store}\beta_{g,B}
\sim10^{-22}.
$$

The end-to-end mechanical source calculation simply multiplies by the missing

$$
\beta_{g,A}\sim10^{-20},
$$

producing the

$$
10^{-42}
$$

scale.

The distinction is operational, not algebraic.

---

# 13. Ideal source versus ordinary receiver

Suppose a special coherently controlled source achieves

$$
\beta_{g,A}\simeq1
$$

while the ordinary receiver remains at

$$
\beta_{g,B}\simeq1.09\times10^{-20}.
$$

Then

$$
\boxed{
\eta_Q^{\rm link}
\simeq
\eta_{\rm store}\beta_{g,B}
\simeq1.71\times10^{-22}.}
$$

This recovers the old receiver-local scale because the source branch penalty has genuinely been removed, not because of better temporal matching alone.

Conversely, if both devices had gravitational branching near unity,

$$
\eta_Q^{\rm link}
\simeq\eta_{\rm store}.
$$

The problem would then be mode capture and timescale rather than weak matter-gravity branching.

---

# 14. Passive-class insertion

For a passive nonrelativistic receiver,

$$
\beta_{g,B}
\lesssim
\min\left[
1,
\frac23Q_B\mathcal C_B\beta_B^3
\right].
$$

Therefore

$$
\boxed{
\eta_Q^{\rm link}
\lesssim
\beta_{g,A}
\frac{25\mathcal O}{16(kR)^2}
\min\left[
1,
\frac23Q_B\mathcal C_B\beta_B^3
\right].}
$$

If both ends are in the passive nonrelativistic class,

$$
\boxed{
\eta_Q^{\rm link}
\lesssim
\frac{25\mathcal O}{16(kR)^2}
\prod_{j=A,B}
\min\left[
1,
\frac23Q_j\mathcal C_j\beta_j^3
\right].}
$$

The temporal factor remains bounded by one on top of this.

---

# 15. Active collective receiver insertion

If a collective receiver enhances all gravitational rates by a factor

$$
F
$$

while internal loss stays fixed, its useful branching becomes

$$
\boxed{
\beta_{\rm useful}(F)
=\beta_{\rm mode}
\frac{F\kappa_{g,0}}
{F\kappa_{g,0}+\kappa_i}.}
$$

The link budget simply replaces

$$
\eta_{\rm store}\beta_{g,B}
$$

by the correctly normalized useful receiver branching.

As

$$
F\to\infty,
$$

this saturates at

$$
\beta_{\rm mode},
$$

not unity unless the receiver is also perfectly mode matched.

Thus the same link-budget architecture survives the active collective extension.

---

# 16. Recommended manuscript notation

The main text should define four dimensionless factors once:

$$
\boxed{
\beta_A\equiv\beta_{g,A},
\qquad
\eta_R\equiv\eta_{\rm store},
\qquad
\beta_B\equiv\beta_{g,B},
\qquad
\mathcal T(t)\equiv\mathcal T_f(t).}
$$

Then write

$$
\boxed{
\tau(t)=\beta_A\eta_R\beta_B\mathcal T(t).}
$$

If notation conflicts with the mechanical

$$
\beta=\omega L/c,
$$

keep the more explicit symbols

$$
\beta_{g,A},\eta_{\rm store},\beta_{g,B},\mathcal T_f.
$$

Do not use \(\beta_A\) for both branching and internal velocity in the same manuscript.

---

# 17. Strongest conceptual statement

> **The end-to-end gravitational quantum link is not weak because one pulse shape happens to be inefficient. It is weak because a source excitation must first choose gravity over every other source channel, the emitted gravitational mode must overlap the receiver, and the receiver must choose gravity over every other receiver channel. Temporal mode shaping only determines how efficiently the already-selected travelling mode is loaded into the memory.**

Mathematically,

$$
\boxed{
\tau_{A\to B}(t)
=
\underbrace{\beta_{g,A}}_{\text{source branching}}
\underbrace{\eta_{\rm store}}_{\text{free-space mode capture}}
\underbrace{\beta_{g,B}}_{\text{receiver branching}}
\underbrace{\mathcal T_f(t)}_{\text{temporal loading}}.
}
$$

This is the recommended quantitative center of the gravity paper.
