# Novelty Collision — Mele–Lami–Giovannetti and the Rank-Two Fock Theorem

**Date:** 2026-08-07  
**Status:** **COLLISION CONFIRMED — DO NOT CLAIM THE PHASE-INSENSITIVE RANK-TWO FOCK RESULT AS NOVEL**

## 1. Result that was under novelty audit

The repository independently derived, for the phase-insensitive one-mode Gaussian channel $\Phi_{\tau,m}$,

$$
\chi_{\Phi_{\tau,m}(O)}(\xi)
=\chi_O(\sqrt\tau\xi)
\exp[-(2m+1-\tau)|\xi|^2/2],
$$

that the Schmidt-rank-two state

$$
|\psi_s\rangle
=\frac{|00\rangle+s|11\rangle}{\sqrt{1+s^2}},
\qquad s>0,
$$

has an NPT output iff

$$
\boxed{\tau>m,}
$$

which is exactly the channel's non-entanglement-breaking region.

The repository's compact proof uses the partial-transpose block

$$
M_s=
\frac{1}{(1+s^2)(m+1)^2}
\begin{pmatrix}
m&s\sqrt\tau\\
s\sqrt\tau&s^2(m+1-\tau)
\end{pmatrix}
$$

and

$$
\boxed{
\det M_s
=\frac{s^2}{(1+s^2)^2}
\frac{m-\tau}{(m+1)^3}.
}
$$

This mathematics still appears correct.

The novelty claim does not survive.

---

## 2. Prior-art source

F. A. Mele, L. Lami, and V. Giovannetti,

**“Maximum tolerable excess noise in continuous-variable quantum key distribution and improved lower bound on two-way capacities,”**

arXiv:2303.12867, first submitted 22 March 2023; later published in *Nature Photonics* (2025), DOI `10.1038/s41566-024-01595-9`.

The relevant material is in the supplementary analysis, especially Definition 1 / equations (S64) onward and Supplementary Remark 1 around equations (S161)–(S165).

---

## 3. Their canonical phase-insensitive channel

Mele–Lami–Giovannetti define

$$
\boxed{
\mathcal N_{g,\lambda}
=\Phi_{g,0}\circ\mathcal E_{\lambda,0},
}
$$

where

- $\mathcal E_{\lambda,0}$ is a quantum-limited pure-loss channel of transmissivity $\lambda$;
- $\Phi_{g,0}$ is a quantum-limited amplifier of gain $g$.

Their covariance transformation shows that the composite channel has amplitude/intensity parameter

$$
\boxed{\tau=g\lambda}
$$

in the repository convention.

Because vacuum passes through the pure-loss stage unchanged and a quantum-limited amplifier of gain $g$ produces vacuum-output occupation

$$
\boxed{m=g-1,}
$$

the parameter mapping is

$$
\boxed{
(\tau,m)=(g\lambda,g-1).
}
$$

---

## 4. Their finite Schmidt-rank-two input family

Their explicit protocol uses

$$
\boxed{
|\Psi_{M,c}\rangle
=c|0,0\rangle+\sqrt{1-c^2}|M,M\rangle,
}
$$

for arbitrary

$$
M\in\mathbb N^+,
\qquad
c\in(0,1).
$$

Bob locally projects his output onto

$$
\boxed{
\Pi_M=|0\rangle\langle0|+|M\rangle\langle M|.
}
$$

Thus their postselected output is a genuine two-qubit state.

---

## 5. Supplementary Remark 1 is the decisive collision

Mele–Lami–Giovannetti evaluate the partial transpose of the projected state and obtain a condition equivalent to

$$
f_{M,0,0}f_{M,M,0}
<
f_{0,M,M}f_{0,0,M}.
$$

Using their explicit coefficients, they reduce this to

$$
\boxed{(1-\lambda)g<1.}
$$

They state that the postselected state is non-PPT/distillable iff this inequality holds, **independently of both $c$ and $M$**.

The condition is also exactly their non-EB condition for $\mathcal N_{g,\lambda}$.

---

## 6. Exact mapping to the repository boundary

Using

$$
\tau=g\lambda,
\qquad
m=g-1,
$$

we have

$$
(1-\lambda)g<1
$$

iff

$$
g-g\lambda<1,
$$

iff

$$
g-1<g\lambda,
$$

iff

$$
\boxed{m<\tau.}
$$

Therefore their analytic condition and the repository determinant condition are the same boundary in different parameterizations.

---

## 7. The repository fixed Bell probe is a direct specialization

Take

$$
M=1,
\qquad
c=1/\sqrt2.
$$

Then their state becomes

$$
\boxed{
|\Psi_{1,1/\sqrt2}\rangle
=\frac{|00\rangle+|11\rangle}{\sqrt2}.
}
$$

This is exactly the repository's fixed vacuum–one-photon Bell probe.

Likewise, arbitrary $c\in(0,1)$ maps to the repository's arbitrary nonzero Schmidt-weight family after writing

$$
s=\frac{\sqrt{1-c^2}}{c}.
$$

Thus the statement that every nonzero Schmidt weight works is also contained in their result.

---

## 8. Why their local projection does not rescue novelty

One apparent distinction is that Mele et al. explicitly apply the local projector $\Pi_M$, whereas the repository proves an NPT principal minor directly in the unfiltered output.

This does not produce a distinct existence theorem.

Suppose the unfiltered output $\rho_{AB}$ were PPT:

$$
\rho_{AB}^{T_A}\ge0.
$$

For any local CP map $\Lambda_B$,

$$
[(I\otimes\Lambda_B)(\rho_{AB})]^{T_A}
=(I\otimes\Lambda_B)(\rho_{AB}^{T_A})
\ge0.
$$

Therefore local filtering cannot transform a PPT state into an NPT state.

Since the Mele postselected state is NPT in the non-EB region, the unfiltered state was already NPT.

The repository's direct determinant is a cleaner witness of that fact, but not a new underlying rank-two sufficiency theorem.

---

## 9. Claims killed by this collision

The following should no longer be presented as candidate discoveries for phase-insensitive Gaussian channels:

1. Schmidt-rank-two input suffices to expose every non-EB channel in the family.
2. Arbitrarily weak nonzero Schmidt-rank-two entanglement suffices.
3. The $|00\rangle+s|11\rangle$ family works for every $s>0$.
4. The fixed Bell state $(|00\rangle+|11\rangle)/\sqrt2$ reaches the exact EB boundary.
5. A reference qubit is sufficient for this family.
6. The vacuum–one-photon sector is sufficient for the sign decision.

The last item can still be presented as a particularly concise reformulation or proof, but not as a newly discovered capability of the channel.

Mele et al. actually prove a broader Fock-pair statement because their result holds for every

$$
M\ge1.
$$

---

## 10. Effect on the arbitrary one-mode Gaussian extension

For regular orientation-preserving one-mode Gaussian channels, standard Gaussian input/output canonicalization reduces the channel to a phase-insensitive form.

Therefore the existence of a Schmidt-rank-two probe for regular channels follows essentially from

1. the Mele phase-insensitive result;
2. standard Gaussian canonical classification;
3. invariance of Schmidt rank and NPT under appropriate local Gaussian unitaries.

The repository's singular $B_1$ closure by finite added noise plus PPT monotonicity appears mathematically valid and may not be explicitly covered by the same simple reduction. However, this is now a relatively small closure argument rather than the previously advertised broad discovery.

**Current judgment:** do not submit the previous rank-two standalone paper architecture as a novelty paper.

---

## 11. What survives and should now be prioritized

This collision does **not** kill the distinct coherent-branch theorem:

$$
\boxed{
\text{every finite nontrivial binary coherent hybrid input is NPT}
\iff
\Phi_{\tau,m}\text{ is non-EB}.
}
$$

Mele et al. use orthogonal Fock branches $|0\rangle$ and $|M\rangle$, not arbitrary finite nonorthogonal coherent branches.

The surviving novelty audit should therefore concentrate on

1. the all-finite-binary-coherent-pairs theorem;
2. the exact matched three-element coherent-state principal-minor witness;
3. whether either result is implicit in earlier effective-entanglement or hybrid-entanglement literature.

Canonical files:

- `DIRECT_GAUSSIAN_BINARY_PROBE_PROOF.md`
- `PURE_LOSS_EDGE_CASE.md`
- `EXACT_THREE_ELEMENT_WITNESS.md`
- `NOVELTY_CHECK_GAUSSIAN_BINARY_PROBE.md`
- `NOVELTY_CHECK_FINITE_CAT.md`
- `PRIOR_ART_BINARY_COHERENT_TESTS.md`

---

## 12. Documentation consequence

Any file still stating that targeted searches found no rank-two equivalent must be treated as stale unless it has been updated after this collision note.

The canonical recovery source is now root `AGENTS.md` plus this file.
