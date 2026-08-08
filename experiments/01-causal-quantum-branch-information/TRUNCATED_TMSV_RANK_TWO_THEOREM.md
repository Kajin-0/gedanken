# Truncated-TMSV Rank-Two Theorem

**Date:** 2026-08-07  
**Status:** Independent proof of Schmidt-rank-two sufficiency for phase-insensitive Gaussian channels. This proof does not use coherent branch states and substantially strengthens the audit of the standalone theorem candidate.

## 1. Fixed Schmidt-rank-two input

Consider the normalized state

$$
\boxed{
|\psi_\lambda\rangle
=
\frac{|0\rangle_R|0\rangle_A
+\lambda|1\rangle_R|1\rangle_A}
{\sqrt{1+\lambda^2}},
\qquad
\lambda>0.
}
$$

This is precisely the first two Schmidt terms of a two-mode squeezed vacuum, but with all higher Fock components removed.

Its Schmidt rank is exactly

$$
\boxed{2.}
$$

The reference system can therefore be a qubit.

---

## 2. Phase-insensitive Gaussian channel

Use the same channel convention as the coherent theorem:

$$
\chi_{\Phi_{\tau,m}(O)}(\xi)
=
\chi_O(\sqrt\tau\xi)
\exp\left[-\frac{2m+1-\tau}{2}|\xi|^2\right].
$$

The established entanglement-breaking boundary is

$$
\boxed{
\Phi_{\tau,m}\in\mathrm{EB}
\iff
m\ge\tau.
}
$$

We show that the one fixed rank-two family $|\psi_\lambda\rangle$ detects exactly the same boundary for **every** $\lambda>0$.

---

## 3. Output block form

Define

$$
A
=\Phi(|0\rangle\langle0|),
$$

$$
B
=\Phi(|1\rangle\langle1|),
$$

$$
X
=\Phi(|0\rangle\langle1|).
$$

The output is

$$
\rho_{RB}
=\frac1{1+\lambda^2}
\begin{pmatrix}
A&\lambda X\\
\lambda X^\dagger&\lambda^2B
\end{pmatrix}
$$

in the reference basis $\{|0\rangle,|1\rangle\}$.

After partial transpose on the reference qubit,

$$
\boxed{
\rho_{RB}^{T_R}
=\frac1{1+\lambda^2}
\begin{pmatrix}
A&\lambda X^\dagger\\
\lambda X&\lambda^2B
\end{pmatrix}.
}
$$

---

## 4. Only three Fock matrix elements are needed

Compress $\rho^{T_R}$ to the two-dimensional subspace

$$
\boxed{
\{|0\rangle_R|1\rangle_B,
\ |1\rangle_R|0\rangle_B\}.
}
$$

The compressed matrix is

$$
M_\lambda
=\frac1{1+\lambda^2}
\begin{pmatrix}
\langle1|A|1\rangle
&
\lambda\langle1|X^\dagger|0\rangle
\\
\lambda\langle0|X|1\rangle
&
\lambda^2\langle0|B|0\rangle
\end{pmatrix}.
$$

We need only

1. $\langle1|\Phi(|0\rangle\langle0|)|1\rangle$;
2. $\langle0|\Phi(|1\rangle\langle1|)|0\rangle$;
3. $\langle0|\Phi(|0\rangle\langle1|)|1\rangle$.

---

## 5. Vacuum output element

The channel sends vacuum to a thermal state of mean occupation $m$:

$$
\Phi(|0\rangle\langle0|)
=
\sum_{n=0}^{\infty}
\frac{m^n}{(m+1)^{n+1}}
|n\rangle\langle n|.
$$

Therefore

$$
\boxed{
\langle1|A|1\rangle
=
\frac{m}{(m+1)^2}.
}
$$

---

## 6. One-photon input, vacuum output probability

Use the coherent-state vacuum-output probability

$$
\langle0|
\Phi(|\alpha\rangle\langle\alpha|)
|0\rangle
=
\frac1{m+1}
\exp\left[-\frac{\tau|\alpha|^2}{m+1}\right].
$$

Expand

$$
|\alpha\rangle\langle\alpha|
=e^{-|\alpha|^2}
\left[
|0\rangle\langle0|
+|\alpha|^2|1\rangle\langle1|
+\text{terms linear in }\alpha,\alpha^*
+O(|\alpha|^3)
\right].
$$

Phase covariance makes the linear contributions vanish in the output vacuum diagonal matrix element.

Comparing the coefficient of $|\alpha|^2$ gives

$$
\boxed{
\langle0|B|0\rangle
=
\frac{m+1-\tau}{(m+1)^2}.
}
$$

Physical complete positivity guarantees this quantity is nonnegative.

---

## 7. One-quantum coherence transfer

Use the exact coherent-dyad matrix element from `DIRECT_GAUSSIAN_BINARY_PROBE_PROOF.md`:

$$
\langle u|
\Phi(|\alpha\rangle\langle\beta|)
|v\rangle
=
\frac{\langle\beta|\alpha\rangle\langle u|v\rangle}{m+1}
\exp\left[
\frac{(\sqrt\tau\beta^*-u^*)(v-\sqrt\tau\alpha)}{m+1}
\right].
$$

Set

$$
\alpha=0,
\qquad
u=0,
$$

and expand to first order in

$$
\beta^*v.
$$

The coefficient is exactly the desired Fock coherence:

$$
\boxed{
\langle0|X|1\rangle
=
\frac{\sqrt\tau}{(m+1)^2}.
}
$$

Thus

$$
\boxed{
|\langle0|X|1\rangle|^2
=
\frac{\tau}{(m+1)^4}.
}
$$

---

## 8. Exact $2\times2$ partial-transpose block

Substituting the three elements gives

$$
\boxed{
M_\lambda
=
\frac{1}{(1+\lambda^2)(m+1)^2}
\begin{pmatrix}
m&\lambda\sqrt\tau\\
\lambda\sqrt\tau&
\lambda^2(m+1-\tau)
\end{pmatrix}.
}
$$

Its determinant is

$$
\det M_\lambda
=
\frac{\lambda^2}{(1+\lambda^2)^2(m+1)^4}
\left[
m(m+1-\tau)-\tau
\right].
$$

But

$$
m(m+1-\tau)-\tau
=(m+1)(m-\tau).
$$

Therefore

$$
\boxed{
\det M_\lambda
=
\frac{\lambda^2}{(1+\lambda^2)^2}
\frac{m-\tau}{(m+1)^3}.
}
$$

This is the central identity.

---

## 9. Exact NPT/EB equivalence

For every

$$
\lambda>0,
$$

all prefactors in the determinant are positive except

$$
m-\tau.
$$

Thus

$$
\boxed{
\det M_\lambda<0
\iff
\tau>m.
}
$$

A negative principal minor of $\rho^{T_R}$ implies NPT.

Conversely, if

$$
m\ge\tau,
$$

the channel is EB and every output is separable.

Hence

$$
\boxed{
(I\otimes\Phi_{\tau,m})(|\psi_\lambda\rangle\langle\psi_\lambda|)
\text{ is NPT}
\iff
\Phi_{\tau,m}\text{ is non-EB}
}
$$

for **every** finite

$$
\lambda>0.
$$

This includes pure loss without a special singular analysis.

---

## 10. Explicit negative eigenvalue lower bound

The smaller eigenvalue of the compressed PT block is

$$
\boxed{
\mu_-(\lambda;\tau,m)
=
\frac{
 m+\lambda^2(m+1-\tau)
-
\sqrt{
[m-\lambda^2(m+1-\tau)]^2
+4\lambda^2\tau
}
}
{2(1+\lambda^2)(m+1)^2}.
}
$$

Therefore

$$
\boxed{
\mathcal N(\rho_{RB})
\ge
[-\mu_-]_+.
}
$$

This gives an explicit absolute rank-two witness strength without any coherent-state analysis displacement.

---

## 11. Arbitrarily weak input entanglement

The Schmidt coefficients of $|\psi_\lambda\rangle$ are

$$
\frac1{\sqrt{1+\lambda^2}},
\qquad
\frac{\lambda}{\sqrt{1+\lambda^2}}.
$$

As

$$
\lambda\to0^+,
$$

the input entanglement tends to zero continuously.

But the determinant remains negative for every finite

$$
\lambda>0
$$

whenever

$$
\tau>m.
$$

Thus phase-insensitive non-EB channels can be witnessed with **arbitrarily weak Schmidt-rank-two entanglement** using this fixed Fock-pair family.

---

## 12. Relation to finite-TMSV prior art

A finite-squeezing TMSV is

$$
|\mathrm{TMSV}(r)\rangle
=\sqrt{1-\lambda^2}
\sum_{n=0}^\infty
\lambda^n|n,n\rangle,
$$

with

$$
\lambda=\tanh r.
$$

De Pasquale et al. show that any finite nonzero $r$ is sufficient in principle to test Gaussian EB behavior.

The present result shows something sharper for the phase-insensitive family:

$$
\boxed{
\text{discard every Schmidt term above }n=1;
\text{ the exact EB boundary is still detected.}
}
$$

Thus the infinite Schmidt tail of the TMSV is unnecessary for this purpose.

---

## 13. Independent proof value

This theorem is structurally different from the binary coherent proof.

### Coherent proof

- bosonic branches are nonorthogonal coherent states;
- exact witness uses coherent-state matrix elements;
- gives the strong statement that **every** nontrivial finite coherent pair works.

### Truncated-TMSV proof

- bosonic branches are orthogonal $|0\rangle,|1\rangle$;
- one fixed PT Fock block detects the boundary;
- directly proves Schmidt-rank-two sufficiency.

The two derivations converge on the same channel boundary from different input families.

This makes an unnoticed algebraic artifact in the rank-two conclusion substantially less likely.

---

## 14. Extension to arbitrary one-mode Gaussian channels

For every regular orientation-preserving one-mode Gaussian channel, Gaussian input/output unitaries reduce the channel to the phase-insensitive canonical form.

Apply the fixed canonical rank-two input

$$
|0\rangle_R|0\rangle_A
+\lambda|1\rangle_R|1\rangle_A.
$$

Pull the bosonic input basis back through the common canonicalizing Gaussian unitary.

The original-channel probe is therefore

$$
\boxed{
|\Psi_{\lambda,\mathcal N}\rangle
\propto
|0\rangle_RU_G|0\rangle_A
+\lambda|1\rangle_RU_G|1\rangle_A.
}
$$

Its Schmidt rank remains two because $U_G|0\rangle$ and $U_G|1\rangle$ remain orthogonal.

For the singular $B_1$ class, the finite regularization/PPT-monotonicity argument applies exactly as in `CONSTRUCTIVE_B1_FINITE_PROBE.md`.

Thus this provides a second proof route to the general statement:

$$
\boxed{
\text{every non-EB one-mode Gaussian channel admits a finite Schmidt-rank-two NPT probe}.
}
$$

Unlike the stronger equal-covariance pure-Gaussian-branch theorem, the pulled-back $U_G|1\rangle$ branch is generally non-Gaussian. The two results should therefore be kept distinct.

---

## 15. Strongest current theorem hierarchy

### Theorem A — universal rank-two sufficiency

Every non-EB one-mode Gaussian channel admits a finite Schmidt-rank-two NPT probe.

Shortest proof route: truncated TMSV + canonical classes.

### Theorem B — Gaussian-branch sufficiency

Every non-EB one-mode Gaussian channel admits a finite rank-two probe whose bosonic branches are two displaced equal-covariance pure Gaussian states.

Proof route: binary coherent theorem + canonicalization + $B_1$ regularization.

### Theorem C — phase-insensitive all-pairs theorem

Every finite nontrivial binary coherent hybrid probe is NPT iff the phase-insensitive channel is non-EB.

These are nested but logically distinct claims.

---

## 16. Novelty warning

The truncated-TMSV result is simple enough that it may exist implicitly or explicitly in older Gaussian-channel work.

The strongest literature search should now include

- truncated two-mode squeezed state Gaussian channel EB;
- two-Fock-level ancilla test of Gaussian EB;
- $|00\rangle+\lambda|11\rangle$ through thermal Gaussian channels;
- finite-dimensional Choi truncations of bosonic Gaussian channels.

No originality claim should be made until that search is exhausted.