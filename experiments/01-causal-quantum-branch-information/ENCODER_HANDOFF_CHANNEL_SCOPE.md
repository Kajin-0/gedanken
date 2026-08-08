# Encoder Handoff and the Scope of the Fixed Virtual Bosonic Channel

**Date:** 2026-08-08  
**Status:** **TIME-DOMAIN SCOPE CORRECTION — THE FOUR-FACTOR COEFFICIENT IS AN ACTUAL FIXED-INPUT BOSONIC TRANSMISSIVITY AFTER ENCODING COMPLETES; DURING ENCODING IT IS ONLY A RESPONSE COEFFICIENT RELATIVE TO THE EVENTUAL CODE NORM**

## 1. Why this distinction matters

`VIRTUAL_DIFFERENCE_MODE_REDUCTION.md` proves that any pair of opposite multimode coherent branch states can be compressed into one virtual difference mode.

However, the V6 physical protocol **creates** the bosonic branch separation dynamically from an initially branch-common work mode. During the encoder interval, the total bosonic branch-distance norm is still growing.

Therefore one must distinguish:

1. an instantaneous virtual difference mode defined from the branch state at that time;
2. the fixed virtual bosonic input mode defined once the local encoding has completed.

The standard one-mode channel theorem applies most cleanly to the second object.

---

# 2. Lossless encoder illustrates the issue exactly

Take the ideal sign-controlled encoder

$$
H_{\rm enc}
=\hbar g\sigma_z(a^\dagger w+a w^\dagger)
$$

with source vacuum and branch-common work mode amplitude

$$
\zeta.
$$

For branch

$$
s=\pm1,
$$

$$
\alpha_s(t)
=-is\zeta\sin(gt),
$$

while the work mode amplitude is branch common,

$$
\gamma_w(t)
=\zeta\cos(gt).
$$

After removing the common work displacement, the only bosonic branch difference lies in the source mode.

Hence the total branch-distance norm at time

$$
t
$$

is

$$
\boxed{
N_{\Delta,{\rm all}}(t)
=4|\zeta|^2\sin^2(gt).}
$$

It begins at zero and reaches

$$
4|\zeta|^2
$$

only at the half-swap

$$
gT=\pi/2.
$$

Thus before the handoff there is no fixed bosonic branch input of amplitude

$$
|\zeta|
$$

whose norm is merely being redistributed among passive output ports.

The branch separation itself is still being created by the controlled local unitary.

---

# 3. Damped encoder and exact handoff accounting

With total source damping

$$
\kappa_A
$$

and underdamped coupling

$$
\Omega=\sqrt{g^2-\kappa_A^2/16},
$$

the exact controller-empty time is

$$
\boxed{
T_*
=\frac{
\pi-\arctan(4\Omega/\kappa_A)
}{\Omega}.}
$$

At that time the source branch amplitude is

$$
\boxed{
|\alpha_s(T_*)|
=|\zeta|e^{-\kappa_AT_*/4}.}
$$

Therefore the branch distance remaining in the source mode is

$$
\boxed{
N_{\Delta,A}(T_*)
=4|\zeta|^2e^{-\kappa_AT_*/2}.}
$$

For vacuum Markov source output ports

$$
j
$$

with rates

$$
\kappa_j,
$$

the branch distance emitted during the encoder is

$$
\boxed{
N_{\Delta,j}^{\rm enc}
=4\frac{\kappa_j}{\kappa_A}
|\zeta|^2
\left(
1-e^{-\kappa_AT_*/2}
\right).}
$$

Summing all source output ports gives

$$
\sum_jN_{\Delta,j}^{\rm enc}
=4|\zeta|^2
\left(
1-e^{-\kappa_AT_*/2}
\right).
$$

Hence

$$
\boxed{
N_{\Delta,A}(T_*)
+
\sum_jN_{\Delta,j}^{\rm enc}
=4|\zeta|^2.}
$$

This identity is crucial.

At the controller-empty handoff, the complete bosonic branch-distance norm has reached the fixed value corresponding to a virtual coherent branch amplitude

$$
\boxed{A_0=|\zeta|.}
$$

The controller carries no branch difference.

---

# 4. Post-handoff dynamics are a fixed-input linear channel

After

$$
T_*,
$$

turn off the branch-dependent encoder coupling or let the controller remain in the branch-common vacuum sector.

The later source/field/receiver evolution is branch independent and linear.

Including all vacuum output ports, that global evolution is unitary on the bosonic dilation.

Therefore the total branch-distance norm is conserved:

$$
\boxed{
N_{\Delta,{\rm all}}(t)
=4A_0^2
=4|\zeta|^2,
\qquad t\ge T_*.}
$$

Only its distribution among

- residual source mechanics;
- gravitational radiation;
- nongravitational source loss;
- receiver memory;
- receiver outputs

changes with time.

Thus for

$$
t\ge T_*
$$

there is one fixed virtual difference mode

$$
d_0
$$

with branch amplitudes

$$
\pm A_0
$$

whose state is being propagated through an ordinary bosonic network.

---

# 5. Receiver transmissivity after handoff

Let the receiver memory branch-distance contribution at time

$$
t\ge T_*
$$

be

$$
N_{\Delta,B}(t)=4|\alpha_B(t)|^2.
$$

Then the exact pure-loss transmissivity from the fixed virtual input mode to the receiver is

$$
\boxed{
\eta_B(t)
=\frac{N_{\Delta,B}(t)}{4|\zeta|^2}.}
$$

For the vacuum one-way V6 network this is precisely the complete coherent-transfer coefficient

$$
\boxed{
\eta_B(t)
=\tau_{A\to B}(t).}
$$

When the source output is compressed into its normalized complete gravitational waveform,

$$
\boxed{
\tau_{A\to B}(t)
=\beta_{g,A}
\eta_{\rm store}
\beta_{g,B}
\mathcal T_f(t),
\qquad t\ge T_*.}
$$

The normalized waveform

$$
f
$$

may contain both

- encoder precursor radiation emitted before
  $$
  T_*;
  $$
- later passive-tail radiation.

There is no problem with including the precursor. At

$$
T_*
$$

it is already one component of the fixed global virtual-mode dilation.

---

# 6. Receiver interaction with precursor before handoff

At a sufficiently small separation, precursor radiation can reach and begin driving the receiver before

$$
T_*.
$$

That does **not** invalidate the physics.

It changes the formal interpretation during that early interval.

For

$$
t<T_*,
$$

define the instantaneous total branch distance

$$
\boxed{
N_{\Delta,{\rm all}}(t)
=4A^2(t).}
$$

The receiver occupies a fraction

$$
\boxed{
\eta_B^{\rm inst}(t)
=\frac{N_{\Delta,B}(t)}
{N_{\Delta,{\rm all}}(t)}.}
$$

At that instant the global state is still exactly reducible to a virtual binary-coherent mode of amplitude

$$
A(t),
$$

so the exact state-level negativity formula can be applied using

$$
A(t)
$$

and

$$
\eta_B^{\rm inst}(t).
$$

However the quantity normalized to the eventual completed code amplitude,

$$
\frac{N_{\Delta,B}(t)}{4|\zeta|^2},
$$

should then be called a **coherent response coefficient**, not the transmissivity of a fixed bosonic input mode that already existed at the initial time.

---

# 7. Why the distinction matters for the Gaussian non-EB theorem

The known binary-coherent Gaussian-channel theorem assumes a fixed bosonic input mode carrying the coherent branches before the channel acts.

For

$$
t\ge T_*,
$$

V6 satisfies that structure exactly through the virtual mode

$$
d_0.
$$

Therefore the channel statement

$$
\boxed{
\Phi_{d_0\to B}(t)
}
$$

and its Gaussian non-EB/NPT criterion are rigorous within the linear model.

For

$$
t<T_*,
$$

the physical process is instead

$$
\boxed{
\text{logical qubit}
+\text{branch-common work mode}
\to
\text{time-dependent multimode coherent branch state}.}
$$

That is a controlled-state-generation protocol, not yet a fixed-input one-mode bosonic channel.

Its entanglement should be evaluated directly at the state level through the instantaneous virtual-mode reduction rather than by inserting the eventual four-factor response coefficient into an abstract one-mode channel theorem.

---

# 8. Cleanest main-paper protocol

The main manuscript can avoid this subtlety almost entirely by defining two stages.

## Stage I — local encoding

From source time

$$
t_s
$$

to

$$
t_s+T_*:
$$

prepare the equal-charge hybrid source state with the exact local encoder.

The precursor radiation is included in the physical state and its total norm is known.

## Stage II — fixed virtual-mode link

At

$$
t_s+T_*:
$$

the controller is branch common and the complete branch-distance norm equals

$$
4|\zeta|^2.
$$

From this point onward, define the fixed virtual bosonic difference mode

$$
d_0
$$

and the source→receiver channel.

The receiver state at any later time includes the coherent effect of any precursor that has already arrived.

This staging preserves

- the true causal origin at
  $$
  t_s;
- the exact post-handoff bosonic channel structure;
- the finite precursor as a controlled correction rather than an omitted artifact.

---

# 9. Fast-encoder limit

If

$$
\kappa_A/g\ll1,
$$

the precursor branch-distance fraction is

$$
\boxed{
\epsilon_{\rm pre}
=1-e^{-\kappa_AT_*/2}
\simeq
\frac{\pi\kappa_A}{4g}.}
$$

Thus the ideal half-swap picture is recovered smoothly.

In that regime almost all branch separation is still in the mechanical source at handoff, and the distinction between

- ``prepare then transmit'';
- the exact finite-duration encoder

is parametrically small.

The full waveform calculation remains useful as a finite-

$$
g
$$

correction to the downstream receiver response.

---

# 10. Actively shaped source pulses after handoff

A different case occurs if the controller continues to drive the source after the nominal handoff in order to synthesize an arbitrary waveform.

Then the logical branch separation can continue to be generated or reshaped by the local control process.

The scalar output relation

$$
N_{\Delta,j}
=4\kappa_j\int|\alpha(t)|^2dt
$$

still correctly partitions the emitted branch record among Markov output ports.

However the process should be described as a **controlled source protocol**, not automatically as a time-independent one-mode channel acting on the handoff source oscillator.

At the end of a closed controlled cycle, when

- source mechanics returns branch common;
- controller returns branch common;
- the generated branch record resides in output modes,

one can again define a fixed final virtual difference mode and apply the same state-level reduction.

Thus active waveform engineering is completely compatible with the virtual-mode picture, but the timing of when the fixed bosonic code is defined must be stated honestly.

---

# 11. Causal front versus channel handoff time

The causal clock starts when the **local intervention begins**, not when the encoder finishes.

Therefore the earliest possible receiver dependence remains

$$
\boxed{
 t_{\rm causal}
\ge t_s+R/c
}
$$

for the centrally triggered compact-source idealization.

The fixed bosonic channel description begins later,

$$
\boxed{
 t_{\rm channel\ handoff}
=t_s+T_*.}
$$

These are different times.

There is no contradiction:

- source-controlled precursor effects may propagate causally before handoff;
- the **fixed-input bosonic channel theorem** is invoked only after the encoded bosonic code has been fully instantiated.

The main paper should not equate these two clocks.

---

# 12. Recommended manuscript wording

Replace any sentence implying that the fixed one-mode source channel exists from the instant the local qubit encoder turns on with:

> ``The local branch encoder first creates the bosonic code. At the controller-empty handoff, the complete branch-distance norm—including any encoder precursor already emitted—equals the norm of one fixed virtual coherent difference mode. Subsequent vacuum linear dynamics redistribute that fixed norm among source, field, receiver, and loss modes, so the receiver is exactly a pure-loss/Gaussian projection of the virtual mode. Before handoff, the process is instead a controlled state-generation protocol and its entanglement is evaluated directly from the instantaneous branch-conditioned coherent states.''

Also distinguish

$$
t_s
$$

(the causal origin) from

$$
t_s+T_*
$$

(the fixed bosonic-channel handoff).

---

# 13. Adversarial verdict

The local encoder does not invalidate the V6 bosonic channel reduction.

It imposes a time-domain scope:

$$
\boxed{
\text{during encoder: controlled qubit→multimode state generation},}
$$

$$
\boxed{
\text{after controller-empty handoff: fixed virtual bosonic channel}.}
$$

At the handoff, exact branch-distance accounting gives

$$
\boxed{
N_{\Delta,{\rm all}}
=4|\zeta|^2,}
$$

so every precursor, residual source component, and later emitted mode belongs to one fixed unitary dilation.

The four-factor link coefficient is therefore a genuine channel transmissivity after encoding completes, while the earlier-time causal precursor is a separate state-generation problem rather than a loophole.
