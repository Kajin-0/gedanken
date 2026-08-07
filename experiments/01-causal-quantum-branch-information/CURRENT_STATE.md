# Current State — Experiment 01

**Last updated:** 2026-08-07 16:21 EDT  
**Experiment:** Causal Transport of Quantum Branch Information by Gravity

This is the canonical compact recovery point. Detailed derivations live in the experiment directory and timestamped `checkpoints/`.

---

## 1. Core operational question

Can gravity transport information about a coherent source alternative to a distant quantum receiver **causally**, while preserving enough coherence between the two histories that source and receiver become entangled?

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

so $C_\Xi$ is the fidelity of the unobserved complementary records. Keep the final theory operational in $(\rho_L,\rho_R,\Xi)$ rather than assuming a fundamental source-field-probe factorization.

---

## 2. Entanglement tests

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

For the weak-cat thermal problem, a targeted PPT witness uses only

$$
P_{+,1},\quad P_{-,0},\quad Z_0=\langle-,1|\rho|+,0\rangle,
$$

with

$$
\boxed{|Z_0|^2>P_{+,1}P_{-,0}}
$$

certifying NPT entanglement exactly at the thermal channel boundary in the weak-cat limit.

---

## 3. Causality and the three fronts

For a controlled source operation at $t=0$ and receiver distance $R$,

$$
D_B(T,R)=0\qquad T<R/c
$$

for the source-controlled contribution.

Distinguish:

1. **signal front** — first causal gravitational response;
2. **NPT front** — first source-receiver entanglement;
3. **global-history front** — first low-cost fidelity/coherence certification.

---

## 4. Gauge-invariant gravitational response

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

All branch-dependent coherent graviton radiation can be compressed into one normalized bosonic **difference mode**:

$$
N_\Delta
=\sum_\lambda\int d^3k\,
|\beta^L_{\mathbf k\lambda}-\beta^R_{\mathbf k\lambda}|^2.
$$

After removing the branch-common displacement, the two field histories are equivalent to

$$
|\pm\sqrt{N_\Delta}/2\rangle.
$$

Thus the wave-zone problem is a one-mode quantum state-transfer problem.

For vacuum capture fraction $\eta$, exact source-receiver entanglement exists for every finite $N_\Delta>0$ and every $\eta>0$, although the simple global-history witness needs $\eta>1/2$.

At tiny capture,

$$
\boxed{N_\Delta^{\rm opt}=4\sqrt\eta+O(\eta)},
$$

$$
\boxed{\mathcal N_{\max}=\eta-2\eta^{3/2}+O(\eta^2)}.
$$

Therefore arbitrarily large stimulated classical response cannot parametrically beat the quantum entanglement-transfer rate.

---

## 6. Thermal channel hierarchy

For a thermal attenuator of capture fraction $\eta$ and bath occupation $\bar n$:

Fundamental weak-cat entanglement boundary:

$$
\boxed{\eta_{\rm ent}=\frac{\bar n}{\bar n+1}}.
$$

Global fidelity-history threshold:

$$
\boxed{\eta_F=\frac{2\bar n+1}{2\bar n+2}}.
$$

The targeted PPT witness reaches $\eta_{\rm ent}$ in the weak-cat limit.

For output thermal occupation $m=(1-\eta)\bar n$,

$$
\boxed{
\mathcal N_{AB}
=\frac{N_\Delta}{4}\frac{\eta-m}{m}+O(N_\Delta^2)
}
$$

for $m>0$ near threshold.

A reproducible truncated Fock-space scan in `numerics/thermal_cat_scan.py` gives preliminary evidence that above the EB boundary the binary coherent source-cat remains NPT for every finite branch separation tested, with negativity peaking at an intermediate $N_\Delta$ and tending back toward zero for very large cats. This is a numerical conjecture, not a theorem.

---

## 7. Source–receiver mode overlap

For complete angular access, the normalized spatial/polarization overlap of source and receiver quadrupolar graviton modes is

$$
\boxed{
\mathcal O_Q
=
\frac{|Q_B^{ij*}Q^S_{ij}|^2}
{(Q_B^{ij*}Q^B_{ij})(Q_S^{ij*}Q^S_{ij})}.
}
$$

For two plus quadrupoles rotated by $\psi$ about their common axis,

$$
\boxed{\mathcal O_Q=\cos^2(2\psi)}.
$$

Random relative orientation gives

$$
\langle\mathcal O_Q\rangle=1/5.
$$

For normalized exponential/Lorentzian temporal modes,

$$
\boxed{
\mathcal O_t
=\frac{4\kappa_S\kappa_B}
{(\kappa_S+\kappa_B)^2+4\Delta^2}.
}
$$

When factors separate,

$$
\boxed{
\mathcal O_{SB}
=\beta_{\rm access}\mathcal O_Q\mathcal O_t\mathcal O_{\rm other}.
}
$$

The useful gravitational rate is

$$
\boxed{\kappa_\Delta=\mathcal O_{SB}\kappa_g.}
$$

---

## 8. Gravitational input-output rate

The receiver's total gravitational coupling equals its spontaneous quadrupole graviton-emission linewidth,

$$
\boxed{
\kappa_g
=\frac{2G\omega_B^5}{5\hbar c^5}
Q_{ij}^{10}Q_{ij}^{01}.
}
$$

By time-reversal reciprocity, the same matrix element controls matched absorption.

For an acoustic bar,

$$
\frac{\kappa_g}{\omega_l}
=\frac{4}{l\pi}
\left(\frac{r_s}{L}\right)
\left(\frac{v_s}{c}\right)^3.
$$

This identifies the severe ordinary-material suppression as compactness times three powers of internal speed divided by $c$.

---

## 9. Passive receiver bound and active loophole

For any stationary **passive** nonrelativistic receiver,

$$
\boxed{
\sum_A\sum_{m<n}
(p_m-p_n)(E_n-E_m)|Q^A_{mn}|^2
=\frac{10}{3}\hbar^2\langle I\rangle_\rho.
}
$$

For a narrow band,

$$
\boxed{
\kappa_{g,\rm net}
\lesssim\frac{4G}{3c^5}\langle I\rangle_\rho\omega_B^4.
}
$$

Define

$$
\mathfrak R_B
=\frac23Q_B\mathcal C_B\beta_B^3,
\qquad
\mathcal C_B=r_{s,B}/L_B,
\quad
\beta_B=\omega_BL_B/c.
$$

Then a necessary passive thermal NPT condition is

$$
\boxed{\mathcal O_{SB}\mathfrak R_B>\bar n_i.}
$$

A necessary global-history condition is

$$
\boxed{(2\mathcal O_{SB}-1)\mathfrak R_B>2\bar n_i+1.}
$$

Known active collective atomic states can exhibit $N^2$ gravitational transition rates. In the published model the same $N^2$ factor multiplies driven/stochastic gravitational response and vacuum gravitational transitions. Thus active collectivity speeds dynamics but does not automatically improve quantum efficiency. The passive sum-rule bound does not apply to those inverted/highly excited states.

---

## 10. Gravitational beta factor

Split

$$
\kappa_g=\kappa_\Delta+\kappa_\perp.
$$

Define

$$
\boxed{
\beta_G
=\frac{\kappa_\Delta}
{\kappa_\Delta+\kappa_\perp+\kappa_i}.
}
$$

Subwavelength $N^2$ collective enhancement multiplies useful and orthogonal gravitational rates together, so it does not improve purely gravitational mode selectivity by itself.

For the plus quadrupole, one ideal hemisphere contains exactly half of the full radiation mode; ideal full-$4\pi$ time-reversal matching can reach unit mode access.

---

## 11. NEW: tight waveform-independent causal NPT speed limit

For a general stationary multiport receiver, define total damping

$$
\kappa_{\rm tot}=\kappa_\Delta+\sum_a\kappa_a
$$

and total thermal injection rate

$$
\boxed{
\Gamma_{\rm th}=\sum_a\bar n_a\kappa_a.
}
$$

For **any normalized incoming branch-difference waveform**,

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

The bound follows from Cauchy-Schwarz and is saturated by the time-reversed receiver kernel in the ideal Markov model.

Therefore a weak-cat NPT front exists only if

$$
\boxed{\kappa_\Delta>\Gamma_{\rm th}.}
$$

When it exists, every normalized input waveform satisfies

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

Define the quantum excess fraction

$$
\boxed{
\epsilon_Q
=1-\Gamma_{\rm th}/\kappa_\Delta.
}
$$

The optimized causal-front law is

$$
\boxed{
T_{\rm NPT}^{\min}-R/c
=-\kappa_{\rm tot}^{-1}\ln\epsilon_Q.
}
$$

At the front,

$$
\boxed{
\left.
\frac{d\eta_{\max}}{dt}
\right|_{T_{\rm NPT}}
=
\kappa_\Delta\epsilon_Q
=
\kappa_\Delta-\Gamma_{\rm th}.
}
$$

Thus the same distance from the EB boundary controls both the logarithmic post-light-cone delay and the vanishing post-front growth rate.

Preliminary novelty search found related quantum-speed-limit work on the opposite process—time to **become** entanglement-breaking—and gravity-channel work on static thermal EB thresholds, but not this exact retarded waveform-optimal entanglement-onset bound. This is promising but unverified.

---

## 12. NEW: relativistic QFT correction

The nonrelativistic passive compactness ceiling does **not** extend automatically to relativistic QFT.

For a smeared stress-energy receiver operator

$$
F_f=\int d^3x\,f_{\mu\nu}(\mathbf x)T^{\mu\nu}(\mathbf x),
$$

passivity gives

$$
\chi_f''(\omega)\ge0
\qquad(\omega>0),
$$

and formally

$$
\int_0^\infty d\omega\,
\omega\chi_f''(\omega)
=
\frac{\pi}{2\hbar^2}
\langle[F_f,[H,F_f]]\rangle_{\rm ren}
$$

when the renormalized double commutator is finite.

However, an explicit free-scalar test shows that smooth **spatial** smearing still permits arbitrarily energetic back-to-back pairs with small total momentum. Stress spectral functions have the expected relativistic UV growth, so no universal finite global oscillator-strength budget follows from passivity alone.

A physical relativistic receiver must therefore be characterized by a finite temporal bandwidth / spacetime smearing or microscopic form factor.

---

## 13. NEW: KMS mode-efficiency law

For a passive Gibbs receiver and one smeared stress-energy mode,

$$
\boxed{
S_H(\omega)
=
\hbar
\coth\left(
\frac{\hbar\omega}{2k_BT}
\right)
\chi''(\omega).
}
$$

Thus relativistic QFT may evade the nonrelativistic **absolute response** ceiling, but it cannot evade the equilibrium **noise-to-response** ratio mode by mode.

For a general multiport receiver, the universal weak-cat thermal condition becomes

$$
\boxed{
\kappa_\Delta
>
\sum_a\bar n_a\kappa_a.
}
$$

The global history witness requires

$$
\boxed{
\kappa_\Delta
>
\sum_a(2\bar n_a+1)\kappa_a.
}
$$

So the relativistic receiver is governed by source-matched spectral cooperativity rather than a universal compactness bound.

---

## 14. Current strongest candidate paper result

The most theorem-like current result is the **causal quantum-front speed limit**:

$$
\boxed{
T_{\rm NPT}^{\min}
=
R/c-\kappa_{\rm tot}^{-1}\ln\epsilon_Q,
\qquad
\epsilon_Q
=1-rac{\Gamma_{\rm th}}
{\mathcal O_{SB}\kappa_g},
}
$$

within an explicitly stated stationary Markov source-mode receiver model.

Its conceptual content is distinct from ordinary retardation:

> The light cone fixes when gravitational influence may arrive. The receiver's quantum efficiency fixes the earliest later time at which enough coherent branch information can have accumulated to survive thermal classicalization.

---

## 15. Immediate frontier

1. Attempt an analytic proof of the finite-cat conjecture suggested by `FINITE_CAT_NUMERICS.md`.
2. Extend the novelty search for causal entanglement-generation latency near EB thresholds.
3. Develop the relativistic source-matched stress-energy spectral cooperativity explicitly for a concrete field-theoretic receiver.
4. Formalize the causal-front speed-limit theorem with assumptions/proof suitable for a paper appendix.

## Current Einstein/Feynman compression

> **The speed of gravity and the speed of gravitational quantum information are not the same question. Relativity says no source-controlled influence may arrive before $R/c$. But after that, the receiver still has to accumulate the correct spin-2 branch mode faster than thermal and uncontrolled channels erase its quantum meaning. Even with the best possible waveform, that takes at least a receiver-lifetime times a logarithm set by the distance from the entanglement-breaking boundary. In ordinary passive matter there is also a severe oscillator-strength ceiling; in relativistic QFT that ceiling disappears, but KMS replaces it with a universal noise-to-response constraint.**