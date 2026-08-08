# Passive End-to-End Source→Receiver Gaussian Channel

**Date:** 2026-08-07  
**Status:** **SOURCE-RESOLVED CHANNEL CORRECTION — SOURCE BRANCHING LOSS MULTIPLIES THE RECEIVER TRANSFER PARAMETER**

## 1. Why the receiver-local channel is not yet end to end

The receiver calculation uses a normalized incident gravitational temporal mode and asks whether the map

$$
\text{incident graviton mode}
\to
\text{receiver oscillator}
$$

is non-entanglement-breaking.

Its phase-insensitive Gaussian parameters are

$$
\tau_f(t)
$$

and

$$
m(t).
$$

The local receiver condition is

$$
\tau_f(t)>m(t).
$$

But a source-resolved experiment begins with a **mechanical source mode**, not an already normalized graviton mode.

If the source loses branch information into nongravitational environments before emission, the full source→receiver map is weaker.

---

## 2. Passive source as a pure-loss splitter

For the free source mode let

$$
\kappa_A
=\kappa_{g,A}+\kappa_{\ell,A}.
$$

Assume for the canonical benchmark that the source loss environments begin in vacuum.

The normalized gravitational output mode receives the fraction

$$
\boxed{
\eta_g
=\frac{\kappa_{g,A}}{\kappa_A}
}
$$

of the source-mode amplitude power.

Thus the map

$$
a_A(0)\to b_g[f_A]
$$

is a pure-loss channel

$$
\boxed{\mathcal L_{\eta_g}.}
$$

At the coherent-state level,

$$
|\alpha\rangle_A
\to
|\sqrt{\eta_g}\alpha\rangle_g
\otimes
|\sqrt{1-\eta_g}\alpha\rangle_\ell.
$$

---

## 3. Receiver channel

Let

$$
\Phi_{\tau_f(t),m(t)}
$$

be the phase-insensitive Gaussian map from the normalized incident gravitational mode to the receiver oscillator at receiver-local time $t$ after causal arrival.

The coherent transfer parameter is

$$
\tau_f(t)
=\kappa_\Delta
\left|
\int_0^t ds\,
 e^{-\kappa_B(t-s)/2}f_A(s)
\right|^2.
$$

The vacuum-output occupation is

$$
m(t)
=n_0e^{-\kappa_Bt}
+\frac{\Gamma_{\rm th}}{\kappa_B}
(1-e^{-\kappa_Bt}).
$$

The geometric free-space storage factor is already contained in

$$
\kappa_\Delta
=\eta_{\rm store}\kappa_{g,B}.
$$

Do not insert $\eta_{\rm store}$ a second time.

---

## 4. Gaussian channel composition

The complete passive source→receiver channel is

$$
\boxed{
\Phi_{A\to B}(t)
=
\Phi_{\tau_f(t),m(t)}
\circ
\mathcal L_{\eta_g}.
}
$$

A pure-loss channel of transmissivity $\eta_g$ scales coherent amplitude by

$$
\sqrt{\eta_g}.
$$

Therefore the composite coherent transfer parameter is

$$
\boxed{
\tau_{A\to B}(t)
=\eta_g\tau_f(t).
}
$$

For vacuum source-loss environments, the pre-loss stage sends vacuum to vacuum and adds no thermal occupation to the receiver vacuum-output state.

Hence

$$
\boxed{
m_{A\to B}(t)=m(t).}
$$

The full source→receiver Gaussian channel is therefore

$$
\boxed{
\Phi_{A\to B}(t)
=\Phi_{\eta_g\tau_f(t),\,m(t)}
}
$$

in the repository convention.

---

## 5. Correct end-to-end entanglement-breaking condition

For a phase-insensitive Gaussian channel,

$$
\Phi_{\tau,m}\text{ is non-EB}
\iff
\tau>m.
$$

Therefore the **source-resolved** passive channel is non-EB iff

$$
\boxed{
\eta_g\tau_f(t)>m(t).
}
$$

Equivalently,

$$
\boxed{
\frac{\kappa_{g,A}}{\kappa_A}
\tau_f(t)
>m(t).
}
$$

This is stricter than the receiver-local condition whenever

$$
\kappa_{\ell,A}>0.
$$

---

## 6. Physical interpretation

There are three conceptually distinct losses:

### source branching loss

$$
\eta_g=\kappa_{g,A}/\kappa_A;
$$

### free-space / receiver geometric coupling

contained in

$$
\kappa_\Delta
=\eta_{\rm store}\kappa_{g,B};
$$

### receiver thermal/noise occupation

$$
m(t).
$$

Only after all three are included does one have an end-to-end channel from the prepared source mode to the receiver.

---

## 7. Matched passive exponential source and receiver

For the exponential source waveform

$$
f_A(t)=\sqrt{\kappa_A}e^{-\kappa_A t/2}
$$

and matched linewidths

$$
\kappa_A=\kappa_B=\kappa,
$$

the receiver transfer is

$$
\tau_{\exp}(t)
=\kappa_\Delta\kappa t^2e^{-\kappa t}.
$$

The maximum occurs at

$$
t_*=2/\kappa
$$

with

$$
\tau_{\exp}^{\max}
=4e^{-2}
\frac{\kappa_\Delta}{\kappa}.
$$

Thus the full end-to-end maximum is

$$
\boxed{
\tau_{A\to B}^{\max}
=4e^{-2}
\frac{\kappa_{g,A}}{\kappa}
\frac{\kappa_\Delta}{\kappa}.
}
$$

The two factors have a clear interpretation:

$$
\frac{\kappa_{g,A}}{\kappa}
$$

is the gravitational branching ratio of the source, while

$$
\frac{\kappa_\Delta}{\kappa}
$$

is the receiver's normalized useful loading strength.

---

## 8. Fully gravitational source

If the source has no nongravitational damping,

$$
\boxed{
\kappa_A=\kappa_{g,A},
}
$$

so

$$
\boxed{\eta_g=1.}
$$

Then the source-resolved and receiver-local capability conditions coincide:

$$
\boxed{
\tau_f(t)>m(t).
}
$$

This is the cleanest passive benchmark.

Its disadvantage is the enormous emission time

$$
1/\kappa_{g,A}.
$$

---

## 9. Nongravitational broadening tradeoff

Suppose one tries to shorten the passive source pulse by increasing

$$
\kappa_{\ell,A}.
$$

Then

$$
\kappa_A
$$

increases, but

$$
\eta_g
=\frac{\kappa_{g,A}}{\kappa_A}
$$

decreases.

At fixed receiver transfer parameter $\tau_f$, the end-to-end coherent transfer is reduced proportionally.

This gives a source-level no-free-lunch relation:

> Passive pulse broadening by ordinary damping makes the source faster only by diverting branch information away from gravity.

---

## 10. Stationary thermal receiver threshold

For a stationary thermal receiver,

$$
m(t)=n_{\rm th}.
$$

At matched passive linewidths the source→receiver channel has a non-EB interval iff

$$
\boxed{
n_{\rm th}
<4e^{-2}
\frac{\kappa_{g,A}}{\kappa}
\frac{\kappa_\Delta}{\kappa}.
}
$$

For a fully gravitational source,

$$
\kappa=\kappa_{g,A},
$$

this reduces to

$$
\boxed{
n_{\rm th}
<4e^{-2}
\frac{\kappa_\Delta}{\kappa}.
}
$$

---

## 11. Correct retarded capability time

Restoring source–receiver delay, define

$$
\boxed{
T_{A\to B}^{\rm cap}(R)
=
\frac Rc
+
\inf\left\{
t>0:
\eta_g\tau_f(t)>m(t)
\right\}.
}
$$

For a finite capability interval, define the closing time similarly from the second crossing.

This is the correct passive **source-resolved** causal front.

The older receiver-local front omitted the source branching factor because it took the normalized incident gravitational mode as the channel input.

Both are valid; they answer different questions.

---

## 12. Binary coherent source certification

Let the initial source oscillator be entangled with a qubit reference through coherent branches

$$
|\pm\alpha_0\rangle_A.
$$

The overall passive channel is phase insensitive with parameters

$$
\tau_{A\to B}(t)
=\eta_g\tau_f(t),
$$

$$
m_{A\to B}(t)=m(t).
$$

Therefore the known binary-coherent survival result implies NPT precisely when

$$
\boxed{
\eta_g\tau_f(t)>m(t).
}
$$

The repository's compact $2\times2$ PT witness can be used as a convenient finite diagnostic, but its generic theorem content is prior art.

---

## 13. Finite-spoke factors

The source branching ratio uses

$$
\kappa_{g,A}(q_A)
=
\kappa_{g,A}^{\rm end}
\mathcal C_\kappa(q_A).
$$

The receiver loading uses

$$
\kappa_\Delta(q_B)
=\eta_{\rm store}
\kappa_{g,B}^{\rm end}
\mathcal C_\kappa(q_B).
$$

Thus a broadened matched source–receiver setup contains explicit finite-support factors in both source and receiver rates.

For $q_A,q_B\ll1$ they remain controlled

$$
1+O(q_A^2)+O(q_B^2).
$$

---

## 14. Adversarial consequence for the paper

The paper should distinguish explicitly between

### Receiver-local quantum capability

Input is an already normalized incoming graviton mode:

$$
\tau_f(t)>m(t).
$$

### Full passive source→receiver quantum capability

Input is the prepared mechanical source mode:

$$
\boxed{
\eta_g\tau_f(t)>m(t).
}
$$

The second is the stronger and more source-resolved statement.

This distinction is likely essential for an end-to-end paper.

---

## 15. Next extension

If source loss baths are thermally occupied rather than vacuum, the source→gravitational-mode stage is no longer pure loss. The next generalization would calculate its added noise and propagate it through the same channel composition.

For the cleanest Gedanken benchmark, keep the passive source loss channels in vacuum or set

$$
\kappa_{\ell,A}=0.
$$
