# Current State — Experiment 01

**Last updated:** 2026-08-07 14:40 EDT  
**Experiment:** Causal Transport of Quantum Branch Information by Gravity

Canonical recovery point. Detailed derivations are preserved in `PROGRESS_LOG.md`, `SCALAR_MATCHED_HISTORY.md`, `GRAVITY_QUADRUPOLE_LIMIT.md`, `TIDAL_RECEIVER.md`, `EXACT_WEYL_CROSSOVER.md`, `WAVEZONE_MODE_CHANNEL.md`, and `checkpoints/`.

## 1. Core operational witness

For a balanced source-path qubit,

$$
\rho_{AB}=\frac12
\begin{pmatrix}
\rho_L & \Xi\\
\Xi^\dagger & \rho_R
\end{pmatrix},
$$

define

$$
C_\Xi=\|\Xi\|_1,
\qquad
D_B=\frac12\|\rho_L-\rho_R\|_1.
$$

Every balanced separable state obeys

$$
\boxed{C_\Xi^2+D_B^2\le1.}
$$

Thus

$$
\boxed{\mathcal W_\Xi=C_\Xi^2+D_B^2-1>0}
$$

certifies source-probe entanglement.

The preferred additive form is

$$
\Gamma_\Xi=-\ln C_\Xi,
\qquad
\chi_B=-\ln(1-D_B^2),
$$

$$
\boxed{
\mathcal M_\Xi=\chi_B-2\Gamma_\Xi.
}
$$

Separable states require

$$
\boxed{\mathcal M_\Xi\le0.}
$$

For pure conditional global histories,

$$
C_\Xi=F(\rho_E^L,\rho_E^R),
$$

so $C_\Xi$ is the indistinguishability of the unobserved complementary records. The paper-level formulation should remain operational in $(\rho_L,\rho_R,\Xi)$ rather than assuming a fundamental factorization of a gravitational-field subsystem.

## 2. Causality

For a controlled source operation at $t=0$ and receiver distance $R$,

$$
D_B(T,R)=0
\qquad T<R/c
$$

for the source-controlled contribution.

Define

$$
T_*(R)=\inf\{T:\mathcal W_\Xi(T,R)>0\}.
$$

A local theory requires

$$
\boxed{T_*(R)\ge R/c.}
$$

The experiment seeks a **causal nonclassicality front**, not merely a retarded classical force.

## 3. Scalar matched-history result

For a source control history $u$ in the scalar-field toy model,

$$
\mathcal M_\Xi[u]
=\langle u,(K_B-N_T)u\rangle,
\qquad
K_B=|r_T\rangle\langle r_T|.
$$

If $N_T$ is invertible on the relevant support, a positive optimized history exists iff

$$
\boxed{
\eta_T=\langle r_T,N_T^{-1}r_T\rangle>1.
}
$$

The optimum is

$$
\boxed{u_{\rm opt}\propto N_T^{-1}r_T,}
$$

i.e. the noise-whitened time reverse of the retarded probe response. In the damped narrow-band limit this becomes a cooperativity-like threshold

$$
\boxed{
\mathcal C_{\rm hist}=\frac{|\mathcal R_B|^2}{\kappa_BS_E}>1.
}
$$

## 4. Clean local GR receiver

The equivalence principle requires a freely falling local receiver to measure tidal curvature, not uniform acceleration. In Fermi normal coordinates,

$$
H_{\rm curv}=\frac{\mu_Bc^2}{2}R_{0i0j}\xi^i\xi^j.
$$

For a differential mode with equilibrium baseline $L_B$ and quantum coordinate $x_B$,

$$
\boxed{
H_{\rm drive}=\mu_BL_B\mathcal E_{nn}x_B,
\qquad
\mathcal E_{ij}=c^2R_{0i0j}.
}
$$

## 5. Exact retarded quadrupole curvature crossover

For the conserved plus-type branch quadrupole

$$
\Delta Q_{xx}=q(t),
\qquad
\Delta Q_{yy}=-q(t),
$$

with the receiver on the $z$ axis and differential baseline along $x$,

$$
\boxed{
\Delta\mathcal E_{xx}(t,R)
=-\frac{G}{R^5}
\left[
3q+\frac{3R}{c}\dot q+\frac{3R^2}{c^2}\ddot q
+\frac{2R^3}{c^3}q^{(3)}+\frac{R^4}{c^4}q^{(4)}
\right]_{t-R/c}.
}
$$

For $q(t)=q_\omega e^{-i\omega t}$ and $\epsilon=\omega R/c$,

$$
\Delta\mathcal E_{xx}
=-\frac{Gq_\omega}{R^5}P(\epsilon)e^{i\epsilon},
$$

$$
\boxed{
P(\epsilon)=3-3i\epsilon-3\epsilon^2+2i\epsilon^3+\epsilon^4,
}
$$

$$
\boxed{
|P|^2=\epsilon^8-2\epsilon^6+3\epsilon^4-9\epsilon^2+9.
}
$$

This single transfer function contains static tidal, induction, and radiation zones.

## 6. Local-receiver causal/capture tension

Define

$$
\nu_G=\frac{G\mu_BL_B^2Q_B\omega_B^3}{c^5}.
$$

For the local differential receiver model,

$$
\boxed{
\mathcal C_{\rm hist}^{(G)}(\epsilon)
=\frac54\nu_G\frac{|P(\epsilon)|^2}{\epsilon^{10}}.
}
$$

Thus

$$
\epsilon\ll1:
\quad
\mathcal C_{\rm hist}^{(G)}\simeq\frac{45}{4}\nu_G\epsilon^{-10},
$$

$$
\epsilon\gg1:
\quad
\mathcal C_{\rm hist}^{(G)}\simeq\frac54\nu_G\epsilon^{-2}.
$$

At the causal crossover $\epsilon=1$,

$$
\boxed{
\mathcal C_{\rm hist}^{(G)}(1)=\frac52\nu_G,
}
$$

which is fantastically small for laboratory receivers. This is not a no-go theorem for GIE; it is a strong-witness/local-mode-capture limitation.

## 7. Wave-zone difference-mode reduction

For branch-dependent coherent gravitational radiation amplitudes

$$
\beta^L_{\mathbf k\lambda},
\qquad
\beta^R_{\mathbf k\lambda},
$$

define

$$
\Delta\beta_{\mathbf k\lambda}=\beta^L_{\mathbf k\lambda}-\beta^R_{\mathbf k\lambda}
$$

and

$$
\boxed{
N_\Delta=\sum_\lambda\int d^3k\,|\Delta\beta_{\mathbf k\lambda}|^2.
}
$$

All coherent $L/R$ distinguishability can be concentrated by a passive mode transformation into one normalized bosonic **difference mode**

$$
\boxed{
 b_\Delta
 =\frac{1}{\sqrt{N_\Delta}}
 \sum_\lambda\int d^3k\,
 \Delta\beta_{\mathbf k\lambda}^*a_{\mathbf k\lambda}.
}
$$

After removing the common coherent displacement, the two radiation states differ only by amplitudes $\pm\sqrt{N_\Delta}/2$ in this single mode.

## 8. Enclosing coherent receiver channel

Let an enclosing collective receiver mode coherently capture fraction $\eta$ of the difference mode. Then

$$
|\Delta\alpha_B|^2=\eta N_\Delta,
\qquad
|\Delta\beta_E|^2=(1-\eta)N_\Delta.
$$

Therefore

$$
\boxed{
D_B^2=1-e^{-\eta N_\Delta},
}
$$

$$
\boxed{
C_\Xi^2=e^{-(1-\eta)N_\Delta}.
}
$$

The strong witness is

$$
\boxed{
\mathcal W_\Xi
=e^{-(1-\eta)N_\Delta}-e^{-\eta N_\Delta},
}
$$

and the logarithmic margin is

$$
\boxed{
\mathcal M_\Xi=(2\eta-1)N_\Delta.
}
$$

Hence

$$
\boxed{
\mathcal W_\Xi>0\iff\eta>1/2.
}
$$

**Important:** this $50\%$ boundary is only the threshold for this strong witness. Exact source-receiver entanglement is nonzero for every finite $N_\Delta>0$ and every coherent capture $\eta>0$.

## 9. Exact source-receiver negativity in the wave-zone model

Define

$$
s_E=e^{-(1-\eta)N_\Delta/2},
\qquad
s_B=e^{-\eta N_\Delta/2}.
$$

Then

$$
\boxed{
\mathcal N_{AB}
=\frac14
\left[
\sqrt{(1+s_E)^2-4s_Es_B^2}
-(1-s_E)
\right].
}
$$

Thus any nonzero coherent capture transfers some source-field entanglement into the receiver. For imperfect capture $\eta<1$, very large $N_\Delta$ eventually makes the uncaptured field an almost perfect branch record and suppresses $\mathcal N_{AB}$ again.

## 10. Source visibility is blind to where the branch record goes

The source-only visibility is

$$
V_A=s_Bs_E=e^{-N_\Delta/2},
$$

independent of $\eta$.

Thus coherent transfer from field to receiver can happen while ordinary source interference remains completely unchanged. At $\eta=0$, the field holds the record; at $\eta=1$, the receiver holds it and the residual field is branch-independent. This strongly motivates the use of $C_\Xi$ rather than visibility alone.

## 11. Optimal branch-radiation strength for the raw witness

For fixed $\eta>1/2$,

$$
\boxed{
N_\Delta^{\rm opt}
=\frac{\ln[\eta/(1-\eta)]}{2\eta-1}
}
$$

maximizes the raw witness $\mathcal W_\Xi$. As $\eta\to1/2^+$, $N_\Delta^{\rm opt}\to2$. The logarithmic margin can grow while the raw measurable witness becomes exponentially small, so $\mathcal W_\Xi$ is the better robustness metric at large branch separation.

## 12. Causal wavepacket capture

For normalized temporal difference-mode envelope $f(t)$ and eventual capture efficiency $\eta_\infty$,

$$
\boxed{
\eta(T)=\eta_\infty\int_{-\infty}^{T-R/c}dt\,|f(t)|^2.
}
$$

The receiver has no source-controlled record before $R/c$. The strong witness turns positive only when

$$
\eta(T)>1/2.
$$

If $\eta_\infty>1/2$,

$$
\boxed{
T_W
=\frac{R}{c}
+F^{-1}\!\left(\frac{1}{2\eta_\infty}\right),
}
$$

where $F$ is the cumulative mode intensity. Exact entanglement begins with the first nonzero coherent capture after causal arrival; the strong history-witness front appears later, once more than half of the branch-difference mode has been transferred.

## 13. Mode-matched receiver and loss threshold

For a local collective receiver mode $c$ with gravitational coupling rate $\kappa_g$ and internal loss $\kappa_i$,

$$
\dot c
=-\frac{\kappa_g+\kappa_i}{2}c
+\sqrt{\kappa_g}\,b_{\rm in}
+\sqrt{\kappa_i}\,\xi_{\rm in}.
$$

For an optimally shaped rising-exponential input mode, the maximum coherent storage efficiency is

$$
\boxed{
\eta_{\max}=\frac{\kappa_g}{\kappa_g+\kappa_i}.
}
$$

Therefore the strong witness can be reached in this one-port model iff

$$
\boxed{
\kappa_g>\kappa_i.
}
$$

If $\kappa_i=0$, then $\eta_{\max}=1$ even for arbitrarily weak gravitational coupling. The cost of weak gravity is an enormous capture time

$$
\tau_{\rm cap}\sim\kappa_g^{-1},
$$

not a fundamental efficiency ceiling.

For a plus-type quadrupole memory $q_B=\Lambda_Bx_B$,

$$
\boxed{
\kappa_g
=\frac{2G\Lambda_B^2\omega_B^4}{5\mu_Bc^5},
}
$$

or, for $\Lambda_B=\mu_BL_B$,

$$
\boxed{
\kappa_g
=\frac{2G\mu_BL_B^2\omega_B^4}{5c^5}.
}
$$

This is absurdly small for laboratory masses/frequencies, explaining why the enclosing receiver is a useful Gedanken limit rather than a practical proposal.

## 14. Current conceptual picture

The project now contains two complementary regimes:

### Near-zone receiver

A local differential quantum receiver interacts mainly with reactive tidal curvature. Coherent branch transfer can dominate clean radiation leakage, but retardation is dynamically tiny.

### Wave-zone receiver

Branch information is carried causally in one outgoing graviton difference mode. A mode-matched enclosing quantum memory can coherently catch that mode and transfer source-field entanglement into matter. The strong witness requires the receiver to hold more than half of the branch-distinguishing mode, although entanglement begins with any nonzero capture.

## 15. Novelty discipline

Established neighboring ingredients include coherent graviton radiation states, graviton counting/state characterization, quantum transduction of gravitational waves, retarded GIE, pure-loss bosonic channels, quantum-state transfer by matched wavepackets, and gravitational decoherence. Do not claim novelty for those components.

Potentially distinctive physics remains the **history-transfer synthesis**:

$$
\boxed{
\text{causal gravitational difference mode}
+\text{coherent capture}
+\text{history-coherence witness/front}.
}
$$

## 16. Immediate frontier

1. Derive the same enclosing-receiver result from explicit linearized-gravity input-output theory rather than the phenomenological beam-splitter map.
2. Include finite thermal occupation and internal decoherence in the receiver and derive the modified history witness.
3. Compare the strong witness with exact negativity to identify the lowest-measurement-cost protocol that works for $\eta<1/2$.
4. Ask whether a classical stochastic gravitational-wave mediator can reproduce the same branch-conditioned receiver states and eraser correlations without violating the separable bound.
5. Search specifically for prior work on **coherent capture of branch-dependent gravitational radiation as an entanglement-transfer protocol** before making any novelty claim.

## Current Einstein/Feynman compression

> **A spatial quantum alternative can imprint itself on an outgoing gravitational wave. Although that radiation occupies many plane-wave modes, all information distinguishing the two alternatives can be compressed into one quantum difference mode. Before the wave arrives, a distant receiver cannot know the branch. When it arrives, an ideal receiver can coherently catch part of that mode. Any nonzero capture transfers some entanglement; once the receiver holds more than half of the distinguishability, a simple history-coherence witness certifies it. Source interference alone cannot see this transfer—the same contrast loss remains whether the branch record is in the gravitational field or in the receiver. In an ideal lossless world even arbitrarily weak gravity permits perfect coherent capture; weak coupling merely stretches the required interaction time. The sharp wave-zone question is therefore whether a gravitational branch record can be caught coherently rather than read out as a classical signal.**