# Current State — Experiment 01

**Last updated:** 2026-08-07 15:40 EDT  
**Experiment:** Causal Transport of Quantum Branch Information by Gravity

This is the compact recovery point. Detailed derivations are in:

- `README.md`
- `RESEARCH_PROGRESS.md`
- `PROGRESS_LOG.md`
- `SCALAR_MATCHED_HISTORY.md`
- `TIDAL_RECEIVER.md`
- `EXACT_WEYL_CROSSOVER.md`
- `WAVEZONE_MODE_CHANNEL.md`
- `THERMAL_LOSS_CHANNEL.md`
- `THERMAL_ENTANGLEMENT_BOUNDARY.md`
- `LOW_COST_PPT_WITNESS.md`
- `CAUSAL_THERMAL_FRONTS.md`
- `INPUT_OUTPUT_THERMAL_FRONTS.md`
- `LINEARIZED_GRAVITY_INPUT_OUTPUT.md`
- `checkpoints/`

---

## 1. Central question

Can gravity transport information about a coherent source alternative to a distant quantum receiver **causally** while preserving enough coherence between the two histories that the source and receiver become entangled?

For a balanced source-path qubit,

$$
\rho_{AB}=\frac12
\begin{pmatrix}
\rho_L & \Xi\\
\Xi^\dagger & \rho_R
\end{pmatrix}.
$$

The key history-coherence quantity is

$$
C_\Xi=\|\Xi\|_1.
$$

For pure conditional global histories,

$$
C_\Xi=F(\rho_E^L,\rho_E^R),
$$

so $C_\Xi$ is the fidelity of the unobserved complementary records. The final theory should be stated operationally in $(\rho_L,\rho_R,\Xi)$ rather than assuming a fundamental factorization of a gravitational-field subsystem.

---

## 2. Operational entanglement tests

Every balanced separable state obeys

$$
\boxed{C_\Xi^2+D_B^2\le1},
\qquad
D_B=\frac12\|\rho_L-\rho_R\|_1.
$$

A stronger fidelity form is

$$
\boxed{C_\Xi\le F_B},
\qquad
F_B=F(\rho_L,\rho_R).
$$

Thus

$$
\boxed{\mathcal M_F=\ln(C_\Xi/F_B)>0}
$$

certifies source-receiver entanglement.

In the weak-cat thermal problem, a more targeted PPT witness reaches the fundamental thermal boundary using only

$$
P_{+,1},\qquad P_{-,0},\qquad Z_0=\langle -,1|\rho|+,0\rangle.
$$

Every PPT state obeys

$$
\boxed{|Z_0|^2\le P_{+,1}P_{-,0}}.
$$

---

## 3. Causality

For a controlled source operation at $t=0$ and receiver distance $R$,

$$
D_B(T,R)=0\qquad T<R/c
$$

for the source-controlled contribution.

The project now distinguishes:

1. **signal front:** first causal source-controlled gravitational response;
2. **NPT front:** first source-receiver entanglement;
3. **global-witness front:** first violation of the simple history/fidelity witness.

---

## 4. Scalar matched-history result

For source control history $u$,

$$
\mathcal M_\Xi[u]=\langle u,(K_B-N_T)u\rangle,
\qquad K_B=|r_T\rangle\langle r_T|.
$$

An optimized positive history exists iff

$$
\boxed{\eta_T=\langle r_T,N_T^{-1}r_T\rangle>1},
$$

with

$$
\boxed{u_{\rm opt}\propto N_T^{-1}r_T}.
$$

The optimal history is the noise-whitened time reverse of the receiver's retarded response.

---

## 5. Gauge-invariant GR response

A self-contained free receiver measures tidal curvature, not uniform acceleration:

$$
H_{\rm drive}=\mu_BL_B\mathcal E_{nn}x_B,
\qquad
\mathcal E_{ij}=c^2R_{0i0j}.
$$

For the conserved plus-type branch quadrupole

$$
\Delta Q_{xx}=q(t),\qquad \Delta Q_{yy}=-q(t),
$$

with receiver on the $z$ axis,

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

For harmonic motion and $\epsilon=\omega R/c$,

$$
P(\epsilon)=3-3i\epsilon-3\epsilon^2+2i\epsilon^3+\epsilon^4.
$$

This one retarded curvature transfer function spans static tidal, induction, and radiation zones.

---

## 6. Wave-zone difference mode

For branch-dependent coherent graviton amplitudes,

$$
N_\Delta
=\sum_\lambda\int d^3k\,
|\beta^L_{\mathbf k\lambda}-\beta^R_{\mathbf k\lambda}|^2.
$$

All $L/R$ distinguishability can be compressed into one normalized bosonic **difference mode** with branch amplitudes

$$
\pm\sqrt{N_\Delta}/2.
$$

Thus the wave-zone problem reduces to coherent state transfer through one effective gravitational bosonic channel.

---

## 7. Thermal channel hierarchy

For a thermal attenuator of transmissivity $\eta$ and bath occupation $\bar n$:

### Fundamental weak-cat entanglement boundary

$$
\boxed{\eta_{\rm ent}=\frac{\bar n}{\bar n+1}}.
$$

### Global fidelity-history threshold

$$
\boxed{\eta_F=\frac{2\bar n+1}{2\bar n+2}}
$$

with

$$
\eta_F=\frac{1+\eta_{\rm ent}}{2}.
$$

The targeted $0/1$-sector PPT witness reaches $\eta_{\rm ent}$ in the weak-cat limit, so the fundamental boundary is operationally accessible without full tomography.

---

## 8. Explicit receiver input-output dynamics — latest dynamical result

For causal arrival time

$$
t_0=R/c,
$$

the matched quantum receiver obeys

$$
\boxed{
\dot c
=-\frac{\kappa}{2}c
+\sqrt{\kappa_g}\,b_{\rm in}
+\sqrt{\kappa_i}\,\xi_{\rm in},
\qquad
\kappa=\kappa_g+\kappa_i.
}
$$

For a fixed normalized gravitational difference-mode envelope $f$,

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

The branch-independent receiver thermal occupation is

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

The weak-cat conditions are therefore simply

$$
\boxed{\text{NPT entanglement: }\eta_f(t)>m(t)},
$$

$$
\boxed{\text{global fidelity witness: }\eta_f(t)>m(t)+\frac12}.
$$

For the minimal PPT witness,

$$
|Z_0|^2-P_{+,1}P_{-,0}
=
\frac{|a|^2}{[1+m(t)]^3}
[\eta_f(t)-m(t)]
+O(|a|^4).
$$

Thus the measured PPT crossing occurs exactly at $\eta_f=m$.

---

## 9. Stationary thermal receiver: exact front times

If the receiver is thermally equilibrated before the gravitational wave arrives,

$$
m_*=\frac{\kappa_i\bar n_i}{\kappa}.
$$

The maximum coherent transfer available by time $\tau$ is

$$
\eta_{\max}(\tau)
=\frac{\kappa_g}{\kappa}(1-e^{-\kappa\tau}).
$$

The NPT front exists iff

$$
\boxed{\kappa_g>\bar n_i\kappa_i},
$$

and then

$$
\boxed{
T_{\rm NPT}^{\rm opt}(R)
=\frac Rc+
\frac1\kappa
\ln\left(
\frac{\kappa_g}
{\kappa_g-\bar n_i\kappa_i}
\right).
}
$$

The global fidelity front exists iff

$$
\boxed{\kappa_g>(2\bar n_i+1)\kappa_i},
$$

and then

$$
\boxed{
T_F^{\rm opt}(R)
=\frac Rc+
\frac1\kappa
\ln\left[
\frac{2\kappa_g}
{\kappa_g-(2\bar n_i+1)\kappa_i}
\right].
}
$$

Near the fundamental threshold

$$
\delta=\kappa_g-\bar n_i\kappa_i\to0^+,
$$

$$
\boxed{
T_{\rm NPT}^{\rm opt}-R/c
\sim\kappa^{-1}\ln(\kappa_g/\delta).
}
$$

This is **critical slowing of the causal entanglement front**.

Important correction: a finite thermal post-light-cone delay is not universal. If the receiver is freshly ground-state prepared at causal arrival, signal and bath noise initially grow with the same exponential factor; then the weak-cat state is either NPT immediately after arrival when $\kappa_g>\bar n_i\kappa_i$, or never in the ideal matched model. The finite delay above is produced by a pre-existing thermal floor.

---

## 10. Linearized-gravity value of the receiver coupling

The phenomenological rate $\kappa_g$ is the receiver's **spontaneous graviton-emission linewidth**.

For a trace-free quadrupole transition $|1\rangle\to|0\rangle$,

$$
\boxed{
\kappa_g
=\frac{2G\omega_B^5}{5\hbar c^5}
Q_{ij}^{10}Q_{ij}^{01}.
}
$$

This follows from the standard gauge-invariant quadrupole graviton-emission rate. By time-reversal reciprocity, the same matrix element controls absorption of the matched incoming graviton mode.

For a harmonic quadrupole

$$
Q_{ij}=\Lambda_B e_{ij}x_B,
$$

$$
\boxed{
\kappa_g
=\frac{G\Lambda_B^2\omega_B^4}{5\mu_Bc^5}
(e_{ij}e_{ij}).
}
$$

For $e_{ij}=\operatorname{diag}(1,-1,0)$,

$$
\kappa_g
=\frac{2G\Lambda_B^2\omega_B^4}{5\mu_Bc^5}.
$$

For an explicit cylindrical bar geometry, use the exact resonator result rather than this abstract normalization. Tobar et al. derive

$$
\boxed{
\kappa_g=\Gamma_{\rm spon}
=\frac{8GML^2\omega_l^4}{l^4\pi^4c^5}
}
$$

for odd longitudinal mode $l$.

Thus the causal front is controlled by exactly the same tiny rate that determines how slowly the receiver would spontaneously radiate a graviton if excited.

---

## 11. Fully gravitational thermal criterion

The weak-cat matched-receiver entanglement condition is

$$
\boxed{
\frac{2G\omega_B^5}{5\hbar c^5}
Q_{ij}^{10}Q_{ij}^{01}
>
\bar n_i\kappa_i.
}
$$

If

$$
\kappa_i=\omega_B/Q_i,
$$

then

$$
\boxed{
Q_i
>
\frac{5\hbar c^5\bar n_i}
{2G\omega_B^4Q_{ij}^{10}Q_{ij}^{01}}.
}
$$

At high temperature,

$$
\bar n_i\simeq\frac{k_BT}{\hbar\omega_B},
$$

so equivalently

$$
\boxed{
Q_i>\frac{k_BT}{\hbar\kappa_g}.
}
$$

The simple global fidelity witness needs approximately twice this thermal cooperativity in the high-temperature regime.

---

## 12. Novelty discipline

Established ingredients include quadrupolar graviton emission/absorption, Gaussian thermal attenuators, entanglement-breaking thresholds, input-output theory, matched pulse capture, PPT witnesses, retarded GIE, and gravitational-wave curvature coupling.

Potentially distinctive physics remains the synthesis:

$$
\boxed{
\text{source spatial cat}
\rightarrow
\text{retarded gravitational difference mode}
\rightarrow
\text{mode-matched quantum receiver}
}
$$

with separate and calculable signal, NPT, and low-cost-certification fronts.

---

## 13. Immediate frontier

1. Numerically evaluate the gravitational cooperativity/front time for representative receiver families and identify favorable scalings.
2. Determine whether the finite-$N_\Delta$ source-cat family remains entangled throughout the full non-entanglement-breaking thermal region.
3. Derive the receiver coupling and angular-mode matching directly from a full spherical graviton input-output basis.
4. Compare the causal-front construction against the latest gravity-mediated quantum communication literature before any novelty claim.

## Current Einstein/Feynman compression

> **The receiver's ability to catch quantum gravitational branch information is governed by the same matrix element that tells us how slowly it would radiate a graviton if we excited it. Turn spontaneous graviton emission around in time and one obtains the matched absorption process. The light cone fixes when that process can begin; the graviton linewidth fixes how fast it can proceed; thermal loss determines whether the captured information remains quantum. Near the thermal boundary the classical gravitational signal can arrive on time while the entanglement front falls arbitrarily far behind it.**