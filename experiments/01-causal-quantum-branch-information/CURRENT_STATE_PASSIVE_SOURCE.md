# Current State — Passive Conserved Source→Gravitational Mode→Noisy Receiver

**Date:** 2026-08-07  
**Status:** **CANONICAL RECOVERY POINT**  
**Read first after a context reset:** root `AGENTS.md`, then this file.

## 1. Executive state

The project has passed through two major adversarial pivots.

First, broad standalone Gaussian-channel novelty claims were killed by prior art:

- rank-two Fock survival — Mele–Lami–Giovannetti;
- all-finite binary coherent survival — Filippov–Ziman;
- even the matched coherent scale and exact exponential sign factor are already encoded in a Filippov–Ziman witness parameter choice.

Those results are retained as short lemmas and diagnostics, not discovery claims.

Second, the gravity source was upgraded from prescribed accelerated endpoint masses to an explicit finite-mass conserved four-spoke elastic source. The support does not cancel the branch quadrupole; it gives a controlled $1+O(q^2)$ correction.

The canonical gravity protocol is now:

$$
\boxed{
\text{common prepared static branch state}
\to
\text{smooth local release}
\to
\text{passive conserved free emission}
\to
\text{retarded gravitational temporal mode}
\to
\text{noisy resonant receiver}.
}
$$

The active $\sin^4$ waveform remains a secondary engineered protocol, not the primary conservation benchmark.

---

## 2. Conserved four-spoke source

Use

- four endpoint masses $\mu$;
- four longitudinal elastic spokes of length $L$;
- central junction/hub;
- longitudinal sound speed $c_s$;
- one-spoke rest mass $m_r$.

Define

$$
\boxed{q=\omega L/c_s.}
$$

For the linear nonrelativistic spoke model,

$$
\boxed{
f_q(x)=\frac{\sin(qx/L)}{\sin q},}
$$

and endpoint traction gives

$$
\boxed{\frac{m_r}{\mu}=q\tan q.}
$$

The controlled regime is

$$
\boxed{\beta=\omega L/c\ll q\ll1,}
$$

with $c_s\ll c$ if one wants to remain strictly inside ordinary linear elasticity.

Do not advertise $m_r/\mu\ge\beta^2$ with coefficient one as a universal relativistic bound; that requires a covariant elastic completion.

---

## 3. Total branch quadrupole

For mirrored plus-mode branches,

$$
\boxed{
\Delta Q_{xx}
=8\mu Lu\frac{\tan q}{q},
}
$$

$$
\boxed{
\Delta Q_{yy}
=-8\mu Lu\frac{\tan q}{q}.
}
$$

Hence finite support reinforces rather than cancels the endpoint quadrupole.

For $q\ll1$,

$$
\boxed{
\frac{\tan q}{q}
=1+\frac{q^2}{3}+rac{2q^4}{15}+O(q^6).
}
$$

Canonical derivation:

- `CONSERVED_SOURCE_ACTUATOR_AUDIT.md`

---

## 4. Quantized mode and corrected gravitational linewidth

Define

$$
\boxed{
A(q)=\frac12+\frac{q}{\sin2q}.}
$$

Then

$$
\boxed{
M_{\rm eff}(q)=4\mu A(q),
}
$$

$$
\boxed{
u_{\rm zpf}(q)
=\sqrt{\frac{\hbar}{2M_{\rm eff}(q)\omega}},}
$$

$$
\boxed{
q_{01}(q)
=4\mu L\frac{\tan q}{q}
\sqrt{\frac{\hbar}{2M_{\rm eff}(q)\omega}}.
}
$$

The corrected spontaneous gravitational linewidth is

$$
\boxed{
\kappa_g(q)
=\frac{8G\mu L^2\omega^4}{5c^5}
\mathcal C_\kappa(q),
}
$$

where

$$
\boxed{
\mathcal C_\kappa(q)
=\frac{(\tan q/q)^2}{A(q)}
=1+\frac{q^2}{3}+\frac{q^4}{9}+O(q^6).
}
$$

Canonical note:

- `QUANTIZED_PLUS_MODE_SOURCE.md`

---

## 5. Finite-size and controller error budget

### Support inertia

Explicitly included through $q$.

### Gravitational finite-size retardation

Because the source is inversion symmetric, the $O(\beta)$ internal-retardation term vanishes. Generic field corrections begin at

$$
\boxed{O(\beta^2),}
$$

with

$$
\beta=\omega L/c.
$$

### Compact hub/controller contamination

For branch-asymmetric controller energy supported inside radius $r_h$,

$$
\boxed{
|\Delta Q_{ij}^{\rm ctrl}|
\le
\frac{r_h^2}{c^2}E_{\rm TV}^{\rm ctrl}.
}
$$

In the ideal controlled-parity model, the controller energy density can be branch common and its direct branch quadrupole vanishes.

### Weak self-gravity

Corrections are controlled by compactness

$$
\boxed{\mathcal C=2GM/(c^2L)\ll1.}
$$

Read:

- `FINITE_SIZE_FIELD_ERROR_BOUND.md`
- `HUB_CONTROLLER_RESIDUAL_BOUND.md`
- `RELATIVISTIC_ELASTICITY_SCOPE_NOTE.md`

---

## 6. Normalized free-space storage coefficient survives support correction

At leading quadrupole order,

$$
\Sigma_{AB}^R
\propto q_{01,A}q_{01,B},
$$

while

$$
\sqrt{\kappa_{g,A}\kappa_{g,B}}
\propto|q_{01,A}q_{01,B}|.
$$

Thus finite-spoke matrix-element factors cancel in the normalized storage amplitude.

The wave-zone storage fraction remains

$$
\boxed{
\eta_{\rm store}
=\frac{25\mathcal O}{16(kR)^2}
}
$$

at leading compact-source quadrupole order.

The **absolute receiver loading rate** still uses the corrected receiver linewidth:

$$
\boxed{
\kappa_\Delta
=\eta_{\rm store}\kappa_{g,B}(q_B).
}
$$

Read:

- `FINITE_SPOKE_STORAGE_INVARIANCE.md`
- `EXPLICIT_FOUR_MASS_SOURCE_RECEIVER_LINK.md`

---

## 7. Passive source is now the primary emission benchmark

After preparation, remove active control and let the source oscillator decay freely.

Let

$$
\boxed{
\kappa_A
=\kappa_{g,A}+\kappa_{\ell,A}.}
$$

The normalized natural source temporal mode is

$$
\boxed{
f_A(t)
=\sqrt{\kappa_A}e^{-\kappa_A t/2},
\qquad t\ge0.}
$$

For vacuum ordinary source-loss ports, the fraction of initial source-mode amplitude power reaching the gravitational output is

$$
\boxed{
\eta_g
=\frac{\kappa_{g,A}}{\kappa_A}.}
$$

The gravitational branch distance is

$$
\boxed{
N_\Delta^{(g)}
=\eta_gN_{\Delta,m}(0).}
$$

If the source is purely gravitationally damped,

$$
\eta_g=1,
$$

and the full initial mechanical branch record is eventually emitted gravitationally.

Canonical note:

- `PASSIVE_CONSERVED_EXPONENTIAL_SOURCE.md`

---

## 8. Thermal passive source channel

If nongravitational source bath $j$ has rate $\kappa_j$ and occupation $\bar n_j$, define

$$
\Gamma_{{\rm th},A}
=\sum_j\kappa_j\bar n_j.
$$

Projecting the gravitational output onto the matched exponential temporal mode gives the exact phase-insensitive source channel

$$
\boxed{
\Phi_A
=\Phi_{\eta_g,m_A},
}

with

$$
\boxed{
m_A
=\frac{\kappa_{g,A}\Gamma_{{\rm th},A}}
{\kappa_A^2}
=\eta_g\frac{\Gamma_{{\rm th},A}}{\kappa_A}.}
$$

The source emission stage itself is non-EB iff

$$
\boxed{
\Gamma_{{\rm th},A}<\kappa_A.}
$$

Canonical note:

- `THERMAL_PASSIVE_SOURCE_CHANNEL.md`

---

## 9. Receiver channel for a normalized incident mode

For receiver total linewidth $\kappa_B$, useful loading rate $\kappa_\Delta$, and normalized source waveform $f_A$,

$$
\boxed{
\tau_f(t)
=\kappa_\Delta
\left|
\int_0^t ds\,
 e^{-\kappa_B(t-s)/2}f_A(s)
\right|^2.
}
$$

Receiver vacuum-output occupation is

$$
\boxed{
m_B(t)
=n_0e^{-\kappa_Bt}
+\frac{\Gamma_{{\rm th},B}}{\kappa_B}
(1-e^{-\kappa_Bt}).}
$$

For the exponential source and $\kappa_A\ne\kappa_B$,

$$
\boxed{
\tau_{\exp}(t)
=
\frac{4\kappa_\Delta\kappa_A}
{(\kappa_B-\kappa_A)^2}
\left(
 e^{-\kappa_A t/2}
-e^{-\kappa_Bt/2}
\right)^2.
}
$$

For matched linewidths $\kappa_A=\kappa_B=\kappa$,

$$
\boxed{
\tau_{\exp}(t)
=\kappa_\Delta\kappa t^2e^{-\kappa t},}
$$

with maximum

$$
\boxed{
\tau_{\exp}^{\max}
=4e^{-2}\frac{\kappa_\Delta}{\kappa}
\simeq0.541341\frac{\kappa_\Delta}{\kappa}.}
$$

---

## 10. Correct full source→receiver Gaussian channel

The receiver-local condition is not the same as the end-to-end condition unless the source emission stage is ideal.

Compose

$$
\Phi_A=\Phi_{\eta_g,m_A}
$$

with

$$
\Phi_B(t)=\Phi_{\tau_f(t),m_B(t)}.
$$

Then

$$
\boxed{
\tau_{A\to B}(t)
=\eta_g\tau_f(t),}
$$

$$
\boxed{
m_{A\to B}(t)
=m_B(t)+\tau_f(t)m_A.}
$$

Therefore the full passive source→receiver channel is non-entanglement-breaking iff

$$
\boxed{
\eta_g\tau_f(t)
>
m_B(t)+\tau_f(t)m_A.}
$$

Equivalently,

$$
\boxed{
\eta_g
\left(1-rac{\Gamma_{{\rm th},A}}{\kappa_A}\right)
\tau_f(t)
>m_B(t).}
$$

This is now the canonical end-to-end capability condition.

Read:

- `PASSIVE_END_TO_END_CHANNEL.md`
- `THERMAL_PASSIVE_SOURCE_CHANNEL.md`

---

## 11. Operational causality: compare release versus hold

Do not claim that all source–receiver correlations vanish outside the light cone.

Use two complete histories that are identical before a localized intervention:

### Control

Hold the prepared static branch state.

### Signal

Smoothly release the plus mode into passive free evolution.

Pre-existing static gravitational dressing or vacuum correlations are common to both histories.

The causal observable is **receiver dependence on the release intervention**.

Before causal contact the source-input→receiver map is a replacer:

$$
\boxed{
\tau_{A\to B}=0.}
$$

The causal clock starts when release begins, not when the earlier branch state was prepared.

Read:

- `CAUSAL_SOURCE_INTERVENTION_PROTOCOL.md`

---

## 12. Explicit $C^2$ release bridge

Let release duration be $T_r$ and define

$$
\boxed{x=t/T_r,\qquad r=\omega T_r.}
$$

Signal minus held-control displacement during release:

$$
\boxed{
\frac{\delta u(t)}{u_0}
=-\frac{r^2}{2}x^3(1-x)^2.}
$$

It satisfies

$$
\delta u(0)=\dot{\delta u}(0)=\ddot{\delta u}(0)=0,
$$

and

$$
\delta u(T_r)=\dot{\delta u}(T_r)=0,
$$

$$
\ddot{\delta u}(T_r)=-\omega^2u_0.
$$

Thus it joins continuously onto free oscillation from the turning point and makes the signal-control quadrupole $C^2$.

Its Fourier tail behaves as

$$
|\widetilde Q(\omega')|=O(\omega'^{-4}),
$$

so both ideal graviton-number and radiated-energy integrals are ultraviolet finite.

Canonical note:

- `SMOOTH_RELEASE_TO_PASSIVE_SOURCE.md`

---

## 13. Release transient is negligible in the resonant channel

The release acceleration is

$$
\boxed{
\ddot{\delta u}(t)
=-u_0\omega^2P(x),
}
$$

with

$$
\boxed{P(x)=3x-12x^2+10x^3.}
$$

Define

$$
\boxed{J(r)=\int_0^1P(x)e^{irx}dx.}
$$

The bridge has two exact moment cancellations:

$$
\boxed{\int_0^1P(x)dx=0,}
$$

$$
\boxed{\int_0^1xP(x)dx=0.}
$$

Therefore

$$
\boxed{
J(r)
=-\frac{r^2}{120}
-i\frac{r^3}{210}
+O(r^4).}
$$

For a high-Q passive source,

$$
\boxed{
\frac{|A_{\rm release}|}{|A_{\rm tail}|}
\simeq
\frac{r|J(r)|}{Q_A}.}
$$

For $0\le r\le1$,

$$
\boxed{
\frac{|A_{\rm release}|}{|A_{\rm tail}|}
\le
\frac{e}{120}
\frac{r^3}{Q_A}
\simeq0.02265\frac{r^3}{Q_A}.}
$$

Examples at $r\le1$:

- $Q_A=10^3$: contamination $<2.27\times10^{-5}$;
- $Q_A=10^6$: contamination $<2.27\times10^{-8}$.

Thus the short local release is negligible in the resonant receiver band while still fixing the causal origin of the later passive signal.

Read:

- `RELEASE_TRANSIENT_RESONANT_SUPPRESSION.md`

---

## 14. Retarded capability front

If the release begins at source time $t_s$, the earliest possible receiver dependence begins at

$$
\boxed{t_s+R/c.}
$$

Define receiver-local time after earliest arrival by $t$.

The thermal passive source-resolved capability time is

$$
\boxed{
T_{A\to B}^{\rm cap}(R)
=t_s+\frac Rc
+
\inf\left\{
t>0:
\eta_g\tau_f(t)
>
m_B(t)+\tau_f(t)m_A
\right\}.}
$$

This is the canonical quantum-capability front.

It is a statement about dependence on the local release/source input, not the absence of all pre-existing field correlations.

---

## 15. Active $\sin^4$ protocol is secondary

The actively shaped compact pulse still has useful properties and a stronger receiver waveform-overlap coefficient:

$$
S_{4,*}\simeq0.7980213
$$

versus the matched passive exponential coefficient

$$
4e^{-2}\simeq0.541341.
$$

But the active pulse requires a controller during the entire emission waveform.

Use it only as an engineered performance benchmark with the controller residual bound explicit.

The passive exponential protocol is the primary conservation benchmark.

---

## 16. Current paper claim candidate

If a dedicated literature audit finds no equivalent end-to-end construction, the possible paper contribution is:

> **An explicit conserved finite-support quantum quadrupole source, a local smooth release intervention, its passive emitted gravitational temporal mode including source thermal branching, retarded wave-zone transfer to a noisy resonant receiver, and the resulting source-resolved finite non-entanglement-breaking interval with explicit source/actuator error controls.**

Do not claim novelty for

- gravity-mediated entanglement;
- gravity as a quantum channel;
- Gaussian EB thresholds;
- rank-two or binary-coherent Gaussian survival theorems;
- generic no-signalling outside the light cone.

---

## 17. Exact next tasks

1. **Fresh literature audit** for the exact conserved-source→graviton-mode→noisy-receiver chain, including release/hold causality.
2. Build `PAPER_CORE_V5_PASSIVE_SOURCE.md` around the passive source, thermal source channel, and source-resolved EB condition.
3. Optionally evaluate the exact finite-bandwidth receiver convolution of the release bridge; the current high-Q bound is already strong.
4. Audit preparation/dressing literature to ensure the release-versus-hold framing is standard and gauge-safe enough for the intended perturbative calculation.
5. Decide whether the explicit $O(\beta^2)$ finite-source coefficient is needed or the current error-budget statement is sufficient.
