# Prior-Art Matrix V5 — End-to-End Gravity Construction

**Date:** 2026-08-08  
**Status:** **SOURCE-LEVEL ADVERSARIAL AUDIT OF THE V5 MANUSCRIPT CLAIM**

## 1. Question being audited

The current manuscript does **not** claim novelty for any of the following separately:

- coherent graviton radiation;
- conserved branch-conditioned graviton emission;
- causal propagation of quantized gravitons;
- gravitationally generated entanglement;
- quantum gravitational-wave reception;
- gravitational quantum communication;
- Gaussian entanglement-breaking thresholds;
- thermal limits on gravitational quantum channels.

The only remaining candidate contribution is the combined construction

$$
\boxed{
\text{local quantum encoder}
\to
\text{conserved finite-support radiative source}
\to
\text{normalized emitted graviton mode}
\to
\text{retarded free-space capture}
\to
\text{noisy resonant receiver}
\to
\text{end-to-end NPT/non-EB condition}.
}
$$

This note asks whether the closest current papers already contain that complete chain, perhaps under different notation.

The conclusion of this audit is:

> **No inspected source was found to contain the complete V5 chain with all interfaces explicitly normalized.**

This is an audit result, **not proof of priority**. The safe manuscript claim remains that V5 provides an explicit source-resolved quantitative synthesis not found in the sources audited here.

---

# 2. Summary matrix

| Work | Local quantum preparation | Closed/conserved radiative source | Explicit propagating graviton mode | Source→receiver free-space normalization | Resonant material receiver | Thermal receiver | EB/NPT/channel criterion | Main overlap with V5 |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Matsui 2026, arXiv:2607.20867 | No explicit local encoder | **Yes** | **Yes** | No distant receiver map | No | Graviton initial state can be nonvacuum, but no receiver bath | Decoherence/field-state overlap, not receiver EB | strongest source-side collision |
| Laga–Suyama 2026, arXiv:2604.20228 | No; prescribed classical source | Conserved classical stress assumed | **Yes**, coherent GW state | No distant receiver map | No | No | No | coherent-source/retarded-field collision |
| Toccacelo–Beitel–Andersen–Pikovski 2026, arXiv:2602.09125 | Incident GW state is input | Source not modeled | **Yes**, already-present incident GW mode | No source-distance normalization | **Yes** | **Yes** | Gaussian transfer implicit; EB not their focus | strongest receiver-side collision |
| Trenggana–Zen 2026, arXiv:2606.12901 | Initial matter states specified | No complete finite conserved actuator/source construction | **Yes** | Causal distance kernel appears directly | Two trapped particles rather than capture receiver | Field noise appears in influence functional; detailed thermal receiver not central | Entanglement after delay, not a source→receiver EB channel | strongest causal-propagation collision |
| Mari–Zippilli–Vitali 2025/2026, arXiv:2504.05998 | Optical input channel | No radiative source | No travelling radiative graviton mode in explicit model | No wave-zone mode capture | Two optomechanical systems | **Yes** | **Yes**, non-EB thermal attenuator | strongest generic gravity-channel collision |
| Toccacelo–Andersen–Brask 2025, arXiv:2503.03585 | Mechanical/communication probes | No radiative source | No explicit propagating wave-zone mode | No | Gravitationally coupled oscillators | Open-system benchmarks | Quantum-communication benchmarks | communication concept collision |
| Miki–Li–Chen 2026, arXiv:2605.26240 | Optical pulses swap states into mechanics | No radiative source | No propagating GW link | No | Two gravitationally coupled mechanics + optical readout | **Yes** | **Yes**, EA/EB and entanglement thresholds | pulse/state-swap + thermal-threshold collision |
| Yant–Blencowe 2025, arXiv:2503.20855 | QFT matter states | QFT source description | Linearized gravity, **static limit** | No radiative transfer link | No dedicated distant resonant capture stage | Not V5 receiver model | GIE observable rather than EB channel | relativistic/QFT matter-model collision |
| **V5** | **Yes: branch-common local resonant encoder** | **Yes: explicit finite-spoke conserved source** | **Yes: complete encoder+tail normalized difference mode** | **Yes: audited \(25/[16(kR)^2]\)** | **Yes** | **Yes** | **Yes: end-to-end NPT/non-EB condition** | combined chain |

---

# 3. Matsui 2026 — strongest source-side collision

**Hiroki Matsui, “Graviton-induced which-path decoherence in matter-wave interferometry,” arXiv:2607.20867 (2026).**

## What Matsui already does

Matsui explicitly states that the radiative problem is treated for a **closed, conserved source**. Each branch is represented by a classical total stress tensor

$$
T_b^{\mu\nu}(x),
$$

with

$$
\partial_\mu T_b^{\mu\nu}=0,
\qquad
\partial_\mu\Delta T^{\mu\nu}=0.
$$

The TT graviton coupling is

$$
H_{\rm int}(t)
=-\frac\kappa2\int d^3x\,
\hat h_{ij}^{\rm TT}(t,\mathbf x)
T^{ij}(t,\mathbf x),
$$

and each branch produces a coherent displacement

$$
\alpha_{b,s}(\mathbf k)
=
\frac{i\kappa}{2\sqrt{2\omega_k}}
\epsilon_{ij}^{s*}(\hat{\mathbf k})
\widetilde T_b^{ij}(\omega_k,\mathbf k).
$$

The difference-mode norm is

$$
N_\Delta
=\sum_s\int\frac{d^3k}{(2\pi)^3}
|\Delta\alpha_s(\mathbf k)|^2,
$$

with

$$
\boxed{\Gamma_{\rm vac}=N_\Delta/2.}
$$

Matsui also uses conservation to reduce the source to the ordinary nonrelativistic mass quadrupole.

## What V5 must therefore not claim

Do not claim as new:

- the need for a closed conserved branch stress tensor;
- branch-conditioned coherent graviton displacements;
- the difference-source graviton mode;
- \(N_\Delta\) as squared coherent-state distance;
- \(\Gamma_{\rm vac}=N_\Delta/2\);
- the quadrupole reduction itself.

## Remaining distinction

Matsui's calculation terminates at the radiated field / matter-decoherence problem. It does not construct

- the finite-spoke source architecture used here;
- the branch-common local resonant preparation gate;
- a distant resonant receiver;
- a source-output→receiver storage coefficient;
- source and receiver branching fractions;
- an end-to-end EB/NPT receiver criterion.

The explicit finite-spoke source should therefore be framed as a **concrete realization of the conserved-source requirement emphasized by Matsui**, not as discovery of that requirement.

Primary source: arXiv:2607.20867, especially Secs. II–V and Eqs. (5), (15), (17), (31)–(36).

---

# 4. Laga and Suyama 2026 — coherent retarded radiation collision

**Felix Laga and Teruaki Suyama, “Quantum description of gravitational waves generated by a classical source,” arXiv:2604.20228 (2026).**

They treat a quantum gravitational-wave field driven by a classical energy-momentum tensor and show that the GW expectation value exactly reproduces the classical **retarded** solution. The emitted graviton statistics are Poissonian, as expected for coherent-state radiation.

This occupies the statement

> a classical/semiclassical stress tensor linearly driving the graviton field produces coherent gravitational radiation whose mean field is the classical retarded waveform.

V5 differs operationally because the source branch degree of freedom is locally prepared and retained as a quantum reference, and because the emitted mode is subsequently connected to a noisy receiver channel.

Do not sell coherent gravitational radiation or recovery of the retarded classical field as novel.

Primary source: arXiv:2604.20228.

---

# 5. Toccacelo et al. 2026 — strongest receiver-side collision

**Kristian Toccacelo, Thomas Beitel, Ulrik Lund Andersen, Igor Pikovski, “Quantum State Characterization of Gravitational Waves via Graviton Counting Statistics,” arXiv:2602.09125 (2026).**

This is the nearest published receiver model.

They begin with an already-present incident quantized GW mode \(a\) and a resonant bulk-acoustic phonon mode \(b_\ell\). Under RWA,

$$
\boxed{
H_{\rm int}
=\hbar\gamma_g
(b_\ell^\dagger a+b_\ell a^\dagger).
}
$$

At resonance,

$$
b_\ell(t)
=e^{-i\omega t}
[\cos(\gamma_gt)b_\ell-i\sin(\gamma_gt)a].
$$

Thus the incoming GW quantum state is coherently transferred to matter through a beam-splitter interaction.

For Gaussian incident radiation, the detector moments contain the exact transfer factors

$$
\sigma_{\rm bar}(t)
=\cos^2(\gamma_gt)\sigma_{\rm bar}(0)
+\sin^2(\gamma_gt)\sigma_{\rm grav}(0),
$$

$$
\bar r_{\rm bar}(t)
=\sin(\gamma_gt)\bar r_{\rm grav}(0).
$$

They also explicitly add a Markov thermal bath. Their open detector solution is

$$
\sigma_{\rm bar}(t)
=e^{-\kappa t}
[
\cos^2(\gamma_gt)\sigma_{\rm bar}(0)
+\sin^2(\gamma_gt)\sigma_{\rm grav}(0)
]
+(1-e^{-\kappa t})(\bar N+1/2)I,
$$

$$
\bar r_{\rm bar}(t)
=e^{-\kappa t/2}
\sin(\gamma_gt)\bar r_{\rm grav}(0).
$$

## Consequence

Do not claim novelty for

- quantum GW → resonant matter state transfer;
- beam-splitter graviton–phonon coupling;
- Gaussian state transfer into the detector;
- Markov thermal noise in such a detector.

## Remaining distinction

Their input is an already-present incident GW mode, motivated primarily by astrophysical waves. They do not derive that mode from a controlled laboratory quantum source at range \(R\), nor do they derive the V5 source-branching × free-space-storage × receiver-branching factorization.

V5's receiver dynamics should therefore be explicitly connected to this paper rather than presented as a new receiver concept.

Primary source: arXiv:2602.09125, especially Sec. II, Eq. (3)/(6), and App. C.2 Eq. (116).

---

# 6. Trenggana and Zen 2026 — causal propagating-entanglement collision

**Anom Trenggana and Freddy P. Zen, “Quantum Gravity Induced Entanglement from Propagating Gravitons,” arXiv:2606.12901 (2026).**

They consider two massive particles in harmonic traps interacting with propagating modes of the quantized gravitational field. The reduced matter dynamics are formulated using a Feynman–Vernon/influence-functional operator treatment.

Their momentum integration produces an explicit retarded condition and a delay

$$
\boxed{t\ge d/c}
$$

before the relevant entangling contribution appears.

Thus the broad claim

> propagating quantized gravitons can produce causally delayed entanglement between separated matter systems

is occupied prior art.

## Important difference in source structure

For their one-dimensional matter configuration they focus on the \(T_{11}\) component,

$$
T_{11}(t,-\mathbf k)
\sim
\frac{p_A^2c^2}{E_A}
 e^{-i\mathbf k\cdot x_A}
+
\frac{p_B^2c^2}{E_B}
 e^{-i\mathbf k\cdot x_B}.
$$

They explicitly state that this is an effective interaction form emphasizing the **causal propagation contribution** rather than a complete treatment of the full tensorial graviton interaction.

Their result is derived in the weak-coupling, nonrelativistic, large-separation/low-fluctuation regime.

## Remaining distinction

V5 is not a calculation of entanglement generated by two oscillators through the common field. It instead tracks a prepared source-reference branch through

1. an explicit conserved radiator;
2. a selected emitted wavepacket;
3. an explicit source→receiver storage normalization;
4. a noisy receiver channel.

That is a narrower source-to-receiver communication/capability problem.

Primary source: arXiv:2606.12901, especially Secs. 2.3–4 and Eq. (4.10).

---

# 7. Mari, Zippilli, and Vitali — gravitational non-EB channel collision

**Andrea Mari, Stefano Zippilli, David Vitali, “Can gravity mediate the transmission of quantum information?” arXiv:2504.05998; Phys. Rev. D 113, L021905 (2026).**

This paper already makes the core quantum-information move of asking whether a gravity-induced communication channel is **entanglement breaking**.

In their explicit model, two optomechanical systems are coupled through a quadratic gravitational interaction

$$
\boxed{
V
=\hbar\lambda
(b_1^\dagger+b_1)(b_2^\dagger+b_2),
}
$$

which they identify with the weak/linearized Newtonian regime. Under RWA the interaction becomes a passive four-mode hopping chain.

The resulting optical transmission line is a phase-insensitive Gaussian thermal attenuator, and its quantum/classical transition is characterized by the standard non-EB condition.

## Consequence

Do not claim novelty for

- gravity-induced quantum communication as a channel;
- using non-EB as the criterion of quantum capability;
- a sharp thermal transition of a gravitational Gaussian channel.

## Remaining distinction

Their explicit gravity interaction is direct/Newtonian between local mechanical resonators. It is not decomposed into

$$
\text{radiating source}
\to
\text{travelling graviton mode}
\to
\text{free-space mode capture}
\to
\text{receiver}.
$$

V5 therefore needs to cite this work as the closest **channel-theoretic** antecedent while making clear that its own contribution is the radiative source-resolved normalization.

Primary source: arXiv:2504.05998, especially Eqs. (5), (8)–(12).

---

# 8. Toccacelo, Andersen, and Brask 2025 — communication benchmark collision

**Kristian Toccacelo, Ulrik Lund Andersen, Jonatan Bohr Brask, “Benchmarks for quantum communication via gravity,” arXiv:2503.03585 (2025).**

This work establishes quantum-communication benchmarks for gravitationally interacting mechanical oscillators and explicitly studies transmission of quantum states under different gravity models.

The conceptual space

> use communication/state-transfer performance rather than only generated entanglement to test gravity

is therefore occupied.

The paper does not supply the V5 radiative source → normalized propagating graviton → distant resonant receiver construction.

Primary source: arXiv:2503.03585.

---

# 9. Miki, Li, and Chen 2026 — pulse/thermal/EB collision

**Daisuke Miki, Alfred Li, Yanbei Chen, “Amplification and generation bounds of gravity-induced entanglement in pulsed optomechanical systems,” arXiv:2605.26240 (2026).**

Their pulse protocol swaps optical states into and out of gravitationally interacting mechanical modes. They prove that, in their model, entanglement generation competes with thermal decoherence through the threshold

$$
\boxed{
g_G>2\gamma_mN_{\rm th}.}
$$

They also identify entanglement-annihilating and entanglement-breaking regimes controlled by accumulated thermal noise.

## Consequence

Do not claim novelty for

- pulse-based preparation/readout around gravitational dynamics;
- gravity-versus-thermal-decoherence thresholds;
- EB analysis of noisy gravitational oscillator channels.

## Remaining distinction

The gravitational interaction is between localized oscillator modes rather than a source-emitted travelling wavepacket with a separately normalized free-space capture stage.

Primary source: arXiv:2605.26240.

---

# 10. Yant and Blencowe 2025 — relativistic/QFT matter-model boundary

**Jackson Yant and Miles Blencowe, “An Operational Quantum Field Theoretic Model for Gravitationally Induced Entanglement,” arXiv:2503.20855 (2025).**

They formulate matter as excitations of a scalar quantum field and study linearized gravity in the **static limit**, deriving an operational GIE observable and relativistic corrections.

This is important for scope discipline: V5's elastic source is not a universal relativistic QFT matter model and should not be advertised as one.

At the same time, this work does not contain V5's propagating radiative source-output → noisy receiver chain.

Primary source: arXiv:2503.20855.

---

# 11. Feature-by-feature collision verdict

## Local branch preparation

Pieces exist in optomechanical state-swap literature and in Miki et al., but the particular V5 role is narrower: a branch-common local work mode prepares opposite coherent amplitudes of the **radiating conserved quadrupole** while returning branch common.

**Status:** no exact collision found in audited gravity papers.

## Explicit conserved finite-support radiator

Matsui requires a closed conserved source but leaves the experimental source trajectory/apparatus generic. V5 gives one explicit finite-spoke realization and propagates its support correction through linewidth and free-space capture.

**Status:** source principle occupied; explicit architecture/application not found.

## Emitted branch-difference graviton mode

Matsui fully occupies the underlying displacement/difference-mode mathematics.

**Status:** prior art. Use, cite, do not claim.

## Propagating causal field

Laga–Suyama establish the retarded coherent field; Trenggana–Zen establish delayed entanglement through propagating gravitons.

**Status:** prior art.

## Quantum resonant receiver

Toccacelo et al. explicitly give graviton–phonon beam-splitter dynamics and Markov thermal noise.

**Status:** prior art.

## Gravity as a non-EB channel

Mari et al. explicitly use non-entanglement-breaking gravitational communication as the criterion; Miki et al. study EB regimes.

**Status:** prior art.

## Source-output → receiver free-space normalization

No audited paper was found deriving the V5 decomposition

$$
\beta_{g,A}
\times
\eta_{\rm store}(R)
\times
\beta_{g,B}
\times
\text{temporal loading},
$$

with

$$
\eta_{\rm store}
=\frac{25\mathcal O}{16(kR)^2}
$$

and a controlled reciprocal-feedback correction.

**Status:** strongest remaining candidate contribution.

## Complete end-to-end condition

No audited source was found beginning with V5's local branch-common preparation and ending with the explicit source-reference NPT condition

$$
\eta_g\tau_{\rm full}(t)>m_B(t)
$$

after separately normalized source branching, radiation propagation/capture, and receiver noise.

The Gaussian inequality itself is prior art. The candidate contribution is the physical reduction of the complete radiative gravity architecture to it.

**Status:** plausible integrated contribution; priority not proven.

---

# 12. Strongest safe novelty language

Recommended manuscript language:

> We do not introduce a new criterion for Gaussian quantum communication, a new mechanism of graviton emission, or a new model of resonant graviton reception. Instead, we give an explicit source-resolved weak-gravity construction in which a locally prepared conserved mechanical source, the emitted propagating graviton mode, free-space mode capture, and a noisy resonant receiver are normalized within one calculation. This makes it possible to factor the end-to-end quantum capability into source branching, propagation/mode overlap, receiver branching, temporal loading, and thermal noise, while retaining separate error controls for finite source size, source preparation, and reciprocal backaction.

Even safer:

> To our knowledge after the targeted comparison summarized here, this complete normalization chain is not presented in the inspected literature.

Avoid:

> first quantum communication protocol using propagating gravitons.

Avoid:

> first causal gravitational entanglement result.

Avoid:

> first conserved quantum source of gravitons.

---

# 13. Publication verdict after this audit

## GO — but as a synthesis/normalization paper

The V5 manuscript still has a defensible center.

The paper becomes weak if framed around any single ingredient, because essentially every ingredient has close prior art.

The paper becomes strongest when framed around the statement:

$$
\boxed{
\text{the interfaces have been closed quantitatively.}
}
$$

The main product is the factorized end-to-end architecture

$$
\boxed{
\tau_{A\to B}^{\max}
\simeq
4e^{-2}
\beta_{g,A}
\eta_{\rm store}(R)
\beta_{g,B}
}
$$

for the optimized passive limit, together with

- the explicit local conserved source that defines \(\beta_{g,A}\);
- the audited radiative normalization defining \(\eta_{\rm store}\);
- the noisy resonant receiver defining \(\beta_{g,B}\) and \(m_B\);
- the exact/controlled finite-\(g\), finite-size, thermal, and feedback corrections.

This is a narrower claim than earlier versions of the project, but it is substantially harder to dismiss as merely juxtaposing unrelated formulas because every interface has now been derived and cross-checked.

---

# 14. Highest-value remaining literature work

Before submission, perform two further searches:

1. **Cascaded/circuit-QED style gravitational transducer papers** that may already multiply emitter branching, propagation efficiency, and receiver cooperativity in an equivalent way.
2. **Classical resonant gravitational-wave antenna reciprocity literature** for the exact aligned quadrupole absorption/storage normalization, especially whether the coefficient
   $$
   25/[16(kR)^2]
   $$
   is an immediate standard reciprocity result under different notation.

The second search is especially important because the \(25/16\) normalization is one of the most distinctive quantitative bridges remaining in V5.
