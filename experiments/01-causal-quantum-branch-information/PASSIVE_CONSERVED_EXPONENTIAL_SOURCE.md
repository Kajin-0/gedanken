# Passive Conserved Exponential Source

**Date:** 2026-08-07  
**Status:** **CANONICAL CLOSED-EMISSION BENCHMARK — NO ACTUATOR ACTS DURING THE EMISSION INTERVAL**

## 1. Why a passive benchmark is needed

The finite-spoke source in `CONSERVED_SOURCE_ACTUATOR_AUDIT.md` is a genuine normal mode of a closed elastic system.

However, imposing the engineered trajectory

$$
u_c(t)
=u_0\sin^4(\pi t/T)\cos\omega t
$$

throughout a finite pulse requires active control. Controlled parity can make that controller branch common, but a fully spatially resolved actuator stress-energy has not yet been written for the driven pulse.

A stricter benchmark is therefore:

1. prepare the mechanical branch state before the emission interval;
2. decouple the preparation apparatus;
3. let the finite-spoke plus mode evolve and radiate freely.

During step 3 there is no active actuator to audit.

---

## 2. Initial mechanical branch state

Let the quantized plus mode begin in

$$
\boxed{
|\Psi(0)\rangle
=
\frac{|0\rangle_R|+\alpha_0\rangle_A
+|1\rangle_R|-\alpha_0\rangle_A}
{\sqrt2},
}
$$

or with arbitrary nonzero branch weights if desired.

The mechanical coherent-state distance is

$$
\boxed{
N_{\Delta,m}(0)
=|(+\alpha_0)-(-\alpha_0)|^2
=4|\alpha_0|^2.
}
$$

For real outer endpoint displacement $\pm u_0$ at a turning point,

$$
\boxed{
\alpha_0
=\frac{u_0}{2u_{\rm zpf}},
}
$$

so

$$
\boxed{
N_{\Delta,m}(0)
=\frac{u_0^2}{u_{\rm zpf}^2}.
}
$$

The finite-spoke zero-point coordinate is

$$
\boxed{
u_{\rm zpf}(q_A)
=\sqrt{\frac{\hbar}{2M_{\rm eff}(q_A)\omega}},
}
$$

with

$$
M_{\rm eff}(q_A)
=4\mu_A
\left[
\frac12+\frac{q_A}{\sin2q_A}
\right].
$$

---

## 3. Free source decay

Let the source mode have total amplitude-decay rate

$$
\boxed{
\kappa_A
=\kappa_{g,A}+\kappa_{\ell,A},
}
$$

where

- $\kappa_{g,A}$ is gravitational radiation;
- $\kappa_{\ell,A}$ represents all branch-record-carrying nongravitational loss channels.

After the preparation apparatus is removed,

$$
\boxed{
\alpha_s(t)
=s\alpha_0e^{-\kappa_A t/2}e^{-i\omega t}.
}
$$

The gravitational output obeys the standard input-output relation

$$
\boxed{
b_g^{\rm out}(t)
=b_g^{\rm in}(t)
+\sqrt{\kappa_{g,A}}\,a(t).
}
$$

Hence the gravitational branch-difference output amplitude is

$$
\boxed{
\Delta b_g^{\rm out}(t)
=2\sqrt{\kappa_{g,A}}
\alpha_0e^{-\kappa_A t/2}e^{-i\omega t}.
}
$$

---

## 4. Normalized emitted temporal mode

Define

$$
\boxed{
f_A(t)
=\sqrt{\kappa_A}
 e^{-\kappa_A t/2},
\qquad t\ge0.
}
$$

Then

$$
\int_0^\infty|f_A(t)|^2dt=1.
$$

The gravitational output branch difference can be written

$$
\boxed{
\Delta b_g^{\rm out}(t)
=
\sqrt{N_\Delta^{(g)}}
 f_A(t)e^{-i\omega t},
}
$$

where

$$
\boxed{
N_\Delta^{(g)}
=\frac{\kappa_{g,A}}{\kappa_A}
N_{\Delta,m}(0).
}
$$

Thus the **gravitational branching ratio** is

$$
\boxed{
\eta_g
=\frac{\kappa_{g,A}}{\kappa_A}.
}
$$

---

## 5. Information conservation among decay channels

For each independent Markov loss channel $j$ with rate $\kappa_j$, the emitted branch distance is

$$
N_\Delta^{(j)}
=\frac{\kappa_j}{\kappa_A}
N_{\Delta,m}(0).
$$

Therefore

$$
\boxed{
\sum_jN_\Delta^{(j)}
=N_{\Delta,m}(0).
}
$$

The initial mechanical branch record is redistributed among the output channels.

This makes the passive-source tradeoff exact:

> Broadening the source with nongravitational damping shortens the pulse but transfers the same branch information into uncontrolled environments instead of the gravitational mode.

For a purely gravitationally damped source,

$$
\boxed{
\kappa_A=\kappa_{g,A}
}
$$

and

$$
\boxed{
N_\Delta^{(g)}
=N_{\Delta,m}(0).
}
$$

Eventually the full initial mechanical branch distance is emitted gravitationally.

---

## 6. Finite-spoke source normalization

The corrected source linewidth is

$$
\boxed{
\kappa_{g,A}(q_A)
=
\frac{8G\mu_AL_A^2\omega^4}{5c^5}
\mathcal C_\kappa(q_A),
}
$$

with

$$
\mathcal C_\kappa(q_A)
=
\frac{(\tan q_A/q_A)^2}
{\frac12+q_A/\sin2q_A}.
$$

The initial branch distance for a fixed outer displacement is

$$
N_{\Delta,m}(0)
=\frac{u_0^2}{u_{\rm zpf}^2}
=
\frac{2M_{\rm eff}(q_A)\omega u_0^2}{\hbar}.
$$

For a purely gravitational source, this is also the total emitted graviton coherent-state distance.

Notice that this passive result differs conceptually from the actively prescribed $\sin^4$ formula. In the passive case the pulse duration is set dynamically by

$$
1/\kappa_A,
$$

not independently by a chosen $T$.

---

## 7. Retarded arrival at the receiver

At source–receiver separation $R$, the normalized incident temporal mode is

$$
\boxed{
f_R(t)
=f_A(t-R/c)\Theta(t-R/c)
}
$$

up to the wave-zone spatial storage amplitude and carrier phase.

No receiver observable can depend on the release/free-emission operation before

$$
\boxed{t=R/c}
$$

relative to the local source change, apart from pre-existing correlations in the chosen initial field state.

The operational comparison must therefore be between runs that differ by a local source preparation/release operation, not between absolute vacuum correlations.

---

## 8. Receiver loading for an exponential waveform

Let the receiver total damping rate be

$$
\kappa_B.
$$

After causal arrival define receiver-local time

$$
t\ge0.
$$

For

$$
f_A(t)=\sqrt{\kappa_A}e^{-\kappa_A t/2},
$$

the coherent receiver transfer is

$$
\tau_{\exp}(t)
=\kappa_\Delta
\left|
\int_0^t ds\,
 e^{-\kappa_B(t-s)/2}
\sqrt{\kappa_A}e^{-\kappa_A s/2}
\right|^2.
$$

For

$$
\kappa_A\ne\kappa_B,
$$

$$
\boxed{
\tau_{\exp}(t)
=
\frac{4\kappa_\Delta\kappa_A}
{(\kappa_B-\kappa_A)^2}
\left(
 e^{-\kappa_A t/2}
-e^{-\kappa_B t/2}
\right)^2.
}
$$

For matched source and receiver linewidths,

$$
\boxed{\kappa_A=\kappa_B=\kappa,}
$$

$$
\boxed{
\tau_{\exp}(t)
=\kappa_\Delta\kappa t^2e^{-\kappa t}.
}
$$

---

## 9. Exact matched-linewidth maximum

Differentiate

$$
t^2e^{-\kappa t}.
$$

The maximum occurs at

$$
\boxed{t_*=2/\kappa.}
$$

Therefore

$$
\boxed{
\tau_{\exp}^{\max}
=4e^{-2}
\frac{\kappa_\Delta}{\kappa}
\simeq
0.541341
\frac{\kappa_\Delta}{\kappa}.
}
$$

This is lower than the optimized active $\sin^4$ waveform coefficient

$$
S_{4,*}\simeq0.7980213,
$$

which quantifies the value of waveform engineering.

But the exponential protocol has the stronger conservation interpretation: no actuator acts during emission.

---

## 10. Thermal non-EB condition

The receiver's vacuum-output occupation remains

$$
m(t)
=n_0e^{-\kappa_Bt}
+\frac{\Gamma_{\rm th}}{\kappa_B}
(1-e^{-\kappa_Bt}).
$$

The receiver is non-entanglement-breaking when

$$
\boxed{
\tau_{\exp}(t)>m(t).
}
$$

For a stationary thermal initial receiver,

$$
n_0=\Gamma_{\rm th}/\kappa,
$$

so

$$
m(t)=n_{\rm th}
$$

is constant.

At matched linewidths a necessary and sufficient condition for some passive non-EB interval is then

$$
\boxed{
n_{\rm th}
<4e^{-2}
\frac{\kappa_\Delta}{\kappa}.
}
$$

Equivalently,

$$
\boxed{
\Gamma_{\rm th}
<4e^{-2}\kappa_\Delta.
}
$$

The passive exponential threshold coefficient is therefore

$$
\boxed{4e^{-2}\simeq0.541341.}
$$

---

## 11. Source strength and channel capability are distinct

The gravitational branch distance

$$
N_\Delta^{(g)}
$$

sets how strongly the two source branches are encoded in the incident gravitational mode.

The receiver channel parameter

$$
\tau_{\exp}(t)
$$

describes how much of a **normalized incident mode** is stored by the receiver.

These should not be multiplied or conflated when deciding whether the receiver map itself is EB.

For source–receiver entanglement strength, both matter:

1. $N_\Delta^{(g)}$ determines the input branch separation;
2. $\tau_{\exp}$ determines receiver capture;
3. uncollected gravitational modes and nongravitational source loss carry which-branch information.

---

## 12. Fully passive source tradeoff

If

$$
\kappa_{\ell,A}=0,
$$

then

$$
\kappa_A=\kappa_{g,A}.
$$

This is the cleanest source from a conservation standpoint, but because gravitational radiation is extremely weak the pulse duration

$$
1/\kappa_{g,A}
$$

is correspondingly long.

Adding ordinary damping can make

$$
\kappa_A
$$

larger and shorten the waveform, but reduces the gravitational branching ratio

$$
\eta_g
=\kappa_{g,A}/\kappa_A.
$$

Thus passive pulse shortening has a direct information cost.

This is the passive analogue of the earlier result that a stronger emitted branch record is not always better when most of the field is uncollected.

---

## 13. Role of the active $\sin^4$ protocol

The active source remains useful as an engineered upper-performance benchmark.

It gives

- compact temporal support;
- a larger receiver waveform-overlap coefficient;
- independently chosen pulse duration;
- exact smooth turn-on and turn-off.

But its actuator must be part of the total source model during emission.

Therefore use the following hierarchy in the paper:

### Passive exponential source

Canonical conservation benchmark.

### Active $\sin^4$ source

Optimized protocol under the additional assumption of an internal parity-symmetric controller whose residual branch quadrupole obeys the bound in `HUB_CONTROLLER_RESIDUAL_BOUND.md`.

---

## 14. Adversarial verdict

The project no longer needs to pretend that a shaped pulse and a free conserved source are the same object.

A fully passive, actuator-free emission interval exists and has an exact normalized exponential waveform.

The price is a fixed source linewidth and potentially very long gravitational decay time.

The active source improves temporal capture at the cost of a stronger actuator-model assumption.

This separation makes the source model more defensible.

---

## 15. Next step

1. Promote the passive exponential source to the primary conserved-source benchmark in `PAPER_CORE_V4_CONSERVED_SOURCE.md`.
2. Keep the $\sin^4$ pulse as a secondary active protocol.
3. Re-run the source→receiver capability plots/thresholds for the exponential waveform using the corrected finite-spoke $\kappa_g(q)$.
4. Treat preparation before the free-emission interval as a separate local operation whose full causal influence must be compared between signal and control histories.
