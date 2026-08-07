# Experiment 01 — Causal Transport of Quantum Branch Information by Gravity

**Status:** Working theoretical note / Gedanken experiment  
**Central question:** *Can gravity transmit information about a coherent spatial alternative without first turning that alternative into a classical fact?*  

---

## Abstract

Place a massive quantum system $A$ in a coherent spatial superposition,

$$
|+\rangle_A=\frac{|L\rangle+|R\rangle}{\sqrt 2},
$$

and place a second quantum system $B$ nearby. The essential question is not merely whether $A$ attracts $B$, but whether gravity can make the future of $B$ depend coherently on both alternatives $L$ and $R$. If the conditional probe states become distinguishable while the source remains coherent, the joint state becomes entangled. In the Newtonian limit the leading entangling interaction is not the uniform gravitational force but the tidal term

$$
H_{\rm ent}=\frac{2Gm_A m_B}{d^3}x_Ax_B,
$$

which couples the quantum position fluctuations of the two systems. A second prepared Schrödinger-cat state is therefore not conceptually necessary: one spatially coherent source and one ordinary quantum probe are sufficient in principle, because gravity itself can generate the conditional probe branches.

The relativistic extension changes the question again. A source-controlled change performed at $A$ cannot influence a distant probe before the future light cone of that operation reaches it. The relevant observable is therefore not the mere existence of correlations—quantum fields may possess spacelike vacuum correlations—but the change in a probe or joint witness caused by creating or modulating the source superposition. A successful experiment would ideally establish three properties simultaneously: branch information is transferred **coherently** rather than through irreversible measurement-and-feedback, **quantum mechanically** rather than through a non-entangling classical channel, and **causally** rather than through an instantaneous Newtonian potential. The resulting operational question is sharper than “is gravity quantum?”: **can the gravitational interaction act as a local quantum-information channel?**

This note develops that question from first principles, states what is already established in the literature, and identifies the remaining conceptual target rather than claiming novelty for known gravitational-entanglement protocols.

---

# 1. The experiment in one paragraph

Put one mass in two places coherently. Put another quantum system nearby in one ordinary state. If gravity responds only to an averaged classical mass distribution, the second system has one gravitational future. If gravity preserves the coherence of the two alternatives, the second system may instead have two conditional futures,

$$
|L\rangle|B_L\rangle+|R\rangle|B_R\rangle.
$$

If $B_L$ and $B_R$ become distinguishable without gravity first deciding whether $L$ or $R$ is real, the systems are entangled. A classical information channel can imitate the correct average force only by acquiring information and paying for it through decoherence or added noise; a coherent quantum interaction can correlate the alternatives without selecting one. General relativity then adds a second demand: the source-controlled branch information must not appear at a distant probe before the appropriate light-cone time. The Gedanken experiment therefore asks whether gravity can transmit **branch information coherently, reversibly, and causally**.

---

# 2. How to put a neutral mass into spatial superposition

The clean conceptual example is a neutral spin-carrying particle such as a neutron. Electrical charge is not required for Stern–Gerlach separation. What is required is a magnetic moment in an inhomogeneous magnetic field,

$$
U=-\boldsymbol{\mu}\cdot\mathbf B,
\qquad
\mathbf F=\nabla(\boldsymbol{\mu}\cdot\mathbf B).
$$

A spin state such as

$$
|+x\rangle=\frac{|\uparrow_z\rangle+|\downarrow_z\rangle}{\sqrt2}
$$

can therefore be converted coherently into a spin-position state,

$$
\frac{|L,\uparrow\rangle+|R,\downarrow\rangle}{\sqrt2}.
$$

Further coherent spin manipulation can, in principle, remove the spin label so that the center-of-mass state takes the idealized form

$$
|+\rangle_A=\frac{|L\rangle+|R\rangle}{\sqrt2}.
$$

The neutron is useful conceptually because it is neutral and quantum mechanically simple at the level relevant to the experiment. It is almost certainly a poor practical gravitational source because gravity scales with mass. The practical lesson is the reverse of the conceptual one:

> **Use the simplest system to understand the physics; use the largest controllable quantum mass to perform the experiment.**

The Gedanken experiment will therefore use an abstract neutral massive system $A$, while keeping the Stern–Gerlach picture as an intuitive way to understand the origin of the spatial superposition.

---

# 3. The first physical question: where is the gravitational source?

For a classical point mass at position $x_A$, Newtonian gravity gives

$$
U_G(x_A,x_B)=-\frac{Gm_A m_B}{|x_A-x_B|}.
$$

But the source is now in

$$
|+\rangle_A=\frac{|L\rangle+|R\rangle}{\sqrt2}.
$$

Three broad possibilities illustrate the conceptual conflict:

1. **Mean-field response.** Gravity is a single classical field sourced by an expectation-value mass density. The probe responds to an averaged source.
2. **Coherent conditional response.** The gravitational interaction preserves the alternatives and correlates them with different probe/field states.
3. **Fundamental decoherence or collapse.** The gravitational sector destroys the coherence between the alternatives.

The point of the thought experiment is to translate these verbal possibilities into different observables.

---

# 4. The minimal conditional Hamiltonian

Assume $A$'s two spatial branches are sufficiently well separated and remain approximately stationary during the interaction. Then the most general branch-conditioned probe Hamiltonian can be written

$$
\boxed{
H=|L\rangle\langle L|\otimes H_L+|R\rangle\langle R|\otimes H_R .
}
$$

Let the probe begin in a pure state $|\psi_B\rangle$. The initial state is

$$
|\Psi(0)\rangle=\frac{|L\rangle+|R\rangle}{\sqrt2}|\psi_B\rangle.
$$

After an interaction time $t$,

$$
|\Psi(t)\rangle
=\frac{|L\rangle U_L(t)|\psi_B\rangle+|R\rangle U_R(t)|\psi_B\rangle}{\sqrt2},
$$

where

$$
U_j(t)=e^{-iH_jt/\hbar}.
$$

Define the two conditional probe states

$$
|\psi_L\rangle=U_L|\psi_B\rangle,
\qquad
|\psi_R\rangle=U_R|\psi_B\rangle,
$$

and their overlap

$$
\boxed{
\Gamma(t)=\langle\psi_L|\psi_R\rangle
=\langle\psi_B|U_L^\dagger U_R|\psi_B\rangle.
}
$$

For this pure bipartite state,

$$
\boxed{|\Gamma|<1\quad\Longleftrightarrow\quad A\text{ and }B\text{ are entangled}.}
$$

The same number controls the interferometric visibility of the source:

$$
\boxed{V=|\Gamma|.}
$$

The reduced density matrix of $A$ is

$$
\rho_A=\frac12
\begin{pmatrix}
1&\Gamma^*\\
\Gamma&1
\end{pmatrix},
$$

with eigenvalues

$$
\lambda_\pm=\frac{1\pm|\Gamma|}{2}.
$$

Hence the source-probe entanglement entropy is

$$
S_A=h_2\!\left(\frac{1+|\Gamma|}{2}\right),
$$

where $h_2$ is the binary entropy. One overlap amplitude therefore measures three related ideas at once: distinguishability of the gravitational alternatives, loss of local interference, and source-probe entanglement.

---

# 5. What does the probe actually need to be quantum about?

Define

$$
\Delta H=H_R-H_L.
$$

For sufficiently short times,

$$
|\Gamma(t)|^2
=1-\frac{t^2}{\hbar^2}\operatorname{Var}_{\psi_B}(\Delta H)+O(t^3).
$$

Therefore entanglement begins to develop whenever

$$
\boxed{\operatorname{Var}_{\psi_B}(\Delta H)>0.}
$$

This is the conceptual resource statement:

> **The second system does not need to be prepared as a second macroscopic cat. It only needs quantum uncertainty in an observable on which the two gravitational alternatives act differently.**

The gravitational interaction can create the conditional probe branches dynamically.

---

# 6. Why the tidal field is the entangling part of Newtonian gravity

Let the equilibrium source-probe separation be $d$, and let their small displacements be $x_A$ and $x_B$. Then

$$
U_G=-\frac{Gm_A m_B}{d+x_B-x_A}.
$$

For $|x_A|,|x_B|\ll d$, expand:

$$
U_G\simeq
-\frac{Gm_A m_B}{d}
+\frac{Gm_A m_B}{d^2}(x_B-x_A)
-\frac{Gm_A m_B}{d^3}(x_B-x_A)^2.
$$

The constant and one-body terms cannot entangle the two systems. The leading cross term is

$$
\boxed{
H_{\rm ent}=\frac{2Gm_A m_B}{d^3}x_Ax_B.
}
$$

The relevant scaling is therefore $d^{-3}$, not the familiar inverse-square force law. This is physically significant. A uniform gravitational acceleration can be removed locally by going to free fall; a tidal field cannot. The leading entangling interaction is therefore associated with the spatial variation of the force—the Newtonian precursor of spacetime curvature.

If the source is a two-position system,

$$
x_A=\frac{\Delta x_A}{2}\sigma_z,
$$

then

$$
H_{\rm ent}=\frac{Gm_A m_B\Delta x_A}{d^3}\sigma_zx_B
=\frac{\delta F}{2}\sigma_zx_B,
$$

where the branch-to-branch force difference on $B$ is approximately

$$
\boxed{
\delta F=\frac{2Gm_A m_B\Delta x_A}{d^3}.
}
$$

Gravity has become a state-dependent force.

---

# 7. One cat and one oscillator

Let $B$ be a quantum harmonic oscillator initially in its ground state. Write

$$
x_B=x_{\rm zpf}(a+a^\dagger),
\qquad
x_{\rm zpf}=\sqrt{\frac{\hbar}{2m_B\omega}}.
$$

Then

$$
H_{\rm int}=\hbar g\,\sigma_z(a+a^\dagger),
$$

with

$$
\boxed{
g=\frac{\delta F\,x_{\rm zpf}}{2\hbar}.}
$$

Starting from

$$
|\Psi(0)\rangle=|+\rangle_A|0\rangle_B,
$$

the interaction produces, up to phases,

$$
\boxed{
|\Psi(t)\rangle
=\frac{|L\rangle|\alpha(t)\rangle+|R\rangle|-\alpha(t)\rangle}{\sqrt2},
}
$$

with

$$
\alpha(t)=\frac{g}{\omega}\left(1-e^{-i\omega t}\right).
$$

The probe was not initially a cat. Gravity created two conditional coherent states.

Their overlap is

$$
V(t)=|\langle-\alpha|\alpha\rangle|
=\exp[-2|\alpha(t)|^2],
$$

or

$$
\boxed{
V(t)=\exp\left[-\frac{8g^2}{\omega^2}
\sin^2\left(\frac{\omega t}{2}\right)\right].
}
$$

At half a mechanical period, the conditional oscillator states are maximally separated in phase space. At one full period,

$$
\alpha(2\pi/\omega)=0,
$$

and the source visibility revives. The sequence is

$$
\text{coherence}\rightarrow\text{entanglement}\rightarrow
\text{local visibility loss}\rightarrow\text{disentanglement}\rightarrow\text{revival}.
$$

This is a gravitational quantum-eraser picture: which-branch information is coherently written into the probe and later erased by unitary dynamics.

---

# 8. The classical information-channel dilemma

Suppose instead gravity is fundamentally a classical mediator. To apply a branch-dependent force, a classical channel must somehow acquire classical information about the source and use that information to act on the probe. Schematically,

$$
\text{measure }A\rightarrow\text{classical record}\rightarrow\text{force on }B.
$$

That creates a generic information-disturbance tradeoff. Strongly learning the source branch decoheres the source; weakly learning it preserves more coherence but makes the inferred force noisy. Classical measurement-and-feedback models of gravity therefore carry irreducible noise if they are required to reproduce Newtonian attraction while remaining non-entangling.

This idea was developed by Kafri, Taylor, and Milburn and has been generalized considerably. In 2026 Fabiano, Fujita, Matsumura, and Carney classified a broad family of non-quantized Newtonian models and derived minimum-noise conditions. For a hybrid two-state system plus mechanical oscillator initially in

$$
\frac{|L\rangle+|R\rangle}{\sqrt2}\otimes|0\rangle,
$$

they show that sufficiently low combined source-decoherence and probe-momentum-diffusion rates imply that the gravitational interaction is entangling. The precise inequality depends on their normalization and assumptions; the important conceptual point is model-independent in spirit:

> **A classical channel must learn and react. A coherent quantum interaction can correlate without learning.**

Visibility loss alone is therefore not sufficient evidence for nonclassical gravity. One must distinguish reversible entanglement from environmental decoherence and from classical stochastic forces.

---

# 9. Newtonian entanglement is still not the whole question

The effective Newtonian interaction

$$
-\frac{Gm_A m_B}{|\hat x_A-\hat x_B|}
$$

is instantaneous. It can be an excellent low-energy effective Hamiltonian, but it hides the causal mechanism of the interaction.

General relativity instead describes local spacetime dynamics. In weak-field language,

$$
g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu},
$$

and matter couples schematically through

$$
H_I=-\frac12\int d^3x\,h_{\mu\nu}(x)T^{\mu\nu}(x).
$$

The causal response of the field is governed by a retarded propagator. Schematically,

$$
D_R(x,x')\propto i\Theta(t-t')\langle[h(x),h(x')]\rangle.
$$

Microcausality requires the commutator to vanish for spacelike-separated events. Therefore a **source-controlled change** performed at $A$ cannot change an observable at a spacelike-separated $B$.

A crucial qualification is that quantum fields can possess vacuum correlations outside a light cone. Therefore the claim cannot simply be “there is no correlation or entanglement before $R/c$.” The operational statement is narrower and stronger:

$$
\boxed{
\text{A controllable operation at }A\text{ cannot alter local statistics at }B
\text{ before causal contact.}
}
$$

---

# 10. The light-cone quantum eraser

Place $A$ and $B$ a distance $R$ apart. At $t=0$, create or modulate the source superposition locally at $A$. Compare two experimental runs:

- **control:** the source operation is not performed;
- **signal:** the source is coherently split or its branch configuration is changed.

For an observable $O_B$, define

$$
\boxed{
\Delta O_B(t)=\langle O_B(t)\rangle_{\rm signal}-\langle O_B(t)\rangle_{\rm control}.
}
$$

A causal local theory requires

$$
\boxed{
\Delta O_B(t)=0\qquad\text{for }t<R/c,
}
$$

up to the finite spacetime support of the actual preparation and detector operations.

As an intuitive approximation, replace the instantaneous conditional force with a causal switching function,

$$
H_I(t)=\hbar g\,\chi(t-R/c)\,\sigma_z(a+a^\dagger),
$$

where $\chi$ vanishes before the retarded arrival. A sharp Heaviside step is only an idealization; a realistic field-theory calculation uses the retarded Green function and finite source/detector switching.

If one nevertheless uses the sharp idealization,

$$
\tau=(t-R/c)_+,
$$

then the oscillator amplitude becomes

$$
\alpha(\tau)=\frac{g}{\omega}\left(1-e^{-i\omega\tau}\right).
$$

Thus the source-controlled conditional displacement satisfies

$$
\alpha=0\qquad (t<R/c),
$$

and begins only after causal contact. The familiar entanglement/visibility cycle is shifted by the propagation delay.

The important experimental signature is not one measured delay but the distance scaling

$$
\boxed{
\frac{dt_{\rm onset}}{dR}=\frac1c.
}
$$

A family of probes at different $R$ would trace the propagation of the source-controlled quantum interaction through spacetime.

---

# 11. What would constitute the strongest observation?

The Gedanken experiment separates three logically distinct properties.

## 11.1 Causal

The source-controlled response follows the spacetime light cone rather than an instantaneous Newtonian update.

## 11.2 Coherent

Branch information is written into another quantum system without first selecting a definite branch, and can in principle be erased/recombined.

## 11.3 Nonclassical / entangling

The joint behavior violates an appropriate non-entangling classical-channel bound or directly demonstrates entanglement.

None of the three alone is enough for the strongest conclusion:

- **retardation alone** is expected in classical general relativity;
- **visibility loss alone** can be ordinary noise;
- **Newtonian entanglement alone** does not by itself establish every property usually associated with a propagating graviton.

The conjunction is the conceptual target:

$$
\boxed{
\text{retarded}+\text{coherent}+\text{entangling}.
}
$$

Operationally, that would support the statement that the gravitational interaction can function as a **local quantum-information channel**.

---

# 12. What is actually being transported?

The useful primitive is not “force” but **branch information**.

The source begins with a coherent alternative,

$$
|L\rangle+|R\rangle.
$$

A local quantum gravitational description suggests that the nearby field becomes conditionally correlated with that alternative before a distant probe does. Schematically,

$$
|L\rangle|g_L\rangle+|R\rangle|g_R\rangle.
$$

After the causal influence reaches $B$,

$$
|L\rangle|g_L\rangle|B_L\rangle
+|R\rangle|g_R\rangle|B_R\rangle.
$$

The field acts as an information-bearing mediator between source and probe. This motivates a deeper question than the usual yes/no question about quantization:

> **Can one formulate an operational measure of source-branch information carried by the gravitational field whose source-controlled propagation respects relativistic causality?**

A naive local “information density” should not be assumed: entanglement and mutual information are not conserved local currents in the same way as electric charge. A rigorous formulation would need to be built from operationally accessible algebras, conditional channels, relative entropy, mutual information, or related quantum-information quantities compatible with gauge constraints and gravitational dressing.

This is one place where a genuinely new theoretical contribution may exist, but it has not been established here.

---

# 13. The conceptual statement

The entire Gedanken experiment can be compressed to this:

> **Put a mass in two places and ask what reaches a distant quantum probe. If gravity responds only to an averaged classical source, the probe has one gravitational future. If gravity preserves the coherence of the alternatives, the probe may acquire two conditional futures. When those futures become distinguishable without either source alternative becoming a classical fact, gravity has transferred branch information by entangling the systems. A purely classical information channel cannot perform the same task reversibly without paying an irreducible price in decoherence or force noise. General relativity adds one further demand: the change caused by creating the source alternative cannot appear outside its future light cone. The sharp question is therefore not simply whether gravity is quantum, but whether gravity can transmit branch information coherently, nonclassically, and causally.**

Or more compactly:

$$
\boxed{
\text{Can spacetime act as a causal quantum-information channel?}
}
$$

---

# 14. What this experiment does **not** establish

The argument should not be overstated.

1. **A single-superposed-source architecture is not novel.** Pesci and Pieri (2023) explicitly proposed testing the nonclassicality of gravity using one delocalized source and one harmonically trapped test mass.
2. **Gravity-mediated entanglement is not a new concept.** Bose et al. and Marletto–Vedral gave the modern landmark proposals in 2017.
3. **Local/retarded gravitational entanglement has already been studied.** Christodoulou et al. derived locally mediated entanglement in linearized quantum gravity, and later work has sharpened the role of retardation.
4. **A single superposed source can support other nonclassical witnesses.** Saldanha, Marletto, and Vedral (2026) proposed a postselected repulsive-gravity witness using one spatially superposed source and a probe wavepacket.
5. **Entanglement does not automatically equal direct graviton detection.** The interpretation depends on locality, mediator assumptions, subsystem definitions, and the field-theoretic description.
6. **The sharp retarded oscillator Hamiltonian used above is pedagogical.** A serious relativistic calculation must use finite switching functions, gauge-consistent observables, gravitational dressing, and the relevant retarded/noise kernels.

The candidate contribution of this project is therefore **not** to rediscover BMV or the one-source geometry. It is to search for the cleanest operational synthesis of three constraints—causality, coherence, and nonclassical channel capacity—and, if possible, to derive a new inequality or information-flow statement that separates a local quantum gravitational mediator from the most general admissible classical alternatives.

---

# 15. Candidate paper-level research program

A publishable theoretical paper would need to go beyond the Gedanken narrative. The strongest route currently appears to be:

### A. Define the classical competitor class

State explicitly the allowed classical gravitational channels: locality/causality assumptions, stochasticity, measurement-feedback structure, Markovian or non-Markovian behavior, conservation laws, and the requirement to recover Newtonian gravity on average.

### B. Replace the sharp retarded force with a covariant kernel

Derive the source-probe channel from linearized gravity using a retarded Green function and finite switching functions. Keep the response kernel and fluctuation/noise kernel separate.

### C. Construct a control-subtracted quantum witness

Use a quantity that isolates changes caused by the source operation rather than preexisting field-vacuum correlations. Candidate observables include a distance-resolved entanglement witness, channel negativity, conditional probe fidelity, or a relative-entropy/channel-discrimination measure.

### D. Derive a causal classical bound

Find an inequality that every admissible local classical gravitational channel must satisfy, combining source decoherence, probe diffusion/noise, and causal onset.

### E. Show a quantum-field violation

Calculate the same quantity in linearized quantum gravity and identify a parameter regime in which the quantum prediction violates the classical bound while remaining inside the light cone.

A result of the schematic form

$$
\boxed{
\mathcal W_{\rm causal}[A,B]
\leq \mathcal B_{\rm classical}
}
$$

for every specified classical mediator, together with

$$
\boxed{
\mathcal W_{\rm QG}>\mathcal B_{\rm classical},
}
$$

would convert the present Gedanken experiment into a falsifiable theorem.

---

# 16. Known literature / novelty boundary

The following papers define the immediate conceptual neighborhood and should be treated as prior work rather than rediscovered results.

1. **R. P. Feynman and the 1957 Chapel Hill discussion.** Feynman used macroscopic quantum-superposition Gedanken experiments to argue that a gravitational field associated with alternative mass configurations should itself require amplitudes. See *The Role of Gravitation in Physics: Report from the 1957 Chapel Hill Conference* (DeWitt/Rickles edition) and later historical analyses of Feynman's argument.
2. **S. Bose et al., “Spin Entanglement Witness for Quantum Gravity,” Phys. Rev. Lett. 119, 240401 (2017).** DOI: https://doi.org/10.1103/PhysRevLett.119.240401
3. **C. Marletto and V. Vedral, “Gravitationally Induced Entanglement between Two Massive Particles is Sufficient Evidence of Quantum Effects in Gravity,” Phys. Rev. Lett. 119, 240402 (2017).** DOI: https://doi.org/10.1103/PhysRevLett.119.240402
4. **D. Kafri, J. M. Taylor, and G. J. Milburn, classical-channel gravity / noise analyses (2014–2015).** See arXiv:1401.0946 and related work.
5. **D. L. Danielson, G. Satishchandran, and R. M. Wald, “Gravitationally Mediated Entanglement: Newtonian Field versus Gravitons,” Phys. Rev. D 105, 086001 (2022).** arXiv:2112.10798.
6. **M. Christodoulou et al., “Locally Mediated Entanglement in Linearized Quantum Gravity,” Phys. Rev. Lett. 130, 100202 (2023).** DOI: https://doi.org/10.1103/PhysRevLett.130.100202
7. **A. Pesci and P. Pieri, “Testing the nonclassicality of gravity with the field of a single delocalized mass,” Phys. Rev. A 108, 062801 (2023).** DOI: https://doi.org/10.1103/PhysRevA.108.062801
8. **N. Mitrakos, M. Papageorgiou, T. R. Perche, and M. Christodoulou, “When does entanglement through gravity imply gravitons?” (2026).** arXiv:2601.03214. The paper emphasizes that detecting retardation in gravity-mediated entanglement would strengthen the inference toward gravitons.
9. **P. L. Saldanha, C. Marletto, and V. Vedral, “Repulsive Gravitational Force as a Witness of the Quantum Nature of Gravity” (2026).** arXiv:2602.12266.
10. **G. Fabiano, T. Fujita, A. Matsumura, and D. Carney, “Minimal noise in non-quantized gravity” (2026).** arXiv:2603.26075. This work derives systematic noise thresholds for broad non-entangling Newtonian models, including a hybrid two-state/mechanical system.

Because this is an active field, any eventual submission should include a fresh literature review immediately before claiming novelty.

---

# 17. Key equations to keep on the blackboard

### Spatial alternative

$$
|+\rangle_A=\frac{|L\rangle+|R\rangle}{\sqrt2}
$$

### Conditional gravitational evolution

$$
H=|L\rangle\langle L|\otimes H_L+|R\rangle\langle R|\otimes H_R
$$

### Probe-history overlap

$$
\Gamma=\langle\psi_B|U_L^\dagger U_R|\psi_B\rangle
$$

### Pure-state entanglement criterion

$$
|\Gamma|<1
$$

### Newtonian entangling / tidal term

$$
H_{\rm ent}=\frac{2Gm_A m_B}{d^3}x_Ax_B
$$

### Source-qubit conditional force

$$
H_{\rm ent}=\frac{\delta F}{2}\sigma_zx_B,
\qquad
\delta F=\frac{2Gm_A m_B\Delta x_A}{d^3}
$$

### Oscillator coupling

$$
H_{\rm int}=\hbar g\sigma_z(a+a^\dagger),
\qquad
g=\frac{\delta F x_{\rm zpf}}{2\hbar}
$$

### Conditional coherent displacement

$$
\alpha(t)=\frac{g}{\omega}(1-e^{-i\omega t})
$$

### Visibility

$$
V=e^{-2|\alpha|^2}
$$

### Causal control subtraction

$$
\Delta O_B(t)=\langle O_B\rangle_{\rm signal}-\langle O_B\rangle_{\rm control}
$$

### Relativistic requirement

$$
\Delta O_B(t)=0\quad\text{outside the future light cone of the source operation}
$$

---

# 18. Final compressed version

**A mass is placed in a coherent superposition of two locations. Gravity must somehow make those alternatives relevant to a distant quantum probe. If gravity is only an averaged classical field, the probe has one future. If gravity is a coherent mediator, the probe can have two conditional futures while neither source alternative is selected, and the systems become entangled. The leading Newtonian interaction that can do this is the tidal coupling $2Gm_A m_Bx_Ax_B/d^3$, not the uniform force. A classical channel that determines which force to apply must acquire classical information and therefore pay an irreducible price in decoherence or noise; a quantum channel can correlate without deciding. Relativity then requires the source-controlled change to propagate locally: vacuum correlations may exist outside the light cone, but information about the operation that created the superposition cannot. The strongest question is therefore whether gravity can transmit branch information coherently, below classical noise bounds, and with relativistic causal propagation. In operational terms: can spacetime act as a causal quantum-information channel?**