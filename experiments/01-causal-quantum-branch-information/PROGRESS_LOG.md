# Progress Log — Experiment 01

This file is the timestamped continuity record for active work on **Causal Transport of Quantum Branch Information by Gravity**. It is intentionally concise enough to recover the project state if conversational context is lost. Detailed derivations live in `README.md` and `RESEARCH_PROGRESS.md`.

---

## 2026-08-07 12:30 EDT — Canonical state of the project

### Core question

Can gravity transfer branch distinguishability from a coherently delocalized source to a distant quantum probe **causally** and **without converting the branch into an irreversible classical record**?

Three-party structure:

$$
A \rightarrow g \rightarrow B,
$$

where $A$ is the source cat state, $g$ is the gravitational mediator/field, and $B$ is a quantum probe.

### Established working model

For the simplest conditional pure-state model,

$$
|\Psi\rangle
=
\frac{|L\rangle|B_L\rangle|g_L\rangle+|R\rangle|B_R\rangle|g_R\rangle}{\sqrt2}.
$$

Define

$$
s_B=|\langle B_L|B_R\rangle|,
\qquad
s_g=|\langle g_L|g_R\rangle|.
$$

Then source visibility is

$$
\boxed{V_A=s_Bs_g.}
$$

This separates branch information stored in the probe from branch information retained by the mediator/environment.

### Source-probe entanglement

For the same factorized conditional model,

$$
\boxed{
\mathcal N_{AB}
=
\frac14\left[
\sqrt{(1+s_g)^2-4s_gs_B^2}-(1-s_g)
\right].
}
$$

Important limits:

- $s_g=1$: $\mathcal N_{AB}=\frac12\sqrt{1-s_B^2}$.
- $s_B=1$: $\mathcal N_{AB}=0$.
- $s_g=0$: $\mathcal N_{AB}=0$ even if the probe has a perfect branch record.

Interpretation: **broadcasting branch information is not enough; entanglement requires branch dependence to be transferred while coherence remains available.**

### Quantum-eraser prediction

After a perfect probe-side erasure, $s_B\to1$, so

$$
\boxed{V_{\rm revival}=|\langle g_L|g_R\rangle|.}
$$

Residual visibility loss after perfect probe reversal isolates branch information left in the gravitational mediator or other uncontrolled environment.

### Causality

For a controlled source operation at $t=0$ and probe distance $R$,

$$
\boxed{D_B(t)=0\qquad t<R/c}
$$

for the source-controlled contribution, where

$$
D_B(t)=\frac12\|\rho_B^L(t)-\rho_B^R(t)\|_1.
$$

Vacuum correlations outside the light cone do not invalidate this: the claim concerns changes caused by the controllable source operation.

### Near-field versus radiation design principle

Desired coherent near-field phase:

$$
\phi_{\rm ent}
\sim
\frac{2Gm_Am_B\Delta x_A\Delta x_B}{\hbar R^3}T.
$$

Representative gravitational-radiation branch leakage for smooth trajectories scales strongly downward with preparation time, schematically

$$
\Gamma_{\rm rad}\propto\frac{Gm^2d^4}{\hbar c^5\tau^4}.
$$

Candidate design rule: **adiabatic splitting/recombination plus long near-field interaction** maximizes coherent mediation relative to radiative branch leakage.

### Gaussian solvable limit

For a two-oscillator Gaussian variant, finite-time channel dynamics

$$
V_T=X_TV_0X_T^T+Y_T
$$

obey a conservative PPT-preserving classicality condition

$$
Y_T+\frac{i\hbar}{2}(\Omega_\Gamma-X_T\Omega_\Gamma X_T^T)\succeq0.
$$

Infinitesimally this reproduces a correlated-noise bound of the form

$$
D_AD_B-D_{AB}^2\ge\hbar^2g^2.
$$

This is a consistency check, not the final framework, because the source cat state is non-Gaussian.

### Correct non-Gaussian object

Use the reduced source-probe block channel

$$
\rho_{AB}(T)
=
\frac12
\begin{pmatrix}
\Phi_L^T(\rho_B) & \Xi_T(\rho_B)\\
\Xi_T^\dagger(\rho_B) & \Phi_R^T(\rho_B)
\end{pmatrix}_A.
$$

$\Phi_L$ and $\Phi_R$ are the two conditional probe channels; $\Xi_T$ is the **conditional-history coherence map**.

### Current frontier

Derive the strongest bound of the schematic form

$$
\boxed{\|\Xi_T\|\le F[\Phi_L,\Phi_R,N,R,T]}
$$

for a specified class of **causal classical gravitational mediators**. Then calculate $\Xi_T$ for a quantum field mediator and test for violation.

### Novelty discipline

Established ingredients include gravitationally induced entanglement, one-delocalized-source architectures, retarded/local gravitational entanglement, classical minimum-noise bounds, gravitational coherent-state overlap/decoherence, and channel-level nonclassicality tests.

Potential novelty is therefore **not the base experiment**, but one or more of:

1. a causal conditional-history coherence bound;
2. a probe quantum-eraser protocol that isolates residual mediator branch records;
3. a quantitative coherent-near-field versus radiative-leakage optimization.

### Current conceptual compression

> Put a mass in two places. Before a light signal could reach a distant probe, the probe cannot acquire source-controlled information about which alternative was created. After causal contact, it can. But merely broadcasting the branch is not quantum mediation: if the mediator leaves a perfectly distinguishable classical record, the source and probe need not be entangled. Quantum mediation requires branch dependence to reach the probe while coherence between the alternatives survives. The question is therefore whether gravity can move quantum branch information through spacetime without turning it into a classical fact.

### Next derivation

Characterize $\Xi_T$ for a general classical instrument / measure-and-prepare mediator and seek a rigorous fidelity or distinguishability bound relating surviving off-diagonal coherence to the distinguishability of the conditional probe channels.
