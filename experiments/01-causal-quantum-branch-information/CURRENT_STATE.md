# Current State — Experiment 01

**Last updated:** 2026-08-07 17:30 EDT  
**Experiment:** Causal Transport of Quantum Branch Information by Gravity

This is the canonical compact recovery point. Detailed derivations live in the experiment directory and timestamped `checkpoints/`.

---

## 1. Central question

Can gravity carry information about a coherent source alternative to a distant quantum receiver **causally**, while preserving enough coherence that source and receiver become entangled rather than merely classically correlated?

For a balanced source-path qubit,

$$
\rho_{AB}=\frac12
\begin{pmatrix}
\rho_L&\Xi\\
\Xi^\dagger&\rho_R
\end{pmatrix}.
$$

Define

$$
C_\Xi=\|\Xi\|_1.
$$

For pure conditional global histories,

$$
C_\Xi=F(\rho_E^L,\rho_E^R),
$$

so $C_\Xi$ is the fidelity of the unobserved complementary branch records. Keep the paper-level theory operational in source/receiver quantities rather than assuming a fundamental source–gravity–receiver Hilbert-space factorization.

---

## 2. Causal structure

For a controlled source operation at $t=0$ and receiver separation $R$,

$$
D_B(T,R)=0\qquad T<R/c
$$

for the source-controlled contribution.

Distinguish four levels:

1. **signal front** — first causal gravitational response;
2. **NPT front** — first source-receiver entanglement;
3. **exact witness front** — first negative matched principal-minor witness;
4. **finite-certification front** — first prescribed nonzero witness margin.

---

## 3. Linearized-gravity branch mode

For a conserved branch stress tensor, propagating TT gravitons are displaced coherently. Define

$$
N_\Delta
=\sum_s\int\frac{d^3k}{(2\pi)^3}
|\Delta\alpha_s(\mathbf k)|^2.
$$

This is the squared phase-space distance between the two branch-conditioned outgoing graviton coherent states. Vacuum radiative decoherence satisfies

$$
\Gamma_{\rm vac}=N_\Delta/2.
$$

For a compact nonrelativistic quadrupole difference,

$$
\boxed{
N_\Delta
=\frac{G}{5\pi\hbar c^5}
\int_0^\infty d\omega\,
\omega^5
|\Delta\widetilde Q_{ij}(\omega)|^2.
}
$$

For the narrow-band plus quadrupole

$$
\Delta Q_{xx}=q_0f(t)\cos\omega_0t,
\qquad
\Delta Q_{yy}=-\Delta Q_{xx},
$$

$$
\boxed{
N_\Delta
\simeq
\frac{Gq_0^2\omega_0^5T_f}{5\hbar c^5},
\qquad
T_f=\int dt\,|f(t)|^2.
}
$$

After a passive mode transformation all branch distinguishability resides in one normalized **difference mode**, with branch states equivalent to

$$
|\pm\sqrt{N_\Delta}/2\rangle.
$$

Detailed source mapping: `GRAVITATIONAL_DIFFERENCE_MODE_AMPLITUDE.md`.

---

## 4. Gauge-invariant local gravitational response

A self-contained free local receiver couples to tidal curvature,

$$
H_{\rm drive}=\mu_BL_B\mathcal E_{nn}x_B,
\qquad
\mathcal E_{ij}=c^2R_{0i0j}.
$$

For the conserved plus quadrupole

$$
\Delta Q_{xx}=q(t),\qquad\Delta Q_{yy}=-q(t),
$$

with receiver on the $z$ axis,

$$
\Delta\mathcal E_{xx}
=-\frac{G}{R^5}
\left[
3q+\frac{3R}{c}\dot q+\frac{3R^2}{c^2}\ddot q
+\frac{2R^3}{c^3}q^{(3)}+\frac{R^4}{c^4}q^{(4)}
\right]_{t-R/c}.
$$

For harmonic motion,

$$
P(\epsilon)=3-3i\epsilon-3\epsilon^2+2i\epsilon^3+\epsilon^4,
\qquad
\epsilon=\omega R/c,
$$

is the exact static/induction/wave-zone crossover for this geometry.

---

## 5. Strongest quantum-information theorem

Consider any nontrivial finite binary coherent hybrid state

$$
|\Psi\rangle
=\sqrt p\,|0\rangle|\alpha\rangle
+e^{i\phi}\sqrt{1-p}\,|1\rangle|\beta\rangle,
$$

with

$$
0<p<1,
\qquad
\alpha\neq\beta.
$$

Send the bosonic subsystem through a one-mode **gauge-covariant phase-insensitive Gaussian channel** $\Phi_{\tau,m}$, where

- $\tau$ is intensity gain/transmission;
- $m$ is the mean output occupation produced by vacuum input.

The channel acts on characteristic functions as

$$
\chi_{\Phi(O)}(\xi)
=\chi_O(\sqrt\tau\xi)
\exp[-(2m+1-\tau)|\xi|^2/2].
$$

Complete positivity requires

$$
m\ge\max(0,\tau-1),
$$

and the channel is entanglement breaking iff

$$
m\ge\tau.
$$

The project now has an analytic proof that

$$
\boxed{
(I\otimes\Phi_{\tau,m})(|\Psi\rangle\langle\Psi|)
\text{ is NPT}
\iff
m<\tau.
}
$$

Thus **every nontrivial finite binary coherent hybrid state is a complete EB probe for the entire gauge-covariant one-mode phase-insensitive Gaussian family**: thermal attenuators, thermal amplifiers, and additive Gaussian noise.

The exact sign parameter is

$$
\boxed{
q
=\exp\left[
\frac{|\alpha-\beta|^2}{2m}(\tau-m)
\right].
}
$$

Full theorem: `PHASE_INSENSITIVE_GAUSSIAN_BINARY_PROBE_THEOREM.md`.

Special thermal-attenuator proof with explicit domain-safe negative vector: `EXACT_FINITE_CAT_THERMAL_THEOREM.md`.

---

## 6. Exact low-dimensional witness

For the symmetric representation $|\pm a\rangle$, choose

$$
v_*=\frac{2\sqrt\tau\,a}{m}.
$$

Define

$$
p_0=\langle0,0|\rho|0,0\rangle,
$$

$$
p_v=\langle1,v_*|\rho|1,v_*\rangle,
$$

and

$$
z_v=\langle1,0|\rho|0,v_*\rangle.
$$

Every separable state obeys

$$
|z_v|^2\le p_0p_v.
$$

For the binary coherent output,

$$
\boxed{
\frac{|z_v|^2}{p_0p_v}
=\exp\left[
\frac{N_\Delta}{m}(\tau-m)
\right],
}
$$

with $N_\Delta=4|a|^2$ in the symmetric branch basis. Therefore

$$
\boxed{
|z_v|^2>p_0p_v
\iff
\tau>m
\iff
\rho\text{ is NPT}.
}
$$

The exact boundary therefore requires only two populations and one joint source-receiver coherence, not full tomography.

Files: `EXACT_FINITE_CAT_WITNESS.md`, `EXACT_THREE_ELEMENT_WITNESS.md`.

---

## 7. Exact passive causal-front theorem

For a stationary passive Markov receiver,

$$
\dot c
=-\frac{\kappa_{\rm tot}}2c
+\sqrt{\kappa_\Delta}\,b_\Delta^{\rm in}
+\sum_a\sqrt{\kappa_a}\,b_a^{\rm in},
$$

with

$$
\kappa_{\rm tot}=\kappa_\Delta+\sum_a\kappa_a,
$$

$$
\Gamma_{\rm th}=\sum_a\bar n_a\kappa_a,
$$

any normalized incoming branch-mode waveform obeys

$$
\eta_f(\tau)
\le
\frac{\kappa_\Delta}{\kappa_{\rm tot}}
(1-e^{-\kappa_{\rm tot}\tau}),
\qquad
\tau=t-R/c.
$$

For every finite binary coherent source encoding, no NPT front exists if

$$
\boxed{\kappa_\Delta\le\Gamma_{\rm th}.}
$$

If

$$
\kappa_\Delta>\Gamma_{\rm th},
$$

the exact waveform-optimal front is

$$
\boxed{
T_{\rm NPT}^{\min}
=
\frac Rc+
\frac1{\kappa_{\rm tot}}
\ln\left[
\frac{\kappa_\Delta}
{\kappa_\Delta-\Gamma_{\rm th}}
\right].
}
$$

The time-reversed receiver ringdown saturates the bound.

Full theorem: `CAUSAL_FRONT_THEOREM.md`.

---

## 8. Finite-strength certification front

Define the exact logarithmic witness margin

$$
\boxed{
\Lambda
=\ln\frac{|z_v|^2}{p_0p_v}.
}
$$

For the binary coherent branch mode,

$$
\boxed{
\Lambda
=\frac{N_\Delta}{m}(\tau-m).
}
$$

For the stationary passive receiver, the optimal time-dependent margin is

$$
\boxed{
\Lambda_{\max}(\tau)
=\frac{N_\Delta}{\Gamma_{\rm th}}
\left[
\kappa_\Delta(1-e^{-\kappa_{\rm tot}\tau})
-\Gamma_{\rm th}
\right].
}
$$

Thus the bare NPT front is the zero-margin limit. Requiring

$$
\Lambda\ge\Lambda_{\rm req}>0
$$

gives

$$
\boxed{
T_\Lambda^{\min}
=
\frac Rc
-
\frac1{\kappa_{\rm tot}}
\ln\left[
1-
\frac{\Gamma_{\rm th}}{\kappa_\Delta}
\left(1+\frac{\Lambda_{\rm req}}{N_\Delta}\right)
\right].
}
$$

It exists only if

$$
\Gamma_{\rm th}
\left(1+\frac{\Lambda_{\rm req}}{N_\Delta}\right)
<\kappa_\Delta.
$$

The maximum available exact margin is

$$
\boxed{
\Lambda_\infty
=N_\Delta
\left(\frac{\kappa_\Delta}{\Gamma_{\rm th}}-1\right).
}
$$

This resolves the amplitude-independence of the mathematical NPT onset: **finite certification explicitly depends on source strength $N_\Delta$.**

File: `FINITE_STRENGTH_CERTIFICATION_FRONT.md`.

---

## 9. Active phase-insensitive receiver

For a stable active receiver with loss ports $\kappa_j^-$ and gain ports $\gamma_k^+$,

$$
\kappa_{\rm eff}
=\kappa_\Delta+\sum_j\kappa_j^-
-\sum_k\gamma_k^+>0.
$$

The unavoidable vacuum-output occupation is driven by

$$
\boxed{
\Gamma_+
=\sum_j\kappa_j^-\bar n_j
+\sum_k\gamma_k^+(\bar n_k^++1).
}
$$

Every phase-insensitive gain port contributes its spontaneous $+1$ quantum even at zero temperature.

The exact NPT-capability condition becomes

$$
\boxed{
\kappa_\Delta>\Gamma_+,
}
$$

with front

$$
\boxed{
T_{\rm NPT}^{\min}
=
\frac Rc+
\frac1{\kappa_{\rm eff}}
\ln\left[
\frac{\kappa_\Delta}
{\kappa_\Delta-\Gamma_+}
\right].
}
$$

Thus phase-insensitive amplification can enlarge a classical signal but cannot advance the quantum front for free.

File: `ACTIVE_GAUSSIAN_CAUSAL_FRONT.md`.

---

## 10. Gravity-specific mode coupling

The useful branch-mode rate is

$$
\boxed{\kappa_\Delta=\mathcal O_{SB}\kappa_g.}
$$

The total receiver graviton linewidth is

$$
\boxed{
\kappa_g
=\frac{2G\omega_B^5}{5\hbar c^5}
Q_{ij}^{10}Q_{ij}^{01}.
}
$$

For complete angular access,

$$
\mathcal O_Q
=\frac{|Q_B^{ij*}Q^S_{ij}|^2}
{(Q_B^{ij*}Q^B_{ij})(Q_S^{ij*}Q^S_{ij})}.
$$

For two plus quadrupoles rotated by $\psi$,

$$
\mathcal O_Q=\cos^2(2\psi).
$$

For exponential/Lorentzian temporal modes,

$$
\mathcal O_t
=\frac{4\kappa_S\kappa_B}
{(\kappa_S+\kappa_B)^2+4\Delta^2}.
$$

---

## 11. Finite-aperture wave-zone quantum reception

For the plus-type quadrupole, the exact source difference-mode fraction in a polar spherical cap of half-angle $\theta_0$ is

$$
\boxed{
\beta_{\rm cap}
=\frac12-
\frac{5c+10c^3+c^5}{32},
\qquad
c=\cos\theta_0.
}
$$

For a small aperture of radius $a_R$ at distance $R$,

$$
\boxed{
\beta_{\rm cap}
\simeq\frac58\frac{a_R^2}{R^2}.
}
$$

Define

$$
K=\frac58a_R^2\mathcal O\kappa_g.
$$

Then

$$
\kappa_\Delta(R)=K/R^2.
$$

The maximum NPT range at nonzero thermal injection is

$$
\boxed{
R_Q=\sqrt{\frac{K}{\Gamma_{\rm th}}}.
}
$$

For a distance-independent internal linewidth $\kappa_0$,

$$
\boxed{
T_{\rm NPT}^{\min}(R)
=
\frac Rc-
\frac1{\kappa_0+K/R^2}
\ln\left[
1-(R/R_Q)^2
\right],
\qquad R<R_Q.
}
$$

The front approaches the light cone at short range and diverges logarithmically as

$$
R\to R_Q^-.
$$

For finite witness margin,

$$
R_\Lambda
=\frac{R_Q}{\sqrt{1+\Lambda_{\rm req}/N_\Delta}},
$$

with an identical nested front obtained by replacing $R_Q\to R_\Lambda$.

Files: `FINITE_APERTURE_WAVEZONE_FRONT.md`, `QUANTUM_RECEPTION_CONE.md`.

---

## 12. Passive nonrelativistic wave-zone feasibility bound

For ordinary passive nonrelativistic matter, the quadrupole oscillator-strength sum rule gives

$$
\frac{\kappa_g}{\omega_B}
\le
\frac23\mathcal C_B\beta_B^3,
$$

where

$$
\mathcal C_B=r_{s,B}/L_B,
\qquad
\beta_B=\omega_BL_B/c.
$$

If the coherent receiver aperture satisfies $a_R\le L_B$, a nonempty wave-zone NPT interval requires the necessary condition

$$
\boxed{
\mathfrak W_B
\equiv
\frac{5\mathcal O}{12}
\frac{Q_B\mathcal C_B\beta_B^5}{\bar n_B}
>\zeta^2,
}
$$

where $R_{\rm WZ}=\zeta c/\omega_B$.

At high temperature,

$$
\boxed{
\mathfrak W_B
\simeq
\frac{5\mathcal O}{12}
Q_B\mathcal C_B\beta_B^6
\frac{\lambda_T}{L_B},
\qquad
\lambda_T=\hbar c/(k_BT).
}
$$

This is a receiver-class feasibility condition, not a universal quantum-gravity no-go theorem.

File: `PASSIVE_WAVEZONE_FEASIBILITY_BOUND.md`.

---

## 13. Receiver-theory caveats

The passive nonrelativistic oscillator-strength ceiling does not automatically extend to relativistic QFT because spatially smeared stress-energy operators retain UV pair excitations.

For passive Gibbs receivers, the robust mode-level statement is KMS/fluctuation-dissipation:

$$
S_H(\omega)
=\hbar\coth\left(\frac{\hbar\omega}{2k_BT}\right)\chi''(\omega).
$$

Active/inverted collective states can show $N^2$ gravitational transition enhancement, but known examples enhance vacuum gravitational transitions as well, so activity does not automatically improve quantum efficiency.

---

## 14. Novelty boundary

Established prior art includes:

- two-coherent-state effective-entanglement tests of quantum devices;
- the exact hybrid qubit–coherent input passed through a thermal beam-splitter channel;
- thermal/phase-insensitive Gaussian-channel EB thresholds;
- entanglement distribution through every non-EB phase-insensitive Gaussian channel using other input/distillation protocols;
- graviton coherent states, quadrupole radiation, retarded GIE, input-output theory, and Gaussian thermal gravity-channel tests.

Closest hybrid predecessor: **Kreis & van Loock, PRA 85, 032307 (2012)**. They study the same symmetric hybrid cat and thermal channel but use a sufficient moment witness and explicitly note that it can fail below the channel EB threshold.

Earlier device-testing prior art: **Häseler, Moroder & Lütkenhaus, PRA 77, 032303 (2008)** use two coherent states and effective entanglement, with moment-based criteria.

A 2023/24 result by **Mele, Lami & Giovannetti** proves that all non-EB phase-insensitive Gaussian channels have nonzero two-way quantum capacity using a different Fock-state/distillation construction.

The targeted searches have **not yet located** the stronger statement now derived here:

$$
\boxed{
\text{every nontrivial finite binary coherent hybrid input}
\text{ is NPT iff a gauge-covariant phase-insensitive Gaussian channel is non-EB}
}
$$

nor the matched exact three-element witness or the gravity-specific causal reception-cone construction.

**Novelty remains unverified.** Do not claim originality until broader literature review and independent mathematical scrutiny are complete.

Files: `NOVELTY_CHECK_FINITE_CAT.md`, `PRIOR_ART_BINARY_COHERENT_TESTS.md`, `BINARY_COHERENT_EB_PROBE_THEOREM.md`, `PHASE_INSENSITIVE_GAUSSIAN_BINARY_PROBE_THEOREM.md`.

---

## 15. Strongest next path

1. Perform a citation-forward/general-theorem novelty check for the all-phase-insensitive binary coherent probe theorem.
2. Evaluate the passive wave-zone figure $\mathfrak W_B$ for representative receiver classes and identify whether any plausible nonrelativistic architecture approaches the required regime.
3. Analyze phase-sensitive/non-Gaussian active receivers as the main remaining quantum-receiver loophole.
4. If the theorem survives, reorganize the main Experiment 01 paper around:
   - exact binary coherent Gaussian-channel lemma;
   - retarded gravitational difference mode;
   - exact causal NPT front;
   - finite-certification front;
   - finite-aperture quantum reception cone.

## Current Einstein/Feynman compression

> **A gravitational branch signal and a quantum gravitational channel are not the same thing. Relativity sets the earliest arrival at $R/c$. After arrival, a receiver becomes entangled with the source only if coherent coupling to the correct gravitational difference mode outruns the receiver's own classicalizing noise. For binary coherent branch records this boundary is exact for the entire phase-insensitive Gaussian-channel family and does not depend on cat size. Cat size reappears when one asks for a finite measurable violation. A finite wave-zone receiver then has an additional geometric problem: it must physically catch enough of a spherical spin-2 mode. The result is a nested spacetime structure—light cone, NPT cone, and finite-certification cone—with a finite thermal quantum-reception range even though the classical gravitational wave continues outward indefinitely.**