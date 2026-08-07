# Current State — Experiment 01

**Last updated:** 2026-08-07 15:32 EDT  
**Experiment:** Causal Transport of Quantum Branch Information by Gravity

Canonical recovery point. Detailed derivations are preserved in:

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
- `checkpoints/`

---

## 1. Core operational state

For a balanced source-path qubit,

$$
\rho_{AB}=\frac12
\begin{pmatrix}
\rho_L & \Xi\\
\Xi^\dagger & \rho_R
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

so $C_\Xi$ measures how indistinguishable the unobserved complementary records remain. Keep the final theory operational in $(\rho_L,\rho_R,\Xi)$ rather than assuming a fundamental source-field-probe factorization.

---

## 2. Separability witnesses

Trace-distance form:

$$
D_B=\frac12\|\rho_L-\rho_R\|_1,
$$

$$
\boxed{C_\Xi^2+D_B^2\le1}
$$

for every balanced separable state.

Stronger fidelity form:

$$
F_B=F(\rho_L,\rho_R),
$$

$$
\boxed{C_\Xi\le F_B}.
$$

Define

$$
\boxed{\mathcal M_F=\ln(C_\Xi/F_B)}.
$$

Then $\mathcal M_F>0$ certifies source-receiver entanglement.

---

## 3. Causality

For a controlled source operation at $t=0$ and receiver distance $R$,

$$
D_B(T,R)=0\qquad T<R/c
$$

for the source-controlled contribution.

The project now distinguishes three fronts:

1. classical/source-controlled signal arrival;
2. source-receiver NPT entanglement arrival;
3. low-cost global history-witness certification.

---

## 4. Scalar matched-history optimization

For source control history $u$,

$$
\mathcal M_\Xi[u]=\langle u,(K_B-N_T)u\rangle,
\qquad K_B=|r_T\rangle\langle r_T|.
$$

A positive optimized history exists iff

$$
\boxed{\eta_T=\langle r_T,N_T^{-1}r_T\rangle>1},
$$

with

$$
\boxed{u_{\rm opt}\propto N_T^{-1}r_T}.
$$

Interpretation: the optimal source history is the noise-whitened time reverse of the retarded receiver response.

---

## 5. Gauge-invariant GR receiver

A self-contained freely falling receiver responds to tidal curvature, not uniform acceleration:

$$
H_{\rm drive}=\mu_BL_B\mathcal E_{nn}x_B,
\qquad \mathcal E_{ij}=c^2R_{0i0j}.
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

This one retarded curvature response spans static tidal, induction, and wave zones.

---

## 6. Wave-zone gravitational difference mode

For branch-dependent coherent radiation amplitudes $\beta^L_{\mathbf k\lambda}$ and $\beta^R_{\mathbf k\lambda}$,

$$
N_\Delta=\sum_\lambda\int d^3k\,|\beta^L_{\mathbf k\lambda}-\beta^R_{\mathbf k\lambda}|^2.
$$

All branch distinguishability can be compressed into one normalized bosonic difference mode. After removing the branch-common displacement, the two field histories differ only by

$$
\pm\sqrt{N_\Delta}/2.
$$

In vacuum, coherent receiver capture fraction $\eta$ gives

$$
D_B^2=1-e^{-\eta N_\Delta},
\qquad
C_\Xi^2=e^{-(1-\eta)N_\Delta}.
$$

The simple global history witness requires $\eta>1/2$, but exact source-receiver entanglement exists for every finite $N_\Delta>0$ and every $\eta>0$.

---

## 7. Thermal channel thresholds

For a thermal attenuator with transmissivity $\eta$ and bath occupation $\bar n$, the true weak-branch entanglement boundary is

$$
\boxed{\eta_{\rm ent}=\frac{\bar n}{\bar n+1}}.
$$

This is the established entanglement-breaking boundary of the thermal attenuator.

The simpler fidelity-history witness requires

$$
\boxed{\eta_F=\frac{2\bar n+1}{2\bar n+2}}
$$

with

$$
\boxed{\eta_F=\frac{1+\eta_{\rm ent}}{2}}.
$$

For the matched receiver memory

$$
\eta=\frac{\kappa_g}{\kappa_g+\kappa_i},
$$

these become

$$
\boxed{\text{entanglement possible: }\kappa_g>\bar n_i\kappa_i},
$$

$$
\boxed{\text{global fidelity witness: }\kappa_g>(2\bar n_i+1)\kappa_i}.
$$

---

## 8. Minimal PPT witness reaches the fundamental thermal boundary

In the weak-cat limit use the source basis

$$
|\pm\rangle=(|L\rangle\pm|R\rangle)/\sqrt2.
$$

Measure

$$
P_{+,1}=\langle +,1|\rho|+,1\rangle,
$$

$$
P_{-,0}=\langle -,0|\rho|-,0\rangle,
$$

and

$$
Z_0=\langle -,1|\rho|+,0\rangle.
$$

Every PPT state obeys

$$
\boxed{|Z_0|^2\le P_{+,1}P_{-,0}}.
$$

Therefore

$$
\boxed{|Z_0|^2>P_{+,1}P_{-,0}}
$$

certifies NPT entanglement using only two populations and one complex joint coherence.

For the thermal attenuator this witness turns on exactly at

$$
\boxed{\eta>\bar n/(\bar n+1)}
$$

in the weak-cat limit. Thus the gap between the fundamental thermal boundary and the global fidelity witness can be closed operationally without full tomography.

A linear witness family is

$$
W_0(\lambda,\theta)
=\lambda P_{+,1}+\lambda^{-1}P_{-,0}
-2\operatorname{Re}(e^{-i\theta}Z_0)\ge0
$$

for PPT states.

---

## 9. Causal thermal fronts — latest result

Let the normalized gravitational difference-mode wavepacket envelope be $f(t)$ and let the eventual coherent capture efficiency be $\eta_\infty$. Define

$$
F(s)=\int_{-\infty}^{s}dt\,|f(t)|^2,
$$

and

$$
\boxed{\eta(T,R)=\eta_\infty F(T-R/c)}.
$$

Then the classical signal front is

$$
\boxed{T_c=R/c}.
$$

If $\eta_\infty>\eta_{\rm ent}$, the weak-cat NPT front is

$$
\boxed{
T_{\rm NPT}(R)
=\frac{R}{c}
+F^{-1}\!\left(\frac{\eta_{\rm ent}}{\eta_\infty}\right).
}
$$

If $\eta_\infty>\eta_F$, the global fidelity-history front is

$$
\boxed{
T_F(R)
=\frac{R}{c}
+F^{-1}\!\left(\frac{\eta_F}{\eta_\infty}\right).
}
$$

Whenever all exist,

$$
\boxed{T_c\le T_{\rm NPT}<T_F}.
$$

At zero temperature, $\eta_{\rm ent}=0$, so entanglement begins with the first nonzero coherent capture after causal arrival. At finite temperature, the receiver must accumulate a finite portion of the gravitational difference mode before entanglement can survive thermal classicalization.

For a causal exponential wavepacket

$$
f(s)=\sqrt\gamma e^{-\gamma s/2}\Theta(s),
$$

$$
T_{\rm NPT}
=\frac{R}{c}
-\frac1\gamma\ln\left(1-\frac{\eta_{\rm ent}}{\eta_\infty}\right).
$$

As $\eta_\infty\to\eta_{\rm ent}^+$, the post-light-cone entanglement delay diverges logarithmically.

---

## 10. Novelty discipline

Do not claim novelty for the thermal attenuator entanglement-breaking threshold, Gaussian fidelity, PPT principal-minor witnesses, matched wavepacket capture, retarded GIE, or quadrupole radiation.

Potentially distinctive physics remains the gravity-specific synthesis

$$
\boxed{
\text{source spatial cat}
\to
\text{retarded gravitational difference mode}
\to
\text{coherent quantum receiver}
}
$$

with explicit separation of

1. causal signal arrival;
2. entanglement-transfer onset;
3. operational certification onset.

---

## 11. Immediate frontier

1. Derive $\eta(T)$, thermal receiver occupation, and $Z_0(T)$ directly from the matched receiver's Markovian input-output equations rather than inserting a phenomenological capture fraction.
2. Determine the exact critical slowing of $T_{\rm NPT}$ near $\kappa_g=\bar n_i\kappa_i$.
3. Solve or tightly characterize the finite-$N_\Delta$ thermal source-cat problem.
4. Derive the same receiver dynamics from explicit linearized-gravity input-output theory.
5. Continue dedicated novelty checks before treating the causal-front synthesis as publication-level novelty.

## Current Einstein/Feynman compression

> **The light cone answers only the first question: when can gravity begin to affect the receiver? Thermal noise creates a second threshold. A receiver can already see a causal gravitational signal while the channel is still too noisy to preserve entanglement. Only after enough of the branch-dependent gravitational mode has been coherently captured does a source-receiver quantum correlation survive. A targeted three-observable PPT test can detect that transition exactly in the weak-cat limit. The Gedanken experiment therefore separates three distinct events in spacetime: gravitational influence arrives, gravitational entanglement arrives, and a simple global history witness finally becomes strong enough to certify it.**