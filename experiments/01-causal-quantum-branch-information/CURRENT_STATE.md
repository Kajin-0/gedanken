# Current State — Experiment 01

**Last updated:** 2026-08-07 16:12 EDT  
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

so $C_\Xi$ is the fidelity of the unobserved complementary records. The final theory should remain operational in $(\rho_L,\rho_R,\Xi)$ rather than assume a fundamental source-field-probe factorization.

---

## 2. Entanglement witnesses

Every balanced separable state obeys

$$
\boxed{C_\Xi^2+D_B^2\le1},
\qquad
D_B=\frac12\|\rho_L-\rho_R\|_1.
$$

A stronger fidelity relation is

$$
\boxed{C_\Xi\le F(\rho_L,\rho_R)}.
$$

For the weak-cat thermal problem, a targeted PPT witness reaches the true thermal boundary using only

$$
P_{+,1},\quad P_{-,0},\quad Z_0=\langle-,1|\rho|+,0\rangle,
$$

with

$$
\boxed{|Z_0|^2>P_{+,1}P_{-,0}}
$$

certifying NPT entanglement.

---

## 3. Causal fronts

For a controlled source operation at $t=0$ and receiver distance $R$,

$$
D_B(T,R)=0\qquad T<R/c
$$

for the source-controlled contribution.

Distinguish:

1. **signal front** — first causal gravitational response;
2. **NPT front** — first source-receiver entanglement;
3. **global-history front** — first low-cost fidelity/coherence certification.

For a stationary thermal matched receiver, weak-cat NPT exists iff

$$
\boxed{\kappa_\Delta>\bar n_i\kappa_i},
$$

where $\kappa_\Delta$ is the useful source-mode gravitational coupling. The optimized front is

$$
\boxed{
T_{\rm NPT}
=\frac Rc+
\frac1{\kappa_g+\kappa_i}
\ln\left[
\frac{\kappa_\Delta}
{\kappa_\Delta-\bar n_i\kappa_i}
\right].
}
$$

Near the threshold the front moves logarithmically behind $R/c$ and the post-front entanglement growth rate vanishes linearly: **double critical slowing**.

---

## 4. Gauge-invariant gravitational signal

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

All branch-dependent coherent graviton radiation can be compressed into one normalized bosonic **difference mode**. Define

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

For vacuum capture fraction $\eta$, exact source-receiver entanglement exists for every finite $N_\Delta>0$ and every $\eta>0$, although the simple global history witness requires $\eta>1/2$.

At tiny capture, optimizing branch-wave strength gives

$$
\boxed{N_\Delta^{\rm opt}=4\sqrt\eta+O(\eta)},
$$

$$
\boxed{\mathcal N_{\max}=\eta-2\eta^{3/2}+O(\eta^2)}.
$$

So a huge coherent gravitational wave cannot parametrically beat a weak quantum capture rate: the uncaptured wave becomes too good a which-branch record.

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

In output-noise variables $m=(1-\eta)\bar n$,

$$
\boxed{
\mathcal N_{AB}
=\frac{N_\Delta}{4}\frac{\eta-m}{m}+O(N_\Delta^2)
}
$$

for $m>0$ near threshold.

---

## 7. Gravitational input-output rate

The receiver-gravity coupling equals the spontaneous quadrupole graviton-emission linewidth,

$$
\boxed{
\kappa_g
=\frac{2G\omega_B^5}{5\hbar c^5}
Q_{ij}^{10}Q_{ij}^{01}.
}
$$

By time-reversal reciprocity, the same matrix element controls matched absorption.

For a cylindrical acoustic bar,

$$
\boxed{
\kappa_g
=\frac{8GML^2\omega_l^4}{l^4\pi^4c^5},
}
$$

and with acoustic dispersion

$$
\boxed{
\frac{\kappa_g}{\omega_l}
=\frac{4}{l\pi}
\left(\frac{r_s}{L}\right)
\left(\frac{v_s}{c}\right)^3.
}
$$

Thus ordinary material receivers are suppressed by tiny compactness and three powers of nonrelativistic internal speed.

---

## 8. Passive receiver oscillator-strength ceiling

For any stationary **passive** nonrelativistic receiver,

$$
\boxed{
\sum_A\sum_{m<n}
(p_m-p_n)(E_n-E_m)|Q^A_{mn}|^2
=\frac{10}{3}\hbar^2\langle I\rangle_\rho.
}
$$

Equivalently,

$$
\boxed{
\int_0^\infty d\omega\,\omega
\sum_A\chi_{AA}''(\omega)
=\frac{10\pi}{3}\langle I\rangle_\rho.
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
\mathcal C_B=\frac{r_{s,B}}{L_B},
\qquad
\beta_B=\frac{\omega_BL_B}{c},
\qquad
\kappa_i=\frac{\omega_B}{Q_B}.
$$

Then

$$
\boxed{
\frac{\kappa_{g,\rm net}}{\kappa_i}
\lesssim
\mathfrak R_B
=\frac23Q_B\mathcal C_B\beta_B^3.
}
$$

This is a **passive receiver bound**, not a universal many-body bound.

---

## 9. Active collective loophole

Known correlated two-level bosonic-atom states can exhibit $N^2$ gravitational transition rates. In the published collective model, favorable states have

$$
\Gamma_{\rm gw}=\frac{N^2}{4}\Gamma_0N_{\rm gw},
$$

$$
\Gamma_{\rm vac}=\frac{N^2}{4}\Gamma_0.
$$

Thus the same $N^2$ factor speeds driven gravitational response and vacuum gravitational transitions. These highly excited states are nonpassive and lie outside the passive sum-rule positivity argument.

For a general stationary active state,

$$
\boxed{
S_+-S_-
=\frac{10}{3}\hbar^2\langle I\rangle_\rho.
}
$$

Response beyond the passive ceiling requires an active/inverted spectral resource $S_-$.

A quantum-limited amplifier toy model gives the same warning: gain can increase classical branch amplitude while added spontaneous noise keeps the channel's distance from entanglement breaking controlled by the underlying weak coupling. Post-capture local amplification cannot increase entanglement at all.

---

## 10. Gravitational beta factor and angular access

Split total gravitational coupling into useful source-mode and orthogonal channels,

$$
\kappa_g=\kappa_\Delta+\kappa_\perp,
$$

and define

$$
\boxed{
\beta_G
=\frac{\kappa_\Delta}
{\kappa_\Delta+\kappa_\perp+\kappa_i}.
}
$$

For a subwavelength collective state, $N^2$ enhancement multiplies $\kappa_\Delta$ and $\kappa_\perp$ together, so it speeds dynamics but does not improve the purely gravitational branching fraction.

For the plus quadrupole, the angular radiation weight is

$$
W=(1+\cos^2\theta)^2\cos^22\phi+4\cos^2\theta\sin^22\phi.
$$

An ideal one-cap angular fraction is

$$
\boxed{
\beta_{\rm cap}
=\frac12-
\frac{u_0^5+10u_0^3+5u_0}{32},
\qquad u_0=\cos\theta_0.
}
$$

One hemisphere contains exactly half of the full mode; ideal full-$4\pi$ access can reach unit mode access.

---

## 11. NEW: invariant source-receiver mode overlap

For complete angular access, the normalized spatial/polarization overlap of source and receiver quadrupolar graviton modes is

$$
\boxed{
\mathcal O_Q
=
\frac{|Q_B^{ij*}Q^S_{ij}|^2}
{(Q_B^{ij*}Q^B_{ij})(Q_S^{ij*}Q^S_{ij})}.
}
$$

For two plus quadrupoles rotated about their common axis by angle $\psi$,

$$
\boxed{\mathcal O_Q=\cos^2(2\psi).}
$$

A $45^\circ$ rotation makes the modes orthogonal; a $90^\circ$ rotation restores unit overlap with sign/phase reversal. Random relative orientation gives

$$
\langle\mathcal O_Q\rangle=1/5.
$$

For normalized exponential/Lorentzian temporal modes with linewidths $\kappa_S,\kappa_B$ and detuning $\Delta$,

$$
\boxed{
\mathcal O_t
=\frac{4\kappa_S\kappa_B}
{(\kappa_S+\kappa_B)^2+4\Delta^2}.
}
$$

When the overlap factors separate,

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

The thermal weak-cat NPT condition is therefore

$$
\boxed{\mathcal O_{SB}\kappa_g>\bar n_i\kappa_i.}
$$

The global history witness requires

$$
\boxed{(2\mathcal O_{SB}-1)\kappa_g>(2\bar n_i+1)\kappa_i,}
$$

so it has an irreducible geometric requirement

$$
\mathcal O_{SB}>1/2.
$$

The mode-corrected NPT front is

$$
\boxed{
T_{\rm NPT}
=\frac Rc+
\frac1{\kappa_g+\kappa_i}
\ln\left[
\frac{\mathcal O_{SB}\kappa_g}
{\mathcal O_{SB}\kappa_g-\bar n_i\kappa_i}
\right].
}
$$

---

## 12. NEW: two-resource passive receiver phase diagram

Combining mode overlap with the passive ceiling gives

$$
\boxed{
\frac{\kappa_\Delta}{\kappa_i}
\lesssim
\mathcal O_{SB}\mathfrak R_B.
}
$$

A necessary passive NPT condition is

$$
\boxed{\mathcal O_{SB}\mathfrak R_B>\bar n_i.}
$$

A necessary global-history condition is

$$
\boxed{(2\mathcal O_{SB}-1)\mathfrak R_B>2\bar n_i+1.}
$$

Thus total gravitational oscillator strength and mode matching are independent resources. Active collective enhancement mainly moves the receiver along the oscillator-strength axis; aperture, tensor alignment, phased-array geometry, and temporal matching move it along the mode-overlap axis.

---

## 13. Relativistic/QFT frontier

The passive bound above relies on a nonrelativistic coordinate quadrupole. In relativistic QFT the natural object is a smeared stress-energy response; equal-time stress-tensor commutators can contain contact/Schwinger terms and require renormalization.

The next theoretical target is therefore a **renormalized spectral-response bound for a smeared stress tensor**, not a naive substitution $Q_{ij}\to T_{ij}$.

---

## 14. Novelty discipline

Do not claim novelty for quadrupole radiation, spin-2 patterns, EWSRs, collective $N^2$ gravitational transitions, Gaussian amplifier noise, input-output mode matching, or thermal entanglement-breaking boundaries.

Potentially distinctive synthesis now includes:

$$
\boxed{
\text{causal branch-difference mode}
+\text{history-coherence/NPT fronts}
+\text{passive receiver oscillator-strength ceiling}
+\text{explicit source-receiver spin-2 mode overlap}.
}
$$

The exact novelty of that synthesis is still unverified.

---

## 15. Immediate frontier

1. Develop the relativistic smeared-stress-tensor spectral formulation.
2. Determine whether a covariant passivity/positivity bound replaces the nonrelativistic compactness ceiling.
3. Quantify whether active gravitational receivers can increase the **distance from entanglement breaking**, not merely transition rate.
4. Continue dedicated primary-literature novelty checks.

## Current Einstein/Feynman compression

> **A gravitational quantum receiver needs two independent resources. It must couple strongly enough to gravity, and it must couple to the right spin-2 mode. Passive nonrelativistic matter has a finite quadrupole-response budget, while geometry and tensor alignment determine what fraction of that budget belongs to the source's actual branch-difference wave. Active collective states can speed the interaction, but if they amplify useful and vacuum channels together they do not automatically make the channel more quantum. The causal entanglement front is controlled by the matched-mode rate, not by raw gravitational sensitivity.**