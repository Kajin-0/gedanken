# Novelty Collision — Miki–Li–Chen and Toccacelo–Beitel–Andersen–Pikovski (2026)

**Timestamp:** 2026-08-07 20:00 EDT  
**Status:** Major narrowing of the receiver-front novelty claim.

## 1. Miki–Li–Chen (2026)

**Daisuke Miki, Alfred Li, Yanbei Chen, “Amplification and generation bounds of gravity-induced entanglement in pulsed optomechanical systems,” arXiv:2605.26240 (2026).**

They study two Newtonian gravitationally coupled mechanical modes with Markov thermal damping,

$$
H_{G,I}
=\hbar g_G(b_Ab_B^\dagger+b_A^\dagger b_B).
$$

Their exact lossy transfer coefficients are

$$
C_{11}=C_{22}
=e^{-\gamma_mt}\cos(g_Gt),
$$

$$
C_{12}=C_{21}
=-ie^{-\gamma_mt}\sin(g_Gt).
$$

The thermal covariance added to the two-mode Gaussian map is

$$
V_{\rm th}
=2(1-e^{-2\gamma_mt})N_{\rm th}I
$$

in their high-temperature convention.

### Universal separability-generation threshold

In the weak-dissipation/weak-interaction regime they prove

$$
\boxed{
g_G>2\gamma_mN_{\rm th}}
$$

is necessary and sufficient for *some* initially separable two-mode Gaussian state to become entangled.

Thus the physical idea

> coherent gravitational coupling must outrun thermal decoherence

is explicit prior art.

### Full two-mode entanglement-breaking threshold

They also calculate the EB condition for the complete two-mode Gaussian channel $\Phi_{AB}$:

$$
\boxed{
2N_{\rm th}\tanh(\gamma_mt_G)\ge1.
}
$$

At weak damping,

$$
\boxed{
2\gamma_mt_GN_{\rm th}\ge1.
}
$$

This EB threshold is independent of $g_G$ because the gravitational beam-splitter is a reversible/unitary component of the full two-mode map; accumulated local thermal noise determines whether the *whole* map breaks entanglement with an external ancilla.

Therefore broad claims about time-dependent EB thresholds in noisy gravitational oscillator dynamics are not new.

---

## 2. Direction of the Miki full-channel crossing

The Miki full two-mode channel has the qualitative evolution

$$
\boxed{
\text{initially quantum-capable}
\longrightarrow
\text{eventually EB as thermal noise accumulates}.
}
$$

This differs from the receiver channel originally emphasized in Experiment 01, where the source-to-receiver link begins with zero source information and can cross

$$
\boxed{
\text{replacer/EB}
\longrightarrow
\text{non-EB as useful signal loads}.
}
$$

However this direction difference does **not** by itself establish novelty, because a reduced one-way transfer channel can be extracted from the Miki input-output equations.

---

## 3. Inferred one-way Miki transfer channel

Fix the input of oscillator $B$ and trace out the unwanted output. Then the useful $A_{\rm in}\to B_{\rm out}$ transfer amplitude has magnitude

$$
|C_{21}(t)|
=e^{-\gamma_mt}|\sin(g_Gt)|,
$$

so the signal intensity coefficient is

$$
\boxed{
\tau_{A\to B}(t)
=e^{-2\gamma_mt}\sin^2(g_Gt).
}
$$

Thermal noise grows from zero during the interaction.

Thus the reduced transfer channel is initially a poor/replacer-like channel and can develop a non-EB window before later thermal degradation.

This exact reduced EB analysis is **our inference from their published input-output map**, not a claim explicitly made in the Miki paper.

The main implication for Experiment 01 is nonetheless clear: a time-dependent EB crossing of a reduced gravitational transfer channel is a natural corollary of existing Newtonian Gaussian state-transfer models.

---

## 4. Toccacelo–Beitel–Andersen–Pikovski (2026)

**Kristian Toccacelo, Thomas Beitel, Ulrik Lund Andersen, Igor Pikovski, “Quantum State Characterization of Gravitational Waves via Graviton Counting Statistics,” arXiv:2602.09125 (2026).**

This is an even closer wave-zone receiver collision.

They model a **passing quantized gravitational-wave mode** $a$ resonantly exchanging quanta with a bulk acoustic detector mode $b$:

$$
\boxed{
H_{\rm int}
=\hbar\gamma_g(b^\dagger a+ba^\dagger).
}
$$

The ideal dynamics are

$$
b(t)
=e^{-i\omega t}
[\cos(\gamma_gt)b-i\sin(\gamma_gt)a].
$$

They explicitly study

- coherent gravitational-wave states;
- squeezed and thermal Gaussian GW states;
- graviton counting statistics;
- transfer of gravitational-wave quantum statistics into a detector;
- detector thermal noise;
- Markov open diffusive dynamics.

Therefore the concept

> quantized propagating gravitational-wave mode $\to$ resonant quantum material receiver

is already established prior art.

---

## 5. Toccacelo open receiver as an implicit Gaussian channel

Their Appendix C gives, for detector initial vacuum,

$$
\sigma_{\rm bar}(t)
=e^{-\kappa t}
\left[
\cos^2(\gamma_gt)\sigma_{\rm bar}(0)
+\sin^2(\gamma_gt)\sigma_{\rm grav}(0)
\right]
+(1-e^{-\kappa t})(\bar N+1/2)I,
$$

and

$$
\bar r_{\rm bar}(t)
=e^{-\kappa t/2}
\sin(\gamma_gt)\bar r_{\rm grav}(0).
$$

Therefore, up to a local phase rotation, the incoming GW mode $\to$ detector mode is a phase-insensitive Gaussian channel with

$$
\boxed{
\tau_{\rm GW\to det}(t)
=e^{-\kappa t}\sin^2(\gamma_gt),
}
$$

and vacuum-output thermal occupation

$$
\boxed{
m_{\rm GW\to det}(t)
=(1-e^{-\kappa t})\bar N.
}
$$

This identification is an inference from their covariance map; they do not discuss the EB boundary.

Applying the established one-mode Gaussian EB criterion gives

$$
\boxed{
e^{-\kappa t}\sin^2(\gamma_gt)
>
(1-e^{-\kappa t})\bar N
}
$$

for a non-entanglement-breaking incident-GW-to-detector channel.

Thus an **EB-to-non-EB temporal window for a noisy quantum gravitational-wave receiver is already latent in published 2026 equations**.

This substantially weakens any novelty claim based only on “a noisy GW receiver crosses the EB boundary in time.”

---

## 6. Short-time structure

For the Toccacelo receiver,

$$
\tau(t)
\simeq\gamma_g^2t^2,
$$

while

$$
m(t)
\simeq\kappa\bar Nt.
$$

Therefore near $t=0$ the channel is EB at any nonzero bath occupation.

A non-EB window can only emerge after coherent state-transfer probability catches up with accumulated thermal noise.

This reveals the same generic structure as a fixed regular waveform loading a receiver:

$$
\boxed{
\text{signal probability }\sim t^2,
\qquad
\text{Markov thermal noise }\sim t.
}
$$

This prior-art comparison directly motivated the correction in `GENERAL_FIXED_WAVEFORM_RECEIVER_FRONT.md`.

---

## 7. What remains distinct after these collisions

The following are **not** safe novelty claims:

- gravity-coupling-vs-thermal-decoherence thresholds;
- time-dependent noisy gravitational state transfer;
- EB conditions in noisy gravitational oscillator channels;
- a quantized passing GW mode interacting with a resonant material receiver;
- Gaussian open dynamics of such a receiver.

The remaining stronger candidate is narrower:

### Full retarded source-to-receiver link

Experiment 01 attempts to connect

$$
\boxed{
\text{controlled quantum source branch history}
\to
\text{emitted graviton difference wavepacket}
\to
\text{retarded free-space propagation}
\to
\text{noisy receiver}
}
$$

in one normalized channel.

Toccacelo et al. begin with an already-present incident GW mode at the detector. They do not derive the mode from a controlled source at separation $R$ or build a source-to-detector causal propagation map.

Miki et al. use a Newtonian near-field interaction between two localized mechanical modes.

Thus the potentially distinctive object is not the receiver alone but the **complete source-emission–propagation–capture channel**, especially its distance/time dependence and branch-information certification.

---

## 8. Strongest revised novelty candidate

The candidate contribution should now be stated cautiously as:

> **A source-resolved, retarded gravitational branch-information channel in which the emitted coherent difference mode, its free-space propagation, and a noisy quantum receiver are combined into one time-dependent map, together with an exact binary-coherent NPT witness for that complete channel.**

Even this may be a novel synthesis rather than a fundamentally new ingredient.

The next work must therefore derive the front from one explicit fixed source quadrupole waveform rather than from a protocol-optimized receiver envelope.

---

## 9. Consequence for paper structure

The receiver front should no longer be advertised as a universal new theorem of noisy gravitational reception.

Instead:

1. cite Miki for Newtonian noisy entanglement/EB bounds;
2. cite Toccacelo et al. for quantized GW-to-detector state transfer with thermal noise;
3. cite Mari for gravitational non-EB channel characterization;
4. cite Christodoulou et al. for retarded gravity-mediated entanglement;
5. present Experiment 01 as the attempt to **join source-controlled relativistic propagation to the quantum-channel receiver description**.

This is a much narrower but more defensible target.