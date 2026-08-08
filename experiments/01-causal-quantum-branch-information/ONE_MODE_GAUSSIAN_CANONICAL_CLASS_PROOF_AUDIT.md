# Canonical-Class Proof Audit for the One-Mode Rank-Two Probe Theorem

**Date:** 2026-08-07  
**Status:** Rigorous class-by-class audit of `COMPLETE_ONE_MODE_GAUSSIAN_TWO_BRANCH_PROBE_THEOREM.md` using the standard Gaussian CP and EB matrix inequalities.

## 1. Gaussian conventions

Use the one-mode Gaussian-channel convention

$$
V\mapsto K^TVK+\beta,
$$

with symplectic form

$$
\Omega=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix}.
$$

Complete positivity is equivalent to

$$
\boxed{
\beta\ge
\pm\frac{i}{2}
(\Omega-K^T\Omega K).
}
$$

The channel is entanglement breaking iff

$$
\boxed{
\beta=\alpha+\nu
}
$$

for real symmetric matrices satisfying

$$
\boxed{
\alpha\ge\frac{i}{2}\Omega,
\qquad
\nu\ge\frac{i}{2}K^T\Omega K.
}
$$

These are standard Gaussian-channel results due to Holevo and are summarized explicitly in De Pasquale–Mari–Porzio–Giovannetti.

---

## 2. One-mode determinant identity

For every real $2\times2$ matrix $K$,

$$
\boxed{
K^T\Omega K
=(\det K)\Omega.
}
$$

Define

$$
\boxed{
\tau=\det K.
}
$$

Then the CP condition becomes

$$
\boxed{
\beta\ge
\pm\frac{i}{2}(1-\tau)\Omega.
}
$$

For a positive real symmetric $2\times2$ matrix $M$, the inequality

$$
M\ge\pm\frac{ic}{2}\Omega
$$

is equivalent to

$$
\boxed{
\sqrt{\det M}\ge\frac{|c|}{2}.
}
$$

This reduces the one-mode class audit to scalar symplectic-eigenvalue inequalities.

---

## 3. Case $\tau=0$: all physical channels are EB

If

$$
\tau=0,
$$

then

$$
K^T\Omega K=0.
$$

CP requires

$$
\beta\ge\pm\frac{i}{2}\Omega.
$$

Choose the EB decomposition

$$
\boxed{
\alpha=\beta,
\qquad
\nu=0.
}
$$

Then

$$
\alpha\ge\frac{i}{2}\Omega
$$

by CP, while

$$
\nu=0
\ge
\frac{i}{2}K^T\Omega K=0.
$$

Therefore

$$
\boxed{
\tau=0
\Longrightarrow
\text{every physical one-mode Gaussian channel is EB}.
}
$$

This covers the canonical $A_1/A_2$ classes.

---

## 4. Case $\tau<0$: all physical channels are EB

Write

$$
\tau=-s,
\qquad
s>0.
$$

Then CP requires

$$
\sqrt{\det\beta}
\ge
\frac{1+s}{2}.
$$

Define

$$
\boxed{
\alpha
=\frac{1}{1+s}\beta,
}
$$

$$
\boxed{
\nu
=\frac{s}{1+s}\beta.
}
$$

Clearly

$$
\beta=\alpha+\nu.
$$

The symplectic eigenvalue of $\alpha$ is

$$
\sqrt{\det\alpha}
=
\frac{\sqrt{\det\beta}}{1+s}
\ge
\frac12,
$$

so

$$
\alpha\ge\frac{i}{2}\Omega.
$$

The symplectic eigenvalue of $\nu$ is

$$
\sqrt{\det\nu}
=
\frac{s\sqrt{\det\beta}}{1+s}
\ge
\frac{s}{2}.
$$

But

$$
K^T\Omega K
=-s\Omega,
$$

so this is exactly sufficient for

$$
\nu\ge
-\frac{is}{2}\Omega
=
\frac{i}{2}K^T\Omega K.
$$

Hence the EB decomposition always exists:

$$
\boxed{
\tau<0
\Longrightarrow
\text{every physical one-mode Gaussian channel is EB}.
}
$$

This covers the orientation-reversing / phase-conjugating canonical class $D$ directly, without appealing only to a classification table.

---

## 5. Case $\tau>0$, $\beta>0$: regular orientation-preserving channels

If

$$
\tau>0
$$

and

$$
\det\beta>0,
$$

the noise is full rank.

Williamson's theorem gives a symplectic output matrix $S_{\rm out}$ such that

$$
S_{\rm out}\beta S_{\rm out}^T
=yI,
$$

where

$$
y=\sqrt{\det\beta}.
$$

Choose

$$
S_{\rm in}
=\sqrt\tau K^{-1}S_{\rm out}^{-1}.
$$

Its determinant is one, so in one mode it is symplectic.

Then

$$
S_{\rm out}KS_{\rm in}
=\sqrt\tau I.
$$

Thus the channel is Gaussian-unitarily equivalent to a gauge-covariant phase-insensitive canonical channel.

The direct binary-coherent theorem therefore supplies a finite two-branch equal-covariance pure-Gaussian NPT probe whenever this channel is non-EB.

This covers the regular $B_2/C$ family and anisotropic full-rank versions thereof.

---

## 6. Why rank-deficient noise can occur only at $\tau=1$ among nonzero-$K$ channels

If

$$
\tau\neq1,
$$

CP requires

$$
\sqrt{\det\beta}
\ge
\frac{|1-\tau|}{2}>0.
$$

Therefore

$$
\boxed{
\det\beta>0
}
$$

and the channel belongs to the regular case above.

Hence the only orientation-preserving nonzero-$K$ singular-noise case that needs separate treatment is

$$
\boxed{
\tau=1,
\qquad
\operatorname{rank}\beta=1,
}
$$

the canonical $B_1$ class.

The zero-noise subcase

$$
\tau=1,
\quad
\beta=0
$$

is simply a Gaussian unitary.

---

## 7. Gaussian-unitary subcase

For

$$
\tau=1,
\qquad
\beta=0,
$$

the channel is a local Gaussian unitary.

Any entangled finite binary coherent hybrid state remains pure entangled after the channel and is therefore NPT.

Thus this boundary case is trivial.

---

## 8. Singular $B_1$: finite regularization proof

Put the rank-one noise into diagonal canonical form,

$$
\boxed{
\beta_{B_1}
=
\begin{pmatrix}
b&0\\
0&0
\end{pmatrix},
\qquad
b>0,
}
$$

with

$$
K=I.
$$

Now apply an additional local additive-noise channel after $B_1$ which adds finite noise

$$
\epsilon>0
$$

in the previously noiseless quadrature:

$$
\boxed{
\beta_\epsilon
=
\begin{pmatrix}
b&0\\
0&\epsilon
\end{pmatrix}.
}
$$

The regularized channel still has

$$
K=I.
$$

A symplectic squeeze turns $\beta_\epsilon$ into isotropic additive noise

$$
\boxed{
y_\epsilon I,
\qquad
y_\epsilon=\sqrt{b\epsilon}.
}
$$

For a unit-gain isotropic additive-noise channel, the Gaussian EB criterion is

$$
\boxed{
y_\epsilon\ge1}
$$

in the present covariance convention where vacuum has covariance $I/2$.

Choose any finite

$$
\boxed{
0<\epsilon<1/b.
}
$$

Then

$$
y_\epsilon<1,
$$

so the regularized channel

$$
\mathcal N_\epsilon
=\mathcal A_\epsilon\circ\mathcal B_1
$$

is non-EB and full rank.

By the regular theorem there exists a **finite** matched two-branch pure-Gaussian input $|\Psi_{G,\epsilon}\rangle$ such that

$$
(I\otimes\mathcal N_\epsilon)
(|\Psi_{G,\epsilon}\rangle\langle\Psi_{G,\epsilon}|)
$$

is NPT.

Suppose, for contradiction, that the state immediately after $\mathcal B_1$ were PPT.

Applying the local CP map $\mathcal A_\epsilon$ to the bosonic subsystem preserves PPT, because

$$
[(I\otimes\mathcal A_\epsilon)(\rho)]^{T_A}
=(I\otimes\mathcal A_\epsilon)(\rho^{T_A})
\ge0
$$

whenever

$$
\rho^{T_A}\ge0.
$$

But the post-processed state is NPT.

Contradiction.

Therefore

$$
\boxed{
(I\otimes\mathcal B_1)
(|\Psi_{G,\epsilon}\rangle\langle\Psi_{G,\epsilon}|)
\text{ is already NPT}.
}
$$

Because $\epsilon$ was chosen finite, the matched probe has finite squeezing and finite energy.

Thus the singular $B_1$ channel is covered without an infinite-squeezing limit.

---

## 9. Class exhaustion

We have now treated every one-mode canonical possibility.

### $\tau=0$

EB.

### $\tau<0$

EB.

### $\tau>0$, full-rank noise

Regular theorem supplies finite rank-two pure-Gaussian probe whenever non-EB.

### $\tau=1$, zero noise

Gaussian unitary; trivial finite probe.

### $\tau=1$, rank-one noise

$B_1$ regularization proof supplies finite probe.

Hence there is no unhandled physical one-mode Gaussian canonical class.

---

## 10. Audited theorem

The class-by-class argument establishes:

$$
\boxed{
\mathcal N\text{ is a non-EB one-mode Gaussian channel}
}
$$

iff there exists a finite Schmidt-rank-two hybrid input

$$
\sqrt p|0\rangle|\psi_0\rangle
+e^{i\phi}\sqrt{1-p}|1\rangle|\psi_1\rangle,
$$

where $|\psi_0\rangle,|\psi_1\rangle$ are distinct displaced copies of the same finite-covariance pure Gaussian state, whose output under $I\otimes\mathcal N$ is NPT.

The converse follows from the definition of an EB channel.

---

## 11. Relation to finite-TMSV prior art

De Pasquale et al. show that any finite nonzero two-mode squeezing can replace the formal infinite-energy Choi state when testing a Gaussian channel for EB.

That resource is finite energy but has infinite Schmidt rank.

The present theorem reduces the reference requirement further:

$$
\boxed{
\text{Schmidt rank }2\text{ is sufficient for every one-mode Gaussian channel.}
}
$$

This is the specific statement whose novelty remains to be established.

---

## 12. Remaining mathematical checks

The proof is now internally complete at the canonical-class level.

The remaining issues are external rather than algebraic:

1. literature search for an equivalent Schmidt-rank-two sufficiency theorem;
2. independent review of the direct phase-insensitive binary-coherent principal-minor proof on which the regular case rests;
3. precise alignment of notation with the most standard Gaussian-channel covariance convention in any manuscript version.