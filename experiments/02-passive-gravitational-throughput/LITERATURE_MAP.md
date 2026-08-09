# Literature Map — Passive Gravitational Throughput

## Purpose

This file tracks nearby results that could collide with, constrain, or sharpen Experiment 02. It is not yet a novelty claim.

The central collision target is:

```text
passive matter gravitational spectral weight
+ propagating TT gravity
+ end-to-end efficiency/rate tradeoff
+ integrated coherent-transfer or capacity bound
```

A paper that derives only a generic transducer efficiency-bandwidth limit, only a gravitational absorption cross section, or only a quantum-capacity integral is relevant prior art but not automatically the same theorem.

---

## 1. Continuous-time quantum capacity of transducers

**C.-H. Wang, F. Li, and L. Jiang, “Quantum capacities of transducers,” Nature Communications 13, 6698 (2022).**

Primary role for Experiment 02:

- establishes a clean continuous-time capacity language for frequency-dependent bosonic transducers;
- defines one-way and two-way pure-loss capacities by integrating per-frequency channel capacities over `d omega / 2 pi`;
- shows that efficiency, bandwidth, and noise should not be collapsed into a peak-efficiency number;
- derives a capacity ceiling set by a physical coherent-coupling scale for a generic coupled-bosonic-chain architecture.

Key distinction:

The physical constraint there is a bounded transducer coupling rate `g_max`. Experiment 02 seeks a **gravity-specific passive matter bound on the available coupling spectral weight itself**, using quadrupole response and linearized gravity.

URL: https://www.nature.com/articles/s41467-022-34373-8

---

## 2. Passive efficiency-bandwidth product and active/entanglement-assisted escape

**H. Shi and Q. Zhuang, “Overcoming the fundamental limit of quantum transduction via intraband entanglement,” Optica Quantum 2, 475 (2024), arXiv:2404.09441.**

Primary role:

- explicitly uses a frequency-integrated transduction efficiency as an efficiency-bandwidth product;
- derives a passive/non-entanglement-assisted ceiling for specific cavity electro-optical/electro-optomechanical architectures;
- shows that an additional nonclassical resource can surpass the passive limit.

Key distinction:

Its bound is set by nonlinear coupling and pump resources in those transducer architectures. The gravitational target would instead derive the passive interface resource ceiling from mass-quadrupole spectral weight.

This paper strongly supports separating the passive theorem from a later “what resource beats it?” paper.

URL: https://arxiv.org/abs/2404.09441

---

## 3. Bandwidth-and-time-limited quantum communication

**A. Gandotra, Z. Wang, A. A. Clerk, and L. Jiang, “Quantum communication over bandwidth-and-time-limited channels,” Phys. Rev. A 113, 032616 (2026), arXiv:2502.08831.**

Primary role:

- warns that finite signal duration and finite bandwidth cannot always be treated as independent asymptotic frequency channels;
- derives optimal encoding/decoding modes for finite-time pure-loss channels, including Lorentzian spectra.

Implication for Experiment 02:

A long-time continuous-frequency metric is appropriate as an asymptotic response bound, but a finite-protocol operational theorem may require singular temporal modes rather than naive mode-counting by `B`.

This reinforces using a spectral integral as the primary physical quantity and treating `B tau` as a single-resonance shorthand only.

URL: https://arxiv.org/abs/2502.08831

---

## 4. Bode–Fano / passive matching analogy

The Bode–Fano criterion and related causal sum-rule bounds establish efficiency-bandwidth tradeoffs for passive linear time-invariant matching and scattering systems.

A useful recent example is:

**X. Yang, E. Wen, and D. F. Sievenpiper, “Broadband Time-Modulated Absorber beyond the Bode-Fano Limit for Short Pulses by Energy Trapping,” Phys. Rev. Applied 17, 044003 (2022).**

Role:

- conceptual analogy only at present;
- indicates that time modulation / nonstationarity is a known route around passive time-invariant matching bounds;
- suggests possible mathematical tools for the later susceptibility/scattering theorem.

Do not imply that Experiment 02 is simply a gravitational Bode–Fano theorem unless an actual analytic mapping is derived.

---

## 5. General scattering sum-rule analogy

A 2026 acoustic result derives a universal causal scattering sum rule that links integrated extinction to static material properties:

**“Acoustic Analogy of Quantum Baldin Sum Rule for Optimal Causal Scattering,” Phys. Rev. Lett. 136, 226902 (2026).**

Role:

This is relevant because Experiment 02 is also trying to convert a positive spectral sum rule into an integrated passive scattering/transfer bound. The mathematical analogy may be useful even though the physical channel is different.

This paper should be inspected closely before any novelty statement using words such as “universal sum rule” or “fundamental response bound.”

---

## 6. V7 inherited gravitational prior art

Experiment 02 inherits, but does not re-audit yet, the V7 references on:

- passive quadrupole energy-weighted sum rules;
- graviton absorption by ordinary bound matter;
- graviton transduction / resonant gravitational receivers;
- propagating gravitational quantum channels.

Before manuscript drafting, the prior-art search must be repeated with the new collision target:

```text
(gravity OR graviton OR gravitational wave)
AND
(sum rule OR oscillator strength OR susceptibility OR passivity)
AND
(bandwidth OR throughput OR integrated transmission OR capacity OR transduction)
```

---

## 7. Current novelty status

**UNKNOWN / DO NOT CLAIM PRIORITY.**

What appears potentially distinctive is not the generic idea that efficiency trades against bandwidth. That is established transducer physics.

The possible new result is specifically:

> deriving a passive gravitational end-to-end rate/response ceiling from the positive mass-quadrupole spectral weight of both material interfaces and the TT propagation channel.

That claim remains unverified until the susceptibility theorem is proved and a dedicated gravity-specific literature sweep is complete.
