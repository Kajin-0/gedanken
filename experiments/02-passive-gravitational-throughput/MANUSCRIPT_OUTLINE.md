# Manuscript Outline — Experiment 02

## Working title candidates

Preferred:

**Passive Throughput Bounds for Propagating Gravitational Quantum Transduction**

Alternative:

**An End-to-End Passive Bound on Gravitational Quantum Transduction**

Avoid titles claiming a universal quantum-capacity theorem.

---

## One-sentence thesis

Historical resonant-mass antenna theory already shows that integrated gravitational absorption is controlled by oscillator strength rather than quality factor alone; here the corresponding **two-ended** problem is closed for compact passive linear matter links by bounding the source gravitational resource, normalized TT propagation, and receiver gravitational resource in one frequency-integrated transfer inequality.

---

## Abstract logic

The abstract should contain only five moves:

1. **Known context:** resonant gravitational antennas have an integrated response that does not grow indefinitely with Q, while modern quantum-transducer theory treats efficiency and bandwidth jointly.
2. **Question:** what is the analogous end-to-end limit when both matter-gravity interfaces and the propagating gravitational channel are explicit?
3. **Theorem:** define

```math
\Gamma_{\rm coh}
=\frac1{2\pi}\int\operatorname{Tr}(T^\dagger T)d\omega
```

and state the passive compact-quadrupole narrowband bound

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega^2}{12c^3R^2}
\min(\langle I_A\rangle,\langle I_B\rangle).
}
```

4. **Meaning:** the bound is independent of endpoint Q, number of passive internal modes, coherent mode mixing, and compact quadrupole orientation within the declared class.
5. **Quantum corollary:** in a stationary vacuum pure-loss realization, the same response theorem gives explicit continuous-time capacity bounds; keep this secondary to the physical theorem.

Do not mention the four-spoke source in the abstract.

---

# 1. Introduction — from one-sided absorption to two-ended transduction

### Paragraph 1 — historical gravitational response

Start with resonant-mass gravitational-wave antennas, not V7.

Credit historical absorption-cross-section theory, especially Paik–Wagoner and later resonant-mass work. State explicitly that a resonant peak can grow with Q while its bandwidth narrows, so integrated absorption is governed by physical oscillator strength rather than Q alone.

This immediately prevents the paper from appearing to rediscover a 1970s antenna fact.

### Paragraph 2 — modern quantum-transducer viewpoint

Introduce continuous-time quantum-transducer metrics: efficiency, bandwidth, and noise are joint properties; an already normalized incident bosonic mode is not the whole physical device problem.

### Paragraph 3 — the missing two-ended question

State the actual question:

```text
Given a passive material source, a propagating gravitational wave channel,
and a passive material receiver, what frequency-integrated coherent transfer
can the complete link support?
```

The distinction from one-sided absorption is that both material interfaces compete for finite gravitational oscillator-strength resources and are connected by a normalized propagating channel.

### Paragraph 4 — contributions

Only three claims:

1. a passive linear-network gravitational cut set;
2. closure of each interface resource using mass-quadrupole spectral weight/EWSR and closure of propagation using the TT singular-channel ceiling;
3. pure-loss capacity corollaries.

No “first,” “universal,” or “fundamental limit” language unless later literature audit supports it.

---

# 2. Physical quantity and system boundary

## 2.1 Frequency-integrated coherent transfer

Define the useful traveling-field transfer matrix `T(omega)` and

```math
\Gamma_{\rm coh}
=\frac1{2\pi}\int_{\mathcal B}
\operatorname{Tr}[T^\dagger T]d\omega.
```

Explain dimensions and normalization.

Make explicit:

- not a quantum capacity;
- no arbitrary FWHM or chosen `B` enters;
- in scalar systems it is the area under transmissivity.

## 2.2 System boundary

Define what belongs to each endpoint and what belongs to free propagation.

State no unaccounted direct local-to-gravity feedthrough. If a physical conversion element exists, it belongs inside the endpoint and consumes its own physical resource.

---

# 3. Passive-network cut-set theorem

Use established passive linear quantum-system notation:

```math
A=-iH-\frac12K^\dagger K.
```

Credit the established full-channel Gramian result rather than presenting it as new.

Partition useful local, gravitational, and loss ports.

Derive

```math
\|S_{g\leftarrow u}\|_2^2
\le\operatorname{Tr}(K_g^\dagger K_g).
```

Then for source, propagation, receiver:

```math
T=S_B P_g S_A.
```

Prove

```math
\boxed{
\Gamma_{\rm coh}
\le
\eta_{\max}
\min[
\operatorname{Tr}(K_{g,A}^\dagger K_{g,A}),
\operatorname{Tr}(K_{g,B}^\dagger K_{g,B})].
}
```

Interpret as a cut-set bound: neither endpoint can transmit more integrated coherent amplitude than its own gravitational port resource.

Keep proof short in main text; detailed Lyapunov algebra can move to an appendix.

---

# 4. Microscopic gravitational port normalization

This section is essential because it prevents the criticism that linewidth and geometry are being double counted.

Define microscopic matter-to-graviton coupling operators

```math
G_A=V_A\Gamma_{g,A}^{1/2},
\qquad
G_B=V_B\Gamma_{g,B}^{1/2}.
```

Then

```math
\boxed{
G_B^\dagger U_RG_A
=
\Gamma_{g,B}^{1/2}
P_g
\Gamma_{g,A}^{1/2},
}
```

with

```math
P_g=V_B^\dagger U_RV_A.
```

Emphasize:

```text
Gamma_g = coupling magnitude / linewidth resource
P_g     = normalized gravitational mode geometry
```

Nonorthogonal radiation patterns and collective radiative damping are automatically included through the Gram matrix.

---

# 5. Passive mass-quadrupole resource

## 5.1 Linear matter normal modes

Diagonalize the isolated passive linear bosonic matter Hamiltonian and show

```math
\operatorname{Tr}(K_g^\dagger K_g)
=\sum_n\kappa_{g,n}.
```

## 5.2 Microscopic one-graviton rate

Use

```math
\kappa_{g,n}
=\frac{2G\omega_n^5}{5\hbar c^5}
Q_{ij}^{0n}Q_{ij}^{n0}.
```

## 5.3 Cumulative EWSR

Define the internal inertia about the center of mass,

```math
I=\sum_a m_a|\mathbf r_a-\mathbf R_{\rm CM}|^2.
```

Then obtain

```math
\boxed{
\operatorname{Tr}(K_g^\dagger K_g)
\le
\frac{4G\Omega^4}{3c^5}\langle I\rangle.
}
```

Historical comparison belongs here: resonant-mass integrated cross sections already express the same broad oscillator-strength logic on the receiver side. Our use is to turn it into the endpoint resource entering the two-ended cut set.

---

# 6. Compact TT propagation ceiling

For arbitrary complex STF quadrupole `Q`, derive

```math
D_Q(\hat n)
=\frac52\frac{Q^*:\Lambda Q}{Q^*:Q}
\le\frac52.
```

Then use normalized one-graviton angular modes and stationary phase to obtain

```math
\boxed{
t_{BA}^{TT}
=-\frac{5i}{4kR}e^{ikR}
\frac{Q_B^*:\Lambda Q_A}{\|Q_A\|\|Q_B\|}
+O((kR)^{-2}).
}
```

Therefore

```math
\boxed{
\eta_{\max}
\le\frac{25}{16(kR)^2}
}
```

at leading wave-zone order.

State explicitly that the result is for compact quadrupole channel spaces; extended apertures and higher multipoles are different architectures.

The reciprocal Friis/effective-area interpretation can be mentioned only after the direct TT proof.

---

# 7. Combined passive gravitational throughput theorem

Combine Sections 3–6:

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega^2}{12c^3R^2}
\min(\langle I_A\rangle,\langle I_B\rangle).
}
```

This should be the visual center of the paper.

Immediately list what disappeared:

```text
Q
branching fractions
number of passive resonances
internal coherent basis
four-spoke geometry
```

Do not say these variables are irrelevant physically; say they cannot increase the integrated transfer beyond the bound within the stated passive class.

---

# 8. Exact two-pole example and optimization

Only now introduce the simplest resonant realization.

Derive

```math
\Gamma_{\rm EBP}
=
\frac{4\eta_{\rm prop}
\kappa_{\rm in}\kappa_{g,A}\kappa_{g,B}\kappa_{\rm out}}
{\kappa_A\kappa_B(\kappa_A+\kappa_B)}.
```

Show:

```math
\Gamma_{\rm EBP}
\le\eta_{\rm prop}\min(\kappa_{g,A},\kappa_{g,B}).
```

For symmetric endpoints:

```math
\kappa_{\rm in}=\kappa_{\rm out}=2\kappa_g,
```

```math
\Gamma_{\rm EBP}^{\rm max}
=\frac8{27}\eta_{\rm prop}\kappa_g.
```

This example should make the theorem intuitive: peak-optimal critical coupling and area-optimal overcoupling are different objectives.

---

# 9. Concrete conserved source benchmark

Use V7 only as an existence/sanity check.

The long-wavelength four-endpoint plus mode has

```math
\kappa_g^{\rm V7}
=\frac{8G\mu L^2\omega^4}{5c^5}
```

against EWSR ceiling

```math
\kappa_{g,\rm EWSR}^{\rm max}
=\frac{16G\mu L^2\omega^4}{3c^5}.
```

Thus it reaches 30% of the endpoint-only material ceiling and saturates compact TT directivity.

Do not reproduce V7 source mechanics. One paragraph plus a small table is enough.

---

# 10. Quantum-information consequences

Keep this short and subordinate.

For pure loss:

```math
\tau_n(\omega)\le\eta_{\max}.
```

Wave-zone compact quadrupole propagation has `eta_max << 1/2`, therefore

```math
Q_1=0
```

for unassisted asymptotic pure-loss capacity.

For two-way assistance,

```math
\boxed{
Q_2
\le
\frac{\Gamma_{\rm coh}}
{\ln2(1-\eta_{\max})}.
}
```

Explain carefully why zero one-way asymptotic capacity does not imply zero finite-use entanglement transfer.

---

# 11. Scope and routes around the theorem

A concise table is appropriate.

| Escape route | Why outside theorem |
|---|---|
| Active/inverted matter | breaks passive positive-resource argument |
| Parametric/time-dependent drive | leaves time-invariant passive network class |
| Extended phased aperture | leaves compact quadrupole directivity ceiling |
| Higher multipoles / relativistic sources | leaves leading nonrelativistic quadrupole regime |
| Near-field exchange | leaves propagating wave-zone channel |
| Intermediate relay | creates additional interfaces/hops requiring a new network bound |
| Curved-space lensing | replaces flat-space TT propagation operator |
| Nonlinear interacting matter | requires a more general response realization |

This section naturally motivates later research without weakening the theorem.

---

# 12. Discussion — what the theorem does and does not add

The central discussion paragraph should be unusually explicit:

- historical gravitational antenna theory already knows integrated one-sided absorption is not improved arbitrarily by Q;
- passive linear quantum-network identities are known;
- continuous-time quantum-transducer metrics are known;
- the candidate contribution is the **closure of these ingredients into a two-ended gravitational quantum-transduction resource inequality**.

This is where the paper earns credibility.

---

# 13. Conclusion

End with the simplest physical statement:

> For direct compact passive quadrupole links, increasing Q, adding passive resonances, or rotating within the compact quadrupole channel cannot evade the integrated source-to-receiver ceiling; any substantial improvement must change the physical resource class rather than merely optimize passive resonant matching.

Do not use “impossible,” “universal,” or “fundamental quantum gravity limit.”

---

# Appendices

## Appendix A — passive Gramian/H2 proof

Full Lyapunov derivation, clearly credited to established completely passive-system theory.

## Appendix B — gravitational-port polar decomposition

Microscopic coupling Gram matrix, nonorthogonal radiation patterns, normalized field subspace.

## Appendix C — quadrupole EWSR

Reproduce only the minimum derivation needed for self-containment and center-of-mass convention.

## Appendix D — TT angular normalization and stationary phase

Full STF projector trace, `8 pi / 5` identity, outgoing stationary-phase coefficient.

## Appendix E — exact two-pole integral and optimization

Lorentzian integral, passive inequality, symmetric `8/27` optimum.

## Appendix F — capacity formulas and assumptions

Pure-loss one-way/two-way formulas and frequency integration.

---

# Figures

Only two figures should be needed.

### Figure 1 — theorem architecture

```text
passive source network
[Tr Gamma_g,A]
        |
        v
normalized TT propagation
[||P_g||^2]
        |
        v
passive receiver network
[Tr Gamma_g,B]
```

Below it, show the final narrowband theorem.

### Figure 2 — efficiency vs spectral area

Use the exact two-pole model to show how increasing Q can raise peak transfer while narrowing width, with the integrated area bounded. Overlay the symmetric area optimum at external coupling `2 kappa_g`.

Do not make the four-spoke source a main figure.

---

# Manuscript go/no-go before drafting

Proceed to full manuscript only if all four are satisfied:

1. the historical two-antenna/reciprocity search still finds no direct collision with the two-ended cut set;
2. an independent rederivation confirms the TT stationary-phase `5/(4kR)` coefficient;
3. the gravitational-port polar factorization is checked against a microscopic multimode example with overlapping angular patterns;
4. the novelty statement remains meaningful after explicitly crediting Paik–Wagoner, susceptibility-based antenna response, passive Gramian theory, and modern transducer capacity literature.

If these survive, the paper should be theorem-first and substantially more general than V7 rather than an extension of the V7 source model.
