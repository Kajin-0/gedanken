# Passive-State Quadrupole Sum Rule and the Active-Receiver Loophole

**Timestamp:** 2026-08-07 16:00 EDT  
**Status:** Active derivation for Experiment 01

This note sharpens the quadrupole oscillator-strength ceiling. The previous derivation used a ground-state receiver. The physically important extension is to **any stationary passive state**, including an ordinary Gibbs thermal state.

---

## 1. Stationary receiver state

Let

$$
H|m\rangle=E_m|m\rangle,
$$

and let the receiver state commute with the Hamiltonian,

$$
\rho=\sum_m p_m|m\rangle\langle m|.
$$

Order the energies so that

$$
E_0\le E_1\le E_2\le\cdots.
$$

The state is passive when higher-energy levels are never more populated than lower-energy levels,

$$
E_m<E_n\quad\Rightarrow\quad p_m\ge p_n.
$$

Gibbs states satisfy this condition.

---

## 2. Finite-temperature double-commutator identity

For any Hermitian operator $F$,

$$
\frac12\operatorname{Tr}\rho[F,[H,F]]
=
\sum_{m<n}(p_m-p_n)(E_n-E_m)|F_{mn}|^2.
$$

The crucial point is that for a passive state every term on the right-hand side is nonnegative.

For the five orthonormal STF mass-quadrupole components $Q_A$, the coordinate-space double commutator derived previously gives

$$
\boxed{
\sum_A\frac12
\operatorname{Tr}\rho[Q_A,[H,Q_A]]
=
\frac{10}{3}\hbar^2\langle I\rangle_\rho,
}
$$

where

$$
I=\sum_am_ar_a^2.
$$

Therefore

$$
\boxed{
\sum_A\sum_{m<n}
(p_m-p_n)(E_n-E_m)
|Q^A_{mn}|^2
=
\frac{10}{3}\hbar^2\langle I\rangle_\rho.
}
$$

This is the passive-state quadrupole oscillator-strength budget.

---

## 3. Positive-frequency quadrupole susceptibility

Using the standard Kubo convention, define for positive frequency

$$
\chi_{AA}''(\omega)
=
\frac{\pi}{\hbar}
\sum_{m<n}
(p_m-p_n)
|Q^A_{mn}|^2
\delta(\omega-\omega_{nm}),
$$

with

$$
\omega_{nm}=\frac{E_n-E_m}{\hbar}.
$$

Passivity implies

$$
\chi_{AA}''(\omega)\ge0
\qquad(\omega>0).
$$

The first frequency moment is fixed:

$$
\boxed{
\int_0^\infty d\omega\,\omega
\sum_A\chi_{AA}''(\omega)
=
\frac{10\pi}{3}\langle I\rangle_\rho.
}
$$

Thus the receiver has a finite positive-frequency quadrupole-response budget to distribute across its spectrum.

---

## 4. Bound for a narrow receiver band

Suppose a selected receiver band near $\omega_B$ contains quadrupole transitions $\mathcal R$. Then

$$
\sum_{(m,n)\in\mathcal R}\sum_A
(p_m-p_n)|Q^A_{mn}|^2
\le
\frac{10}{3}
\frac{\hbar\langle I\rangle_\rho}{\omega_{\min}},
$$

where $\omega_{\min}$ is the smallest transition frequency in the selected band.

For a narrow band,

$$
\omega_{nm}\simeq\omega_B,
$$

so

$$
\boxed{
\sum_{\mathcal R,A}
(p_m-p_n)|Q^A_{mn}|^2
\lesssim
\frac{10}{3}
\frac{\hbar\langle I\rangle_\rho}{\omega_B}.
}
$$

This is the finite-temperature/passive analogue of the earlier single-transition ground-state bound.

---

## 5. Population-weighted gravitational coupling ceiling

For an individual quadrupole transition,

$$
\gamma_{nm}^{(g)}
=
\frac{2G\omega_{nm}^5}{5\hbar c^5}
Q_{ij}^{nm}Q_{ij}^{mn}.
$$

The quantity relevant to passive linear response is weighted by the population difference $p_m-p_n$. For a narrow band define

$$
\kappa_{g,\rm net}
\equiv
\sum_{\mathcal R}
(p_m-p_n)\gamma_{nm}^{(g)}.
$$

The passive quadrupole budget gives

$$
\boxed{
\kappa_{g,\rm net}
\lesssim
\frac{4G}{3c^5}
\langle I\rangle_\rho\,\omega_B^4.
}
$$

Thus the same compactness/internal-speed ceiling survives at finite temperature when formulated in terms of the **net absorptive gravitational spectral weight** rather than a bare matrix element.

---

## 6. Why the known $N^2$ collective enhancement does not contradict the bound

Quinones, Oniga, Varcoe, and Wang (Phys. Rev. D 96, 044018, 2017) study correlated two-level bosonic atoms coupled through quadrupole operators to gravitational fluctuations. They identify specially prepared states whose gravitational decay/excitation rates can scale as $N^2$.

Such states need not be passive. For a general stationary but nonpassive population distribution, some pairs satisfy

$$
p_n>p_m
\qquad(E_n>E_m).
$$

Then individual terms in the double-commutator spectral identity can be negative. The positive-frequency absorption strength is no longer bounded by the right-hand side alone because large positive and negative spectral weights can cancel.

Therefore the earlier receiver ceiling must **not** be stated as a universal prohibition of $N^2$ gravitational collective enhancement.

The correct statement is:

> **A passive nonrelativistic receiver has a finite positive quadrupole oscillator-strength budget. Superextensive collective gravitational rates require leaving that passive class or leaving the nonrelativistic Hamiltonian assumptions.**

---

## 7. An activity-budget decomposition

For an arbitrary stationary state define

$$
S_+
=
\sum_{A,m<n:\,p_m\ge p_n}
(p_m-p_n)(E_n-E_m)|Q^A_{mn}|^2,
$$

and

$$
S_-
=
\sum_{A,m<n:\,p_n>p_m}
(p_n-p_m)(E_n-E_m)|Q^A_{mn}|^2.
$$

The exact double-commutator identity becomes

$$
\boxed{
S_+-S_-
=
\frac{10}{3}\hbar^2\langle I\rangle_\rho.
}
$$

Hence

$$
\boxed{
S_+
=
\frac{10}{3}\hbar^2\langle I\rangle_\rho
+S_-.
}
$$

Any positive quadrupole spectral weight beyond the passive ceiling must therefore be accompanied by an **inverted/active spectral budget** $S_-$. This does not yet identify the minimum thermodynamic work required to create the active state, but it makes the resource accounting explicit.

---

## 8. Passive-state phase bound

Let

$$
L_B^2=\frac{\langle I\rangle_\rho}{M},
$$

$$
\mathcal C_B=\frac{r_{s,B}}{L_B},
\qquad
\beta_B=\frac{\omega_BL_B}{c}.
$$

Then the passive net gravitational-response ceiling retains the form

$$
\boxed{
\frac{\kappa_{g,\rm net}}{\omega_B}
\lesssim
\frac23\mathcal C_B\beta_B^3.
}
$$

The exact interpretation is now stronger and cleaner:

- it is not merely a ground-state matrix-element bound;
- it is a bound on the positive dissipative response of any passive stationary nonrelativistic receiver.

---

## 9. Connection to the Gedanken experiment

The receiver question now divides into two strategies.

### Passive quantum memory

The receiver begins near equilibrium and tries to coherently absorb the gravitational branch-difference mode without supplying free energy. It is constrained by the passive quadrupole sum rule.

### Active quantum transducer/amplifier

The receiver is prepared in an excited, inverted, squeezed, or otherwise nonpassive state. Collective rates can exceed the passive ceiling, potentially even with $N^2$ scaling. But then the receiver itself supplies a quantum resource and its added noise/stability must be included in the history-coherence bookkeeping.

This suggests a new question:

> **Can an active gravitational receiver parametrically increase source-receiver entanglement-transfer rate after accounting for the quantum noise and branch records introduced by preparing and maintaining the active state?**

That is the correct way to investigate the $N^2$ loophole.

---

## 10. Relativistic/QFT limitation

The passive sum rule above relies on a finite coordinate quadrupole and a standard nonrelativistic kinetic Hamiltonian. In relativistic quantum field theory, the natural receiver operator is a smeared stress-energy functional. Equal-time stress-tensor commutators can contain contact/Schwinger terms and stress-tensor correlation functions require renormalization.

Therefore there is no justification yet for carrying the simple geometric ceiling

$$
\kappa_g\lesssim GI\omega^4/c^5
$$

unchanged into relativistic QFT.

The relativistic analogue should instead be formulated as a **spectral-response sum rule for a suitably smeared stress tensor**, with renormalization and contact terms treated explicitly.

---

## 11. Novelty discipline

Established ingredients:

- Kubo spectral representations;
- energy-weighted/double-commutator sum rules;
- passive thermal response;
- collective gravitational transitions, including $N^2$ rates in selected correlated atomic states.

The literature search so far has not identified a primary source explicitly combining the passive quadrupole EWSR with the graviton transition formula to state a gravitational quantum-receiver linewidth ceiling. That absence is not proof of novelty.

The corrected candidate contribution is narrower than the earlier claim:

$$
\boxed{
\text{passive quadrupole sum rule}
\Rightarrow
\text{bound on passive gravitational quantum reception}
}
$$

with active collective receivers treated as a separate resource class.

---

## 12. Immediate next step

1. Quantify the active-receiver loophole: relate excess quadrupole spectral weight $S_-$ to a thermodynamic/ergotropy resource and added quantum noise.
2. Develop a relativistic smeared-stress-tensor spectral formulation rather than extrapolating the nonrelativistic bound.
3. Search more deeply for gravitational oscillator-strength bounds in nuclear, atomic, and many-body transition literature before any novelty claim.