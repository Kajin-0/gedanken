# Current State — Experiment 01

**Last updated:** 2026-08-07 17:02 EDT  
**Experiment:** Causal Transport of Quantum Branch Information by Gravity

This is the canonical compact recovery point. Detailed derivations and timestamped checkpoints live in this experiment directory.

---

## 1. Central operational question

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

so $C_\Xi$ is the fidelity of the unobserved complementary branch records. Keep the paper-level formulation operational in $(\rho_L,\rho_R,\Xi)$ rather than assuming a fundamental source–gravity–receiver Hilbert-space factorization.

---

## 2. Causality

For a controlled source operation at $t=0$ and receiver distance $R$,

$$
D_B(T,R)=0\qquad T<R/c
$$

for the source-controlled contribution.

Distinguish:

1. **signal front** — first causal gravitational response;
2. **NPT front** — first source-receiver entanglement;
3. **global-history front** — first simple coherence/fidelity certification.

---

## 3. Gravitational signal and wave-zone mode

A self-contained freely falling receiver couples to tidal curvature,

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
\Delta\mathcal E_{xx}
=-\frac{G}{R^5}
\left[
3q+\frac{3R}{c}\dot q+\frac{3R^2}{c^2}\ddot q
+\frac{2R^3}{c^3}q^{(3)}+\frac{R^4}{c^4}q^{(4)}
\right]_{t-R/c}.
$$

All coherent branch-distinguishing outgoing graviton radiation can be compressed into one normalized bosonic **difference mode**. If

$$
N_\Delta
=\sum_\lambda\int d^3k\,
|\beta^L_{\mathbf k\lambda}-\beta^R_{\mathbf k\lambda}|^2,
$$

then, after removing the common displacement, the two field histories are equivalent to

$$
|\pm\sqrt{N_\Delta}/2\rangle.
$$

Thus the wave-zone problem becomes one-mode quantum state transfer.

---

## 4. Strongest theorem: exact finite-cat thermal boundary

Consider

$$
|\Psi_a\rangle
=\frac{|0\rangle|a\rangle+|1\rangle|-a\rangle}{\sqrt2},
\qquad 0<|a|<\infty,
$$

with the bosonic mode sent through a thermal attenuator of transmissivity $\eta$ and environmental occupation $\bar n$. Define

$$
\boxed{m=(1-\eta)\bar n.}
$$

Then for **every finite nonzero cat amplitude**,

$$
\boxed{
\rho_{AB}\text{ is NPT}
\iff
\eta>m
\iff
\eta>\frac{\bar n}{\bar n+1}.
}
$$

Thus this hybrid family is NPT everywhere and only everywhere the thermal attenuator is non-entanglement-breaking.

The sign boundary is independent of cat size. Cat size changes the amount and observability of entanglement, not whether the channel can transfer it.

The proof reduces the partial transpose to a displacement-unitary block with

$$
q=\exp\left[
\frac{2|a|^2}{m}(\eta-m)
\right]
$$

and constructs an explicit normalizable negative vector when $q>1$, avoiding reliance on spectral equivalence under an unbounded inverse congruence.

Full proof: `EXACT_FINITE_CAT_THERMAL_THEOREM.md`.

---

## 5. Exact parameter-matched finite-cat witness

The explicit negative vector gives

$$
|\omega\rangle
=\frac{
|0\rangle_A|0\rangle_B
-A|1\rangle_A|v\rangle_B
}{\sqrt{1+A^2}},
$$

with

$$
A=\exp\left(\frac{2\eta a^2}{m^2}\right),
\qquad
v=\frac{2\sqrt\eta\,a}{m}.
$$

For

$$
W=(|\omega\rangle\langle\omega|)^{\Gamma_A},
$$

$$
\boxed{
\operatorname{Tr}(W\rho_{AB})<0
\iff
\eta>m.
}
$$

The associated negativity lower bound is

$$
\mathcal N(\rho_{AB})
\ge
\frac{P(q-1)}{1+A^2},
$$

where

$$
P=\frac1{m+1}e^{-\eta a^2/(m+1)}.
$$

Full derivation: `EXACT_FINITE_CAT_WITNESS.md`.

---

## 6. Exact three-element witness

The same boundary is visible in a single $2\times2$ principal minor of $\rho^{\Gamma_A}$.

Choose

$$
\boxed{
v_*=\frac{2\sqrt\eta\,a}{m}.}
$$

Measure

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

For the finite thermal cat,

$$
\boxed{
\frac{|z_v|^2}{p_0p_v}
=\exp\left[
\frac{4a^2}{m}(\eta-m)
\right].
}
$$

Therefore

$$
\boxed{
|z_v|^2>p_0p_v
\iff
\eta>m
\iff
\rho_{AB}\text{ is NPT}.
}
$$

This detects the exact boundary using **two populations and one joint coherence**, not full tomography.

Full derivation: `EXACT_THREE_ELEMENT_WITNESS.md`.

---

## 7. Exact causal NPT-front theorem

For a passive stationary Markov receiver,

$$
\dot c
=-\frac{\kappa_{\rm tot}}2c
+\sqrt{\kappa_\Delta}\,b_\Delta^{\rm in}
+\sum_a\sqrt{\kappa_a}\,b_a^{\rm in},
$$

where

$$
\kappa_{\rm tot}=\kappa_\Delta+\sum_a\kappa_a
$$

and

$$
\Gamma_{\rm th}=\sum_a\bar n_a\kappa_a.
$$

Any normalized incoming difference-mode waveform obeys

$$
\eta_f(\tau)
\le
\frac{\kappa_\Delta}{\kappa_{\rm tot}}
(1-e^{-\kappa_{\rm tot}\tau}),
\qquad
\tau=t-R/c.
$$

The exact finite-cat theorem gives, at fixed time,

$$
\boxed{
\rho_{AB}(t)\text{ NPT}
\iff
\eta_f(t)>m(t).
}
$$

For a stationary thermal receiver,

$$
m_*=\Gamma_{\rm th}/\kappa_{\rm tot}.
$$

Hence no finite coherent cat can generate an NPT front if

$$
\boxed{\kappa_\Delta\le\Gamma_{\rm th}.}
$$

Above threshold, the tight waveform-independent front is

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

The time-reversed receiver ringdown saturates the bound in the ideal Markov model.

Define

$$
\epsilon_Q=1-\Gamma_{\rm th}/\kappa_\Delta.
$$

Then

$$
T_{\rm NPT}^{\min}-R/c
=-\kappa_{\rm tot}^{-1}\ln\epsilon_Q.
$$

This is now exact for the entire finite coherent-cat family within the stated model.

Full theorem: `CAUSAL_FRONT_THEOREM.md`.

---

## 8. Gravity-specific receiver parameters

The useful branch-mode rate is

$$
\boxed{\kappa_\Delta=\mathcal O_{SB}\kappa_g.}
$$

The total gravitational receiver linewidth is

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

The exact gravitational front is therefore

$$
T_{\rm NPT}^{\min}
=
\frac Rc+
\frac1{\kappa_{\rm tot}}
\ln\left[
\frac{\mathcal O_{SB}\kappa_g}
{\mathcal O_{SB}\kappa_g-\Gamma_{\rm th}}
\right]
$$

within the receiver model.

---

## 9. Receiver limits

For ordinary stationary passive nonrelativistic matter, an energy-weighted quadrupole sum rule limits net gravitational oscillator strength. Active/inverted collective states can show $N^2$ gravitational transition enhancement, but known examples enhance vacuum gravitational transitions by the same collective factor and therefore do not automatically improve quantum efficiency.

The nonrelativistic absolute-response ceiling does not extend automatically to relativistic QFT because spatially smeared stress-energy operators retain UV pair excitations.

For a passive Gibbs receiver, what does survive mode by mode is KMS/fluctuation-dissipation:

$$
S_H(\omega)
=
\hbar\coth\left(
\frac{\hbar\omega}{2k_BT}
\right)\chi''(\omega).
$$

---

## 10. Novelty boundary — latest literature result

The closest predecessor is:

**Kreis & van Loock, Phys. Rev. A 85, 032307 (2012), arXiv:1111.0478.**

They study the **same hybrid state**

$$
(|0\rangle|\alpha\rangle+|1\rangle|-\alpha\rangle)/\sqrt2
$$

through the **same one-sided thermal beam-splitter channel**.

They derive the exact noisy output, then use a finite-order Shchukin–Vogel moment determinant as a sufficient witness. Their witness has an amplitude-dependent detection region. Crucially, their footnote [47] explicitly compares it with the thermal channel's entanglement-breaking boundary and notes that the witness may miss entangled states below that boundary.

The present theorem appears to close exactly that gap:

$$
\boxed{
\text{for every finite }\alpha\neq0,
\quad
\text{non-EB thermal channel}
\iff
\text{NPT hybrid output}.
}
$$

The present three-element witness additionally detects the complete region for this state family.

Other close primary work found so far treats different two-mode non-Gaussian states or lower bounds under thermal noise, not this exact hybrid iff result.

Detailed literature note: `NOVELTY_CHECK_FINITE_CAT.md`.

**Status:** promising, but novelty remains unverified until broader citation-forward searching and independent mathematical review are complete.

---

## 11. Strongest next path

1. Search for a general theorem that would imply the finite-cat iff result indirectly, especially binary coherent-state probes of entanglement-breaking Gaussian channels.
2. Optimize/simplify the exact three-element witness for practical source-receiver measurements.
3. Derive exact or tight near-boundary negativity scaling for arbitrary finite cat amplitude.
4. If those survive, reorganize the main Experiment 01 paper around the exact finite-cat causal-front theorem.
5. Then insert fully explicit linearized-gravity source and receiver wavepackets.

## Current Einstein/Feynman compression

> **Relativity fixes when a gravitational branch signal may arrive: not before $R/c$. But arrival alone does not make the receiver quantum-correlated with the source. The receiver must catch the correct branch-difference mode faster than thermal noise turns that information into an ordinary record. For the entire finite coherent-cat family this boundary is exact and independent of cat size. A larger cat cannot force an entanglement-breaking channel to transmit entanglement. If the channel is quantum-capable, every finite nonzero cat transmits some entanglement, and a matched three-element source-receiver witness can detect it exactly at the same boundary.**