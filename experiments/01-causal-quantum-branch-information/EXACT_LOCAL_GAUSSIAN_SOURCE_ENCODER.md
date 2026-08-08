# Exact Local Gaussian Encoder with a Branch-Common Controller

**Date:** 2026-08-07  
**Status:** **MODAL ENCODER CLOSED — EXACT COHERENT-STATE TRANSFER WITH CONTROLLER FACTORIZATION; SPATIAL COUPLER MICROPHYSICS REMAINS AN ERROR-BUDGET ITEM**

## 1. Purpose

`PASSIVE_SOURCE_INITIALIZATION_CAUSALITY_AUDIT.md` identified the remaining gap between

1. the exact microcausal source-controlled theorem; and
2. the passive future-emission source model.

The missing ingredient was a local encoder that starts with an input-independent mechanical source/controller state and creates opposite mechanical coherent branches without leaving the controller as an uncontrolled which-branch record.

At the normal-mode level there is an unusually simple exact solution.

Use a resonant auxiliary controller oscillator $c$ and the finite-spoke plus mode $a$, with a source qubit controlling only the **sign** of an energy-conserving beam-splitter interaction.

The controller remains branch common throughout the ideal encoding and can be exactly emptied at the handoff to passive emission.

---

# 2. Local mode model

Let

- $a$ = finite-spoke source plus mode;
- $c$ = compact auxiliary controller/work mode;
- $\sigma_z|s\rangle=s|s\rangle$, $s=\pm1$;
- both bosonic modes have resonance frequency $\omega$.

Take

$$
H_0
=\hbar\omega(a^\dagger a+c^\dagger c),
$$

and during the local encoding gate

$$
\boxed{
H_{\rm enc}
=\hbar g\,\sigma_z
(a^\dagger c+a c^\dagger).
}
$$

In the resonant interaction picture,

$$
\boxed{
H_I
=\hbar g\,\sigma_z
(a^\dagger c+a c^\dagger).
}
$$

The interaction is number conserving:

$$
\boxed{
[H_I,a^\dagger a+c^\dagger c]=0.
}
$$

Thus the controller supplies the source mechanical excitation by coherent state transfer rather than by branch-dependent work.

The sign change between $s=+1$ and $s=-1$ is related by mechanical parity,

$$
P_a aP_a^\dagger=-a,
$$

so

$$
H_{I,-}=P_aH_{I,+}P_a^\dagger.
$$

---

# 3. Exact lossless encoder

For branch $s$, define

$$
U_s(t)
=\exp\left[
-isgt(a^\dagger c+a c^\dagger)
\right].
$$

The mode transformation is

$$
\boxed{
a(t)=a(0)\cos(gt)-is\,c(0)\sin(gt),}
$$

$$
\boxed{
c(t)=c(0)\cos(gt)-is\,a(0)\sin(gt).}
$$

Start with

$$
|0\rangle_a|\beta\rangle_c.
$$

Because a passive linear-optical unitary maps products of coherent states to products of coherent states,

$$
\boxed{
|0\rangle_a|\beta\rangle_c
\longrightarrow
|-is\beta\sin(gt)\rangle_a
|\beta\cos(gt)\rangle_c.
}
$$

The controller amplitude

$$
\beta\cos(gt)
$$

is **independent of $s$ at every time**.

Hence for an arbitrary source-qubit state

$$
|\psi\rangle_G
=c_+|+\rangle+c_-|-\rangle,
$$

the total state is

$$
\boxed{
|\Psi(t)\rangle
=
|\beta\cos(gt)\rangle_c
\otimes
\left[
 c_+|+\rangle|-i\beta\sin(gt)\rangle_a
+c_-|-\rangle|+i\beta\sin(gt)\rangle_a
\right].
}
$$

Therefore the controller is not merely locally indistinguishable between branches. It is **exactly factorized from the source qubit and mechanical branch degree of freedom** throughout the ideal gate.

---

# 4. Exact half-swap

Choose

$$
\boxed{gT=\frac\pi2.}
$$

Then

$$
\cos(gT)=0,
\qquad
\sin(gT)=1,
$$

and

$$
\boxed{
|\Psi(T)\rangle
=|0\rangle_c
\otimes
\left[
 c_+|+\rangle|-i\beta\rangle_a
+c_-|-\rangle|+i\beta\rangle_a
\right].
}
$$

If one wants real mechanical coherent amplitudes $\pm\alpha_0$, choose

$$
\boxed{
\beta=i\alpha_0.
}
$$

Then

$$
\boxed{
|\psi\rangle_G|0\rangle_a|i\alpha_0\rangle_c
\longrightarrow
|0\rangle_c
\otimes
\left[
 c_+|+\rangle|+\alpha_0\rangle_a
+c_-|-\rangle|-\alpha_0\rangle_a
\right].
}
$$

This is exactly the desired local branch encoder at the modal level.

---

# 5. Energy bookkeeping

The initial controller mean excitation is

$$
\langle n_c\rangle=|\beta|^2.
$$

At the half-swap,

$$
\langle n_c\rangle=0,
$$

and each mechanical branch has

$$
\langle n_a\rangle=|\beta|^2.
$$

The two branches have identical energy because

$$
|+\alpha_0|^2=|-\alpha_0|^2.
$$

Thus the branch label changes only the phase/sign of the state transfer, not the amount of controller energy consumed.

This gives a concrete realization of the earlier qualitative statement that the source controller can supply equal work in the two branches.

---

# 6. Mechanical displacement and quadrupole

For the finite-spoke plus mode,

$$
u
=u_{\rm zpf}(a+a^\dagger).
$$

For real mechanical amplitude $s\alpha_0$,

$$
\boxed{
\langle u\rangle_s
=2s u_{\rm zpf}\alpha_0.
}
$$

The branch-difference outer displacement is

$$
\boxed{
\Delta u
=4u_{\rm zpf}\alpha_0.
}
$$

The one-branch plus quadrupole is

$$
\delta Q_{xx}
=4\mu L\frac{\tan q}{q}u,
$$

so the encoded branch-difference expectation is

$$
\boxed{
\langle\Delta Q_{xx}\rangle
=16\mu L u_{\rm zpf}\alpha_0
\frac{\tan q}{q},
}
$$

with

$$
\langle\Delta Q_{yy}\rangle
=-\langle\Delta Q_{xx}\rangle.
$$

The finite-spoke normalization therefore enters exactly as in the existing source model.

---

# 7. Include source damping during the encoder

Now let the mechanical source mode have total amplitude-decay rate

$$
\boxed{
\kappa_A=\sum_j\kappa_j,
}
$$

including the gravitational port and any ordinary vacuum loss ports.

Take the controller mode to be lossless over the short encoding interval.

For branch $s$, coherent amplitudes obey

$$
\dot\alpha_s
=-\frac{\kappa_A}{2}\alpha_s
-isg\gamma_s,
$$

$$
\dot\gamma_s
=-isg\alpha_s.
$$

Define

$$
b_s=s\alpha_s.
$$

Then

$$
\dot b_s
=-\frac{\kappa_A}{2}b_s
-ig\gamma_s,
$$

$$
\dot\gamma_s
=-igb_s,
$$

which are independent of $s$.

Thus the controller coherent amplitude remains branch common even with damping.

---

# 8. Exact damped solution

For

$$
\boxed{g>\kappa_A/4,}
$$

define

$$
\boxed{
\Omega
=\sqrt{g^2-\frac{\kappa_A^2}{16}}.
}
$$

With

$$
\alpha_s(0)=0,
\qquad
\gamma_s(0)=\beta,
$$

the exact coherent amplitudes are

$$
\boxed{
\gamma_s(t)
=\beta e^{-\kappa_A t/4}
\left[
\cos(\Omega t)
+\frac{\kappa_A}{4\Omega}
\sin(\Omega t)
\right],
}
$$

and

$$
\boxed{
\alpha_s(t)
=-is\beta
\frac{g}{\Omega}
 e^{-\kappa_A t/4}
\sin(\Omega t).
}
$$

Again,

$$
\gamma_s(t)=\gamma(t)
$$

is exactly branch independent.

---

# 9. Exact controller-empty handoff despite damping

Choose the first positive time $T_*$ satisfying

$$
\boxed{
\cos(\Omega T_*)
+\frac{\kappa_A}{4\Omega}
\sin(\Omega T_*)=0.
}
$$

Equivalently,

$$
\boxed{
\tan(\Omega T_*)
=-\frac{4\Omega}{\kappa_A},
}
$$

with the root in the second quadrant,

$$
\boxed{
T_*
=\frac{
\pi-\arctan(4\Omega/\kappa_A)
}{\Omega}.
}
$$

At this root,

$$
\sin(\Omega T_*)=\frac{\Omega}{g},
$$

$$
\cos(\Omega T_*)=-\frac{\kappa_A}{4g}.
$$

Therefore

$$
\boxed{
\gamma_s(T_*)=0,
}
$$

and

$$
\boxed{
\alpha_s(T_*)
=-is\beta e^{-\kappa_A T_*/4}.
}
$$

So the controller can still be emptied **exactly** at a finite handoff time even when the source mode radiates/loses energy during the encoding stage.

In the weak-damping limit,

$$
T_*
=\frac\pi{2g}
+O\left(\frac{\kappa_A}{g^2}\right).
$$

---

# 10. Exact controller factorization for vacuum loss ports

For vacuum source-loss inputs, the conditioned source/controller/bath dynamics is a passive linear Gaussian network driven by

- one coherent controller input;
- mechanical vacuum;
- bath vacua.

A passive linear network maps these inputs to a multimode product of coherent states.

Therefore for each branch $s$ the complete conditioned state has the form

$$
|\alpha_s(t)\rangle_a
|\gamma(t)\rangle_c
\bigotimes_j|\mathcal E_{j,s}(t)\rangle,
$$

where the bath coherent amplitudes reverse sign with $s$ while the controller amplitude does not.

At $T_*$,

$$
\boxed{
|\gamma(T_*)\rangle_c=|0\rangle_c.
}
$$

Hence the controller is exactly

1. branch independent;
2. vacuum;
3. disentangled from the source qubit, mechanics, and emitted vacuum-port fields.

This closes the modal controller-factorization problem identified in `PASSIVE_SOURCE_INITIALIZATION_CAUSALITY_AUDIT.md` for the clean vacuum-loss benchmark.

---

# 11. Controller energy needed for a target source amplitude

Suppose the desired mechanical handoff amplitude is

$$
\boxed{|\alpha_s(T_*)|=\alpha_0.}
$$

Then choose

$$
\boxed{
|\beta|
=\alpha_0e^{\kappa_A T_*/4}.
}
$$

The controller begins with slightly more coherent excitation than remains in the mechanical mode because some energy is emitted during the local encoder.

The overhead is

$$
\boxed{
\frac{|\beta|^2}{\alpha_0^2}
=e^{\kappa_A T_*/2}.
}
$$

For

$$
g\gg\kappa_A,
$$

this approaches unity.

---

# 12. Encoding-stage radiation is a calculable precursor

Let bath channel $j$ have rate

$$
\kappa_j,
$$

and define

$$
\eta_j=\frac{\kappa_j}{\kappa_A}.
$$

The branch difference of the source coherent amplitude is

$$
\Delta\alpha_a(t)=2\alpha_+(t),
$$

up to the phase convention.

The coherent branch distance emitted into channel $j$ during encoding is

$$
N_{\Delta,j}^{\rm enc}
=\kappa_j
\int_0^{T_*}dt\,
|\Delta\alpha_a(t)|^2.
$$

Instead of performing the integral directly, use excitation conservation for one conditioned branch:

$$
\frac{d}{dt}
\left(
|\alpha_s|^2+|\gamma|^2
\right)
=-\kappa_A|\alpha_s|^2.
$$

Since

$$
|\gamma(0)|^2=|\beta|^2,
$$

$$
|\alpha_s(0)|^2=0,
$$

and

$$
|\gamma(T_*)|^2=0,
$$

$$
|\alpha_s(T_*)|^2
=|\beta|^2e^{-\kappa_AT_*/2},
$$

we obtain

$$
\boxed{
\kappa_A
\int_0^{T_*}dt\,
|\alpha_s(t)|^2
=|\beta|^2
\left(
1-e^{-\kappa_AT_*/2}
\right).
}
$$

Therefore

$$
\boxed{
N_{\Delta,j}^{\rm enc}
=4\eta_j|\beta|^2
\left(
1-e^{-\kappa_AT_*/2}
\right).
}
$$

For the gravitational port,

$$
\boxed{
N_{\Delta,g}^{\rm enc}
=4\eta_g|\beta|^2
\left(
1-e^{-\kappa_AT_*/2}
\right),
}
$$

where

$$
\eta_g=\kappa_{g,A}/\kappa_A.
$$

The preparation radiation is therefore explicit and cannot be silently omitted.

---

# 13. Mechanical branch distance available for the passive tail

At the handoff,

$$
\boxed{
N_{\Delta,m}(T_*)
=|\alpha_+(T_*)-\alpha_-(T_*)|^2
=4|\beta|^2e^{-\kappa_AT_*/2}.
}
$$

If the source subsequently decays passively through the same ports, the gravitational branch distance emitted in the tail is

$$
\boxed{
N_{\Delta,g}^{\rm tail}
=4\eta_g|\beta|^2e^{-\kappa_AT_*/2}.
}
$$

Thus

$$
\boxed{
N_{\Delta,g}^{\rm enc}
+N_{\Delta,g}^{\rm tail}
=4\eta_g|\beta|^2.
}
$$

The analogous identity holds for every independent loss port.

The local encoder therefore partitions, rather than hides, the branch-dependent outgoing coherent field.

---

# 14. Precursor fraction

The fraction of the total gravitational branch distance emitted during encoding is

$$
\boxed{
\epsilon_{\rm pre}
\equiv
\frac{N_{\Delta,g}^{\rm enc}}
{N_{\Delta,g}^{\rm enc}+N_{\Delta,g}^{\rm tail}}
=1-e^{-\kappa_AT_*/2}.
}
$$

For

$$
g\gg\kappa_A,
$$

$$
T_*\simeq\frac\pi{2g},
$$

so

$$
\boxed{
\epsilon_{\rm pre}
\simeq
\frac{\pi\kappa_A}{4g}
+O\left(\frac{\kappa_A^2}{g^2}\right).
}
$$

Thus precursor radiation is unavoidable for a genuine local encoding, but it can be made parametrically small relative to the passive tail while remaining explicitly accounted for.

---

# 15. Causal origin

Unlike a pre-existing branch-displaced mechanical state, the present modal protocol can start from

$$
\boxed{
\rho_G
\otimes
|0\rangle_a\langle0|
\otimes
|\beta\rangle_c\langle\beta|
\otimes
|0\rangle_E\langle0|,
}
$$

where the environment and energetic controller are independent of the source-qubit input state.

The local source input influences the rest of the system only when the sign-controlled interaction is enabled in the source region.

Therefore the operational microcausal theorem can take the beginning of this local gate as its causal origin.

Every graviton emitted during the gate is part of the source-controlled signal and reaches a distant receiver only after retarded propagation from its emission event.

---

# 16. Local switching of the coupling

The exact modal gate requires the source/controller interaction to be disabled after the controller-empty time $T_*$ so that the mechanical mode can enter passive free decay rather than swap back into the controller.

This can be represented by a branch-independent local coupling envelope

$$
g\to g(t).
$$

In the ideal lossless resonant model, because the interaction-picture generator is the same operator at every time,

$$
[H_I(t),H_I(t')]=0,
$$

and the coherent transformation depends only on the pulse area

$$
\Theta=\int dt\,g(t).
$$

A smooth pulse with

$$
\boxed{\Theta=\pi/2}
$$

therefore implements the same exact half-swap while avoiding an abrupt coupling quench.

The coupling envelope itself is branch common. Any compact branch-dependent energy-density residual of its physical switching apparatus belongs to the same controller error budget bounded in `HUB_CONTROLLER_RESIDUAL_BOUND.md`.

For the damped exact-root construction, a smooth finite switch-off near $T_*$ produces a controllable perturbation; the constant-$g$ solution above gives the analytic benchmark.

---

# 17. What is and is not closed

## Closed at the normal-mode quantum level

The encoder now explicitly provides

$$
\boxed{
\text{independent local source input}
\to
\text{opposite mechanical coherent branches}
}
$$

with

- equal branch energies;
- exact controller branch independence;
- exact controller factorization in the ideal coherent/vacuum benchmark;
- exact controller-empty handoff;
- calculable encoding-stage radiation;
- parametrically small precursor fraction for $g\gg\kappa_A$.

## Still not a microscopic material design

The file does **not** derive

- a specific microscopic device realizing the $\sigma_z$-controlled resonant beam-splitter coupling;
- the full spatial stress-energy tensor of that coupler during switching;
- finite-temperature controller noise;
- counter-rotating corrections when $g/\omega$ is not small.

These are implementation/error-budget questions, not an unresolved modal factorization problem.

---

# 18. Required operating hierarchy

A clean parameter regime is

$$
\boxed{
\kappa_A\ll g\ll\omega.
}
$$

The first inequality gives

- high-fidelity state transfer;
- small precursor fraction;
- short encoding relative to passive decay.

The second supports the resonant rotating-wave beam-splitter description.

For the gravitationally dominated ideal source,

$$
\kappa_A\simeq\kappa_{g,A}
$$

is extraordinarily small, leaving a very large formal scale separation available in a Gedanken model.

---

# 19. Consequence for the full source→receiver channel

The complete source-controlled radiation waveform now has two pieces:

1. the finite local encoding precursor on $0<t<T_*$;
2. the passive source tail after $T_*$.

Let their branch-difference gravitational amplitudes be combined into the single normalized outgoing difference mode

$$
f_{\rm full}(t)
\propto
\Delta b_g^{\rm out}(t).
$$

The total coherent branch distance is the norm of the entire waveform, including both pieces.

A receiver sees the retarded version

$$
f_{\rm full}(t-R/c).
$$

The causal front begins from the first nonzero local encoder output, not from the end of the gate.

In the regime

$$
\epsilon_{\rm pre}\ll1,
$$

the passive exponential tail remains the dominant normalized source mode and the existing passive source→receiver formulas become a controlled approximation to the complete local-encoding protocol.

---

# 20. Strongest current source chain

At the modal level the source architecture can now be written as

$$
\boxed{
\text{source qubit}
\xrightarrow{\text{local sign-controlled swap}}
\text{finite-spoke plus mode}
\xrightarrow{\text{passive radiation}}
\text{graviton difference mode}.
}
$$

The controller can begin energetic but source-input independent and end in the same vacuum state in both branches.

This directly bridges the abstract microcausal source-input theorem to the explicit passive radiation source without assuming that a branch-displaced mechanical state appears from nowhere at the causal origin.

---

# 21. Next calculation

The next useful refinement is no longer controller factorization. It is the **receiver response to the complete encoder-plus-tail waveform**.

Calculate

$$
\tau_{\rm full}(t)
=
\kappa_\Delta
\left|
\int_0^t ds\,
 e^{-\kappa_B(t-s)/2}
 f_{\rm full}(s)
\right|^2,
$$

and compare it with the pure exponential-tail approximation.

In the controlled regime

$$
\kappa_A/g\ll1,
$$

the difference should scale with the small precursor norm

$$
\epsilon_{\rm pre}
\simeq\pi\kappa_A/(4g).
$$

This will quantify exactly how close the fully locally encoded causal protocol is to the simpler passive end-to-end channel.
