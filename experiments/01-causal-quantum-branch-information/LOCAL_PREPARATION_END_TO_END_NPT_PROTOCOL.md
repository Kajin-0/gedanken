# Local Preparation → Conserved Gravity → Noisy Receiver NPT Protocol

**Date:** 2026-08-07  
**Status:** **END-TO-END PROTOCOL THEOREM WITH EXPLICIT LOCAL CAUSAL ORIGIN — GAUSSIAN SIGN THEOREM IS PRIOR ART, GRAVITY CONSTRUCTION IS THE APPLICATION**

## 1. Purpose

The repository now has all ingredients needed to state the cleanest current experiment without assuming that a branch-displaced gravitating source already existed at the causal origin.

The protocol is

$$
\boxed{
\text{degenerate local reference qubit}
+
\text{branch-common work mode}
\xrightarrow{\text{local encoder}}
R{:}A\text{ coherent-branch probe}
\xrightarrow{\text{conserved source emission}}
\text{graviton difference mode}
\xrightarrow{\text{retarded capture}}
B.
}
$$

The reference qubit $R$ remains at the source.

The Gaussian non-entanglement-breaking statement belongs to the **bosonic source/gravitational mode → receiver channel**, not to a reduced qubit→receiver map.

---

# 2. Initial local state

Before the causal source operation begins, choose

$$
\boxed{
|\Psi(0)\rangle
=
\frac{|0\rangle_R+|1\rangle_R}{\sqrt2}
\otimes
|0\rangle_A
\otimes
|\beta\rangle_C
\otimes
|0\rangle_E.
}
$$

Here

- $R$ is a degenerate internal reference/control qubit;
- $A$ is the finite-spoke plus mode, initially in vacuum;
- $C$ is a compact energetic work/controller mode, initially branch common;
- $E$ contains source vacuum output ports, including the gravitational vacuum.

The logical states of $R$ should be chosen so that their local stress-energy is identical to the working perturbative accuracy.

The mechanical source itself is branch common before the encoder starts.

---

# 3. Local sign-controlled encoder

Use the source-local interaction

$$
\boxed{
H_{\rm enc}
=
\hbar g\,\sigma_z
(a^\dagger c+a c^\dagger).
}
$$

The complete modal solution is derived in

- `EXACT_LOCAL_GAUSSIAN_SOURCE_ENCODER.md`.

For vacuum source-loss ports there is a finite controller-empty time $T_*$ at which

$$
\boxed{
|\Psi(T_*)\rangle
=
|0\rangle_C
\otimes
\frac{
|0\rangle_R|+\alpha_*\rangle_A|E_+^{\rm enc}\rangle
+
|1\rangle_R|-\alpha_*\rangle_A|E_-^{\rm enc}\rangle
}{\sqrt2},
}
$$

up to branch-common phases and a choice of quadrature convention.

The controller is exactly

- branch independent;
- vacuum;
- factorized.

Any radiation generated during the local encoder is included in

$$
|E_s^{\rm enc}\rangle.
$$

It is not discarded as a preparation artifact.

---

# 4. Complete source output after passive decay

After $T_*$, decouple the controller locally and allow the finite-spoke source mode to decay through its physical output ports.

Let

$$
\boxed{
\kappa_A
=\kappa_{g,A}
+\sum_\ell\kappa_{\ell,A}
}
$$

and define

$$
\boxed{
\eta_g
=\frac{\kappa_{g,A}}{\kappa_A}.
}
$$

For vacuum nongravitational ports, all source signal amplitudes share the same complete normalized encoder-plus-tail temporal waveform.

After the source has fully emptied, the branch-conditioned output can therefore be compressed into

- one normalized gravitational mode $G$;
- one collective orthogonal loss mode $L$.

The state has the exact coherent form

$$
\boxed{
|\Psi\rangle_{RGL}
=
\frac1{\sqrt2}
\left(
|0\rangle_R
|+\sqrt{\eta_g}\,\beta\rangle_G
|+\sqrt{1-\eta_g}\,\beta\rangle_L
+
|1\rangle_R
|-\sqrt{\eta_g}\,\beta\rangle_G
|-\sqrt{1-\eta_g}\,\beta\rangle_L
\right),
}
$$

up to known branch-common phase-space rotations.

The precise temporal split between encoding precursor and passive tail does not change the port branching fractions.

---

# 5. Equivalent pure-loss source channel

Trace the unobserved source-loss mode $L$.

The resulting $R{:}G$ state is exactly what one obtains by applying a pure-loss channel

$$
\boxed{
\mathcal L_{\eta_g}
}
$$

to the bosonic half of the virtual binary coherent state

$$
\boxed{
|\Psi_\beta\rangle_{RA_0}
=
\frac{
|0\rangle_R|+\beta\rangle_{A_0}
+
|1\rangle_R|-\beta\rangle_{A_0}
}{\sqrt2}.
}
$$

Therefore

$$
\boxed{
\rho_{RG}
=
(I_R\otimes\mathcal L_{\eta_g})
(|\Psi_\beta\rangle\langle\Psi_\beta|).
}
$$

This is an **equivalent channel representation** of the locally generated output state. It does not require the virtual bosonic mode $A_0$ to have existed as a branch-displaced gravitating system before the local encoder.

---

# 6. Explicit gravitational source normalization

The source mode is the conserved finite-spoke quadrupole from

- `CONSERVED_SOURCE_ACTUATOR_AUDIT.md`;
- `QUANTIZED_PLUS_MODE_SOURCE.md`.

For

$$
q_A=\omega L_A/c_{s,A},
$$

$$
\boxed{
\kappa_{g,A}(q_A)
=
\frac{8G\mu_A L_A^2\omega^4}{5c^5}
\mathcal C_\kappa(q_A),
}
$$

with

$$
\boxed{
\mathcal C_\kappa(q)
=
\frac{(\tan q/q)^2}
{\frac12+q/\sin2q}.
}
$$

The graviton branch-distance normalization is externally cross-checked against Matsui 2026 in

- `MATSUI_NDELTA_NORMALIZATION_CROSSCHECK.md`.

---

# 7. Retarded gravitational mode at the receiver

Let the source–receiver distance be $R$.

The complete source difference waveform is retarded by

$$
\boxed{R/c.}
$$

In the aligned wave-zone compact-source limit,

$$
\boxed{
\eta_{\rm store}
=
\frac{25\mathcal O}{16(kR)^2}
}
$$

for spatial/polarization mode overlap $\mathcal O$.

The receiver useful loading rate is

$$
\boxed{
\kappa_\Delta
=\eta_{\rm store}\kappa_{g,B}.
}
$$

Finite-spoke matrix-element corrections cancel from the **normalized** compact-source $25/16$ coefficient while remaining in the absolute source/receiver linewidths.

---

# 8. Complete encoder-plus-tail temporal mode

Let

$$
f_{\rm full}(t)
$$

be the normalized source temporal mode derived in

- `LOCAL_BOSONIC_INPUT_SWAP_CHANNEL.md`.

The same mode shape applies to the branch-dependent output of the sign-controlled coherent encoder because the conditioned source equations differ only by the overall branch sign.

For a constant-$g$ encoding interval,

$$
\boxed{
f_{\rm full}(t)
=
\sqrt{\kappa_A}\frac g\Omega
 e^{-\kappa_A t/4}\sin(\Omega t),
\qquad0<t<T_*,
}
$$

and

$$
\boxed{
f_{\rm full}(t)
=
\sqrt{\kappa_A}
 e^{-\kappa_A T_*/4}
 e^{-\kappa_A(t-T_*)/2},
\qquad t>T_*.
}
$$

It satisfies

$$
\boxed{
\int_0^\infty|f_{\rm full}(t)|^2dt=1.
}
$$

The encoding precursor norm is

$$
\boxed{
\epsilon_{\rm pre}
=1-e^{-\kappa_AT_*/2}
\simeq
\frac{\pi\kappa_A}{4g}
}
$$

for $g\gg\kappa_A$.

---

# 9. Receiver Gaussian channel

Let receiver-local time $t$ be measured after the earliest causal arrival from the beginning of the local encoder.

The normalized incident gravitational mode → receiver map is

$$
\boxed{
\Phi_B(t)
=
\Phi_{\tau_{\rm full}(t),m_B(t)},
}
$$

with

$$
\boxed{
\tau_{\rm full}(t)
=
\kappa_\Delta
\left|
\int_0^t ds\,
 e^{-\kappa_B(t-s)/2}
 f_{\rm full}(s)
\right|^2.
}
$$

The receiver vacuum-output occupation is

$$
\boxed{
m_B(t)
=n_0e^{-\kappa_Bt}
+
\frac{\Gamma_{{\rm th},B}}{\kappa_B}
(1-e^{-\kappa_Bt}).
}
$$

---

# 10. Complete source-output → receiver composition

The source loss stage is

$$
\mathcal L_{\eta_g}.
$$

The receiver stage is

$$
\Phi_{\tau_{\rm full},m_B}.
$$

For vacuum source-loss ports,

$$
\boxed{
\Phi_{\rm eff}(t)
=
\Phi_B(t)\circ\mathcal L_{\eta_g}
=
\Phi_{\eta_g\tau_{\rm full}(t),m_B(t)}.
}
$$

The useful coherent transfer is therefore

$$
\boxed{
\tau_{\rm eff}(t)
=\eta_g\tau_{\rm full}(t).
}
$$

---

# 11. Exact NPT condition for the locally prepared probe

The phase-insensitive binary coherent survival theorem is established prior art in substance and must not be claimed as new.

Applying that theorem to the equivalent channel representation above gives, for every finite

$$
\beta\ne0,
$$

$$
\boxed{
\rho_{RB}(t)
\text{ is NPT}
\iff
\eta_g\tau_{\rm full}(t)>m_B(t).
}
$$

Thus the same inequality simultaneously gives

- the non-EB boundary of the effective bosonic source-output→receiver channel; and
- the NPT boundary of the explicit locally prepared source-reference probe.

The source branch amplitude controls the **magnitude** of the surviving entanglement but not the sign boundary.

---

# 12. Exact pre-light-cone statement

Let the local encoder begin at source time

$$
t_s=0.
$$

For receiver events spacelike separated from the encoder support, microcausality gives no source-operation dependence of the receiver state.

Therefore

$$
\boxed{
\tau_{\rm full}^{\rm ret}(t)=0,
\qquad
 t<R/c,
}
$$

for the source-controlled signal component.

Hence

$$
\boxed{
\rho_{RB}(t)
\text{ cannot acquire entanglement from this local preparation protocol before causal contact.}
}
$$

This statement does not deny pre-existing vacuum correlations. It refers only to entanglement carried/generated by the localized source operation relative to the common pre-encoding state.

---

# 13. Causal NPT capability window

Define receiver-local time after earliest arrival

$$
\theta=t-R/c.
$$

The locally prepared gravitational probe is NPT at the receiver when

$$
\boxed{
\eta_g\tau_{\rm full}(\theta)
>m_B(\theta).
}
$$

Define

$$
\boxed{
T_{\rm NPT}(R)
=
\frac Rc
+
\inf\left\{
\theta>0:
\eta_g\tau_{\rm full}(\theta)>m_B(\theta)
\right\}.
}
$$

If the source waveform has finite loading support in the receiver, a second crossing defines the closing time of the quantum-capability bubble.

---

# 14. Matched passive/high-Q limit

When

$$
\kappa_A=\kappa_B=\kappa
$$

and

$$
\kappa/g\ll1,
$$

the exact full-waveform maximum is

$$
\boxed{
\tau_{\rm full}^{\max}
=
4e^{-2}
\frac{\kappa_\Delta}{\kappa}
\left[
1+\left(1-\frac\pi4\right)
\frac\kappa g
+O\left(\frac{\kappa^2}{g^2}\right)
\right].
}
$$

Therefore the source-resolved end-to-end maximum is

$$
\boxed{
\tau_{\rm eff}^{\max}
=
4e^{-2}
\eta_g
\frac{\kappa_\Delta}{\kappa}
\left[
1+\left(1-\frac\pi4\right)
\frac\kappa g
+O\left(\frac{\kappa^2}{g^2}\right)
\right].
}
$$

The local encoder changes the passive exponential benchmark only at controlled relative order

$$
O(\kappa/g).
$$

---

# 15. Stationary thermal receiver threshold

For a receiver initially in its stationary thermal state,

$$
m_B(t)=n_{\rm th,B}.
$$

A nonempty NPT interval exists iff

$$
\boxed{
 n_{\rm th,B}
<
\eta_g\tau_{\rm full}^{\max}.
}
$$

In the fast-encoder matched limit,

$$
\boxed{
 n_{\rm th,B}
<
4e^{-2}
\eta_g
\frac{\kappa_\Delta}{\kappa}
\left[
1+\left(1-\frac\pi4\right)
\frac\kappa g
+\cdots
\right].
}
$$

This is the clean local-preparation analogue of the passive end-to-end threshold.

---

# 16. What is genuinely gravity-specific here

None of the following generic ingredients should be sold as new:

- coherent-state Gaussian channel survival;
- beam-splitter state transfer;
- graviton coherent states from a classical/semiclassical source;
- quantum GW → resonant receiver coupling;
- use of an EB threshold.

The project-specific construction is the quantitative composition of

1. an explicitly local branch preparation with branch-common controller;
2. a conserved finite-mass elastic gravitational source;
3. an externally cross-checked graviton branch-distance normalization;
4. normalized retarded free-space storage;
5. source branching loss;
6. receiver thermal noise;
7. finite-source/controller error bounds;
8. a causal NPT capability interval.

---

# 17. Remaining physical caveat

The sign-controlled swap is exact at the normal-mode level.

A full microscopic implementation would still need the spatial stress-energy of

- the resonant source/controller coupler;
- its branch-common switching mechanism;
- any finite controller mode support.

These do not create an uncontrolled branch record in the ideal modal solution, but they remain part of the physical source error budget.

The existing hub/controller quadrupole bound is the correct place to control them.

---

# 18. Adversarial verdict

The project now has a coherent end-to-end protocol in which

- the mechanical source is branch common before the causal operation;
- the branch-dependent quadrupole is created locally;
- the work controller returns to the same state;
- encoding radiation is included;
- the complete conserved source output is normalized;
- ordinary source loss is included;
- free-space capture is retarded and normalized;
- receiver noise is included;
- the final source-reference/receiver NPT boundary is explicit.

At the current model level,

$$
\boxed{
\rho_{RB}(t)\text{ NPT}
\iff
\eta_g\tau_{\rm full}(t)>m_B(t).
}
$$

The next strongest attack should therefore move away from missing modal pieces and toward either

1. the spatial stress-energy realization of the local coupler; or
2. a final gravity-specific prior-art audit of the **complete local-preparation + conserved radiative source + noisy receiver** protocol.
