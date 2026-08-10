# Current State — Experiment 02

**Status:** **PHYSICS THEOREM CHECKPOINT CLOSED; FULL-TEXT GRAVITATIONAL-ANTENNA AND GENERIC-WAVE PRIOR-ART GATES COMPLETED; MANUSCRIPT CLAIM NARROWED TO THE GRAVITY-SPECIFIC CUMULATIVE CLOSURE; FURTHER BROADENING STOPPED**

## 1. Headline theorem

For a direct narrowband link between compact passive nonrelativistic **linear bosonic** source and receiver networks, coupled through quadrupolar linearized gravity in the weak one-way wave zone,

```math
\Gamma_{\rm coh}
=\frac1{2\pi}\int_{\mathcal B}
\operatorname{Tr}[T^\dagger(\omega)T(\omega)]d\omega
```

obeys, at the retained order,

```math
\boxed{
\Gamma_{\rm coh}
\lesssim
\frac{25G\omega^2}{12c^3R^2}
\min\!\left(\langle I_A\rangle,\langle I_B\rangle\right).
}
```

`I_A` and `I_B` are internal mass inertia moments about the endpoint centers of mass.

The final ceiling contains no endpoint quality factor, no assumed number of passive resonances, no internal coherent-mixing parameter, and no four-spoke-specific parameter. `Gamma_coh` is an integrated coherent-transfer quantity, **not itself a quantum capacity**.

Experiment 01 / V7 remains frozen and is not modified by this branch.

---

## 2. Proof chain

### A. Passive selected-port H2 cut set

For a stable completely passive endpoint,

```math
A=-iH-\frac12K^\dagger K,
```

standard Gramian identities imply

```math
\boxed{
\Gamma_{\rm coh}
\le
\eta_{\max}
\min\!\left[
\operatorname{Tr}(K_{g,A}^\dagger K_{g,A}),
\operatorname{Tr}(K_{g,B}^\dagger K_{g,B})
\right].
}
```

Arbitrary finite-dimensional passive coherent mode mixing and overlapping resonances are allowed. The H2/Gramian mathematics is established prior art.

Canonical file: `PASSIVE_NETWORK_CUTSET_THEOREM.md`.

### B. Microscopic gravitational-port factorization

For narrowband matter-to-graviton coupling,

```math
G=V\Gamma_g^{1/2},
\qquad
\Gamma_g=G^\dagger G,
```

so

```math
\boxed{
G_B^\dagger U_RG_A
=\Gamma_{g,B}^{1/2}P_g\Gamma_{g,A}^{1/2},
\qquad
P_g=V_B^\dagger U_RV_A.
}
```

This separates endpoint coupling magnitude from normalized propagation geometry and retains nonorthogonal radiation patterns through the gravitational Gram matrix.

Canonical file: `GRAVITATIONAL_PORT_FACTORIZATION.md`.

### C. Cumulative quadrupole resource

For passive linear bosonic matter,

```math
\operatorname{Tr}(K_g^\dagger K_g)
=\sum_n\kappa_{g,n},
```

with

```math
\kappa_{g,n}
=\frac{2G\omega_n^5}{5\hbar c^5}
Q_{ij}^{0n}Q_{ij}^{n0}.
```

The mass-quadrupole EWSR yields, for retained quadrupole-active modes below `Omega`,

```math
\boxed{
\operatorname{Tr}(K_g^\dagger K_g)
\le
\frac{4G}{3c^5}\langle I\rangle\Omega^4.
}
```

This cumulative closure is the step that prevents arbitrarily many passive resonances from increasing the endpoint gravitational resource without increasing the underlying matter/inertia resource.

Canonical files: `MATERIAL_RESPONSE_BRIDGE.md`, `SPECTRAL_GENERALIZATION.md`.

### D. Normalized compact TT propagation

For arbitrary complex STF transition quadrupoles,

```math
\|P_g(\omega)\|_{\rm op}^2
\le
\frac{25}{16[k(\omega)R]^2}
```

at leading wave-zone order, with amplitude

```math
t_{BA}^{\rm TT}
=-\frac{5i}{4kR}e^{ikR}
\frac{Q_B^*:\Lambda(\hat R):Q_A}
{\sqrt{Q_A^*:Q_A}\sqrt{Q_B^*:Q_B}}
+O((kR)^{-2}).
```

The real-STF directivity functional itself is historical; see Sec. 5 below.

Canonical files: `TT_PROPAGATION_BOUND.md`, `INDEPENDENT_TT_COEFFICIENT_CHECK.md`.

---

## 3. Independent classical-to-quantum normalization closure

Full-text inspection of Hirakawa, Narihara, and Fujimoto (1976) gives an independent normalization bridge.

For their compact elastic mode,

```math
A_{Gn}=\frac{2\,q_n:q_n}{M\mu_n}.
```

Quantizing the same normal coordinate gives

```math
Q^{01}:Q^{10}
=\frac{\hbar M A_{Gn}}{4\omega_n},
```

and therefore the Experiment 02 one-graviton rate becomes

```math
\boxed{
\kappa_{g,n}
=\frac{GMA_{Gn}\omega_n^4}{10c^5}.
}
```

The historical short-pulse result may equivalently be written

```math
\boxed{
\frac{E}{F(\nu_n)}
=\frac{\pi}{2}\frac{\kappa_{g,n}}{k_n^2}
f_n(\hat n).
}
```

Thus the open-system gravitational linewidth is exactly the quantized form of the historical gravitational mode oscillator-strength normalization. No factor-of-two or `2 pi` inconsistency was found.

Canonical file: `HIRAKAWA_EFFECTIVE_AREA_QUANTUM_LINEWIDTH_CROSSCHECK.md`.

---

## 4. Exact two-resonator specialization and quantum corollaries

For explicit local source and receiver ports,

```math
\Gamma_{\rm EBP}
=
\frac{4\eta_{\rm prop}
\kappa_{\rm in}\kappa_{g,A}\kappa_{g,B}\kappa_{\rm out}}
{\kappa_A\kappa_B(\kappa_A+\kappa_B)}
\le
\eta_{\rm prop}\min(\kappa_{g,A},\kappa_{g,B}).
```

For the symmetric lossless family,

```math
\kappa_{\rm in}=\kappa_{\rm out}=2\kappa_g,
\qquad
\Gamma_{\rm EBP}^{\rm max}
=\frac8{27}\eta_{\rm prop}\kappa_g.
```

Peak-optimal critical coupling and integrated-throughput-optimal coupling are therefore different objectives.

For a stationary vacuum pure-loss realization,

```math
\eta_{\max}\le\frac12
\Rightarrow Q_1=0,
```

while

```math
Q_2
\le
\frac{\Gamma_{\rm coh}}
{\ln2\,(1-\eta_{\max})}.
```

These are channel-specific corollaries, not universal capacity claims.

---

## 5. Prior-art boundary after full-text and cross-field audits

### Gravitational antenna physics — historical

Full-text inspection establishes that the following are not new:

- complete source--gravitational-field--receiver calculations and architecture-specific end-to-end limitations (Grishchuk--Sazhin 1975);
- compact mechanical gravitational antenna eigenmodes (Hirakawa--Narihara--Fujimoto 1976);
- quadrupole-defined gravitational oscillator strength;
- the same mode resource controlling emission and reception;
- gravitational antenna reciprocity;
- `Q`-independent short-pulse / integrated resonant response;
- the compact real-STF directivity functional and its `D=5/2` maximum.

For real STF `q`, Hirakawa Eq. (15) is algebraically identical to

```math
D_q(\hat n)=\frac52\frac{q:\Lambda(\hat n):q}{q:q}.
```

Canonical audits:

- `GRISHCHUK_SAZHIN_1975_COLLISION_AUDIT.md`
- `HIRAKAWA_NARIHARA_FUJIMOTO_1976_COLLISION_AUDIT.md`
- `HIRAKAWA_EFFECTIVE_AREA_QUANTUM_LINEWIDTH_CROSSCHECK.md`

### Generic wave-transfer structure — historical

Cross-field prior art also removes novelty from the abstract source--propagation--receiver operator architecture. Generic wave theory already contains

- orthogonal/singular source--receiver communication channels;
- sums of squared channel connection strengths;
- two-body response-resource bounds connected by a free-space Green operator;
- Frobenius/trace transfer metrics and transmission singular-value bounds.

Canonical audit: `GENERIC_WAVE_TRANSFER_COLLISION_AUDIT_2026-08-09.md`.

### Sum-rule-to-integrated-response methodology — historical

Recent acoustic work also provides an explicit modern precedent for using a physical sum rule to constrain an integrated passive scattering response. This strengthens the requirement that Experiment 02 not claim novelty for the sum-rule methodology itself.

### Surviving candidate contribution

The only remaining candidate novelty is the **gravity-specific cumulative closure**:

```text
established passive selected-port H2 integral
-> smaller source/receiver gravitational coupling trace
-> microscopic quadrupole identification of those traces
-> cumulative mass-quadrupole EWSR at BOTH endpoints
-> normalized compact separated TT propagation
-> explicit inertia-controlled many-mode end-to-end ceiling.
```

Equivalently, the candidate contribution is the final elimination of all phenomenological endpoint coupling parameters in favor of

```math
\boxed{
\frac{25G\omega^2}{12c^3R^2}
\min(\langle I_A\rangle,\langle I_B\rangle).
}
```

No inspected primary source has been found stating this exact cumulative gravitational theorem. That is a **negative search result, not a priority proof**.

---

## 6. Validation state

Analytic and numerical validation remains unchanged and passing:

1. exact two-pole spectral area and random passive rates;
2. random multimode passive Gramians and directly integrated cascades;
3. random complex STF quadrupoles, TT angular normalization, and the `25/16` coefficient;
4. microscopic gravitational-port factorization with overlapping radiation patterns;
5. independent historical `A_G <-> kappa_g` normalization match.

Physics regression run:

```text
run 31311724347
job 93240439026
PASS
```

Latest manuscript build after the Hirakawa normalization and generic-wave prior-art revisions:

```text
run 31343168940
job 93320172594
LaTeX compile:             PASS
unresolved refs/citations: PASS
PDF artifact upload:       PASS
```

The earlier empty-journal BibTeX warning for the Srivastava--Widom--Pizzella arXiv preprint was removed by treating it as an arXiv `@misc` entry.

---

## 7. Publication decision

```text
PHYSICS THEOREM:                       GO WITH DECLARED SCOPE
MICROSCOPIC NORMALIZATION:             GO; HISTORICAL A_G MATCH FOUND
NUMERICAL VALIDATION:                  GO
GENERIC SOURCE--RECEIVER NOVELTY:      NO
GENERIC SINGULAR-CHANNEL NOVELTY:      NO
Q-INDEPENDENT GRAVITATIONAL RESPONSE:  NO
GRAVITATIONAL RECIPROCITY/DIRECTIVITY: NO
SUM-RULE METHODOLOGY NOVELTY:          NO
GRAVITY-SPECIFIC CUMULATIVE INERTIA CLOSURE:
                                       PROVISIONAL GO / NO EXACT COLLISION FOUND
MANUSCRIPT AFTER CLAIM CORRECTION:     GO
PRIORITY CLAIM:                        NO
V7 MODIFICATION:                       NO
THEOREM BROADENING:                    NO FOR THIS PAPER
```

The main publication risk is now **significance rather than correctness**: a referee may reasonably view the result as a technically sound synthesis of historical gravitational-antenna physics, established wave-channel theory, passive H2 mathematics, and an established quadrupole sum rule. The manuscript must stand on whether the resulting gravity-specific cumulative inertia bound is a useful and nontrivial closure.

---

## 8. Hard stop and next epistemic step

Do **not** broaden the theorem further internally.

The next useful step is a hostile external-referee-style review focused on:

1. whether the H2-to-microscopic-gravity interface contains an unstated normalization/Markov assumption;
2. whether one-way separated TT propagation is the correct subsystem boundary in the common gravitational bath;
3. whether an equivalent cumulative two-ended theorem exists under old network, mutual-impedance, scattering, antenna-gain, or sum-rule language;
4. whether the final inertia-only closure is significant enough for publication even if technically new.

Reopen the physics only for a concrete counterexample, proof defect, exact prior-art collision, or external specialist objection.

### Forbidden claims

- first gravitational efficiency-bandwidth bound;
- new `Q`-independent gravitational response law;
- first end-to-end gravitational link bound;
- new gravitational antenna reciprocity/directivity law;
- new generic singular-channel transfer formalism;
- new use of a sum rule to constrain integrated passive response;
- universal gravitational quantum capacity bound;
- all passive matter;
- globally optimal/saturable coefficient;
- first/unique/unprecedented language without substantially stronger evidence.
