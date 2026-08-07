# Current State — Experiment 01

**Last updated:** 2026-08-07 13:58 EDT  
**Experiment:** Causal Transport of Quantum Branch Information by Gravity

This is the compact recovery point. Earlier derivations are preserved in `PROGRESS_LOG.md` and `checkpoints/`.

## Core operational witness

For a balanced source path qubit,

$$
\rho_{AB}(T)=\frac12
\begin{pmatrix}
\rho_L(T) & \Xi_T\\
\Xi_T^\dagger & \rho_R(T)
\end{pmatrix}.
$$

Define

$$
C_\Xi=\|\Xi_T\|_1,
\qquad
D_B=\frac12\|\rho_L-\rho_R\|_1.
$$

Every balanced separable source-probe state satisfies

$$
\boxed{C_\Xi^2+D_B^2\le1.}
$$

The preferred logarithmic witness is

$$
\Gamma_\Xi=-\ln C_\Xi,
\qquad
\chi_B=-\ln(1-D_B^2),
$$

$$
\boxed{
\mathcal M_\Xi
=\chi_B-2\Gamma_\Xi.
}
$$

Every separable state satisfies

$$
\boxed{\mathcal M_\Xi\le0,}
$$

so $\mathcal M_\Xi>0$ certifies source-probe entanglement.

For pure conditional global histories,

$$
\boxed{C_\Xi=F(\rho_E^L,\rho_E^R),}
$$

so $C_\Xi$ measures how indistinguishable the **unobserved complementary records** of the two histories remain. This avoids assuming a fundamental factorization into source, gravitational field, and probe Hilbert spaces.

## Causality

For a controllable source operation at $t=0$ and separation $R$,

$$
D_B(T,R)=0
\qquad T<R/c
$$

for the source-controlled contribution.

Define

$$
T_*(R)=\inf\{T:\mathcal M_\Xi(T,R)>0\}.
$$

Locality requires

$$
\boxed{T_*(R)\ge R/c.}
$$

## Scalar-field toy model

Use a source-current difference

$$
\Delta J_A(\mathbf x,t)=s(\mathbf x)u(t)
$$

and a harmonic probe linearly coupled to a massless scalar field. In the weak one-way coherent-drive approximation define

$$
r_T(t')
=\frac{i\lambda_Bx_{\rm zpf}}{\hbar}
\int_{t'}^Tdt\,e^{i\omega_Bt}
\int d^3x'\,G_R(x_B,t;\mathbf x',t')s(\mathbf x').
$$

Then

$$
\Delta\alpha_B=\langle r_T,u\rangle,
\qquad
\chi_B=|\Delta\alpha_B|^2
=\langle u,K_Bu\rangle,
$$

with

$$
K_B=|r_T\rangle\langle r_T|.
$$

Write the complementary history-record cost as

$$
2\Gamma_\Xi=\langle u,N_Tu\rangle,
$$

where $N_T\succeq0$ is obtained from the Hadamard/noise sector. Therefore

$$
\boxed{
\mathcal M_\Xi[u]
=\langle u,(K_B-N_T)u\rangle.
}
$$

The retarded kernel carries the useful branch response; the Hadamard/complementary kernel measures branch information leaked into unobserved outputs.

## Matched-history optimization

Under a quadratic source-control budget $\langle u,Wu\rangle=1$,

$$
\boxed{
\mathcal M_{\Xi,\max}
=\lambda_{\max}\left[
W^{-1/2}(K_B-N_T)W^{-1/2}
\right].
}
$$

Because $K_B$ is rank one, if $N_T$ is invertible on the relevant support define

$$
\boxed{
\eta_T=\langle r_T,N_T^{-1}r_T\rangle.
}
$$

Then

$$
\boxed{
\eta_T>1
\iff
\exists\,u:\mathcal M_\Xi[u]>0.
}
$$

The optimal complex-envelope source history is

$$
\boxed{u_{\rm opt}\propto N_T^{-1}r_T.}
$$

This is a **noise-whitened matched history**: the source trajectory is matched to the time-reversed retarded probe mode after whitening by the environment's ability to record the branch.

## Explicit vacuum field-record kernel

For a prescribed classical current coupled linearly to a free scalar field initially in vacuum, the two branch-conditioned field states are coherent states. With Fourier conventions

$$
\widetilde s(\mathbf k)=\int d^3x\,e^{-i\mathbf k\cdot\mathbf x}s(\mathbf x),
\qquad
\widetilde u(\omega)=\int dt\,e^{i\omega t}u(t),
$$

the branch-dependent field-mode displacement has the structure

$$
\Delta\beta_{\mathbf k}
\propto
\frac{\widetilde s(\mathbf k)\widetilde u(\omega_k)}
{\sqrt{2\hbar\omega_k(2\pi)^3}}.
$$

Hence

$$
\boxed{
2\Gamma_\Xi
=\|\Delta\beta\|^2
=\int\frac{d^3k}{(2\pi)^3}
\frac{|\widetilde s(\mathbf k)|^2|\widetilde u(\omega_k)|^2}
{2\hbar\omega_k},
}
$$

within the drive-only vacuum model. A finite spatial profile and smooth switching are essential; pointlike abrupt currents create ultraviolet artifacts.

Equivalently define a positive radiation/record spectrum $S_E(\omega)$ by

$$
\boxed{
2\Gamma_\Xi
=\int\frac{d\omega}{2\pi}
S_E(\omega)|\widetilde u(\omega)|^2.
}
$$

For an isotropic simple scalar monopole source in $3+1$D vacuum, $S_E(\omega)$ is Ohmic at low frequency,

$$
S_E(\omega)\propto\omega|\widetilde s(\omega/c)|^2.
$$

## Long-time / narrow-band limit

For an interaction window

$$
\tau=T-R/c
$$

long compared with the probe period and with $S_E(\omega)$ slowly varying across the Fourier width $\sim1/\tau$, the response mode is narrow around $\omega_B$. Define the source-to-probe frequency response

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
\tau\,\gamma_{\rm hist}(R,\omega_B),
}
$$

where the **history-transfer rate** is

$$
\boxed{
\gamma_{\rm hist}(R,\omega_B)
\equiv
\frac{|\mathcal R_B(\omega_B,R)|^2}
{S_E(\omega_B)}.
}
$$

Normalization factors are fixed by the chosen field/current conventions; the ratio is defined operationally by the preceding quadratic forms.

Therefore the optimized strong-witness onset is approximately

$$
\boxed{
T_*(R)
\simeq
\frac{R}{c}
+
\gamma_{\rm hist}^{-1}(R,\omega_B).
}
$$

This produces a **two-stage causal delay**:

1. light-travel delay $R/c$;
2. coherent history-transfer build time $1/\gamma_{\rm hist}$.

## Source strength cancels from the ideal threshold

In a linear mediator, both the useful exponent $\chi_B$ and complementary leakage exponent $2\Gamma_\Xi$ scale quadratically with the source-history amplitude. Therefore the dimensionless efficiency $\eta_T$ and the sign threshold $\eta_T>1$ are independent of the overall source amplitude.

Increasing source mass, scalar charge, or branch separation increases the **magnitude** of a measurable witness but does not by itself improve the ideal fraction of branch information reaching the intended probe rather than the complement.

This explains the source-mass cancellation already found in the radiation-limited gravitational estimate.

## Pure-loss channel interpretation

If one effective branch-dependent bosonic displacement $\Delta$ is passively divided so that a fraction $\tau_{\rm ch}$ reaches the probe and $1-\tau_{\rm ch}$ reaches the complementary output, then

$$
\chi_B=\tau_{\rm ch}|\Delta|^2,
\qquad
2\Gamma_\Xi=(1-\tau_{\rm ch})|\Delta|^2,
$$

and

$$
\boxed{
\mathcal M_\Xi=(2\tau_{\rm ch}-1)|\Delta|^2.
}
$$

Thus the **strong history-transfer witness** is positive iff

$$
\boxed{\tau_{\rm ch}>1/2.}
$$

This is the same $50\%$ boundary at which the ordinary pure-loss bosonic channel changes from antidegradable to degradable. This does **not** mean source-probe entanglement is impossible below $1/2$; $\mathcal M_\Xi>0$ is a sufficient, deliberately strong witness. The connection shows that the witness asks whether the intended probe receives a better copy of the branch record than the unobserved output.

## Reactive versus radiative physics

For a stationary Gaussian field, fluctuation-dissipation relations tie the Hadamard/noise spectrum to the dissipative spectral part of the retarded response, schematically

$$
G_H(\omega)
\propto
\hbar\coth\left(\frac{\hbar\omega}{2k_BT}\right)
\operatorname{Im}G_R(\omega).
$$

The intended coherent response uses the **full retarded kernel**, including its dispersive/reactive component, while unavoidable equilibrium record formation is tied to the spectral/dissipative sector. This is the main physical lever: operate where the interaction is strongly reactive and weakly radiative.

## Gravity specialization and new scaling implication

For a slowly varying source branch separation $\Delta x_A(t)$ and a mechanical probe in the Newtonian near zone,

$$
\Delta F_B(t)
\simeq
\frac{2Gm_Am_B}{R^3}\Delta x_A(t-R/c).
$$

Thus the branch-dependent coherent response amplitude scales as

$$
\mathcal R_B^{(G)}\propto R^{-3},
$$

and its squared useful exponent scales as $R^{-6}$. Fundamental branch leakage generated at the source does not acquire this receiver-distance suppression. Therefore, in the ideal near-zone radiation-limited picture,

$$
\boxed{
\gamma_{\rm hist}^{(G)}\propto R^{-6},
\qquad
T_*(R)-R/c\propto R^6
}
$$

up to frequency, geometry, and apparatus factors.

This exposes a severe **causality-versus-coupling tradeoff**: increasing $R$ makes the light-travel delay easier to resolve but destroys near-field coherent transfer extremely rapidly. A gravity-specific derivation must use the conserved total stress-energy tensor, including the source actuator/apparatus, before this scaling is promoted beyond the near-zone schematic level.

## Novelty discipline

Do not claim novelty for the underlying separability inequality, matched-filter mathematics, scalar communication channels, pure-loss $50\%$ threshold, fluctuation-dissipation relation, retarded GIE, resonant enhancement, minimum-noise bounds, gravitational decoherence, or dressing issues.

The potentially distinctive physics synthesis is now

$$
\boxed{
\text{retarded branch transfer}
+\text{history-coherence margin}
+\text{complementary-record spectrum}
+\text{optimal causal history}
+\text{causality/build-time scaling}.
}
$$

## Immediate frontier

1. Calculate $S_E(\omega)$ and $\gamma_{\rm hist}$ with a specific smooth scalar source profile and switching function, including all normalization factors.
2. Verify the $T_*(R)=R/c+1/\gamma_{\rm hist}$ asymptotic formula numerically against the exact finite-time kernel.
3. Add probe damping and finite temperature; determine whether a finite positive-margin window survives.
4. Replace the scalar source by a conserved linearized-gravity stress-energy difference and compute the gravity-specific response and complementary spectra.
5. Investigate whether the $R^6$ buildup penalty produces a useful no-go/optimization result for simultaneous retardation and near-field nonclassicality.

## Current conceptual compression

> **The field receives a branch-dependent disturbance and divides its information between an intended quantum probe and everything left unobserved. The probe cannot receive the source-controlled record before $R/c$. After arrival, a positive strong witness requires the probe to accumulate branch distinguishability faster than the complement accumulates an irreversible record. In the scalar toy model this becomes a matched-filter problem with an intrinsic transfer efficiency $\eta_T$. The threshold is controlled by channel efficiency rather than source strength. The near field is favorable because coherent reactive response can remain large while radiative record formation is small; for gravity, however, the useful near-zone response falls so rapidly with distance that resolving causal retardation and obtaining strong nonclassicality become competing goals.**
