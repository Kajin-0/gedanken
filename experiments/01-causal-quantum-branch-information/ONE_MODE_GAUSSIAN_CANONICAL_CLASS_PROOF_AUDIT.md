# Canonical-Class Audit for One-Mode Gaussian Channels

**Date:** 2026-08-07  
**Status:** **MATHEMATICS AUDIT — COVARIANCE CONVENTION CORRECTED; RANK-TWO NOVELTY RETIRED**

This file now has two purposes:

1. record a convention-consistent reduction of arbitrary one-mode Gaussian channels to the phase-insensitive canonical family where applicable;
2. record the singular $B_1$ closure argument.

The previously advertised Schmidt-rank-two novelty is no longer active because of the confirmed Mele–Lami–Giovannetti prior-art collision. See `NOVELTY_COLLISION_MELE_RANK_TWO.md`.

---

## 1. Fixed covariance convention

Use throughout

$$
\boxed{
V\mapsto K^T V K+\beta,
}
$$

with

$$
\Omega=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix}.
$$

In this convention a Gaussian unitary with symplectic matrix $S$ acts as

$$
\boxed{V\mapsto S^T V S.}
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

These are the standard Gaussian CP/EB matrix conditions written in the present transpose convention.

---

## 2. Composition rule in this convention

This was the main notation defect in the previous version of this file.

Let a Gaussian input unitary $S_{\rm in}$ act before the channel and an output unitary $S_{\rm out}$ act after it.

Starting from

$$
V
\xrightarrow{S_{\rm in}}
S_{\rm in}^T V S_{\rm in}
\xrightarrow{(K,\beta)}
K^T S_{\rm in}^T V S_{\rm in}K+\beta
\xrightarrow{S_{\rm out}}
S_{\rm out}^T
\left(K^T S_{\rm in}^T V S_{\rm in}K+\beta\right)
S_{\rm out},
$$

we obtain

$$
\boxed{
K' = S_{\rm in} K S_{\rm out},
}
$$

$$
\boxed{
\beta'=S_{\rm out}^T\beta S_{\rm out}.
}
$$

The previous audit incorrectly mixed this with the alternative convention $V\mapsto KVK^T+\beta$ and wrote the symplectic matrices in the opposite order.

The correction changes the bookkeeping, not the existence of the one-mode canonical reduction.

---

## 3. One-mode determinant identity

For every real $2\times2$ matrix $K$,

$$
\boxed{
K^T\Omega K=(\det K)\Omega.
}
$$

Define

$$
\boxed{\tau=\det K.}
$$

Then CP becomes

$$
\boxed{
\beta\ge
\pm\frac{i}{2}(1-\tau)\Omega.
}
$$

For a positive real symmetric $2\times2$ matrix $M$,

$$
M\ge\pm\frac{ic}{2}\Omega
$$

is equivalent to

$$
\boxed{
\sqrt{\det M}\ge\frac{|c|}{2}.
}
$$

Thus the one-mode class audit can be reduced to scalar determinant inequalities.

---

## 4. Case $\tau=0$: every physical channel is EB

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

Choose

$$
\alpha=\beta,
\qquad
\nu=0.
$$

Then the EB decomposition conditions are satisfied directly. Therefore

$$
\boxed{
\tau=0\Longrightarrow\text{EB}.
}
$$

This covers the one-mode $A_1/A_2$ canonical classes.

---

## 5. Case $\tau<0$: every physical channel is EB

Write

$$
\tau=-s,
\qquad
s>0.
$$

CP requires

$$
\sqrt{\det\beta}\ge\frac{1+s}{2}.
$$

Define

$$
\alpha=\frac{1}{1+s}\beta,
$$

$$
\nu=\frac{s}{1+s}\beta.
$$

Then

$$
\beta=\alpha+\nu,
$$

and

$$
\sqrt{\det\alpha}
=\frac{\sqrt{\det\beta}}{1+s}
\ge\frac12,
$$

while

$$
\sqrt{\det\nu}
=\frac{s\sqrt{\det\beta}}{1+s}
\ge\frac{s}{2}.
$$

Since

$$
K^T\Omega K=-s\Omega,
$$

the EB decomposition exists. Hence

$$
\boxed{
\tau<0\Longrightarrow\text{EB}.
}
$$

This covers the orientation-reversing / phase-conjugating class $D$.

---

## 6. Regular orientation-preserving case: corrected canonicalization

Assume

$$
\tau>0,
\qquad
\det\beta>0.
$$

Let

$$
y=\sqrt{\det\beta}.
$$

By one-mode Williamson reduction, choose a symplectic $S_{\rm out}$ satisfying

$$
\boxed{
S_{\rm out}^T\beta S_{\rm out}=yI.
}
$$

Now choose

$$
\boxed{
S_{\rm in}
=\sqrt\tau\,S_{\rm out}^{-1}K^{-1}.
}
$$

Then

$$
S_{\rm in}KS_{\rm out}
=\sqrt\tau I.
$$

Moreover,

$$
\det S_{\rm in}
=\frac{\tau}{\det K}
=1.
$$

For one mode,

$$
Sp(2,\mathbb R)=SL(2,\mathbb R),
$$

so $S_{\rm in}$ is symplectic.

Therefore, using the composition rule from Section 2,

$$
(K,\beta)
\longrightarrow
(\sqrt\tau I,yI).
$$

Thus every regular orientation-preserving one-mode Gaussian channel is Gaussian-unitarily equivalent to a gauge-covariant phase-insensitive channel.

### Probe transformation

If

$$
\Phi_{\rm PI}
=\mathcal U_{\rm out}
\circ\mathcal N
\circ\mathcal U_{\rm in},
$$

then a canonical probe state $\rho_{RA}^{\rm can}$ for $\Phi_{\rm PI}$ corresponds to the original-channel input

$$
\boxed{
\rho_{RA}^{\mathcal N}
=(I_R\otimes U_{\rm in})
\rho_{RA}^{\rm can}
(I_R\otimes U_{\rm in}^\dagger).
}
$$

The original-channel output is related to the canonical output by the local output unitary $U_{\rm out}$, so PPT/NPT is unchanged.

This removes the former ambiguity over whether the input unitary or its inverse should appear in the channel-matched probe.

---

## 7. Rank-deficient noise can occur only at $\tau=1$ for nonzero orientation-preserving $K$

If

$$
\tau\ne1,
$$

CP requires

$$
\sqrt{\det\beta}
\ge\frac{|1-\tau|}{2}>0.
$$

Therefore

$$
\det\beta>0.
$$

Hence the only orientation-preserving nonzero-$K$ singular-noise case requiring separate treatment is

$$
\boxed{
\tau=1,
\qquad
\operatorname{rank}\beta=1,
}
$$

the $B_1$ class.

The subcase

$$
\tau=1,
\qquad
\beta=0
$$

is a Gaussian unitary.

---

## 8. Gaussian-unitary subcase

For

$$
\tau=1,
\qquad
\beta=0,
$$

the channel is a local Gaussian unitary.

Any entangled finite Schmidt-rank-two input remains entangled and NPT if it was initially a pure rank-two state.

No special channel analysis is needed.

---

## 9. Singular $B_1$: finite regularization proof

Put the rank-one noise into canonical form

$$
\boxed{
\beta_{B_1}
=\begin{pmatrix}
b&0\\0&0\end{pmatrix},
\qquad b>0,
}
$$

with

$$
K=I.
$$

Apply local post-processing that adds finite noise $\epsilon>0$ to the clean quadrature:

$$
\boxed{
\beta_\epsilon
=\begin{pmatrix}
b&0\\0&\epsilon\end{pmatrix}.
}
$$

A finite one-mode squeeze isotropizes this to

$$
\boxed{
y_\epsilon I,
\qquad
y_\epsilon=\sqrt{b\epsilon}.
}
$$

For a unit-gain isotropic additive-noise channel in the present convention, EB occurs at

$$
y_\epsilon\ge1.
$$

Choose

$$
\boxed{0<\epsilon<1/b.}
$$

Then

$$
y_\epsilon<1,
$$

so the regularized full-rank channel is non-EB.

Use any finite rank-two input known to produce NPT for that regularized channel. Suppose the same input immediately after $B_1$ were PPT. Since the added noise is a local CP map,

$$
[(I\otimes\mathcal A_\epsilon)(\rho)]^{T_R}
=(I\otimes\mathcal A_\epsilon)(\rho^{T_R})
\ge0
$$

would follow, contradicting the NPT regularized output.

Therefore the original $B_1$ output is already NPT.

The construction is finite for every finite $b>0$ and every finite allowed $\epsilon$.

---

## 10. Class exhaustion

The one-mode canonical classes are therefore exhausted as follows:

- $\tau=0$: EB;
- $\tau<0$: EB;
- $\tau>0$, full-rank noise: Gaussian-unitarily phase-insensitive;
- $\tau=1$, zero noise: Gaussian unitary;
- $\tau=1$, rank-one noise: $B_1$ finite-regularization closure.

No physical one-mode Gaussian canonical class is omitted.

---

## 11. What this audit does and does not establish after the Mele collision

### Mathematical statement

Combining existing phase-insensitive finite-rank prior art with the corrected canonical reduction and the $B_1$ closure supports the mathematical statement

$$
\boxed{
\text{every non-EB one-mode Gaussian channel admits a finite Schmidt-rank-two NPT probe.}
}
$$

### Novelty statement

Do **not** present that broad result as the repository's principal discovery.

Mele–Lami–Giovannetti already establish the substantive phase-insensitive rank-two phenomenon for a larger Fock-pair family. For regular one-mode channels the extension is essentially standard canonicalization. The main additional ingredient here is the singular $B_1$ closure.

See:

- `NOVELTY_COLLISION_MELE_RANK_TWO.md`
- `NOVELTY_AUDIT_SCHMIDT_RANK_TWO_GAUSSIAN_PROBE.md`

---

## 12. Active use of this file

This canonical audit remains useful if the **binary coherent theorem** is later extended from phase-insensitive channels to arbitrary one-mode Gaussian channels.

For a regular original channel, the canonical coherent pair pulls through $U_{\rm in}$ to two displaced copies of one finite-covariance pure Gaussian state. The $B_1$ case remains separately handled by the finite-regularization/PPT-monotonicity argument.

Any future manuscript must preserve the covariance convention in Sections 1–2 exactly or explicitly redefine all channel matrices before changing transpose order.
