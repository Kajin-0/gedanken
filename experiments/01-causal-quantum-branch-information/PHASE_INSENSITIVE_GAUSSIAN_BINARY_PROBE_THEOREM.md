# Binary Coherent Hybrid Probe Theorem for Gauge-Covariant Phase-Insensitive Gaussian Channels

**Timestamp:** 2026-08-07 17:08 EDT  
**Status:** Analytic generalization; novelty unverified.

## 1. Channel convention

Consider a one-mode gauge-covariant phase-insensitive Gaussian channel $\Phi_{\tau,m}$ defined through the symmetrically ordered Weyl characteristic function

$$
\boxed{
\chi_{\Phi(O)}(\xi)
=
\chi_O(\sqrt\tau\,\xi)
\exp\left[-\frac{2m+1-\tau}{2}|\xi|^2\right].
}
$$

Here

- $\tau\ge0$ is the intensity transmission/gain;
- $m\ge0$ is the mean output occupation generated when the input is vacuum.

Indeed, for vacuum input,

$$
\chi_{|0\rangle\langle0|}(\sqrt\tau\xi)
=\exp[-\tau|\xi|^2/2],
$$

so

$$
\chi_{\rm out}(\xi)
=\exp[-(2m+1)|\xi|^2/2].
$$

Complete positivity requires

$$
\boxed{m\ge\max(0,\tau-1).}
$$

In this convention the gauge-covariant channel is entanglement breaking iff

$$
\boxed{m\ge\tau.}
$$

Thus the non-EB region is

$$
\boxed{m<\tau.}
$$

Special cases:

### Thermal attenuator

$$
0\le\tau\le1,
\qquad
m=(1-\tau)\bar n_E.
$$

### Thermal amplifier

$$
\tau>1,
\qquad
m=(\tau-1)(\bar n_E+1).
$$

For a quantum-limited amplifier $\bar n_E=0$,

$$
m=\tau-1<\tau,
$$

so it is not entanglement breaking at any finite gain.

### Additive classical Gaussian noise

$$
\tau=1,
$$

and $m$ is the added output occupation. The EB boundary is

$$
m\ge1.
$$

---

## 2. Binary coherent hybrid input

Take

$$
\boxed{
|\Psi\rangle
=
\sqrt p\,|0\rangle|\alpha\rangle
+e^{i\phi}\sqrt{1-p}\,|1\rangle|\beta\rangle,
}
$$

with

$$
0<p<1,
\qquad
\alpha\neq\beta,
\qquad
|\alpha|,|\beta|<\infty.
$$

Only the bosonic subsystem is sent through $\Phi_{\tau,m}$.

---

## 3. Theorem

> **Binary coherent phase-insensitive Gaussian probe theorem.** For every nontrivial finite binary coherent hybrid state above,
>
> $$
> \boxed{
> (I\otimes\Phi_{\tau,m})(|\Psi\rangle\langle\Psi|)
> \text{ is NPT}
> \iff
> m<\tau.
> }
> $$
>
> Since $m<\tau$ is exactly the non-entanglement-breaking region of the gauge-covariant one-mode phase-insensitive Gaussian channel, every such binary coherent hybrid state is a complete EB probe for this entire channel family.

The threshold is independent of

- coherent-state midpoint;
- phase-space orientation of the separation;
- any finite nonzero coherent-state separation;
- any nonzero branch weights;
- source relative phase.

These parameters affect entanglement magnitude, not whether the output is NPT.

---

## 4. Why the proof is channel-universal

For the coherent dyad $|\alpha\rangle\langle\beta|$,

$$
\boxed{
\chi_{\alpha\beta}(\xi)
=
\langle\beta|\alpha\rangle
\exp\left[
-\frac{|\xi|^2}{2}
+\beta^*\xi-\alpha\xi^*
\right].
}
$$

Applying the general channel gives

$$
\chi_{\rm out}(\xi)
=
\langle\beta|\alpha\rangle
\exp\left[
-\frac{2m+1}{2}|\xi|^2
+\sqrt\tau\,(\beta^*\xi-\alpha\xi^*)
\right].
$$

The key point is that this output dyad depends on the channel **only through $\tau$ and $m$**.

It has exactly the same analytic form as the thermal-attenuator output used in `EXACT_FINITE_CAT_THERMAL_THEOREM.md`, with the replacement

$$
\eta\rightarrow\tau.
$$

Therefore the complete normal-ordered block factorization and explicit negative-vector proof carry over unchanged.

---

## 5. Reduction of arbitrary coherent pair

Using displacement covariance, define

$$
\gamma=\frac{\alpha+\beta}{2},
\qquad
\delta=\alpha-\beta.
$$

The common midpoint $\gamma$ is removable by a local output displacement and cannot affect entanglement. Phase covariance rotates $\delta$ to positive real. Thus the problem reduces to

$$
|\pm a\rangle,
\qquad
\boxed{a=|\alpha-\beta|/2.}
$$

Unequal nonzero branch weights factor into the diagonal Gaussian block factors and cancel from the normalized off-diagonal operator exactly as in `BINARY_COHERENT_EB_PROBE_THEOREM.md`.

---

## 6. Exact NPT parameter

The same factorization gives

$$
\boxed{
q
=
\exp\left[
\frac{2a^2}{m}(\tau-m)
\right]
}
$$

for the symmetric representation, or equivalently

$$
\boxed{
q
=
\exp\left[
\frac{|\alpha-\beta|^2}{2m}(\tau-m)
\right].
}
$$

For every finite distinct coherent pair,

$$
q>1
\iff
\tau>m.
$$

The explicit normalizable negative vector from the attenuator proof therefore proves

$$
\tau>m
\Rightarrow\rho_{AB}^{\Gamma_A}\not\succeq0.
$$

Conversely, if

$$
m\ge\tau,
$$

the channel is entanglement breaking, so every output is separable.

Combining both directions proves the theorem.

---

## 7. General exact principal-minor witness

For the symmetric representation $|\pm a\rangle$, choose

$$
\boxed{
v_*=\frac{2\sqrt\tau\,a}{m}.}
$$

Equivalently, in terms of the original coherent separation,

$$
\boxed{
|v_*|=\frac{\sqrt\tau\,|\alpha-\beta|}{m}.
}
$$

After applying the local displacement/rotation that maps the pair to $|\pm a\rangle$, define

$$
p_0=\langle0,0|\rho|0,0\rangle,
$$

$$
p_v=\langle1,v_*|\rho|1,v_*\rangle,
$$

and

$$
z_v=\langle1,0|\rho|0,v_*\rangle.
$$

Then

$$
\boxed{
\frac{|z_v|^2}{p_0p_v}
=
\exp\left[
\frac{|\alpha-\beta|^2}{m}(\tau-m)
\right].
}
$$

Hence

$$
\boxed{
|z_v|^2>p_0p_v
\iff
\tau>m
\iff
\Phi_{\tau,m}\text{ is non-EB}.
}
$$

Thus the exact state-level boundary can be certified with two populations and one joint coherence throughout the full gauge-covariant phase-insensitive Gaussian family.

---

## 8. Amplifier consequence

For a thermal amplifier of gain

$$
G=\tau>1
$$

with environment occupation $\bar n_E$,

$$
m=(G-1)(\bar n_E+1).
$$

The output hybrid state is NPT iff

$$
(G-1)(\bar n_E+1)<G.
$$

Therefore

$$
\boxed{
\bar n_E<\frac1{G-1}.
}
$$

This is exactly the amplifier EB threshold.

For the quantum-limited amplifier,

$$
\bar n_E=0,
$$

so every finite gain remains on the NPT side for every nontrivial binary coherent hybrid input. As $G\to\infty$, the state can approach the boundary continuously even though it never crosses it at finite gain.

This explains why naive finite-Fock two-mode-squeezer numerics are particularly unreliable near high-gain/high-temperature thresholds: the required environmental Hilbert-space support grows rapidly.

---

## 9. Additive-noise consequence

For

$$
\tau=1,
$$

the binary coherent hybrid output is NPT iff

$$
\boxed{m<1.}
$$

Thus the exact binary-probe transition also coincides with the additive Gaussian-noise EB threshold.

---

## 10. Gravity relevance

The passive gravitational receiver analyzed so far is attenuator-like, so the previous causal-front theorem remains unchanged.

However, the generalized theorem clarifies active receiver extensions. If an active linear receiver produces an effective gauge-covariant Gaussian channel with instantaneous parameters

$$
\tau(t),\qquad m(t),
$$

then any nontrivial finite binary coherent branch encoding is NPT at that time exactly when

$$
\boxed{
\tau(t)>m(t).
}
$$

Therefore gain itself is not the quantum resource. The relevant quantity is the **excess coherent gain/transmission above vacuum-output occupation**,

$$
\boxed{\Delta_Q(t)=\tau(t)-m(t).}
$$

An active receiver can amplify a classical branch response enormously while still approaching the EB surface if its added noise grows with the gain.

---

## 11. Literature / novelty status

The channel classification and EB conditions are established Gaussian-channel theory. Binary coherent states and effective-entanglement channel tests are also established.

The targeted search performed on 2026-08-07 has not located the stronger exact statement that **every nontrivial finite binary coherent hybrid state is NPT iff an arbitrary gauge-covariant one-mode phase-insensitive Gaussian channel is non-entanglement-breaking**, nor the matched three-element principal-minor witness reaching that boundary.

This remains **novelty unverified**. A general structural theorem may imply the result indirectly.

---

## 12. Strongest next step

1. Search for a general Gaussian-channel theorem implying binary coherent probe completeness.
2. Independently audit the amplifier and additive-noise cases using analytic covariance/characteristic-function methods rather than finite-Fock dilation.
3. If no prior theorem is found, treat this as a candidate standalone quantum-information lemma and use the gravitational causal-front theorem as its physical application.
4. Extend the causal-front bound to active Gaussian receivers in terms of the dynamical excess $\Delta_Q(t)=\tau(t)-m(t)$.
