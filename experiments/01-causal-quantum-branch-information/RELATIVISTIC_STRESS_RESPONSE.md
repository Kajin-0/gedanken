# Relativistic Receiver: Passive Smeared Stress-Energy Response

**Timestamp:** 2026-08-07 16:15 EDT  
**Status:** Active theoretical formulation for Experiment 01

This note develops the relativistic analogue of the nonrelativistic quadrupole receiver bound without making the unjustified substitution $Q_{ij}\to T_{ij}$. The robust object is a **smeared stress-energy response spectrum**.

---

## 1. Linearized gravity couples to stress energy

In linearized gravity,

$$
\boxed{
H_I(t)
=-\frac12
\int d^3x\,
h_{\mu\nu}(t,\mathbf x)
T^{\mu\nu}(t,\mathbf x).
}
$$

Choose a real, smooth, compactly supported tensor smearing $f_{\mu\nu}(\mathbf x)$ representing one receiver mode / gravitational field profile and define the Hermitian receiver operator

$$
\boxed{
F_f
=\int d^3x\,
f_{\mu\nu}(\mathbf x)
T^{\mu\nu}(\mathbf x).
}
$$

For a normalized graviton mode, the exact relation between $f_{\mu\nu}$ and the field normalization carries the appropriate powers of $G$, $\hbar$, and mode volume. The purpose here is first to isolate the receiver's intrinsic matter response.

---

## 2. Passive stationary spectral representation

Let

$$
\rho=\sum_mp_m|m\rangle\langle m|
$$

commute with the receiver Hamiltonian.

Define the Kubo susceptibility

$$
\chi_f(t)
=\frac{i}{\hbar}\Theta(t)
\operatorname{Tr}\rho
[F_f(t),F_f(0)].
$$

For positive frequency,

$$
\boxed{
\chi_f''(\omega)
=\frac{\pi}{\hbar}
\sum_{m<n}
(p_m-p_n)
|F^f_{mn}|^2
\delta(\omega-\omega_{nm}),
}
$$

where

$$
\omega_{nm}=(E_n-E_m)/\hbar.
$$

If the state is thermodynamically passive,

$$
E_m<E_n\Rightarrow p_m\ge p_n,
$$

then

$$
\boxed{
\chi_f''(\omega)\ge0
\qquad(\omega>0).
}
$$

Thus the absorptive response of a passive relativistic receiver is a positive spectral measure, just as in the nonrelativistic quadrupole problem.

---

## 3. General energy-weighted sum rule

The spectral representation gives

$$
\int_0^\infty d\omega\,
\omega\chi_f''(\omega)
=
\frac{\pi}{\hbar^2}
\sum_{m<n}
(p_m-p_n)(E_n-E_m)|F^f_{mn}|^2.
$$

Whenever the renormalized double commutator is well defined,

$$
\boxed{
\int_0^\infty d\omega\,
\omega\chi_f''(\omega)
=
\frac{\pi}{2\hbar^2}
\left\langle
[F_f,[H,F_f]]
\right\rangle_{\rm ren}.
}
$$

This is the relativistic response-budget identity that survives independently of a particle-coordinate quadrupole model.

---

## 4. Passive band bound

Because

$$
\chi_f''(\omega)\ge0
$$

for a passive state, the response in any positive-frequency band $\mathcal B$ with lower edge $\omega_{\min}>0$ satisfies

$$
\boxed{
\int_{\mathcal B}d\omega\,
\chi_f''(\omega)
\le
\frac{\pi}{2\hbar^2\omega_{\min}}
\left\langle
[F_f,[H,F_f]]
\right\rangle_{\rm ren}.
}
$$

This is the direct relativistic analogue of the logic used for the passive quadrupole receiver:

> a passive receiver has a finite amount of positive absorptive spectral weight available in a chosen frequency band, **if** the smeared renormalized double commutator is finite.

---

## 5. Why there is no universal compactness ceiling yet

For the nonrelativistic coordinate quadrupole,

$$
[Q,[H,Q]]
$$

reduced to a simple positive geometric operator because

- the kinetic energy was quadratic in momentum;
- the potential commuted with the coordinate quadrupole.

For a relativistic stress-energy operator this simplification does not generally occur.

Stress-energy tensors are composite local operators. Their equal-time commutators can contain

- derivatives of delta functions;
- contact terms;
- Schwinger/anomaly terms;
- renormalization-dependent local pieces.

Therefore one cannot currently replace the right-hand side by a universal expression such as

$$
MR^2
$$

without specifying the quantum field theory, the smearing, and the renormalization prescription.

The correct conclusion is:

$$
\boxed{
\text{passive spectral positivity survives;
 the simple geometric ceiling does not automatically survive.}
}
$$

---

## 6. Gravitational receiver spectral density

For a normalized linearized-gravity mode $u_{\mu\nu}(x)$, define the corresponding smeared matter operator

$$
F_u
=\int d^3x\,
u_{\mu\nu}(\mathbf x)T^{\mu\nu}(\mathbf x),
$$

where $\nu_{\mu\nu}$ contains the spatial/polarization profile and normalization of the mode at the receiver.

The receiver's graviton absorption/emission spectral density is built from the matrix elements

$$
|\langle n|F_u|m\rangle|^2
$$

multiplied by the universal linearized-gravity field normalization.

Schematically,

$$
\boxed{
J_g^{(u)}(\omega)
\propto
G\,\omega^{\alpha}
\chi_u''(\omega),
}
$$

where the exact power and tensor normalization depend on whether $u$ is represented through $h_{\mu\nu}$, the electric Weyl tensor, or another gauge-invariant normalized mode variable.

The receiver problem can therefore be stated entirely in terms of a **projected stress-energy spectral function**.

---

## 7. Thermal equilibrium ties noise to response

For a Gibbs state, the KMS/detailed-balance relation gives

$$
S_f(-\omega)
=e^{-\beta\hbar\omega}S_f(+\omega),
$$

where $S_f$ is the unsymmetrized stress-energy fluctuation spectrum of the smeared operator.

The commutator spectrum is

$$
S_f(+\omega)-S_f(-\omega),
$$

so the fluctuation-dissipation relation ties the absorptive response to equilibrium noise.

Thus increasing a passive thermal receiver's gravitational absorptive spectral weight necessarily increases the associated equilibrium stress-energy fluctuations according to the KMS factor.

This is the relativistic field-theory version of the same response-versus-noise tension encountered earlier in oscillator language.

---

## 8. Mode selectivity remains independent

Even if a relativistic receiver has a large total stress-energy response, only the projection onto the source branch-difference graviton mode is useful.

Let the source mode be $u_S$ and receiver radiative mode be $u_B$. Define

$$
\mathcal O_{SB}=|\langle u_B|u_S\rangle|^2.
$$

The useful response spectrum is the projection into that shared mode, while orthogonal stress-energy/gravitational channels contribute to the complementary record.

Therefore the same two-resource structure survives:

$$
\boxed{
\text{total passive response budget}
\times
\text{source-mode overlap}.
}
$$

The nonrelativistic quantities $\mathfrak R_B$ and $\mathcal O_{SB}$ should be viewed as one concrete realization of this more general structure.

---

## 9. Active relativistic receiver

For a nonpassive stationary state, some population differences are inverted and $\chi_f''(\omega)$ can become negative over frequency bands: the system supplies energy and acts as an amplifier.

Then the positive-term band bound no longer follows from the double-commutator identity alone.

This is the relativistic analogue of the active collective loophole.

However, an active receiver must also possess enhanced fluctuation/noise channels. The correct figure of merit remains the distance of the full source-receiver quantum channel from entanglement breaking, not the magnitude of $\chi''$ alone.

---

## 10. A candidate relativistic receiver functional

Define the useful gravitational response in the source mode by a positive-frequency functional

$$
\boxed{
\mathcal R_u[\mathcal B]
=\int_{\mathcal B}d\omega\,
W_g(\omega)\chi_u''(\omega),
}
$$

where $W_g(\omega)$ contains the normalized graviton mode density/coupling factors.

For passive states,

$$
\mathcal R_u[\mathcal B]\ge0.
$$

A corresponding noise functional can be constructed from the symmetrized or complementary stress-energy spectrum,

$$
\mathcal N_u[\mathcal B]
=\int_{\mathcal B}d\omega\,
W_g(\omega)S_{u,H}(\omega).
$$

The relativistic analogue of the earlier history-transfer problem is therefore to determine whether

$$
\boxed{
\mathcal R_u
\text{ can exceed the classical/separable noise cost }
\mathcal N_u
}
$$

for the source-matched gravitational mode while respecting causality.

The exact inequality has not yet been derived here.

---

## 11. What would count as a genuine relativistic theorem

A strong paper-level result would have the form:

> For every passive relativistic receiver satisfying specified locality, energy, and support assumptions, a source-matched gravitational response functional obeys
> 
> $$
> \mathcal R_u\le\mathcal B[T_{\mu\nu},f,\rho],
> $$
> 
> where $\mathcal B$ is finite, renormalization-controlled, and accompanied by a corresponding minimum complementary-noise functional.

Then one could compare that bound with an explicitly quantum gravitational source-to-receiver channel.

At present, only the abstract spectral positivity and double-commutator identity are established in our derivation; the closed relativistic bound remains open.

---

## 12. Novelty discipline

Stress-tensor spectral functions, Kubo response, fluctuation-dissipation relations, Schwinger/contact terms, and stress-tensor sum rules are established QFT topics. There are also many theory-specific stress-tensor sum rules in thermal/QCD/conformal systems.

No novelty is claimed for the general spectral identity above.

The research opportunity is whether the **causal gravitational quantum-receiver problem** selects a useful smeared stress-energy functional for which a finite, theory-controlled receiver bound can be proved and connected to history-coherence transfer.

---

## 13. Immediate next step

Test the relativistic framework in the simplest explicit QFT: a free massive scalar receiver field in a finite spatial smearing. Compute

$$
\langle[F_f,[H,F_f]]\rangle
$$

and the corresponding stress-energy spectral density explicitly. This will show whether the relativistic receiver bound is finite after smearing and what replaces the nonrelativistic compactness factor.