# Current State Addendum — Rank-Two Gaussian Theorem

**Date:** 2026-08-07  
**Purpose:** Latest recovery point after the Schmidt-rank-two theorem audit. Read this together with `CURRENT_STATE.md`; this addendum contains the newest result that postdates the last full canonical rewrite.

## 1. Strongest standalone result in the repository

The current strongest candidate theorem is now independent of gravity:

$$
\boxed{
\text{Every non-entanglement-breaking one-mode Gaussian channel admits a finite Schmidt-rank-two input whose output is NPT.}
}
$$

Equivalently, for one-mode Gaussian channels,

> **if a channel destroys entanglement for every Schmidt-rank-two input, then it is fully entanglement breaking.**

A qubit reference is sufficient.

Novelty remains unverified, but targeted searches have not located an equivalent theorem.

---

## 2. Short independent proof for the phase-insensitive family

For the canonical channel $\Phi_{\tau,m}$, use the fixed input

$$
\boxed{
|\psi_\lambda\rangle
=
\frac{|00\rangle+\lambda|11\rangle}
{\sqrt{1+\lambda^2}},
\qquad\lambda>0.
}
$$

After partial transpose, the subspace

$$
\{|0\rangle_R|1\rangle_B,
|1\rangle_R|0\rangle_B\}
$$

contains the block

$$
\boxed{
M_\lambda
=
\frac1{(1+\lambda^2)(m+1)^2}
\begin{pmatrix}
m&\lambda\sqrt\tau\\
\lambda\sqrt\tau&\lambda^2(m+1-\tau)
\end{pmatrix}.
}
$$

Its determinant is exactly

$$
\boxed{
\det M_\lambda
=
\frac{\lambda^2}{(1+\lambda^2)^2}
\frac{m-\tau}{(m+1)^3}.
}
$$

Therefore, for **every** $\lambda>0$,

$$
\boxed{
\rho_{\rm out}\text{ NPT}
\iff
\tau>m
\iff
\Phi_{\tau,m}\text{ non-EB}.
}
$$

This proof is structurally independent of the binary coherent-state proof.

File: `TRUNCATED_TMSV_RANK_TWO_THEOREM.md`.

---

## 3. Fixed Bell-state / two-dimensional Choi criterion

Set

$$
\lambda=1.
$$

Then the single fixed Bell state

$$
\boxed{
|\Phi_2\rangle
=\frac{|00\rangle+|11\rangle}{\sqrt2}
}
$$

in the vacuum–one-photon subspace detects the full phase-insensitive EB boundary.

The relevant channel process elements are

$$
A_{11}=\frac{m}{(m+1)^2},
$$

$$
B_{00}=\frac{m+1-\tau}{(m+1)^2},
$$

$$
X_{01}=\frac{\sqrt\tau}{(m+1)^2}.
$$

Thus

$$
\boxed{
|X_{01}|^2>A_{11}B_{00}
\iff
\tau>m.
}
$$

The full infinite-dimensional EB transition is therefore already visible in the two-dimensional vacuum–one-photon Choi truncation.

File: `TWO_DIMENSIONAL_CHOI_TRUNCATION_CRITERION.md`.

---

## 4. Exact absolute lower bound for the fixed Bell probe

The smaller eigenvalue of the selected PT block simplifies to

$$
\boxed{
\mu_-^{(01)}
=\frac{m-\tau}{2(m+1)^2}.
}
$$

Hence

$$
\boxed{
\mathcal N(\rho_{\rm out})
\ge
\frac{[\tau-m]_+}{2(m+1)^2}.
}
$$

For pure loss this selected block gives the exact negativity of the Bell-state output.

---

## 5. Complete one-mode Gaussian extension

Use the one-mode identity

$$
K^T\Omega K=(\det K)\Omega
$$

and Holevo's Gaussian CP/EB matrix criteria.

Canonical-class audit:

- $\det K=0$: every physical channel is EB.
- $\det K<0$: every physical orientation-reversing/phase-conjugating channel is EB.
- $\det K>0$, full-rank noise: Gaussian-unitarily equivalent to phase-insensitive canonical form; pull the rank-two Fock probe back through the common input Gaussian unitary.
- Gaussian-unitary boundary: trivial.
- singular $B_1$ rank-one noise: finite regularization plus PPT monotonicity supplies a finite rank-two NPT probe.

Thus every non-EB one-mode Gaussian channel is covered.

Files:

- `COMPLETE_ONE_MODE_GAUSSIAN_TWO_BRANCH_PROBE_THEOREM.md`
- `ONE_MODE_GAUSSIAN_CANONICAL_CLASS_PROOF_AUDIT.md`
- `CONSTRUCTIVE_B1_FINITE_PROBE.md`

---

## 6. Constructive singular $B_1$ probe

For

$$
Y_{B_1}=\operatorname{diag}(b,0),
\qquad b>0,
$$

choose any

$$
0<y<1
$$

and add finite local post-processing noise

$$
\epsilon=y^2/b
$$

in the clean quadrature.

The regularized channel has isotropic canonical noise $y<1$ and is non-EB.

The required matched input squeezing is finite:

$$
\boxed{
r=\frac12\ln\frac{b}{y}.
}
$$

If the original $B_1$ output were PPT, local post-processing could not turn it into the NPT regularized output. Therefore the original channel already preserves NPT for the same finite rank-two probe.

---

## 7. Stronger pure-Gaussian-branch result remains separate

The rank-two theorem above does **not** require Gaussian branch states; its shortest proof uses canonical $|0\rangle$ and $|1\rangle$.

A stronger result derived earlier remains:

> Every non-EB one-mode Gaussian channel admits a rank-two probe whose two bosonic branches are displaced copies of one finite-covariance pure Gaussian state.

For the phase-insensitive family the stronger statement is:

> **every finite nontrivial binary coherent hybrid probe works.**

This stronger theorem relies on the coherent-state principal-minor proof and canonicalization.

---

## 8. Arbitrarily weak rank-two entanglement

For

$$
|\psi_\lambda\rangle
\propto
|00\rangle+\lambda|11\rangle,
$$

the input entanglement tends to zero as

$$
\lambda\to0^+.
$$

But the PT determinant remains negative for every finite $\lambda>0$ whenever the channel is non-EB.

Thus

$$
\boxed{
\text{arbitrarily weak Schmidt-rank-two entanglement suffices.}
}
$$

This is not meant to supersede the known arbitrarily weak finite-TMSV result; the candidate novelty is fixing Schmidt rank to two.

File: `ARBITRARILY_WEAK_RANK_TWO_GAUSSIAN_PROBES.md`.

---

## 9. Prior-art status

Known neighboring results:

- finite-squeezing TMSV states can test Gaussian EB behavior;
- arbitrarily weak finite squeezing can suffice;
- coherent-state ensemble benchmarks can certify quantum-domain behavior of all one-mode Gaussian channels;
- general Schmidt-number / partially-entanglement-breaking channel theory exists.

Targeted searches have not located:

1. universal Schmidt-rank-two sufficiency for one-mode Gaussian EB testing;
2. the exact vacuum–one-photon Choi truncation criterion for the full phase-insensitive EB boundary;
3. the stronger all-finite-coherent-pairs NPT/EB equivalence;
4. the exact minimal coherent-state three-element witness.

This is not proof of novelty.

Files:

- `NOVELTY_AUDIT_SCHMIDT_RANK_TWO_GAUSSIAN_PROBE.md`
- `NOVELTY_ADDENDUM_COHERENT_BENCHMARKS_VS_RANK_TWO.md`

---

## 10. Independent numerical audit

The phase-insensitive theorem is now checked by:

1. analytic coherent-state proof;
2. pure-loss edge proof;
3. direct thermal-loss dilation;
4. explicit thermal-amplifier Stinespring simulation;
5. explicit additive random-displacement simulation;
6. independent truncated-TMSV analytic proof.

File:

- `NUMERICAL_AUDIT_AMPLIFIER_ADDITIVE_NOISE.md`

---

## 11. Current publication priority

If novelty survives expert review, the cleanest publication order is now:

### Paper A — standalone theorem

**Schmidt-Rank-Two Probes Suffice to Detect Entanglement Breaking in One-Mode Gaussian Channels**

Preferred architecture:

- `PAPER_CORE_RANK_TWO_GAUSSIAN_EB_V2.md`

### Paper B — gravity application

Use Paper A as a lemma in the source-resolved gravitational receiver calculation in `PAPER_CORE_V3.md`.

---

## 12. Strongest next step

The internal mathematics is now substantially stronger than the novelty evidence.

Next priority:

1. expert-level literature review of finite Choi truncations / ancilla dimension for Gaussian EB;
2. independent human proof review;
3. only then prepare a standalone manuscript.

For the gravity application, the strongest remaining technical check is the exact conserved actuator/control stress-energy, not another receiver architecture.