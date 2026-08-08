# Claim Ledger Addendum — Post-Mele Prior-Art Audit

**Date:** 2026-08-07  
**Purpose:** Update the canonical claim ledger after the confirmed Mele–Lami–Giovannetti rank-two collision and the subsequent equation-level binary-coherent prior-art audit.

This addendum supersedes any older claim-ledger language that describes Schmidt-rank-two Fock sufficiency as candidate novelty.

---

## A. COLLISION CONFIRMED — DO NOT CLAIM

### A12. Phase-insensitive Schmidt-rank-two Fock sufficiency

Mele–Lami–Giovannetti, arXiv:2303.12867 / *Nature Photonics* (2025), use

$$
|\Psi_{M,c}\rangle
=c|0,0\rangle+\sqrt{1-c^2}|M,M\rangle,
$$

with arbitrary

$$
M\ge1,
\qquad
0<c<1,
$$

and prove after a local $\{|0\rangle,|M\rangle\}$ projection that the state is non-PPT/distillable exactly when their phase-insensitive Gaussian channel is non-EB.

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
\boxed{\tau>m.}
$$

Therefore do not claim novelty for

- phase-insensitive Schmidt-rank-two sufficiency;
- arbitrary nonzero Schmidt weights in the Fock-pair family;
- the fixed vacuum–one-photon Bell probe;
- qubit ancilla sufficiency for the phase-insensitive family;
- arbitrarily weak Schmidt-rank-two Fock entanglement sufficiency.

Canonical collision note:

- `NOVELTY_COLLISION_MELE_RANK_TWO.md`

### A13. Binary coherent effective-entanglement/NPT architecture

Rigas–Gühne–Lütkenhaus (2006), Namiki (2008), Häseler–Moroder–Lütkenhaus (2008), Killoran–Häseler–Lütkenhaus (2010), and related work already establish

- source-replacement states of the form
  $$
  \sqrt{p_0}|0\rangle|\alpha\rangle
  +\sqrt{p_1}|1\rangle|-\alpha\rangle;
  $$
- binary coherent-state prepare-and-measure channel tests;
- PPT/NPT-based effective-entanglement verification;
- negativity lower bounds for the same virtual hybrid state;
- thermal beam-splitter noise as a test channel;
- displaced coherent-state/vacuum projections;
- finite coherent alphabets as strong EB/non-EB channel benchmarks.

None of these broad ideas is candidate novelty.

---

## B. INTERNALLY DERIVED — MATHEMATICS AUDITED, NOVELTY UNVERIFIED

### B4. Every finite binary coherent pair detects the exact phase-insensitive EB boundary

For

$$
|\Psi\rangle
=\sqrt p|0\rangle|\alpha\rangle
+e^{i\phi}\sqrt{1-p}|1\rangle|\beta\rangle,
$$

with

$$
0<p<1,
\qquad
\alpha\ne\beta,
$$

the repository derives

$$
\boxed{
(I\otimes\Phi_{\tau,m})(|\Psi\rangle\langle\Psi|)
\text{ NPT}
\iff
\tau>m.
}
$$

For symmetric real $|\pm a\rangle$ and $m>0$,

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

Pure loss is covered separately by a finite witness displacement.

Files:

- `DIRECT_GAUSSIAN_BINARY_PROBE_PROOF.md`
- `PURE_LOSS_EDGE_CASE.md`

**Current status:** candidate novelty, unverified.

### B5. Exact three-element coherent-state PT witness

A selected block

$$
M_\Gamma
=\begin{pmatrix}
p_0&z_v^*\\
z_v&p_v
\end{pmatrix}
$$

inside the output partial transpose satisfies

$$
\boxed{|z_v|^2>p_0p_v}
$$

exactly at the channel non-EB boundary when $v=v_*$.

This gives an iff channel/state test from two selected populations and one coherence rather than a restricted first/second-moment SDP.

File:

- `EXACT_THREE_ELEMENT_WITNESS.md`

**Current status:** candidate novelty, unverified.

---

## C. IMPORTANT PRIOR-ART NEAR MISSES — DO NOT OVERSTATE THE DIFFERENCE

### C1. Rigas–Gühne–Lütkenhaus (2006)

They use the exact symmetric binary coherent hybrid state and PPT/EVM criteria.

For their symmetric Gaussian-noise example they identify the necessary relation

$$
\delta<2\eta,
\qquad
\delta=\sigma^2-1.
$$

For a thermal attenuator,

$$
\delta=2(1-\eta)\bar n,
$$

so this becomes

$$
\boxed{
\bar n<\frac{\eta}{1-\eta},
}
$$

the exact non-EB boundary.

However, their **actual detection curves remain overlap-dependent and sufficient**, not an exact all-pair actual-state theorem.

### C2. Namiki (2008)

Explicitly describes the earlier binary-coherent virtual-state criterion as NPT based and develops a two-nonorthogonal-state quantum-domain benchmark.

### C3. Killoran–Häseler–Lütkenhaus (2010)

Use the same virtual hybrid state, negativity, and a thermal beam-splitter test channel. They state that their lower bounds do not provide the full entanglement picture and become trivial before all verifiable entanglement disappears.

### C4. Häseler–Lütkenhaus (2010)

Show that three coherent states can produce an optimal-strength channel benchmark for the lossy thermal-noise model. Therefore the candidate novelty is not “few coherent states reach an EB boundary.”

### C5. Kreis–van Loock (2012)

Study the same balanced hybrid state through thermal photon noise and give an amplitude-dependent sufficient Shchukin–Vogel witness, explicitly leaving part of the non-EB region undetected.

Detailed audit:

- `COHERENT_PRIOR_ART_DEEP_AUDIT.md`

---

## D. ACTIVE PUBLICATION QUESTION

The only currently defensible standalone mathematical candidate in this branch is the narrow exact-completion statement:

> **For a known phase-insensitive one-mode Gaussian channel, every finite nontrivial binary coherent hybrid source-replacement state is NPT exactly in the channel's non-entanglement-breaking region, and one matched coherent-state $2\times2$ PT minor detects this iff boundary.**

This is not yet an originality claim.

Before publication, the project must exhaust citation-forward searches from

- Rigas et al. (2006);
- Häseler et al. (2008);
- Namiki (2008);
- Killoran et al. (2010);
- Kreis–van Loock (2012).

Search supplements, dissertations, follow-up QKD papers, and hybrid-entanglement papers for exact state-level PPT/NPT calculations.

---

## E. CURRENT STOP/GO

### STOP

- old rank-two Fock standalone novelty paper;
- broad claims that binary coherent states or NPT-based effective-entanglement tests are new;
- broad claims that a finite coherent alphabet can newly benchmark the Gaussian EB boundary.

### GO

- exact all-binary-coherent-pairs theorem adversarial audit;
- exact three-element witness adversarial audit;
- independent analytic proof rederivation;
- reproducible amplifier/additive-noise numerical implementations;
- gravity only after the above novelty question is substantially resolved.
