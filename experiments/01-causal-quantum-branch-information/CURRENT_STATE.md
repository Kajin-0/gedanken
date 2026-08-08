# Current State — Experiment 01

**Last updated:** 2026-08-07 20:04 EDT  
**Experiment:** Causal Transport of Quantum Branch Information by Gravity

This is the canonical recovery point. The project has undergone a substantial novelty and model audit. Several broad claims are now known prior art; the strongest remaining target is a **source-resolved retarded gravitational link** from a controlled branch history to a noisy receiver.

---

## 1. Current central question

The broad question

> Can gravity mediate quantum information?

is already occupied by existing work.

The sharper current question is:

> **Given one explicit coherent source branch history, what retarded gravitational wavepacket does it emit, how much of that wavepacket reaches a specified quantum receiver, and during what spacetime interval is the complete source-mode $\to$ receiver channel non-entanglement-breaking?**

The desired chain is

$$
\boxed{
\text{controlled source branch}
\to
\text{emitted graviton difference mode}
\to
\text{retarded propagation}
\to
\text{noisy receiver}.
}
$$

---

## 2. Major prior-art collisions

Do **not** claim novelty for the following.

### Gravity as a quantum/non-EB channel

Mari–Zippilli–Vitali (2026) already formulate gravity as a quantum-information channel and use the thermal-attenuator non-entanglement-breaking boundary.

### Coherent-state gravity channel tests

Lami–Pedernales–Plenio (2024), Toccacelo–Andersen–Brask (2025), and Mari et al. already use coherent-state channel benchmarks / characterization in gravitational settings.

### Retarded gravity-mediated entanglement

Christodoulou et al. (2023) already derive locally mediated retarded gravitational entanglement and light-crossing onset.

### Relativistic source-to-receiver channel causality

Cliche–Kempf already show that a localized sender cannot alter a spacelike-separated receiver channel even though vacuum entanglement can still be harvested.

### Coupling versus thermal decoherence in gravitational oscillators

Miki–Li–Chen (2026) derive pulsed gravitational entanglement-generation and entanglement-breaking bounds for noisy Newtonian oscillator dynamics.

### Quantized gravitational wave $\to$ quantum material receiver

Toccacelo–Beitel–Andersen–Pikovski (2026) already model a passing quantized GW mode swapping quantum state with a resonant acoustic detector and include thermal open-system dynamics.

Therefore the remaining contribution must be narrower than any of these ingredients individually.

Files:

- `NOVELTY_COLLISION_CHANNEL_RETARDATION_LITERATURE.md`
- `NOVELTY_COLLISION_MIKI_TOCCACELO_2026.md`

---

## 3. Strongest surviving mathematical result

For any finite nontrivial binary coherent hybrid state

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

and any one-mode gauge-covariant phase-insensitive Gaussian channel

$$
\Phi_{\tau,m},
$$

the current theorem is

$$
\boxed{
(I\otimes\Phi_{\tau,m})(|\Psi\rangle\langle\Psi|)
\text{ is NPT}
\iff
m<\tau.
}
$$

But

$$
\Phi_{\tau,m}\text{ is non-EB}
\iff
m<\tau.
$$

Thus every finite nontrivial binary coherent hybrid input detects the exact EB boundary of this Gaussian family.

### Direct finite-minor proof

For the chosen characteristic-function convention,

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

For symmetric branches $|\pm a\rangle$ and $m>0$, one optimized $2\times2$ principal minor gives

$$
\boxed{
\frac{|z_{v_*}|^2}{p_0p_{v_*}}
=\exp\left[
\frac{4a^2}{m}(\tau-m)
\right],
\qquad
v_*=\frac{2\sqrt\tau a}{m}.
}
$$

Pure loss $m=0$ has a separate finite coherent-state test, so the edge case is closed.

Files:

- `DIRECT_GAUSSIAN_BINARY_PROBE_PROOF.md`
- `PURE_LOSS_EDGE_CASE.md`
- `EXACT_THREE_ELEMENT_WITNESS.md`

**Novelty:** still promising but unverified. Existing coherent-state channel tests do not yet appear to state this exact all-finite-amplitude NPT/EB equivalence.

---

## 4. General physical receiver equation — corrected

A real source produces one fixed physical waveform. Let

$$
\int_0^\infty ds\,|f(s)|^2=1.
$$

For a Markov receiver after retarded arrival,

$$
\dot c
=-\frac\kappa2c
+\sqrt{\kappa_\Delta}\,b_\Delta^{\rm in}
+\sum_a\sqrt{\kappa_a}\,b_a^{\rm in}.
$$

The exact coherent transmission from the selected source mode into the receiver at local time $t$ is

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

If the receiver begins with occupation $n_0$, while occupied baths inject

$$
\Gamma_{\rm th}=\sum_a\kappa_a\bar n_a,
$$

then the vacuum-output occupation is

$$
\boxed{
m(t)
=n_0e^{-\kappa t}
+\frac{\Gamma_{\rm th}}{\kappa}
(1-e^{-\kappa t}).
}
$$

Therefore the exact fixed-waveform capability condition is

$$
\boxed{
\tau_f(t)>m(t).
}
$$

For the binary coherent source probe, the same inequality is exactly the NPT condition.

Restoring propagation,

$$
\boxed{
T_{\rm cap}(R;f)
=\frac Rc+
\inf\{t>0:\tau_f(t)>m(t)\}.
}
$$

File: `GENERAL_FIXED_WAVEFORM_RECEIVER_FRONT.md`.

---

## 5. The old logarithmic front is only an envelope

Cauchy–Schwarz gives

$$
\tau_f(t)
\le
\frac{\kappa_\Delta}{\kappa}
(1-e^{-\kappa t}).
$$

The saturating waveform depends on the chosen target time.

For arbitrary initial occupation, the protocol-optimized envelope crosses the EB boundary at

$$
\boxed{
T_{\rm cap}^{\rm env}
=\frac1\kappa
\ln\left[
1+
\frac{\kappa n_0}
{\kappa_\Delta-\Gamma_{\rm th}}
\right]
}
$$

when

$$
\kappa_\Delta>\Gamma_{\rm th}.
$$

For a stationary thermal initial state,

$$
n_0=\Gamma_{\rm th}/\kappa,
$$

this reduces to the previously derived logarithm

$$
\boxed{
T_{\rm cap}^{\rm env}
=\frac1\kappa
\ln\frac{\kappa_\Delta}
{\kappa_\Delta-\Gamma_{\rm th}}.
}
$$

This remains a useful **best-case stationary benchmark**, not the universal front.

File renamed in scope, not path: `MASTER_CAUSAL_FRONT_EQUATION.md`.

---

## 6. First source-specific analytic benchmark: exponential branch pulse

Take

$$
\boxed{
f_S(t)
=\sqrt{\Gamma_S}
e^{-\Gamma_St/2}\Theta(t).
}
$$

For bandwidth matching

$$
\Gamma_S=\kappa,
$$

and local time

$$
x=\kappa t,
$$

$$
\boxed{
\tau(t)
=\frac{\kappa_\Delta}{\kappa}
x^2e^{-x}.
}
$$

For a ground-state receiver,

$$
\boxed{
m(t)
=\frac{\Gamma_{\rm th}}{\kappa}(1-e^{-x}).
}
$$

The channel is non-EB iff

$$
\boxed{
h(x)
\equiv
\frac{x^2}{e^x-1}
>
r,
\qquad
r=\frac{\Gamma_{\rm th}}{\kappa_\Delta}.
}
$$

The function has a single maximum at

$$
\boxed{
x_*
=2+W_0(-2e^{-2})
\simeq1.59362,
}
$$

with

$$
\boxed{
h_*
\simeq0.647610.
}
$$

Therefore a non-EB interval exists iff

$$
\boxed{
\kappa_\Delta
>1.54414\,\Gamma_{\rm th}.
}
$$

When it exists there are two roots

$$
x_-<x_*<x_+,
$$

and the physical receiver evolves

$$
\boxed{
\mathrm{EB}
\to
\mathrm{non\!-\!EB}
\to
\mathrm{EB}.
}
$$

This is a **finite quantum-capability window**, not a permanently open cone.

File: `EXPONENTIAL_SOURCE_QUANTUM_WINDOW.md`.

---

## 7. Gravity-specific wave-zone map

For aligned resonant plus-type source and receiver quadrupoles,

$$
\boxed{
\Sigma_{AB}^{R}
=\frac54
\sqrt{\kappa_{g,A}\kappa_{g,B}}
\frac{P(\epsilon)e^{i\epsilon}}
{\epsilon^5},
\qquad
\epsilon=\omega R/c,
}
$$

with

$$
P(\epsilon)
=3-3i\epsilon-3\epsilon^2+2i\epsilon^3+\epsilon^4.
$$

The source-output $\to$ receiver-input storage amplitude is

$$
\boxed{
t_{A\to B}^{\rm store}
=-i\Sigma_{AB}^{R}/
\sqrt{\kappa_{g,A}\kappa_{g,B}}.
}
$$

Wave zone:

$$
\boxed{
\eta_{\rm store}(R)
\simeq
\frac{25\mathcal O}{16(kR)^2}.
}
$$

Hence

$$
\boxed{
\kappa_\Delta(R)
=\frac{25\mathcal O}{16(kR)^2}\kappa_g.
}
$$

This is currently the essential source-distance link that is absent from the local incident-GW receiver model.

Files:

- `NORMALIZED_GRAVITATIONAL_CROSS_RESPONSE.md`
- `DELAYED_GRAVITATIONAL_INPUT_OUTPUT.md`
- `INDEPENDENT_CROSS_RESPONSE_CHECK.md`

---

## 8. Exponential source spacetime window

Define the old optimized-envelope distance scale

$$
\boxed{
R_{\rm env}
=\frac5{4k}
\sqrt{
\frac{\mathcal O\kappa_g}
{\Gamma_{\rm th}}
}.
}
$$

For the matched decaying exponential source,

$$
r(R)
=\left(\frac{R}{R_{\rm env}}\right)^2.
$$

The source-specific non-EB window exists only for

$$
\boxed{
R<R_{\rm exp}
=\sqrt{h_*}\,R_{\rm env}
\simeq0.804742\,R_{\rm env}.
}
$$

Its two spacetime boundaries are

$$
\boxed{
T_\pm(R)
=\frac Rc+
\frac{x_\pm[r(R)]}{\kappa}.
}
$$

As

$$
R\to R_{\rm exp}^{-},
$$

the two boundaries merge at the finite time

$$
\boxed{
T_*-R/c
\simeq1.59362/\kappa.
}
$$

The window closes with square-root root merging, not logarithmic divergence.

This is currently the strongest source-specific gravitational spacetime result.

---

## 9. Source branch strength

For a compact nonrelativistic conserved quadrupole branch difference,

$$
\boxed{
N_\Delta
=\frac{G}{5\pi\hbar c^5}
\int_0^\infty d\omega\,
\omega^5
|\Delta\widetilde Q_{ij}(\omega)|^2.
}
$$

For a narrowband source

$$
\Delta Q_{ij}^{(+)}(t)
=q_{ij}e^{-i\omega_0t}g(t),
$$

with

$$
\Delta\omega\ll\omega_0,
$$

the normalized emitted graviton temporal mode follows $g(t)$ to leading order because the $\omega^{5/2}$ radiative weighting is nearly constant across the pulse bandwidth.

This connects a physical source trajectory to the channel waveform $f(t)$.

File: `GRAVITATIONAL_DIFFERENCE_MODE_AMPLITUDE.md`.

---

## 10. Finite-certification metric requires correction

The normalized exact witness ratio

$$
\Lambda
=\ln\frac{|z|^2}{p_0p_v}
$$

is excellent for locating the NPT/EB **sign boundary**.

It is not sufficient as an experimental-strength metric near vanishing transmission, because the optimized coherent analysis state can move far into phase space and the absolute event probabilities can become exponentially small.

The next preferred quantities are

1. the negative eigenvalue of the matched $2\times2$ partial-transpose block;
2. the corresponding rigorous lower bound on full negativity;
3. exact full negativity when analytically available.

The older `FINITE_STRENGTH_CERTIFICATION_FRONT.md` should therefore be treated as a normalized-boundary construction, not the final practical certification theory.

---

## 11. Passive receiver bounds remain secondary

For passive nonrelativistic matter,

$$
\frac{\kappa_g}{\omega}
\le
\frac23\mathcal C_B\beta_B^3.
$$

In vacuum and weak capture,

$$
\mathcal N_{\max}
\simeq
\eta_Q,
$$

leading to the receiver-class ceiling

$$
\boxed{
\mathcal N_{\max}^{\rm WZ}
\lesssim
\frac{25\mathcal O}{24\zeta^2}
Q_B\mathcal C_B\beta_B^3.
}
$$

This is useful feasibility context but not the central novelty claim.

---

## 12. Strongest remaining novelty candidates

### Candidate A — binary coherent exact NPT/EB theorem

No equivalent all-finite-amplitude state-level theorem has yet been located.

### Candidate B — exact three-element principal-minor witness

No equivalent minimal witness saturating the full phase-insensitive Gaussian EB boundary has yet been located.

### Candidate C — source-resolved retarded complete link

The most promising gravity-specific synthesis is

$$
\boxed{
\text{controlled branch source}
\to
\text{emitted difference wavepacket}
\to
\text{distance-dependent retarded propagation}
\to
\text{noisy receiver channel}.
}
$$

### Candidate D — source-specific spacetime quantum-capability window

For an explicit quadrupole pulse, derive the complete EB/non-EB region in $(R,T)$ rather than assuming an already-arrived GW mode or a Newtonian instantaneous interaction.

Novelty remains unverified and must be stated cautiously.

---

## 13. Strongest next path

1. Replace normalized finite-certification margin by an **absolute negativity/witness-gap theory**.
2. Replace the sharp exponential turn-on by a **smooth finite conserved quadrupole pulse**, calculate its normalized emitted graviton mode, and derive its source-specific EB window.
3. Update `PAPER_CORE_V2.md` and `CLAIM_LEDGER.md` only after those corrections are complete.
4. Continue citation-forward searching specifically for the exact binary coherent NPT/EB theorem.

## Current Feynman-level compression

> **The receiver does not become quantum simply because the gravitational signal has arrived. A real source emits one finite waveform. At first the receiver has accumulated too little of that coherent branch record; thermal noise may dominate. A quantum window can then open when coherent capture overtakes the classicalizing noise, and it can close again after the pulse passes. The exact timing depends on the emitted source waveform, the retarded source-to-receiver mode overlap, and the receiver's noise. The strongest remaining question is therefore not whether gravity can carry quantum information in principle, but whether one can derive and certify that complete source-to-receiver quantum window from a specified coherent gravitational source history.**