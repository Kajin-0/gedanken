# Current State — Experiment 01

**Last updated:** 2026-08-07 15:47 EDT  
**Experiment:** Causal Transport of Quantum Branch Information by Gravity

This is the compact recovery point. Detailed derivations live in the experiment directory; the newest technical notes are `INPUT_OUTPUT_THERMAL_FRONTS.md`, `LINEARIZED_GRAVITY_INPUT_OUTPUT.md`, `VACUUM_CAPTURE_OPTIMIZATION.md`, and `THERMAL_CRITICAL_RATE.md`.

---

## 1. Central operational state

For the balanced source path qubit,

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

so $C_\Xi$ is the fidelity of the unobserved complementary records. Keep the paper-level formulation operational in $(\rho_L,\rho_R,\Xi)$ rather than assuming a fundamental gravitational-field subsystem factorization.

Every balanced separable state obeys

$$
C_\Xi^2+D_B^2\le1,
\qquad
D_B=\frac12\|\rho_L-\rho_R\|_1,
$$

and the stronger fidelity bound

$$
\boxed{C_\Xi\le F(\rho_L,\rho_R)}.
$$

---

## 2. Causal structure

For a controlled source operation at $t=0$ and receiver distance $R$,

$$
D_B(T,R)=0\qquad T<R/c
$$

for the source-controlled contribution.

The experiment distinguishes three fronts:

1. signal front — first causal gravitational response;
2. NPT front — first source-receiver entanglement;
3. global-history front — first simple fidelity/coherence certification.

---

## 3. Gauge-invariant gravitational signal

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

For harmonic motion, the full near-to-wave crossover is controlled by

$$
P(\epsilon)=3-3i\epsilon-3\epsilon^2+2i\epsilon^3+\epsilon^4,
\qquad
\epsilon=\omega R/c.
$$

---

## 4. Wave-zone difference mode

All branch-dependent coherent graviton radiation can be compressed into one normalized bosonic difference mode. Define

$$
N_\Delta
=\sum_\lambda\int d^3k\,
|\beta^L_{\mathbf k\lambda}-\beta^R_{\mathbf k\lambda}|^2.
$$

After subtracting the branch-common displacement, the two field histories are equivalent to

$$
|\pm\sqrt{N_\Delta}/2\rangle.
$$

Thus the causal wave-zone problem is a one-mode quantum state-transfer problem.

---

## 5. Thermal channel thresholds

For a thermal attenuator of capture fraction $\eta$ and environment occupation $\bar n$:

Fundamental weak-cat entanglement boundary:

$$
\boxed{\eta_{\rm ent}=\frac{\bar n}{\bar n+1}}.
$$

Global fidelity-history threshold:

$$
\boxed{\eta_F=\frac{2\bar n+1}{2\bar n+2}}.
$$

A targeted $0/1$-sector PPT witness reaches the fundamental boundary using

$$
|Z_0|^2>P_{+,1}P_{-,0}.
$$

Thus full tomography is not required in the weak-cat limit.

---

## 6. Explicit receiver input-output dynamics

For causal arrival $t_0=R/c$,

$$
\dot c
=-\frac{\kappa}{2}c
+\sqrt{\kappa_g}\,b_{\rm in}
+\sqrt{\kappa_i}\,\xi_{\rm in},
\qquad
\kappa=\kappa_g+\kappa_i.
$$

For normalized gravitational difference-mode envelope $f$,

$$
\boxed{
\eta_f(t)
=\kappa_g
\left|
\int_{t_0}^{t}ds\,
e^{-\kappa(t-s)/2}f(s)
\right|^2.
}
$$

The branch-independent thermal occupation is

$$
\boxed{
 m(t)
=e^{-\kappa\tau}\bar n_0
+\frac{\kappa_i\bar n_i}{\kappa}
(1-e^{-\kappa\tau}),
\qquad
\tau=t-R/c.
}
$$

Weak-cat NPT condition:

$$
\boxed{\eta_f(t)>m(t)}.
$$

Global fidelity-history condition:

$$
\boxed{\eta_f(t)>m(t)+1/2}.
$$

For a stationary thermal receiver,

$$
m_*=\frac{\kappa_i\bar n_i}{\kappa}.
$$

Using the optimally matched transfer

$$
\eta_{\max}=\frac{\kappa_g}{\kappa}(1-e^{-\kappa\tau}),
$$

the NPT front is

$$
\boxed{
T_{\rm NPT}^{\rm opt}
=\frac Rc+rac1\kappa
\ln\frac{\kappa_g}{\kappa_g-\bar n_i\kappa_i}
}
$$

when $\kappa_g>\bar n_i\kappa_i$.

---

## 7. Linearized-gravity receiver rate

The receiver-gravity coupling is not phenomenological. It equals the spontaneous quadrupole graviton-emission linewidth,

$$
\boxed{
\kappa_g
=\frac{2G\omega_B^5}{5\hbar c^5}
Q_{ij}^{10}Q_{ij}^{01}.
}
$$

By time-reversal reciprocity, the same matrix element controls absorption of the matched incoming graviton mode.

For the cylindrical bar geometry analyzed by Tobar et al.,

$$
\boxed{
\kappa_g
=\frac{8GML^2\omega_l^4}{l^4\pi^4c^5}.
}
$$

The fundamental stationary thermal criterion is therefore

$$
\boxed{\kappa_g>\bar n_i\kappa_i}.
$$

At high temperature with $\kappa_i=\omega/Q_i$,

$$
\boxed{Q_i>\frac{k_BT}{\hbar\kappa_g}}.
$$

---

## 8. Vacuum capture optimization — latest information-rate result

For vacuum pure-loss capture fraction $\eta$, the exact source-receiver negativity is

$$
\mathcal N
=\frac14
\left[
\sqrt{(1+s_E)^2-4s_Es_B^2}
-(1-s_E)
\right],
$$

with

$$
s_B=e^{-\eta N_\Delta/2},
\qquad
s_E=e^{-(1-\eta)N_\Delta/2}.
$$

At fixed imperfect capture $\eta<1$,

$$
N_\Delta\to\infty
\quad\Rightarrow\quad
\mathcal N\to0.
$$

A huge branch-dependent wave leaves too strong a which-branch record in the uncaptured field.

For $\eta\ll1$, optimization gives

$$
\boxed{N_\Delta^{\rm opt}=4\sqrt\eta+O(\eta)},
$$

$$
\boxed{\mathcal N_{\max}=\eta-2\eta^{3/2}+O(\eta^2)}.
$$

For an ideal matched receiver at short times,

$$
\eta\simeq\kappa_g\tau,
$$

so

$$
\boxed{\mathcal N_{\max}(\tau)\simeq\kappa_g\tau}.
$$

Therefore increasing coherent gravitational-wave amplitude cannot parametrically beat the weak quantum capture rate when the goal is entanglement transfer. Strong stimulation can accelerate a classical response, but not coherent source-receiver entanglement transfer.

---

## 9. Thermal double critical slowing — latest thermal result

For finite output thermal occupation $m>0$, the weak-cat negativity simplifies to

$$
\boxed{
\mathcal N_{AB}
=\frac{N_\Delta}{4}
\frac{\eta-m}{m}
+O(N_\Delta^2).
}
$$

For the stationary matched receiver define

$$
\delta=\kappa_g-\bar n_i\kappa_i>0.
$$

As $\delta\to0^+$,

$$
\boxed{
T_{\rm NPT}-R/c
\sim\kappa^{-1}\ln(\kappa_g/\delta)
}
$$

while immediately after the front

$$
\boxed{
\left.
\frac{d\mathcal N_{AB}}{dt}
\right|_{T_{\rm NPT}^+}
=
\frac{N_\Delta}{4m_*}\delta
+O(N_\Delta^2).
}
$$

Thus the quantum/classical boundary shows **double critical slowing**:

1. the entanglement front retreats logarithmically behind the light cone;
2. the post-front entanglement growth rate vanishes linearly.

---

## 10. Important receiver-preparation correction

Finite temperature does not automatically imply a post-light-cone delay. If the receiver is freshly ground-state prepared at $R/c$, coherent capture and bath noise initially grow with the same factor. In that ideal matched case the weak-cat state is either NPT immediately after causal arrival when

$$
\kappa_g>\bar n_i\kappa_i,
$$

or never. The finite delay above is generated by a pre-existing thermal floor or by a fixed/mismatched physical wavepacket.

---

## 11. Novelty discipline

Do not claim novelty for coherent-state loss optimization, Gaussian thermal channels, entanglement-breaking thresholds, input-output theory, quadrupole graviton emission, or PPT witnesses.

The potentially distinctive physics remains the synthesis:

$$
\boxed{
\text{causal gravitational branch transport}
+\text{receiver history coherence}
+\text{separate signal/NPT/certification fronts}
}
$$

and especially the gravity-specific interpretation that **stimulated gravitational detection and entanglement transfer have parametrically different limits**.

---

## 12. Immediate frontier

1. Numerically evaluate representative receiver architectures and identify the most favorable scaling of $\kappa_g/(\bar n_i\kappa_i)$.
2. Test finite-$N_\Delta$ thermal entanglement across the full non-entanglement-breaking region.
3. Search specifically for prior work on causal entanglement-front critical slowing and stimulated-response versus entanglement-transfer rate separation.
4. Derive full spherical-mode matching between a branch source quadrupole and an enclosing quantum receiver.

## Current Einstein/Feynman compression

> **A gravitational wave can be made arbitrarily strong, but that does not mean it can transfer entanglement arbitrarily fast. If the receiver catches only a tiny fraction, the rest of the wave becomes an increasingly good record of which source branch occurred. Optimizing this tradeoff shows that the maximum entanglement initially grows only at the receiver's spontaneous-graviton linewidth. At finite temperature there is an even sharper transition: near the point where thermal record formation equals gravitational capture, the entanglement front moves logarithmically far behind the light cone and then grows with a rate that collapses to zero.**