# Current State — Experiment 01

**Last updated:** 2026-08-07 16:00 EDT  
**Experiment:** Causal Transport of Quantum Branch Information by Gravity

This is the canonical compact recovery point. Full derivations remain in the experiment directory and timestamped `checkpoints/`.

---

## 1. Central question

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

so $C_\Xi$ is the fidelity of the unobserved complementary records. Keep the final formulation operational in $(\rho_L,\rho_R,\Xi)$ rather than assuming a fundamental factorization of a gravitational-field subsystem.

---

## 2. Operational entanglement tests

Every balanced separable state obeys

$$
C_\Xi^2+D_B^2\le1,
\qquad
D_B=\frac12\|\rho_L-\rho_R\|_1,
$$

and the stronger fidelity relation

$$
\boxed{C_\Xi\le F(\rho_L,\rho_R)}.
$$

For the weak-cat thermal problem, a targeted PPT test reaches the exact thermal boundary using only

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
3. **global-history front** — first simple fidelity/coherence certification.

For a stationary thermal matched receiver,

$$
\dot c
=-\frac{\kappa}{2}c
+\sqrt{\kappa_g}\,b_{\rm in}
+\sqrt{\kappa_i}\,\xi_{\rm in},
\qquad
\kappa=\kappa_g+\kappa_i,
$$

and weak-cat NPT exists iff

$$
\boxed{\kappa_g>\bar n_i\kappa_i}.
$$

The optimized NPT front is

$$
\boxed{
T_{\rm NPT}^{\rm opt}
=\frac Rc+rac1\kappa
\ln\frac{\kappa_g}{\kappa_g-\bar n_i\kappa_i}.
}
$$

Near

$$
\delta=\kappa_g-\bar n_i\kappa_i\to0^+,
$$

the delay diverges logarithmically and the post-front entanglement growth rate vanishes linearly: **double critical slowing**.

---

## 4. Gauge-invariant gravitational signal

A self-contained freely falling receiver couples to tidal curvature,

$$
H_{\rm drive}=\mu_BL_B\mathcal E_{nn}x_B,
\qquad
\mathcal E_{ij}=c^2R_{0i0j}.
$$

For the conserved plus-type source quadrupole

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

For harmonic motion the near-to-wave crossover is controlled by

$$
P(\epsilon)=3-3i\epsilon-3\epsilon^2+2i\epsilon^3+\epsilon^4,
\qquad
\epsilon=\omega R/c.
$$

---

## 5. Wave-zone difference mode

All branch-dependent coherent graviton radiation can be compressed into one normalized bosonic difference mode. Define

$$
N_\Delta
=\sum_\lambda\int d^3k\,
|\beta^L_{\mathbf k\lambda}-\beta^R_{\mathbf k\lambda}|^2.
$$

After subtracting the common displacement, the two field histories are equivalent to

$$
|\pm\sqrt{N_\Delta}/2\rangle.
$$

Thus the wave-zone problem is a one-mode quantum state-transfer problem.

For vacuum capture fraction $\eta$, exact source-receiver entanglement survives for every finite $N_\Delta>0$ and every $\eta>0$, although the simple global history witness requires $\eta>1/2$.

At fixed imperfect capture, arbitrarily increasing $N_\Delta$ eventually destroys source-receiver entanglement because the uncaptured field becomes an almost perfect branch record. For $\eta\ll1$,

$$
\boxed{N_\Delta^{\rm opt}=4\sqrt\eta+O(\eta)},
$$

$$
\boxed{\mathcal N_{\max}=\eta-2\eta^{3/2}+O(\eta^2)}.
$$

With short-time matched capture $\eta\simeq\kappa_g\tau$,

$$
\boxed{\mathcal N_{\max}\simeq\kappa_g\tau}.
$$

Hence large stimulated classical response does not parametrically beat the quantum entanglement-transfer rate.

---

## 6. Thermal one-mode channel

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

In output-noise variables $m=(1-\eta)\bar n$, weak-cat negativity is

$$
\boxed{
\mathcal N_{AB}
=\frac{N_\Delta}{4}\frac{\eta-m}{m}+O(N_\Delta^2),
\qquad m>0.
}
$$

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

By reciprocity, the same matrix element controls absorption of the matched incoming graviton mode.

For the cylindrical acoustic bar geometry analyzed by Tobar et al.,

$$
\boxed{
\kappa_g
=\frac{8GML^2\omega_l^4}{l^4\pi^4c^5}.
}
$$

With acoustic dispersion,

$$
\boxed{
\frac{\kappa_g}{\omega_l}
=\frac{4}{l\pi}
\left(\frac{r_s}{L}\right)
\left(\frac{v_s}{c}\right)^3.
}
$$

This makes the laboratory material suppression transparent: tiny compactness times three powers of nonrelativistic internal speed.

---

## 8. Passive quadrupole oscillator-strength ceiling — corrected theorem

The earlier ground-state sum-rule result has now been generalized correctly.

For a stationary state

$$
\rho=\sum_mp_m|m\rangle\langle m|,
$$

with nonincreasing populations with energy (a **passive** state), the quadrupole double-commutator identity is

$$
\boxed{
\sum_A\sum_{m<n}
(p_m-p_n)(E_n-E_m)|Q^A_{mn}|^2
=\frac{10}{3}\hbar^2\langle I\rangle_\rho,
}
$$

where

$$
I=\sum_am_ar_a^2.
$$

Every term is nonnegative for a passive state. Equivalently, the positive-frequency quadrupole susceptibility obeys

$$
\boxed{
\int_0^\infty d\omega\,\omega
\sum_A\chi_{AA}''(\omega)
=\frac{10\pi}{3}\langle I\rangle_\rho.
}
$$

For a narrow receiver band near $\omega_B$, the population-difference-weighted gravitational coupling obeys

$$
\boxed{
\kappa_{g,\rm net}
\lesssim\frac{4G}{3c^5}
\langle I\rangle_\rho\omega_B^4.
}
$$

Thus the compactness/internal-speed receiver ceiling applies to the **net absorptive response of any passive stationary nonrelativistic receiver**, including a Gibbs thermal receiver.

---

## 9. Active collective loophole — important correction

The passive bound is **not** a universal ban on $N^2$ gravitational collective enhancement.

Existing work on correlated two-level bosonic atoms finds specially prepared states with gravitational decay/excitation rates scaling as $N^2$. These are not constrained by the positive-term passive argument because nonpassive population inversions introduce negative spectral terms that can cancel in the double-commutator identity.

Define

$$
S_+=\sum_{p_m\ge p_n}(p_m-p_n)\Delta E_{nm}|Q_{mn}|^2,
$$

$$
S_-=\sum_{p_n>p_m}(p_n-p_m)\Delta E_{nm}|Q_{mn}|^2.
$$

Then exactly

$$
\boxed{
S_+-S_-
=\frac{10}{3}\hbar^2\langle I\rangle_\rho.
}
$$

Hence

$$
\boxed{
S_+
=\frac{10}{3}\hbar^2\langle I\rangle_\rho+S_-.
}
$$

Positive quadrupole response beyond the passive ceiling therefore requires an **active/inverted spectral resource** $S_-$.

The project must now distinguish:

- **passive quantum memory:** constrained by the sum-rule ceiling;
- **active quantum receiver/transducer:** may exceed that ceiling but supplies stored free energy and must include its own quantum noise and branch-record bookkeeping.

---

## 10. Passive receiver phase bound

Define

$$
\mathcal C_B=\frac{r_{s,B}}{L_B},
\qquad
\beta_B=\frac{\omega_BL_B}{c},
\qquad
\kappa_i=\frac{\omega_B}{Q_B}.
$$

For the passive net response,

$$
\boxed{
\frac{\kappa_{g,\rm net}}{\kappa_i}
\lesssim
\mathfrak R_B
\equiv\frac23Q_B\mathcal C_B\beta_B^3.
}
$$

Within the passive nonrelativistic receiver class, necessary conditions remain

$$
\boxed{\mathfrak R_B>\bar n_i}
$$

for finite-temperature NPT transfer, and

$$
\boxed{\mathfrak R_B>2\bar n_i+1}
$$

for the simple global fidelity-history regime.

These are receiver-screening conditions, not universal gravity no-go theorems.

---

## 11. Relativistic/QFT frontier

The passive sum rule uses a coordinate quadrupole and a standard nonrelativistic kinetic Hamiltonian. In relativistic QFT, the natural object is a smeared stress-energy response. Equal-time stress-tensor commutators contain contact/Schwinger terms and stress-tensor correlators require renormalization, so the simple finite geometric ceiling cannot yet be extrapolated unchanged.

The relativistic target is therefore a renormalized spectral-response sum rule for a smeared stress tensor, not a naive replacement $Q_{ij}\to T_{ij}$.

---

## 12. Novelty discipline

Primary-literature searches have not yet identified the exact combination

$$
\text{passive quadrupole EWSR}
\Rightarrow
\text{graviton receiver-linewidth ceiling}
\Rightarrow
\text{thermal receiver phase bound},
$$

but absence from targeted searches is not proof of novelty.

Known collective gravitational sensing work already establishes $N^2$ enhancement in selected active states, so any paper theorem must explicitly state the **passive** assumption.

---

## 13. Immediate frontier

1. Quantify whether an active receiver can actually increase **entanglement-transfer rate**, not merely classical response, after its quantum noise is included.
2. Relate the active spectral budget $S_-$ to a thermodynamic resource such as ergotropy if possible.
3. Develop a relativistic smeared-stress-tensor response bound, with contact terms and renormalization treated explicitly.
4. Continue finite-$N_\Delta$ thermal analysis.

## Current Einstein/Feynman compression

> **A passive receiver cannot obtain unlimited gravitational sensitivity merely by arranging more constituents coherently: it has a finite positive quadrupole oscillator-strength budget. An active, inverted collective state can evade that positivity argument and even show $N^2$ gravitational rates, but then the receiver is supplying stored free energy. That changes the question. The issue is no longer whether the classical response can be amplified, but whether the active receiver can increase the rate at which source entanglement is captured after the amplifier's own quantum noise and branch records are included.**