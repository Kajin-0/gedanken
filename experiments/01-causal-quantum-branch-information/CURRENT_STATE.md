# Current State — Experiment 01

**Last updated:** 2026-08-07 15:19 EDT  
**Experiment:** Causal Transport of Quantum Branch Information by Gravity

This is the compact canonical recovery point. Detailed derivations are preserved in:

- `README.md`
- `RESEARCH_PROGRESS.md`
- `PROGRESS_LOG.md`
- `SCALAR_MATCHED_HISTORY.md`
- `GRAVITY_QUADRUPOLE_LIMIT.md`
- `TIDAL_RECEIVER.md`
- `EXACT_WEYL_CROSSOVER.md`
- `WAVEZONE_MODE_CHANNEL.md`
- `THERMAL_LOSS_CHANNEL.md`
- `checkpoints/`

---

## 1. Central operational question

Can gravity make a distant quantum receiver distinguish the two branches of a coherently delocalized source **after causal contact** while retaining more recoverable coherence between those histories than any separable/classicalized source-receiver state permits?

For a balanced source-path qubit,

$$
\rho_{AB}=\frac12
\begin{pmatrix}
\rho_L & \Xi\\
\Xi^\dagger & \rho_R
\end{pmatrix}.
$$

Define the history-coherence norm

$$
C_\Xi=\|\Xi\|_1.
$$

For pure conditional global histories,

$$
C_\Xi=F(\rho_E^L,\rho_E^R),
$$

so $C_\Xi$ is the indistinguishability of the **unobserved complementary records**. The paper-level theorem should remain operational in $(\rho_L,\rho_R,\Xi)$ rather than assuming a fundamental factorization of a gravitational-field Hilbert space.

---

## 2. Two separability witnesses

### Trace-distance witness

Define

$$
D_B=\frac12\|\rho_L-\rho_R\|_1.
$$

Every balanced separable state obeys

$$
\boxed{C_\Xi^2+D_B^2\le1.}
$$

Thus

$$
\mathcal W_\Xi=C_\Xi^2+D_B^2-1>0
$$

certifies source-receiver entanglement.

### Stronger fidelity witness

Let

$$
F_B=F(\rho_L,\rho_R)
$$

be root Uhlmann fidelity. A separable-state decomposition plus joint concavity of fidelity gives the stronger bound

$$
\boxed{C_\Xi\le F_B.}
$$

Define

$$
\boxed{
\mathcal M_F=\ln\frac{C_\Xi}{F_B}.
}
$$

Then

$$
\boxed{\mathcal M_F>0}
$$

certifies entanglement. This is now the preferred witness for Gaussian/thermal calculations because displaced thermal-state fidelity is analytic.

The underlying fidelity/coherence mathematics is not claimed as novel; the gravity-specific causal history-transfer application is the research target.

---

## 3. Causality

For a controlled source operation at $t=0$ and receiver separation $R$,

$$
D_B(T,R)=0
\qquad T<R/c
$$

for the source-controlled contribution.

The experiment therefore seeks a **causal nonclassicality front**, not merely a retarded classical force.

---

## 4. Scalar-field matched-history result

For source control history $u$,

$$
\mathcal M_\Xi[u]
=\langle u,(K_B-N_T)u\rangle,
\qquad
K_B=|r_T\rangle\langle r_T|.
$$

If $N_T$ is invertible on the relevant support, an optimized positive-margin history exists iff

$$
\boxed{
\eta_T=\langle r_T,N_T^{-1}r_T\rangle>1.
}
$$

The optimal source history is

$$
\boxed{u_{\rm opt}\propto N_T^{-1}r_T,}
$$

the noise-whitened time reverse of the retarded receiver response.

---

## 5. Clean GR local receiver

A self-contained freely falling receiver must measure **tidal curvature**, not uniform gravitational acceleration. For a differential mode,

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

For harmonic $q$ and $\epsilon=\omega R/c$, the transfer polynomial is

$$
P(\epsilon)=3-3i\epsilon-3\epsilon^2+2i\epsilon^3+\epsilon^4.
$$

This single gauge-invariant curvature response spans static tidal, induction, and radiation zones.

A local receiver faces a severe causal/capture tension: deep near field is highly coherent but retardation is tiny; around $\epsilon\sim1$ retardation is explicit but local capture is fantastically weak.

---

## 6. Wave-zone difference-mode reduction

For branch-dependent coherent gravitational radiation amplitudes $\beta^L_{\mathbf k\lambda}$ and $\beta^R_{\mathbf k\lambda}$, define

$$
N_\Delta
=\sum_\lambda\int d^3k\,
|\beta^L_{\mathbf k\lambda}-\beta^R_{\mathbf k\lambda}|^2.
$$

All $L/R$ distinguishability can be compressed by a passive mode transformation into one normalized bosonic **difference mode**. After removing the common coherent displacement, the two radiation histories differ only by amplitudes

$$
\pm\sqrt{N_\Delta}/2
$$

in that one mode.

For an ideal vacuum receiver capturing fraction $\eta$,

$$
D_B^2=1-e^{-\eta N_\Delta},
$$

$$
C_\Xi^2=e^{-(1-\eta)N_\Delta}.
$$

The simple trace-distance witness becomes positive iff

$$
\boxed{\eta>1/2.}
$$

This $50\%$ threshold is **not** the true entanglement threshold: exact negativity is nonzero for every finite $N_\Delta>0$ and every coherent capture $\eta>0$.

---

## 7. Thermal-loss result — latest major step

Model the capture of the gravitational difference mode as a thermal attenuator with transmissivity $\eta$ and thermal loss-port occupation $\bar n$.

Define

$$
D=1+2(1-\eta)\bar n.
$$

The two receiver states are displaced thermal states with root fidelity

$$
\boxed{
F_B
=\exp\left[-\frac{\eta N_\Delta}{2D}\right].
}
$$

Purifying the thermal port and evaluating the complementary Gaussian fidelity gives

$$
\boxed{
C_\Xi
=\exp\left[
-\frac{(1-\eta)(2\bar n+1)N_\Delta}{2D}
\right].
}
$$

Therefore

$$
\boxed{
\mathcal M_F
=
\frac{N_\Delta}{2D}
\left[
2(\bar n+1)\eta-(2\bar n+1)
\right].
}
$$

The thermal fidelity witness is positive iff

$$
\boxed{
\eta>\eta_c(\bar n)
=\frac{2\bar n+1}{2\bar n+2}.
}
$$

Thus

$$
\bar n=0\Rightarrow\eta_c=1/2,
$$

while

$$
\bar n\to\infty\Rightarrow\eta_c\to1.
$$

Equivalent forms are

$$
\bar n<\frac{2\eta-1}{2(1-\eta)}
$$

and, with output thermal occupancy $\bar n_B=(1-\eta)\bar n$,

$$
\boxed{\bar n_B<\eta-\frac12.}
$$

Interpretation: **thermal uncertainty does not merely shrink the branch signal; it forces the receiver to capture an increasingly complete fraction of the gravitational difference mode before the low-cost history witness can beat separability.**

---

## 8. Thermal matched-memory threshold

For a collective receiver memory

$$
\dot c
=-\frac{\kappa_g+\kappa_i}{2}c
+\sqrt{\kappa_g}\,b_{\rm in}
+\sqrt{\kappa_i}\,\xi_{\rm in},
$$

an optimally shaped input gives

$$
\eta_{\max}=\frac{\kappa_g}{\kappa_g+\kappa_i}.
$$

If the internal bath has mean occupation $\bar n_i$, the thermal fidelity-witness threshold becomes

$$
\boxed{
\kappa_g>(2\bar n_i+1)\kappa_i.
}
$$

Define

$$
\boxed{
\mathcal C_{\rm hist}^{(T)}
=\frac{\kappa_g}{(2\bar n_i+1)\kappa_i}.
}
$$

Then

$$
\boxed{\mathcal C_{\rm hist}^{(T)}>1}
$$

is the matched-memory thermal history-transfer threshold.

This is consistent in spirit with existing spin/interferometer–oscillator analyses: an initially thermal oscillator can still become entangled, while continuous thermal bath contact makes sufficiently high quality factor essential.

---

## 9. Continuous thermal damping

For a branch-driven oscillator with conditional trajectory separation $\Delta\alpha(t)$, damping rate $\kappa$, and bath occupation $\bar n_b$,

$$
F_B(T)
=\exp\left[
-\frac{|\Delta\alpha(T)|^2}{2(2\bar n_B(T)+1)}
\right],
$$

while the bath exports history coherence at rate

$$
\boxed{
\Gamma_{\rm bath}(T)
=\frac{\kappa}{2}(2\bar n_b+1)
\int_0^Tdt\,|\Delta\alpha(t)|^2.
}
$$

Hence

$$
\boxed{
\mathcal M_F(T)
=
\frac{|\Delta\alpha(T)|^2}{2(2\bar n_B(T)+1)}
-
\Gamma_{\rm bath}(T).
}
$$

Initial thermal occupation mainly broadens the receiver and weakens branch resolution; continuous thermal damping additionally creates an uncontrolled branch record and directly spends history coherence.

---

## 10. Novelty discipline

Do not claim novelty for Gaussian-state fidelity, thermal attenuator channels, thermal oscillator decoherence, retarded GIE, quadrupole radiation, or matched-wavepacket capture.

Potentially distinctive physics remains the synthesis

$$
\boxed{
\text{causal gravitational difference mode}
+\text{history-coherence/fidelity witness}
+\text{coherent quantum capture}
+\text{thermal history cooperativity}.
}
$$

---

## 11. Immediate frontier

1. Calculate the **exact source-receiver negativity** for the qubit + thermal-attenuator family.
2. Determine whether finite temperature creates a true minimum capture efficiency for entanglement, or only a minimum efficiency for the fidelity witness.
3. Derive the same thermal channel directly from linearized-gravity input-output theory.
4. Compare the thermal fidelity witness with existing thermal atom/interferometer–oscillator witnesses and entanglement-breaking Gaussian-channel thresholds.
5. Only after that assess whether the thermal history-transfer threshold contains a genuinely new gravity-specific prediction.

## Current Einstein/Feynman compression

> **The gravitational wave can carry the two source alternatives coherently in one difference mode. A cold receiver need only catch more than half of that mode for a simple history-coherence witness to certify nonclassical transfer. A hot or lossy receiver is different: thermal fluctuations hide the branch inside the receiver while the uncontrolled loss channel acquires its own record. The exact Gaussian calculation says that the required coherent capture fraction rises from one half at zero temperature toward unity as the thermal occupation grows. In a matched quantum memory this becomes the simple requirement $\kappa_g>(2\bar n_i+1)\kappa_i$: coherent gravitational capture must beat internal loss multiplied by the thermal noise factor.**