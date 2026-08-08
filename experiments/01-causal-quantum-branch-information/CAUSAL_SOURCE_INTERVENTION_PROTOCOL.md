# Causal Source Intervention Protocol

**Date:** 2026-08-07  
**Status:** **OPERATIONAL CAUSALITY DEFINITION — FRONT REFERS TO SOURCE-INPUT DEPENDENCE, NOT ABSENCE OF ALL PRE-EXISTING CORRELATIONS**

## 1. The preparation problem

A naive statement such as

> “the source and receiver cannot be correlated before $R/c$”

is not correct in quantum field theory.

The initial gravitational field can possess vacuum correlations, static source dressing, and other correlations outside the future light cone of a later source operation.

Likewise, simply declaring a matter–field product state with a spatially superposed gravitating source at $t=0$ can hide gauge/constraint and dressing issues.

The causal claim must therefore be operational.

---

## 2. Compare complete histories

Define two experimental histories:

### Control history

The source remains in its reference evolution.

### Signal history

A localized operation is applied inside a compact source worldtube

$$
\mathcal O_A.
$$

The two histories are identical outside the intervention and identical before the intervention begins.

Let the intervention support begin at source time

$$
\boxed{t=t_s.}
$$

All causal times must be measured from $t_s$, not from the end or midpoint of a preparation pulse.

---

## 3. Receiver dependence is the causal observable

Let

$$
\rho_B^{\rm sig}(t)
$$

and

$$
\rho_B^{\rm ctrl}(t)
$$

be receiver states in the two histories.

Define a local causal-influence measure such as

$$
\boxed{
\mathcal C_B(t)
=\frac12
\|\rho_B^{\rm sig}(t)-\rho_B^{\rm ctrl}(t)\|_1.
}
$$

More generally, if the source input is a quantum system $A$, define the channel

$$
\Phi_{A\to B}(t)
$$

from the locally encoded source input to the receiver.

Before causal contact, microcausality/no-signalling requires that the receiver output not depend on that local input.

Operationally,

$$
\boxed{
\Phi_{A\to B}(t)
=\mathcal R_B(t)
\qquad
\text{for spacelike separation},
}
$$

where

$$
\mathcal R_B(t)[\rho_A]
=\sigma_B(t)
$$

is a replacer channel independent of $\rho_A$.

This does **not** require the total initial field/receiver state to be uncorrelated.

---

## 4. Gaussian-channel representation

In the retarded one-mode receiver model, the source-dependent coherent transfer parameter obeys

$$
\boxed{
\tau_{A\to B}(t)=0
}
$$

before the retarded source response reaches the receiver.

The receiver may still have nonzero local occupation

$$
m_B(t)
$$

from its initial state and environment.

Therefore the pre-arrival channel is

$$
\boxed{
\Phi_{A\to B}
=\Phi_{0,m_B},
}
$$

a replacer/EB channel.

After arrival, the coherent transfer turns on according to the retarded input-output kernel.

For the passive source with thermal source noise,

$$
\tau_{A\to B}(t)
=\eta_g\tau_f(t),
$$

$$
m_{A\to B}(t)
=m_B(t)+\tau_f(t)m_A.
$$

The channel becomes non-EB only when

$$
\boxed{
\eta_g\tau_f(t)
>
m_B(t)+\tau_f(t)m_A.
}
$$

---

## 5. Pre-existing correlations are not the transmitted signal

The initial state may contain

- vacuum entanglement;
- static gravitational dressing;
- branch-independent receiver/environment correlations;
- static branch-dependent near fields common to signal and control histories.

These do not invalidate the causal channel definition.

The transmitted signal is the **change caused by the localized intervention**.

A pre-existing correlation can be physically relevant, but it cannot be used as evidence that the later intervention influenced the receiver outside its future light cone.

---

## 6. Clean source protocol: common static branch state, then release versus hold

A useful causal comparison is:

### Before $t_s$

Prepare the same static branch-correlated source state in both histories.

The endpoint/spoke plus coordinate has branch expectation

$$
\boxed{
u_s=s u_0.}
$$

The source may possess a static branch-dependent gravitational dressing. It is identical in signal and control runs before $t_s$.

### Control

Continue holding the source static.

### Signal

Locally release the plus mode into free evolution.

The intervention is the **release operation**, not the original creation of the source superposition.

The receiver observable is the difference between release and hold histories.

---

## 7. Resonant receiver rejects the static baseline

The held source produces a static quadrupolar field.

The released source produces an oscillatory quadrupole near frequency

$$
\omega.
$$

A high-Q receiver centered on

$$
\omega
$$

is naturally insensitive to the DC static baseline.

In addition, in the wave zone the static quadrupole metric scales parametrically as

$$
h_{\rm static}
\sim
\frac{GQ}{c^2R^3},
$$

while the radiative TT field scales as

$$
h_{\rm rad}
\sim
\frac{G\omega^2Q}{c^4R}.
$$

Thus

$$
\boxed{
\frac{h_{\rm static}}
{h_{\rm rad}}
\sim
\frac1{(kR)^2}.
}
$$

For

$$
kR\gg1,
$$

the static branch field is parametrically smaller than the radiative component at the receiver in addition to being spectrally off resonance.

Intermediate-zone terms are likewise suppressed by powers of

$$
1/(kR).
$$

---

## 8. Release must be smooth

An instantaneous release is not a good ultraviolet idealization.

If the signal-control quadrupole difference has insufficient differentiability at $t_s$, its high-frequency Fourier tail can make idealized graviton-number integrals poorly behaved or divergent.

Therefore use a finite release interval

$$
\boxed{T_r>0}
$$

with a smooth switching function.

A sufficient design is to choose the signal-control quadrupole difference so that it and enough time derivatives vanish at the beginning of the release.

The previously used compact $\sin^4$ envelope is one example of a sufficiently smooth profile, but it corresponds to active shaping throughout the pulse.

For the passive protocol, use smooth switch-off only during preparation/release and free exponential evolution afterward.

---

## 9. Causal origin for a finite release operation

If the release begins at

$$
t_s
$$

and ends at

$$
t_s+T_r,
$$

the **earliest** possible receiver dependence begins at

$$
\boxed{
t_s+R/c.}
$$

Do not shift the front to

$$
t_s+T_r+R/c
$$

unless the chosen source waveform actually has no branch-dependent change before the end of the release interval.

The complete support of the source intervention determines the retarded waveform.

---

## 10. Correct source-resolved capability time

Let receiver-local time after the earliest causal arrival be

$$
\tau=t-(t_s+R/c).
$$

Then define

$$
\boxed{
T_{A\to B}^{\rm cap}
=t_s+\frac Rc
+
\inf\left\{
\tau>0:
\tau_{A\to B}(\tau)
>m_{A\to B}(\tau)
\right\}.
}
$$

For the passive thermal source,

$$
\boxed{
\eta_g\tau_f(\tau)
>
m_B(\tau)+\tau_f(\tau)m_A.
}
$$

This is the operational quantum-capability front.

---

## 11. What may happen before the front

Before

$$
t_s+R/c,
$$

one may still have

- nonzero source–field correlations;
- vacuum field entanglement;
- static branch dressing;
- receiver/environment correlations;
- even changes in some **joint** correlation measure if pre-shared correlations are explicitly consumed by the local operation.

Therefore the paper must **not** state

$$
\text{“there is no entanglement before the light cone.”}
$$

The safe statement is

$$
\boxed{
\text{receiver dependence on the localized source intervention is zero before causal contact.}
}
$$

---

## 12. Relation to the source qubit

The source qubit is best treated as a reference/control degree of freedom that labels the two mirrored plus-mode alternatives.

The end-to-end channel question is:

> If quantum information initially encoded in the source-mode branch degree of freedom is changed/modulated by a local intervention, when can the receiver output begin to depend on that quantum input, and when is the resulting source→receiver map non-entanglement-breaking?

This is narrower and more operational than asking whether absolute source–receiver entanglement exists at some spacelike separation.

---

## 13. Preparation apparatus scope

The static branch state itself still requires preparation.

For the causal release experiment, that preparation is **not omitted**; it is placed in the common past of both signal and control histories.

Any field/dressing produced by preparation is part of the common initial condition.

The causal claim concerns the later release-versus-hold intervention.

If one instead wants to claim causal propagation from the **creation** of the branch superposition itself, then the entire preparation apparatus and its full spacetime support must be included in

$$
\mathcal O_A
$$

and the causal clock must start when preparation begins.

---

## 14. Adversarial verdict

The passive source should not be presented as an undressed product state suddenly appearing at $t=0$.

A defensible causal protocol is instead:

1. common prepared branch state in the past;
2. localized smooth release versus hold intervention;
3. retarded receiver comparison;
4. receiver-local or source-resolved Gaussian channel capability evaluated only after causal arrival.

This preserves the physically meaningful causal claim without denying pre-existing quantum-field correlations.

---

## 15. Next step

The remaining calculation is to choose an explicit smooth release function that

1. connects the held static branch state to the passive free exponential source;
2. has a UV-finite quadrupole spectrum;
3. keeps the release controller branch common under the parity symmetry;
4. allows the release-generated transient and passive tail to be separated quantitatively.

That release transient can then be included in the source waveform rather than treated as an unspecified preparation artifact.
