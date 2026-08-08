# Constructive Finite Probe for the Singular $B_1$ Gaussian Channel

**Date:** 2026-08-07  
**Status:** Explicit finite-squeezing version of the $B_1$ regularization argument used in the complete one-mode Gaussian rank-two probe theorem.

## 1. Canonical $B_1$ channel

Use quadratures in which

$$
K=I,
$$

and the rank-one additive-noise matrix is

$$
\boxed{
Y_{B_1}
=
\begin{pmatrix}
b&0\\0&0\end{pmatrix},
\qquad b>0.
}
$$

The channel is singular because one quadrature receives finite Gaussian noise while the conjugate quadrature receives none.

---

## 2. Add a deliberately weak local post-processing noise

Choose a target isotropic canonical additive-noise level

$$
\boxed{0<y<1.}
$$

The unit-gain isotropic additive channel at noise $y$ is non-entanglement-breaking in the convention where the EB threshold is

$$
y=1.
$$

Now add finite noise

$$
\boxed{
\epsilon=rac{y^2}{b}
}
$$

in the previously clean quadrature.

The post-processed noise matrix is

$$
\boxed{
Y_\epsilon
=
\begin{pmatrix}
b&0\\0&y^2/b\end{pmatrix}.
}
$$

Its determinant is

$$
\det Y_\epsilon=y^2.
$$

Thus its one-mode symplectic noise eigenvalue is exactly

$$
\boxed{y.}
$$

---

## 3. Explicit canonicalizing squeeze

Let

$$
S_{\rm out}
=
\begin{pmatrix}
s&0\\0&s^{-1}\end{pmatrix}.
$$

Choose

$$
\boxed{
s^2=\frac{y}{b}.}
$$

Then

$$
S_{\rm out}
Y_\epsilon
S_{\rm out}^T
=
\begin{pmatrix}
y&0\\0&y\end{pmatrix}
=yI.
$$

Because

$$
K=I,
$$

choose

$$
S_{\rm in}=S_{\rm out}^{-1}.
$$

Then

$$
S_{\rm out}KS_{\rm in}=I.
$$

Hence the regularized $B_1$ channel is Gaussian-unitarily equivalent to the unit-gain isotropic additive-noise channel

$$
\boxed{
\Phi_{1,y}.
}
$$

---

## 4. Finite squeezing parameter

Write the input squeeze as

$$
S_{\rm in}
=
\begin{pmatrix}
e^r&0\\0&e^{-r}\end{pmatrix}.
$$

Since

$$
e^{2r}=b/y,
$$

$$
\boxed{
r=\frac12\ln\frac{b}{y}.}
$$

For every finite

$$
b>0
$$

and every finite

$$
0<y<1,
$$

the required squeezing is finite.

Thus the $B_1$ proof does not hide an infinite-energy limit.

---

## 5. Explicit rank-two probe

Take any nontrivial coherent pair in canonical coordinates,

$$
|+a\rangle,
\qquad
|-a\rangle,
\qquad a>0.
$$

The binary coherent theorem guarantees

$$
(I\otimes\Phi_{1,y})
\left[
\frac{(|0\rangle|a\rangle+|1\rangle|-a\rangle)
(\langle0|\langle a|+\langle1|\langle-a|)}{2}
\right]
$$

is NPT because

$$
y<1.
$$

Pull the coherent branches back through the finite common input squeeze:

$$
\boxed{
|\psi_\pm\rangle
=U(S_{\rm in})|\pm a\rangle.
}
$$

These are two displaced copies of one finite squeezed-vacuum covariance state.

The original rank-two input is

$$
\boxed{
|\Psi_{B_1}\rangle
=
\frac{
|0\rangle|\psi_+\rangle
+|1\rangle|\psi_-\rangle
}{\sqrt2}.
}
$$

---

## 6. Why this proves NPT before the added noise

Let

$$
\mathcal B_1
$$

be the original singular channel and

$$
\mathcal A_\epsilon
$$

the deliberately added local Gaussian noise.

Then

$$
\mathcal N_\epsilon
=
\mathcal A_\epsilon\circ\mathcal B_1.
$$

The chosen input gives an NPT state after $\mathcal N_\epsilon$.

If the state after $\mathcal B_1$ were PPT, then applying the local CP map $\mathcal A_\epsilon$ would preserve positivity of the partial transpose.

Therefore the state after $\mathcal B_1$ must already have been NPT:

$$
\boxed{
(I\otimes\mathcal B_1)
(|\Psi_{B_1}\rangle\langle\Psi_{B_1}|)
\text{ is NPT}.
}
$$

This is a constructive finite-energy proof.

---

## 7. Simple choices

### If $0<b<1$

Choose

$$
y=b.
$$

Then

$$
epsilon=b,
$$

and

$$
\boxed{r=0.}
$$

So ordinary coherent branches already suffice through this argument.

### If $b\ge1$

Choose, for example,

$$
y=\frac12.
$$

Then

$$
\epsilon=rac{1}{4b},
$$

and

$$
\boxed{
r=\frac12\ln(2b).}
$$

This is finite for every finite $b$.

One can reduce the squeezing by choosing $y$ closer to $1$ while remaining strictly below the EB threshold.

---

## 8. Probe energy

For a squeezed coherent branch, the mean bosonic excitation is finite:

$$
\bar n
=\sinh^2r
+|\alpha_{\rm phys}|^2
$$

with the displacement term determined by the squeezed quadrature orientation.

For fixed finite $b$, $y$, and $a$, all terms are finite.

The required energy may become large in extreme singular-noise limits, but the theorem claims **finite sufficiency**, not a uniform channel-independent energy bound.

---

## 9. Importance

The singular class was the only place where the complete one-mode Gaussian theorem might have required an infinite-squeezing limiting state.

It does not.

The probe can be made explicit, finite, and Schmidt rank two for every finite $B_1$ noise strength.

This substantially strengthens the standalone theorem candidate.