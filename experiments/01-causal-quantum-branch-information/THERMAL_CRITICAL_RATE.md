# Critical Entanglement Growth Near the Thermal Boundary

**Timestamp:** 2026-08-07 15:47 EDT  
**Status:** Active derivation for Experiment 01

This note sharpens the thermal transition by deriving not only when the NPT front appears, but how rapidly source-receiver entanglement grows immediately after it appears.

---

## 1. Weak-cat negativity in output-noise variables

For the thermal attenuator, the weak-cat negativity derived previously is

$$
\mathcal N_{AB}
=\frac{N_\Delta}{4}
\frac{[\eta(\bar n+1)-\bar n][\bar n+1-\eta\bar n]}
{(1-\eta)\bar n[1+(1-\eta)\bar n]}
+O(N_\Delta^2).
$$

Define the receiver's branch-independent thermal occupation for vacuum signal input,

$$
\boxed{m=(1-\eta)\bar n.}
$$

Then

$$
\eta(\bar n+1)-\bar n=\eta-m,
$$

and

$$
\bar n+1-\eta\bar n=1+m.
$$

The denominator is

$$
m(1+m).
$$

Therefore the entire expression collapses to

$$
\boxed{
\mathcal N_{AB}
=
\frac{N_\Delta}{4}
\frac{\eta-m}{m}
+O(N_\Delta^2),
\qquad m>0.
}
$$

This makes the thermal entanglement-breaking boundary completely transparent:

$$
\boxed{\eta=m.}
$$

The vacuum limit $m\to0$ is nonuniform and must be treated separately; there the leading negativity scales as $\sqrt{\eta N_\Delta}$.

---

## 2. Stationary matched receiver

For a pre-equilibrated receiver,

$$
\kappa=\kappa_g+\kappa_i,
$$

$$
\boxed{m_*=\frac{\kappa_i\bar n_i}{\kappa}.}
$$

For the optimally matched incoming gravitational mode,

$$
\boxed{
\eta(\tau)
=\frac{\kappa_g}{\kappa}
(1-e^{-\kappa\tau}),
\qquad
\tau=t-R/c.
}
$$

The NPT onset satisfies

$$
\eta(\tau_*)=m_*.
$$

Hence

$$
\boxed{
\tau_*
=\frac1\kappa
\ln\left(
\frac{\kappa_g}
{\kappa_g-\bar n_i\kappa_i}
\right),
}
$$

which exists only if

$$
\kappa_g>\bar n_i\kappa_i.
$$

---

## 3. The entanglement-growth slope at the front

Differentiate the coherent transfer coefficient:

$$
\frac{d\eta}{d\tau}
=\kappa_g e^{-\kappa\tau}.
$$

At the NPT front,

$$
e^{-\kappa\tau_*}
=1-\frac{\bar n_i\kappa_i}{\kappa_g}.
$$

Therefore

$$
\boxed{
\left.
\frac{d\eta}{d\tau}
\right|_{\tau_*}
=\kappa_g-\bar n_i\kappa_i.
}
$$

Define the distance above the thermal classicalization boundary,

$$
\boxed{
\delta
\equiv
\kappa_g-\bar n_i\kappa_i>0.
}
$$

Immediately after the front,

$$
\eta(\tau)-m_*
=\delta(\tau-\tau_*)
+O[(\tau-\tau_*)^2].
$$

Substituting into the weak-cat negativity gives

$$
\boxed{
\mathcal N_{AB}(\tau)
=
\frac{N_\Delta}{4m_*}
\delta(\tau-\tau_*)
+O[(\tau-\tau_*)^2,N_\Delta^2].
}
$$

Thus the post-front entanglement growth rate is

$$
\boxed{
\left.
\frac{d\mathcal N_{AB}}{dt}
\right|_{T_{\rm NPT}^+}
=
\frac{N_\Delta}{4m_*}
(\kappa_g-\bar n_i\kappa_i)
+O(N_\Delta^2).
}
$$

---

## 4. Double critical slowing

As

$$
\delta\to0^+,
$$

two things happen simultaneously.

### The front moves arbitrarily far behind the light cone

$$
\boxed{
T_{\rm NPT}-R/c
\sim
\frac1\kappa
\ln\left(\frac{\kappa_g}{\delta}\right).
}
$$

### The entanglement grows arbitrarily slowly after it finally appears

$$
\boxed{
\left.
\frac{d\mathcal N_{AB}}{dt}
\right|_{T_{\rm NPT}^+}
\propto\delta.
}
$$

This gives a genuine **double critical slowing** of the causal quantum-information front near the thermal entanglement-breaking boundary.

The classical gravitational response can already be present, but the quantum part both arrives increasingly late and builds increasingly slowly.

---

## 5. Fully gravitational form

Using

$$
\boxed{
\kappa_g
=
\frac{2G\omega_B^5}{5\hbar c^5}
Q_{ij}^{10}Q_{ij}^{01},
}
$$

the control parameter is

$$
\boxed{
\delta
=
\frac{2G\omega_B^5}{5\hbar c^5}
Q_{ij}^{10}Q_{ij}^{01}
-\bar n_i\kappa_i.
}
$$

Thus the thermal transition can be stated directly as a competition between

- the receiver's quadrupolar graviton absorption/emission rate;
- the receiver's thermal decoherence rate.

The NPT front exists only when $\delta>0$.

---

## 6. Relation to the vacuum weak-capture result

At finite $m_*>0$, the weak-cat negativity is analytic in $N_\Delta$ and begins as

$$
\mathcal N\propto N_\Delta(\eta-m_*).
$$

At zero temperature, $m_*=0$, this expansion becomes singular. The vacuum channel instead has

$$
\mathcal N\sim\frac12\sqrt{\eta N_\Delta}
$$

for a sufficiently weak cat, and optimizing over branch strength at $\eta\ll1$ yields

$$
N_\Delta^{\rm opt}\sim4\sqrt\eta,
$$

$$
\mathcal N_{\max}\sim\eta.
$$

So the zero-temperature and finite-temperature critical laws are genuinely different limits.

---

## 7. Conceptual statement

> **A thermal receiver has a quantum/classical threshold set by the competition between gravitational capture and thermal record formation. Approaching that threshold from the quantum side does not merely make the final entanglement smaller. It changes spacetime dynamics: the entanglement front retreats logarithmically behind the light cone, and the rate at which entanglement grows after the front collapses linearly to zero.**

This is one of the sharpest dynamical predictions produced by the Gedankenexperiment so far.

---

## 8. Novelty discipline

Critical behavior near entanglement-breaking Gaussian-channel boundaries is a general quantum-information topic, so the existence of threshold behavior should not itself be claimed as new.

The potentially distinctive result is the **causal gravitational interpretation** in which the distance from the channel boundary controls both

1. a spacetime delay relative to $R/c$;
2. the post-arrival entanglement growth rate.

A dedicated literature check is still required before treating the double-critical-slowing formulation as novel.

---

## 9. Immediate next step

Numerically optimize finite-$N_\Delta$ source-receiver negativity across the thermal boundary and test whether the maximum negativity obeys a universal near-threshold scaling law in $\delta$ beyond the weak-cat approximation.