# Initial Novelty Sweep — Experiment 02

## Status

**CORE Q-CANCELLATION IS PRIOR ART; TWO-ENDED QUANTUM CUT-SET COLLISION NOT FOUND — NO PRIORITY CLAIM**

This note records the current novelty state after a deeper literature pass. The result is more constrained than the first sweep.

---

## 1. Important collision found: integrated gravitational response is historical

Resonant-mass gravitational-wave antenna theory has long used absorption cross sections and their frequency integrals as measures of coupling to an incident gravitational wave.

A foundational source is:

**H. J. Paik and R. V. Wagoner, “Calculation of the absorption cross section of a cylindrical gravitational-wave antenna,” Phys. Rev. D 13, 2694 (1976).**

Later resonant-mass literature explicitly treats the **integrated absorption cross section** of bars and spheres. In this language, increasing mechanical Q raises the resonant peak while narrowing the response, so the integrated gravitational coupling is controlled by oscillator strength/material parameters rather than growing without limit with Q.

### Consequence

The following is **not new** and must not be sold as the Experiment 02 result:

```text
high Q improves peak response but not the total frequency-integrated
passive gravitational response without limit.
```

This historical result is conceptually close to the first intuition that motivated Experiment 02.

---

## 2. Material susceptibility is also established gravitational-antenna language

**Y. N. Srivastava, A. Widom, and G. Pizzella, “Electronic Enhancements in the Detection of Gravitational Waves by Metallic Antennae,” arXiv:gr-qc/0302024 (2003)** expresses gravitational absorption/scattering in terms of dynamical elastic response and Kubo-type material susceptibilities.

Related work by Widom et al. (arXiv:gr-qc/0402097) connects graviton absorption to nonlocal viscous response, while Branchina, Gasparini, and Rissone (Phys. Rev. D 70, 024004; arXiv:gr-qc/0402048) gives a microscopic Hamiltonian treatment of gravitational antenna response.

### Consequence

A future arbitrary-susceptibility reformulation would be an extension of established gravitational-response language, not a conceptual first. The novelty would have to lie in the **end-to-end resource inequality** built on top of it.

---

## 3. Passive network mathematics is established

The passive bosonic input-output form used here is standard. Guță and Yamamoto (2014) give the passive transfer representation, and Techakesari and Nurdin (2017; arXiv:1408.1855) establish that the controllability Gramian is the identity for asymptotically stable completely passive linear quantum systems.

### Consequence

The passive Gramian/H2 machinery in Experiment 02 is a tool, not the physics novelty.

---

## 4. Integrated quantum-transducer metrics are established

Wang, Li, and Jiang (Nature Communications 13, 6698, 2022) formulate continuous-time quantum capacities of transducers as frequency integrals of per-frequency channel capacities.

Shi and Zhuang (Optica Quantum 2, 475, 2024; arXiv:2404.09441) derive passive efficiency-bandwidth limitations for specific quantum-transducer architectures and show that additional entanglement resources can overcome them.

### Consequence

Neither `integrated transmissivity`, `efficiency-bandwidth product`, nor `continuous-time capacity` is new terminology or methodology here.

---

## 5. Existing gravitational quantum-channel literature

The closest gravitational-QI works inspected still address different cuts through the problem:

- gravity-mediated Gaussian quantum channels and entanglement-breaking behavior;
- propagating-graviton entanglement;
- quantum-state characterization of an already incident gravitational field;
- photon-graviton or related transduction;
- detector sensitivity and physical coupling limits.

No inspected source in the current search closed the same chain

```text
source passive matter resource
-> gravitational emission port
-> normalized propagating TT channel
-> receiver passive matter resource
-> integrated end-to-end coherent transfer
-> capacity corollary.
```

This remains a negative search result, not proof of priority.

---

## 6. Current defensible novelty target

The potentially distinctive result is now much narrower and clearer:

> **A two-ended passive gravitational transduction cut set.** Established passive-network identities are combined with microscopic mass-quadrupole spectral bounds at both interfaces and with the normalized TT propagation singular value to bound the frequency-integrated source-to-receiver coherent transfer.

In the narrowband compact-quadrupole wave zone, the present theorem reduces to

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega^2}{12c^3R^2}
\min(\langle I_A\rangle,\langle I_B\rangle).
}
```

The theorem's possible value is therefore **not** that it discovers an efficiency-bandwidth tradeoff. It is that it closes the historical one-sided response problem into an end-to-end quantum/passive-network inequality with both gravitational interfaces explicit.

---

## 7. Strongest restrained future framing

Good:

> Resonant-mass antenna theory already shows that integrated gravitational absorption is controlled by oscillator strength rather than by Q alone. We ask the corresponding end-to-end question for passive quantum transduction: when both matter-gravity interfaces and the propagating TT channel are explicit, what integrated coherent transfer can any compact passive linear matter link support?

Also good:

> We combine established passive-system identities with quadrupole spectral and propagation bounds to derive a two-ended frequency-integrated ceiling for direct passive gravitational transduction.

Avoid:

- “first gravitational efficiency-bandwidth bound”;
- “new Q-independent gravitational response law”;
- “new passive-network theorem”;
- “universal gravitational quantum capacity limit”;
- “all passive matter.”

---

## 8. Remaining collision risks before manuscript drafting

The highest-risk hidden prior art is now:

1. a historical **two-antenna** gravitational reciprocity/transfer calculation that already combines source and receiver integrated cross sections;
2. a general multiport H2/scattering theorem that makes the exact gravitational cut-set corollary nearly immediate;
3. a gravitational oscillator-strength or antenna sum rule already written explicitly as a source-to-receiver transfer ceiling;
4. a recent quantum-transducer paper that specializes a general capacity cut set to gravitational channels.

The next literature pass should target these four possibilities rather than repeating broad “gravitational quantum communication” searches.

---

## 9. Current judgment

The historical collision **weakens the easy novelty story but strengthens the research direction**. It removes the temptation to oversell the Q tradeoff and leaves a cleaner question:

```text
Can historical one-sided integrated gravitational response theory be closed
into a rigorous two-ended passive quantum-transduction bound?
```

The current derivation says yes within the compact passive linear-bosonic wave-zone class. Whether that closure is publication-level novel remains the key unresolved literature question.
