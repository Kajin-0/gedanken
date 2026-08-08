# Claim Ledger Addendum — Post Mele and Filippov–Ziman Audits

**Date:** 2026-08-07  
**Purpose:** Canonical claim classification after two confirmed prior-art collisions.

This file supersedes earlier addenda that described either the rank-two Fock theorem or the all-binary-coherent survival theorem as active novelty candidates.

---

## A. COLLISION CONFIRMED — DO NOT CLAIM

### A12. Phase-insensitive Schmidt-rank-two Fock sufficiency

Mele–Lami–Giovannetti, arXiv:2303.12867 / *Nature Photonics* (2025), already use finite Schmidt-rank-two Fock-pair inputs

$$
|\Psi_{M,c}\rangle
=c|00\rangle+\sqrt{1-c^2}|MM\rangle
$$

and prove non-PPT/distillability exactly in the non-EB phase-insensitive region after local projection.

Their condition

$$
(1-\lambda)g<1
$$

maps under

$$
\tau=g\lambda,
\qquad
m=g-1
$$

to

$$
\tau>m.
$$

Do not claim novelty for

- phase-insensitive Schmidt-rank-two sufficiency;
- arbitrary nonzero Fock-pair Schmidt weights;
- fixed vacuum–one-photon Bell sufficiency;
- qubit-ancilla sufficiency for the phase-insensitive family;
- arbitrarily weak rank-two Fock entanglement sufficiency.

Read:

- `NOVELTY_COLLISION_MELE_RANK_TWO.md`

### A13. Binary coherent effective-entanglement/NPT architecture

Rigas–Gühne–Lütkenhaus, Häseler–Moroder–Lütkenhaus, Namiki, Killoran–Häseler–Lütkenhaus, Killoran–Lütkenhaus, Kreis–van Loock, and related work already establish

- source-replacement states based on $|\pm\alpha\rangle$;
- binary coherent channel tests;
- PPT/NPT effective-entanglement verification;
- negativity lower bounds for the same virtual hybrid state;
- thermal beam-splitter examples;
- finite coherent alphabets as strong Gaussian-channel benchmarks.

None of these broad ideas is new.

### A14. Every finite binary coherent hybrid survives iff the phase-insensitive channel is non-EB

Filippov–Ziman, *Phys. Rev. A* **90**, 010301(R) (2014), arXiv:1405.1754, study

$$
|\psi_\gamma\rangle
\propto
|\gamma\rangle|0\rangle-|0\rangle|\gamma\rangle
$$

under asymmetric phase-insensitive Gaussian channels and derive a coherent-state weighted-swap witness.

Specializing one side to the identity and tuning their witness gives, for every finite $\gamma\ne0$, a negative witness exactly when the remaining channel is non-EB.

In their variables,

$$
a=\mu-\frac12|\kappa-1|
$$

is excess noise and the EB condition is

$$
a\ge\min(\kappa,1).
$$

With their quantum-limited decomposition parameter

$$
T=
\begin{cases}
1+a,&\kappa<1,\\
\kappa+a,&\kappa>1,
\end{cases}
$$

and $t=1-\lambda>0$, the one-sided witness becomes

$$
E(t;x)=e^{-Ax}+e^{-Bx}-2e^{-Cx},
\qquad x=|\gamma|^2,
$$

where

$$
A=\frac\kappa T,
\qquad
B=1+\frac{1-T}{Tt^2},
\qquad
C=1-\frac{\sqrt\kappa}{Tt}.
$$

Choosing

$$
t^2=\frac{T-1}{T-\kappa}
$$

gives $A=B$, and the sign condition factors to

$$
(a+1)(a-\kappa)<0
\iff a<\kappa
$$

for attenuation, and

$$
(a+\kappa)(a-1)<0
\iff a<1
$$

for amplification. The additive-noise limit is $a<1$.

These are exactly the complements of the EB condition.

An invertible local filter on

$$
\operatorname{span}\{|0\rangle,|\gamma\rangle\}
$$

maps the untouched Filippov–Ziman reference to orthogonal qubit labels with arbitrary nonzero branch weights. A common displacement/rotation maps $|0\rangle,|\gamma\rangle$ to any finite distinct coherent pair.

Finite Fock truncations of their weighted-swap witness satisfy

$$
W_{\lambda,N}^{T_2}\ge0,
$$

so the one-sided negative witness can be interpreted as NPT certification; the convergent limiting expectation forces a negative finite truncation.

Therefore do not claim novelty for the underlying statement

$$
\boxed{
\text{every finite binary coherent hybrid is NPT iff the phase-insensitive channel is non-EB}.
}
$$

Read:

- `NOVELTY_COLLISION_FILIPPOV_BINARY_COHERENT.md`

---

## B. INTERNALLY DERIVED — MATHEMATICS AUDITED, POSSIBLE NOVELTY STILL UNVERIFIED

### B4. Direct coherent-dyad kernel and compressed proof

The repository independently derives

$$
\langle u|\Phi_{\tau,m}(|\alpha\rangle\langle\beta|)|v\rangle
=
\frac{\langle\beta|\alpha\rangle\langle u|v\rangle}{m+1}
\exp\left[
\frac{(\sqrt\tau\beta^*-u^*)(v-\sqrt\tau\alpha)}{m+1}
\right].
$$

The resulting all-pairs theorem is prior art in substance, but this direct proof remains much shorter than the Filippov–Ziman route.

Files:

- `DIRECT_GAUSSIAN_BINARY_PROBE_PROOF.md`
- `COHERENT_THEOREM_ADVERSARIAL_PROOF_AUDIT.md`

### B5. Exact three-element coherent-state PT witness

For symmetric $|\pm a\rangle$, one literal $2\times2$ block of the actual partial transpose is

$$
M_\Gamma
=\begin{pmatrix}
p_0&z_v^*\\
z_v&p_v
\end{pmatrix}.
$$

The condition

$$
|z_v|^2>p_0p_v
$$

certifies NPT.

For $m>0$, the exact matched analysis displacement is

$$
\boxed{
v_*=\frac{2\sqrt\tau a}{m},
}
$$

and

$$
\boxed{
\frac{|z_{v_*}|^2}{p_0p_{v_*}}
=\exp\left[\frac{4a^2}{m}(\tau-m)\right].
}
$$

This exposes the full EB boundary from only two populations and one coherence.

File:

- `EXACT_THREE_ELEMENT_WITNESS.md`

**Current status:** strongest surviving novelty candidate, unverified.

### B6. Absolute selected-block negativity strength

The negative eigenvalue of the selected block gives

$$
G(v)=\frac12
\max\left\{0,
\sqrt{(p_0-p_v)^2+4|z_v|^2}
-(p_0+p_v)
\right\}.
$$

The repository derives optimized weak-link asymptotics and explicit constants.

Files:

- `ABSOLUTE_THREE_ELEMENT_WITNESS_GAP.md`
- `WEAK_LINK_ABSOLUTE_GAP_ASYMPTOTIC.md`

**Current status:** quantitative novelty unverified.

---

## C. ACTIVE PUBLICATION QUESTION

The broad survival theorems are dead as novelty claims.

The only defensible standalone question is now:

> **Is the full phase-insensitive binary-coherent NPT boundary reducible to an exact three-matrix-element $2\times2$ PT principal minor in a way that is genuinely new and useful relative to Filippov–Ziman's weighted-swap witness and earlier EVM/moment criteria?**

A possible paper, if this survives, must be framed as

- minimal exact certification;
- proof compression;
- closed-form matched analysis displacement;
- possibly an exact absolute witness-strength bound.

It must not be framed as discovery of binary coherent entanglement survival.

---

## D. CURRENT STOP/GO

### STOP

- rank-two Fock survival novelty paper;
- all-binary-coherent survival novelty paper;
- broad coherent-state benchmarking novelty claims.

### GO

1. search for exact $2\times2$ coherent-state PT principal-minor prior art;
2. try to derive the repository three-element witness directly from Filippov–Ziman's weighted-swap witness;
3. audit absolute selected-block strength formulas;
4. only then decide whether a narrow note is worth writing;
5. if not, return focus to the gravity application.
