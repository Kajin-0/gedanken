# Weak-Link Absolute Witness Gap

**Timestamp:** 2026-08-07 20:04 EDT  
**Status:** Leading-order analytic optimization of the absolute three-element witness in the weak-link regime. This is the practically relevant limit for gravitational reception.

## 1. Goal

The exact absolute witness gap is

$$
G(v)
=\frac12
\max\left\{
0,
\sqrt{(p_0-p_v)^2+4|z_v|^2}
-(p_0+p_v)
\right\}.
$$

We now optimize it analytically when the receiver channel is very weak:

$$
\tau\ll1,
\qquad
m\ll1,
$$

while the ratio

$$
r=m/\tau
$$

is held fixed with

$$
0\le r<1.
$$

This is the regime in which the channel is only slightly above a replacer channel but remains non-entanglement-breaking.

---

## 2. Correct source-cat scaling

Take the symmetric binary coherent source branches

$$
|\pm a\rangle.
$$

The absolute-gap optimum does **not** use a fixed finite cat as $\tau\to0$.

Write

$$
\boxed{
a=A\sqrt\tau.}
$$

Let the coherent analysis displacement remain finite,

$$
\boxed{v=V=O(1).}
$$

This scaling is confirmed by direct numerical optimization and follows analytically from the first nonzero perturbation of the partial-transpose principal minor.

---

## 3. Expand the normalized determinant ratio

The exact principal-minor ratio obeys

$$
\ln R(v)
=-4a^2-v^2
+\frac{4\tau a^2+4\sqrt\tau av+v^2}{m+1}.
$$

Set

$$
m=r\tau,
$$

$$
a=A\sqrt\tau,
$$

$$
v=V.
$$

To first order in $\tau$,

$$
\boxed{
\ln R
=\tau
\left[
-4A^2+4AV-rV^2
\right]
+O(\tau^2).
}
$$

Define

$$
L(A,V;r)
=-4A^2+4AV-rV^2.
$$

For fixed $V$, $L$ is maximized at

$$
\boxed{A=V/2,}
$$

for which

$$
\boxed{
L_{\max}(V;r)
=(1-r)V^2.
}
$$

Thus the source-cat amplitude that maximizes the **absolute** witness scales as

$$
\boxed{
a\simeq\frac{V}{2}\sqrt\tau.}
$$

This is parametrically smaller than a fixed finite cat.

---

## 4. First-order negative eigenvalue

At zeroth order in $\tau$,

$$
p_0^{(0)}=\frac12,
$$

$$
p_v^{(0)}=\frac12e^{-V^2},
$$

$$
|z_v^{(0)}|^2
=\frac14e^{-V^2}.
$$

The $2\times2$ compression therefore has one zero eigenvalue at zeroth order.

Its determinant is

$$
\det M_v
=p_0p_v(1-R).
$$

Using

$$
R=1+\tau L+O(\tau^2),
$$

$$
\det M_v
=-\frac14e^{-V^2}\tau L
+O(\tau^2).
$$

The positive zeroth-order eigenvalue is

$$
\lambda_+^{(0)}
=\frac12(1+e^{-V^2}).
$$

Hence the small negative eigenvalue is

$$
\lambda_-
=\frac{\det M_v}{\lambda_+^{(0)}}
+O(\tau^2).
$$

Therefore

$$
\boxed{
G(V)
=\tau
\frac{e^{-V^2}}
{2(1+e^{-V^2})}
L(A,V;r)
+O(\tau^2).
}
$$

After optimizing $A=V/2$,

$$
\boxed{
G(V)
=\tau(1-r)
\frac{V^2}{2(e^{V^2}+1)}
+O(\tau^2).
}
$$

---

## 5. Exact analytic optimum over the analysis displacement

Let

$$
x=V^2.
$$

We need to maximize

$$
f(x)
=\frac{x}{2(e^x+1)}.
$$

The stationary condition is

$$
(e^x+1)-xe^x=0,
$$

or

$$
(x-1)e^x=1.
$$

Thus

$$
\boxed{
x_*
=1+W(e^{-1}),
}
$$

where $W$ is the principal Lambert function.

Therefore

$$
\boxed{
V_*
=\sqrt{1+W(e^{-1})}
\simeq1.130692.
}
$$

The optimized source-cat amplitude is

$$
\boxed{
a_*
=\frac12
\sqrt{1+W(e^{-1})}
\sqrt\tau
+O(\tau^{3/2}),
}
$$

or numerically

$$
\boxed{
a_*
\simeq0.565346\sqrt\tau.}
$$

---

## 6. Universal weak-link absolute-gap coefficient

Using the stationary-point identity

$$
e^{x_*}=1/W(e^{-1}),
$$

we obtain

$$
\frac{x_*}{2(e^{x_*}+1)}
=\frac12W(e^{-1}).
$$

Hence

$$
\boxed{
G_{\rm abs}^{\rm opt}
=\frac{W(e^{-1})}{2}
\tau(1-r)
+O(\tau^2).
}
$$

But

$$
\tau(1-r)=\tau-m.
$$

Therefore the result simplifies to

$$
\boxed{
G_{\rm abs}^{\rm opt}
=\frac{W(e^{-1})}{2}
(\tau-m)
+O(\tau^2),
}
$$

with

$$
\boxed{
\frac{W(e^{-1})}{2}
\simeq0.1392322714.
}
$$

This is the central result.

---

## 7. Physical interpretation

Near a replacer channel, the **absolute observable negative partial-transpose weight** is controlled not by the relative ratio

$$
\frac{\tau-m}{m},
$$

but by the absolute excess

$$
\boxed{\tau-m.}
$$

The optimized three-element witness captures a universal fraction

$$
\boxed{\simeq13.9\%}
$$

of that small quantum excess at leading order.

Thus the weak gravitational link has a simple operational metric:

$$
\boxed{
\text{measurable NPT weight}
\propto
\text{coherent transfer}
-
\text{classicalizing occupation}.
}
$$

---

## 8. Finite-certification threshold

If an experiment requires an absolute witness gap

$$
G_{\rm abs}^{\rm opt}
\ge G_{\rm req},
$$

then in the weak-link regime

$$
\boxed{
\tau-m
\gtrsim
\frac{2G_{\rm req}}
{W(e^{-1})}.
}
$$

Numerically,

$$
\boxed{
\tau-m
\gtrsim
7.18282\,G_{\rm req}.
}
$$

This creates a finite-certification region strictly inside the bare non-EB region

$$
\tau>m.
$$

Unlike the normalized $\Lambda$ threshold, it cannot remain finite while all received probabilities vanish.

---

## 9. Application to a fixed gravitational waveform

For a source-specific receiver channel,

$$
\tau=\tau_f(t,R),
$$

$$
m=m(t).
$$

Therefore

$$
\boxed{
G_{\rm abs}^{\rm opt}(t,R)
\simeq
\frac{W(e^{-1})}{2}
[\tau_f(t,R)-m(t)]_+
}
$$

whenever

$$
\tau_f,m\ll1.
$$

Here

$$
[x]_+=\max(x,0).
$$

This is especially appropriate for gravity because all useful transfer probabilities are expected to be extremely small for ordinary receivers.

---

## 10. Smooth finite pulse

For the smooth $\sin^2$ source in `SMOOTH_SIN2_SOURCE_QUANTUM_WINDOW.md`,

$$
\tau_f(t,R)
=\frac{8\kappa_\Delta(R)}{3T}
e^{-\kappa t}
I^2[\min(t,T)],
$$

and for an initially ground-state receiver,

$$
m(t)
=\frac{\Gamma_{\rm th}}{\kappa}(1-e^{-\kappa t}).
$$

Hence the leading absolute witness bubble is simply

$$
\boxed{
G_{\rm abs}^{\rm opt}(t,R)
\simeq
\frac{W(e^{-1})}{2}
\left[
\frac{8\kappa_\Delta(R)}{3T}
e^{-\kappa t}
I^2[\min(t,T)]
-
\frac{\Gamma_{\rm th}}{\kappa}(1-e^{-\kappa t})
\right]_+.
}
$$

This turns the mathematical EB/non-EB bubble directly into an absolute finite-strength prediction.

---

## 11. Relation to exact full negativity

This is a rigorous lower bound obtained from one $2\times2$ partial-transpose compression.

It need not equal the full optimized negativity.

For pure loss, the full binary-cat negativity can be larger and has a different optimal cat scaling:

$$
N_\Delta^{\rm opt}
\sim4\sqrt\tau.
$$

The present result should therefore be interpreted as

> **the analytically optimized strength of the minimal three-element witness**, not a universal equality for total entanglement.

That distinction is important.

---

## 12. Strongest next step

Use the absolute-gap expression to derive a finite-certification spacetime radius/time for the optimized smooth source pulse for a specified $G_{\rm req}$, and compare it with the bare EB/non-EB bubble.