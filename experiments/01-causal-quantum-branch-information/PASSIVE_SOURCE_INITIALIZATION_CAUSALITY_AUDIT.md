# Passive Source Initialization and Causality Audit

**Date:** 2026-08-07  
**Status:** **SCOPE CORRECTION — PASSIVE DECAY IS A CLEAN FUTURE-EMISSION CHANNEL, BUT ITS INITIAL STATE DOES NOT BY ITSELF DEFINE THE LOCAL ENCODING EVENT REQUIRED BY THE MICROCAUSAL FRONT THEOREM**

## 1. Problem

The passive source construction begins at a reference time $t=0$ with a branch-dependent mechanical state such as

$$
\frac{|0\rangle_R|+\alpha_0\rangle_A
+|1\rangle_R|-\alpha_0\rangle_A}{\sqrt2},
$$

then allows the finite-spoke mechanical mode to decay freely.

This is an excellent conservation benchmark for the **future emission stage** because no active actuator is required after $t=0$.

However, the microcausal replacer theorem in

- `MICROCAUSAL_REPLACER_THEOREM.md`

assumes a different operational structure:

1. an input register $G$ is initially independent of the rest of the world;
2. a local encoding operation $V_A$ in a bounded source region begins at the causal origin;
3. the receiver channel is defined by varying the state of $G$ while holding the pre-encoding environment fixed.

A branch-dependent mechanical state already present at $t=0$ is **not automatically the same thing** as such a local encoding event.

This distinction must be explicit in the paper.

---

# 2. Why the distinction is especially important in gravity

In an ordinary quantum-optical input-output model one often writes, at an initial time,

$$
\rho_A\otimes\rho_{\rm bath}
$$

and treats $\rho_A$ as an arbitrary oscillator input.

For the radiative TT sector of weak linearized gravity, this is a useful effective open-system convention.

For the **full gravitational system**, however, matter configurations and their long-range gravitational dressing/constraint fields are not generically independent tensor factors.

A different mass configuration can already be accompanied by a different nonradiative gravitational field before the chosen $t=0$.

Therefore the statement

> “the source is in $|\pm\alpha_0\rangle$ at $t=0$, so no source information can exist at the receiver before $R/c$ measured from that same $t=0$”

requires additional assumptions.

The exact microcausal theorem avoids this issue by defining a **local source operation** whose input is independent of the pre-existing state.

---

# 3. Three distinct maps that must not be conflated

## 3.1 Receiver-local channel

Input:

$$
\text{already-defined incident graviton wavepacket}.
$$

Output:

$$
\text{receiver mode}.
$$

This is the channel described by

$$
\Phi_{\tau_f(t),m_B(t)}.
$$

It is unambiguous once the incident mode is specified.

---

## 3.2 Passive future-emission channel

Input:

$$
\text{source oscillator state on a chosen initial slice}.
$$

Output:

$$
\text{future gravitational output mode}.
$$

Within the Markov input-output model this is

$$
\Phi_A
$$

or, for vacuum source loss,

$$
\mathcal L_{\eta_g}.
$$

Composing this with the receiver gives

$$
\Phi_{A\to B}^{\rm future}(t).
$$

This is a valid and useful **conditional future-transfer map**.

It answers:

> Given the source oscillator state at the initial slice, how much of its future outgoing branch information reaches the receiver?

It does **not**, by itself, specify how that source oscillator state was locally encoded from an initially independent input register.

---

## 3.3 Operational source-controlled communication channel

Input:

$$
\rho_G
$$

on a local register initially independent of the environment.

A local source operation

$$
V_A
$$

acts in a bounded spacetime region and produces whatever mechanical/gravitational source state follows.

The receiver output defines

$$
\mathcal A_{R,t}:\rho_G\mapsto\rho_B(t).
$$

For spacelike separation from the encoding region,

$$
\boxed{
\mathcal A_{R,t}\text{ is a replacer channel.}
}
$$

This is the map to which the strict microcausal

$$
T_{\rm cap}\ge R/c
$$

statement applies.

---

# 4. Consequence for the passive formula

The passive end-to-end calculation currently defines

$$
T_{A\to B}^{\rm cap}(R)
=
\frac Rc
+
\inf\{t>0:\eta_g\tau_f(t)>m_B(t)\}
$$

or its thermal-source generalization.

This expression is exact **for the future-transfer model when $t=0$ is taken as the source-mode initial slice and the incoming radiative bath after that slice is independent**.

It should not automatically be described as the total latency from a fresh local encoding of an independent quantum register.

A safer label is

$$
\boxed{
T_{\rm future}^{\rm cap}(R)
}
$$

or

> passive future-emission capability time.

The full source-controlled communication latency must additionally account for the encoding stage.

---

# 5. Precursor radiation from preparation

Suppose the mechanical branch state is prepared during

$$
-T_{\rm enc}<t<0.
$$

If the quadrupole changes during preparation, the preparation operation itself emits branch-dependent gravitational radiation.

That precursor is not optional bookkeeping. It can

- carry which-branch information;
- decohere the retained source/reference;
- reach the receiver before the later passive tail;
- modify the earliest non-EB source-controlled signal.

Therefore a complete local protocol beginning before preparation must include the entire quadrupole history

$$
\Delta Q_{ij}(t),
\qquad
-T_{\rm enc}<t<\infty.
$$

The passive exponential tail alone is not the complete radiation history of that protocol.

---

# 6. Static / constraint-field prehistory

If a source is held in different displaced configurations before release, then even if it emits no TT radiation while static, its branch-dependent nonradiative gravitational field is already present.

A receiver that has interacted with that field before the chosen release time may already carry branch information or correlations.

Therefore “release time” is not automatically a universal causal origin for the **full** gravitational state.

Two clean ways to avoid overclaiming are:

1. define the calculation explicitly as a channel for the **radiative TT future output**, with the constraint sector control-subtracted; or
2. include an explicit local encoding operation whose prehistory is input-independent.

The second route gives the strongest operational causality statement.

---

# 7. Receiver reset can define a conditional future-transfer experiment

There is a useful operational workaround when the source has already been prepared.

Let the source evolve freely through $t=0$ and define its oscillator state at that slice as the input to the future-transfer calculation.

At the receiver, after all radiation emitted before $t=0$ has passed, locally reset the receiver mode to a fixed state before admitting the future source wavepacket.

In ideal wave-zone propagation, radiation emitted after source time $0$ begins arriving at receiver time

$$
R/c.
$$

A local receiver reset immediately before that arrival removes any receiver memory of earlier radiation.

Then the passive formula characterizes

$$
\boxed{
\text{source state at }t=0
\to
\text{receiver state due to future output}
}
$$

without claiming that the source state itself was freshly created at $t=0$.

This is a legitimate benchmark, but it is a **conditional transfer protocol**, not the same operational question as sending a newly encoded input at $t=0$.

---

# 8. Stronger route: autonomous local encoding stage

The repository already contains the ingredients for a more complete protocol.

Use

$$
\boxed{
H
=H_m(u,p_u)+H_c(q_c,p_c)
-\sigma_zg(q_c)u.
}
$$

Interpret $q_c$ as a localized autonomous clock/controller coordinate.

Choose the initial state before the controller reaches the interaction region as

$$
\rho_G
\otimes
|0\rangle_m\langle0|
\otimes
\rho_c
\otimes
\rho_g,
$$

with the external gravitational state independent of the input register $G$.

When the controller enters the compact interaction region, the coupling generates mirrored mechanical trajectories.

For source branch $s=\pm1$,

$$
u_s(t)=s u_+(t).
$$

Because the branch Hamiltonians are related by mechanical parity,

$$
H_-=P_uH_+P_u^\dagger,
$$

and a parity-even initial mechanical state gives branch-related evolution.

The generalized force on the controller contains

$$
-\partial_{q_c}H
\supset
\sigma_zg'(q_c)u.
$$

Since

$$
\sigma_z u_s=s(su_+)=u_+,
$$

its semiclassical backreaction is branch common.

This is the correct structural mechanism for a local autonomous encoder.

---

# 9. What remains to make the autonomous encoder exact enough for the paper

The Hamiltonian symmetry is not yet the same thing as a fully solved spatial source.

A publication-grade encoder should establish:

1. the controller begins outside the interaction region with input-independent state;
2. its coupling turns on autonomously through local dynamics rather than an externally prescribed function of coordinate time;
3. the controller/hub reduced state is branch common to the required accuracy after preparation;
4. any controller–mechanical residual entanglement is bounded;
5. the complete spatial stress-energy during encoding is conserved;
6. all gravitational radiation produced during encoding is included in the outgoing source history;
7. after the encoding pulse, the controller leaves the source mode in the desired $|\pm\alpha_0\rangle$ pair for passive decay.

If these are shown, then the exact microcausal theorem applies from the beginning of the autonomous local encoding operation.

---

# 10. Important distinction: identical controller marginal vs factorized controller

Controlled parity can guarantee that the two branches give the same controller **marginal state** under the ideal symmetry.

That is enough to prevent the controller alone from serving as a local which-branch readout.

It does not automatically prove that, after encoding,

$$
|\Psi_s\rangle_{mc}
=|s\alpha_0\rangle_m\otimes|c_f\rangle_c.
$$

The controller may remain entangled with the mechanical mode in the same branch-symmetric way.

For the mechanical source mode to be an exact standalone Gaussian channel input, one should either

- engineer a controller trajectory that disentangles at the end of the encoding stage; or
- keep the controller as part of the source input system and propagate its residual correlations explicitly.

This is the next nontrivial source-preparation calculation.

---

# 11. A practical paper hierarchy

Until the autonomous encoder is fully solved, use three levels of claim.

## Level I — exact general causal theorem

For any genuinely local input encoding,

$$
\boxed{T_{\rm cap}\ge R/c.}
$$

This is model independent within the local-QFT assumptions of `MICROCAUSAL_REPLACER_THEOREM.md`.

## Level II — exact passive future-emission transfer model

Given a prepared source oscillator at a chosen initial slice, the future source→receiver Gaussian channel is calculable exactly in the Markov model.

This is where

$$
\eta_g\tau_f(t)>m_B(t)
$$

and the thermal generalization belong.

## Level III — explicit end-to-end physical encoding protocol

This requires solving the local autonomous preparation stage and including its radiation.

Do not imply Level III has been completed merely because Levels I and II are separately available.

---

# 12. Relation to gravitational dressing literature

Perturbative gravity does not admit naive strictly local gauge-invariant matter operators without gravitational dressing. This complicates exact tensor-factor statements for “source” and “field.”

For Experiment 01 this does not destroy the operational program, but it reinforces the need to phrase the causality result in terms of

- local source operations;
- source-controlled differences;
- accessible receiver observables;
- the radiative TT channel as an explicitly chosen effective subsystem.

The repository should avoid claiming an exact fundamental Hilbert-space factorization of full quantum gravity.

---

# 13. Adversarial verdict

The passive exponential source solves the **during-emission actuator problem**.

It does **not** by itself solve the **initial encoding problem**.

Therefore:

### PASS

- passive free decay as a conserved source-emission benchmark;
- source branching ratio $\eta_g$;
- passive source→receiver Gaussian composition;
- future radiative transfer after a specified source initial slice.

### NARROW

- the formula $R/c+t_{\rm load}$ should be called a passive future-transfer capability time unless the local encoding assumptions are explicitly supplied.

### OPEN

- an explicit autonomous local encoder that starts from an input-independent environment and ends with the desired mechanical branch state while keeping the controller sufficiently branch common/disentangled.

---

# 14. Recommended next calculation

Construct the minimal autonomous Gaussian controller model that implements

$$
|s\rangle_G|0\rangle_m|c_i\rangle
\longrightarrow
|s\rangle_G|s\alpha_0\rangle_m|c_f\rangle
$$

with the same $|c_f\rangle$ for $s=\pm1$ up to a controlled error.

Then derive

1. the complete encoding-stage quadrupole waveform;
2. the precursor graviton norm;
3. the residual controller overlap;
4. the total source-controlled channel including encoding + passive tail.

That would close the remaining gap between the abstract microcausal theorem and the explicit passive source benchmark.

---

## Background references

- W. Donnelly and S. B. Giddings, *Observables, gravitational dressing, and obstructions to locality and subsystems*, arXiv:1607.01025.
- W. Donnelly and S. B. Giddings, *Gravitational splitting at first order: Quantum information localization in gravity*, arXiv:1805.11095.
- A. Belenchia et al., *Quantum Superposition of Massive Objects and the Quantization of Gravity*, arXiv:1807.07015.
