# Current State — Experiment 01

**Last updated:** 2026-08-07 12:45 EDT  
**Experiment:** Causal Transport of Quantum Branch Information by Gravity

This is the compact recovery point for active work. `PROGRESS_LOG.md` preserves the derivation history; timestamped checkpoints preserve immutable snapshots.

## Central operational question

Can gravity make a distant quantum probe distinguish the two branches of a coherently delocalized source **after causal contact** while retaining more recoverable coherence between the two histories than any separable/classicalized source-probe state permits?

For a balanced source path qubit, write

$$
\rho_{AB}(T)=\frac12
\begin{pmatrix}
\rho_L(T) & \Xi_T\\
\Xi_T^\dagger & \rho_R(T)
\end{pmatrix}.
$$

Define

$$
C_\Xi(T)=\|\Xi_T\|_1,
\qquad
D_B(T)=\frac12\|\rho_L(T)-\rho_R(T)\|_1.
$$

For every separable balanced source-probe state,

$$
\boxed{C_\Xi^2+D_B^2\le1.}
$$

Therefore

$$
\boxed{\mathcal W_\Xi(T,R)=C_\Xi^2+D_B^2-1>0}
$$

certifies source-probe entanglement.

Equivalent coherence-loss form: define

$$
\Gamma_\Xi=-\ln C_\Xi.
$$

Then every separable state satisfies

$$
\boxed{
\Gamma_\Xi\ge-\frac12\ln(1-D_B^2),
}
$$

and for weak branch distinguishability,

$$
\boxed{\Gamma_\Xi\gtrsim\frac{D_B^2}{2}.}
$$

Interpretation: a classicalized/separable interaction must spend recoverable history coherence in order to deliver branch information to the probe. A coherent controlled interaction can have $C_\Xi=1$ while $D_B>0$.

## Causality

For a controllable source operation at $t=0$ and source-probe separation $R$,

$$
D_B(T,R)=0
\qquad
T<R/c
$$

for the source-controlled contribution. Define the nonclassicality onset

$$
T_*(R)=\inf\{T:\mathcal W_\Xi(T,R)>0\}.
$$

A local theory requires

$$
\boxed{T_*(R)\ge R/c.}
$$

The target observable is therefore a **causal nonclassicality front**, not merely a delayed classical force.

## Operational witness without full tomography

For a probe observable $M$ with $\|M\|_\infty\le1$ and a chosen probe eraser unitary $U$, define measurable lower bounds

$$
d_M\le D_B,
\qquad
c_U\le C_\Xi.
$$

Every separable state obeys

$$
\boxed{c_U^2+d_M^2\le1.}
$$

A useful linearized family follows because for any $\vartheta$,

$$
\boxed{
c_U\cos\vartheta+d_M\sin\vartheta\le1
}
$$

for separable states. This can be implemented as a conventional linear entanglement witness built from a branch-sensitive probe observable and an eraser-aligned joint coherence observable.

## Exact conditional-channel definitions for the field-theory calculation

For a mediator initially in state $\rho_E$ and branch-conditioned total propagators $U_L(T),U_R(T)$,

$$
\Phi_j^T(\rho_B)
=
\operatorname{Tr}_E\!\left[
U_j(T)(\rho_B\otimes\rho_E)U_j^\dagger(T)
\right],
$$

while the off-diagonal history map is

$$
\boxed{
\Xi_T(\rho_B)
=
\operatorname{Tr}_E\!\left[
U_L(T)(\rho_B\otimes\rho_E)U_R^\dagger(T)
\right].
}
$$

For a Gaussian scalar field, the influence functional separates into a retarded/commutator kernel controlling causal response and a Hadamard kernel controlling fluctuations/decoherence. This is the next calculational route.

## Important gravitational-dressing correction

Do **not** formulate the final theorem by assuming a fundamental Hilbert-space factorization

$$
\mathcal H_A\otimes\mathcal H_g\otimes\mathcal H_B.
$$

Gauge constraints and gravitational dressing make strict subsystem factorization nontrivial. The three-party picture $A\to g\to B$ is useful intuition and is legitimate in gauge-fixed/toy models, but the paper-level witness should be defined entirely through operational source-probe quantities $\rho_L$, $\rho_R$, and $\Xi_T$.

When a clean Stinespring environment factorization is available, $C_\Xi$ can be interpreted as fidelity of the complementary/environmental branch records; it should not automatically be called the overlap of a separately factorized gravitational-field subsystem.

## Oscillator specialization

For conditional coherent probe states $|\pm\alpha\rangle$,

$$
D_B^2=1-e^{-4|\alpha|^2}.
$$

If unobserved history coherence contributes $C_\Xi=e^{-\Gamma_g}$, then

$$
\boxed{
\mathcal W_\Xi=e^{-2\Gamma_g}-e^{-4|\alpha|^2}.
}
$$

The witness is positive iff

$$
\boxed{\Gamma_g<2|\alpha|^2.}
$$

With idealized retarded response

$$
\alpha(T,R)=\frac{g}{\omega}(1-e^{-i\omega(T-R/c)})
$$

for $T\ge R/c$ and zero beforehand, the positive-witness region begins only after causal contact.

## Novelty discipline

The underlying coherence-distinguishability mathematics is related to established wave-particle duality and block-coherence results and should **not** be claimed as new without a dedicated proof of novelty. Gravity-mediated quantum communication, entanglement-breaking channel tests, retarded GIE, classical minimum-noise bounds, and gravitational decoherence are also established neighboring literatures.

The plausible new physics target is the synthesis:

$$
\boxed{
\text{retarded gravitational response}
+
\text{history-coherence witness}
+
\text{operational no-factorization formulation}.
}
$$

## Current frontier

1. Derive $\Phi_L$, $\Phi_R$, and $\Xi_T$ explicitly for a massless scalar-field mediator with finite switching.
2. Express $D_B$ in terms of the retarded kernel and $C_\Xi$ in terms of the complementary/noise kernel.
3. Determine the weak-coupling expansion of

$$
\mathcal W_\Xi(T,R).
$$

4. Identify whether a positive region occurs after $R/c$ and what controls its magnitude.
5. Only then replace the scalar mediator by linearized gravity.

## Current conceptual compression

> **A classicalized interaction can make the probe know the branch only by spending recoverable coherence between the histories. A coherent quantum interaction can make the probe branch-distinguishing while keeping that history coherence available for erasure. The witness $\mathcal W_\Xi$ measures this distinction using only source-probe observables, and relativity requires its source-controlled distinguishability term to remain zero before $R/c$.**
