# Current State — Experiment 01

**Last updated:** 2026-08-07 15:28 EDT  
**Experiment:** Causal Transport of Quantum Branch Information by Gravity

Canonical recovery point. Detailed derivations are preserved in:

- `README.md`
- `RESEARCH_PROGRESS.md`
- `PROGRESS_LOG.md`
- `SCALAR_MATCHED_HISTORY.md`
- `GRAVITY_QUADRUPOLE_LIMIT.md`
- `TIDAL_RECEIVER.md`
- `EXACT_WEYL_CROSSOVER.md`
- `WAVEZONE_MODE_CHANNEL.md`
- `THERMAL_LOSS_CHANNEL.md`
- `THERMAL_ENTANGLEMENT_BOUNDARY.md`
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

so $C_\Xi$ measures how indistinguishable the unobserved complementary records remain. Keep the final theory operational in $(\rho_L,\rho_R,\Xi)$; do not assume a fundamental source-field-probe Hilbert-space factorization because gravitational dressing/gauge constraints complicate that split.

---

## 2. Current separability witnesses

### Trace-distance form

$$
D_B=\frac12\|\rho_L-\rho_R\|_1.
$$

Every balanced separable state obeys

$$
\boxed{C_\Xi^2+D_B^2\le1.}
$$

### Stronger fidelity form

Let

$$
F_B=F(\rho_L,\rho_R)
$$

be root Uhlmann fidelity. Every balanced separable state obeys

$$
\boxed{C_\Xi\le F_B.}
$$

Define

$$
\boxed{
\mathcal M_F=\ln(C_\Xi/F_B).
}
$$

Then

$$
\boxed{\mathcal M_F>0}
$$

certifies source-receiver entanglement. The fidelity witness is preferred for Gaussian/thermal calculations because displaced thermal-state fidelity is analytic.

---

## 3. Causality

For a controlled source operation at $t=0$ and receiver distance $R$,

$$
D_B(T,R)=0
\qquad T<R/c
$$

for the source-controlled contribution.

The experiment seeks a **causal nonclassicality front**: the receiver first acquires branch dependence only after causal contact, and then the question is whether the resulting source-receiver state lies outside all separable/classicalized descriptions.

---

## 4. Scalar matched-history result

For source history $u$,

$$
\mathcal M_\Xi[u]
=\langle u,(K_B-N_T)u\rangle,
\qquad
K_B=|r_T\rangle\langle r_T|.
$$

An optimized positive history exists iff

$$
\boxed{
\eta_T=\langle r_T,N_T^{-1}r_T\rangle>1,
}
$$

with optimal waveform

$$
\boxed{u_{\rm opt}\propto N_T^{-1}r_T.}
$$

This is the noise-whitened time reverse of the receiver's retarded response.

---

## 5. Clean GR receiver and exact retarded curvature

The equivalence principle requires a self-contained freely falling receiver to respond to **tidal curvature**, not uniform acceleration:

$$
H_{\rm drive}=\mu_BL_B\mathcal E_{nn}x_B,
\qquad
\mathcal E_{ij}=c^2R_{0i0j}.
$$

For the conserved plus-type source quadrupole

$$
\Delta Q_{xx}=q(t),
\qquad
\Delta Q_{yy}=-q(t),
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

For harmonic $q$ and $\epsilon=\omega R/c$,

$$
P(\epsilon)=3-3i\epsilon-3\epsilon^2+2i\epsilon^3+\epsilon^4.
$$

This single response spans static tidal, induction, and radiation zones. A local receiver faces a severe tradeoff: the deep near field is coherent but retardation is tiny; around $\epsilon\sim1$ retardation is explicit but local gravitational capture is fantastically weak.

---

## 6. Wave-zone difference mode

For branch-dependent coherent gravitational radiation amplitudes $\beta^L_{\mathbf k\lambda}$ and $\beta^R_{\mathbf k\lambda}$, define

$$
N_\Delta
=\sum_\lambda\int d^3k\,
|\beta^L_{\mathbf k\lambda}-\beta^R_{\mathbf k\lambda}|^2.
$$

All branch distinguishability can be compressed into one normalized bosonic **difference mode**. After removing the common coherent displacement, the two radiation histories differ only by amplitudes

$$
\pm\sqrt{N_\Delta}/2.
$$

For vacuum coherent capture fraction $\eta$,

$$
D_B^2=1-e^{-\eta N_\Delta},
$$

$$
C_\Xi^2=e^{-(1-\eta)N_\Delta}.
$$

The simple history witness turns positive iff

$$
\eta>1/2,
$$

but exact source-receiver entanglement is nonzero for every finite $N_\Delta>0$ and every coherent capture $\eta>0$.

---

## 7. Thermal-loss fidelity witness

For a thermal attenuator with transmissivity $\eta$ and environment occupation $\bar n$, define

$$
D=1+2(1-\eta)\bar n.
$$

The conditional receiver-state fidelity is

$$
F_B
=\exp\left[-\frac{\eta N_\Delta}{2D}\right],
$$

while complementary-history coherence is

$$
C_\Xi
=\exp\left[
-\frac{(1-\eta)(2\bar n+1)N_\Delta}{2D}
\right].
$$

Therefore

$$
\boxed{
\mathcal M_F
=\frac{N_\Delta}{2D}
\left[2(\bar n+1)\eta-(2\bar n+1)\right].
}
$$

The low-cost fidelity witness certifies entanglement iff

$$
\boxed{
\eta>\eta_F
=\frac{2\bar n+1}{2\bar n+2}.
}
$$

For a matched receiver memory with gravitational coupling $\kappa_g$, internal loss $\kappa_i$, and thermal occupation $\bar n_i$,

$$
\boxed{
\kappa_g>(2\bar n_i+1)\kappa_i
}
$$

is the fidelity-history threshold.

---

## 8. Latest result: true weak-branch thermal entanglement boundary

Take the source-field wave-zone state

$$
|\Psi\rangle
=\frac{|L\rangle|+a\rangle+|R\rangle|-a\rangle}{\sqrt2},
\qquad
N_\Delta=4|a|^2.
$$

For $|a|\ll1$,

$$
|\Psi\rangle
=|+\rangle|0\rangle+a|-\rangle|1\rangle+O(a^2).
$$

After a thermal attenuator, the partially transposed source-receiver state decomposes into $2\times2$ Fock blocks. Every potentially negative block changes sign at the same condition

$$
\boxed{
\eta>\eta_{\rm ent}
=\frac{\bar n}{\bar n+1}.
}
$$

This is exactly the established entanglement-breaking boundary of the bosonic thermal attenuator.

Thus, in the infinitesimal branch-separation limit, **our specific source-cat / gravitational-difference-mode family becomes entangled immediately when the thermal channel ceases to be entanglement-breaking.**

For $\bar n>0$, the leading negativity is

$$
\boxed{
\mathcal N_{AB}
=\frac{N_\Delta}{4}
\frac{[\eta(\bar n+1)-\bar n][\bar n+1-\eta\bar n]}
{(1-\eta)\bar n[1+(1-\eta)\bar n]}
+O(N_\Delta^2)
}
$$

when $\eta>\bar n/(\bar n+1)$.

The vacuum limit is nonuniform and instead begins as

$$
\mathcal N_{AB}\sim\frac{\sqrt{N_\Delta}}{2}\sqrt\eta.
$$

---

## 9. Three thermal regimes

There are now three sharply distinct regions:

### I. Fundamentally impossible through this thermal channel

$$
\boxed{
\eta\le\frac{\bar n}{\bar n+1}.
}
$$

The channel is entanglement-breaking.

### II. Entanglement transferred but simple history witness fails

$$
\boxed{
\frac{\bar n}{\bar n+1}
<\eta\le
\frac{2\bar n+1}{2\bar n+2}.
}
$$

The weak source-cat state is entangled, but $C_\Xi\le F_B$ is not violated.

### III. Low-cost history certification

$$
\boxed{
\eta>
\frac{2\bar n+1}{2\bar n+2}.
}
$$

The fidelity-history witness certifies the transfer directly.

The two thresholds satisfy

$$
\boxed{
\eta_F=\frac{1+\eta_{\rm ent}}{2}.
}
$$

For the matched memory,

$$
\boxed{
\text{entanglement possible: }\kappa_g>\bar n_i\kappa_i,
}
$$

whereas

$$
\boxed{
\text{simple fidelity witness: }\kappa_g>(2\bar n_i+1)\kappa_i.
}
$$

This hierarchy is currently one of the cleanest results of the project.

---

## 10. Literature boundary

The thermal attenuator and its entanglement-breaking transition are established Gaussian-channel theory. Mari, Zippilli, and Vitali (PRD 113, L021905, 2026) already model a gravity-mediated optical link as a Gaussian thermal attenuator and use its entanglement-breaking transition as a gravity nonclassicality criterion.

Therefore **the channel threshold itself is not novel**.

Potentially distinctive here is the causal wave-zone construction:

$$
\boxed{
\text{source spatial cat}
\rightarrow
\text{retarded gravitational difference mode}
\rightarrow
\text{coherent receiver capture}
}
$$

combined with a direct separation between

1. the fundamental entanglement-transfer boundary;
2. the low-cost history-coherence witness boundary;
3. the causal arrival time of the branch record.

---

## 11. Immediate frontier

1. Solve the finite-$N_\Delta$ thermal problem and determine whether the source-cat family remains entangled throughout the full non-entanglement-breaking region.
2. Optimize $N_\Delta$ at finite temperature for measurable negativity / witness strength.
3. Derive a low-complexity observable witness capable of closing the gap between $\eta_{\rm ent}$ and $\eta_F$.
4. Derive the same thermal channel from explicit linearized-gravity input-output theory rather than a phenomenological attenuator.
5. Compare the resulting causal thresholds against current gravity-mediated quantum-channel proposals before any novelty claim.

## Current Einstein/Feynman compression

> **Thermal noise creates two different limits, and they should not be confused. Below $\eta=\bar n/(\bar n+1)$ the receiver channel is genuinely incapable of carrying entanglement: the gravitational branch information has been classicalized by noise. Above that point, even an arbitrarily weak source cat can transfer some entanglement. But our simple history-coherence test does not see it until the stronger threshold $\eta=(2\bar n+1)/(2\bar n+2)$. Thus the Gedanken experiment now separates three questions cleanly: when can the gravitational signal arrive, when can it carry quantum entanglement at all, and when can that entanglement be certified with a simple operational history test?**