# Quantum-Capability Window of the Closed Four-Mass Source

**Timestamp:** 2026-08-07 20:04 EDT  
**Status:** Source-specific receiver calculation for the normalized narrowband graviton mode emitted by `CONSERVED_FOUR_MASS_QUADRUPOLE_SOURCE.md`.

## 1. Emitted temporal mode

The explicit four-mass branch quadrupole uses

$$
q(t)
=q_0
\sin^4\left(\frac{\pi t}{T}\right)
\cos(\omega_0t),
\qquad 0<t<T,
$$

with

$$
q_0=4\mu d_0.
$$

In the narrowband regime

$$
\omega_0T\gg1,
$$

the normalized positive-frequency graviton difference mode is

$$
\boxed{
f_4(t)
=\sqrt{\frac{128}{35T}}
\sin^4\left(\frac{\pi t}{T}\right),
\qquad 0<t<T.
}
$$

It vanishes outside the pulse.

---

## 2. Receiver response

Let the receiver total linewidth be

$$
\kappa
$$

and useful source-mode coupling rate be

$$
\kappa_\Delta(R).
$$

After retarded arrival, the stored coherent amplitude is

$$
A_4(t)
=\sqrt{\kappa_\Delta}
\int_0^t ds\,
e^{-\kappa(t-s)/2}f_4(s).
$$

Define

$$
u=\min(t,T).
$$

Then

$$
\boxed{
A_4(t)
=\sqrt{\frac{128\kappa_\Delta}{35T}}
e^{-\kappa t/2}I_4(u),
}
$$

where

$$
I_4(u)
=\int_0^u ds\,
e^{\kappa s/2}
\sin^4\left(\frac{\pi s}{T}\right).
$$

The signal transmissivity is

$$
\boxed{
\tau_4(t)
=\frac{128\kappa_\Delta}{35T}
e^{-\kappa t}
I_4^2[\min(t,T)].
}
$$

---

## 3. Closed form

Let

$$
\alpha=\kappa/2,
$$

and define

$$
E(\Omega,u)
=\int_0^u ds\,
e^{\alpha s}\cos(\Omega s).
$$

Then

$$
\boxed{
E(\Omega,u)
=\frac{
e^{\alpha u}
[\alpha\cos(\Omega u)+\Omega\sin(\Omega u)]
-\alpha
}{\alpha^2+\Omega^2}.
}
$$

Also

$$
E(0,u)
=\frac{e^{\alpha u}-1}{\alpha}.
$$

Using

$$
\sin^4\theta
=\frac38-
\frac12\cos(2\theta)
+\frac18\cos(4\theta),
$$

we obtain

$$
\boxed{
I_4(u)
=\frac38E(0,u)
-\frac12E(2\pi/T,u)
+\frac18E(4\pi/T,u).
}
$$

Thus the complete fixed-source receiver channel is elementary.

---

## 4. Dimensionless form

Define

$$
\boxed{x=t/T,}
$$

$$
\boxed{q=\kappa T,}
$$

and

$$
y=\min(x,1).
$$

Let

$$
\boxed{
J_{4,q}(y)
=\int_0^y dz\,
e^{qz/2}\sin^4(\pi z).
}
$$

Define

$$
\boxed{
S_{4,q}(x)
=\frac{128q}{35}
e^{-qx}J_{4,q}^2(y).
}
$$

Then

$$
\boxed{
\tau_4(x,R)
=\frac{\kappa_\Delta(R)}{\kappa}
S_{4,q}(x).
}
$$

For an initially ground-state receiver with occupied-bath injection rate $\Gamma_{\rm th}$,

$$
\boxed{
m(x)
=\frac{\Gamma_{\rm th}}{\kappa}
N_q(x),
}
$$

where

$$
\boxed{
N_q(x)=1-e^{-qx}.
}
$$

---

## 5. Exact EB/non-EB condition

The source-mode $\to$ receiver channel is non-entanglement-breaking exactly when

$$
\tau_4>m.
$$

Therefore

$$
\boxed{
\frac{\kappa_\Delta}{\Gamma_{\rm th}}
H_{4,q}(x)>1,
}
$$

where

$$
\boxed{
H_{4,q}(x)
=\frac{S_{4,q}(x)}{N_q(x)}.
}
$$

Define

$$
H_{4,\max}(q)
=\max_{x>0}H_{4,q}(x).
$$

A non-EB time window exists iff

$$
\boxed{
\frac{\Gamma_{\rm th}}
{\kappa_\Delta}
<H_{4,\max}(q).
}
$$

---

## 6. Receiver-bandwidth optimum

Numerical optimization of the exact closed response gives

$$
\boxed{
q_{\rm cap,opt}
=\kappa T
\simeq5.41429,
}
$$

with the maximum occurring at

$$
\boxed{
x_{\rm cap,opt}
\simeq0.668187.
}
$$

The global maximum is

$$
\boxed{
H_{4,*}
\simeq0.8136763.
}
$$

Therefore the mechanically explicit pulse can develop a non-EB window only if

$$
\boxed{
\kappa_\Delta
>
\frac1{H_{4,*}}\Gamma_{\rm th}
\simeq1.22899\,\Gamma_{\rm th}.
}
$$

This is only about $22.9\%$ more demanding than the ideal target-time-specific envelope condition

$$
\kappa_\Delta>\Gamma_{\rm th}.
$$

---

## 7. Gravity-specific maximum range

Use the wave-zone source-mode coupling

$$
\boxed{
\kappa_\Delta(R)
=\frac{25\mathcal O}{16(kR)^2}\kappa_g.
}
$$

The source-specific quantum window exists only when

$$
\frac{16(kR)^2\Gamma_{\rm th}}
{25\mathcal O\kappa_g}
<H_{4,\max}(q).
$$

Therefore

$$
\boxed{
R<R_{Q,4}(q)
=\frac5{4k}
\sqrt{
\frac{\mathcal O\kappa_g}
{\Gamma_{\rm th}}
H_{4,\max}(q)
}.
}
$$

At optimal bandwidth,

$$
\boxed{
R_{Q,4}^{\rm opt}
=\sqrt{H_{4,*}}R_{\rm env}
\simeq0.902040\,R_{\rm env},
}
$$

where

$$
R_{\rm env}
=\frac5{4k}
\sqrt{
\frac{\mathcal O\kappa_g}
{\Gamma_{\rm th}}
}
$$

is the unattainable target-time-reoptimized envelope radius.

Thus the explicit closed mechanical source retains about $90.2\%$ of the ideal envelope's maximum capability range.

---

## 8. Very smooth wavefront: signal begins as $t^{10}$

Near the causal wavefront,

$$
\sin^4(\pi t/T)
\simeq
\pi^4t^4/T^4.
$$

Hence

$$
f_4(t)
\simeq
\sqrt{\frac{128}{35T}}
\frac{\pi^4t^4}{T^4}.
$$

The receiver amplitude begins as

$$
A_4(t)
\simeq
\sqrt{\kappa_\Delta}
\sqrt{\frac{128}{35T}}
\frac{\pi^4}{5T^4}t^5.
$$

Therefore

$$
\boxed{
\tau_4(t)
\simeq
\frac{128\pi^8}{875}
\kappa_\Delta
\frac{t^{10}}{T^9}.
}
$$

Meanwhile

$$
m(t)
\simeq
\Gamma_{\rm th}t.
$$

Thus

$$
\boxed{
\text{coherent branch transfer}\sim t^{10},
\qquad
\text{Markov thermal occupation}\sim t.
}
$$

A finite post-light-cone capability delay is unavoidable at nonzero $\Gamma_{\rm th}$.

In the early-time regime the first crossing satisfies approximately

$$
\boxed{
\frac{t_-}{T}
\simeq
\left[
\frac{875}{128\pi^8}
\frac{\Gamma_{\rm th}}
{\kappa_\Delta}
\right]^{1/9}.
}
$$

Numerically,

$$
\left(
\frac{875}{128\pi^8}
\right)^{1/9}
\simeq0.44755.
$$

The wavefront exponent is therefore directly controlled by source smoothness.

---

## 9. Finite quantum window

For a fixed $q$ and $R$, solve

$$
\boxed{
H_{4,q}(x)
=\frac{\Gamma_{\rm th}}
{\kappa_\Delta(R)}
}
$$

for the two roots

$$
x_-(R)<x_+(R)
$$

when they exist.

Then the source-resolved channel is non-EB only for

$$
\boxed{
\frac Rc+Tx_-(R)
<T_{\rm lab}<
\frac Rc+Tx_+(R).
}
$$

At maximum range the two boundaries merge at the maximum of $H_{4,q}$.

Thus the explicit closed source produces a finite **quantum-capability bubble** inside the ordinary future light cone.

---

## 10. Absolute witness bubble

In the weak-link regime, the optimized minimal witness satisfies

$$
G_{\rm abs}^{\rm opt}
\simeq
c_0[\tau_4-m]_+,
$$

with

$$
c_0=\frac12W(e^{-1}).
$$

Therefore

$$
\boxed{
G_{\rm abs}^{\rm opt}(x,R)
\simeq
\frac{c_0}{\kappa}
\left[
\kappa_\Delta(R)S_{4,q}(x)
-\Gamma_{\rm th}N_q(x)
\right]_+.
}
$$

A finite certification requirement $G_{\rm req}$ produces the exact leading-order radius-at-time bound

$$
\boxed{
R^2
\le
\frac{
K_GS_{4,q}(x)
}{
\Gamma_{\rm th}N_q(x)
+\kappa G_{\rm req}/c_0
},
}
$$

where

$$
K_G
=\frac{25\mathcal O}{16k^2}\kappa_g.
$$

Thus the explicit mechanical source has both

1. a bare EB/non-EB bubble;
2. a smaller absolute-certification bubble.

---

## 11. Vacuum absolute-strength optimization

In vacuum,

$$
\Gamma_{\rm th}=0,
$$

the bare pure-loss channel is mathematically non-EB whenever the source coupling is nonzero.

The absolute witness range remains finite.

For this $\sin^4$ source family, numerical optimization of

$$
S_{4,q}^{\max}
=\max_xS_{4,q}(x)
$$

gives

$$
\boxed{
q_{\rm vac,opt}
\simeq6.40192,
}
$$

$$
\boxed{
x_{\rm vac,opt}
\simeq0.659687,
}
$$

and

$$
\boxed{
S_{4,*}
\simeq0.7980213.
}
$$

Therefore the optimized weak-link three-element witness obeys

$$
\boxed{
R_{G,4}^{\rm vac,opt}
=
\sqrt{
\frac{c_0K_GS_{4,*}}
{\kappa G_{\rm req}}
}.
}
$$

Numerically,

$$
\sqrt{c_0S_{4,*}}
\simeq0.33333,
$$

so approximately

$$
\boxed{
R_{G,4}^{\rm vac,opt}
\simeq
0.3333
\sqrt{
\frac{K_G}
{\kappa G_{\rm req}}
}.
}
$$

The near-$1/3$ coefficient is numerical for this optimization and should not be treated as an exact identity without an analytic proof.

---

## 12. Source strength in mechanical parameters

The explicit source has branch-mode coherent distance

$$
\boxed{
N_\Delta
\simeq
\frac78
\frac{G\mu^2d_0^2\omega_0^5T}
{\hbar c^5}.
}
$$

Therefore source preparation and receiver certification can now be related through physical parameters

$$
\mu,\ d_0,\ L,\ \omega_0,\ T,\ R,\ \kappa_g,\ \Gamma_{\rm th},\ \kappa.
$$

This is the first fully explicit source-to-receiver parameter chain in Experiment 01.

---

## 13. Current strongest interpretation

> **The source smoothness determines how quickly quantum branch information can build immediately behind the light cone. The source geometry determines the emitted coherent branch distance. Free-space gravity determines how the useful mode falls with distance. The receiver determines whether that arriving mode ever outruns its thermal record. For the closed four-mass pulse, these pieces produce a finite non-entanglement-breaking bubble in spacetime, and a still smaller bubble in which a finite absolute NPT weight can be certified.**

---

## 14. Strongest next step

The remaining source-side weakness is the actuator/stress model. Construct an explicit closed Hamiltonian for the four-mass deformation, or show that any conserved internal stress realization with the same leading STF quadrupole produces the same far-zone branch mode up to post-Newtonian corrections.