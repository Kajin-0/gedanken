# Current State — Experiment 01

**Last updated:** 2026-08-07 13:50 EDT  
**Experiment:** Causal Transport of Quantum Branch Information by Gravity

This is the compact recovery point. `PROGRESS_LOG.md` and `checkpoints/` preserve the derivation history.

## 1. Operational state and witness

For the balanced source path qubit,

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

Every balanced separable source-probe state obeys

$$
\boxed{C_\Xi^2+D_B^2\le1.}
$$

Thus

$$
\boxed{\mathcal W_\Xi=C_\Xi^2+D_B^2-1>0}
$$

certifies source-probe entanglement.

The preferred logarithmic form is

$$
\Gamma_\Xi=-\ln C_\Xi,
\qquad
\chi_B=-\ln(1-D_B^2),
$$

$$
\boxed{
\mathcal M_\Xi
=\chi_B-2\Gamma_\Xi
=\ln\frac{C_\Xi^2}{1-D_B^2}.
}
$$

Separable states require

$$
\boxed{\mathcal M_\Xi\le0.}
$$

For weak distinguishability,

$$
\Gamma_\Xi\gtrsim D_B^2/2.
$$

## 2. Meaning of $C_\Xi$

For pure conditional global outputs $|\Phi_L\rangle_{BE}$ and $|\Phi_R\rangle_{BE}$,

$$
\Xi=\operatorname{Tr}_E|\Phi_L\rangle\langle\Phi_R|,
$$

and

$$
\boxed{C_\Xi=F(\rho_E^L,\rho_E^R).}
$$

Thus $C_\Xi$ is the indistinguishability of the **unobserved complementary records** of the two histories. The final theorem should be phrased only in operational source-probe quantities rather than assuming a fundamental $A\otimes g\otimes B$ factorization.

## 3. Causality

For a controllable source operation at $t=0$ and source-probe separation $R$,

$$
D_B(T,R)=0
\qquad T<R/c
$$

for the source-controlled contribution.

Define

$$
T_*(R)=\inf\{T:\mathcal M_\Xi(T,R)>0\}.
$$

A local theory requires

$$
\boxed{T_*(R)\ge R/c.}
$$

The target is a **causal nonclassicality front**, not merely a retarded classical force.

## 4. Operational measurement

For a chosen eraser unitary $U$ and probe observable $M$ with $\|M\|_\infty\le1$, measurable lower bounds $c_U\le C_\Xi$ and $d_M\le D_B$ obey

$$
\boxed{c_U^2+d_M^2\le1}
$$

for every separable state. A violation certifies entanglement without full tomography.

## 5. Exact conditional maps

For branch-conditioned propagators $U_L,U_R$ on probe plus unobserved output $E$,

$$
\Phi_j^T(\rho_B)
=\operatorname{Tr}_E[U_j(\rho_B\otimes\rho_E)U_j^\dagger],
$$

$$
\boxed{
\Xi_T(\rho_B)
=\operatorname{Tr}_E[U_L(\rho_B\otimes\rho_E)U_R^\dagger].
}
$$

These definitions are the non-Gaussian framework for the original one-cat/one-probe experiment.

## 6. Scalar-field influence-functional structure

For a Gaussian scalar mediator, with forward/backward currents

$$
J_1=J_A^{(L)}+j_B[q],
\qquad
J_2=J_A^{(R)}+j_B[q'],
$$

and

$$
J^-=\Delta J_A+j_B^-,
\qquad
J^+=\bar J_A+j_B^+,
$$

the off-diagonal influence functional has the structural form

$$
\ln\mathcal F_{LR}
=
 iJ^-G_RJ^+
-
\frac12J^-G_HJ^-.
$$

The retarded kernel $G_R$ produces the causal branch-dependent probe response; the Hadamard kernel $G_H$ controls fluctuations and loss of history coherence. The environment distinguishes the **complete source-plus-probe history difference**, not the source in isolation.

## 7. Coherent-drive limit

Let the source-current difference be

$$
\Delta J_A(\mathbf x,t)=s(\mathbf x)u(t),
$$

and let $B$ be a harmonic probe initially in its ground state. Work first in the weak one-way coherent-drive approximation.

The branch-dependent force is

$$
\Delta F_B(t)
=\lambda_B\int d^4x'\,G_R(x_B,t;x')\Delta J_A(x').
$$

Define the finite-time retarded response mode

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

and

$$
\boxed{
\chi_B=|\Delta\alpha_B|^2
=\langle u,K_Bu\rangle,
\qquad
K_B=|r_T\rangle\langle r_T|.
}
$$

Write the complementary record exponent as

$$
\boxed{
2\Gamma_\Xi=\langle u,N_Tu\rangle,
}
$$

where $N_T\succeq0$ is the finite-time unobserved-record/noise kernel obtained from the Hadamard sector (or equivalently from the conditional complementary coherent displacement in this limit).

Therefore the central functional is

$$
\boxed{
\mathcal M_\Xi[u]
=\langle u,(K_B-N_T)u\rangle.
}
$$

This is the first explicit response-minus-record functional for the Gedanken experiment.

## 8. Matched-history optimization theorem

With a quadratic source-control budget

$$
\langle u,Wu\rangle=1,
\qquad W\succ0,
$$

the maximum margin is

$$
\boxed{
\mathcal M_{\Xi,\max}
=\lambda_{\max}\!\left[
W^{-1/2}(K_B-N_T)W^{-1/2}
\right].
}
$$

Thus a positive-margin trajectory exists iff this largest generalized eigenvalue is positive.

Because $K_B$ is rank one, when $N_T$ is positive definite (or on its supported subspace using the Moore-Penrose pseudoinverse), define

$$
\boxed{
\eta_T
=\langle r_T,N_T^{-1}r_T\rangle.
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

For a real source trajectory, use the corresponding realified/symmetrized kernels; the generalized-eigenvalue structure is unchanged.

**Interpretation:** the optimal history is the **noise-whitened time reverse of the probe's retarded response**. Mathematically this is a matched filter, but the quantity being whitened is the unobserved world's ability to record which branch occurred.

## 9. Explicit $3+1$D scalar light-cone limit

For the ideal massless scalar retarded Green function (up to normalization convention)

$$
G_R(R,t-t')\propto\frac{\delta(t-t'-R/c)}{4\pi R},
$$

one finds

$$
r_T(t')\propto
\frac{i\lambda_Bx_{\rm zpf}}{4\pi\hbar R}
 e^{i\omega_B(t'+R/c)}
\Theta(T-R/c-t'),
$$

and therefore

$$
\boxed{
\chi_B(T,R)
\propto
\frac{\lambda_B^2x_{\rm zpf}^2}{16\pi^2\hbar^2R^2}
\left|
\int_0^{T-R/c}dt\,u(t)e^{i\omega_Bt}
\right|^2.
}
$$

This makes causality and resonant history matching explicit. A finite spatial profile and smooth switching are required to make the complementary field kernel ultraviolet well behaved.

## 10. Reactive versus radiative sector

For a stationary Gaussian field, fluctuation-dissipation relations connect the Hadamard/noise spectrum to the dissipative spectral part of the retarded response, schematically

$$
G_H(\omega)
\propto
\hbar\coth\!\left(\frac{\hbar\omega}{2k_BT}\right)
\operatorname{Im}G_R(\omega)
$$

(up to convention-dependent factors).

The useful probe response depends on the **full** retarded kernel, including its dispersive/reactive part, whereas equilibrium fluctuations are tied to its spectral/dissipative sector. This identifies the physical lever behind the Gedanken experiment: an adiabatic near-field interaction can carry coherent branch dependence with little radiative record formation.

For the $3+1$D scalar propagator, the low-frequency regime $\omega R/c\ll1$ is increasingly reactive. Gravity is even more favorable qualitatively because conserved stress-energy forbids gravitational monopole and dipole radiation; the leading radiative channel is quadrupolar.

## 11. Gravity specialization

For a slowly varying spatial branch separation $\Delta x_A(t)$ and a distant mechanical probe, the leading near-zone tidal force difference is

$$
\Delta F_B(t)
\simeq
\frac{2Gm_Am_B}{R^3}\Delta x_A(t-R/c).
$$

Therefore

$$
\boxed{
\Delta\alpha_B(T)
\simeq
\frac{2iGm_Am_Bx_{\rm zpf}}{\hbar R^3}
\int_0^{T-R/c}dt\,\Delta x_A(t)e^{i\omega_B(t+R/c)}.
}
$$

For a static branch separation this reproduces the previous bounded oscillator-displacement result. The matched-history solution suggests resonance as an amplifier, but a gravity-specific radiation calculation must include the actuator/apparatus stress-energy; the radiative source is the conserved total stress-energy tensor, not the moving test mass in isolation. Resonant/parametric GIE enhancement already exists in the literature and is not claimed as novel here.

## 12. Existing gravity radiation floor

For conditional oscillator states $|\pm\alpha\rangle$ and coherent radiative-graviton leakage,

$$
\mathcal M_\Xi\simeq4|\alpha|^2-N_g.
$$

For the static tidal interaction at half an oscillator period,

$$
4|\alpha|_{\max}^2
=\frac{8G^2m_A^2m_Bd^2}{\hbar R^6\omega^3}.
$$

Using the known smooth-trajectory vacuum-graviton decoherence scaling gives a radiation-limited threshold in which $m_A$ cancels from the sign condition. Radiative graviton leakage is expected to be vastly below ordinary technical/environmental decoherence in experimentally relevant regimes.

## 13. Novelty discipline

Do not claim novelty for the underlying coherence-distinguishability inequality, matched-filter mathematics, Gaussian influence-functional formalism, fluctuation-dissipation relation, quantum communication through gravity, retarded GIE, resonant GIE enhancement, minimum classical-noise results, graviton decoherence, or gravitational-dressing issues.

The potentially distinctive synthesis is now

$$
\boxed{
\text{retarded branch transfer}
+\text{history-coherence margin}
+\text{complementary-record kernel}
+\text{optimal causal source history}.
}
$$

The strongest candidate paper object is

$$
\boxed{
\mathcal M_\Xi[\Delta J_A;T,R]
=\chi_B[\Delta J_A;T,R]-2\Gamma_\Xi[\Delta J_A;T,R]
}
$$

and its optimal history.

## 14. Immediate frontier

1. Compute $N_T$ explicitly for a spatially smeared massless scalar source with finite switching.
2. Evaluate

$$
\eta_T=\langle r_T,N_T^{-1}r_T\rangle
$$

and determine whether/when $\eta_T>1$ after $R/c$.
3. Derive the long-time/narrow-band limit and express $\eta_T$ directly in terms of reactive response versus fluctuation spectral density.
4. Only then replace the scalar current with a conserved weak-field stress-energy tensor and derive the linearized-gravity kernels.
5. Keep all novelty statements provisional until a dedicated literature comparison is complete.

## Current conceptual compression

> **A mass is placed in two coherent histories. The field can make a distant probe distinguish those histories only after causal contact. The useful quantum signal is the branch distinguishability deposited coherently in the probe; the cost is the distinguishability leaked into everything left unobserved. Their logarithmic difference, $\mathcal M_\Xi$, is positive only when the source and probe are entangled. In the scalar toy model this becomes a quadratic response-minus-record functional. The optimal source history is obtained by whitening the environment's branch-record kernel and matching the result to the retarded probe response. The physical lever is the reactive near field: it can mediate coherent response while radiative modes—the modes that carry an irreversible branch record—remain strongly suppressed.**
