# Binary Coherent Theorem — Prior-Art Audit, Second Pass

**Date:** 2026-08-07  
**Status:** **NO EXACT COLLISION FOUND IN SECOND PASS; NOVELTY STILL UNVERIFIED**

This note continues `COHERENT_PRIOR_ART_DEEP_AUDIT.md` after the first equation-level pass.

---

## 1. Claim under audit

The candidate statement is deliberately narrow:

> For a known gauge-covariant phase-insensitive one-mode Gaussian channel, every finite nontrivial binary coherent hybrid source-replacement state has NPT output iff the channel is non-entanglement-breaking, and one channel-matched coherent-state $2\times2$ principal minor detects this exact boundary.

For symmetric $|\pm a\rangle$ and $m>0$,

$$
\boxed{
v_*=\frac{2\sqrt\tau a}{m},
}
$$

$$
\boxed{
R(v_*)
=\frac{|z_{v_*}|^2}{p_0p_{v_*}}
=\exp\left[\frac{4a^2}{m}(\tau-m)\right].
}
$$

Everything broader than this has substantial prior art.

---

## 2. Killoran–Lütkenhaus (2011): stronger quantitative benchmarking still not exact state-level completion

**N. Killoran and N. Lütkenhaus**, “Strong quantitative benchmarking of quantum optical devices,” *Phys. Rev. A* **83**, 052320 (2011), arXiv:1102.3233.

This paper is an important follow-up to the earlier two-coherent-state effective-entanglement work.

### What it establishes

They explicitly describe the effective-entanglement construction

$$
|\psi^{\rm ent}\rangle
=\frac1{\sqrt d}
\sum_k |k\rangle|\psi_k\rangle,
$$

and specialize the benchmarking framework to two coherent test states

$$
\{|\alpha\rangle,|-\alpha\rangle\}.
$$

They quantify surviving entanglement using negativity and rigorous finite-Fock-subspace truncations.

They emphasize that their new method gives much stronger lower bounds than the earlier two-qubit projection and is often faithful over **nearly all** of the quantum domain.

### Why it still does not kill the candidate theorem

Their experimental information is tomographically incomplete. They therefore define a minimization over all compatible states and derive a rigorous **lower bound** on the entanglement of the unknown hybrid output.

They explicitly state that in general they cannot estimate the actual output entanglement exactly.

Thus their problem is

$$
\text{limited conditional-output data}
\longrightarrow
\text{worst-case negativity lower bound},
$$

whereas the repository theorem is

$$
\text{known Gaussian channel}
\longrightarrow
\text{exact actual-state PT matrix element}
\longrightarrow
\text{exact NPT iff boundary}.
$$

The approaches are closely related but logically different.

**Verdict:** very strong benchmark prior art; no exact collision located.

---

## 3. Kreis diploma thesis (2011/2012 version): no hidden stronger result located

**K. Kreis**, “Characterizing And Exploiting Hybrid Entanglement,” arXiv:1211.2880.

This thesis is important because it is much longer than the associated 2012 PRA paper and could have contained an unadvertised exact calculation.

The thesis itself states that all major results were carried into

Kreis and van Loock, *Phys. Rev. A* **85**, 032307 (2012).

The extended thesis material surveyed in this pass did not reveal an exact actual-state thermal-channel NPT boundary stronger than the published treatment already audited in `NOVELTY_CHECK_FINITE_CAT.md`.

**Verdict:** no additional collision found; keep the thesis in the bibliography as a close source.

---

## 4. Simon–Jaeger–Sergienko (2013): coherent entanglement witness under Gaussian cloning noise

**D. S. Simon, G. Jaeger, and A. V. Sergienko**, “Coherent State Quantum Key Distribution with Entanglement Witnessing,” arXiv:1305.3975.

They consider entangled coherent optical states subjected to Gaussian cloning/eavesdropping noise and evaluate Shchukin–Vogel-type moment determinants.

The paper explicitly distinguishes its chosen witness from a strong necessary-and-sufficient witness: a nonnegative witness value does not imply separability, and entanglement may persist after the sign crossing.

The physical state is also a two-bosonic-mode entangled coherent state rather than the repository's qubit–mode source-replacement state.

**Verdict:** relevant moment-witness neighborhood, but no exact collision.

---

## 5. Ivan–Sabapathy–Simon (2013): nonclassicality-breaking versus entanglement-breaking

**J. Solomon Ivan, K. K. Sabapathy, and R. Simon**, “Is nonclassicality-breaking the same thing as entanglement-breaking?”, arXiv:1306.5536.

They prove a deep structural relation between nonclassicality-breaking and entanglement-breaking bosonic Gaussian channels, modulo a fixed output Gaussian unitary.

This result is important because it reaches Gaussian EB boundaries without an explicit bipartite probe in its nonclassicality formulation.

However, it does **not** state or immediately imply that

$$
\text{every finite binary coherent hybrid state}
$$

remains NPT for every non-EB phase-insensitive channel.

An equivalence between channel-level nonclassicality breaking and EB does not fix the behavior of each particular nonorthogonal two-branch entangled input.

**Verdict:** structural near-neighbor; no all-pairs theorem collision found.

---

## 6. General faithful quantum-memory verification does not collapse the distinction

Later resource-theoretic work proves that complete families of tests can faithfully certify every non-entanglement-breaking memory/channel, for example

- Rosset–Buscemi–Liang, arXiv:1710.04710;
- later continuous-variable quantum-memory verification work.

These results establish the **existence of faithful channel tests** under particular trusted-input/game assumptions.

They do not imply that a fixed class consisting of every finite binary coherent hybrid source-replacement state individually has NPT output exactly throughout the phase-insensitive non-EB region.

**Verdict:** important scope boundary, not a collision.

---

## 7. Search conclusion after two passes

The literature now establishes essentially every surrounding ingredient:

1. binary coherent source-replacement states;
2. NPT/PPT-based effective-entanglement verification;
3. thermal-noise examples for the same hybrid state;
4. negativity lower bounds for the same state;
5. finite-subspace quantitative benchmarking;
6. optimal finite coherent-alphabet channel benchmarks;
7. exact Gaussian EB boundaries;
8. channel-level nonclassicality-breaking/EB relations.

What has **not** yet been located is the precise analytic completion

$$
\boxed{
\forall\,\alpha\ne\beta,\ 0<p<1:
\quad
(I\otimes\Phi_{\tau,m})(|\Psi\rangle\langle\Psi|)
\text{ NPT}
\iff
\tau>m,
}
$$

together with the exact coherent-state principal minor

$$
\boxed{
R(v_*)=\exp[4a^2(\tau-m)/m].
}
$$

This remains **absence of a located collision, not proof of novelty**.

---

## 8. Scope language for any manuscript

The manuscript must not claim:

- invention of binary coherent effective-entanglement testing;
- invention of NPT verification for the virtual hybrid state;
- that two coherent states are generally a new way to test EB channels;
- experimental-resource minimality relative to prepare-and-measure benchmarks;
- that the three selected matrix elements can be obtained from the two conditional output states alone.

The off-diagonal term contains

$$
\Phi(|a\rangle\langle-a|),
$$

so the exact three-element criterion assumes coherent access to the source-replacement/process coherence or an equivalent measurement.

The defensible potential contribution is an exact analytic property of the **actual hybrid output state**, not a new minimal-data benchmark.

---

## 9. Next literature targets

The remaining search should prioritize sources likely to contain full state calculations rather than benchmarks from incomplete data:

1. hybrid qubit–oscillator decoherence papers with exact density operators;
2. dissertations/theses citing Kreis–van Loock and Killoran–Lütkenhaus;
3. exact entanglement-negativity calculations for displaced thermal hybrid blocks;
4. binary-modulated CV-QKD entanglement-based security proofs that retain source coherence explicitly;
5. coherent-state process-tomography papers that derive off-diagonal dyad transfer kernels;
6. Shchukin–Vogel determinant hierarchies specialized far enough to recover the exact Gaussian EB threshold;
7. recent papers citing Kreis–van Loock specifically for thermal hybrid entanglement.

No originality claim should be made until these searches are substantially exhausted.
