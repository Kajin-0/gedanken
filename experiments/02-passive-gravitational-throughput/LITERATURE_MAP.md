# Literature Map — Passive Gravitational Throughput

## Purpose

This file tracks nearby results that could collide with, constrain, or sharpen Experiment 02. It is not yet a novelty claim.

The current collision target is deliberately narrow:

```text
known passive linear-network machinery
+ microscopic matter-to-graviton coupling
+ mass-quadrupole spectral resource at BOTH endpoints
+ normalized propagating TT channel
+ end-to-end integrated transfer cut set
+ quantum-information corollary.
```

Several ingredients of this chain are old and must be credited explicitly. In particular, neither passive Gramian theory nor the Q-independence of an integrated resonant gravitational response is new here.

---

## 1. Historical resonant-mass absorption cross sections

### Paik and Wagoner — cylindrical gravitational-wave antenna

**H. J. Paik and R. V. Wagoner, “Calculation of the absorption cross section of a cylindrical gravitational-wave antenna,” Phys. Rev. D 13, 2694 (1976).**

This is foundational prior art for resonant-mass gravitational absorption. It computes the absorption cross section of Weber-type cylindrical antennas from their elastic eigenmodes.

The broader resonant-mass literature subsequently uses the **frequency-integrated absorption cross section** as the natural measure of coupling to a gravitational-wave packet. This quantity removes the apparent advantage of arbitrarily large Q: the resonant peak grows as the linewidth shrinks, leaving a finite integrated oscillator-strength-like response.

Later reviews explicitly write the integrated cross section of a bar antenna and show that adding a resonant transducer redistributes that integrated response among coupled normal modes rather than generating unlimited gravitational coupling strength.

**Novelty consequence for Experiment 02:**

> The statement “high Q cannot increase the integrated gravitational response without limit” is historical gravitational-antenna physics and is **not** a novelty claim of Experiment 02.

Experiment 02 must instead ask what happens when this response logic is closed **end to end**, with both matter-gravity interfaces and the propagating quantum channel retained in one passive cut-set bound.

Primary record: Phys. Rev. D 13, 2694 (1976).

---

## 2. Gravitational absorption expressed through material response

### Srivastava, Widom, Pizzella — metallic antenna susceptibility

**Y. N. Srivastava, A. Widom, and G. Pizzella, “Electronic Enhancements in the Detection of Gravitational Waves by Metallic Antennae,” arXiv:gr-qc/0302024 (2003).**

This is close prior art to the susceptibility/material-response side of Experiment 02. It expresses gravitational-wave absorption and scattering in terms of the dynamical elastic response of matter and develops a Kubo/viscosity description of the antenna.

The important lesson is that a gravitational absorption cross section can be written directly in terms of an **imaginary material response function**, rather than only as a single mechanical-mode linewidth.

This means a future non-Markov susceptibility extension of Experiment 02 cannot be presented as conceptually unprecedented. The possible new step would be to combine such a material-response description with the two-ended passive cut set and normalized TT propagation channel.

URL: https://arxiv.org/abs/gr-qc/0302024

### Widom, Drosdoff, Sivasubramanian, Srivastava

**“Electronic Detection of Gravitational Disturbances and Collective Coulomb Interactions,” arXiv:gr-qc/0402097 (2004).**

This work likewise connects graviton absorption cross sections to nonlocal viscous response functions of metallic crystals and emphasizes the need for the full microscopic stress response.

URL: https://arxiv.org/abs/gr-qc/0402097

### Branchina, Gasparini, Rissone

**“Electronic contribution to the oscillations of a gravitational antenna,” Phys. Rev. D 70, 024004 (2004), arXiv:gr-qc/0402048.**

This provides a microscopic Hamiltonian treatment of gravitational antenna response and is relevant to any claim about whether electronic or mechanical sectors dominate a material coupling resource.

**Novelty consequence:** the material-response bridge must be framed as a particular **sum-rule closure of an endpoint resource used in an end-to-end theorem**, not as the invention of susceptibility-based gravitational absorption.

---

## 3. Continuous-time quantum capacity of transducers

**C.-H. Wang, F. Li, and L. Jiang, “Quantum capacities of transducers,” Nature Communications 13, 6698 (2022).**

Primary role for Experiment 02:

- establishes a clean continuous-time capacity language for frequency-dependent bosonic transducers;
- defines one-way and two-way pure-loss capacities by integrating per-frequency channel capacities over `d omega / 2 pi`;
- shows that efficiency, bandwidth, and noise should not be collapsed into peak efficiency;
- derives a capacity ceiling controlled by a physical coupling scale for generic coupled-bosonic transducers.

Key distinction:

Their resource ceiling is a transducer coupling scale supplied as part of the device model. Experiment 02 attempts to derive the **gravity-specific endpoint coupling resource itself** from mass-quadrupole spectral weight and then place two such resources on opposite sides of a propagating gravitational channel.

URL: https://www.nature.com/articles/s41467-022-34373-8

---

## 4. Passive efficiency-bandwidth limits and resource-assisted escape

**H. Shi and Q. Zhuang, “Overcoming the fundamental limit of quantum transduction via intraband entanglement,” Optica Quantum 2, 475 (2024), arXiv:2404.09441.**

This work explicitly studies a frequency-integrated transduction efficiency and derives passive architecture limits for electro-optic/electro-optomechanical transducers, then shows how an additional nonclassical resource can surpass them.

Key distinction:

Its bound is set by the couplings and pump resources of those architectures. Experiment 02 seeks a passive **gravitational** material-resource ceiling derived from mass quadrupole response.

This paper strongly supports separating a passive gravitational theorem from a later “what physical resource beats it?” paper.

URL: https://arxiv.org/abs/2404.09441

---

## 5. Bandwidth-and-time-limited quantum communication

**A. Gandotra, Z. Wang, A. A. Clerk, and L. Jiang, “Quantum communication over bandwidth-and-time-limited channels,” Phys. Rev. A 113, 032616 (2026), arXiv:2502.08831.**

This work warns that finite signal duration and finite bandwidth cannot always be treated as independent asymptotic frequency channels and derives optimal temporal modes for finite-time pure-loss channels.

Implication:

`Gamma_coh` is best regarded as an asymptotic continuous-frequency response quantity. A finite-duration communication theorem may require singular temporal modes rather than naive mode counting.

URL: https://arxiv.org/abs/2502.08831

---

## 6. Passive linear quantum input-output formalism

### Guță and Yamamoto

**M. Guță and N. Yamamoto, “System identification for passive linear quantum systems,” Phys. Rev. A 89, 032103 (2014), arXiv:1303.3771.**

This establishes the standard passive bosonic realization

```math
A=-i\Omega-\frac12C^\dagger C
```

and transfer matrix

```math
\Xi(s)=I-C(sI-A)^{-1}C^\dagger,
```

with complete real-frequency scattering unitary when all passive channels are retained.

URL: https://arxiv.org/abs/1303.3771

### Techakesari and Nurdin

**P. Techakesari and H. I. Nurdin, “On the quasi-balanceable class of linear quantum stochastic systems,” Automatica 78, 272–281 (2017); arXiv:1408.1855.**

For an asymptotically stable completely passive linear quantum stochastic system, the controllability Gramian is the identity,

```math
P=I.
```

That is exactly the full-channel Gramian fact used in Experiment 02.

> **The identity `P=I`, passive scattering unitarity, and the underlying Gramian/H2 machinery are established mathematics and are not part of the novelty claim.**

Experiment 02 uses this known structure to form a gravitational-port cut set and then closes that abstract resource using microscopic gravitational physics.

URL: https://arxiv.org/abs/1408.1855

Related physical-realizability literature: A. Kh. Sichani and I. R. Petersen, arXiv:1609.07595.

---

## 7. Passive matching and scattering-sum-rule analogies

Bode–Fano and related passive causal bounds already establish generic response-bandwidth tradeoffs in electromagnetic networks. Time modulation/nonstationarity is a known route around passive time-invariant limits.

A recent acoustic result, **“Acoustic Analogy of Quantum Baldin Sum Rule for Optimal Causal Scattering,” Phys. Rev. Lett. 136, 226902 (2026),** is especially relevant mathematically because it converts a spectral sum rule into an integrated scattering bound.

These analogies mean Experiment 02 should avoid broad claims such as “the first efficiency-bandwidth theorem” or “a new universal sum-rule method.”

---

## 8. Existing gravitational quantum-channel and transducer work

Experiment 02 also inherits the V7 literature on:

- propagating-graviton entanglement;
- graviton-sensitive receivers;
- gravity-mediated Gaussian quantum channels;
- photon-graviton and related transduction proposals;
- weak graviton absorption by ordinary bound matter.

The targeted search performed for Experiment 02 has not yet found a paper that closes **both passive matter interfaces plus propagating TT geometry plus an integrated quantum-transfer metric** in one theorem. This is a negative search result, not proof of priority.

---

## 9. Current novelty status

**NARROWED / PROMISING / UNVERIFIED — DO NOT CLAIM PRIORITY.**

### Explicitly not new

- resonant gravitational absorption cross sections;
- the use of an integrated gravitational absorption cross section;
- the cancellation of resonant Q enhancement against shrinking bandwidth in an integrated response;
- susceptibility/Kubo descriptions of gravitational absorption by matter;
- passive linear quantum input-output theory;
- the complete passive Gramian identity `P=I`;
- continuous-time quantum-capacity integrals;
- generic passive transducer efficiency-bandwidth limitations;
- quadrupole sum rules by themselves.

### Potentially distinctive conjunction

```text
historical one-sided integrated gravitational response
+ known passive quantum-network cut-set machinery
+ microscopic matter-to-graviton port factorization
+ mass-quadrupole EWSR resource at source AND receiver
+ compact TT propagation singular-value ceiling
+ end-to-end integrated coherent-transfer theorem
+ pure-loss quantum-capacity corollary.
```

A restrained future manuscript claim could be:

> We extend the one-sided integrated-response viewpoint familiar from resonant gravitational antennas to an end-to-end passive quantum-transduction setting in which both matter-gravity interfaces and the propagating TT channel are bounded explicitly.

Or, more technically:

> We combine established passive linear-system identities with microscopic quadrupole spectral and propagation bounds to derive an end-to-end frequency-integrated ceiling for direct passive gravitational transduction between compact matter systems.

The remaining novelty question is whether this **two-ended closure** has already appeared under different gravitational-antenna, scattering, or network language.
