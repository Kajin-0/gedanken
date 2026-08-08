# Smooth Finite Source Quantum-Capability Window

**Timestamp:** 2026-08-07 20:04 EDT  
**Status:** Source-specific analytic benchmark for a smooth finite branch pulse. This is currently a cleaner physical source model than the sharp-onset exponential benchmark.

## 1. Smooth normalized source mode

Choose the normalized temporal branch-difference mode

$$
\boxed{
f_T(t)
=\sqrt{\frac{8}{3T}}
\sin^2\left(\frac{\pi t}{T}\right),
\qquad 0<t<T,
}
$$

and

$$
f_T(t)=0
$$

otherwise.

Normalization follows from

$$
\int_0^Tdt\,
\sin^4\left(\frac{\pi t}{T}\right)
=\frac{3T}{8}.
$$

The pulse satisfies

$$
f_T(0)=f_T(T)=0,
$$

and

$$
\dot f_T(0)=\dot f_T(T)=0.
$$

Thus the branch-wavepacket amplitude and its first derivative switch on and off continuously.

In the narrowband source construction,

$$
\Delta Q_{ij}^{(+)}(t)
\propto
q_{ij}e^{-i\omega_0t}f_T(t),
$$

with

$$
\omega_0T\gg1,
$$

so the normalized outgoing graviton mode follows the same envelope to leading order in $1/(\omega_0T)$.

---

## 2. Receiver convolution

Let the receiver have total linewidth

$$
\kappa
$$

and useful source-mode coupling rate

$$
\kappa_\Delta.
$$

After retarded arrival, the stored coherent amplitude is

$$
A(t)
=\sqrt{\kappa_\Delta}
\int_0^t ds\,
e^{-\kappa(t-s)/2}f_T(s).
$$

Since the source vanishes after $T$, define

$$
u=\min(t,T).
$$

Then

$$
\boxed{
A(t)
=\sqrt{\frac{8\kappa_\Delta}{3T}}
e^{-\kappa t/2}
I(\nu),
}
$$

where

$$
I(u)
=\int_0^u ds\,
e^{\kappa s/2}
\sin^2\left(\frac{\pi s}{T}\right).
$$

---

## 3. Closed form of the pulse integral

Define

$$
\alpha=\kappa/2,
$$

$$
\Omega=2\pi/T.
$$

Using

$$
\sin^2(\pi s/T)
=\frac12[1-\cos(\Omega s)],
$$

we obtain

$$
\boxed{
I(u)
=\frac12
\left[
\frac{e^{\alpha u}-1}{\alpha}
-
\frac{
e^{\alpha u}[\alpha\cos(\Omega u)+\Omega\sin(\Omega u)]-\alpha
}
{\alpha^2+\Omega^2}
\right].
}
$$

Therefore the exact source-mode transmission is

$$
\boxed{
\tau_T(t)
=\frac{8\kappa_\Delta}{3T}
e^{-\kappa t}
I^2[\min(t,T)].
}
$$

For $t>T$, the source has ended and the stored signal simply decays as

$$
\tau_T(t)\propto e^{-\kappa t}.
$$

---

## 4. Ground-state receiver noise

Prepare the receiver initially in its ground state,

$$
n_0=0.
$$

For stationary occupied bath injection

$$
\Gamma_{\rm th},
$$

the vacuum-output occupation is

$$
\boxed{
m(t)
=\frac{\Gamma_{\rm th}}{\kappa}
(1-e^{-\kappa t}).
}
$$

The source-mode $\to$ receiver channel is non-entanglement-breaking iff

$$
\boxed{
\tau_T(t)>m(t).
}
$$

For the binary coherent branch probe, this is simultaneously the exact NPT condition.

---

## 5. Dimensionless form

Define

$$
\boxed{x=t/T,}
$$

$$
\boxed{q=\kappa T.}
$$

Also define

$$
y=\min(x,1).
$$

Let

$$
\boxed{
J_q(y)
=\int_0^y dz\,
e^{qz/2}\sin^2(\pi z).
}
$$

Then

$$
\boxed{
\tau_T(x)
=\frac{8\kappa_\Delta T}{3}
e^{-qx}J_q^2(y).
}
$$

The ratio to thermal occupation is

$$
\boxed{
\frac{\tau_T(x)}{m(x)}
=\frac{\kappa_\Delta}{\Gamma_{\rm th}}
H_q(x),
}
$$

where

$$
\boxed{
H_q(x)
=\frac{8q}{3}
\frac{e^{-qx}J_q^2[\min(x,1)]}
{1-e^{-qx}}.
}
$$

Thus the complete capability problem depends only on

1. source/receiver bandwidth ratio $q$;
2. thermal-to-useful coupling ratio $\Gamma_{\rm th}/\kappa_\Delta$.

---

## 6. Exact capability condition for the smooth pulse

Define

$$
r
=\frac{\Gamma_{\rm th}}{\kappa_\Delta}.
$$

Then

$$
\boxed{
\text{channel non-EB at }x
\iff
H_q(x)>r.
}
$$

Because

$$
H_q(0)=0,
$$

and

$$
H_q(x)\to0
$$

as $x\to\infty$, any non-EB region is a finite time window.

For each $q$, define

$$
\boxed{
H_{\max}(q)
=\max_{x>0}H_q(x).
}
$$

A quantum-capability window exists iff

$$
\boxed{
\frac{\Gamma_{\rm th}}{\kappa_\Delta}
<H_{\max}(q).
}
$$

---

## 7. Optimal receiver bandwidth for this pulse family

Numerical maximization of the closed analytic function $H_q(x)$ gives

$$
\boxed{
q_{\rm opt}
=\kappa T
\simeq3.06881,
}
$$

with the optimum occurring at

$$
\boxed{
x_{\rm opt}
=t_{\rm opt}/T
\simeq0.744147.
}
$$

The maximum dimensionless capability ratio is

$$
\boxed{
H_*
\equiv
\max_{q,x}H_q(x)
\simeq0.838841.
}
$$

Therefore, within this smooth $\sin^2$ pulse family, **no choice of receiver linewidth can generate a non-EB window unless**

$$
\boxed{
\kappa_\Delta
>
\frac{1}{H_*}\Gamma_{\rm th}
\simeq1.19212\,\Gamma_{\rm th}.
}
$$

This is only about $19\%$ more demanding than the unconstrained temporal-mode envelope condition

$$
\kappa_\Delta>\Gamma_{\rm th}.
$$

---

## 8. Comparison with the exponential pulse

For the bandwidth-matched decaying exponential benchmark,

$$
\kappa_\Delta
>1.54414\,\Gamma_{\rm th}
$$

was required for a ground-state receiver.

The smooth finite pulse improves this to

$$
\boxed{
\kappa_\Delta
>1.19212\,\Gamma_{\rm th}
}
$$

after optimizing $\kappa T$.

The reason is temporal mode matching: the symmetric finite pulse distributes more of its energy into the receiver's useful loading interval than an abruptly emitted decaying ringdown does.

It still cannot reach the target-time-specific Cauchy–Schwarz envelope exactly because one fixed finite pulse cannot be the time-reversed receiver impulse response for every observation time.

---

## 9. Smooth turn-on produces a stronger causal delay

Near $t=0$,

$$
\sin^2(\pi t/T)
\simeq
\pi^2t^2/T^2.
$$

Hence

$$
f_T(t)
\simeq
\sqrt{\frac8{3T}}
\frac{\pi^2t^2}{T^2}.
$$

The receiver amplitude therefore begins as

$$
A(t)
\simeq
\sqrt{\kappa_\Delta}
\sqrt{\frac8{3T}}
\frac{\pi^2}{3T^2}t^3,
$$

so

$$
\boxed{
\tau_T(t)
\simeq
\frac{8\pi^4}{27}
\kappa_\Delta
\frac{t^6}{T^5}.
}
$$

Meanwhile

$$
\boxed{
m(t)
\simeq
\Gamma_{\rm th}t.
}
$$

Thus the source-controlled quantum signal begins as

$$
\boxed{t^6}
$$

while Markov thermal occupation begins as

$$
\boxed{t}.
$$

A nonzero thermal bath therefore guarantees a finite post-light-cone delay before the channel can become non-EB.

In the early-time regime, the first crossing is approximately

$$
\boxed{
\frac{t_-}{T}
\simeq
\left[
\frac{27}{8\pi^4}
\frac{\Gamma_{\rm th}}{\kappa_\Delta}
\right]^{1/5}.
}
$$

This fifth-root onset scaling is a direct consequence of the smooth quadratic wavefront of the chosen source pulse.

---

## 10. Gravity-specific maximum range

Insert the wave-zone source-to-receiver coupling

$$
\boxed{
\kappa_\Delta(R)
=\frac{25\mathcal O}{16(kR)^2}\kappa_g.
}
$$

A smooth-pulse non-EB window can exist only if

$$
\frac{16(kR)^2\Gamma_{\rm th}}
{25\mathcal O\kappa_g}
<H_{\max}(q).
$$

Thus for fixed $q$,

$$
\boxed{
R<R_Q^{\sin^2}(q)
=\frac5{4k}
\sqrt{
\frac{\mathcal O\kappa_g}
{\Gamma_{\rm th}}
H_{\max}(q)
}.
}
$$

Optimizing receiver bandwidth gives

$$
\boxed{
R_Q^{\sin^2,\rm opt}
=\sqrt{H_*}\,R_{\rm env},
}
$$

where

$$
R_{\rm env}
=\frac5{4k}
\sqrt{
\frac{\mathcal O\kappa_g}
{\Gamma_{\rm th}}
}.
$$

Numerically,

$$
\boxed{
R_Q^{\sin^2,\rm opt}
\simeq0.915883\,R_{\rm env}.
}
$$

Thus this one fixed smooth pulse recovers about $91.6\%$ of the ideal envelope's maximum quantum-reception radius.

---

## 11. Spacetime quantum window

For a chosen $q$ and distance $R$, solve

$$
\boxed{
H_q(x)
=
\frac{16(kR)^2\Gamma_{\rm th}}
{25\mathcal O\kappa_g}
}
$$

for the two boundary roots

$$
x_-(R)<x_+(R)
$$

when they exist.

The source-resolved quantum-capability window is

$$
\boxed{
T_-(R)
< T <
T_+(R),
}

with

$$
\boxed{
T_\pm(R)
=\frac Rc+Tx_\pm(R).
}
$$

At the maximum range the two roots merge at the maximum of $H_q$.

Therefore a finite smooth source produces a bounded **quantum bubble in spacetime**, not a permanent quantum cone.

---

## 12. Physical source interpretation

The pulse is not merely a mathematical input mode.

Take a narrowband coherent branch quadrupole

$$
\Delta Q_{ij}^{(+)}(t)
=q_{ij}
e^{-i\omega_0t}
\sin^2\left(\frac{\pi t}{T}\right)
$$

for $0<t<T$.

Its radiative graviton mode has spectral amplitude proportional to

$$
\omega^{5/2}\Delta\widetilde Q_{ij}(\omega).
$$

When

$$
\omega_0T\gg1,
$$

the factor $\omega^{5/2}$ varies little across the pulse bandwidth, so the normalized outgoing branch-difference wavepacket inherits the $\sin^2$ envelope up to controlled narrowband corrections.

A fully conserved stress-energy source must still include whatever internal stresses/forces realize the quadrupole trajectory; the far-zone TT radiation depends on the conserved quadrupole history, not on a nonconserved point-mass prescription.

---

## 13. Why this benchmark is stronger than the old logarithmic front

The old stationary optimized envelope answered:

> If I may choose the best temporal mode separately for each target time, how early could a stationary receiver possibly become non-EB?

The present pulse answers:

> For one smooth finite physical source history and one fixed receiver, when is the actual retarded link non-EB?

The latter is the more relevant Gedanken prediction.

It also exhibits a source-dependent wavefront law: changing how smoothly the source turns on changes the early-time power of the coherent transfer and therefore changes the post-light-cone quantum delay.

---

## 14. Next strongest step

1. Evaluate the **absolute witness gap** $G_{\rm abs}(t,R)$ for this smooth pulse.
2. Optimize source branch separation $a$ and receiver analysis displacement $v$ for a required absolute negativity lower bound.
3. Compare the resulting finite-certification bubble with the bare EB/non-EB bubble.
4. Only then revise the paper core around a source-specific spacetime window rather than a universal logarithmic front.