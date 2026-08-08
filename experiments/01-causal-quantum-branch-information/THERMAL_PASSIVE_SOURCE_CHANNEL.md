# Thermal Passive Source→Graviton Output Channel

**Date:** 2026-08-07  
**Status:** **EXACT MARKOV MODE-MATCHED SOURCE CHANNEL — THERMAL SOURCE NOISE PROPAGATED END TO END**

## 1. Purpose

`PASSIVE_CONSERVED_EXPONENTIAL_SOURCE.md` treated nongravitational source losses as vacuum ports, giving a pure-loss source→graviton mode with transmissivity

$$
\eta_g=\kappa_{g,A}/\kappa_A.
$$

A natural objection is that realistic source damping baths may be thermally occupied.

Because the passive source is a linear Markov oscillator, the exact mode-matched source→gravitational-output channel can still be derived analytically.

---

## 2. Source Langevin equation

Let the source mode obey

$$
\boxed{
\dot a
=-\frac{\kappa_A}{2}a
-\sqrt{\kappa_g}\,b_g^{\rm in}
-\sum_j\sqrt{\kappa_j}\,b_j^{\rm in},
}
$$

with

$$
\boxed{
\kappa_A
=\kappa_g+\sum_j\kappa_j.
}
$$

The gravitational output is

$$
\boxed{
b_g^{\rm out}
=b_g^{\rm in}+\sqrt{\kappa_g}\,a.}
$$

Assume

- the gravitational input is vacuum;
- nongravitational bath $j$ has thermal occupation $\bar n_j$;
- the initial source mode $a(0)$ is the channel input.

---

## 3. Natural exponential temporal mode

Define

$$
\boxed{
f_A(t)
=\sqrt{\kappa_A}
 e^{-\kappa_A t/2},
\qquad t\ge0.}
$$

Then

$$
\int_0^\infty|f_A(t)|^2dt=1.
$$

Define matched input/output field modes

$$
B_j^{\rm in}
=\int_0^\infty dt\,
f_A(t)b_j^{\rm in}(t),
$$

$$
B_g^{\rm out}
=\int_0^\infty dt\,
f_A(t)b_g^{\rm out}(t).
$$

Also define branching fractions

$$
\boxed{
\eta_g=\frac{\kappa_g}{\kappa_A},
}
$$

$$
\boxed{
\eta_j=\frac{\kappa_j}{\kappa_A}.}
$$

They satisfy

$$
\eta_g+\sum_j\eta_j=1.
$$

---

## 4. Exact matched-mode transformation

Solving the source equation and projecting the gravitational output onto $f_A$ gives

$$
\boxed{
B_g^{\rm out}
=
\sqrt{\eta_g}\,a(0)
+(1-\eta_g)B_g^{\rm in}
-
\sum_j
\sqrt{\eta_g\eta_j}
B_j^{\rm in}.
}
$$

The overall signs depend on input-output convention and are irrelevant for the phase-insensitive noise parameters.

The coefficients satisfy

$$
\eta_g
+(1-\eta_g)^2
+\eta_g\sum_j\eta_j
=1.
$$

Hence

$$
[B_g^{\rm out},B_g^{{\rm out}\dagger}]=1.
$$

This is an exact canonical mode transformation.

---

## 5. Source→graviton Gaussian channel parameters

The coherent amplitude transfer from the initial source mode is

$$
\sqrt{\eta_g}.
$$

Therefore

$$
\boxed{
\tau_A=\eta_g.
}
$$

Now set the source input to vacuum. The gravitational input contribution is vacuum and adds no occupation. The thermal source baths contribute

$$
\sum_j
\eta_g\eta_j\bar n_j.
$$

Thus the vacuum-output mean occupation is

$$
\boxed{
m_A
=\eta_g
\sum_j\eta_j\bar n_j.
}
$$

Define the source thermal injection rate

$$
\boxed{
\Gamma_{{\rm th},A}
=\sum_j\kappa_j\bar n_j.
}
$$

Then

$$
\boxed{
m_A
=\frac{\kappa_g\Gamma_{{\rm th},A}}
{\kappa_A^2}.
}
$$

Equivalently,

$$
\boxed{
m_A
=\eta_g
\frac{\Gamma_{{\rm th},A}}{\kappa_A}.
}
$$

Therefore the passive source→graviton temporal mode is the phase-insensitive channel

$$
\boxed{
\Phi_A
=\Phi_{\eta_g,m_A}.
}
$$

---

## 6. Source-channel EB condition

For the repository convention,

$$
\Phi_{\tau,m}\text{ non-EB}
\iff
\tau>m.
$$

Hence the source→graviton output mode is non-EB iff

$$
\eta_g>m_A.
$$

Using the expression above,

$$
\eta_g
>
\eta_g
\frac{\Gamma_{{\rm th},A}}{\kappa_A}.
$$

For

$$
\eta_g>0,
$$

this becomes

$$
\boxed{
\Gamma_{{\rm th},A}<\kappa_A.
}
$$

Thus source thermalization can make the **emission channel itself** entanglement breaking before free-space propagation is considered.

---

## 7. Composition with the receiver

Let the normalized incident gravitational mode pass through the receiver channel

$$
\Phi_B(t)
=\Phi_{\tau_f(t),m_B(t)}.
$$

For phase-insensitive Gaussian channels written in the vacuum-output-occupation convention, composition obeys

$$
\tau_{\rm out}
=\tau_2\tau_1,
$$

and

$$
m_{\rm out}
=m_2+\tau_2m_1,
$$

because mean occupation transforms as

$$
\langle n\rangle
\to
\tau\langle n\rangle+m.
$$

Therefore

$$
\boxed{
\tau_{A\to B}(t)
=\eta_g\tau_f(t),
}
$$

and

$$
\boxed{
m_{A\to B}(t)
=m_B(t)+\tau_f(t)m_A.
}
$$

---

## 8. Exact thermal end-to-end EB condition

The full passive source→receiver channel is non-EB iff

$$
\tau_{A\to B}>m_{A\to B}.
$$

Hence

$$
\boxed{
\eta_g\tau_f(t)
>
m_B(t)+\tau_f(t)m_A.
}
$$

Equivalently,

$$
\boxed{
\tau_f(t)
[\eta_g-m_A]
>m_B(t).
}
$$

Using

$$
m_A
=\eta_g
\Gamma_{{\rm th},A}/\kappa_A,
$$

$$
\boxed{
\eta_g
\left(
1-\frac{\Gamma_{{\rm th},A}}{\kappa_A}
\right)
\tau_f(t)
>m_B(t).
}
$$

This is the clean source-and-receiver thermal capability condition.

---

## 9. Vacuum source-loss limit

If every nongravitational source bath is in vacuum,

$$
\Gamma_{{\rm th},A}=0,
$$

so

$$
m_A=0.
$$

The condition reduces to

$$
\boxed{
\eta_g\tau_f(t)>m_B(t),
}
$$

as derived in `PASSIVE_END_TO_END_CHANNEL.md`.

---

## 10. Purely gravitational source limit

If

$$
\kappa_A=\kappa_g
$$

and there are no other source ports,

$$
\boxed{
\eta_g=1,
\qquad
m_A=0.
}
$$

Then

$$
\boxed{
\tau_f(t)>m_B(t).
}
$$

The end-to-end channel capability reduces to the receiver-local condition.

---

## 11. Single thermal source-loss bath

For one ordinary loss bath with

$$
\kappa_\ell
$$

and occupation

$$
\bar n_A,
$$

$$
\kappa_A
=\kappa_g+\kappa_\ell,
$$

$$
\Gamma_{{\rm th},A}
=\kappa_\ell\bar n_A.
$$

The source emission channel is non-EB iff

$$
\boxed{
\kappa_\ell\bar n_A
<\kappa_g+\kappa_\ell.
}
$$

If

$$
\kappa_g\ll\kappa_\ell,
$$

this is approximately

$$
\boxed{\bar n_A<1.}
$$

Thus even though only a tiny fraction of source amplitude leaves gravitationally, the matched gravitational output mode does not become EB until the weighted thermal injection is of order the total source linewidth.

---

## 12. Source noise versus source branching loss

Source branching loss and source thermal noise are distinct:

### Vacuum ordinary loss

reduces

$$
\tau_A=\eta_g
$$

but leaves

$$
m_A=0.
$$

### Thermal ordinary loss

reduces

$$
\tau_A=\eta_g
$$

and also produces

$$
m_A>0.
$$

The first effect weakens end-to-end coherent transfer; the second can independently push the source emission stage toward EB.

---

## 13. Finite-spoke dependence

The gravitational source rate is

$$
\kappa_g(q_A)
=
\frac{8G\mu_AL_A^2\omega^4}{5c^5}
\mathcal C_\kappa(q_A).
$$

Therefore

$$
\eta_g(q_A)
=\frac{\kappa_g(q_A)}
{\kappa_g(q_A)+\sum_j\kappa_j}.
$$

Finite-support conservation corrections enter the passive source channel through this physically transparent branching ratio.

---

## 14. End-to-end causal capability time

The thermal passive source-resolved causal front is

$$
\boxed{
T_{A\to B}^{\rm cap}(R)
=
\frac Rc
+
\inf\left\{
t>0:
\eta_g\tau_f(t)
>
m_B(t)+\tau_f(t)m_A
\right\}.
}
$$

This replaces the receiver-local condition when the prepared mechanical source mode is taken as the channel input.

---

## 15. Adversarial verdict

A warm passive source bath does not invalidate the channel framework.

It produces an additional, exactly calculable Gaussian noise parameter

$$
\boxed{
m_A
=\kappa_g\Gamma_{{\rm th},A}/\kappa_A^2.
}
$$

The full source→receiver capability condition is correspondingly strengthened to

$$
\boxed{
\eta_g\tau_f
>m_B+\tau_fm_A.
}
$$

This closes the obvious thermal-source loophole within the same Markov model.

---

## 16. Next limitation to attack

The remaining source-preparation issue is not thermal decay during passive emission. It is the **initial preparation operation itself**:

- how the branch-dependent coherent source state is created;
- whether preparation emits a precursor gravitational field/wavepacket;
- how signal/control histories should be defined so the causal claim compares only operations inside the intended source region.

That causality/preparation issue should be treated separately rather than hidden inside the passive decay model.
