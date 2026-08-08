# Resonant Suppression of the Smooth Release Transient

**Date:** 2026-08-07  
**Status:** **QUANTITATIVE CAUSAL-INTERVENTION RESULT — RELEASE TRANSIENT IS PARAMETRICALLY SMALL IN THE PASSIVE RESONANT BAND**

## 1. Question

`SMOOTH_RELEASE_TO_PASSIVE_SOURCE.md` constructs a finite release from a held static branch state into passive free evolution:

$$
\frac{\delta u(t)}{u_0}
=-\frac{(\omega T_r)^2}{2}x^3(1-x)^2,
\qquad
x=t/T_r.
$$

The release is $C^2$ and ultraviolet finite, but a remaining concern is quantitative:

> Does the short release transient itself dominate the resonant gravitational signal seen by the receiver?

For a high-Q passive source, it does not. The bridge has two exact moment cancellations, and its carrier-frequency overlap is suppressed by

$$
O\!\left(\frac{(\omega T_r)^3}{Q_A}\right)
$$

relative to the passive resonant tail.

---

## 2. Release acceleration

Define

$$
\boxed{r\equiv\omega T_r.}
$$

Let

$$
f(x)=x^3(1-x)^2=x^3-2x^4+x^5.
$$

Then

$$
\delta u(t)
=-\frac{u_0r^2}{2}f(x).
$$

Since

$$
\frac{d^2}{dt^2}
=\frac1{T_r^2}\frac{d^2}{dx^2}
$$

and

$$
\frac{r^2}{T_r^2}=\omega^2,
$$

we obtain

$$
\boxed{
\ddot{\delta u}(t)
=-u_0\omega^2P(x),
}
$$

where

$$
\boxed{
P(x)=3x-12x^2+10x^3.
}
$$

At the release boundaries,

$$
P(0)=0,
$$

$$
P(1)=1,
$$

so the acceleration joins continuously from zero onto the free value

$$
-\omega^2u_0.
$$

---

## 3. Carrier-frequency overlap of the release

The resonant gravitational field amplitude is proportional to the Fourier component of the quadrupole acceleration near the mechanical carrier.

Apart from the constant quadrupole factor, define

$$
\boxed{
J(r)
=\int_0^1dx\,P(x)e^{irx}.
}
$$

Then the release contribution at the carrier has magnitude proportional to

$$
\boxed{
|A_{\rm rel}|
\propto
u_0\omega^2T_r|J(r)|.
}
$$

---

## 4. Two exact moment cancellations

For

$$
P(x)=3x-12x^2+10x^3,
$$

one finds

$$
\boxed{
\int_0^1P(x)dx=0,
}
$$

and

$$
\boxed{
\int_0^1xP(x)dx=0.
}
$$

These are not accidental. They reflect the fact that the release returns to the same

- velocity;
- displacement

at the end of the bridge before the passive tail begins.

More generally,

$$
\boxed{
\int_0^1x^nP(x)dx
=\frac{n(n-1)}{(n+2)(n+3)(n+4)}.
}
$$

Therefore the Taylor series begins at $n=2$:

$$
\boxed{
J(r)
=\sum_{n=2}^{\infty}
\frac{(ir)^n}
{(n-2)!(n+2)(n+3)(n+4)}.
}
$$

Hence

$$
\boxed{
J(r)
=-\frac{r^2}{120}
-i\frac{r^3}{210}
+O(r^4).
}
$$

The release has no $O(1)$ or $O(r)$ carrier overlap.

---

## 5. Closed form

For completeness, with

$$
z=ir,
$$

the integral can be written

$$
\boxed{
J(r)
=
\frac{
 e^z(z^3-9z^2+36z-60)
+3z^2+24z+60
}{z^4}.
}
$$

The apparent singularity at $z=0$ is removable; the moment expansion above is the stable small-$r$ representation.

---

## 6. Passive-tail carrier amplitude

After the release, take the high-Q passive tail

$$
u_{\rm tail}(\tau)
\simeq
u_0e^{-\kappa_A\tau/2}
\cos(\omega\tau),
\qquad
\tau=t-T_r.
$$

Near resonance,

$$
\ddot u_{\rm tail}
\simeq
-\omega^2u_0e^{-\kappa_A\tau/2}
\cos(\omega\tau)
$$

up to relative corrections

$$
O(\kappa_A/\omega).
$$

The resonant Fourier component of the real oscillation is therefore

$$
\boxed{
|A_{\rm tail}|
\propto
\frac{u_0\omega^2}{\kappa_A}
\left[1+O\!\left(\frac{\kappa_A}{\omega}\right)\right].
}
$$

The factor $1/2$ from the positive-frequency component cancels the factor $2/\kappa_A$ from the exponential integral.

---

## 7. Exact scaling of release contamination

Combining the two amplitudes gives

$$
\boxed{
\frac{|A_{\rm rel}|}{|A_{\rm tail}|}
\simeq
\kappa_AT_r|J(r)|
=
\frac{\kappa_A}{\omega}
 r|J(r)|.
}
$$

Define source quality factor

$$
\boxed{Q_A=\omega/\kappa_A.}
$$

Then

$$
\boxed{
\frac{|A_{\rm rel}|}{|A_{\rm tail}|}
\simeq
\frac{r|J(r)|}{Q_A}.
}
$$

For

$$
r\ll1,
$$

$$
\boxed{
\frac{|A_{\rm rel}|}{|A_{\rm tail}|}
=
\frac{r^3}{120Q_A}
\left[1+O(r)\right].
}
$$

Thus the release contamination is suppressed simultaneously by

1. the short release duration relative to one period;
2. the source quality factor.

---

## 8. Rigorous bound for $0\le r\le1$

From the series,

$$
|J(r)|
\le
\sum_{n=2}^{\infty}
\frac{r^n}
{(n-2)!(n+2)(n+3)(n+4)}.
$$

For

$$
n\ge2,
$$

$$
(n+2)(n+3)(n+4)\ge120.
$$

Therefore

$$
|J(r)|
\le
\frac{r^2}{120}
\sum_{k=0}^{\infty}\frac{r^k}{k!}
=
\frac{r^2e^r}{120}.
$$

For

$$
0\le r\le1,
$$

$$
\boxed{
|J(r)|
\le
\frac{e}{120}r^2.
}
$$

Hence

$$
\boxed{
\frac{|A_{\rm rel}|}{|A_{\rm tail}|}
\le
\frac{e}{120}
\frac{r^3}{Q_A}
\simeq
0.02265
\frac{r^3}{Q_A}.
}
$$

This is deliberately conservative.

---

## 9. Numerical scale

For

$$
r=\omega T_r\le1,
$$

the rigorous bound gives

### $Q_A=10^3$

$$
\boxed{
|A_{\rm rel}|/|A_{\rm tail}|
<2.27\times10^{-5}.
}
$$

### $Q_A=10^6$

$$
\boxed{
|A_{\rm rel}|/|A_{\rm tail}|
<2.27\times10^{-8}.
}
$$

### $Q_A=10^9$

$$
\boxed{
|A_{\rm rel}|/|A_{\rm tail}|
<2.27\times10^{-11}.
}
$$

The actual coefficient at $r=1$ is smaller than the bound.

---

## 10. Receiver interpretation

A narrowband receiver centered near $\omega$ responds to the spectral/mode overlap in this carrier band, not to the total broadband graviton number emitted during switching.

Therefore the quantity above is the relevant contamination measure for the passive resonant source→receiver protocol.

The release can still emit broadband radiation. But for

$$
\omega T_r\lesssim1
$$

and

$$
Q_A\gg1,
$$

its projection into the passive resonant channel is parametrically negligible.

---

## 11. Why the suppression is stronger than a simple duration ratio

One might have expected only

$$
|A_{\rm rel}|/|A_{\rm tail}|
\sim
\kappa_AT_r.
$$

The actual bridge is much better because the first two moments vanish:

$$
\int P=0,
\qquad
\int xP=0.
$$

Thus

$$
J(r)=O(r^2),
$$

and the ratio becomes

$$
\boxed{
O\!\left(
\frac{(\omega T_r)^3}{Q_A}
\right).
}
$$

This is a direct benefit of matching both displacement and velocity while switching the acceleration continuously.

---

## 12. Relation to causality

Making the release spectrally negligible does **not** move the causal front.

The signal and control histories begin to differ at the start of the release, so the earliest possible receiver dependence remains

$$
\boxed{R/c}
$$

after that start time.

The small release projection only means that most receiver-band signal arrives in the later passive resonant tail.

---

## 13. Adversarial verdict

For a high-Q passive source, the explicit $C^2$ release bridge can be made both

- ultraviolet finite;
- negligible in the resonant receiver channel.

The controlled regime

$$
\boxed{
\omega T_r\lesssim1,
\qquad
Q_A\gg1
}
$$

gives a rigorous carrier-band contamination bound

$$
\boxed{
|A_{\rm rel}|/|A_{\rm tail}|
\le
0.02265
\frac{(\omega T_r)^3}{Q_A}.
}
$$

Thus the source can be treated operationally as a short local release intervention followed by a dominant autonomous passive emission tail.

---

## 14. Next refinement

A future numerical check may project the full retarded release waveform through the exact finite-bandwidth receiver convolution rather than using the carrier-frequency estimate.

For the high-Q regime, that refinement should differ from the result above only by controlled corrections in

$$
\kappa_A/\omega,
\qquad
\kappa_B/\omega.
$$
