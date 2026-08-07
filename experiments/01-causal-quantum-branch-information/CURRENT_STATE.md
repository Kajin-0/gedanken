# Current State — Experiment 01

**Last updated:** 2026-08-07 14:05 EDT  
**Experiment:** Causal Transport of Quantum Branch Information by Gravity

This is the compact recovery point. Detailed work is preserved in `PROGRESS_LOG.md`, `SCALAR_MATCHED_HISTORY.md`, `GRAVITY_QUADRUPOLE_LIMIT.md`, and `checkpoints/`.

## 1. Core source-probe witness

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

Every balanced separable state obeys

$$
\boxed{C_\Xi^2+D_B^2\le1.}
$$

Define

$$
\Gamma_\Xi=-\ln C_\Xi,
\qquad
\chi_B=-\ln(1-D_B^2),
$$

and the **history-transfer margin**

$$
\boxed{
\mathcal M_\Xi=\chi_B-2\Gamma_\Xi.
}
$$

Then

$$
\boxed{\mathcal M_\Xi>0}
$$

is a sufficient source-probe entanglement witness.

For pure conditional global histories,

$$
C_\Xi=F(\rho_E^L,\rho_E^R),
$$

so $C_\Xi$ is the indistinguishability of the unobserved complementary records. The final theorem does not require a fundamental factorization into source, gravitational field, and probe Hilbert spaces.

## 2. Causal requirement

For a controlled source operation at $t=0$ and separation $R$,

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

## 3. Scalar-field matched-history result

For a source branch-current difference

$$
\Delta J_A(\mathbf x,t)=s(\mathbf x)u(t),
$$

the weak one-way scalar model gives

$$
\chi_B=\langle u,K_Bu\rangle,
\qquad
2\Gamma_\Xi=\langle u,N_Tu\rangle,
$$

with

$$
K_B=|r_T\rangle\langle r_T|.
$$

Thus

$$
\boxed{
\mathcal M_\Xi[u]
=\langle u,(K_B-N_T)u\rangle.
}
$$

If $N_T$ is invertible on the relevant support,

$$
\boxed{
\eta_T=\langle r_T,N_T^{-1}r_T\rangle>1
}
$$

is equivalent to the existence of a source waveform with positive margin. The optimal complex-envelope history is

$$
\boxed{u_{\rm opt}\propto N_T^{-1}r_T.}
$$

This is a **noise-whitened matched history**: the source history is matched to the retarded receiver mode after whitening by the environment's ability to retain branch information.

## 4. Long-time rate and finite receiver memory

In the narrow-band limit,

$$
\eta_T\simeq(T-R/c)\gamma_{\rm hist},
$$

where

$$
\boxed{
\gamma_{\rm hist}(R,\omega_B)
=\frac{|\mathcal R_B(\omega_B,R)|^2}{S_E(\omega_B)}.
}
$$

Hence

$$
\boxed{
T_*(R)\simeq\frac{R}{c}+\gamma_{\rm hist}^{-1}.
}
$$

With probe damping $\kappa_B$ define

$$
\boxed{
\mathcal C_{\rm hist}
=\frac{|\mathcal R_B|^2}{\kappa_BS_E}.
}
$$

The optimized strong witness can survive finite receiver memory only if

$$
\boxed{\mathcal C_{\rm hist}>1.}
$$

The threshold is a property of channel efficiency, not overall source amplitude; source strength scales both useful response and complementary leakage quadratically and cancels from the ideal ratio.

## 5. Conserved gravity source: axisymmetric quadrupole

To move beyond a nonconserved translating point-mass picture, use a compact source whose branch-difference STF mass quadrupole is

$$
\Delta Q_{ij}(t)
=q(t)\left(n_in_j-\frac13\delta_{ij}\right).
$$

On-axis the Newtonian quadrupole potential difference is

$$
|\Delta\Phi_Q|=\frac{G|q|}{R^3},
$$

and a radial probe experiences branch force difference

$$
\boxed{
|\Delta F_B|
=\frac{3Gm_B}{R^4}|q(t-R/c)|.
}
$$

The narrow-band coherent response coefficient is therefore

$$
|\mathcal R_B^{(G)}|
=\frac{3Gm_Bx_{\rm zpf}}{\hbar R^4}.
$$

The quadrupole radiation formula gives a branch-distinguishing graviton record spectrum with robust scaling

$$
\boxed{S_G(\omega)\propto\frac{G}{\hbar c^5}\omega^5.}
$$

With the axisymmetric convention used in `GRAVITY_QUADRUPOLE_LIMIT.md`,

$$
S_G(\omega)\simeq\frac{2G}{15\hbar c^5}\omega^5
$$

up to one-sided/two-sided Fourier convention factors.

## 6. Gravity history-transfer rate and cooperativity

Combining near-field quadrupole response with coherent graviton leakage gives

$$
\boxed{
\gamma_{\rm hist}^{(G)}
\simeq
\frac{135}{4}
\frac{Gm_Bc^5}{R^8\omega_B^6}
}
$$

within the stated convention, with robust scaling

$$
\gamma_{\rm hist}^{(G)}\propto R^{-8}\omega_B^{-6}.
$$

With probe damping,

$$
\boxed{
\mathcal C_{\rm hist}^{(G)}
\simeq
\frac{135}{4}
\frac{Gm_Bc^5}{\kappa_BR^8\omega_B^6}
=
\frac{135}{4}
\frac{Gm_Bc^5Q_B}{R^8\omega_B^7}.
}
$$

The source quadrupole amplitude cancels from the ideal efficiency ratio.

The radiation-only critical radius is

$$
\boxed{
R_c
\simeq
\left[
\frac{135}{4}
\frac{Gm_Bc^5}{\kappa_B\omega_B^6}
\right]^{1/8}.
}
$$

Illustrative radiation-only values:

- $m_B=1\,\mathrm g$, $f_B=1\,\mathrm{Hz}$, $Q_B=10^8$: $R_c\sim14\,\mathrm{km}$;
- $m_B=1\,\mathrm{kg}$, $f_B=100\,\mathrm{Hz}$, $Q_B=10^6$: $R_c\sim330\,\mathrm m$.

These are **efficiency** thresholds only, not detectability thresholds. Absolute branch-dependent gravitational signals may still be extraordinarily small.

## 7. Near-field / wave-zone tradeoff

Define

$$
\epsilon=\frac{\omega_BR}{c},
\qquad
\mu_G=\frac{Gm_BQ_B\omega_B}{c^3}.
$$

Then the near-zone cooperativity can be written

$$
\boxed{
\mathcal C_{\rm hist}^{(G)}
\simeq
\frac{135}{4}\mu_G\epsilon^{-8}.
}
$$

For laboratory systems $\mu_G\ll1$. Therefore the regime in which a local receiver strongly dominates over graviton leakage is parametrically

$$
\epsilon\ll1.
$$

This exposes the central new tradeoff:

- **near zone:** coherent/reactive branch transfer can dominate radiative leakage, but the propagation delay is tiny compared with the probe dynamics;
- **wave zone:** retardation becomes dynamically visible, but branch information is exported into propagating gravitational modes and a local receiver captures only a fraction.

The near-zone formula must not be extrapolated quantitatively to $\epsilon\sim1$. A full retarded TT calculation is now the main technical target.

## 8. Ideal shell-receiver Gedanken version

The tradeoff is not a logical prohibition; it is largely a mode-capture problem. An ideal enclosing quantum receiver matched to the outgoing quadrupolar gravitational mode could coherently capture a large fraction $\tau_{\rm ch}$ of the branch-distinguishing radiation.

For a pure-loss benchmark,

$$
\mathcal M_\Xi=(2\tau_{\rm ch}-1)|\Delta|^2,
$$

so the strong history-transfer witness requires

$$
\boxed{\tau_{\rm ch}>1/2.}
$$

This suggests two complementary versions of Experiment 01:

1. **near-field local-probe experiment:** optimized for strong nonclassicality with negligible retardation;
2. **wave-zone enclosing-receiver Gedanken experiment:** optimized to make causal quantum branch-information transport conceptually explicit.

## 9. Novelty discipline

Established ingredients include wave-particle coherence/distinguishability bounds, scalar quantum channels, matched filtering, cooperativity, pure-loss thresholds, quadrupole gravity, quadrupole radiation, retarded GIE, graviton decoherence, and gravitational-dressing subtleties.

Potentially distinctive physics is their synthesis into a source-probe **history-transfer** problem and especially the quantified near-field/wave-zone tradeoff.

## Immediate frontier

1. Derive the **full retarded linearized-gravity transfer kernel** for the conserved quadrupole source, not merely the Newtonian $R^{-4}$ limit.
2. Derive the matching TT complementary-output kernel from the same conserved stress-energy history.
3. Compute $\mathcal M_\Xi(T,R)$ continuously through the near-zone to wave-zone crossover.
4. Determine whether a rigorous bound exists connecting resolvable retardation to local receiver history-transfer efficiency.
5. Compare a local receiver with the ideal mode-matched spherical receiver.

## Current conceptual compression

> **A conserved mass quadrupole in two coherent histories perturbs a distant quantum probe and also radiates branch information into gravitational modes. The intended probe receives a useful record through the retarded response; everything else that can distinguish the histories reduces recoverable coherence. In the near field, the interaction is overwhelmingly reactive and the probe can outperform gravitational radiation, but the light-travel delay is dynamically tiny. In the wave zone, causal propagation is obvious, but the branch record spreads into many outgoing modes and a local receiver becomes lossy. The central question has therefore sharpened again: can gravity be shown to carry quantum branch information causally in a regime where the intended quantum receiver captures that information more coherently than the rest of spacetime does?**
