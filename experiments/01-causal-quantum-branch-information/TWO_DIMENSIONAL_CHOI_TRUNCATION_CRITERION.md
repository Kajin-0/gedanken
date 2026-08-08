# Two-Dimensional Choi-Truncation Criterion for Phase-Insensitive Gaussian Channels

**Date:** 2026-08-07  
**Status:** Exact corollary of `TRUNCATED_TMSV_RANK_TWO_THEOREM.md`. This may be the cleanest operational/mathematical form of the phase-insensitive result.

## 1. Vacuum–one-photon Bell probe

Take the fixed rank-two maximally entangled state

$$
\boxed{
|\Phi_2\rangle
=
\frac{|0\rangle_R|0\rangle_A
+|1\rangle_R|1\rangle_A}{\sqrt2}.
}
$$

This is the maximally entangled state of the two-dimensional bosonic input subspace

$$
\boxed{
\mathcal H_{01}
=\operatorname{span}\{|0\rangle,|1\rangle\}.
}
$$

Thus it is the ordinary finite-dimensional Choi probe of the channel restriction to $\mathcal H_{01}$.

---

## 2. Phase-insensitive Gaussian channel

For

$$
\Phi_{\tau,m},
$$

the full infinite-dimensional channel is entanglement breaking iff

$$
\boxed{m\ge\tau.}
$$

The question is whether this full EB boundary is already visible in the $0$–$1$ Choi truncation.

It is.

---

## 3. Three process matrix elements

Define

$$
A_{11}
=\langle1|
\Phi(|0\rangle\langle0|)
|1\rangle,
$$

$$
B_{00}
=\langle0|
\Phi(|1\rangle\langle1|)
|0\rangle,
$$

and

$$
X_{01}
=\langle0|
\Phi(|0\rangle\langle1|)
|1\rangle.
$$

The exact values are

$$
\boxed{
A_{11}
=\frac{m}{(m+1)^2},
}
$$

$$
\boxed{
B_{00}
=\frac{m+1-\tau}{(m+1)^2},
}
$$

$$
\boxed{
X_{01}
=\frac{\sqrt\tau}{(m+1)^2}.
}
$$

---

## 4. Partial-transpose Choi block

Send half of $|\Phi_2\rangle$ through the channel.

After partial transpose on the reference, restrict to

$$
\{|0\rangle_R|1\rangle_B,
|1\rangle_R|0\rangle_B\}.
$$

The block is

$$
\boxed{
M_{01}
=
\frac12
\begin{pmatrix}
A_{11}&X_{01}^*\\
X_{01}&B_{00}
\end{pmatrix}.
}
$$

Its determinant is

$$
\det M_{01}
=
\frac14
(A_{11}B_{00}-|X_{01}|^2).
$$

Substituting the exact channel elements gives

$$
\boxed{
\det M_{01}
=\frac{m-\tau}{4(m+1)^3}.
}
$$

---

## 5. Exact channel criterion

Therefore

$$
\boxed{
|X_{01}|^2>A_{11}B_{00}
\iff
\tau>m.
}
$$

But

$$
\tau>m
$$

is exactly the full infinite-dimensional channel's non-entanglement-breaking region.

Hence

$$
\boxed{
\Phi_{\tau,m}\text{ is non-EB}
\iff
(I\otimes\Phi_{\tau,m})(|\Phi_2\rangle\langle\Phi_2|)
\text{ is NPT}.
}
$$

Equivalently:

$$
\boxed{
\text{the vacuum–one-photon two-dimensional Choi truncation detects the exact EB boundary.}
}
$$

---

## 6. Higher Fock sectors are unnecessary for the sign decision

A finite-squeezing TMSV test uses

$$
\sum_{n=0}^\infty\lambda^n|n,n\rangle.
$$

The present result shows that, for the phase-insensitive Gaussian family, all terms with

$$
n\ge2
$$

can be discarded without losing the ability to decide whether the full channel is EB.

The sign of the EB resource is already visible in the $n=0,1$ sector.

This is stronger than merely saying that a finite-dimensional approximation converges to the correct answer.

It is an **exact finite truncation**.

---

## 7. Process-level interpretation

The full Gaussian EB transition can be reconstructed from only

1. vacuum $\to$ one-photon leakage probability $A_{11}$;
2. one-photon $\to$ vacuum probability $B_{00}$;
3. vacuum–one-photon coherence transfer $X_{01}$.

The criterion is the Cauchy-Schwarz-like inequality

$$
\boxed{
|X_{01}|^2
\le
A_{11}B_{00}
}
$$

for the EB side.

Violation certifies a non-EB channel.

Thus the infinite-dimensional Gaussian channel's EB property is encoded in one $2\times2$ process minor.

---

## 8. Exact absolute NPT weight

The smaller eigenvalue of $M_{01}$ is

$$
\boxed{
\mu_-^{(01)}
=
\frac{
2m+1-\tau
-
\sqrt{(\tau-1)^2+4\tau}
}{4(m+1)^2}
}
$$

when $\lambda=1$.

Since

$$
\sqrt{(\tau-1)^2+4\tau}
=\tau+1,
$$

this simplifies dramatically:

$$
\boxed{
\mu_-^{(01)}
=
\frac{m-\tau}{2(m+1)^2}.
}
$$

Therefore the vacuum–one-photon Choi block gives the explicit negativity lower bound

$$
\boxed{
\mathcal N
\ge
\frac{[\tau-m]_+}{2(m+1)^2}.
}
$$

For the fixed Bell probe, the selected $2\times2$ block's negative weight is therefore directly proportional to the channel quantum excess.

**Audit note:** this simplification should be checked carefully against the exact $M_{01}$ trace/eigenvalue algebra before manuscript use; the determinant criterion itself is already exact.

---

## 9. General Schmidt weight

For

$$
|\psi_\lambda\rangle
\propto
|00\rangle+\lambda|11\rangle,
$$

the exact PT determinant is

$$
\boxed{
\det M_\lambda
=
\frac{\lambda^2}{(1+\lambda^2)^2}
\frac{m-\tau}{(m+1)^3}.
}
$$

Thus every

$$
\lambda>0
$$

has the same EB sign boundary.

The maximally entangled choice

$$
\lambda=1
$$

is simply the channel-independent fixed representative.

---

## 10. Extension to arbitrary regular one-mode Gaussian channels

For a regular orientation-preserving channel $\mathcal N$, choose Gaussian input/output unitaries such that

$$
\Phi
=U_{\rm out}\circ\mathcal N\circ U_{\rm in}
$$

is phase insensitive.

Then the matched two-dimensional bosonic input subspace is

$$
\boxed{
\mathcal H_{\mathcal N}^{(2)}
=
\operatorname{span}
\{U_{\rm in}|0\rangle,
U_{\rm in}|1\rangle\}.
}
$$

The maximally entangled qubit–subspace state

$$
\boxed{
|\Phi_{2,\mathcal N}\rangle
=
\frac{
|0\rangle_RU_{\rm in}|0\rangle
+|1\rangle_RU_{\rm in}|1\rangle
}{\sqrt2}
}
$$

has NPT output iff the regular channel is non-EB.

Thus the two-dimensional Choi-truncation idea survives canonicalization, although the physical bosonic two-dimensional subspace becomes channel matched.

---

## 11. Novelty language

If literature review finds no equivalent result, the strongest concise statement is:

> **For phase-insensitive one-mode Gaussian channels, the full entanglement-breaking boundary is exactly visible in the vacuum–one-photon Choi truncation.**

The general one-mode corollary is:

> **Every non-EB one-mode Gaussian channel has a channel-matched two-dimensional bosonic input subspace whose qubit Choi state is NPT.**

These formulations may be more recognizable and searchable than “Schmidt-rank-two probe sufficiency.”