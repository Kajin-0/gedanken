# Novelty Audit — Schmidt-Rank-Two Probe Sufficiency for One-Mode Gaussian Channels

**Date:** 2026-08-07  
**Status:** Targeted prior-art comparison for `COMPLETE_ONE_MODE_GAUSSIAN_TWO_BRANCH_PROBE_THEOREM.md`. No originality claim is made.

## 1. Candidate theorem under audit

The current project result states:

> **Every non-entanglement-breaking one-mode Gaussian channel admits a finite Schmidt-rank-two probe whose bosonic branches are two displaced copies of one finite-covariance pure Gaussian state, and whose channel output is NPT.**

Equivalently, for one-mode Gaussian channels, deciding EB versus non-EB never requires a reference system larger than a qubit if the two bosonic branch states are allowed to be channel matched.

For the phase-insensitive subclass the result is stronger: every nontrivial finite coherent pair works.

---

## 2. Important prior art: finite-energy Gaussian probes already suffice

De Pasquale, Mari, Porzio, and Giovannetti (2013), **Amendable Gaussian channels: restoring entanglement via a unitary filter**, explicitly discuss testing whether a Gaussian channel is EB with finite physical resources.

They use the equivalence between the formal maximally entangled Choi test and any full-rank local filtering of that test state.

For continuous variables they choose a finite-squeezing two-mode squeezed vacuum,

$$
|\mathrm{TMSV}(r)\rangle
=\frac1{\cosh r}
\sum_{n=0}^{\infty}
(\tanh r)^n
|n,n\rangle.
$$

They state that **arbitrary finite nonzero squeezing is sufficient in principle** to test whether the channel is EB.

Therefore the following is established prior art and must not be claimed:

$$
\boxed{
\text{finite energy / finite entanglement can suffice for Gaussian EB testing.}
}
$$

---

## 3. Why the present candidate is still structurally different

For every finite

$$
r>0,
$$

the TMSV expansion has infinitely many nonzero Schmidt coefficients.

Hence

$$
\boxed{
\operatorname{SRank}(|\mathrm{TMSV}(r)\rangle)=\infty.
}
$$

By contrast, the present probe is

$$
|\Psi_G\rangle
=\sqrt p|0\rangle|\psi_0\rangle
+e^{i\phi}\sqrt{1-p}|1\rangle|\psi_1\rangle.
$$

For

$$
0<p<1
$$

and linearly independent $|\psi_0\rangle,|\psi_1\rangle$,

$$
\boxed{
\operatorname{SRank}(|\Psi_G\rangle)=2.
}
$$

Distinct displaced pure Gaussian states are linearly independent, so the candidate test uses exactly Schmidt rank two.

Thus the real reduction is

$$
\boxed{
\text{infinite Schmidt rank TMSV test}
\longrightarrow
\text{Schmidt-rank-two matched test}.
}
$$

---

## 4. General partially-entanglement-breaking literature

There is established general theory of

- Schmidt number of infinite-dimensional states;
- partially entanglement-breaking channels;
- Schmidt-number-breaking channels.

Important examples include work by Shirokov and by Chruściński–Kossakowski.

That literature studies how channel action constrains or lowers Schmidt number and provides the correct general conceptual neighborhood for the present theorem.

The targeted searches performed so far have **not** located a result specific to one-mode Gaussian channels stating that

$$
\boxed{
\text{non-EB}
\iff
\text{survival of NPT entanglement for some finite Schmidt-rank-two pure-Gaussian-branch probe}.
}
$$

Absence from a targeted search is not proof of novelty.

---

## 5. Stronger phase-insensitive result versus generic rank-two sufficiency

Keep two theorem levels distinct.

### Phase-insensitive canonical family

For

$$
\Phi_{\tau,m},
$$

every finite nontrivial binary coherent hybrid state satisfies

$$
\boxed{
\rho_{\rm out}\text{ NPT}
\iff
\Phi_{\tau,m}\text{ non-EB}.
}
$$

This is an **all-probes-in-the-family** statement.

### Arbitrary one-mode Gaussian channel

There exists a channel-matched finite pair of equal-covariance pure Gaussian branches such that

$$
\boxed{
\rho_{\rm out}\text{ NPT}
\iff
\mathcal N\text{ non-EB}.
}
$$

This is an **existence** statement.

The latter follows from the former plus canonical-unitary reduction and a separate singular-$B_1$ argument.

---

## 6. Why Schmidt rank two is nontrivial

The definition of an EB channel quantifies over arbitrary ancilla dimensions and arbitrary entangled inputs.

In infinite dimensions, the formal maximally entangled Choi state is nonnormalizable, and finite-energy replacements such as TMSV still use an infinite-dimensional reference and infinite Schmidt rank.

The candidate theorem says that the entire one-mode Gaussian EB boundary is already visible to a reference qubit:

$$
\boxed{
\dim\mathcal H_R=2.
}
$$

Only two bosonic branch states are required.

This is a substantially stronger resource reduction than finite squeezing alone.

---

## 7. Operational interpretation

A possible experimental channel test would require only

1. a qubit reference;
2. preparation of two displaced copies of one pure Gaussian state;
3. coherent superposition of the two branches;
4. an NPT witness after the channel.

For phase-insensitive channels, the two branches can be ordinary coherent states.

For a general regular channel they are matched squeezed coherent states.

This is conceptually simpler than preparing a TMSV with two full bosonic modes, though practical implementation difficulty may differ.

---

## 8. Relation to Schmidt-number terminology

Be cautious with terminology.

“Partially entanglement-breaking channel” often refers to the Schmidt number of a channel/Choi object rather than directly to the minimum Schmidt rank of an input needed to witness non-EB behavior.

The present claim should therefore initially be worded operationally:

> **Schmidt-rank-two probe sufficiency for detecting non-EB one-mode Gaussian channels.**

Do not equate it with an existing $k$-PEB definition without a careful formal mapping.

---

## 9. Current prior-art verdict

### Definitely not new

- finite-energy EB testing of Gaussian channels;
- arbitrarily weak finite TMSV as an EB test resource;
- Gaussian-channel canonical classification;
- general Schmidt-number / partially-EB channel theory.

### Still not located in targeted search

- universal qubit-ancilla sufficiency for one-mode Gaussian EB testing;
- universal Schmidt-rank-two pure-Gaussian-branch sufficiency;
- the stronger “every finite coherent pair works” theorem for phase-insensitive channels;
- the exact three-element principal-minor witness that reaches the full phase-insensitive EB boundary.

---

## 10. Strongest next literature search

Search by the following conceptual phrases rather than by the project's terminology:

- finite Schmidt rank witness of Gaussian entanglement-breaking channels;
- ancilla dimension required to detect entanglement-breaking bosonic channels;
- Schmidt-number-breaking one-mode Gaussian channels;
- two-state / binary-state ancilla-assisted Gaussian channel certification;
- non-Gaussian finite-rank entangled probes of Gaussian noise.

If no equivalent theorem is found after citation-forward searching from the 2013 finite-TMSV paper and the Schmidt-number channel literature, the rank-two sufficiency theorem becomes the strongest standalone publication candidate in the repository.