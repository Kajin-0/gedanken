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
2. a probe quantum-eraser protocol that isolates residual gravitational branch records;
3. a quantitative coherent-near-field versus radiative-leakage optimization.

### Current conceptual compression

> Put a mass in two places. Before a light signal could reach a distant probe, the probe cannot acquire source-controlled information about which alternative was created. After causal contact, it can. But merely broadcasting the branch is not quantum mediation: if the mediator leaves a perfectly distinguishable classical record, the source and probe need not be entangled. Quantum mediation requires branch dependence to reach the probe while coherence between the alternatives survives. The question is therefore whether gravity can move quantum branch information through spacetime without turning it into a classical fact.

### Next derivation

Characterize $\Xi_T$ for a general classical instrument / measure-and-prepare mediator and seek a rigorous fidelity or distinguishability bound relating surviving off-diagonal coherence to the distinguishability of the conditional probe channels.

---

## 2026-08-07 12:34 EDT — Candidate classical-record coherence inequality

### Classical-record mediator model

Model the complete classical transcript carried from source to probe by a variable $\lambda$. For source branch $j\in\{L,R\}$ let the transcript occur with probability $p_j(\lambda)$. Conditional on $\lambda$, the probe is prepared/evolved into a state $\sigma_\lambda$; all source-branch dependence reaching the probe is assumed to pass through the classical transcript.

For each transcript value, positivity of the source instrument implies an off-diagonal coefficient $c_\lambda$ satisfying

$$
|c_\lambda|^2\le p_L(\lambda)p_R(\lambda).
$$

The reduced source-probe blocks therefore have the form

$$
\rho_B^L=\sum_\lambda p_L(\lambda)\sigma_\lambda,
$$

$$
\rho_B^R=\sum_\lambda p_R(\lambda)\sigma_\lambda,
$$

and

$$
\Xi=\sum_\lambda c_\lambda\sigma_\lambda.
$$

Define the **history-coherence norm**

$$
\boxed{C_\Xi\equiv\|\Xi\|_1}
$$

and the probe branch distinguishability

$$
\boxed{D_B\equiv\frac12\|\rho_B^L-\rho_B^R\|_1.}
$$

Triangle inequality gives

$$
C_\Xi\le\sum_\lambda\sqrt{p_L(\lambda)p_R(\lambda)}\equiv B_C,
$$

where $B_C$ is the classical Bhattacharyya coefficient. Contractivity under the classical-to-quantum preparation map gives

$$
D_B\le\frac12\sum_\lambda|p_L(\lambda)-p_R(\lambda)|\equiv D_C.
$$

For classical probability distributions,

$$
B_C^2+D_C^2\le1.
$$

Therefore the classical-record mediator obeys the candidate bound

$$
\boxed{C_\Xi^2+D_B^2\le1.}
$$

### Quantum controlled interaction

For a coherent conditional unitary

$$
U=|L\rangle\langle L|\otimes U_L+|R\rangle\langle R|\otimes U_R,
$$

acting on an arbitrary normalized probe state $\rho_B$,

$$
\rho_B^L=U_L\rho_BU_L^\dagger,
\qquad
\rho_B^R=U_R\rho_BU_R^\dagger,
$$

and

$$
\Xi=U_L\rho_BU_R^\dagger.
$$

Unitary invariance of the trace norm gives

$$
\boxed{C_\Xi=\|\rho_B\|_1=1.}
$$

Hence any nonzero conditional probe distinguishability $D_B>0$ gives

$$
\boxed{C_\Xi^2+D_B^2>1,}
$$

violating the classical-record bound in the ideal coherent case.

Define a provisional witness

$$
\boxed{\mathcal W_\Xi=C_\Xi^2+D_B^2-1.}
$$

Then

$$
\mathcal W_\Xi\le0
$$

for the specified classical-record/measure-and-prepare mediator class, whereas an ideal coherent controlled interaction gives

$$
\mathcal W_\Xi=D_B^2>0.
$$

### Three-party interpretation

For the factorized conditional field model

$$
|\Psi\rangle=\frac{|L\rangle|B_L\rangle|g_L\rangle+|R\rangle|B_R\rangle|g_R\rangle}{\sqrt2},
$$

tracing out gravity gives

$$
\Xi=\langle g_R|g_L\rangle\,|B_L\rangle\langle B_R|,
$$

so

$$
C_\Xi=s_g.
$$

For pure probe branches,

$$
D_B=\sqrt{1-s_B^2}.
$$

The classical-record bound becomes

$$
\boxed{s_g\le s_B.}
$$

Interpretation: **a classical mediator cannot leave behind a less distinguishable record than the distinguishability it has delivered to the probe.** This is a data-processing statement. A coherent quantum mediator can behave as a reversible bus: it may transfer branch dependence to the probe and later return close to the same mediator state, allowing $s_g>s_B$.

### Why this differs from ordinary interferometric complementarity

The ordinary source visibility is

$$
V_A=|\operatorname{Tr}\Xi|,
$$

whereas the new quantity is

$$
C_\Xi=\|\Xi\|_1.
$$

A coherent controlled interaction can drive $V_A$ toward zero while keeping $C_\Xi=1$. Thus $C_\Xi$ measures coherence retained **between the two conditional histories**, not merely locally visible source interference.

This is precisely the resource needed for quantum erasure or coherent reversal.

### Scope and novelty status

The inequality above is currently a **derived candidate result for a clearly specified classical-record / measure-and-prepare mediator class**. It has not yet been shown to cover every LOCC, non-Markovian, nonlinear, or relativistic classical-gravity model. It also requires a dedicated literature search before any novelty claim; nearby literature already contains gravitational quantum-communication benchmarks and entanglement-breaking channel tests.

### Updated frontier

1. Prove the bound for the broadest possible classical causal transcript model, ideally arbitrary finite-round LOCC consistent with preservation of the $L/R$ branch basis.
2. Determine the operational measurement protocol for $C_\Xi=\|\Xi\|_1$ using source-probe joint observables / optimized quantum erasure.
3. Calculate $C_\Xi(T,R)$ and $D_B(T,R)$ for a scalar-field mediator, then linearized gravity.
4. Test whether the retarded quantum-field prediction produces a spacetime region with

$$
\mathcal W_\Xi(T,R)>0
$$

only after causal contact.

---

## 2026-08-07 12:38 EDT — General separable-state bound and operational witness

### Stronger result: the bound is not limited to measure-and-prepare models

Consider any balanced source-probe state written in the source path basis as

$$
\rho_{AB}
=
\frac12
\begin{pmatrix}
\rho_L & \Xi\\
\Xi^\dagger & \rho_R
\end{pmatrix},
\qquad
\operatorname{Tr}\rho_L=\operatorname{Tr}\rho_R=1.
$$

If $\rho_{AB}$ is separable, write

$$
\rho_{AB}=\sum_k p_k\,\tau_A^{(k)}\otimes\sigma_B^{(k)},
$$

with

$$
\tau_A^{(k)}=
\begin{pmatrix}
a_k&c_k\\
c_k^*&b_k
\end{pmatrix},
\qquad
a_k+b_k=1.
$$

Positivity gives

$$
|c_k|\le\sqrt{a_kb_k}.
$$

Using the balanced normalization,

$$
\rho_L=2\sum_kp_ka_k\sigma_k,
\qquad
\rho_R=2\sum_kp_kb_k\sigma_k,
$$

and

$$
\Xi=2\sum_kp_kc_k\sigma_k.
$$

Therefore

$$
C_\Xi=\|\Xi\|_1
\le\sum_kp_k\,2\sqrt{a_kb_k},
$$

while

$$
D_B=\frac12\|\rho_L-\rho_R\|_1
\le\sum_kp_k|a_k-b_k|.
$$

For every $k$,

$$
\left(2\sqrt{a_kb_k}\right)^2+(a_k-b_k)^2=(a_k+b_k)^2=1.
$$

By convexity of the Euclidean norm,

$$
\boxed{C_\Xi^2+D_B^2\le1}
$$

for **every separable balanced source-probe state**.

Thus

$$
\boxed{\mathcal W_\Xi=C_\Xi^2+D_B^2-1>0}
$$

is a sufficient entanglement witness. Classical gravitational mediation that cannot generate source-probe entanglement is therefore excluded whenever this witness is positive.

### Literature boundary

This mathematical structure is closely related to established wave-particle duality / block-positivity results. In particular, Xin Lü (Physics Letters A 397, 127259, 2021) derives general coherence-distinguishability relations using positivity of $2\times2$ block matrices, and related work treats off-diagonal-block norms as coherence/decoherence measures. Therefore **the inequality itself should not currently be claimed as novel**. The potentially new physics is its use as a time-resolved gravitational-history witness together with retarded causal propagation and mediator-record accounting.

### Direct operational measurement of $C_\Xi$

Trace-norm duality gives

$$
\boxed{
C_\Xi
=
\max_{U_B,\theta}
\langle O(U_B,\theta)\rangle,
}
$$

where $U_B$ is unitary and

$$
O(U_B,\theta)
=
e^{i\theta}|L\rangle\langle R|\otimes U_B
+
e^{-i\theta}|R\rangle\langle L|\otimes U_B^\dagger.
$$

$O$ is Hermitian and dichotomic when $U_B$ is unitary. Its expectation value is

$$
\langle O\rangle
=
\operatorname{Re}\left[e^{-i\theta}\operatorname{Tr}(U_B^\dagger\Xi)\right].
$$

Optimizing over $\theta$ and $U_B$ gives $\|\Xi\|_1$.

This gives $C_\Xi$ a concrete meaning: it is the maximum coherent correlation obtainable by optimally aligning the two conditional probe histories. For a controlled unitary, the optimal $U_B$ is the relative-history reversal associated with the polar decomposition of $\Xi$.

### No full tomography is required for a witness

For any chosen probe observable $M$ with $\|M\|_\infty\le1$, define

$$
d_M
=
\frac12\left|\operatorname{Tr}[M(\rho_L-\rho_R)]\right|
\le D_B.
$$

For any chosen eraser unitary $U$ and phase $\theta$,

$$
c_U=|\langle O(U,\theta)\rangle|\le C_\Xi.
$$

Hence every separable state obeys

$$
\boxed{c_U^2+d_M^2\le1.}
$$

Therefore

$$
\boxed{c_U^2+d_M^2>1}
$$

is already sufficient to certify source-probe entanglement using only selected joint correlations and a branch-discrimination measurement.

### Oscillator specialization

For conditional coherent probe states

$$
|B_L\rangle=|\alpha\rangle,
\qquad
|B_R\rangle=|-\alpha\rangle,
$$

one has

$$
s_B=e^{-2|\alpha|^2},
$$

and

$$
D_B^2=1-e^{-4|\alpha|^2}.
$$

If residual unobserved mediator coherence contributes

$$
C_\Xi=s_g=e^{-\Gamma_g},
$$

then

$$
\boxed{
\mathcal W_\Xi
=e^{-2\Gamma_g}-e^{-4|\alpha|^2}.
}
$$

The witness is positive exactly when

$$
\boxed{\Gamma_g<2|\alpha|^2.}
$$

For the idealized retarded oscillator response

$$
\alpha(T,R)
=
\frac{g}{\omega}\left(1-e^{-i\omega\tau}\right),
\qquad
\tau=(T-R/c)_+,
$$

this becomes

$$
\boxed{
\Gamma_g(T,R)
<
\frac{8g^2}{\omega^2}
\sin^2\left(\frac{\omega(T-R/c)}{2}\right).
}
$$

Before causal contact the right-hand side is zero. After causal contact, a positive-witness region can emerge only if coherent probe record formation outruns irreversible/unobserved mediator record formation.

### Updated conceptual interpretation

The strongest simple statement is now:

> **A classicalized interaction can trade source coherence for branch knowledge, but a coherent quantum interaction can make the probe branch-distinguishing while preserving recoverable coherence between the two histories. The quantity $\|\Xi\|_1$ distinguishes those situations even when ordinary source interference has vanished.**

### Updated frontier

1. Determine whether the specific trace-norm witness above is already explicitly known in the same form in the wave-particle/block-coherence literature; assume it is not novel until proven otherwise.
2. Treat $\mathcal W_\Xi(T,R)$ as a gravity-specific causal witness rather than claiming novelty for the underlying quantum-information inequality.
3. Derive $\Xi$, $D_B$, and the residual coherence exponent $\Gamma_g$ from an explicit retarded scalar-field model.
4. Replace the scalar mediator with linearized gravity and determine the leading weak-field scaling of the positive-witness region.
