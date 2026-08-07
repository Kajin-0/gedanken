# Thermal Fronts from Explicit Input-Output Dynamics

**Timestamp:** 2026-08-07 15:36 EDT  
**Status:** Active derivation for Experiment 01

This note replaces the phenomenological time-dependent capture fraction by the explicit Markovian input-output dynamics of a matched quantum receiver.

---

## 1. Receiver Langevin equation

Let $t_0=R/c$ denote the earliest causal arrival of the branch-dependent gravitational wavepacket at the receiver. For $t\ge t_0$, model a collective receiver mode $c$ by

$$
\boxed{
\dot c(t)
=-\frac{\kappa}{2}c(t)
+\sqrt{\kappa_g}\,b_{\rm in}(t)
+\sqrt{\kappa_i}\,\xi_{\rm in}(t),
}
$$

where

$$
\kappa=\kappa_g+\kappa_i.
$$

Here

- $\kappa_g$ is coupling to the selected gravitational input channel;
- $\kappa_i$ is uncontrolled internal loss;
- $b_{\rm in}$ is the gravitational input field;
- $\xi_{\rm in}$ is a thermal internal bath with mean occupation $\bar n_i$.

The exact solution after causal arrival, with $\tau=t-t_0$, is

$$
\boxed{
 c(t)
=e^{-\kappa\tau/2}c(t_0)
+\sqrt{\kappa_g}
\int_{t_0}^{t}ds\,e^{-\kappa(t-s)/2}b_{\rm in}(s)
+\sqrt{\kappa_i}
\int_{t_0}^{t}ds\,e^{-\kappa(t-s)/2}\xi_{\rm in}(s).
}
$$

This is standard quantum input-output theory; the gravity-specific assumption is that the branch-dependent outgoing gravitational difference mode couples into this selected receiver port.

---

## 2. Exact coherent transfer coefficient for an arbitrary incoming wavepacket

Let the branch difference in the input field be

$$
\langle b_{\rm in}(s)\rangle_L
-
\langle b_{\rm in}(s)\rangle_R
=
\sqrt{N_\Delta}\,f(s),
$$

with normalized temporal mode

$$
\int ds\,|f(s)|^2=1.
$$

The receiver branch-displacement difference is

$$
\Delta\alpha_c(t)
=
\sqrt{\kappa_gN_\Delta}
\int_{t_0}^{t}ds\,
e^{-\kappa(t-s)/2}f(s).
$$

Define the exact time-dependent coherent transfer coefficient

$$
\boxed{
\eta_f(t)
\equiv
\frac{|\Delta\alpha_c(t)|^2}{N_\Delta}
=
\kappa_g
\left|
\int_{t_0}^{t}ds\,
e^{-\kappa(t-s)/2}f(s)
\right|^2.
}
$$

This is the correct dynamical replacement for the earlier phenomenological cumulative fraction $\eta_\infty F(t-R/c)$.

By Cauchy-Schwarz,

$$
\boxed{
\eta_f(t)
\le
\eta_{\max}(\tau)
=
\frac{\kappa_g}{\kappa}
\left(1-e^{-\kappa\tau}\right).
}
$$

The bound is saturated by the normalized time-reversed receiver kernel on the available interval,

$$
f_{\rm opt}^{(t)}(s)
\propto
e^{-\kappa(t-s)/2},
\qquad t_0\le s\le t.
$$

For $\tau\to\infty$,

$$
\eta_{\max}\to
\frac{\kappa_g}{\kappa_g+\kappa_i},
$$

recovering the earlier matched-memory efficiency.

---

## 3. Exact branch-independent receiver noise

Let the receiver occupation at causal arrival be

$$
\bar n_0=\langle c^\dagger c\rangle_{t_0}
$$

apart from coherent branch displacement. With the gravitational input port in vacuum apart from its coherent signal,

$$
\boxed{
 m(t)
=e^{-\kappa\tau}\bar n_0
+
\frac{\kappa_i\bar n_i}{\kappa}
\left(1-e^{-\kappa\tau}\right).
}
$$

Here $m(t)$ is the conditional receiver thermal occupation; it is identical for the two source branches.

At each time, the selected gravitational input mode therefore induces an effective phase-insensitive attenuator into the receiver with

- signal transmissivity $\eta_f(t)$;
- output thermal occupation $m(t)$ for vacuum signal input.

Equivalently, when $\eta_f<1$, its effective environmental occupation is

$$
\bar n_{\rm eff}(t)
=
\frac{m(t)}{1-\eta_f(t)}.
$$

---

## 4. Instantaneous weak-cat entanglement condition

For a thermal attenuator with transmissivity $\eta$ and output thermal occupation $m=(1-\eta)\bar n$, the entanglement-breaking condition

$$
\eta\le\frac{\bar n}{\bar n+1}
$$

is exactly equivalent to

$$
\boxed{\eta\le m.}
$$

Therefore the weak source-cat becomes NPT at time $t$ iff

$$
\boxed{
\eta_f(t)>m(t).
}
$$

This is the simplest dynamical thermal criterion obtained so far.

---

## 5. Instantaneous fidelity-history condition

For the same effective channel, the conditional receiver-state root fidelity is

$$
\boxed{
F_B(t)
=
\exp\left[
-\frac{\eta_f(t)N_\Delta}
{2[1+2m(t)]}
\right].
}
$$

The complementary history coherence is

$$
\boxed{
C_\Xi(t)
=
\exp\left[
-\frac{[1-\eta_f(t)+2m(t)]N_\Delta}
{2[1+2m(t)]}
\right].
}
$$

Hence

$$
\boxed{
\mathcal M_F(t)
=
\frac{N_\Delta}{2[1+2m(t)]}
\left[2\eta_f(t)-1-2m(t)\right].
}
$$

The global fidelity-history witness is positive iff

$$
\boxed{
\eta_f(t)>m(t)+\frac12.
}
$$

Thus the exact dynamical hierarchy is

$$
\boxed{
\text{NPT: }\eta_f>m,
\qquad
\text{fidelity witness: }\eta_f>m+\frac12.
}
$$

---

## 6. Minimal PPT observable in dynamical form

In the weak-cat limit write the incoming difference-mode state as

$$
|+\rangle|0\rangle+a|-\rangle|1_f\rangle+O(a^2).
$$

At time $t$, define

$$
G(t)=1+m(t).
$$

The three quantities in the targeted principal-minor witness become

$$
P_{+,1}(t)
=
\frac{m(t)}{G(t)^2}
+O(|a|^2),
$$

$$
P_{-,0}(t)
=
|a|^2
\frac{G(t)-\eta_f(t)}{G(t)^2}
+O(|a|^4),
$$

$$
Z_0(t)
=
a\frac{\sqrt{\eta_f(t)}}{G(t)^2}
+O(|a|^3).
$$

Therefore

$$
\boxed{
|Z_0(t)|^2
-P_{+,1}(t)P_{-,0}(t)
=
\frac{|a|^2}{[1+m(t)]^3}
\left[\eta_f(t)-m(t)\right]
+O(|a|^4).
}
$$

So the minimal $0/1$-sector PPT witness crosses zero at exactly the same dynamical condition

$$
\boxed{\eta_f(t)=m(t).}
$$

This gives a direct operational definition of the causal NPT front from the receiver dynamics.

---

## 7. Pre-equilibrated receiver: exact optimal front times

A physically natural case is a receiver that has been coupled to both ports for a long time before the gravitational wave arrives. Its stationary occupation is

$$
\boxed{
 m_*
=\frac{\kappa_i\bar n_i}{\kappa}.
}
$$

Thus

$$
m(t)=m_*
$$

throughout the coherent capture process.

Using the optimally matched transfer coefficient

$$
\eta_{\max}(\tau)
=
\frac{\kappa_g}{\kappa}
\left(1-e^{-\kappa\tau}\right),
$$

the NPT front exists iff

$$
\boxed{
\kappa_g>\bar n_i\kappa_i.
}
$$

When it exists,

$$
\boxed{
T_{\rm NPT}^{\rm opt}(R)
=
\frac{R}{c}
+
\frac1\kappa
\ln\left(
\frac{\kappa_g}
{\kappa_g-\bar n_i\kappa_i}
\right).
}
$$

The fidelity-history front exists iff

$$
\boxed{
\kappa_g>(2\bar n_i+1)\kappa_i,
}
$$

and then

$$
\boxed{
T_F^{\rm opt}(R)
=
\frac{R}{c}
+
\frac1\kappa
\ln\left[
\frac{2\kappa_g}
{\kappa_g-(2\bar n_i+1)\kappa_i}
\right].
}
$$

These are the first explicit post-light-cone onset times derived directly from the receiver Langevin dynamics.

---

## 8. Critical slowing at the quantum/classical boundary

Let

$$
\delta
=\kappa_g-\bar n_i\kappa_i>0.
$$

Near the fundamental thermal boundary,

$$
\boxed{
T_{\rm NPT}^{\rm opt}-\frac{R}{c}
\sim
\frac1\kappa
\ln\left(\frac{\kappa_g}{\delta}\right).
}
$$

Thus the NPT onset moves arbitrarily far behind the classical light-cone arrival as the receiver approaches its entanglement-breaking threshold from the quantum side.

Similarly, defining

$$
\delta_F
=\kappa_g-(2\bar n_i+1)\kappa_i>0,
$$

$$
T_F^{\rm opt}-R/c
\sim
\kappa^{-1}\ln(2\kappa_g/\delta_F).
$$

This **critical slowing of the nonclassicality front** is a sharper dynamical statement than the static channel thresholds alone.

---

## 9. Cold-prepared versus stationary receiver

The finite post-light-cone delay is not caused by temperature in an abstract sense; it depends on receiver preparation.

If the memory is actively prepared in its ground state at $t_0$, so $\bar n_0=0$, then

$$
m(t)
=
\frac{\kappa_i\bar n_i}{\kappa}
(1-e^{-\kappa\tau}).
$$

For the optimally matched input,

$$
\eta_{\max}(t)
=
\frac{\kappa_g}{\kappa}
(1-e^{-\kappa\tau}).
$$

Thus

$$
\frac{\eta_{\max}(t)}{m(t)}
=
\frac{\kappa_g}{\kappa_i\bar n_i}
$$

for every $\tau>0$.

Therefore:

- if $\kappa_g>\bar n_i\kappa_i$, weak-cat entanglement begins immediately with the first nonzero coherent capture after $R/c$;
- if $\kappa_g\le\bar n_i\kappa_i$, it never begins in this ideal matched model.

So the **post-light-cone NPT delay is a consequence of a pre-existing thermal noise floor**, not an unavoidable consequence of a hot bath by itself.

This corrects the overly broad earlier statement that finite temperature necessarily creates an additional delay.

---

## 10. Fixed physical wavepacket

For an actual fixed source waveform $f$, the causal NPT time is not obtained from the optimized $\eta_{\max}$ but from

$$
\boxed{
T_{\rm NPT}(R)
=
\inf\left\{
T\ge R/c:
\eta_f(T)>m(T)
\right\}.
}
$$

Likewise,

$$
\boxed{
T_F(R)
=
\inf\left\{
T\ge R/c:
\eta_f(T)>m(T)+\frac12
\right\}.
}
$$

This is the correct general definition of the two quantum fronts for a finite physical gravitational wavepacket.

The earlier cumulative-intensity model is therefore a useful intuition, while the convolution above is the actual matched-filter dynamics.

---

## 11. Literature boundary

The Markovian input-output equation, matched temporal-mode absorption, thermal attenuator structure, and Gaussian entanglement-breaking threshold are established quantum-optics/channel theory. Relevant primary literature includes quantum input-output treatments of cavity pulse modes and Holevo's Gaussian entanglement-breaking condition; Mari, Zippilli, and Vitali already apply a Gaussian thermal attenuator criterion to a gravity-mediated channel.

No novelty is claimed for those mathematical ingredients.

Potentially distinctive here is their use to derive an explicit **causal gravitational entanglement-front dynamics**:

$$
\boxed{
T_{\rm signal}=R/c
\quad\hbox{versus}\quad
T_{\rm NPT}>R/c
}
$$

with a logarithmically diverging post-light-cone delay near the thermal classicalization boundary.

---

## 12. Immediate next step

The next target is to remove the remaining phenomenological element $\kappa_g$ by deriving the receiver input-output coupling rate directly from the linearized-gravity interaction with a normalized quadrupolar graviton wavepacket. This should connect

$$
\kappa_g
$$

directly to the receiver quadrupole matrix element and the gravitational radiation spectral density, and thereby turn the front times above into fully gravitational predictions.