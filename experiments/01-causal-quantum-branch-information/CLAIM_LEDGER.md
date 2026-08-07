# Claim Ledger — Experiment 01

**Timestamp:** 2026-08-07 18:22 EDT  
**Purpose:** Separate established ingredients, internally derived results, model-dependent corollaries, and unresolved novelty claims before constructing a formal paper.

---

## A. Established external ingredients

These should be cited, not presented as new.

### A1. Gravity-mediated entanglement / BMV logic

Established.

### A2. Local/retarded linearized-gravity mediation

Established: linearized quantum gravity can be formulated as a local field mediator and retarded effects have been studied.

### A3. One-delocalized-source + quantum-probe architectures

Established.

### A4. Classical/non-quantized gravity minimum-noise tradeoffs

Established neighboring literature.

### A5. Gaussian-channel entanglement-breaking thresholds

Established.

For the parameterization used here,

$$
\Phi_{\tau,m}\text{ is EB}
\iff
m\ge\tau.
$$

### A6. Two-coherent-state effective-entanglement channel tests

Established.

### A7. Same symmetric hybrid cat through thermal attenuation

Established by Kreis & van Loock (2012), including the exact noisy state and a sufficient moment witness.

### A8. Every non-EB phase-insensitive Gaussian channel can distribute entanglement using some protocol

Established by later capacity/distillation work. Existing constructive protocols use different inputs/operations than the minimal binary coherent probe used here.

### A9. Input-output theory / time-reversed wavepacket loading

Established.

### A10. Quadrupole graviton emission and absorption

Established.

### A11. Planck-area weak bound-state graviton absorption

Established for the specific weak bound-state calculations in the literature.

### A12. Gaussian/unitary canonical reductions and phase-sensitive pre/post processing

Established.

### A13. Entanglement-breaking channels as a quantum-memory free set / channel resource perspective

Established quantum-information idea.

---

## B. Internally derived mathematical results — strong confidence

These have explicit derivations in the repo and currently survive internal audit. Novelty is **not yet established**.

### B1. Exact coherent-dyad matrix element for the chosen channel parameterization

$$
\boxed{
\langle u|
\Phi_{\tau,m}(|\alpha\rangle\langle\beta|)
|v\rangle
=
\frac{\langle\beta|\alpha\rangle\langle u|v\rangle}{m+1}
\exp\left[
\frac{(\sqrt\tau\beta^*-u^*)(v-\sqrt\tau\alpha)}{m+1}
\right].
}
$$

This follows directly from Weyl reconstruction and a Gaussian integral.

File: `DIRECT_GAUSSIAN_BINARY_PROBE_PROOF.md`.

### B2. Binary coherent complete-EB-probe theorem

For every nontrivial finite binary coherent hybrid state

$$
\sqrt p|0\rangle|\alpha\rangle
+e^{i\phi}\sqrt{1-p}|1\rangle|\beta\rangle,
$$

$$
\boxed{
(I\otimes\Phi_{\tau,m})(|\Psi\rangle\langle\Psi|)
\text{ is NPT}
\iff
m<\tau.
}
$$

The direct proof uses one finite $2\times2$ principal minor. The converse uses the established EB criterion.

Pure loss $m=0$ has a separate finite coherent-state test and is included exactly.

Files:

- `PHASE_INSENSITIVE_GAUSSIAN_BINARY_PROBE_THEOREM.md`
- `DIRECT_GAUSSIAN_BINARY_PROBE_PROOF.md`
- `PURE_LOSS_EDGE_CASE.md`

### B3. Exact matched three-element witness

For symmetric branches $|\pm a\rangle$ and $m>0$,

$$
v_*=2\sqrt\tau a/m,
$$

$$
\boxed{
\frac{|z_{v_*}|^2}{p_0p_{v_*}}
=
\exp\left[
\frac{4a^2}{m}(\tau-m)
\right].
}
$$

Thus the witness reaches the exact EB/NPT boundary.

### B4. General separable history-coherence bound

For a balanced source-receiver state

$$
\rho_{AB}=\frac12
\begin{pmatrix}
\rho_L&\Xi\\
\Xi^\dagger&\rho_R
\end{pmatrix},
$$

every separable state satisfies

$$
\boxed{
\|\Xi\|_1^2+
\frac14\|\rho_L-\rho_R\|_1^2
\le1.
}
$$

This is mathematically related to established coherence/distinguishability results and is not being claimed as new.

### B5. Accessible Gaussian cascade criterion

For capture $(\tau_c,m_c)$ followed by readout $(\tau_r,m_r)$,

$$
\tau_{\rm tot}=\tau_c\tau_r,
$$

$$
m_{\rm tot}=\tau_rm_c+m_r,
$$

and therefore

$$
\boxed{
\text{accessible binary output NPT}
\iff
\tau_r(\tau_c-m_c)>m_r.
}
$$

This is straightforward composition plus B2.

---

## C. Internally derived causal/channel results — strong confidence under stated assumptions

### C1. Microcausal replacer theorem

For a controllable local source encoding and a spacelike-separated receiver region,

$$
\boxed{
\mathcal A_{R,t}(\rho)=\sigma_{R,t}\operatorname{Tr}\rho
}
$$

for the source-controlled input-to-receiver channel.

Hence

$$
\boxed{
\mathcal A_{R,t}\in\mathrm{EB}
\qquad t<R/c.
}
$$

This is a direct local-commutativity/no-signalling consequence and does not assert that all spacelike field correlations vanish.

File: `MICROCAUSAL_REPLACER_THEOREM.md`.

### C2. General capability-front definition

$$
\boxed{
T_{\rm cap}(R)
=\inf\{t:\mathcal A_{R,t}\notin\mathrm{EB}\}
\ge R/c.
}
$$

### C3. Front-faithfulness of binary coherent probes for the Gaussian receiver family

Because of B2,

$$
\boxed{
T_{\rm binary}^{\rm NPT}(R)
=T_{\rm cap}(R)
}
$$

whenever $\mathcal A_{R,t}$ remains within the covered phase-insensitive Gaussian family.

This is an interpretation/corollary of B2 + C2.

### C4. Passive Markov receiver front

For a stationary passive one-mode receiver,

$$
\boxed{
T_{\rm cap}^{\min}
=\frac Rc+
\frac1{\kappa_{\rm tot}}
\ln\frac{\kappa_\Delta}
{\kappa_\Delta-\Gamma_{\rm th}}
}
$$

when $\kappa_\Delta>\Gamma_{\rm th}$.

The bound follows from Cauchy-Schwarz optimization over normalized incoming waveforms and is saturated by the time-reversed receiver ringdown.

---

## D. Linearized-gravity calculations — strong but model/convention dependent

### D1. Exact aligned-plus electric-Weyl crossover

$$
\Delta\mathcal E_{xx}
=-\frac{G}{R^5}
\left[
3q+\frac{3R}{c}\dot q+\frac{3R^2}{c^2}\ddot q
+\frac{2R^3}{c^3}q^{(3)}
+\frac{R^4}{c^4}q^{(4)}
\right]_{t-R/c}.
$$

The harmonic polynomial is

$$
P(\epsilon)
=3-3i\epsilon-3\epsilon^2+2i\epsilon^3+\epsilon^4.
$$

The real part/norm is independently consistent with a published vacuum-graviton quadrupole-resonance calculation.

### D2. Receiver quadrupole graviton linewidth

$$
\boxed{
\kappa_g
=\frac{2G\omega^5}{5\hbar c^5}
Q_{ij}^{10}Q_{ij}^{01}.
}
$$

Normalization checked against classical coherent-state quadrupole radiation.

### D3. Normalized retarded source-receiver response

For aligned plus quadrupoles,

$$
\boxed{
\Sigma_{AB}^{R}
=\frac54
\sqrt{\kappa_{g,A}\kappa_{g,B}}
\frac{P(\epsilon)e^{i\epsilon}}{\epsilon^5}.
}
$$

The cross-damping imaginary part is independently reproduced by an angular common-bath integral.

### D4. Delayed storage amplitude

Within the RWA/narrow-band input-output identification,

$$
\boxed{
t_{AB}^{\rm store}
=-i\Sigma_{AB}^{R}/\sqrt{\kappa_{g,A}\kappa_{g,B}}.
}
$$

Far zone:

$$
\boxed{
\eta_{\rm store}
\simeq
\frac{25\mathcal O}{16(kR)^2}.
}
$$

This is a **storage/absorption** coefficient. Do not replace it by the four-times-larger unitary scattering coefficient.

### D5. Branch-mode coherent-state distance

For a compact nonrelativistic source quadrupole,

$$
\boxed{
N_\Delta
=\frac{G}{5\pi\hbar c^5}
\int_0^\infty d\omega\,
\omega^5|\Delta\widetilde Q_{ij}(\omega)|^2.
}
$$

---

## E. Central combined prediction — model specific but current paper spine

For the wave-zone resonant Gaussian receiver,

$$
\kappa_\Delta(R)
=\frac{25\mathcal O}{16(kR)^2}\kappa_g.
$$

The bare capability/NPT front is

$$
\boxed{
T_{\rm cap}(R)
=\frac Rc-
\frac1{\kappa_{\rm tot}}
\ln\left[
1-
\frac{16(kR)^2\Gamma_{\rm th}}
{25\mathcal O\kappa_g}
\right].
}
$$

The finite-certification front is

$$
\boxed{
T_\Lambda^{\min}(R)
=\frac Rc-
\frac1{\kappa_{\rm tot}}
\ln\left[
1-
\frac{16(kR)^2\Gamma_{\rm th}}
{25\mathcal O\kappa_g}
\left(1+\frac{\Lambda_{\rm req}}{N_\Delta}\right)
\right].
}
$$

This is the current central quantitative result of Experiment 01.

File: `MASTER_CAUSAL_FRONT_EQUATION.md`.

---

## F. Receiver feasibility results — model-class bounds, not universal gravity theorems

### F1. Passive nonrelativistic oscillator-strength ceiling

$$
\boxed{
\kappa_g
\le\frac{4G}{3c^5}I\omega^4,
}
$$

or

$$
\boxed{
\kappa_g/\omega
\le\frac23\mathcal C_B\beta_B^3.
}
$$

Applies under passive nonrelativistic particle-coordinate assumptions.

### F2. Vacuum passive wave-zone entanglement ceiling

For weak total capture,

$$
\boxed{
\mathcal N_{\max}^{\rm WZ}
\lesssim
\frac{25\mathcal O}{24\zeta^2}
Q_B\mathcal C_B\beta_B^3.
}
$$

This applies to the passive nonrelativistic resonant receiver class, not arbitrary relativistic/strong-gravity systems.

### F3. Gravitational beta-factor bound

For a normalized incoming source mode,

$$
\boxed{
\kappa_\Delta\le\kappa_g.
}
$$

Arrays may increase total oscillator strength and/or improve directivity, but useful source-mode coupling cannot exceed total gravitational coupling.

---

## G. Interpretive results / strong clues

### G1. Planck-area vs resonant cross section

Weak bound-state graviton absorption results with

$$
\sigma\sim\ell_P^2
$$

are consistent with wavelength-scale peak resonant storage because the same systems have

$$
\Gamma_g/\omega\sim(k\ell_P)^2.
$$

The robust interpretation is a peak-area × fractional-bandwidth tradeoff.

This is a reconciliation, not a claim that the Planck-area literature is wrong.

### G2. Strong self-gravity escape

Black-hole-like quasinormal modes demonstrate that Planck-suppressed fractional gravitational linewidth is not universal. Strong self-gravity can make gravitational coupling/bandwidth large.

### G3. Capture–coherence–accessibility tradeoff

Strong absorption is not sufficient. The complete incoming-mode $\to$ controllable-output channel must remain non-EB.

The Gaussian cascade gives one exact realization; the general EB-resource formulation is broader.

---

## H. Open/conjectural items

### H1. Novelty of B2/B3

Targeted searches have not found the exact binary coherent completeness theorem or matched exact witness, but novelty remains unverified.

### H2. Exact universality of the resonant storage coefficient beyond the stated geometry/RWA

The $25/16$ far-zone aligned-plus coefficient is strongly cross-checked but remains tied to the stated quadrupolar geometry and input-output normalization.

### H3. General non-Gaussian front-faithful probe families

Open.

### H4. Strong-gravity accessible readout channels

Open. Do not assign Gaussian $(\tau,m)$ parameters to black-hole/Hawking readout without an explicit derivation.

### H5. Universal covariant capture–coherence bound

Open. No universal Planck-area or nonrelativistic oscillator-strength ceiling has been established for all relativistic receivers.

---

## I. Claims that have been corrected/superseded

### I1. Universal $\beta^5$ passive wave-zone penalty — **superseded**

The extra $\beta^2$ arose from assuming effective coherent collection area could not exceed literal material area. This is valid only for geometric-aperture-limited absorbers.

Compact resonant receivers can have effective absorption area of order $k^{-2}$.

### I2. $25/[4(kR)^2]$ storage coefficient — **incorrect for storage**

That factor corresponds to the scattering/extinction normalization produced by doubling the self-energy amplitude. The coherent memory storage coefficient is

$$
25/[16(kR)^2].
$$

### I3. “No entanglement before $R/c$” — **too strong**

Spacelike vacuum entanglement/harvesting is possible. The correct causal statement is that the **source-controlled receiver channel is a replacer/EB channel before causal contact**.

---

## J. Paper-level claim hierarchy

The strongest defensible core is presently:

1. direct binary coherent Gaussian-channel theorem;
2. exact finite three-element witness;
3. microcausal source-controlled replacer theorem;
4. general channel-capability front;
5. exact stationary Gaussian receiver front;
6. linearized-gravity difference-mode and delayed storage map;
7. master causal NPT/certification front.

Passive feasibility bounds and strong-gravity receiver discussion should follow as consequences/discussion rather than being mixed into the central proof.