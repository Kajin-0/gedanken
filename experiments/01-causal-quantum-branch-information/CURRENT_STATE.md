# Current State — Experiment 01

**Last updated:** 2026-08-07 15:55 EDT  
**Experiment:** Causal Transport of Quantum Branch Information by Gravity

This is the canonical compact recovery point. Detailed derivations live in the experiment directory. Newest notes include `QUADRUPOLE_SUM_RULE_BOUND.md` and `RECEIVER_PHASE_BOUND.md`.

---

## 1. Central operational state

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

so $C_\Xi$ is the fidelity of the unobserved complementary records. The paper-level formulation should remain operational in $(\rho_L,\rho_R,\Xi)$ rather than assuming a fundamental gravitational-field subsystem factorization.

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

A targeted weak-cat PPT witness uses only

$$
P_{+,1},\quad P_{-,0},\quad Z_0=\langle-,1|\rho|+,0\rangle,
$$

with

$$
\boxed{|Z_0|^2>P_{+,1}P_{-,0}}
$$

certifying NPT entanglement.

---

## 2. Causal structure

For a controlled source operation at $t=0$ and receiver distance $R$,

$$
D_B(T,R)=0\qquad T<R/c
$$

for the source-controlled contribution.

The experiment distinguishes three fronts:

1. **signal front:** first causal gravitational response;
2. **NPT front:** first source-receiver entanglement;
3. **global-history front:** first simple fidelity/coherence certification.

---

## 3. Gauge-invariant gravitational signal

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

is the exact near-field/induction/wave-zone crossover polynomial for this geometry.

---

## 4. Wave-zone difference mode

All branch-dependent coherent graviton radiation can be compressed into one normalized bosonic difference mode. Define

$$
N_\Delta
=\sum_\lambda\int d^3k\,
|\beta^L_{\mathbf k\lambda}-\beta^R_{\mathbf k\lambda}|^2.
$$

After subtracting the branch-common coherent displacement, the two field histories are equivalent to

$$
|\pm\sqrt{N_\Delta}/2\rangle.
$$

Thus the wave-zone problem becomes a one-mode quantum state-transfer channel.

---

## 5. Thermal channel thresholds and causal fronts

For a thermal attenuator of capture fraction $\eta$ and environment occupation $\bar n$:

Fundamental weak-cat entanglement boundary:

$$
\boxed{\eta_{\rm ent}=\frac{\bar n}{\bar n+1}}.
$$

Global fidelity-history threshold:

$$
\boxed{\eta_F=\frac{2\bar n+1}{2\bar n+2}}.
$$

The targeted $0/1$-sector PPT witness reaches $\eta_{\rm ent}$ in the weak-cat limit.

For a matched receiver,

$$
\dot c
=-\frac{\kappa}{2}c
+\sqrt{\kappa_g}\,b_{\rm in}
+\sqrt{\kappa_i}\,\xi_{\rm in},
\qquad
\kappa=\kappa_g+\kappa_i,
$$

and a fixed normalized input envelope $f$,

$$
\boxed{
\eta_f(t)
=\kappa_g
\left|
\int_{R/c}^{t}ds\,e^{-\kappa(t-s)/2}f(s)
\right|^2.
}
$$

The branch-independent receiver occupation is

$$
\boxed{
 m(t)
=e^{-\kappa\tau}\bar n_0
+\frac{\kappa_i\bar n_i}{\kappa}(1-e^{-\kappa\tau}),
\qquad
\tau=t-R/c.
}
$$

Weak-cat conditions:

$$
\boxed{\text{NPT entanglement: }\eta_f(t)>m(t)},
$$

$$
\boxed{\text{global fidelity witness: }\eta_f(t)>m(t)+1/2}.
$$

For a stationary thermal receiver, the optimized NPT front exists iff

$$
\boxed{\kappa_g>\bar n_i\kappa_i},
$$

and then

$$
\boxed{
T_{\rm NPT}^{\rm opt}
=\frac Rc+\frac1\kappa
\ln\frac{\kappa_g}{\kappa_g-\bar n_i\kappa_i}.
}
$$

Near

$$
\delta=\kappa_g-\bar n_i\kappa_i\to0^+,
$$

$$
T_{\rm NPT}-R/c\sim\kappa^{-1}\ln(\kappa_g/\delta),
$$

while the post-front entanglement growth rate vanishes linearly in $\delta$. This is the current **double critical slowing** result.

---

## 6. Linearized-gravity receiver rate

The gravitational input-output rate is the receiver's spontaneous quadrupole graviton-emission linewidth,

$$
\boxed{
\kappa_g
=\frac{2G\omega_B^5}{5\hbar c^5}
Q_{ij}^{10}Q_{ij}^{01}.
}
$$

By time-reversal reciprocity, the same matrix element controls absorption of the matched incoming graviton mode.

For the cylindrical acoustic bar geometry of Tobar et al.,

$$
\boxed{
\kappa_g
=\frac{8GML^2\omega_l^4}{l^4\pi^4c^5}.
}
$$

For acoustic dispersion $\omega_l=l\pi v_s/L$,

$$
\boxed{
\frac{\kappa_g}{\omega_l}
=\frac{4}{l\pi}
\left(\frac{r_s}{L}\right)
\left(\frac{v_s}{c}\right)^3.
}
$$

Thus ordinary material receivers are suppressed by tiny compactness multiplied by three powers of nonrelativistic internal speed.

---

## 7. Vacuum entanglement-transfer rate limit

For pure-loss capture fraction $\eta$, the exact source-receiver negativity vanishes again for $N_\Delta\to\infty$ when $\eta<1$, because the uncaptured field becomes an almost perfect branch record.

For $\eta\ll1$, optimizing over branch-wave strength gives

$$
\boxed{N_\Delta^{\rm opt}=4\sqrt\eta+O(\eta)},
$$

$$
\boxed{\mathcal N_{\max}=\eta-2\eta^{3/2}+O(\eta^2)}.
$$

With ideal short-time matched capture $\eta\simeq\kappa_g\tau$,

$$
\boxed{\mathcal N_{\max}(\tau)\simeq\kappa_g\tau}.
$$

Therefore arbitrarily strong coherent stimulation can accelerate a classical detector response but cannot parametrically beat the underlying quantum entanglement-transfer rate.

---

## 8. NEW: quadrupole oscillator-strength sum-rule ceiling

Assume a standard nonrelativistic receiver Hamiltonian

$$
H=\sum_a\frac{\mathbf p_a^2}{2m_a}+V(\mathbf x_1,\ldots,\mathbf x_N),
$$

with position-dependent $V$, and STF mass quadrupole

$$
Q_{ij}=\sum_am_a
\left(x_{ai}x_{aj}-\frac13\delta_{ij}r_a^2\right).
$$

Using the energy-weighted double-commutator sum rule over an orthonormal five-component STF basis gives

$$
\boxed{
\sum_A\sum_n(E_n-E_0)
|\langle n|Q_A|0\rangle|^2
=\frac{10}{3}\hbar^2 I,
}
$$

where

$$
I=\sum_am_a\langle r_a^2\rangle_0.
$$

Hence any one transition of frequency $\omega$ satisfies

$$
\boxed{
Q_{ij}^{10}Q_{ij}^{01}
\le\frac{10}{3}\frac{\hbar I}{\omega}.
}
$$

Combining this with the graviton quadrupole rate yields

$$
\boxed{
\kappa_g
\le\frac{4G}{3c^5}I\omega^4.
}
$$

If $L_B^2=I/M$ and $r_{s,B}=2GM/c^2$,

$$
\boxed{
\frac{\kappa_g}{\omega}
\le
\frac23
\left(\frac{r_{s,B}}{L_B}\right)
\left(\frac{\omega L_B}{c}\right)^3.
}
$$

Interpretation: within this nonrelativistic receiver class, many-body quantum engineering may redistribute quadrupole oscillator strength among transitions, but cannot make one finite-frequency transition arbitrarily superextensive at fixed mass, size, and frequency. This blocks a naive unlimited $N^2$ collective enhancement loophole.

Scope warning: momentum-dependent interactions, gauge fields, relativistic dynamics, strongly self-gravitating systems, and field-theoretic modes can lie outside the derivation.

---

## 9. NEW: receiver phase bound

Define receiver compactness and internal-speed parameter

$$
\boxed{\mathcal C_B=\frac{r_{s,B}}{L_B}},
\qquad
\boxed{\beta_B=\frac{\omega_BL_B}{c}}.
$$

With internal linewidth

$$
\kappa_i=\frac{\omega_B}{Q_B},
$$

the sum-rule ceiling implies

$$
\boxed{
\frac{\kappa_g}{\kappa_i}
\le
\mathfrak R_B
\equiv
\frac23Q_B\mathcal C_B\beta_B^3.
}
$$

Therefore a **necessary** condition for any receiver in this class to support a finite-temperature weak-cat NPT front is

$$
\boxed{\mathfrak R_B>\bar n_i}.
$$

A necessary condition for the global fidelity-history regime is

$$
\boxed{\mathfrak R_B>2\bar n_i+1}.
$$

This defines three receiver-level regions:

1. $\mathfrak R_B\le\bar n_i$: NPT transfer impossible within the assumed nonrelativistic quadrupole class;
2. $\bar n_i<\mathfrak R_B\le2\bar n_i+1$: NPT not excluded but strong global history witness excluded by the ceiling;
3. $\mathfrak R_B>2\bar n_i+1$: strong-history capture not ruled out by the sum rule.

At high temperature, with

$$
\lambda_T=\frac{\hbar c}{k_BT},
$$

$$
\boxed{
\frac{\kappa_g}{\bar n_i\kappa_i}
\le
\frac23Q_B\mathcal C_B\beta_B^4
\frac{\lambda_T}{L_B}.
}
$$

So high-temperature nonrelativistic gravitational quantum reception is suppressed by compactness, four powers of the internal relativistic speed parameter, and the thermal length ratio.

---

## 10. Current interpretation

The project now separates **channel capacity** from **receiver capability**.

Gravity may possess coherent quantum channel capacity, while an ordinary material receiver can still be incapable of demonstrating it because its quadrupole oscillator strength and gravitational radiative participation are bounded.

The nonrelativistic sum-rule ceiling points toward the only obvious escape routes:

- relativistic internal dynamics;
- strong compactness/self-gravity;
- field-theoretic receiver degrees of freedom outside the particle-coordinate Hamiltonian used in the sum rule.

---

## 11. Novelty discipline

Established ingredients include energy-weighted sum rules, graviton quadrupole emission, Gaussian thermal channels, entanglement-breaking thresholds, input-output theory, retarded GIE, and coherent-state loss optimization.

The **exact combination**

$$
\text{quadrupole oscillator-strength sum rule}
\Rightarrow
\text{upper bound on gravitational quantum receiver linewidth}
\Rightarrow
\text{receiver phase diagram}
$$

has not yet been established as novel. It requires a dedicated literature search before any novelty claim.

---

## 12. Immediate frontier

1. Search primary literature for quadrupole sum rules explicitly used to bound graviton emission/absorption rates.
2. Determine what replaces the nonrelativistic sum-rule ceiling for relativistic quantum fields or strongly gravitating receivers.
3. Investigate whether a stress-energy spectral sum rule can yield a covariant receiver bound.
4. Continue finite-$N_\Delta$ thermal analysis and test whether the source-cat family remains NPT throughout the full non-entanglement-breaking region.

## Current Einstein/Feynman compression

> **The gravitational quantum receiver problem is not solved by putting more atoms into a clever collective state. Ordinary nonrelativistic matter has only a finite amount of quadrupole oscillator strength to distribute among its transitions. Combining that sum rule with the graviton-emission rate gives an upper bound controlled by compactness and internal relativistic speed. Thus there are two distinct questions: can gravity carry a quantum branch record, and can a chosen receiver possess enough gravitational oscillator strength to catch it before ordinary noise turns it classical? The second problem may be the harder one for laboratory matter.**