# Accessible Receiver Cascade Theorem

**Timestamp:** 2026-08-07 18:00 EDT  
**Status:** Exact for cascades of one-mode gauge-covariant phase-insensitive Gaussian channels, using the binary coherent probe theorem.

## 1. Motivation

A system can absorb gravitational branch information efficiently without being a useful quantum receiver.

Experiment 01 ultimately needs the branch record to reach a **controllable accessible register** on which one can perform

- a joint source-receiver witness;
- an eraser/reversal;
- or another operational entanglement test.

This suggests separating the receiver into two stages:

$$
\boxed{
\text{source}
\to
\text{gravitational capture mode}
\to
\text{accessible readout register}.
}
$$

The distinction is negligible for a laboratory oscillator whose mode is directly measured, but potentially decisive for

- compact objects;
- strongly scrambling systems;
- horizon absorbers;
- buried collective modes;
- any receiver whose gravitationally active degree of freedom is not directly controllable.

---

## 2. Two phase-insensitive Gaussian stages

Let the capture channel be

$$
\Phi_c=\Phi_{\tau_c,m_c},
$$

and the readout/accessibility channel be

$$
\Phi_r=\Phi_{\tau_r,m_r}.
$$

For a gauge-covariant phase-insensitive Gaussian channel,

$$
\chi_{\Phi(O)}(\xi)
=\chi_O(\sqrt\tau\xi)
\exp[-(2m+1-\tau)|\xi|^2/2].
$$

Apply $\Phi_c$ first and $\Phi_r$ second.

The coherent gain/transmission composes as

$$
\boxed{
\tau_{\rm tot}
=\tau_c\tau_r.
}
$$

The vacuum-output occupation composes as

$$
\boxed{
 m_{\rm tot}
=\tau_r m_c+m_r.
}
$$

This follows directly from substitution of the characteristic-function kernels.

---

## 3. Exact accessible-entanglement criterion

The binary coherent Gaussian-channel theorem gives

$$
\text{accessible output NPT}
\iff
\tau_{\rm tot}>m_{\rm tot}.
$$

Therefore

$$
\tau_c\tau_r
>
\tau_r m_c+m_r.
$$

Equivalently,

$$
\boxed{
\tau_r(\tau_c-m_c)>m_r.
}
$$

Define the capture-stage quantum excess

$$
\boxed{
\Delta_c
=\tau_c-m_c.
}
$$

Then

$$
\boxed{
\text{accessible NPT}
\iff
\tau_r\Delta_c>m_r.
}
$$

This is the central result.

---

## 4. Composition law for quantum excess

For any phase-insensitive Gaussian channel define

$$
\boxed{
\Delta_Q
=\tau-m.
}
$$

A channel is non-entanglement-breaking iff

$$
\Delta_Q>0.
$$

For two stages,

$$
\Delta_{rc}
=\tau_r\tau_c-(\tau_rm_c+m_r),
$$

so

$$
\boxed{
\Delta_{rc}
=\tau_r\Delta_c-m_r.
}
$$

This has a simple interpretation:

> **The readout transmits the quantum excess already present in the captured state and then subtracts its own classicalizing noise budget.**

Thus quantum excess is not multiplicative; every downstream noisy stage can consume it.

---

## 5. Important limits

### Perfectly accessible readout

If

$$
\tau_r=1,
\qquad
m_r=0,
$$

then

$$
\Delta_{rc}=\Delta_c.
$$

The accessible register inherits the capture channel's quantum capability exactly.

### Pure-loss readout

If

$$
m_r=0,
\qquad
\tau_r>0,
$$

then

$$
\Delta_{rc}=\tau_r\Delta_c.
$$

Any nonzero pure-loss accessibility preserves the **sign** of NPT if the capture stage is non-EB, although the amount and witness strength can become arbitrarily small.

### Thermal/noisy readout

If

$$
m_r>0,
$$

there is a genuine accessibility threshold:

$$
\boxed{
\tau_r>
\frac{m_r}{\Delta_c}.
}
$$

A capture mode can therefore be strongly quantum while the accessible register is completely separable from the source.

### Perfect capture

If

$$
\tau_c=1,
\qquad
m_c=0,
$$

then

$$
\boxed{
\text{accessible NPT}
\iff
\tau_r>m_r.
}
$$

The problem reduces to whether the readout channel itself is non-EB.

This is the idealized compact-object lesson: perfect absorption alone is insufficient.

---

## 6. N-stage cascade

For channels

$$
\Phi_1,\Phi_2,\ldots,\Phi_N
$$

applied in that order,

$$
\boxed{
\tau_{1:N}
=\prod_{j=1}^{N}\tau_j.
}
$$

The total vacuum-output occupation is

$$
\boxed{
 m_{1:N}
=m_N
+\tau_Nm_{N-1}
+\tau_N\tau_{N-1}m_{N-2}
+\cdots
+\left(\prod_{j=2}^{N}\tau_j\right)m_1.
}
$$

Hence every downstream stage weights and transmits upstream noise while adding its own noise.

The exact finite binary coherent probe remains NPT iff

$$
\boxed{
\tau_{1:N}>m_{1:N}.
}
$$

This gives a compact criterion for a complete source $\to$ gravity $\to$ receiver $\to$ transducer $\to$ readout chain.

---

## 7. Exact witness through the cascade

For a symmetric binary coherent branch encoding with initial branch-mode distance $N_\Delta$, the exact matched three-element witness at the accessible output satisfies

$$
\boxed{
\Lambda_{\rm acc}
=
\frac{N_\Delta}{m_{\rm tot}}
(\tau_{\rm tot}-m_{\rm tot}).
}
$$

For the two-stage receiver,

$$
\boxed{
\Lambda_{\rm acc}
=
\frac{N_\Delta}
{\tau_rm_c+m_r}
\left[
\tau_r(\tau_c-m_c)-m_r
\right].
}
$$

Thus accessibility affects both

- whether entanglement survives at all;
- how strongly the exact witness can be violated.

---

## 8. Time-dependent accessible front

Let the gravitational capture stage evolve causally after

$$
t_0=R/c.
$$

Write

$$
\tau_c(t),
\qquad
m_c(t).
$$

Let the readout channel be applied after or during capture with parameters

$$
\tau_r(t),
\qquad
m_r(t).
$$

Then the source and accessible register are NPT exactly when

$$
\boxed{
\tau_r(t)
[\tau_c(t)-m_c(t)]
>m_r(t).
}
$$

This defines an **accessible NPT front** that can occur strictly later than the internal capture-mode NPT front.

Therefore Experiment 01 can possess three genuinely different quantum times:

1. gravitational signal arrival;
2. internal receiver entanglement;
3. accessible/readable entanglement.

---

## 9. Compact-object interpretation

### Weak laboratory resonator

Usually the gravitationally active mode is itself controllable, so

$$
\tau_r\simeq1,
\qquad
m_r\simeq0.
$$

The primary problem is weak capture.

### Compact-star mode

Capture can be much stronger, but extracting one coherent mode from the enormous internal stellar environment may correspond to

$$
\tau_r\ll1
$$

and/or

$$
m_r\gg0.
$$

### Black-hole-like absorber

A horizon may absorb gravitational branch information extremely efficiently. But if the only readout is Hawking radiation or another highly scrambling retrieval channel, the relevant criterion is not horizon absorption alone. It is

$$
\boxed{
\tau_r\Delta_c>m_r.
}
$$

This makes “accessibility” a precise channel quantity rather than a qualitative objection.

A serious black-hole application would require deriving the effective readout channel rather than guessing its Gaussian parameters.

---

## 10. Coupling–coherence–accessibility triangle in channel form

The earlier qualitative receiver triangle can now be expressed through exact channel variables.

### Capture

$$
\tau_c
$$

measures coherent branch-mode transmission into the internal receiver.

### Coherence

$$
\Delta_c=\tau_c-m_c
$$

measures how far the capture channel lies from its EB boundary.

### Accessibility

$$
\tau_r,
\qquad
m_r
$$

measure how much of that internal quantum excess reaches a controllable output.

The useful accessible quantum excess is

$$
\boxed{
\Delta_{\rm acc}
=\tau_r\Delta_c-m_r.
}
$$

A useful receiver requires

$$
\boxed{
\Delta_{\rm acc}>0.
}
$$

---

## 11. Strongest consequence

> **Strong gravitational absorption is not sufficient for a quantum-gravity experiment. The absorbed branch information must survive a second channel into degrees of freedom that can actually be measured coherently. In the phase-insensitive Gaussian regime, this entire requirement collapses to one exact inequality: downstream readout must transmit the capture channel's quantum excess faster than it adds its own noise.**

This is the current cleanest unification of weak laboratory receivers and strong-gravity absorbers.

---

## 12. Next strongest path

1. Test whether a realistic compact-object readout channel can be mapped onto $(\tau_r,m_r)$.
2. More abstractly, generalize the cascade criterion beyond Gaussian channels using entanglement-breaking composition or quantum capacity monotones.
3. Use the accessible quantum excess $\Delta_{\rm acc}$ as the receiver figure of merit when comparing weak matter, compact stars, black holes, and field-theoretic receivers.
