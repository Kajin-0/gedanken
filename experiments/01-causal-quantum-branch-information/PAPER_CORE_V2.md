# Paper Core V2 — Causal Quantum Branch Transport by Gravity

**Timestamp:** 2026-08-07 18:25 EDT  
**Status:** Working theorem-centered paper architecture. Novelty claims remain provisional pending broader literature review.

## Provisional title

**Causal Quantum Branch Transport by Gravity: Exact Binary-Coherent Channel Witnesses and Receiver Fronts**

Alternative shorter title:

**When Can Gravity Carry a Quantum Branch Record?**

---

## Abstract — working version

We formulate gravity-mediated nonclassicality as a causal quantum-receiver problem. A source-controlled gravitational branch mode reaches a distant receiver only after relativistic causal contact; the stronger question is when the complete receiver map becomes capable of preserving entanglement rather than merely carrying a classical branch record. We first prove a quantum-information result for one-mode phase-insensitive Gaussian channels: every finite nontrivial binary coherent hybrid state remains NPT exactly when the channel is not entanglement breaking. The proof reduces to a closed coherent-state matrix element and a single optimized $2\times2$ principal minor, yielding an exact three-element entanglement witness. We then define a time-resolved receiver capability front. Microcausality makes the source-controlled receiver map a replacer channel outside the future light cone, so the quantum-capability front cannot precede $R/c$. For a stationary Gaussian receiver, optimizing over all normalized incoming waveforms gives an exact earliest NPT time with logarithmic critical slowing at the entanglement-breaking boundary. In linearized gravity, a conserved quadrupolar source creates a branch-dependent coherent graviton difference mode. For aligned resonant quadrupole transitions, the retarded Green function determines the delayed source-to-receiver storage amplitude, giving a wave-zone storage probability proportional to $(kR)^{-2}$. Combining these results yields a closed spacetime front for both bare NPT onset and finite witness certification. The framework separates ordinary causal signal arrival, quantum-channel capability, finite experimental certification, and downstream accessibility of the stored branch record.

**Novelty note for internal use:** do not claim that each ingredient is new. The candidate paper contribution is the theorem stack and its gravitational synthesis.

---

# 1. The question

The motivating question is not merely

> Can gravity entangle two masses?

It is

> **Can a controllable gravitational branch record propagate causally into a distant receiver while remaining quantum rather than becoming an ordinary classical record?**

This splits the problem into three logically independent questions:

1. **Causality:** when may a source-controlled influence arrive?
2. **Quantum capability:** when is the receiver channel non-entanglement-breaking?
3. **Certification:** when can a finite experiment prove that fact?

The paper's central object is therefore a time-resolved source-controlled receiver channel

$$
\mathcal A_{R,t}.
$$

---

# 2. Binary coherent channel theorem

## Theorem 1 — coherent dyad matrix element

For the one-mode gauge-covariant phase-insensitive Gaussian channel

$$
\chi_{\Phi_{\tau,m}(O)}(\xi)
=\chi_O(\sqrt\tau\xi)
\exp[-(2m+1-\tau)|\xi|^2/2],
$$

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

### Proof strategy

1. Write the coherent-dyad Weyl characteristic function.
2. Apply the Gaussian channel.
3. Reconstruct the operator in the Weyl basis.
4. Evaluate one elementary complex Gaussian integral.

This lemma makes the later NPT proof finite-dimensional.

---

## Theorem 2 — binary coherent complete-EB probe

Let

$$
|\Psi\rangle
=\sqrt p|0\rangle|\alpha\rangle
+e^{i\phi}\sqrt{1-p}|1\rangle|\beta\rangle,
$$

with

$$
0<p<1,
\qquad
\alpha\neq\beta.
$$

Then

$$
\boxed{
(I\otimes\Phi_{\tau,m})(|\Psi\rangle\langle\Psi|)
\text{ is NPT}
\iff
m<\tau.
}
$$

Since

$$
\Phi_{\tau,m}\text{ is EB}
\iff
m\ge\tau,
$$

the binary coherent hybrid state detects the exact EB boundary.

### Direct proof

By displacement and phase covariance reduce the pair to

$$
|\pm a\rangle.
$$

Consider one $2\times2$ principal minor of the partial transpose in the subspace

$$
\{|0\rangle|0\rangle,\ |1\rangle|v\rangle\}.
$$

For $m>0$, its determinant becomes negative at the optimized coherent analysis amplitude

$$
\boxed{
v_*=\frac{2\sqrt\tau a}{m},
}
$$

because

$$
\boxed{
\frac{|z_{v_*}|^2}{p_0p_{v_*}}
=\exp\left[
\frac{4a^2}{m}(\tau-m)
\right].
}
$$

Thus $\tau>m$ implies NPT. If $m\ge\tau$, the channel is EB and the output is separable.

For pure loss $m=0$, choose finite

$$
v>a(1-\tau)/\sqrt\tau
$$

for every $\tau>0$ to obtain a negative principal minor.

---

## Corollary 2.1 — exact three-element witness

Define

$$
p_0=\langle0,0|\rho|0,0\rangle,
$$

$$
p_v=\langle1,v_*|\rho|1,v_*\rangle,
$$

$$
z_v=\langle1,0|\rho|0,v_*\rangle.
$$

Every separable state satisfies

$$
|z_v|^2\le p_0p_v.
$$

For the Gaussian output,

$$
\boxed{
\Lambda
\equiv
\ln\frac{|z_v|^2}{p_0p_v}
=
\frac{N_\Delta}{m}(\tau-m).
}
$$

Therefore

$$
\boxed{
\Lambda>0
\iff
\text{NPT}
\iff
\text{channel non-EB}.
}
$$

This is the minimal operational witness used later in the gravitational receiver.

---

# 3. Causal channel capability

## Definition — source-controlled accessible receiver channel

Let

$$
\mathcal A_{R,t}
$$

map the state of a controllable outgoing gravitational branch mode to the accessible receiver register at time $t$.

All internal capture, storage, noise, transduction, and readout are included.

---

## Theorem 3 — microcausal replacer theorem

Before causal contact,

$$
\boxed{
\mathcal A_{R,t}(\rho)
=\sigma_{R,t}\operatorname{Tr}\rho,
\qquad t<R/c.
}
$$

Hence

$$
\boxed{
\mathcal A_{R,t}\in\mathrm{EB}
\qquad t<R/c.
}
$$

### Proof strategy

A local source encoding operator in region $A$ commutes with every receiver observable in spacelike-separated region $B$. Receiver expectation values are therefore independent of the source input state. The reduced source-controlled channel is a replacer.

This statement is compatible with spacelike vacuum correlations and entanglement harvesting because it concerns **controlled communication**, not the absence of all correlations.

---

## Definition — quantum capability front

$$
\boxed{
T_{\rm cap}(R)
=\inf\{t:\mathcal A_{R,t}\notin\mathrm{EB}\}.
}
$$

Microcausality gives

$$
\boxed{
T_{\rm cap}(R)\ge R/c.
}
$$

---

## Definition — front-faithful probe

A probe family is front faithful for a channel family if its output becomes entangled exactly when the channel leaves the EB set.

By Theorem 2, finite binary coherent hybrid probes are front faithful for the covered phase-insensitive Gaussian channel family.

Therefore

$$
\boxed{
T_{\rm binary}^{\rm NPT}(R)
=T_{\rm cap}(R).
}
$$

---

# 4. Exact receiver front

Consider a stationary passive one-mode receiver

$$
\dot c
=-\frac{\kappa_{\rm tot}}2c
+\sqrt{\kappa_\Delta}\,b_\Delta^{\rm in}
+\sum_a\sqrt{\kappa_a}\,b_a^{\rm in}.
$$

Define

$$
\Gamma_{\rm th}
=\sum_a\bar n_a\kappa_a.
$$

For any normalized incoming waveform $f$,

$$
\tau_f(\Delta t)
\le
\frac{\kappa_\Delta}{\kappa_{\rm tot}}
(1-e^{-\kappa_{\rm tot}\Delta t}).
$$

The time-reversed receiver ringdown saturates this bound.

---

## Theorem 4 — waveform-optimal channel-capability front

If

$$
\kappa_\Delta\le\Gamma_{\rm th},
$$

the receiver remains EB for all time.

If

$$
\kappa_\Delta>\Gamma_{\rm th},
$$

$$
\boxed{
T_{\rm cap}^{\min}(R)
=\frac Rc+
\frac1{\kappa_{\rm tot}}
\ln\frac{\kappa_\Delta}
{\kappa_\Delta-\Gamma_{\rm th}}.
}
$$

The exact binary coherent NPT front and zero-margin matched-witness front coincide with this channel front.

Near the EB boundary,

$$
T_{\rm cap}-R/c
$$

diverges logarithmically.

---

# 5. Linearized gravity: source and receiver

## 5.1 Conserved quadrupole source

Use a branch quadrupole difference

$$
\Delta Q_{xx}=q(t),
\qquad
\Delta Q_{yy}=-q(t).
$$

For receiver on the $z$ axis,

$$
\boxed{
\Delta\mathcal E_{xx}(t,R)
=-\frac{G}{R^5}
\left[
3q+
\frac{3R}{c}\dot q+
\frac{3R^2}{c^2}\ddot q+
\frac{2R^3}{c^3}q^{(3)}+
\frac{R^4}{c^4}q^{(4)}
\right]_{t-R/c}.
}
$$

For harmonic motion,

$$
P(\epsilon)
=3-3i\epsilon-3\epsilon^2+2i\epsilon^3+\epsilon^4,
\qquad
\epsilon=\omega R/c.
$$

---

## 5.2 Branch-difference graviton mode

The outgoing branch coherent-state distance is

$$
\boxed{
N_\Delta
=\frac{G}{5\pi\hbar c^5}
\int_0^\infty d\omega\,
\omega^5|\Delta\widetilde Q_{ij}(\omega)|^2.
}
$$

For a narrow-band plus quadrupole,

$$
N_\Delta
\simeq
\frac{Gq_0^2\omega_0^5T_f}{5\hbar c^5}.
$$

---

## 5.3 Receiver graviton linewidth

For a receiver quadrupole transition,

$$
\boxed{
\kappa_g
=\frac{2G\omega^5}{5\hbar c^5}
Q_{ij}^{10}Q_{ij}^{01}.
}
$$

For the plus transition,

$$
\kappa_g
=\frac{4G\omega^5|q_B|^2}{5\hbar c^5}.
$$

---

## Theorem 5 — normalized gravitational retarded cross response

For resonant aligned plus quadrupoles,

$$
\boxed{
\Sigma_{AB}^{R}(\omega,R)
=\frac54
\sqrt{\kappa_{g,A}\kappa_{g,B}}
\frac{P(\epsilon)e^{i\epsilon}}
{\epsilon^5}.
}
$$

The real part is independently consistent with the published vacuum-graviton resonance interaction. The imaginary part obeys the expected common-bath cross-damping relation.

---

## Corollary 5.1 — delayed storage map

The source-controlled receiver equation contains

$$
\dot a_B(t)|_A
=-i\Sigma_{BA}^{R}a_A(t-R/c).
$$

With ordinary input-output normalization,

$$
\boxed{
t_{BA}^{\rm store}
=\frac{-i\Sigma_{BA}^{R}}
{\sqrt{\kappa_{g,A}\kappa_{g,B}}}.
}
$$

In the wave zone,

$$
\boxed{
\eta_{\rm store}(R)
=|t|^2
\simeq
\frac{25\mathcal O}{16(kR)^2}.
}
$$

Here $\mathcal O$ is a normalized residual mode-overlap factor.

---

# 6. Master gravitational front

The useful source-mode loading rate is

$$
\boxed{
\kappa_\Delta(R)
=\frac{25\mathcal O}{16(kR)^2}\kappa_g.
}
$$

Substitute this into Theorem 4.

---

## Theorem 6 — wave-zone gravitational channel-capability front

For nonzero stationary thermal injection,

$$
\boxed{
T_{\rm cap}(R)
=\frac Rc-
\frac1{\kappa_{\rm tot}}
\ln\left[
1-
\frac{16(kR)^2\Gamma_{\rm th}}
{25\mathcal O\kappa_g}
\right],
}
$$

provided

$$
\boxed{
\frac{25\mathcal O\kappa_g}
{16(kR)^2\Gamma_{\rm th}}>1.
}
$$

The binary coherent NPT and exact zero-margin witness fronts coincide with this capability front.

Define

$$
\boxed{
R_Q
=\frac{5}{4k}
\sqrt{\frac{\mathcal O\kappa_g}{\Gamma_{\rm th}}}.
}
$$

Then no Gaussian receiver capability front exists for

$$
R\ge R_Q.
$$

As $R\to R_Q^-$, the front diverges logarithmically.

Well inside the range,

$$
T_{\rm cap}-R/c\propto R^2.
$$

---

## Corollary 6.1 — finite-certification front

For target exact-witness margin $\Lambda_{\rm req}>0$,

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

The finite-certification radius is

$$
\boxed{
R_\Lambda
=\frac{R_Q}
{\sqrt{1+\Lambda_{\rm req}/N_\Delta}}.
}
$$

Thus

$$
R_\Lambda<R_Q.
$$

---

# 7. Vacuum limit and feasibility

At zero thermal occupation the pure-loss channel is non-EB for every nonzero transmission, so there is no finite mathematical NPT range.

The physically relevant quantity is maximum transferable entanglement.

For total storage fraction

$$
\eta_Q(R)
=\frac{25\mathcal O}{16(kR)^2}
\frac{\kappa_g}{\kappa_{\rm tot}},
$$

and $\eta_Q\ll1$,

$$
\boxed{
\mathcal N_{\max}
=\eta_Q-2\eta_Q^{3/2}+O(\eta_Q^2).
}
$$

A very large branch wave does not bypass weak capture because the uncaptured field becomes a strong which-branch record.

---

## Passive nonrelativistic receiver corollary

The quadrupole sum rule gives

$$
\frac{\kappa_g}{\omega}
\le
\frac23\mathcal C_B\beta_B^3.
$$

For $\kappa_{\rm tot}\simeq\omega/Q_B$ and wave-zone condition $kR\ge\zeta$,

$$
\boxed{
\mathcal N_{\max}^{\rm WZ}
\lesssim
\frac{25\mathcal O}{24\zeta^2}
Q_B\mathcal C_B\beta_B^3.
}
$$

This is a receiver-class feasibility bound, not a universal gravity theorem.

---

# 8. Accessibility beyond capture

A strongly gravitating object can absorb a branch mode efficiently while failing as an experimental quantum receiver because the internal record may be inaccessible.

Model

$$
\text{capture}\to\text{readout}.
$$

For Gaussian stages,

$$
\boxed{
\tau_{\rm tot}=\tau_c\tau_r,
\qquad
m_{\rm tot}=\tau_rm_c+m_r.
}
$$

Thus

$$
\boxed{
\text{accessible output NPT}
\iff
\tau_r(\tau_c-m_c)>m_r.
}
$$

For arbitrary channels, use the complete accessible map

$$
\mathcal A=\mathcal R\circ\mathcal C
$$

and ask whether

$$
\mathcal A\notin\mathrm{EB}.
$$

The EB robustness satisfies the bottleneck law

$$
R_{\rm EB}(\mathcal A)
\le
\min\{R_{\rm EB}(\mathcal C),R_{\rm EB}(\mathcal R)\}.
$$

This is the correct framework for compact objects and non-Gaussian receivers.

---

# 9. Planck-area absorption and loading time

Weak bound-state calculations give

$$
\sigma_{\rm GR}
=\Gamma_g/\omega^3
\sim\ell_P^2.
$$

This is compatible with wavelength-scale peak resonant storage because

$$
\Gamma_g/\omega
\sim(k\ell_P)^2.
$$

Thus the Planck suppression appears in the **fractional bandwidth/loading time**:

$$
T_{\rm load}\sim\Gamma_g^{-1}.
$$

Strong self-gravity can evade this tiny linewidth, but then accessibility/scrambling becomes the main receiver problem.

This belongs in discussion, not in the central theorem proof.

---

# 10. Figures that would make the paper clear

## Figure 1 — Experiment architecture

Source branch register $S$ → local gravitational encoding → retarded branch-difference mode → receiver → accessible register.

Show

- light cone $R/c$;
- internal receiver mode;
- discarded environment/readout complement.

## Figure 2 — Gaussian channel plane

Axes:

$$
\tau,\quad m.
$$

Show EB boundary

$$
m=\tau.
$$

Every binary coherent probe becomes NPT on exactly the same side.

## Figure 3 — exact principal-minor witness

Plot

$$
\Lambda
=N_\Delta(\tau-m)/m
$$

versus channel distance from EB boundary.

## Figure 4 — spacetime fronts

Plot

$$
R/c,
\quad
T_{\rm cap}(R),
\quad
T_\Lambda(R).
$$

Show logarithmic divergence at

$$
R_Q,
\quad
R_\Lambda.
$$

## Figure 5 — vacuum receiver feasibility

Plot passive receiver parameter

$$
Q_B\mathcal C_B\beta_B^3
$$

and resulting upper bound on optimized wave-zone negativity.

---

# 11. What the paper must NOT claim

Do not claim:

- that BMV/gravity-generated entanglement is new;
- that retarded gravity-mediated entanglement is new;
- that two coherent states have never been used for channel testing;
- that the Gaussian EB boundary is new;
- that finite quantum communication range under thermal loss is new;
- that all gravitational receivers obey the passive nonrelativistic sum-rule bound;
- that Planck area is a universal graviton-absorption peak cross section;
- that arbitrary source-receiver entanglement cannot exist spacelike.

---

# 12. Candidate paper contributions — cautious wording

Pending broader novelty verification, the paper may plausibly contribute the following combination:

1. a direct finite-principal-minor proof that **every nontrivial finite binary coherent hybrid state exactly detects the EB boundary of a one-mode gauge-covariant phase-insensitive Gaussian channel**;
2. an exact three-element matched witness saturating that boundary;
3. a microcausal definition of a **source-controlled quantum capability front**;
4. an exact waveform-optimal capability/NPT front for a Gaussian quantum receiver;
5. a linearized-gravity mapping from quadrupole branch histories to the receiver channel via the retarded gravitational Green function;
6. a closed gravitational NPT/certification front in spacetime.

The gravity paper should be built around this theorem stack. Passive receiver bounds and strong-gravity accessibility should be secondary sections/discussion.

---

# 13. Next actions before calling this a draft paper

1. Perform a citation-forward search from Kreis & van Loock and Häseler–Moroder–Lütkenhaus specifically for exact binary coherent NPT/EB equivalence.
2. Have the direct Gaussian proof independently rederived in a second notation/convention.
3. Cross-check the gravitational storage coefficient with a fully explicit mode-normalized single-graviton scattering/input-output derivation.
4. Convert this core into a conventional manuscript only after those three checks survive.