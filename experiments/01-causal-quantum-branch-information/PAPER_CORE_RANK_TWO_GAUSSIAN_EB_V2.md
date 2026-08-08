# Paper Core V2 — Schmidt-Rank-Two Tests of One-Mode Gaussian Entanglement Breaking

**Date:** 2026-08-07  
**Status:** Preferred standalone theorem architecture after the independent truncated-TMSV proof. Novelty remains unverified.

## Working title

**Schmidt-Rank-Two Probes Suffice to Detect Entanglement Breaking in One-Mode Gaussian Channels**

Alternative:

**The First Two Schmidt Terms Are Enough for One-Mode Gaussian Entanglement-Breaking Tests**

---

## Abstract — working version

Entanglement breaking of an infinite-dimensional bosonic channel is formally defined by its action on arbitrary entangled inputs. Finite-energy tests of Gaussian channels are known using two-mode squeezed vacuum states, but every nonzero finite-squeezing TMSV has infinite Schmidt rank. We show that this infinite Schmidt tail is unnecessary for one-mode Gaussian channels. For every phase-insensitive Gaussian channel, the fixed Schmidt-rank-two family

$$
(|00\rangle+\lambda|11\rangle)/\sqrt{1+\lambda^2},
\qquad\lambda>0,
$$

has an NPT output exactly when the channel is not entanglement breaking. The proof requires only one $2\times2$ principal minor of the output partial transpose, whose determinant is proportional to $m-\tau$, the exact Gaussian EB boundary. Gaussian-unitary canonical reduction extends the result to all regular orientation-preserving one-mode Gaussian channels. The remaining singular $B_1$ class is handled by a finite-noise regularization and PPT monotonicity, while the rank-deficient and phase-conjugating canonical classes are entanglement breaking directly from the Gaussian EB criterion. Consequently, every non-EB one-mode Gaussian channel can be witnessed by a qubit ancilla and a finite Schmidt-rank-two input. We additionally prove a stronger result for phase-insensitive channels: every finite nontrivial binary coherent hybrid probe has NPT output exactly in the non-EB region, yielding an exact three-element coherent-state witness.

---

# 1. Prior-art starting point

Known:

1. Gaussian EB criteria and one-mode canonical classification.
2. Finite-squeezing TMSV states can test Gaussian EB behavior.
3. Arbitrarily weak finite squeezing can suffice in principle.
4. Coherent-state ensemble benchmarks can certify quantum-domain behavior of all one-mode Gaussian channels.
5. General Schmidt-number / partially-EB channel theory exists.

Not located in targeted search:

$$
\boxed{
\text{universal Schmidt-rank-two sufficiency for one-mode Gaussian EB testing}.
}
$$

Therefore the paper must claim only the **rank reduction**, not finite energy or operational simplicity in general.

---

# 2. Canonical phase-insensitive channel

Use

$$
\chi_{\Phi_{\tau,m}(O)}(\xi)
=\chi_O(\sqrt\tau\xi)
\exp[-(2m+1-\tau)|\xi|^2/2].
$$

The known EB boundary is

$$
\boxed{
\Phi_{\tau,m}\in\mathrm{EB}
\iff
m\ge\tau.
}
$$

---

# 3. Main rank-two probe

For any

$$
\lambda>0,
$$

define

$$
\boxed{
|\psi_\lambda\rangle
=
\frac{|0\rangle_R|0\rangle_A
+\lambda|1\rangle_R|1\rangle_A}
{\sqrt{1+\lambda^2}}.
}
$$

This state has Schmidt rank exactly two.

It is the TMSV state with every Schmidt component above $n=1$ removed.

---

# 4. Three channel matrix elements

Let

$$
A=\Phi(|0\rangle\langle0|),
$$

$$
B=\Phi(|1\rangle\langle1|),
$$

$$
X=\Phi(|0\rangle\langle1|).
$$

Only three matrix elements are needed:

$$
\boxed{
\langle1|A|1\rangle
=\frac{m}{(m+1)^2},
}
$$

$$
\boxed{
\langle0|B|0\rangle
=\frac{m+1-\tau}{(m+1)^2},
}
$$

$$
\boxed{
\langle0|X|1\rangle
=\frac{\sqrt\tau}{(m+1)^2}.
}
$$

These follow from the channel's vacuum thermal output and the coherent-state generating kernel.

---

# 5. Exact principal-minor theorem

After partial transpose on the reference qubit, restrict to

$$
\{|0\rangle_R|1\rangle_B,
|1\rangle_R|0\rangle_B\}.
$$

The compressed matrix is

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

Its determinant is

$$
\boxed{
\det M_\lambda
=
\frac{\lambda^2}{(1+\lambda^2)^2}
\frac{m-\tau}{(m+1)^3}.
}
$$

Therefore, for every

$$
\lambda>0,
$$

$$
\boxed{
\det M_\lambda<0
\iff
\tau>m.
}
$$

Hence

$$
\boxed{
(I\otimes\Phi_{\tau,m})(|\psi_\lambda\rangle\langle\psi_\lambda|)
\text{ is NPT}
\iff
\Phi_{\tau,m}\text{ is non-EB}.
}
$$

This is the central theorem.

---

# 6. Exact absolute NPT lower bound

The smaller eigenvalue of $M_\lambda$ is

$$
\boxed{
\mu_-
=
\frac{
 m+\lambda^2(m+1-\tau)
-
\sqrt{[m-\lambda^2(m+1-\tau)]^2+4\lambda^2\tau}
}
{2(1+\lambda^2)(m+1)^2}.
}
$$

Thus

$$
\boxed{
\mathcal N(\rho_{RB})
\ge[-\mu_-]_+.
}
$$

No coherent-state postselection or infinite-dimensional determinant is needed.

---

# 7. Arbitrarily weak entanglement

As

$$
\lambda\to0^+,
$$

the input entanglement tends to zero.

Yet for every finite

$$
\lambda>0,
$$

the determinant has the same sign

$$
\operatorname{sgn}(m-\tau).
$$

Therefore every non-EB phase-insensitive Gaussian channel is witnessed by arbitrarily weak Schmidt-rank-two entanglement.

This parallels the known arbitrarily weak finite-TMSV result but removes the infinite Schmidt rank.

---

# 8. Extension to regular one-mode Gaussian channels

For

$$
\det K>0,
\qquad
\det Y>0,
$$

Gaussian input/output unitaries reduce the channel to phase-insensitive canonical form.

If

$$
\Phi
=\mathcal U_{\rm out}\circ\mathcal N\circ\mathcal U_{\rm in},
$$

use the original-channel probe

$$
\boxed{
|\Psi_{\lambda,\mathcal N}\rangle
\propto
|0\rangle_RU_{\rm in}|0\rangle_A
+\lambda|1\rangle_RU_{\rm in}|1\rangle_A.
}
$$

The bosonic branch states remain orthogonal because $U_{\rm in}$ is unitary.

The Schmidt rank remains two.

The output is NPT exactly when the canonical output is NPT.

Thus every non-EB regular one-mode Gaussian channel has a finite rank-two NPT probe.

---

# 9. Canonical classes that are automatically EB

Use

$$
K^T\Omega K=(\det K)\Omega
$$

and Holevo's Gaussian EB decomposition criterion.

## $\det K=0$

Every physical channel is EB.

## $\det K<0$

Every physical orientation-reversing/phase-conjugating one-mode Gaussian channel is EB.

The paper should include the explicit matrix decomposition rather than merely cite the classification table.

---

# 10. Singular $B_1$ class

Canonical form:

$$
K=I,
$$

$$
Y=
\begin{pmatrix}b&0\\0&0\end{pmatrix}.
$$

Choose any finite

$$
0<y<1
$$

and add local post-processing noise

$$
\epsilon=y^2/b
$$

in the clean quadrature.

The regularized noise matrix has symplectic eigenvalue $y$ and is Gaussian-unitarily equivalent to the non-EB unit-gain additive channel $\Phi_{1,y}$.

The rank-two theorem supplies a finite NPT input for the regularized channel.

If the state before the added local noise were PPT, the post-processed state could not be NPT.

Hence the original $B_1$ channel already has an NPT output for the same finite rank-two input.

The required matching squeeze is finite:

$$
\boxed{
r=\frac12\ln(b/y).
}
$$

---

# 11. Complete one-mode theorem

## Theorem 2

For an arbitrary one-mode Gaussian channel $\mathcal N$,

$$
\boxed{
\mathcal N\text{ non-EB}
}
$$

iff there exists a finite Schmidt-rank-two input state with a qubit reference such that the output under

$$
I\otimes\mathcal N
$$

is NPT.

The proof is constructive in every non-EB canonical class.

---

# 12. Stronger Gaussian-branch theorem

The universal rank-two theorem above uses the canonical Fock pair $|0\rangle,|1\rangle$.

A separate stronger result holds.

For the phase-insensitive family, **every** finite nontrivial binary coherent hybrid state is NPT iff the channel is non-EB.

For every non-EB one-mode Gaussian channel, one can also choose two displaced equal-covariance pure Gaussian branches by the coherent theorem plus canonical reduction and the $B_1$ regularization argument.

These stronger structural statements should be presented as corollaries after the minimal rank-two theorem, not used as the main proof.

---

# 13. Prior-art distinction

## Known finite TMSV test

Finite-squeezing TMSV tests use

$$
\sum_{n=0}^{\infty}\lambda^n|n,n\rangle
$$

and therefore infinite Schmidt rank.

## Present rank-two result

Only

$$
|00\rangle+\lambda|11\rangle
$$

is needed in the phase-insensitive canonical coordinates.

Thus the proposed resource reduction is exactly

$$
\boxed{
\text{infinite Schmidt tail is unnecessary.}
}
$$

## Coherent-state benchmarks

Namiki–Azuma and other benchmark work already show that coherent-state ensembles can certify quantum-domain Gaussian-channel behavior.

Therefore the paper should not claim experimental-resource minimality in a broad sense.

The theorem is a statement about **single-state Schmidt rank / ancilla dimension**.

---

# 14. Potential strongest headline

If novelty survives literature review, the cleanest theorem statement is:

> **For one-mode Gaussian channels, breaking all Schmidt-rank-two entanglement is equivalent to being fully entanglement breaking.**

Operationally:

> **A qubit ancilla is enough to detect every non-entanglement-breaking one-mode Gaussian channel.**

The first wording is mathematically sharper; the second is more intuitive.

---

# 15. Submission-critical novelty searches

Search specifically for

- two-dimensional Choi truncations of bosonic Gaussian channels;
- $|00\rangle+\lambda|11\rangle$ tests of thermal attenuators/amplifiers;
- finite Schmidt-rank Gaussian EB witnesses;
- ancilla dimension required to witness non-EB bosonic channels;
- equality between EB and “rank-two-entanglement-breaking” for Gaussian channels.

If no equivalent result is found, this is currently the strongest standalone publication candidate in the repository.