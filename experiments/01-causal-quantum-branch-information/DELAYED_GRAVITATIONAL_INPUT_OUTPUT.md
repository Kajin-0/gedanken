# Delayed Gravitational Source-to-Receiver Input-Output Map

**Timestamp:** 2026-08-07 17:40 EDT  
**Status:** Linearized/RWA common-field derivation establishing the coherent storage amplitude from the retarded source-receiver self-energy. This resolves the storage-versus-scattering factor-of-two ambiguity.

## 1. Goal

For the wave-zone Gedanken receiver we need the coherent amplitude with which a normalized outgoing gravitational branch mode from source $A$ enters receiver $B$.

Three related quantities must be kept distinct:

1. reciprocal retarded self-energy $\Sigma_{BA}^{R}$;
2. common-bath collective damping $\Gamma_{BA}$;
3. one-way source-output $\rightarrow$ receiver-input **storage amplitude** $t_{BA}^{\rm store}$.

The first two are related by the imaginary part of the Green function. The third is obtained by comparing the actual source output field with the receiver input drive.

---

## 2. Generic continuum model

Work near one resonant transition frequency $\omega_0$ and use an RWA form for two localized quadrupole modes $a_A,a_B$ coupled to continuum graviton channels $b_\lambda(\omega)$:

$$
\frac{H_I}{\hbar}
=i\sum_{j=A,B}\sum_\lambda
\int_0^\infty d\omega
\left[
 g_{j\lambda}(\omega)
 b_\lambda^\dagger(\omega)a_j
-
 g_{j\lambda}^*(\omega)
a_j^\dagger b_\lambda(\omega)
\right].
$$

All propagation phases, TT polarization contractions, and source/receiver spatial structure are included in $g_{j\lambda}(\omega)$.

The field equation is

$$
\dot b_\lambda(\omega,t)
=-i\omega b_\lambda(\omega,t)
+\sum_jg_{j\lambda}(\omega)a_j(t).
$$

Its formal solution is

$$
b_\lambda(\omega,t)
=e^{-i\omega(t-t_0)}b_\lambda(\omega,t_0)
+
\sum_jg_{j\lambda}(\omega)
\int_{t_0}^{t}ds\,
e^{-i\omega(t-s)}a_j(s).
$$

Substituting into the receiver equation gives

$$
\dot a_B(t)
=
\text{free/input terms}
-
\int_{t_0}^{t}ds\,
K_{BB}(t-s)a_B(s)
-
\int_{t_0}^{t}ds\,
K_{BA}(t-s)a_A(s),
$$

where the cross kernel is

$$
\boxed{
K_{BA}(\tau)
=
\sum_\lambda
\int_0^\infty d\omega\,
 g_{B\lambda}^*(\omega)
 g_{A\lambda}(\omega)
e^{-i(\omega-\omega_0)\tau}.
}
$$

This is the common-field source-to-receiver memory kernel.

---

## 3. Retarded far-zone reduction

For localized source and receiver separated by $R$, the propagating part of the kernel is retarded. In a narrow-band/Markov treatment around $\omega_0$,

$$
K_{BA}(\tau)
\rightarrow
 i\Sigma_{BA}^{R}(\omega_0,R)
\delta(\tau-R/c)
$$

up to the overall Hamiltonian/input-output phase convention.

Thus the source-dependent term in the receiver equation is

$$
\boxed{
\dot a_B(t)\big|_A
=-i\Sigma_{BA}^{R}(\omega_0,R)
 a_A(t-R/c).
}
$$

The complete complex self-energy contains both coherent/dispersive and radiative pieces. For the aligned plus quadrupoles derived earlier,

$$
\boxed{
\Sigma_{BA}^{R}
=\frac54
\sqrt{\kappa_{g,A}\kappa_{g,B}}
\frac{P(\epsilon)e^{i\epsilon}}{\epsilon^5},
\qquad
\epsilon=\omega_0R/c.
}
$$

---

## 4. Source output field

The source's normalized outgoing field satisfies the standard input-output relation

$$
\boxed{
b_{\rm out,A}(t)
=b_{\rm in,A}(t)
+\sqrt{\kappa_{g,A}}\,a_A(t).
}
$$

For the source-generated contribution with vacuum input,

$$
\boxed{
b_{\rm out,A}^{(S)}(t)
=\sqrt{\kappa_{g,A}}\,a_A(t).
}
$$

Here $b_{\rm out,A}^{(S)}$ denotes the normalized branch-mode component of the complete gravitational output associated with the source transition. Orthogonal continuum modes are handled by the mode-overlap decomposition.

---

## 5. Receiver input field

Let the source output reach the source-matched receiver input mode with complex amplitude $t_{BA}^{\rm store}$:

$$
\boxed{
b_{\rm in,B}^{(S)}(t)
=t_{BA}^{\rm store}\,
 b_{\rm out,A}^{(S)}(t-R/c).
}
$$

The receiver input-output equation is

$$
\dot a_B
=-\frac{\kappa_{g,B}}2a_B
+\sqrt{\kappa_{g,B}}\,b_{\rm in,B}
+\cdots.
$$

Therefore the source-dependent receiver drive is

$$
\dot a_B(t)\big|_A
=t_{BA}^{\rm store}
\sqrt{\kappa_{g,A}\kappa_{g,B}}
 a_A(t-R/c).
$$

Compare with the retarded field-elimination result,

$$
\dot a_B(t)\big|_A
=-i\Sigma_{BA}^{R}a_A(t-R/c).
$$

Hence

$$
\boxed{
t_{BA}^{\rm store}
=
\frac{-i\Sigma_{BA}^{R}}
{\sqrt{\kappa_{g,A}\kappa_{g,B}}}
}
$$

up to an irrelevant convention-dependent global phase.

This is the source-output $\rightarrow$ receiver-input amplitude relevant to coherent storage and state transfer.

---

## 6. Exact aligned-plus storage amplitude

Insert the exact plus-quadrupole self-energy:

$$
\boxed{
t_{BA}^{\rm store}(\epsilon)
=-\frac{5i}{4}
\frac{P(\epsilon)e^{i\epsilon}}
{\epsilon^5}.
}
$$

In the wave zone,

$$
P(\epsilon)\simeq\epsilon^4,
$$

so

$$
\boxed{
t_{BA}^{\rm store}
\simeq
-\frac{5i}{4}
\frac{e^{i\epsilon}}{\epsilon}.
}
$$

Thus

$$
\boxed{
\eta_{BA}^{\rm store}
=|t_{BA}^{\rm store}|^2
\simeq
\frac{25}{16(kR)^2}.
}
$$

For imperfect tensor/polarization/temporal matching,

$$
\boxed{
\eta_{BA}^{\rm store}
=\frac{25\mathcal O}{16(kR)^2},
\qquad 0\le\mathcal O\le1.
}
$$

---

## 7. Why collective damping contains a factor of two

Eliminating a reciprocal common bath gives a two-system master equation whose cross terms have the standard structure

$$
\dot\rho
\supset
-i[J_{AB}a_A^\dagger a_B+\mathrm{h.c.},\rho]
+
\Gamma_{AB}
\left(
 a_B\rho a_A^\dagger
-\frac12\{a_A^\dagger a_B,\rho\}
+\mathrm{h.c.}
\right).
$$

The complex self-energy can be written schematically as

$$
\Sigma_{AB}^{R}
=J_{AB}-i\Gamma_{AB}/2
$$

or the equivalent convention with real/imaginary parts interchanged by the chosen Fourier phase.

Therefore

$$
\boxed{
\Gamma_{AB}
=2\,|\operatorname{Im}\Sigma_{AB}^{R}|
}
$$

in the convention used by the common-bath check.

That factor two is the conversion from **self-energy amplitude** to a **decay rate**. It does not imply

$$
t_{BA}^{\rm store}=2\Sigma_{AB}^{R}/\sqrt{\kappa_A\kappa_B}.
$$

Conflating these two relations produces the factor-of-four error in storage probability.

---

## 8. Absorption versus scattering cross-section check

For the aligned plus quadrupole, the on-axis source power fraction is

$$
\frac1{P_G}
\frac{dP_G}{d\Omega}\bigg|_z
=\frac{5}{8\pi}.
$$

Using the storage efficiency

$$
\eta_{\rm store}
=\frac{25}{16k^2R^2}
$$

in

$$
\eta
=\frac1{P_G}\frac{dP_G}{d\Omega}\bigg|_z
\frac{\sigma}{R^2}
$$

gives

$$
\boxed{
\sigma_{\rm abs,max}^{(l=2)}
=\frac{5\pi}{2k^2}.
}
$$

This is the critical-coupling maximum absorptive/storage cross-section for one $l=2$ channel.

The factor-four larger unitary scattering value is

$$
\boxed{
\sigma_{\rm sca,max}^{(l=2)}
=\frac{10\pi}{k^2}.
}
$$

The quantum-memory problem uses the absorptive/storage coefficient, not the full scattering coefficient.

The dipole analogue provides the same check:

$$
\sigma_{\rm abs,max}^{(l=1)}
=\frac{3\pi}{2k^2},
\qquad
\sigma_{\rm sca,max}^{(l=1)}
=\frac{6\pi}{k^2}.
$$

---

## 9. Receiver linewidth bookkeeping

The receiver's total graviton linewidth

$$
\kappa_{g,B}
$$

is intrinsic and independent of source range.

The source branch mode occupies only a fraction

$$
\eta_{BA}^{\rm store}(R)
$$

of the receiver's gravitational bath. Therefore

$$
\boxed{
\kappa_\Delta(R)
=\eta_{BA}^{\rm store}(R)\kappa_{g,B},
}
$$

while

$$
\kappa_{g,\perp}
=\kappa_{g,B}-\kappa_\Delta(R).
$$

Thus

$$
\boxed{
\kappa_{\rm tot}
=\kappa_{g,B}+\kappa_i+\cdots
}
$$

is range independent.

This point is important for the correct spacetime front: range weakens the selected input channel, not the receiver's intrinsic lifetime.

---

## 10. Consequence for Experiment 01

For the far-zone aligned resonant receiver,

$$
\boxed{
\kappa_\Delta(R)
=\frac{25\mathcal O}{16(kR)^2}
\kappa_{g,B}.
}
$$

The exact binary-coherent thermal theorem then gives the NPT capability condition

$$
\boxed{
\frac{25\mathcal O}{16(kR)^2}
\kappa_{g,B}
>\Gamma_{\rm th}.
}
$$

Everything entering the quantum reception cone is now tied to

- a retarded Green function;
- intrinsic graviton linewidths;
- ordinary input-output normalization;
- receiver thermal noise.

No geometric receiver area needs to be assumed for the compact resonant architecture.

---

## 11. Literature connection

Standard input-output theory relates a localized system's internal amplitude to normalized travelling input/output modes via its coupling rate. Pulse-mode/cascaded formulations make the source-output $\rightarrow$ receiver-input interpretation explicit.

The gravitational retarded Green kernel used here is independently consistent with linearized-gravity resonance calculations of quadrupole-coupled objects.

The derivation above is therefore primarily a normalization/identification step: it connects those two established structures in the specific gravitational receiver model.

---

## 12. Remaining scope

The derivation uses

- weak linearized gravity;
- one resonant quadrupole transition per system;
- RWA/narrow-band input-output language;
- far-zone interpretation when $\Sigma^R$ is converted to a propagating transmission amplitude;
- a source-matched normalized mode decomposition.

Near-zone virtual/reactive interactions are contained in $\Sigma^R$ but should not be interpreted as a pure-loss propagation transmissivity.
