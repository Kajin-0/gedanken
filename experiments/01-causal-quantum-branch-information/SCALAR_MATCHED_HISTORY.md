# Scalar Matched-History Derivation

**Timestamp:** 2026-08-07 14:00 EDT  
**Status:** Technical toy-model derivation; not yet linearized gravity

This note derives the finite-time history-transfer functional for a massless scalar mediator and its long-time/damped limits.

---

## 1. Model and assumptions

Use a prescribed source-branch current difference

$$
\Delta J_A(\mathbf x,t)=s(\mathbf x)u(t),
$$

with a smooth spatial profile $s$ and smooth finite switching/history $u$. A harmonic probe $B$ at $\mathbf z_B$ couples linearly to a free massless scalar field. The first pass uses the weak one-way coherent-drive approximation:

- the source history is externally prescribed;
- source backreaction is neglected;
- the probe starts in its ground state;
- probe backreaction on the field is neglected when evaluating the leading complementary record;
- the field starts in vacuum unless otherwise stated.

The final gravity calculation must relax the prescribed-current approximation and use conserved total stress-energy.

---

## 2. Retarded probe response

The branch-dependent force on the probe is

$$
\Delta F_B(t)
=\lambda_B\int d^4x'\,G_R(x_B,t;x')\Delta J_A(x').
$$

With

$$
x_B=x_{\rm zpf}(a+a^\dagger),
$$

the branch-dependent coherent displacement difference at interrogation time $T$ is

$$
\Delta\alpha_B(T)
=\frac{i x_{\rm zpf}}{\hbar}
\int_0^Tdt\,e^{i\omega_Bt}\Delta F_B(t).
$$

Define

$$
r_T(t')
=\frac{i\lambda_Bx_{\rm zpf}}{\hbar}
\int_{t'}^Tdt\,e^{i\omega_Bt}
\int d^3x'\,G_R(x_B,t;\mathbf x',t')s(\mathbf x').
$$

Then

$$
\boxed{
\Delta\alpha_B(T)=\int_0^Tdt'\,r_T(t')u(t').
}
$$

For conditional coherent probe states,

$$
\chi_B
=-\ln(1-D_B^2)
=|\Delta\alpha_B|^2.
$$

Therefore

$$
\boxed{
\chi_B=\langle u,K_Bu\rangle,
\qquad
K_B=|r_T\rangle\langle r_T|.
}
$$

$K_B$ is rank one because the final ideal oscillator displacement is one complex mode amplitude.

---

## 3. Vacuum complementary record

Use the standard mode expansion of the free scalar field. For a prescribed classical current, the conditional vacuum output is a multimode coherent state. With

$$
\widetilde s(\mathbf k)=\int d^3x\,e^{-i\mathbf k\cdot\mathbf x}s(\mathbf x),
$$

$$
\widetilde u(\omega)=\int dt\,e^{i\omega t}u(t),
$$

the branch-difference coherent displacement has the structure

$$
\Delta\beta_{\mathbf k}
\propto
\frac{\widetilde s(\mathbf k)\widetilde u(\omega_k)}
{\sqrt{2\hbar\omega_k(2\pi)^3}}.
$$

Therefore the complementary history-coherence exponent is

$$
\boxed{
2\Gamma_\Xi
=\|\Delta\beta\|^2
=\int\frac{d^3k}{(2\pi)^3}
\frac{|\widetilde s(\mathbf k)|^2|\widetilde u(\omega_k)|^2}
{2\hbar\omega_k}
}
$$

within these conventions.

Define $S_E(\omega)\ge0$ by

$$
\boxed{
2\Gamma_\Xi
=\int\frac{d\omega}{2\pi}
S_E(\omega)|\widetilde u(\omega)|^2.
}
$$

Equivalently in time-domain operator notation,

$$
\boxed{2\Gamma_\Xi=\langle u,N_Tu\rangle.}
$$

For a simple isotropic scalar monopole source in $3+1$ dimensions,

$$
S_E(\omega)\propto
\omega|\widetilde s(\omega/c)|^2
$$

at low frequency. A spatially finite $s$ supplies a UV form factor.

---

## 4. History-transfer functional

The logarithmic witness becomes

$$
\boxed{
\mathcal M_\Xi[u]
=\chi_B-2\Gamma_\Xi
=\langle u,(K_B-N_T)u\rangle.
}
$$

This is a response-minus-record functional.

With a quadratic control budget

$$
\langle u,Wu\rangle=1,
$$

$$
\boxed{
\mathcal M_{\Xi,\max}
=\lambda_{\max}\left[
W^{-1/2}(K_B-N_T)W^{-1/2}
\right].
}
$$

If $N_T$ is positive definite on the relevant support, define

$$
\boxed{
\eta_T=\langle r_T,N_T^{-1}r_T\rangle.
}
$$

Because $K_B$ is rank one,

$$
\boxed{
\eta_T>1
\iff
\exists\,u:\mathcal M_\Xi[u]>0.
}
$$

The optimal complex-envelope history is

$$
\boxed{u_{\rm opt}\propto N_T^{-1}r_T.}
$$

The real-control problem is obtained by realifying/symmetrizing the kernels.

---

## 5. Gaussian spatial source

Take

$$
s(\mathbf x)
=\frac{Q}{(2\pi\sigma^2)^{3/2}}
\exp\left(-\frac{|\mathbf x|^2}{2\sigma^2}\right).
$$

Then

$$
\widetilde s(\mathbf k)
=Qe^{-\sigma^2k^2/2}.
$$

For $R\gg\sigma$, the source-to-probe retarded frequency response is approximately

$$
\mathcal G_s(\omega,R)
\simeq
\frac{Q}{4\pi R}
\exp\left(-\frac{\sigma^2\omega^2}{2c^2}\right)
 e^{i\omega R/c}
$$

up to the scalar-field normalization convention.

The vacuum record spectrum contains the same form factor,

$$
S_E(\omega)
\propto
\omega Q^2
\exp\left(-\frac{\sigma^2\omega^2}{c^2}\right).
$$

Thus in the narrow-band ratio

$$
\frac{|\mathcal G_s(\omega,R)|^2}{S_E(\omega)},
$$

the overall source strength $Q^2$ and the Gaussian source-size form factor cancel. The ideal transfer efficiency is therefore primarily a property of receiver coupling, frequency, distance, and the field channel rather than source amplitude.

This is the scalar analogue of the source-mass cancellation found in the radiation-limited gravity estimate.

---

## 6. Long-time / narrow-band limit

Let

$$
\tau=T-R/c>0
$$

be the causal interaction time. If $\tau$ is long enough that the response mode is narrow around $\omega_B$, define

$$
\mathcal R_B(\omega_B,R)
=\frac{\lambda_Bx_{\rm zpf}}{\hbar}
\int d^3x\,G_R(\omega_B;\mathbf z_B,\mathbf x)s(\mathbf x).
$$

Then

$$
\boxed{
\eta_T
\simeq
\tau\gamma_{\rm hist}(R,\omega_B),
}
$$

with

$$
\boxed{
\gamma_{\rm hist}(R,\omega_B)
=\frac{|\mathcal R_B(\omega_B,R)|^2}
{S_E(\omega_B)}.
}
$$

The optimized strong-witness onset is therefore

$$
\boxed{
T_*(R)
\simeq
\frac{R}{c}
+\gamma_{\rm hist}^{-1}(R,\omega_B).
}
$$

The first term is causal propagation; the second is coherent history-transfer buildup.

For the Gaussian scalar source, the low-frequency scaling is schematically

$$
\gamma_{\rm hist}
\propto
\frac{\lambda_B^2x_{\rm zpf}^2}{\hbar\omega_BR^2}
\propto
\frac{\lambda_B^2}{m_B\omega_B^2R^2},
$$

up to convention-dependent constants and powers of $c$.

---

## 7. Finite temperature

For a stationary thermal Gaussian field, the Hadamard/noise spectrum is enhanced by the fluctuation-dissipation factor

$$
S_E^{(T)}(\omega)
=S_E^{(0)}(\omega)
\coth\left(\frac{\hbar\omega}{2k_BT}\right)
$$

in the standard equilibrium normalization, while the retarded response is unchanged.

Therefore the history-transfer rate is suppressed approximately as

$$
\boxed{
\gamma_{\rm hist}^{(T)}
=\gamma_{\rm hist}^{(0)}
\tanh\left(\frac{\hbar\omega_B}{2k_BT}\right).
}
$$

At high temperature,

$$
\gamma_{\rm hist}^{(T)}
\sim
\gamma_{\rm hist}^{(0)}
\frac{\hbar\omega_B}{2k_BT}.
$$

This is a toy-model thermal penalty; the eventual gravity experiment also has ordinary mechanical/environmental thermal decoherence that must be added separately.

---

## 8. Probe damping and history cooperativity

Now include probe amplitude damping rate $\kappa_B$. In the narrow-band rotating-wave limit, the final displacement response mode has the form

$$
r_T(t)
\propto
\mathcal R_B(\omega_B,R)
 e^{-\kappa_B(T_R-t)/2}e^{i\omega_Bt},
$$

where $T_R=T-R/c$.

If $S_E(\omega)$ is nearly constant over the probe linewidth,

$$
\boxed{
\eta_T
\simeq
\mathcal C_{\rm hist}
\left(1-e^{-\kappa_BT_R}\right),
}
$$

where

$$
\boxed{
\mathcal C_{\rm hist}
\equiv
\frac{|\mathcal R_B(\omega_B,R)|^2}
{\kappa_BS_E(\omega_B)}.
}
$$

This is a cooperativity-like dimensionless history-transfer efficiency.

A positive optimized strong witness is possible at finite damping only if

$$
\boxed{\mathcal C_{\rm hist}>1.}
$$

When this holds, the approximate causal buildup time is

$$
\boxed{
T_*(R)
\simeq
\frac{R}{c}
-
\frac{1}{\kappa_B}
\ln\left(1-\frac{1}{\mathcal C_{\rm hist}}\right).
}
$$

For $\mathcal C_{\rm hist}\gg1$ this reduces to the undamped result

$$
T_*(R)-R/c
\simeq
\gamma_{\rm hist}^{-1}.
$$

Physical interpretation: once the receiver has finite memory time, waiting indefinitely cannot compensate for a channel that leaks branch information faster than the receiver can coherently store it.

---

## 9. Pure-loss channel benchmark

If one effective branch displacement is split passively with transmissivity $\tau_{\rm ch}$,

$$
\chi_B=\tau_{\rm ch}|\Delta|^2,
$$

$$
2\Gamma_\Xi=(1-\tau_{\rm ch})|\Delta|^2,
$$

so

$$
\boxed{
\mathcal M_\Xi=(2\tau_{\rm ch}-1)|\Delta|^2.
}
$$

The strong witness is positive iff

$$
\tau_{\rm ch}>1/2.
$$

This coincides with the pure-loss bosonic degradable/antidegradable boundary. It does not imply entanglement is absent below $1/2$; the present witness is sufficient rather than necessary.

---

## 10. Gravity implications

For the Newtonian near-zone branch-dependent force,

$$
\Delta F_B(t)
\simeq
\frac{2Gm_Am_B}{R^3}\Delta x_A(t-R/c),
$$

so

$$
|\mathcal R_B^{(G)}|^2\propto R^{-6}.
$$

Source-generated fundamental radiation/decoherence does not receive the same receiver-distance factor. Hence schematically

$$
\gamma_{\rm hist}^{(G)}\propto R^{-6},
$$

and, in the undamped build-up regime,

$$
T_*(R)-R/c\propto R^6.
$$

This exposes a strong causality-versus-coupling tradeoff: making $R/c$ easier to resolve destroys near-field transfer efficiency rapidly.

With probe damping, the natural gravity target becomes a history-cooperativity condition

$$
\boxed{
\mathcal C_{\rm hist}^{(G)}>1,
}
$$

with the numerator supplied by the retarded tidal response and the denominator by probe memory loss times the complementary gravitational record spectrum.

A correct gravity calculation must include the conserved stress-energy of the complete source-plus-actuator system.

---

## 11. Novelty discipline

Matched filters, cooperativity, scalar quantum communication, fluctuation-dissipation theory, and the pure-loss $50\%$ threshold are established concepts. No novelty claim is attached to those mathematical structures.

The potentially distinctive physics target is their use in the gravity-specific history problem:

$$
\boxed{
\text{causal branch transfer}
+\text{recoverable-history witness}
+\text{complementary gravitational record}
+\text{optimal spacetime source history}.
}
$$

The most important next step is not additional analogy. It is to replace the scalar current by a conserved weak-field stress-energy difference and calculate the gravitational equivalents of $\mathcal R_B$, $S_E$, and $\mathcal C_{\rm hist}$.
