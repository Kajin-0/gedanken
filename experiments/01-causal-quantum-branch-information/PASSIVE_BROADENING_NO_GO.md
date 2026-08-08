# Passive Source Broadening No-Go for End-to-End Quantum Transfer

**Date:** 2026-08-07  
**Status:** **EXACT SOURCE-RESOLVED OPTIMIZATION — VACUUM NONGRAVITATIONAL BROADENING STRICTLY REDUCES MAXIMUM END-TO-END COHERENT TRANSFER**

## 1. Question

For a normalized incident exponential gravitational mode, temporal matching suggests choosing the source linewidth close to the receiver linewidth.

But a real source does not begin with a normalized graviton mode. Broadening the passive source with an ordinary loss channel changes the gravitational branching fraction

$$
\eta_g=\kappa_g/\kappa_A.
$$

The correct question is therefore:

> At fixed intrinsic gravitational source rate $\kappa_g$, receiver loading rate $\kappa_\Delta$, and receiver linewidth $\kappa_B$, can adding vacuum nongravitational source damping ever improve the maximum coherent transfer from the initial source oscillator to the receiver?

The answer is no.

---

## 2. Receiver-local transfer for arbitrary exponential linewidth ratio

Let

$$
f_A(t)=\sqrt{\kappa_A}e^{-\kappa_A t/2}
$$

and define

$$
\boxed{r=\kappa_A/\kappa_B.}
$$

The receiver-local coherent transfer is

$$
\tau_f(t)
=
\frac{4\kappa_\Delta\kappa_A}
{(\kappa_B-\kappa_A)^2}
\left(
 e^{-\kappa_A t/2}
-e^{-\kappa_Bt/2}
\right)^2.
$$

Set

$$
x=\kappa_Bt/2.
$$

Then

$$
\tau_f(x)
=
4\frac{\kappa_\Delta}{\kappa_B}
\frac{r}{(1-r)^2}
\left(e^{-rx}-e^{-x}\right)^2.
$$

---

## 3. Exact optimal receiver time

For

$$
r\ne1,
$$

differentiate the bracket:

$$
-r e^{-rx}+e^{-x}=0.
$$

Therefore

$$
\boxed{
x_*(r)
=-\frac{\ln r}{1-r}
=
\frac{\ln(1/r)}{1-r}.}
$$

Equivalently,

$$
\boxed{
t_*(r)
=
\frac{2}{\kappa_B}
\frac{\ln(1/r)}{1-r}.}
$$

As

$$
r\to1,
$$

$$
t_*\to2/\kappa_B.
$$

---

## 4. Exact receiver-local maximum

At the optimum,

$$
e^{-x_*}
=r e^{-rx_*}.
$$

Thus

$$
e^{-rx_*}-e^{-x_*}
=(1-r)e^{-rx_*}.
$$

Substitution gives

$$
\boxed{
\tau_f^{\max}(r)
=
\frac{\kappa_\Delta}{\kappa_B}
S_{\exp}(r),
}
$$

where

$$
\boxed{
S_{\exp}(r)
=4r^{(1+r)/(1-r)}.
}
$$

The continuous matched-linewidth limit is

$$
\boxed{
S_{\exp}(1)=4e^{-2}\simeq0.541341.
}
$$

The function satisfies the symmetry

$$
S_{\exp}(r)=S_{\exp}(1/r),
$$

and is maximized at

$$
r=1
$$

for the **receiver-local problem with a normalized incident mode**.

---

## 5. Source-resolved transfer includes gravitational branching

For vacuum source loss ports, the source→gravitational-mode transmissivity is

$$
\boxed{
\eta_g
=\frac{\kappa_g}{\kappa_A}
=\frac{\kappa_g}{r\kappa_B}.
}
$$

Therefore the maximum full source→receiver coherent transfer is

$$
\tau_{A\to B}^{\max}
=\eta_g\tau_f^{\max}.
$$

Hence

$$
\boxed{
\tau_{A\to B}^{\max}(r)
=
4
\frac{\kappa_g\kappa_\Delta}
{\kappa_B^2}
F(r),
}
$$

where it is convenient to define

$$
\boxed{
F(r)
=r^{2r/(1-r)}.
}
$$

Equivalently, keeping the factor of four inside the shape function,

$$
\boxed{
\mathcal F(r)
=4r^{2r/(1-r)}.
}
$$

---

## 6. Exact monotonicity theorem

For

$$
F(r)=r^{2r/(1-r)},
$$

$$
\ln F
=\frac{2r\ln r}{1-r}.
$$

Differentiate:

$$
\boxed{
\frac{d}{dr}\ln F
=
\frac{2(\ln r+1-r)}{(1-r)^2}.
}
$$

The elementary inequality

$$
\ln r\le r-1
$$

is strict for

$$
r\ne1.
$$

Therefore

$$
\boxed{
\frac{d}{dr}\ln F<0
\qquad(r>0),
}
$$

with the derivative defined continuously through $r=1$.

Thus

$$
\boxed{
F(r)
\text{ is strictly decreasing on }(0,\infty).
}
$$

---

## 7. Main no-go result

At fixed

$$
\kappa_g,
\qquad
\kappa_\Delta,
\qquad
\kappa_B,
$$

increasing the total source linewidth

$$
\kappa_A
$$

by adding vacuum nongravitational damping strictly decreases the maximum source→receiver coherent transfer.

Therefore

$$
\boxed{
\text{passive nongravitational broadening cannot improve end-to-end transfer.}
}
$$

The optimum is the smallest allowed source linewidth.

If the only unavoidable decay is gravitational,

$$
\boxed{
\kappa_A=\kappa_g
}
$$

is the passive optimum.

---

## 8. Why this does not contradict receiver-local impedance matching

For an already normalized incoming gravitational mode, the receiver-local overlap function

$$
S_{\exp}(r)
$$

is best at

$$
r=1.
$$

But broadening the physical source changes the probability that the initial source excitation enters the gravitational mode at all:

$$
\eta_g\propto1/\kappa_A.
$$

The gain in temporal overlap is always smaller than the loss in gravitational branching.

Thus

$$
\boxed{
\text{waveform matching and source branching must be optimized together.}
}
$$

---

## 9. Limiting cases

### Narrow source: $r\to0^+$

Since

$$
\frac{2r\ln r}{1-r}\to0,
$$

$$
\boxed{F(r)\to1.}
$$

Therefore

$$
\boxed{
\tau_{A\to B}^{\max}
\to
4
\frac{\kappa_g\kappa_\Delta}
{\kappa_B^2}.
}
$$

The source pulse becomes very long, but nearly all of the available source amplitude remains in the gravitational decay branch when ordinary broadening is removed.

### Matched linewidth: $r=1$

$$
\boxed{F(1)=e^{-2}.}
$$

Thus

$$
\boxed{
\tau_{A\to B}^{\max}(1)
=4e^{-2}
\frac{\kappa_g\kappa_\Delta}
{\kappa_B^2}.
}
$$

This is smaller than the narrow-source limit by a factor

$$
\boxed{e^{-2}\simeq0.135335.}
$$

### Broad source: $r\to\infty$

$$
F(r)\sim r^{-2}
$$

up to logarithmic/exponent corrections from the exact expression, so the end-to-end transfer vanishes.

---

## 10. Thermal source broadening is even worse

If the added source loss bath is thermally occupied, then broadening also produces source noise

$$
m_A
=\frac{\kappa_g\Gamma_{{\rm th},A}}
{\kappa_A^2}.
$$

The end-to-end non-EB condition is

$$
\eta_g\tau_f
>m_B+\tau_fm_A.
$$

Thus thermal broadening both

1. reduces coherent gravitational branching;
2. adds noise.

The vacuum-bath no-go is therefore the most favorable case for passive broadening.

---

## 11. Engineering implication

If a shorter source waveform is required without sacrificing the gravitational branching ratio, one must use **coherent active shaping** rather than dissipative broadening.

This explains the role of the active $\sin^4$ protocol:

- passive loss cannot improve end-to-end transfer;
- coherent control may reshape the source temporal mode without dumping branch information into an uncontrolled environment, provided the controller remains quantum coherent and its stress-energy is included/bounded.

Thus active waveform engineering and passive broadening are fundamentally different resources.

---

## 12. Adversarial verdict

A naive recommendation to broaden the source until

$$
\kappa_A\sim\kappa_B
$$

is wrong for the full source-resolved channel when the broadening is implemented by ordinary loss.

The exact optimization gives

$$
\boxed{
\frac{d}{d\kappa_A}
\tau_{A\to B}^{\max}<0
}

at fixed intrinsic $\kappa_g,\kappa_\Delta,\kappa_B$.

The passive optimum is to eliminate nongravitational source loss rather than impedance-match it dissipatively.

---

## 13. Next question

For a purely gravitational source,

$$
\kappa_A=\kappa_g
$$

may be vastly smaller than the receiver linewidth.

The next optimization question is therefore:

> Can a **coherent**, branch-common controller reshape the gravitational emission into a receiver-matched temporal mode without introducing an equivalent which-branch environment or large controller quadrupole?

That is the correct role for the active source protocol and should be treated as a coherent-control problem, not as passive damping.
