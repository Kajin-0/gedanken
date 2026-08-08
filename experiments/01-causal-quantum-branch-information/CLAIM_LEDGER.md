# Claim Ledger — Experiment 01

**Updated:** 2026-08-07 20:04 EDT  
**Purpose:** Separate established prior art, internally derived mathematics, model-specific gravitational results, corrected claims, and remaining novelty candidates.

---

## A. Established prior art — do not claim

### A1. Gravity-mediated entanglement

Established by the BMV literature and later work.

### A2. Locally mediated / retarded gravity-generated entanglement

Christodoulou et al. (2023) derive entanglement using local linearized quantum gravity and explicitly discuss light-crossing retardation.

### A3. Gravity as a quantum-information channel

Mari–Zippilli–Vitali (2026) explicitly ask whether gravity can mediate quantum information and characterize a gravity-induced thermal-attenuator channel through its entanglement-breaking boundary.

### A4. Coherent-state gravity channel benchmarks

Lami–Pedernales–Plenio (2024), Toccacelo–Andersen–Brask (2025), Mari et al. (2026), and related work already use coherent states / channel benchmarks in gravitational settings.

### A5. Noisy gravitational state transfer and thermal thresholds

Toccacelo–Andersen–Brask (2025) study noisy Newtonian oscillator communication. Miki–Li–Chen (2026) derive entanglement-generation and entanglement-breaking thresholds for thermally damped gravitational oscillator dynamics.

### A6. Quantized passing GW mode coupled to a quantum detector

Toccacelo–Beitel–Andersen–Pikovski (2026) model a quantized incident gravitational-wave mode swapping quantum state with a resonant acoustic detector and include thermal open-system dynamics.

### A7. Relativistic sender→receiver quantum-channel causality

Cliche–Kempf already show that a spacelike-separated receiver cannot depend on a localized sender input, while vacuum correlations can still generate detector entanglement.

### A8. Gaussian-channel EB boundaries

Established.

For the convention used here,

$$
\Phi_{\tau,m}\text{ is EB}
\iff
m\ge\tau.
$$

### A9. Two-coherent-state effective-entanglement tests

Established by Häseler–Moroder–Lütkenhaus and subsequent quantum-device benchmark work.

### A10. Same hybrid coherent/qubit state under thermal attenuation

Kreis–van Loock (2012) study the same symmetric hybrid input under a thermal beam-splitter channel and construct a sufficient moment witness.

### A11. Nonclassicality-breaking / EB relations for Gaussian channels

Ivan–Sabapathy–Simon (2013) establish an essential equivalence between nonclassicality-breaking and entanglement-breaking Gaussian channels. This is not the same statement as the binary-hybrid NPT theorem below.

---

## B. Strongest internally derived mathematical result — novelty unverified

### B1. Exact coherent-dyad matrix element

For the one-mode gauge-covariant phase-insensitive Gaussian channel,

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

This follows directly from the characteristic function and one complex Gaussian integral.

### B2. Binary coherent exact NPT/EB equivalence

For every finite nontrivial

$$
|\Psi\rangle
=\sqrt p|0\rangle|\alpha\rangle
+e^{i\phi}\sqrt{1-p}|1\rangle|\beta\rangle,
$$

with $0<p<1$ and $\alpha\neq\beta$,

$$
\boxed{
(I\otimes\Phi_{\tau,m})(|\Psi\rangle\langle\Psi|)
\text{ is NPT}
\iff
\tau>m.
}
$$

Since $\tau>m$ is exactly the channel non-EB region, every nontrivial finite binary coherent hybrid input detects the EB transition.

A direct proof uses one finite $2\times2$ principal minor. Pure loss $m=0$ has a separate finite coherent-state witness and is included exactly.

**Novelty status:** targeted searches have not found an equivalent theorem, but absence is not established.

Files:

- `DIRECT_GAUSSIAN_BINARY_PROBE_PROOF.md`
- `PURE_LOSS_EDGE_CASE.md`

### B3. Exact three-element boundary witness

For symmetric $|\pm a\rangle$ and $m>0$,

$$
\boxed{
v_*=\frac{2\sqrt\tau a}{m},
}
$$

and

$$
\boxed{
\frac{|z_{v_*}|^2}{p_0p_{v_*}}
=\exp\left[
\frac{4a^2}{m}(\tau-m)
\right].
}
$$

Thus one $2\times2$ partial-transpose principal minor reaches the exact EB boundary.

**Novelty status:** promising but unverified.

---

## C. Absolute finite-strength witness — internally derived

For

$$
M_v=
\begin{pmatrix}
p_0&z_v^*\\
z_v&p_v
\end{pmatrix}
$$

inside the partial transpose, define

$$
\boxed{
G(v)
=\frac12
\max\left\{
0,
\sqrt{(p_0-p_v)^2+4|z_v|^2}
-(p_0+p_v)
\right\}.
}
$$

Then

$$
\boxed{
\mathcal N(\rho)\ge G(v).
}
$$

This is an absolute negativity lower bound, unlike the normalized ratio $\Lambda$.

### Weak-link asymptotic

For $\tau,m\ll1$ with fixed $m/\tau<1$, optimizing the source coherent separation and analysis displacement gives

$$
\boxed{
G_{\rm abs}^{\rm opt}
=\frac12W(e^{-1})(\tau-m)+O(\tau^2).
}
$$

Numerically,

$$
\boxed{
\frac12W(e^{-1})
\simeq0.1392323.
}
$$

The corresponding leading optimal source coherent amplitude is

$$
\boxed{
a_*
\simeq0.565346\sqrt\tau.
}
$$

File: `WEAK_LINK_ABSOLUTE_GAP_ASYMPTOTIC.md`.

---

## D. Correct general receiver statement

A physical source emits one fixed normalized temporal waveform $f$.

For a Markov receiver,

$$
\boxed{
\tau_f(t)
=\kappa_\Delta
\left|
\int_0^t ds\,
e^{-\kappa(t-s)/2}f(s)
\right|^2,
}
$$

and

$$
\boxed{
m(t)
=n_0e^{-\kappa t}
+\frac{\Gamma_{\rm th}}{\kappa}
(1-e^{-\kappa t}).
}
$$

Therefore

$$
\boxed{
\text{receiver channel non-EB}
\iff
\tau_f(t)>m(t).
}
$$

For the binary coherent hybrid input, this is simultaneously the exact NPT condition.

Restoring propagation,

$$
\boxed{
T_{\rm cap}(R;f)
=\frac Rc+
\inf\{t>0:\tau_f(t)>m(t)\}.
}
$$

This is now the **general receiver equation** within the one-mode Gaussian Markov model.

File: `GENERAL_FIXED_WAVEFORM_RECEIVER_FRONT.md`.

---

## E. Corrected status of the logarithmic front

The earlier logarithmic formula is **not universal**.

It assumes

1. stationary thermal initial receiver
   $$
   n_0=\Gamma_{\rm th}/\kappa;
   $$
2. target-time-specific temporal-mode optimization.

Under those assumptions,

$$
\boxed{
T_{\rm cap}^{\rm env}
=\frac Rc+
\frac1\kappa
\ln\frac{\kappa_\Delta}
{\kappa_\Delta-\Gamma_{\rm th}}.
}
$$

It is now a best-case **optimized envelope**, not the paper's master physical front.

File: `MASTER_CAUSAL_FRONT_EQUATION.md` with corrected scope.

---

## F. Gravity-specific field calculations — strong but convention/model dependent

### F1. Branch coherent-mode distance

For a conserved nonrelativistic quadrupole branch difference,

$$
\boxed{
N_\Delta
=\frac{G}{5\pi\hbar c^5}
\int_0^\infty d\omega\,
\omega^5
|\Delta\widetilde Q_{ij}(\omega)|^2.
}
$$

### F2. Receiver graviton linewidth

$$
\boxed{
\kappa_g
=\frac{2G\omega^5}{5\hbar c^5}
Q_{ij}^{10}Q_{ij}^{01}.
}
$$

### F3. Aligned-plus retarded cross response

$$
\boxed{
\Sigma_{AB}^{R}
=\frac54
\sqrt{\kappa_{g,A}\kappa_{g,B}}
\frac{P(\epsilon)e^{i\epsilon}}{\epsilon^5},
}
$$

where

$$
P(\epsilon)
=3-3i\epsilon-3\epsilon^2+2i\epsilon^3+\epsilon^4.
$$

### F4. Source-output→receiver-input storage coefficient

$$
\boxed{
t_{AB}^{\rm store}
=-i\Sigma_{AB}^{R}/\sqrt{\kappa_{g,A}\kappa_{g,B}}.
}
$$

Wave zone:

$$
\boxed{
\eta_{\rm store}
\simeq
\frac{25\mathcal O}{16(kR)^2}.
}
$$

The factor $25/16$ is the **storage/absorption** normalization; the four-times-larger value belongs to scattering/extinction bookkeeping.

**Remaining audit:** desirable to rederive in a second fully explicit field convention.

---

## G. Explicit conserved-source benchmark

A four-mass cross with branch-dependent radii

$$
X_s^2=L^2+s\,d(t),
$$

$$
Y_s^2=L^2-s\,d(t)
$$

has zero center-of-mass motion and exact branch difference

$$
\boxed{
\Delta Q_{xx}=4\mu d(t),
\qquad
\Delta Q_{yy}=-4\mu d(t),
\qquad
\Delta Q_{zz}=0.
}
$$

Using

$$
d(t)\propto
\sin^4(\pi t/T)\cos\omega t
$$

makes the compact quadrupole pulse sufficiently smooth for finite $N_\Delta$.

The small-deformation plus normal mode has

$$
M_{\rm eff}=4\mu,
$$

$$
u_{\rm zpf}=\sqrt{\hbar/(8\mu\omega)},
$$

and

$$
\boxed{
\kappa_g
=\frac{8G\mu L^2\omega^4}{5c^5}.
}
$$

A state-dependent internal force can create the coherent mechanical cat and return the mechanical mode to the origin after the pulse.

Files:

- `CONSERVED_FOUR_MASS_QUADRUPOLE_SOURCE.md`
- `QUANTIZED_PLUS_MODE_SOURCE.md`

---

## H. Source-specific quantum-capability bubble

For the normalized narrowband $\sin^4$ graviton mode,

$$
f_4(t)
=\sqrt{128/(35T)}\sin^4(\pi t/T),
$$

define

$$
S_{4,q}(x)
=\frac{128q}{35}e^{-qx}J_{4,q}^2[\min(x,1)],
$$

$$
N_q(x)=1-e^{-qx}.
$$

Then

$$
\boxed{
\tau_4
=\frac{\kappa_\Delta}{\kappa}S_{4,q}(x),
}
$$

$$
\boxed{
m
=\frac{\Gamma_{\rm th}}{\kappa}N_q(x).
}
$$

The channel is non-EB iff

$$
\boxed{
\frac{\kappa_\Delta}{\Gamma_{\rm th}}
\frac{S_{4,q}(x)}{N_q(x)}>1.
}
$$

Optimizing $q$ and $x$ gives

$$
\boxed{
H_{4,*}\simeq0.8136763,
}
$$

so the pulse can produce a non-EB window only if

$$
\boxed{
\kappa_\Delta>1.22899\,\Gamma_{\rm th}.
}
$$

The two time boundaries form a finite EB $\to$ non-EB $\to$ EB spacetime bubble.

File: `SIN4_MECHANICAL_SOURCE_QUANTUM_WINDOW.md`.

---

## I. Explicit source-to-receiver link

For the same four-mass plus mode as receiver, total endpoint mass $M=4\mu$:

$$
\boxed{
\kappa_\Delta(R)
=\frac{5\mathcal O}{8}
\frac{GM L^2\omega^2}
{c^3R^2}.
}
$$

At $kR=\zeta$ and with ordinary linewidth $\kappa\simeq\omega/Q$,

$$
\boxed{
\frac{\kappa_\Delta}{\kappa}
=\frac{5\mathcal O}{16\zeta^2}
Q\mathcal C\beta^3,
}
$$

where

$$
\mathcal C=2GM/(c^2L),
$$

$$
\beta=\omega L/c.
$$

For the optimized $\sin^4$ pulse in vacuum,

$$
\boxed{
\mathcal N_{\max}^{\rm WZ}
\simeq
0.249382
\frac{\mathcal O}{\zeta^2}
Q\mathcal C\beta^3
}
$$

in the weak-capture limit.

The minimal three-element absolute witness reaches

$$
\boxed{
G_{\rm abs,max}^{\rm WZ}
\simeq
0.0347220
\frac{\mathcal O}{\zeta^2}
Q\mathcal C\beta^3.
}
$$

File: `EXPLICIT_FOUR_MASS_SOURCE_RECEIVER_LINK.md`.

---

## J. Information-flow result: stronger source is not always better

For pure-loss capture fraction $\eta\ll1$, exact binary-cat negativity is optimized at

$$
\boxed{
N_\Delta^{\rm opt}
\simeq4\sqrt\eta.
}
$$

Thus an arbitrarily strong emitted branch record is counterproductive when one tiny receiver captures only a small fraction of the outgoing field. The uncollected gravitational modes become a which-branch environment.

This is an important physical consequence of the exact pure-loss state, not a claim that weak sources are universally optimal for every protocol.

---

## K. Corrected / superseded claims

### K1. Universal logarithmic quantum cone — superseded

Only a stationary target-time-optimized envelope.

### K2. Universal $\beta^5$ receiver penalty — superseded

Only geometric-aperture-limited absorbers. Compact resonant absorbers can have wavelength-scale effective cross sections.

### K3. $25/[4(kR)^2]$ state-storage coefficient — incorrect

That is scattering/extinction normalization. State storage uses $25/[16(kR)^2]$.

### K4. “No source-receiver entanglement before $R/c$” — too strong

The correct causal statement concerns **source-controlled communication/input dependence**, not all background/vacuum entanglement.

### K5. $\sin^2$ compact quadrupole as literal mechanical source — insufficiently smooth

A hard $\sin^2$ quadrupole pulse has endpoint derivative structure that is not UV safe for the ideal $\omega^5|\widetilde Q|^2$ coherent-graviton norm. Use $\sin^4$ or a smoother envelope for an explicit compact mechanical source.

---

## L. Remaining novelty candidates

### L1. Exact binary coherent NPT/EB theorem

Strongest mathematical candidate.

### L2. Exact minimal principal-minor witness saturating the Gaussian EB boundary

Strongest operational quantum-information candidate.

### L3. Source-resolved retarded full gravitational link

A controlled quantum branch source is mapped into an emitted coherent graviton difference mode, propagated over explicit distance, and captured by a noisy quantum receiver in one normalized calculation.

### L4. Source-specific spacetime quantum-capability / finite-certification bubble

Unlike prior work that starts from a Newtonian pair or an already-incident GW mode, the current construction derives the temporal receiver channel from a specified source-side coherent quadrupole history.

**Novelty status for L3/L4:** promising synthesis; targeted searches have not located the same full construction, but no originality claim is yet justified.

---

## M. Strongest next audit

1. Broader citation-forward search for L1/L2.
2. Independent field-normalization derivation of $25/16$.
3. Rewrite the paper around **source-resolved fixed-waveform dynamics**, not the obsolete universal logarithmic front.
4. Keep passive feasibility and compact-object discussion secondary.