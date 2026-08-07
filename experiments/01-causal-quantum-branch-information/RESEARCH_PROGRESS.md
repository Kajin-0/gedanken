# Research Progress — Experiment 01

**Experiment:** Causal Transport of Quantum Branch Information by Gravity  
**Status:** Active theoretical development  
**Purpose:** Preserve the strongest insights that emerged after the first working paper draft while keeping tentative novelty claims separate from established results.

---

## 1. Current conceptual core

The experiment has evolved from the question

> What gravitational field belongs to a mass in spatial superposition?

into the sharper operational question

> **Can gravity transfer branch distinguishability from a coherently delocalized source to a distant quantum probe without converting the branch into an irreversible classical record, and while respecting relativistic causality?**

The relevant three-party structure is

$$
A \rightarrow g \rightarrow B,
$$

where

- $A$ is the spatially superposed source,
- $g$ denotes the gravitational mediator/field,
- $B$ is the quantum probe.

This is conceptually stronger than treating the problem only as an effective $A$-$B$ Newtonian interaction.

---

## 2. Branch information can reside in both the probe and the field

For the simplest conditional pure-state model,

$$
|\Psi\rangle
=
\frac{
|L\rangle|B_L\rangle|g_L\rangle
+
|R\rangle|B_R\rangle|g_R\rangle
}{\sqrt2},
$$

define the conditional-state overlaps

$$
s_B=|\langle B_L|B_R\rangle|,
$$

and

$$
s_g=|\langle g_L|g_R\rangle|.
$$

The source interference visibility is then

$$
\boxed{V_A=s_Bs_g.}
$$

This corrects the simpler effective-potential picture, where the mediator is integrated out and one implicitly sets $s_g=1$.

Define distinguishabilities

$$
D_B=\sqrt{1-s_B^2},
\qquad
D_g=\sqrt{1-s_g^2}.
$$

Then

$$
\boxed{V_A^2=(1-D_B^2)(1-D_g^2).}
$$

An additive fidelity-based bookkeeping can also be introduced,

$$
\mathcal J_B=-\ln s_B^2,
\qquad
\mathcal J_g=-\ln s_g^2,
$$

so that

$$
\boxed{-2\ln V_A=\mathcal J_B+\mathcal J_g.}
$$

This provides a useful language for asking **where the branch record resides**.

---

## 3. Source-probe entanglement depends on residual mediator coherence

For the same factorized conditional model, tracing out the gravitational field gives a source-probe negativity

$$
\boxed{
\mathcal N_{AB}
=
\frac14
\left[
\sqrt{(1+s_g)^2-4s_gs_B^2}
-
(1-s_g)
\right].
}
$$

Important limits:

### No residual gravitational branch record

If

$$
s_g=1,
$$

then

$$
\mathcal N_{AB}
=
\frac12\sqrt{1-s_B^2}
=
\frac{D_B}{2}.
$$

### Probe has no branch information

If

$$
s_B=1,
$$

then

$$
\mathcal N_{AB}=0.
$$

### Gravity holds a perfectly distinguishable branch record

If

$$
s_g=0,
$$

then

$$
\boxed{\mathcal N_{AB}=0}
$$

even when the probe states themselves are perfectly distinguishable.

This leads to a central conceptual statement:

> **Quantum mediation is not merely the transmission of branch information. It is the transmission of branch dependence while coherence between the alternatives remains available.**

A mediator that simply broadcasts a perfectly distinguishable classical branch record can correlate source and probe without entangling them.

---

## 4. Incomplete quantum-erasure revival

A particularly useful prediction follows immediately.

Suppose the probe dynamics are reversed perfectly so that

$$
|B_L\rangle=|B_R\rangle,
$$

or equivalently

$$
s_B\rightarrow1.
$$

The source visibility does **not** necessarily return to unity. Instead,

$$
\boxed{
V_{\rm revival}=|\langle g_L|g_R\rangle|=s_g.
}
$$

Therefore a perfect probe-side quantum eraser leaves a residual visibility deficit

$$
\boxed{
1-V_{\rm revival}
=1-|\langle g_L|g_R\rangle|.
}
$$

Interpretation:

- temporary visibility loss can be caused by branch information stored in the probe;
- non-recoverable residual loss after perfect probe erasure measures branch information left in the gravitational field or another uncontrolled environment.

This is one of the strongest candidate observables produced by the Gedanken experiment.

**Novelty status:** the role of branch-dependent gravitational coherent-state overlap in decoherence is established in the literature; the specific use of a controlled probe quantum eraser to isolate a residual gravitational visibility ceiling requires a dedicated literature search before any novelty claim.

---

## 5. Causal branch-information transport

If the source superposition is created or modulated locally at $t=0$ and the probe is a distance $R$ away, then any **source-controlled** branch distinguishability appearing in the probe must satisfy

$$
\boxed{D_B(t)=0\qquad t<R/c.}
$$

This does not mean that all correlations vanish outside the light cone. Quantum fields may possess spacelike vacuum correlations. The claim is narrower:

> **A controllable operation at the source cannot change the local probe statistics or create source-controlled branch distinguishability outside the future light cone.**

A useful time-resolved picture is therefore

$$
A\rightarrow g
\quad\xrightarrow{R/c}\quad
B.
$$

Before causal contact, branch information may already be encoded in the near gravitational field while remaining absent from the remote probe. After causal contact, branch distinguishability can begin to appear in $B$.

A possible operational quantity is

$$
D_B(t)
=
\frac12
\|\rho_B^L(t)-\rho_B^R(t)\|_1.
$$

The broader theoretical question is whether one can formulate a rigorous spacetime-resolved operational measure of **branch-information transport** in the gravitational field.

---

## 6. Near-field coherent interaction versus radiative branch leakage

The desired coherent Newtonian/near-zone entangling interaction scales as

$$
H_{\rm ent}
\sim
\frac{2Gm_Am_B}{R^3}x_Ax_B.
$$

For two spatial amplitudes $\Delta x_A$ and $\Delta x_B$, the accumulated coherent phase scales approximately as

$$
\phi_{\rm ent}
\sim
\frac{2Gm_Am_B\Delta x_A\Delta x_B}{\hbar R^3}T.
$$

Thus

$$
\phi_{\rm ent}\propto T.
$$

By contrast, branch-dependent gravitational radiation produced during rapid splitting/recombination can carry which-path information away and reduce $s_g$. Existing calculations of graviton-induced decoherence for smooth trajectories show very strong suppression for slower preparation, with representative vacuum scaling of the form

$$
\Gamma_{\rm rad}
\propto
\frac{Gm^2d^4}{\hbar c^5\tau^4}
$$

up to trajectory-dependent numerical factors.

This suggests a design principle:

$$
\boxed{
\text{maximize coherent near-field phase while minimizing radiative branch leakage.}
}
$$

A provisional figure of merit is

$$
\mathcal Q_G
=
\frac{\phi_{\rm ent}}{\Gamma_{\rm rad}}.
$$

The scaling suggests that **adiabatic preparation plus long interaction time** may strongly favor coherent mediation over radiative which-path leakage.

**Novelty status:** both near-field gravitational entanglement and graviton-induced decoherence are established topics. A unified optimization of coherent entangling phase against gravitational branch leakage may be a useful paper direction but is not yet established as novel.

---

## 7. Classical mediation and the irreversibility cost

The classical-channel viewpoint remains central.

A classical mediator that reproduces a branch-dependent gravitational response must conceptually perform something equivalent to

$$
\text{acquire source information}
\rightarrow
\text{classical record}
\rightarrow
\text{conditioned force on the probe}.
$$

Known measurement-and-feedback and non-quantized-gravity results imply a tradeoff between

- source decoherence,
- probe diffusion/noise,
- and the strength of the reproduced gravitational interaction.

The conceptual distinction is

$$
\boxed{
\text{classical mediator: learn and react}
}
$$

versus

$$
\boxed{
\text{quantum mediator: correlate without deciding}.
}
$$

The next paper-level goal is to formulate this not only as a Newtonian or Markovian minimum-noise statement but as a **causal conditional-coherence bound** for the original one-cat/one-probe geometry.

---

## 8. The correct non-Gaussian channel object

The original source state is non-Gaussian,

$$
\frac{|L\rangle+|R\rangle}{\sqrt2},
$$

so a purely Gaussian covariance-matrix channel description is not the final framework for the Gedanken experiment.

A more appropriate reduced source-probe map has block structure

$$
\boxed{
\rho_{AB}(T)
=
\frac12
\begin{pmatrix}
\Phi_L^T(\rho_B) & \Xi_T(\rho_B)\\
\Xi_T^\dagger(\rho_B) & \Phi_R^T(\rho_B)
\end{pmatrix}_A.
}
$$

Here

- $\Phi_L^T$ is the probe channel conditioned on source branch $L$;
- $\Phi_R^T$ is the probe channel conditioned on source branch $R$;
- $\Xi_T$ is the **conditional-history coherence map** linking the two alternatives.

A classical mediator can easily generate

$$
\Phi_L\neq\Phi_R.
$$

The difficult resource is maintaining a large

$$
\Xi_T.
$$

This suggests the main candidate theorem:

> **Given a measured branch-dependent gravitational response and a specified class of causal classical mediators, what is the maximum conditional-history coherence $\Xi_T$ that can survive?**

Schematically, seek a bound

$$
\boxed{
\|\Xi_T\|
\le
F[\Phi_L,\Phi_R,N,R,T]
}
$$

for every admissible causal classical gravitational channel, with $N$ denoting the required noise/decoherence resources.

A violation by linearized quantum gravity would provide a genuine discriminator.

---

## 9. Gaussian solvable limit

For two Gaussian oscillator systems, the finite-time Gaussian channel

$$
V_T=X_TV_0X_T^T+Y_T
$$

is completely positive only if

$$
Y_T+
\frac{i\hbar}{2}
(\Omega-X_T\Omega X_T^T)
\succeq0.
$$

A conservative classicality test is obtained by demanding complete PPT preservation,

$$
\boxed{
Y_T+
\frac{i\hbar}{2}
(\Omega_\Gamma-X_T\Omega_\Gamma X_T^T)
\succeq0.
}
$$

This exactly applies to the two-oscillator Gaussian variant, not to the cat-source experiment itself.

Its infinitesimal gravitational limit reproduces the familiar correlated-noise determinant structure

$$
\boxed{
D_AD_B-D_{AB}^2\ge\hbar^2g^2.
}
$$

The Gaussian result should therefore be kept as a **solvable consistency check and limiting model**, while the non-Gaussian $\Xi_T$ problem remains the primary target.

---

## 10. Scalar-field toy model and field-theory structure

A massless scalar mediator provides a clean relativistic toy model before introducing gravitational gauge constraints.

After integrating out a Gaussian field, two kernels appear:

$$
G_R(x,x')
=
\frac{i}{\hbar}\Theta(t-t')
\langle[\phi(x),\phi(x')]\rangle,
$$

and

$$
G_H(x,x')
=
\frac12
\langle\{\phi(x),\phi(x')\}\rangle.
$$

Their roles are

$$
\boxed{G_R\rightarrow\text{causal response}}
$$

and

$$
\boxed{G_H\rightarrow\text{fluctuations/decoherence}.}
$$

Linearized gravity has the same broad influence-functional structure with tensor-valued stress-energy kernels.

This provides a systematic route to calculating

1. the causal conditional probe response;
2. the residual mediator branch overlap;
3. the source-probe coherence map $\Xi_T$;
4. the competition between reversible entanglement and gravitational-field record formation.

---

## 11. Candidate predictions to develop

### Prediction A — Causal branch-information front

For a controlled source operation at $t=0$,

$$
D_B(t)=0
\quad\text{for}\quad
t<R/c,
$$

followed by source-controlled growth after causal contact.

The potentially new element is a fully operational, time-resolved branch-information transport formulation rather than retardation alone.

### Prediction B — Residual visibility after perfect probe erasure

$$
\boxed{
V_{\rm revival}=|\langle g_L|g_R\rangle|.
}
$$

This separates branch information temporarily stored in the probe from branch information irreversibly or persistently stored in the gravitational field.

### Prediction C — Coherent-mediation window

There should exist an experimentally favorable regime maximizing

$$
\phi_{\rm ent}
$$

while minimizing

$$
\Gamma_{\rm rad},
$$

favoring slow superposition preparation and long near-field interaction.

### Prediction D — Causal conditional-coherence bound

For every specified classical mediator class,

$$
\|\Xi_T\|
\le
F[\Phi_L,\Phi_R,N,R,T].
$$

A quantum-gravity calculation violating this bound would be the strongest candidate paper result.

---

## 12. Novelty assessment

### Established ingredients

- gravitationally induced entanglement;
- one-delocalized-source plus quantum-probe architectures;
- retarded/local gravitational entanglement;
- minimum-noise bounds for non-entangling/non-quantized gravity;
- branch-dependent gravitational coherent states and graviton-induced decoherence;
- channel-level approaches to gravitational nonclassicality.

### Potentially novel synthesis

The current project combines these into the three-party problem

$$
A\rightarrow g\rightarrow B
$$

and focuses on **causal transfer of branch distinguishability under a mediator-record coherence constraint**.

The most promising paper-level targets are:

1. a causal conditional-history coherence bound for classical gravity;
2. a controlled quantum-eraser protocol isolating residual gravitational branch records;
3. a quantitative coherent-near-field versus radiative-leakage optimization.

No novelty claim should be made until each is checked against the current literature in detail.

---

## 13. Current Einstein/Feynman compression

> **Put a mass in two places. Before a light signal could reach a distant probe, that probe cannot know which alternative was created. The gravitational field may already carry branch dependence locally. After causal contact, the probe can begin to distinguish the alternatives. But merely broadcasting the branch is not quantum mediation: if the gravitational field leaves a perfectly distinguishable record of which branch occurred, the source and probe need not be entangled. Quantum mediation requires the branch dependence to reach the probe while coherence between the alternatives survives. A perfect probe-side quantum eraser therefore need not restore full source interference; the unrecovered contrast measures branch information left in the mediator. The central question is not simply whether gravity transmits information, but whether it can transmit distinguishability causally without classicalizing the alternative.**

The corresponding short form is

$$
\boxed{
\text{Can gravity move quantum branch information through spacetime without turning it into a classical fact?}
}
$$
