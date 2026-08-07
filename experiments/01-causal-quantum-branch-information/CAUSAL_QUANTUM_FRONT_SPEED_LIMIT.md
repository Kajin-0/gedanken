# Causal Quantum-Front Speed Limit

**Timestamp:** 2026-08-07 16:25 EDT  
**Status:** Active derivation for Experiment 01

This note converts the matched-receiver result into a waveform-independent bound. The result is an exact lower bound on how soon a stationary noisy receiver can become entangled with the source after the gravitational light cone arrives, within the Markov single-mode model.

---

## 1. General multiport receiver

Let the desired source-matched gravitational channel couple to the receiver memory at rate

$$
\kappa_\Delta.
$$

Let all other vacuum, gravitational, and material channels contribute rates $\kappa_a$. Define

$$
\boxed{
\kappa_{\rm tot}
=\kappa_\Delta+
\sum_a\kappa_a.
}
$$

The desired branch-difference input has normalized temporal envelope

$$
\int_{-\infty}^{\infty}dt\,|f(t)|^2=1.
$$

Measure time from causal arrival,

$$
\tau=t-R/c.
$$

---

## 2. Coherent capture from an arbitrary waveform

The branch-dependent receiver displacement is proportional to

$$
\sqrt{\kappa_\Delta}
\int_0^\tau ds\,
e^{-\kappa_{\rm tot}(\tau-s)/2}f(s).
$$

Therefore the coherent transfer coefficient is

$$
\boxed{
\eta_f(\tau)
=\kappa_\Delta
\left|
\int_0^\tau ds\,
e^{-\kappa_{\rm tot}(\tau-s)/2}f(s)
\right|^2.
}
$$

---

## 3. Cauchy–Schwarz speed bound

Cauchy–Schwarz gives

$$
\left|
\int_0^\tau ds\,
e^{-\kappa_{\rm tot}(\tau-s)/2}f(s)
\right|^2
\le
\left[
\int_0^\tau ds\,
e^{-\kappa_{\rm tot}(\tau-s)}
\right]
\left[
\int_0^\tau ds\,|f(s)|^2
\right].
$$

Since the entire incoming wavepacket is normalized,

$$
\int_0^\tau ds\,|f(s)|^2\le1.
$$

Hence

$$
\boxed{
\eta_f(\tau)
\le
\eta_{\max}(\tau)
=
\frac{\kappa_\Delta}{\kappa_{\rm tot}}
\left(1-e^{-\kappa_{\rm tot}\tau}
\right).
}
$$

This is a waveform-independent bound.

Equality is achievable in the ideal model by placing all available pulse norm in the interval $[0,\tau]$ with the time-reversed receiver kernel

$$
f_{\rm opt}(s)
\propto
e^{-\kappa_{\rm tot}(\tau-s)/2}.
$$

Thus the bound is tight.

---

## 4. Stationary thermal floor

Let uncontrolled channel $a$ have thermal occupation $\bar n_a$. Vacuum channels have $\bar n_a=0$.

Define the total thermal injection rate

$$
\boxed{
\Gamma_{\rm th}
=\sum_a\bar n_a\kappa_a.
}
$$

For a receiver stationary before the gravitational wave arrives, its branch-independent occupation is

$$
\boxed{
 m_*
=\frac{\Gamma_{\rm th}}
{\kappa_{\rm tot}}.
}
$$

The weak-cat source-receiver state can become NPT only when

$$
\eta_f(\tau)>m_*.
$$

---

## 5. Exact earliest NPT front

Because no waveform can exceed $\eta_{\max}$, NPT is impossible before

$$
\frac{\kappa_\Delta}{\kappa_{\rm tot}}
(1-e^{-\kappa_{\rm tot}\tau})
>
\frac{\Gamma_{\rm th}}
{\kappa_{\rm tot}}.
$$

Therefore a front exists only if

$$
\boxed{
\kappa_\Delta>\Gamma_{\rm th}.
}
$$

When it exists, every normalized input waveform obeys

$$
\boxed{
T_{\rm NPT}
\ge
\frac Rc+
\frac1{\kappa_{\rm tot}}
\ln\left[
\frac{\kappa_\Delta}
{\kappa_\Delta-\Gamma_{\rm th}}
\right].
}
$$

The time-reversed matched waveform saturates this inequality in the ideal Markov model.

Thus this is a **tight causal quantum-front speed limit** within the stated receiver class.

---

## 6. Quantum excess fraction

Define the dimensionless distance above the thermal entanglement-breaking boundary,

$$
\boxed{
\epsilon_Q
=1-
\frac{\Gamma_{\rm th}}{\kappa_\Delta}.
}
$$

The quantum regime has

$$
0<\epsilon_Q\le1.
$$

The optimized front law becomes

$$
\boxed{
T_{\rm NPT}^{\min}-\frac Rc
=-\frac1{\kappa_{\rm tot}}
\ln\epsilon_Q.
}
$$

This is one of the cleanest formulas produced by Experiment 01.

It says that the post-light-cone quantum delay is controlled entirely by

1. the receiver relaxation timescale $\kappa_{\rm tot}^{-1}$;
2. the fractional distance of the useful gravitational channel above the thermal classicalization boundary.

---

## 7. Critical slowing follows immediately

As

$$
\epsilon_Q\to0^+,
$$

$$
\boxed{
T_{\rm NPT}^{\min}-R/c
\sim
\kappa_{\rm tot}^{-1}
\ln(1/\epsilon_Q).
}
$$

The earliest possible quantum front therefore retreats logarithmically behind the relativistic signal front as the channel approaches entanglement breaking.

No pulse shaping can remove this divergence because the bound was optimized over all normalized waveforms.

---

## 8. Post-front growth rate uses the same excess

At the matched front,

$$
e^{-\kappa_{\rm tot}\tau_*}
=\epsilon_Q.
$$

Differentiate the optimal capture coefficient:

$$
\frac{d\eta_{\max}}{d\tau}
=\kappa_\Delta e^{-\kappa_{\rm tot}\tau}.
$$

At the front,

$$
\boxed{
\left.
\frac{d\eta_{\max}}{d\tau}
\right|_{\tau_*}
=
\kappa_\Delta\epsilon_Q
=
\kappa_\Delta-\Gamma_{\rm th}.
}
$$

Thus the same quantum excess that determines the logarithmic delay also determines how quickly the coherent branch transfer grows after the threshold.

For the weak-cat negativity at finite thermal floor $m_*>0$,

$$
\boxed{
\left.
\frac{d\mathcal N}{dt}
\right|_{T_{\rm NPT}^+}
=
\frac{N_\Delta}{4m_*}
\kappa_\Delta\epsilon_Q
+O(N_\Delta^2).
}
$$

This makes the earlier double critical slowing a single unified law.

---

## 9. Global history-witness speed limit

The global fidelity-history witness requires

$$
\eta_f>m_*+\frac12.
$$

Therefore a front exists only if

$$
\boxed{
\kappa_\Delta
>
\Gamma_{\rm th}+rac12\kappa_{\rm tot}.
}
$$

Equivalently,

$$
\boxed{
\kappa_\Delta
>
\sum_a(2\bar n_a+1)\kappa_a.
}
$$

When it exists,

$$
\boxed{
T_F
\ge
\frac Rc+
\frac1{\kappa_{\rm tot}}
\ln\left[
\frac{\kappa_\Delta}
{\kappa_\Delta-\Gamma_{\rm th}-\kappa_{\rm tot}/2}
\right].
}
$$

Again, the matched waveform saturates the ideal Markov bound.

---

## 10. Insert gravitational mode overlap

For source-receiver graviton mode overlap $\mathcal O_{SB}$,

$$
\kappa_\Delta
=\mathcal O_{SB}\kappa_g.
$$

Therefore the NPT speed limit becomes

$$
\boxed{
T_{\rm NPT}
\ge
\frac Rc+
\frac1{\kappa_{\rm tot}}
\ln\left[
\frac{\mathcal O_{SB}\kappa_g}
{\mathcal O_{SB}\kappa_g-\Gamma_{\rm th}}
\right].
}
$$

A causal entanglement front can exist only if

$$
\boxed{
\mathcal O_{SB}\kappa_g>\Gamma_{\rm th}.
}
$$

Thus source tensor alignment, aperture, temporal match, and thermal receiver noise all enter one compact causal bound.

---

## 11. Passive nonrelativistic corollary

For a passive nonrelativistic receiver,

$$
\kappa_g/\kappa_i
\lesssim
\mathfrak R_B
=
\frac23Q_B\mathcal C_B\beta_B^3.
$$

Therefore the useful-mode excess is bounded by

$$
\epsilon_Q
\le
1-
\frac{\Gamma_{\rm th}}
{\mathcal O_{SB}\mathfrak R_B\kappa_i}
$$

whenever the denominator exceeds $\Gamma_{\rm th}$.

This combines the passive receiver ceiling and the causal front law directly.

---

## 12. Relativistic QFT corollary

For a relativistic passive receiver there may be no universal absolute ceiling on $\kappa_g$, but KMS fixes the thermal noise associated with each uncontrolled absorptive channel.

The same front speed limit therefore remains valid with mode-resolved rates obtained from the smeared stress-energy spectral functions.

The bound is thus more general than the nonrelativistic quadrupole ceiling that motivated it.

---

## 13. Conceptual statement

> **The speed of a gravitational quantum-information front is not set by the speed of light alone. Light speed tells us when the first influence is allowed to arrive. After that, the receiver must coherently accumulate enough of the source's matched gravitational mode to rise above its thermal record floor. Even with the optimally shaped possible wavepacket, that takes a finite time. The exact delay is the receiver lifetime multiplied by the logarithm of the inverse distance from the entanglement-breaking boundary.**

---

## 14. Novelty discipline

Cauchy-Schwarz matched-filter bounds, Markov input-output theory, thermal entanglement-breaking thresholds, and pulse-shape optimization are established tools.

What may be distinctive is the **causal gravitational interpretation and combination**:

$$
\boxed{
T_{\rm NPT}^{\min}
=R/c-\kappa_{\rm tot}^{-1}\ln\epsilon_Q
}
$$

with

$$
\epsilon_Q
=1-\Gamma_{\rm th}/(\mathcal O_{SB}\kappa_g).
$$

A dedicated literature search is required before calling this a new quantum speed limit.

---

## 15. Immediate next step

Search specifically for existing results on entanglement-generation onset / quantum-channel front delays near entanglement-breaking thresholds. If no close prior result is found, formulate this as a candidate theorem with explicit assumptions and proof in the eventual paper.