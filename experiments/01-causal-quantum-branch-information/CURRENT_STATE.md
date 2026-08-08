# Current State — Experiment 01

**Last updated:** 2026-08-07  
**Experiment:** Causal Transport of Quantum Branch Information by Gravity

This is the canonical recovery point after the fixed-waveform, prior-art, explicit-source, and normalization audits.

---

## 1. Current central question

The broad question

> Can gravity mediate quantum information?

is already prior art.

The current sharp question is:

> **Given one explicit coherent source branch history, what normalized gravitational branch-difference wavepacket does it emit, how does that wavepacket propagate to a distant receiver, and during what spacetime interval is the complete source-mode→receiver channel non-entanglement-breaking?**

The chain is

$$
\boxed{
\text{source branch qubit}
\to
\text{quantized quadrupole cat}
\to
\text{emitted graviton difference mode}
\to
\text{retarded free-space propagation}
\to
\text{noisy receiver}.
}
$$

---

## 2. Major prior-art boundary

Do **not** claim novelty for:

- gravity-mediated entanglement;
- retarded/local gravity-mediated entanglement;
- gravity as a non-entanglement-breaking quantum channel;
- coherent-state gravitational channel benchmarks;
- noisy Newtonian gravitational state transfer;
- thermal entanglement/EB thresholds for gravitationally coupled oscillators;
- a quantized incident GW mode coupled to a quantum material receiver;
- relativistic sender→receiver channel no-signalling outside the light cone.

Key neighboring work now includes:

- Christodoulou et al. (2023): local retarded gravity-mediated entanglement;
- Lami–Pedernales–Plenio (2024): channel/LOCC gravity tests with coherent-state ensembles;
- Toccacelo–Andersen–Brask (2025): coherent-state gravitational communication benchmarks with noise;
- Mari–Zippilli–Vitali (2026): gravity-induced non-EB thermal-attenuator channel;
- Miki–Li–Chen (2026): pulsed noisy gravitational oscillator entanglement/EB bounds;
- Toccacelo–Beitel–Andersen–Pikovski (2026): quantized incident GW→acoustic detector state transfer with thermal open dynamics;
- Cliche–Kempf: relativistic field-mediated sender→receiver channel causality.

Files:

- `NOVELTY_COLLISION_CHANNEL_RETARDATION_LITERATURE.md`
- `NOVELTY_COLLISION_MIKI_TOCCACELO_2026.md`
- `CLAIM_LEDGER.md`

---

## 3. Strongest mathematical candidate: exact binary coherent NPT/EB theorem

For any finite nontrivial hybrid state

$$
|\Psi\rangle
=\sqrt p|0\rangle|\alpha\rangle
+e^{i\phi}\sqrt{1-p}|1\rangle|\beta\rangle,
$$

with

$$
0<p<1,
\qquad
\alpha\neq\beta,
$$

and any one-mode gauge-covariant phase-insensitive Gaussian channel $\Phi_{\tau,m}$,

$$
\boxed{
(I\otimes\Phi_{\tau,m})(|\Psi\rangle\langle\Psi|)
\text{ is NPT}
\iff
\tau>m.
}
$$

But

$$
\Phi_{\tau,m}\text{ is non-EB}
\iff
\tau>m.
$$

Thus every finite nontrivial binary coherent hybrid input detects the exact EB boundary of this Gaussian family.

The direct coherent-dyad identity is

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

For symmetric $|\pm a\rangle$ and $m>0$,

$$
\boxed{
v_*=\frac{2\sqrt\tau a}{m},
}
$$

and one $2\times2$ partial-transpose principal minor gives

$$
\boxed{
\frac{|z_{v_*}|^2}{p_0p_{v_*}}
=\exp\left[
\frac{4a^2}{m}(\tau-m)
\right].
}
$$

Pure loss $m=0$ is handled separately with a finite coherent test state.

**Novelty:** promising but unverified. Targeted searches have not located an equivalent all-finite-amplitude state-level theorem.

Files:

- `DIRECT_GAUSSIAN_BINARY_PROBE_PROOF.md`
- `PURE_LOSS_EDGE_CASE.md`
- `EXACT_THREE_ELEMENT_WITNESS.md`

---

## 4. Absolute finite-strength witness

The normalized ratio above is ideal for the sign boundary but can hide exponentially small event probabilities.

Compress the partial transpose to

$$
M_v=
\begin{pmatrix}
p_0&z_v^*\\
z_v&p_v
\end{pmatrix}.
$$

Define the absolute negative weight

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

In the weak-link regime $\tau,m\ll1$, jointly optimizing source separation and analysis displacement gives

$$
\boxed{
G_{\rm abs}^{\rm opt}
=\frac{W(e^{-1})}{2}
(\tau-m)+O(\tau^2),
}
$$

with

$$
\boxed{
\frac{W(e^{-1})}{2}
\simeq0.1392323.
}
$$

The leading optimal source coherent amplitude is

$$
\boxed{
a_*
\simeq0.565346\sqrt\tau.}
$$

Thus, in the weak gravitational link, absolute certifiable NPT weight is proportional to the **absolute channel quantum excess** $\tau-m$.

Files:

- `ABSOLUTE_THREE_ELEMENT_WITNESS_GAP.md`
- `WEAK_LINK_ABSOLUTE_GAP_ASYMPTOTIC.md`

---

## 5. Correct general receiver equation: fixed physical waveform

A real source emits one normalized temporal mode $f$,

$$
\int_0^\infty ds\,|f(s)|^2=1.
$$

For a Markov receiver after causal arrival,

$$
\dot c
=-\frac\kappa2c
+\sqrt{\kappa_\Delta}\,b_\Delta^{\rm in}
+\sum_a\sqrt{\kappa_a}\,b_a^{\rm in}.
$$

The coherent source-mode transfer is

$$
\boxed{
\tau_f(t)
=\kappa_\Delta
\left|
\int_0^t ds\,
e^{-\kappa(t-s)/2}f(s)
\right|^2.
}
$$

For receiver initial occupation $n_0$ and occupied-bath injection

$$
\Gamma_{\rm th}=\sum_a\kappa_a\bar n_a,
$$

the vacuum-output occupation is

$$
\boxed{
m(t)
=n_0e^{-\kappa t}
+\frac{\Gamma_{\rm th}}{\kappa}
(1-e^{-\kappa t}).
}
$$

Therefore the exact Gaussian capability condition is

$$
\boxed{
\tau_f(t)>m(t).
}
$$

For the binary coherent probe, this is simultaneously the NPT condition.

Restoring separation,

$$
\boxed{
T_{\rm cap}(R;f)
=\frac Rc+
\inf\{t>0:\tau_f(t)>m(t)\}.
}
$$

File: `GENERAL_FIXED_WAVEFORM_RECEIVER_FRONT.md`.

---

## 6. Old logarithmic front: correct but special

Cauchy–Schwarz gives the protocol envelope

$$
\tau_f(t)
\le
\frac{\kappa_\Delta}{\kappa}
(1-e^{-\kappa t}).
$$

The saturating source mode depends on the chosen target time.

For a stationary thermal initial receiver,

$$
n_0=\Gamma_{\rm th}/\kappa,
$$

the optimized envelope crosses the EB boundary at

$$
\boxed{
T_{\rm cap}^{\rm env}
=\frac Rc+
\frac1\kappa
\ln\frac{\kappa_\Delta}
{\kappa_\Delta-\Gamma_{\rm th}}.
}
$$

This is a best-case stationary benchmark, **not** the universal physical front.

File: `MASTER_CAUSAL_FRONT_EQUATION.md` with corrected scope.

---

## 7. Explicit quantum source: four-mass plus normal mode

Use four equal endpoint masses $\mu$ in a cross. In branch $s=\pm1$,

$$
X_s^2=L^2+s\,d(t),
$$

$$
Y_s^2=L^2-s\,d(t).
$$

The center of mass is fixed and the STF branch difference is exactly

$$
\boxed{
\Delta Q_{xx}=4\mu d(t),
\qquad
\Delta Q_{yy}=-4\mu d(t),
\qquad
\Delta Q_{zz}=0.
}
$$

For small deformation define one plus normal coordinate $u$:

$$
X\simeq L+u,
\qquad
Y\simeq L-u.
$$

Then

$$
\boxed{M_{\rm eff}=4\mu,}
$$

and

$$
\boxed{
\delta Q_{xx}=4\mu Lu,
\qquad
\delta Q_{yy}=-4\mu Lu.
}
$$

Quantize

$$
u=u_{\rm zpf}(a+a^\dagger),
$$

$$
\boxed{
u_{\rm zpf}=\sqrt{\hbar/(8\mu\omega)}.}
$$

A state-dependent internal force

$$
\boxed{H_F=-\sigma_zF(t)u}
$$

creates coherent mechanical branches $|\pm\alpha(t)\rangle$.

Choose the closed smooth trajectory

$$
\boxed{
u_c(t)
=u_0\sin^4(\pi t/T)\cos\omega t,
\qquad0<t<T.}
$$

The source returns to the same mechanical phase-space point after emitting a branch-dependent gravitational wavepacket.

Files:

- `CONSERVED_FOUR_MASS_QUADRUPOLE_SOURCE.md`
- `QUANTIZED_PLUS_MODE_SOURCE.md`

---

## 8. Explicit emitted graviton mode

For a conserved nonrelativistic quadrupole branch difference,

$$
\boxed{
N_\Delta
=\frac{G}{5\pi\hbar c^5}
\int_0^\infty d\omega'\,
\omega'^5
|\Delta\widetilde Q_{ij}(\omega')|^2.
}
$$

For the four-mass $\sin^4$ narrowband source,

$$
\boxed{
N_\Delta
\simeq
\frac72
\frac{G\mu^2L^2u_0^2\omega^5T}
{\hbar c^5}.
}
$$

The normalized outgoing temporal mode is

$$
\boxed{
f_4(t)
=\sqrt{\frac{128}{35T}}
\sin^4(\pi t/T),
\qquad0<t<T,}
$$

up to controlled narrowband corrections.

The same $N_\Delta$ follows independently from the mechanical-mode input-output identity

$$
N_\Delta
=\kappa_g\int dt\,|\Delta\alpha_m(t)|^2.
$$

---

## 9. Receiver gravitational linewidth and retarded propagation

For the four-mass plus mode,

$$
\boxed{
\kappa_g
=\frac{8G\mu L^2\omega^4}{5c^5}.
}
$$

For aligned source and receiver plus quadrupoles, the retarded cross response is

$$
\boxed{
\Sigma_{AB}^{R}
=\frac54
\sqrt{\kappa_{g,A}\kappa_{g,B}}
\frac{P(\epsilon)e^{i\epsilon}}
{\epsilon^5},
}
$$

where

$$
P(\epsilon)
=3-3i\epsilon-3\epsilon^2+2i\epsilon^3+\epsilon^4,
\qquad
\epsilon=\omega R/c.
$$

The source-output→receiver-input storage amplitude is

$$
\boxed{
t_{AB}^{\rm store}
=-i\Sigma_{AB}^{R}/
\sqrt{\kappa_{g,A}\kappa_{g,B}}.
}
$$

Wave zone:

$$
\boxed{
\eta_{\rm store}(R)
=\frac{25\mathcal O}{16(kR)^2}.
}
$$

---

## 10. $25/16$ storage normalization now has three independent checks

### Green-function route

$$
\Sigma_{AB}^{R}
\to
\frac54
\frac{e^{ikR}}{kR}
\sqrt{\kappa_A\kappa_B}.
$$

### Gravitational power-flow / partial-wave route

The plus-quadrupole angular pattern has

$$
\frac1P\frac{dP}{d\Omega}\bigg|_{z}
=\frac{5}{8\pi}.
$$

A critically coupled single $l=2$ channel has

$$
\sigma_{\rm abs,max}^{(2)}
=\frac{5\pi}{2k^2}.
$$

Thus

$$
\boxed{
\frac{P_{\rm abs}}P
=\frac{5}{8\pi R^2}
\frac{5\pi}{2k^2}
=\frac{25}{16(kR)^2}.
}
$$

### Electromagnetic control

For a transverse electric dipole,

$$
\frac1P\frac{dP}{d\Omega}\bigg|_{\rm max}
=\frac{3}{8\pi},
$$

and

$$
\sigma_{\rm abs,max}^{(1)}
=\frac{3\pi}{2k^2}.
$$

Therefore

$$
\eta_{\rm dip}^{\rm store}
=\frac{9}{16(kR)^2},
$$

matching the standard normalized far-zone electromagnetic Green coupling.

The four-times-larger gravitational coefficient corresponds to the unitary **scattering** cross section, not state storage.

File: `STORAGE_NORMALIZATION_25_OVER_16_AUDIT.md`.

---

## 11. Explicit source-specific quantum-capability bubble

For the normalized $\sin^4$ source, let

$$
x=t/T,
\qquad
q=\kappa T.
$$

Define

$$
J_{4,q}(y)
=\int_0^y dz\,e^{qz/2}\sin^4(\pi z),
$$

$$
\boxed{
S_{4,q}(x)
=\frac{128q}{35}
e^{-qx}J_{4,q}^2[\min(x,1)],
}
$$

and

$$
N_q(x)=1-e^{-qx}.
$$

Then

$$
\boxed{
\tau_4
=\frac{\kappa_\Delta(R)}\kappa S_{4,q}(x),
}
$$

$$
\boxed{
m
=\frac{\Gamma_{\rm th}}\kappa N_q(x).
}
$$

The channel is non-EB iff

$$
\boxed{
\frac{\kappa_\Delta(R)}{\Gamma_{\rm th}}
\frac{S_{4,q}(x)}{N_q(x)}>1.
}
$$

Optimizing the receiver bandwidth and pulse time gives

$$
\boxed{
\kappa T\simeq5.41429,
}
$$

$$
\boxed{H_{4,*}\simeq0.8136763.}
$$

Thus the fixed mechanical pulse has a non-EB window only if

$$
\boxed{
\kappa_\Delta>1.22899\,\Gamma_{\rm th}.
}
$$

For each allowed distance there are two time boundaries: EB → non-EB → EB.

Near the smooth causal wavefront,

$$
f_4(t)\sim t^4,
$$

so

$$
\boxed{	au_4(t)\sim t^{10}}
$$

while Markov thermal occupation grows as $t$.

Thus the post-light-cone quantum delay depends explicitly on source smoothness/history.

File: `SIN4_MECHANICAL_SOURCE_QUANTUM_WINDOW.md`.

---

## 12. Explicit end-to-end passive scaling

Let total receiver endpoint mass be

$$
M=4\mu.
$$

Then

$$
\boxed{
\kappa_\Delta(R)
=\frac{5\mathcal O}{8}
\frac{GM L^2\omega^2}
{c^3R^2}.
}
$$

At wave-zone radius $kR=\zeta$, with ordinary receiver linewidth $\kappa\simeq\omega/Q$, define

$$
\mathcal C=\frac{2GM}{c^2L},
\qquad
\beta=\frac{\omega L}{c}.
$$

Then

$$
\boxed{
\frac{\kappa_\Delta}{\kappa}
=\frac{5\mathcal O}{16\zeta^2}
Q\mathcal C\beta^3.
}
$$

For the optimized $\sin^4$ pulse in vacuum and weak capture,

$$
\boxed{
\mathcal N_{\max}^{\rm WZ}
\simeq
0.249382
\frac{\mathcal O}{\zeta^2}
Q\mathcal C\beta^3.
}
$$

The minimal absolute three-element witness reaches

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

## 13. Stronger source is not automatically better

For a pure-loss link with small capture fraction $\eta$,

$$
\boxed{
N_\Delta^{\rm opt}
\simeq4\sqrt\eta.
}
$$

A much larger emitted branch record mostly goes into gravitational modes the receiver does not catch, which creates a stronger which-branch environment and reduces retained source–receiver entanglement.

The central information-flow lesson is:

> **source strength and link quality are separate resources.**

---

## 14. Current novelty candidates

### Candidate A
Exact binary coherent NPT/EB equivalence for the full phase-insensitive Gaussian family.

### Candidate B
Exact minimal three-element principal-minor witness reaching that boundary.

### Candidate C
The controlled source-branch → emitted normalized difference wavepacket → explicit-distance propagation → noisy receiver calculation as one complete link.

### Candidate D
The resulting source-specific spacetime quantum-capability bubble and smaller absolute-certification bubble.

Targeted searches have not yet located exact equivalents for A/B or the same complete source-resolved construction for C/D. This does **not** establish novelty.

---

## 15. Strongest next path

The project is mature enough that expansion is now lower value than verification.

1. **Broaden citation-forward novelty search for Candidate A/B.**
2. **Independently rederive the binary theorem in a second formalism** if possible.
3. **Perform one canonical-TT mode derivation of the $25/16$ link** as a final field-normalization audit, although three independent checks already agree.
4. **Audit the source actuator/control stress-energy** so the explicit mechanical source is genuinely closed/conserved at the required order.
5. Only after these checks, convert `PAPER_CORE_V3.md` into a conventional manuscript.

## Current Feynman-level compression

> **A real quantum source emits one gravitational branch wavepacket, not an abstract force. The receiver sees only the fraction of that wavepacket that reaches and matches its quantum mode. At first too little coherent branch information has arrived; a noisy receiver may become quantum-capable only for a finite interval, and then lose that capability again after the pulse passes. Making the source arbitrarily stronger does not solve the problem, because the gravitational field the receiver fails to catch becomes a which-branch record of its own. The clean question is therefore: for one closed coherent source history, how much branch information reaches one distant receiver, and is the resulting source-to-receiver map ever measurably non-entanglement-breaking?**