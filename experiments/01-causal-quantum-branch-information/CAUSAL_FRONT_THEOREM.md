# Candidate Theorem — Causal Quantum-Front Speed Limit

**Timestamp:** 2026-08-07 16:21 EDT  
**Status:** Paper-candidate theorem within an explicit Markov weak-cat receiver model; novelty unverified

---

## 1. Model assumptions

The theorem below is intentionally narrow. It assumes:

1. **Source branch qubit.** The source has balanced alternatives $|L\rangle,|R\rangle$.
2. **Weak branch encoding.** To first nontrivial order, the source branch difference is encoded in one normalized incoming bosonic mode as
   $$
   |+\rangle|0\rangle+a|-\rangle|1_f\rangle+O(a^2).
   $$
3. **Relativistic causality.** The source-controlled mode has no support at the receiver before $t_0=R/c$.
4. **Linear Markov receiver.** One receiver mode $c$ obeys
   $$
   \dot c
   =-\frac{\kappa_{\rm tot}}2c
   +\sqrt{\kappa_\Delta}\,b_\Delta^{\rm in}
   +\sum_a\sqrt{\kappa_a}\,b_a^{\rm in},
   $$
   where $\kappa_\Delta$ is the coupling to the source-matched mode and the $a$ ports are uncontrolled channels.
5. **Stationary thermal floor.** Uncontrolled port $a$ has mean occupation $\bar n_a$, and the receiver is stationary before causal arrival.
6. **Normalized source wavepacket.** Its temporal envelope satisfies
   $$
   \int_0^\infty d\tau\,|f(\tau)|^2=1.
   $$
7. **Weak-cat NPT criterion.** For the resulting phase-insensitive Gaussian receiver channel, the source-receiver state is NPT to leading nontrivial order iff the coherent signal transmissivity exceeds the output thermal occupation.

Define

$$
\kappa_{\rm tot}
=\kappa_\Delta+\sum_a\kappa_a,
$$

and

$$
\boxed{
\Gamma_{\rm th}
=\sum_a\bar n_a\kappa_a.
}
$$

---

## 2. Theorem

### Causal quantum-front speed limit

Under assumptions 1--7, no normalized source wavepacket can produce source-receiver NPT entanglement before

$$
\boxed{
T_{\rm NPT}^{\min}
=
\frac Rc+
\frac1{\kappa_{\rm tot}}
\ln\left[
\frac{\kappa_\Delta}
{\kappa_\Delta-\Gamma_{\rm th}}
\right]
}
$$

provided

$$
\boxed{
\kappa_\Delta>\Gamma_{\rm th}.
}
$$

If

$$
\boxed{
\kappa_\Delta\le\Gamma_{\rm th},
}
$$

then no source-receiver NPT front exists at any finite time within the model.

The lower bound is tight: for every admissible parameter set above threshold, a time-reversed exponential receiver-matched input saturates it.

---

## 3. Proof

Measure time after causal arrival,

$$
\tau=t-R/c.
$$

The receiver's source-controlled branch displacement is proportional to

$$
\sqrt{\kappa_\Delta}
\int_0^\tau ds\,
e^{-\kappa_{\rm tot}(\tau-s)/2}f(s).
$$

Define the corresponding coherent transfer coefficient

$$
\eta_f(\tau)
=\kappa_\Delta
\left|
\int_0^\tau ds\,
e^{-\kappa_{\rm tot}(\tau-s)/2}f(s)
\right|^2.
$$

By Cauchy--Schwarz,

$$
\eta_f(\tau)
\le
\kappa_\Delta
\left[
\int_0^\tau ds\,
e^{-\kappa_{\rm tot}(\tau-s)}
\right]
\left[
\int_0^\tau ds\,|f(s)|^2
\right].
$$

Since the complete source mode is normalized,

$$
\int_0^\tau ds\,|f(s)|^2\le1.
$$

Therefore

$$
\boxed{
\eta_f(\tau)
\le
\frac{\kappa_\Delta}{\kappa_{\rm tot}}
\left(1-e^{-\kappa_{\rm tot}\tau}\right).
}
$$

The stationary receiver thermal occupation is

$$
\boxed{
 m_*
=\frac{\Gamma_{\rm th}}{\kappa_{\rm tot}}.
}
$$

The weak-cat NPT condition is

$$
\eta_f(\tau)>m_*.
$$

Hence a necessary condition at time $\tau$ is

$$
\kappa_\Delta
\left(1-e^{-\kappa_{\rm tot}\tau}\right)
>\Gamma_{\rm th}.
$$

If $\kappa_\Delta\le\Gamma_{\rm th}$, the left side never exceeds the right side, proving the no-front statement.

If $\kappa_\Delta>\Gamma_{\rm th}$, rearrange:

$$
e^{-\kappa_{\rm tot}\tau}
<1-\frac{\Gamma_{\rm th}}{\kappa_\Delta}.
$$

Thus

$$
\tau>
\frac1{\kappa_{\rm tot}}
\ln\left[
\frac{\kappa_\Delta}
{\kappa_\Delta-\Gamma_{\rm th}}
\right].
$$

Adding the causal delay $R/c$ proves the lower bound.

---

## 4. Saturating waveform

At a chosen target time $\tau_*$, equality in Cauchy--Schwarz is achieved by

$$
\boxed{
f_{\rm opt}(s)
=
\sqrt{
\frac{\kappa_{\rm tot}}
{1-e^{-\kappa_{\rm tot}\tau_*}}
}
\,
e^{-\kappa_{\rm tot}(\tau_*-s)/2}
\Theta(s)\Theta(\tau_*-s).
}
$$

This is the time reverse of the receiver's free ringdown over the available interval.

It is normalized:

$$
\int_0^{\tau_*}ds\,|f_{\rm opt}(s)|^2=1.
$$

Therefore the speed limit is not merely a loose inequality; it is achievable within the ideal model.

---

## 5. Quantum excess fraction

Define

$$
\boxed{
\epsilon_Q
=1-
\frac{\Gamma_{\rm th}}
{\kappa_\Delta}.
}
$$

For a quantum-capable receiver,

$$
0<\epsilon_Q\le1.
$$

The theorem becomes

$$
\boxed{
T_{\rm NPT}^{\min}-R/c
=-\frac1{\kappa_{\rm tot}}\ln\epsilon_Q.
}
$$

Thus the earliest possible entanglement front is controlled by two timescales:

1. propagation time $R/c$;
2. receiver quantum build time $-\kappa_{\rm tot}^{-1}\ln\epsilon_Q$.

---

## 6. Corollary: double critical slowing

As the receiver approaches the thermal entanglement-breaking boundary,

$$
\epsilon_Q\to0^+,
$$

so

$$
\boxed{
T_{\rm NPT}^{\min}-R/c
\to\infty
}
$$

logarithmically.

At the saturating front,

$$
\frac{d\eta_{\max}}{d\tau}
=\kappa_\Delta e^{-\kappa_{\rm tot}\tau}.
$$

Since

$$
e^{-\kappa_{\rm tot}\tau_*}=\epsilon_Q,
$$

$$
\boxed{
\left.
\frac{d\eta_{\max}}{d\tau}
\right|_{\tau_*}
=\kappa_\Delta\epsilon_Q.
}
$$

Thus the front both

- arrives increasingly late;
- grows increasingly slowly after arrival.

---

## 7. Gravitational corollary

For a source-receiver graviton mode overlap $\mathcal O_{SB}$ and receiver total graviton linewidth $\kappa_g$,

$$
\boxed{
\kappa_\Delta
=\mathcal O_{SB}\kappa_g.
}
$$

Therefore

$$
\boxed{
\epsilon_Q
=1-
\frac{\Gamma_{\rm th}}
{\mathcal O_{SB}\kappa_g}.
}
$$

The gravitational NPT front obeys

$$
\boxed{
T_{\rm NPT}^{\min}
=
\frac Rc-
\frac1{\kappa_{\rm tot}}
\ln\left[
1-
\frac{\Gamma_{\rm th}}
{\mathcal O_{SB}\kappa_g}
\right]
}
$$

when

$$
\mathcal O_{SB}\kappa_g>\Gamma_{\rm th}.
$$

The source tensor orientation, angular access, temporal/spectral matching, gravitational oscillator strength, and thermal receiver noise therefore enter one causal formula.

---

## 8. What the theorem does NOT say

The theorem is not a universal statement about all quantum gravity models.

It does **not** cover automatically:

- non-Markovian receivers;
- strongly nonlinear receivers;
- arbitrary non-Gaussian thermal environments;
- active/inverted receivers;
- finite source cats beyond the weak-cat NPT criterion;
- gravitational dressing subtleties not captured by the operational input mode;
- pre-existing source-receiver correlations.

It also does not claim that entanglement itself is a locally propagating observable. The causal statement concerns a controlled source operation and a receiver channel whose source-dependent input has no support before $R/c$.

---

## 9. Why this is stronger than a retardation statement

Classical relativity already predicts that a controlled gravitational disturbance cannot arrive before $R/c$.

The theorem adds a second restriction:

> **even after the gravitational disturbance is allowed to arrive, quantum entanglement cannot appear until the receiver has accumulated enough matched coherent mode weight to cross its thermal entanglement-breaking boundary.**

Thus

$$
\boxed{
\text{signal causality}
\neq
\text{quantum-information latency}.
}
$$

---

## 10. Current novelty status

A preliminary search found related literature on

- entanglement-breaking times of dissipative quantum channels;
- quantum speed limits for channels becoming entanglement breaking;
- thermal attenuator thresholds;
- gravity-mediated quantum communication.

The exact reverse problem formulated here—**earliest entanglement generation after retarded arrival, optimized over all normalized receiver waveforms**—was not located in the targeted search.

This is not sufficient to claim novelty. The theorem should currently be labeled

> **candidate original application / synthesis, novelty unverified.**

---

## 11. Paper-level role

If the novelty check survives, this theorem could serve as the mathematical spine of Experiment 01:

1. derive a source branch-difference gravitational mode;
2. prove it has no receiver support before $R/c$;
3. derive the matched receiver rates;
4. invoke the theorem to predict the earliest possible NPT front;
5. compare classicalized, thermal, and coherent gravitational mediation.

The result would turn the Gedankenexperiment from a qualitative question about whether gravity can carry quantum information into a quantitative prediction for **when a distant receiver can first become quantum-correlated with the source.**