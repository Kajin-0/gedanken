# Novelty Audit — Schmidt-Rank-Two Probe Sufficiency for One-Mode Gaussian Channels

**Date:** 2026-08-07  
**Status:** **COLLISION CONFIRMED — THE PRINCIPAL RANK-TWO NOVELTY CLAIM IS RETIRED**

## 1. Previous candidate theorem

The repository independently derived the statement

> Every non-entanglement-breaking one-mode Gaussian channel admits a finite Schmidt-rank-two input whose output is NPT.

For the canonical phase-insensitive family $\Phi_{\tau,m}$ the repository obtained the particularly simple input

$$
|\psi_s\rangle
=\frac{|00\rangle+s|11\rangle}{\sqrt{1+s^2}},
\qquad s>0,
$$

and the exact principal-minor determinant

$$
\boxed{
\det M_s
=\frac{s^2}{(1+s^2)^2}
\frac{m-\tau}{(m+1)^3}.
}
$$

Hence

$$
\rho_{\rm out}\text{ NPT}
\iff
\tau>m
\iff
\Phi_{\tau,m}\text{ non-EB}.
$$

The mathematics remains useful. The novelty assessment has changed decisively.

---

## 2. Fatal prior-art collision

The decisive source is

F. A. Mele, L. Lami, and V. Giovannetti,

**“Maximum tolerable excess noise in continuous-variable quantum key distribution and improved lower bound on two-way capacities,”**

arXiv:2303.12867, first submitted 22 March 2023; later *Nature Photonics* (2025), DOI `10.1038/s41566-024-01595-9`.

Their supplementary material studies the phase-insensitive normal form

$$
\boxed{
\mathcal N_{g,\lambda}
=\Phi_{g,0}\circ\mathcal E_{\lambda,0}
}
$$

and the Schmidt-rank-two Fock-pair family

$$
\boxed{
|\Psi_{M,c}\rangle
=c|0,0\rangle+\sqrt{1-c^2}|M,M\rangle,
}
$$

with

$$
M\in\mathbb N^+,
\qquad
c\in(0,1).
$$

After local projection onto

$$
\Pi_M=|0\rangle\langle0|+|M\rangle\langle M|,
$$

Supplementary Remark 1 proves that the resulting two-qubit state is non-PPT/distillable iff

$$
\boxed{(1-\lambda)g<1,}
$$

and states explicitly that this condition is independent of $c$ and $M$.

---

## 3. Exact parameter collision

For their normal form,

$$
\tau=g\lambda,
\qquad
m=g-1
$$

in the repository's phase-insensitive convention.

Therefore

$$
(1-\lambda)g<1
$$

iff

$$
g\lambda>g-1,
$$

iff

$$
\boxed{\tau>m.}
$$

This is exactly the repository's sign boundary.

This is not merely neighboring work. It is the same finite-rank entanglement-survival phenomenon in different channel coordinates.

See the full collision note:

- `NOVELTY_COLLISION_MELE_RANK_TWO.md`

---

## 4. Fixed Bell-state result is contained as a specialization

Set

$$
M=1,
\qquad
c=1/\sqrt2.
$$

Then

$$
|\Psi_{M,c}\rangle
=\frac{|00\rangle+|11\rangle}{\sqrt2}.
$$

Thus the repository's fixed vacuum–one-photon Bell probe is already contained in the Mele family.

Likewise, arbitrary $c\in(0,1)$ contains every nonzero relative Schmidt weight in

$$
|00\rangle+s|11\rangle.
$$

Mele et al. actually prove the broader statement for all positive Fock indices $M$.

---

## 5. Why postselection does not create a novelty distinction

Mele et al. diagnose non-PPT after Bob's local projection onto $\{|0\rangle,|M\rangle\}$.

This does not leave open the possibility that the unprojected state is PPT.

If

$$
\rho^{T_A}\ge0,
$$

then for any local CP map $\Lambda_B$,

$$
[(I\otimes\Lambda_B)(\rho)]^{T_A}
=(I\otimes\Lambda_B)(\rho^{T_A})
\ge0.
$$

Therefore local filtering cannot convert PPT into NPT.

Their postselected NPT state proves that the pre-filter state was already NPT.

The repository's direct $2\times2$ determinant supplies a cleaner unfiltered certificate but does not establish a different rank-two existence theorem.

---

## 6. Revised verdict on individual claims

### COLLISION CONFIRMED — do not claim as new

- phase-insensitive Schmidt-rank-two sufficiency;
- survival of NPT for every nonzero Schmidt weight of the $|0,0\rangle$/$|1,1\rangle$ pair;
- the fixed vacuum–one-photon Bell probe as a complete non-EB detector;
- qubit-reference sufficiency for the phase-insensitive family;
- arbitrarily weak Schmidt-rank-two Fock entanglement as sufficient;
- the broad fact that a finite Fock-pair probe reaches the exact phase-insensitive EB boundary.

### Possibly useful reformulations, not currently novelty claims

- the particularly short determinant
  $$
  \det M_s\propto m-\tau;
  $$
- the explicit selected-block negativity lower bound;
- phrasing the $M=1$ result as a vacuum–one-photon Choi-subspace criterion.

A shorter proof can still be pedagogically or technically useful, but a publication would need to justify the value of the simplification rather than claim the underlying theorem as new.

---

## 7. Effect on the arbitrary one-mode theorem

For regular orientation-preserving one-mode Gaussian channels, standard Gaussian input/output unitaries reduce the channel to phase-insensitive canonical form.

Therefore rank-two sufficiency for that regular class is substantially an immediate corollary of

1. the Mele finite-Fock-pair result;
2. standard one-mode Gaussian canonical classification;
3. invariance of Schmidt rank and NPT under local unitary transformations.

The repository separately handles the singular rank-one-noise $B_1$ class through finite regularization and PPT monotonicity.

That argument appears correct:

$$
Y_{B_1}=\operatorname{diag}(b,0)
\longrightarrow
Y_\epsilon=\operatorname{diag}(b,\epsilon),
$$

with

$$
0<\epsilon<1/b
$$

so that

$$
\sqrt{b\epsilon}<1.
$$

The regularized channel is non-EB; an NPT state after the added local noise implies the same input was already NPT before that noise.

### Publication consequence

The $B_1$ closure may be a technically useful observation, but it does not currently justify presenting the broad rank-two theorem as a new standalone result.

---

## 8. Prior finite-TMSV literature remains relevant but is no longer the closest threat

De Pasquale, Mari, Porzio, and Giovannetti previously showed that finite nonzero two-mode squeezing can test Gaussian EB behavior. Such a TMSV has infinite Schmidt rank.

Before the Mele collision, this made the repository's rank-two reduction appear potentially new.

After inspection of Mele et al.'s supplementary Fock-pair protocol, that distinction no longer supports novelty: finite Schmidt rank two is already present explicitly.

---

## 9. New active novelty boundary

The research priority moves to the structurally different coherent-branch statement:

$$
\boxed{
\text{Every finite nontrivial binary coherent hybrid probe is NPT}
\iff
\text{the phase-insensitive Gaussian channel is non-EB.}
}
$$

The bosonic branch states are now nonorthogonal coherent states rather than orthogonal Fock states.

The associated exact matched principal-minor witness uses selected coherent-state matrix elements and, for symmetric $|\pm a\rangle$ with $m>0$, yields

$$
\boxed{
v_*=\frac{2\sqrt\tau a}{m},
}
$$

$$
\boxed{
\frac{|z_{v_*}|^2}{p_0p_{v_*}}
=\exp\left[\frac{4a^2}{m}(\tau-m)\right].
}
$$

No exact equivalent of this **all-finite-coherent-pairs actual-output NPT theorem** has yet been located.

That absence remains only a search result, not proof of novelty.

Files:

- `DIRECT_GAUSSIAN_BINARY_PROBE_PROOF.md`
- `EXACT_THREE_ELEMENT_WITNESS.md`
- `NOVELTY_CHECK_GAUSSIAN_BINARY_PROBE.md`
- `NOVELTY_CHECK_FINITE_CAT.md`
- `PRIOR_ART_BINARY_COHERENT_TESTS.md`

---

## 10. Required next search

Do not spend additional effort trying to establish novelty of the Fock rank-two theorem unless the question is specifically whether the repository's **short proof** itself is independently publishable.

Instead search aggressively for the coherent theorem through

- two-state effective-entanglement literature;
- hybrid qubit–coherent thermal-entanglement literature;
- papers citing Kreis–van Loock (2012);
- papers citing Häseler–Moroder–Lütkenhaus (2008);
- exact negativity/PPT calculations for hybrid cats under thermal attenuation, amplification, and additive noise;
- coherent-state principal-minor witnesses and displaced-vacuum tests;
- binary-modulated CV-QKD entanglement proofs.

Search supplements and appendices. The Mele collision demonstrates that title/abstract searches are insufficient.

---

## 11. Current conclusion

The rank-two Fock result should now be described as

> **an independent compact rederivation of an entanglement-survival property already contained in Mele–Lami–Giovannetti's finite-Fock-pair protocol.**

The previous standalone rank-two paper architecture is retired as a novelty claim.

The surviving candidate contribution is the binary coherent-state exact NPT/EB equivalence and its matched three-element witness, pending a new adversarial literature audit.
