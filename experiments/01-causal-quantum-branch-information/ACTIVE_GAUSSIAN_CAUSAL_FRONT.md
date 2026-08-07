# Exact Causal Front for Stable Active Phase-Insensitive Gaussian Receivers

**Timestamp:** 2026-08-07 17:16 EDT  
**Status:** Exact within the stable linear Markov / gauge-covariant Gaussian receiver model; uses `PHASE_INSENSITIVE_GAUSSIAN_BINARY_PROBE_THEOREM.md`.

## 1. Motivation

The passive receiver theorem leaves an obvious loophole:

> Could an active or inverted receiver amplify the gravitational branch mode and make the NPT front substantially earlier?

For a **phase-insensitive linear Gaussian receiver**, the answer is constrained by the spontaneous noise required by the gain process.

The general binary coherent probe theorem gives a simple instantaneous criterion for any gauge-covariant Gaussian channel:

$$
\boxed{
\text{binary coherent hybrid output NPT}
\iff
\tau(t)>m(t),
}
$$

where $\tau$ is coherent intensity gain/transmission from the selected branch mode and $m$ is the output occupation produced by vacuum input.

---

## 2. Stable active receiver model

Let the receiver mode obey

$$
\boxed{
\dot c
=-\frac{\kappa_{\rm eff}}2c
+\sqrt{\kappa_\Delta}\,b_\Delta^{\rm in}
+\sum_j\sqrt{\kappa_j^-}\,b_j^{\rm in}
+\sum_k\sqrt{\gamma_k^+}\,d_k^{{\rm in}\dagger}.
}
$$

Here

- $\kappa_\Delta$ is coupling to the desired source branch-difference mode;
- $\kappa_j^-$ are ordinary damping/loss ports;
- $\gamma_k^+$ are phase-insensitive gain/heating ports.

The net stable damping is

$$
\boxed{
\kappa_{\rm eff}
=\kappa_\Delta+\sum_j\kappa_j^-
-\sum_k\gamma_k^+
>0.
}
$$

Let the ordinary bath occupations be $\bar n_j$ and the gain-bath occupations be $\bar n_k^+$.

---

## 3. Coherent source-mode transfer

For a normalized incoming branch waveform $f(t)$ beginning after causal arrival,

$$
\int_0^\infty dt\,|f(t)|^2=1,
$$

the coherent transfer parameter by time $\tau=t-R/c$ is

$$
\boxed{
\tau_f(\tau)
=\kappa_\Delta
\left|
\int_0^\tau ds\,
e^{-\kappa_{\rm eff}(\tau-s)/2}f(s)
\right|^2.
}
$$

Cauchy-Schwarz gives the waveform-independent ceiling

$$
\boxed{
\tau_f(\tau)
\le
\frac{\kappa_\Delta}{\kappa_{\rm eff}}
\left(1-e^{-\kappa_{\rm eff}\tau}\right).
}
$$

This can exceed unity when the active receiver is sufficiently close to threshold, corresponding to an amplifying effective channel.

The bound is saturated by the time-reversed net receiver ringdown kernel.

---

## 4. Vacuum-output occupation

The branch-independent occupation obeys

$$
\frac{d\langle n\rangle}{dt}
=-\kappa_{\rm eff}\langle n\rangle
+\Gamma_+,
$$

where

$$
\boxed{
\Gamma_+
=\sum_j\kappa_j^-\bar n_j
+\sum_k\gamma_k^+(\bar n_k^++1).
}
$$

The $+1$ in every gain port is the unavoidable spontaneous quantum-noise contribution.

For a stationary receiver,

$$
\boxed{
m_*=\frac{\Gamma_+}{\kappa_{\rm eff}}.}
$$

This is exactly the vacuum-output occupation parameter appearing in the general Gaussian binary-probe theorem.

---

## 5. Exact active NPT condition

For **every finite nontrivial binary coherent branch encoding**, the receiver output is NPT iff

$$
\tau_f(\tau)>m_*.
$$

Using the waveform ceiling, an NPT front can exist only if

$$
\boxed{
\kappa_\Delta>\Gamma_+.
}
$$

Thus the gain process does not appear merely through a larger coherent response. Every phase-insensitive gain port contributes

$$
\gamma_k^+(\bar n_k^++1)
$$

to the classicalizing noise budget.

At zero gain-bath temperature,

$$
\boxed{
\Gamma_+\supset\gamma_k^+.
}
$$

Spontaneous amplifier noise is therefore unavoidable even at $T=0$.

---

## 6. Tight active causal-front law

If

$$
\kappa_\Delta>\Gamma_+,
$$

the earliest NPT front satisfies

$$
\boxed{
T_{\rm NPT}^{\min}
=
\frac Rc+
\frac1{\kappa_{\rm eff}}
\ln\left[
\frac{\kappa_\Delta}
{\kappa_\Delta-\Gamma_+}
\right].
}
$$

If

$$
\kappa_\Delta\le\Gamma_+,
$$

no finite binary coherent branch encoding can become NPT with the receiver within this stable Gaussian model.

The result has exactly the same functional form as the passive theorem, but

$$
\Gamma_{\rm th}
\longrightarrow
\Gamma_+
$$

includes both thermal loss noise and quantum-limited amplifier spontaneous noise.

---

## 7. Active quantum-excess parameter

Define

$$
\boxed{
\epsilon_Q^{\rm active}
=1-rac{\Gamma_+}{\kappa_\Delta}.
}
$$

Then

$$
\boxed{
T_{\rm NPT}^{\min}-R/c
=-\kappa_{\rm eff}^{-1}
\ln\epsilon_Q^{\rm active}.
}
$$

The receiver may have large classical gain while

$$
\epsilon_Q^{\rm active}\to0^+.
$$

In that limit the NPT front is pushed arbitrarily late.

---

## 8. Simple zero-temperature amplifier example

Take

- useful coupling $\kappa_\Delta$;
- one ordinary vacuum loss port $\kappa_0$;
- one zero-temperature gain port $\gamma$.

Then

$$
\kappa_{\rm eff}=\kappa_\Delta+\kappa_0-\gamma>0,
$$

and

$$
\Gamma_+=\gamma.
$$

The exact quantum-capability condition is

$$
\boxed{\kappa_\Delta>\gamma.}
$$

The earliest front is

$$
\boxed{
T_{\rm NPT}^{\min}-R/c
=
\frac{1}{\kappa_\Delta+\kappa_0-\gamma}
\ln\left(
\frac{\kappa_\Delta}{\kappa_\Delta-\gamma}
\right).
}
$$

As

$$
\gamma\to\kappa_\Delta^{-},
$$

the classical gain becomes large but the quantum front diverges logarithmically.

This is the phase-insensitive amplifier no-free-lunch statement in causal-front form.

---

## 9. Relation to active collective gravitational receivers

Known collectively excited matter models can show $N^2$ gravitational transition enhancement. That enhancement can increase $\kappa_\Delta$ if the collective transition is mode matched to the source.

However, activity also implies spontaneous transitions. In the Gaussian linearized description those appear as gain/noise rates $\gamma_k^+$ and enter $\Gamma_+$ with their vacuum $+1$ term.

Therefore the relevant question is not

$$
\text{How large is the collective gain?}
$$

but

$$
\boxed{
\text{How large is }\kappa_\Delta-\Gamma_+\text{?}
}
$$

A collective enhancement that multiplies useful absorption and spontaneous gravitational transitions by the same factor speeds the dynamics but does not automatically improve the dimensionless quantum excess.

---

## 10. Finite-strength witness

For branch-mode strength $N_\Delta$ and stationary $m_*>0$, the general exact three-element margin is

$$
\boxed{
\Lambda(\tau)
=\frac{N_\Delta}{m_*}
[\tau_f(\tau)-m_*].
}
$$

Under optimal waveform capture,

$$
\boxed{
\Lambda_{\max}(\tau)
=
\frac{N_\Delta}{\Gamma_+}
\left[
\kappa_\Delta(1-e^{-\kappa_{\rm eff}\tau})
-\Gamma_+
\right].
}
$$

Thus active gain cannot create a strong quantum certificate unless useful branch-mode coupling exceeds the full spontaneous-plus-thermal noise budget.

---

## 11. Scope

This theorem covers stable **phase-insensitive Gaussian** active receivers. It does not automatically apply to

- phase-sensitive noiseless quadrature amplification;
- heralded non-deterministic noiseless linear amplification;
- strongly nonlinear receivers;
- explicitly non-Gaussian active matter;
- unstable above-threshold oscillators.

These are separate loopholes requiring separate analysis.

## 12. Strongest next question

Phase-sensitive amplification can amplify one quadrature without the same half-quantum penalty. Determine whether a source branch-difference mode can be encoded and captured in one known quadrature so that a phase-sensitive receiver advances the causal NPT/certification front, or whether the need to preserve the full binary coherent-state overlap restores an equivalent quantum-noise cost.
