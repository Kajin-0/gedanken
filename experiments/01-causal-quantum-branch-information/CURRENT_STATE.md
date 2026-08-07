# Current State — Experiment 01

**Last updated:** 2026-08-07 16:46 EDT  
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

The history-coherence norm is

$$
C_\Xi=\|\Xi\|_1.
$$

For pure conditional global histories,

$$
C_\Xi=F(\rho_E^L,\rho_E^R),
$$

so $C_\Xi$ measures how indistinguishable the unobserved complementary records remain. Keep the paper-level theory operational in $(\rho_L,\rho_R,\Xi)$ rather than assuming a fundamental source-field-probe Hilbert-space factorization.

---

## 2. Operational entanglement tests

Every balanced separable state obeys

$$
\boxed{C_\Xi^2+D_B^2\le1},
\qquad
D_B=\frac12\|\rho_L-\rho_R\|_1,
$$

and the stronger fidelity bound

$$
\boxed{C_\Xi\le F(\rho_L,\rho_R)}.
$$

A positive violation certifies source-receiver entanglement.

---

## 3. Causal structure

For a controlled source operation at $t=0$ and receiver distance $R$,

$$
D_B(T,R)=0\qquad T<R/c
$$

for the source-controlled contribution.

Distinguish three fronts:

1. **signal front** — first causal gravitational response;
2. **NPT front** — first source-receiver entanglement;
3. **global-history front** — first low-cost coherence/fidelity certification.

---

## 4. Gauge-invariant gravitational signal

A self-contained free receiver couples to tidal curvature,

$$
H_{\rm drive}=\mu_BL_B\mathcal E_{nn}x_B,
\qquad
\mathcal E_{ij}=c^2R_{0i0j}.
$$

For the conserved plus quadrupole

$$
\Delta Q_{xx}=q(t),\qquad \Delta Q_{yy}=-q(t),
$$

with receiver on the $z$ axis,

$$
\boxed{
\Delta\mathcal E_{xx}
=-\frac{G}{R^5}
\left[
3q+\frac{3R}{c}\dot q+\frac{3R^2}{c^2}\ddot q
+\frac{2R^3}{c^3}q^{(3)}+\frac{R^4}{c^4}q^{(4)}
\right]_{t-R/c}.
}
$$

For harmonic motion,

$$
P(\epsilon)=3-3i\epsilon-3\epsilon^2+2i\epsilon^3+\epsilon^4,
\qquad
\epsilon=\omega R/c,
$$

is the exact static/induction/wave-zone crossover polynomial for this geometry.

---

## 5. Wave-zone difference mode

All coherent branch-distinguishing graviton radiation can be compressed into one normalized bosonic difference mode. Define

$$
N_\Delta
=\sum_\lambda\int d^3k\,
|\beta^L_{\mathbf k\lambda}-\beta^R_{\mathbf k\lambda}|^2.
$$

After subtracting the common coherent displacement, the two radiation histories are equivalent to

$$
|\pm\sqrt{N_\Delta}/2\rangle.
$$

Thus the wave-zone problem reduces to one-mode quantum state transfer.

---

## 6. NEW strongest analytic result: exact finite-cat thermal theorem

For the hybrid source-cat input

$$
|\Psi_a\rangle
=\frac{|L\rangle|a\rangle+|R\rangle|-a\rangle}{\sqrt2},
\qquad 0<|a|<\infty,
$$

send the bosonic branch-difference mode through a thermal attenuator of coherent transmissivity $\eta$ and environment occupation $\bar n$.

Define the output thermal occupation generated from vacuum,

$$
m=(1-\eta)\bar n.
$$

Then, for **every finite nonzero cat amplitude**,

$$
\boxed{
\rho_{AB}\text{ is NPT}
\iff
\eta>m
\iff
\eta>\frac{\bar n}{\bar n+1}.
}
$$

This closes the previous finite-cat numerical conjecture analytically.

The proof factorizes the partially transposed thermal-channel blocks and reduces them, by congruence on the analytic domain, to

$$
\frac12
\begin{pmatrix}
I&qD(-u)\\
qD(u)&I
\end{pmatrix},
$$

where $D(u)$ is unitary and

$$
\boxed{
q=\exp\left[
\frac{2|a|^2}{m}(\eta-m)
\right].
}
$$

Hence a negative direction exists exactly when $q>1$, i.e. $\eta>m$. Below that point the thermal attenuator is entanglement breaking and the output is separable for every input.

Full derivation: `EXACT_FINITE_CAT_THERMAL_THEOREM.md`.

**Key consequence:** cat amplitude controls the amount of entanglement, but **not the exact thermal NPT boundary**.

---

## 7. Exact causal quantum-front speed limit

For the passive Markov receiver

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

and thermal injection

$$
\boxed{
\Gamma_{\rm th}=\sum_a\bar n_a\kappa_a,
}
$$

any normalized incoming branch-difference waveform obeys

$$
\boxed{
\eta_f(\tau)
\le
\frac{\kappa_\Delta}{\kappa_{\rm tot}}
(1-e^{-\kappa_{\rm tot}\tau}),
\qquad
\tau=t-R/c.
}
$$

The exact finite-cat theorem gives

$$
\boxed{
\rho_{AB}(t)\text{ is NPT}
\iff
\eta_f(t)>m(t)
}
$$

at every time where the reduced receiver channel is a thermal attenuator.

For a stationary receiver,

$$
m_*=\frac{\Gamma_{\rm th}}{\kappa_{\rm tot}}.
$$

Therefore **no finite source cat** can generate an NPT front if

$$
\boxed{\kappa_\Delta\le\Gamma_{\rm th}.}
$$

Above threshold, every normalized waveform satisfies the tight causal bound

$$
\boxed{
T_{\rm NPT}
\ge
\frac Rc+
\frac1{\kappa_{\rm tot}}
\ln\left[
\frac{\kappa_\Delta}
{\kappa_\Delta-\Gamma_{\rm th}}
\right].
}
$$

The bound is saturated by the time-reversed receiver ringdown waveform.

Define

$$
\epsilon_Q
=1-\frac{\Gamma_{\rm th}}{\kappa_\Delta}.
$$

Then

$$
\boxed{
T_{\rm NPT}^{\min}-R/c
=-\kappa_{\rm tot}^{-1}\ln\epsilon_Q.
}
$$

This is now an **exact finite-cat result within the stated thermal single-mode Markov model**, not a weak-cat approximation.

Detailed theorem: `CAUSAL_FRONT_THEOREM.md`.

---

## 8. Source-receiver gravitational mode matching

The useful branch-mode rate is

$$
\boxed{\kappa_\Delta=\mathcal O_{SB}\kappa_g.}
$$

For complete angular access, the quadrupole overlap is

$$
\boxed{
\mathcal O_Q
=\frac{|Q_B^{ij*}Q^S_{ij}|^2}
{(Q_B^{ij*}Q^B_{ij})(Q_S^{ij*}Q^S_{ij})}.
}
$$

For two plus quadrupoles rotated by $\psi$,

$$
\mathcal O_Q=\cos^2(2\psi).
$$

For normalized Lorentzian/exponential temporal modes,

$$
\mathcal O_t
=\frac{4\kappa_S\kappa_B}
{(\kappa_S+\kappa_B)^2+4\Delta^2}.
$$

When separable,

$$
\mathcal O_{SB}
=\beta_{\rm access}\mathcal O_Q\mathcal O_t\mathcal O_{\rm other}.
$$

---

## 9. Receiver gravitational coupling

The total gravitational receiver coupling is its spontaneous quadrupole graviton linewidth,

$$
\boxed{
\kappa_g
=\frac{2G\omega_B^5}{5\hbar c^5}
Q_{ij}^{10}Q_{ij}^{01}.
}
$$

Time-reversal reciprocity gives the same matrix element for matched absorption.

For ordinary passive nonrelativistic matter, a quadrupole oscillator-strength sum rule gives a strong receiver ceiling. Active/inverted collective states can evade that passive bound and show $N^2$ transition enhancement, but known models enhance vacuum gravitational transitions by the same collective factor, so activity does not automatically improve quantum efficiency.

---

## 10. Relativistic receiver correction

The nonrelativistic compactness/oscillator-strength ceiling does not extend automatically to relativistic QFT: spatially smeared stress energy still contains UV pair excitations.

What survives for a passive Gibbs receiver is the mode-resolved KMS fluctuation-dissipation relation

$$
\boxed{
S_H(\omega)
=
\hbar\coth\left(
\frac{\hbar\omega}{2k_BT}
\right)\chi''(\omega).
}
$$

Thus relativistic receivers may evade an absolute response ceiling, but not the passive equilibrium noise-to-response relation.

---

## 11. Novelty status

Established neighboring ingredients include thermal-attenuator entanglement-breaking thresholds, entangled coherent states in noisy channels, retarded gravity-mediated entanglement, Gaussian thermal gravity-channel tests, input-output state transfer, graviton quadrupole emission, and quantum speed limits for channels becoming entanglement breaking.

A targeted 2026-08-07 search did **not** locate the exact combination now obtained:

1. finite hybrid coherent cats are NPT for every nonzero finite amplitude iff the thermal attenuator is non-entanglement-breaking;
2. combining that exact family theorem with a retarded matched receiver produces a waveform-optimal earliest NPT front after $R/c$.

This is **promising but novelty unverified**. Do not claim originality until a broader literature review and independent proof check are completed.

---

## 12. Strongest next path

1. Independently check the finite-cat operator-factorization proof, especially infinite-dimensional domain details.
2. Search more broadly for an equivalent finite-cat theorem in hybrid entanglement / non-Gaussian Gaussian-channel literature.
3. If the proof survives, rewrite Experiment 01 around the exact finite-cat causal-front theorem rather than the earlier heuristic history-transfer narrative.
4. Derive the NPT magnitude near the exact boundary and its dependence on $N_\Delta$ to obtain experimentally useful scaling.
5. Then map the exact receiver theorem onto linearized gravity with fully explicit source and receiver wavepackets.

## Current Einstein/Feynman compression

> **Relativity fixes when the gravitational branch signal may first arrive: not before $R/c$. But arrival is not enough. The receiver must coherently catch the correct branch-difference mode faster than thermal noise turns that information into an ordinary classical record. For the full finite coherent-cat family, this transition is exact: every nonzero finite cat becomes entangled with the receiver if and only if coherent capture exceeds the receiver's thermal occupation. No larger cat can force an entanglement-breaking receiver to become quantum. Once the channel is quantum-capable, cat size changes how much entanglement appears, but not when the NPT front is allowed to begin.**