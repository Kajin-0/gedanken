# Arbitrarily Weak Schmidt-Rank-Two Gaussian Probes

**Date:** 2026-08-07  
**Status:** Corollary of the complete one-mode Gaussian rank-two probe theorem. This does not claim that arbitrarily weak entanglement as such is new; finite-TMSV Gaussian EB tests already have that feature. The sharper point is that it remains true at Schmidt rank two.

## 1. Equal-covariance two-branch probe

For every non-entanglement-breaking one-mode Gaussian channel, the current theorem provides a finite probe of the form

$$
|\Psi_G\rangle
=\sqrt p|0\rangle|\psi_0\rangle
+e^{i\phi}\sqrt{1-p}|1\rangle|\psi_1\rangle,
$$

where $|\psi_0\rangle$ and $|\psi_1\rangle$ are two distinct displaced copies of one pure Gaussian state.

For the regular canonical construction,

$$
|\psi_j\rangle
=U_G|\alpha_j\rangle
$$

with the same Gaussian unitary $U_G$ on both branches.

Therefore branch overlap is invariant:

$$
\boxed{
\langle\psi_0|\psi_1\rangle
=\langle\alpha_0|\alpha_1\rangle.
}
$$

For coherent states,

$$
\boxed{
|\langle\alpha_0|\alpha_1\rangle|
=
\exp\left[-\frac12|\alpha_0-\alpha_1|^2\right].
}
$$

Define

$$
\delta=\alpha_0-\alpha_1.
$$

Then

$$
\boxed{
s\equiv|\langle\psi_0|\psi_1\rangle|
=e^{-|\delta|^2/2}.
}
$$

---

## 2. Balanced probe entanglement

For

$$
p=1/2,
$$

the pure input state is

$$
|\Psi_G\rangle
=\frac{|0\rangle|\psi_0\rangle
+|1\rangle|\psi_1\rangle}{\sqrt2}.
$$

The reduced qubit state is

$$
\rho_R
=\frac12
\begin{pmatrix}
1&\langle\psi_1|\psi_0\rangle\\
\langle\psi_0|\psi_1\rangle&1
\end{pmatrix}.
$$

Its eigenvalues are

$$
\boxed{
\lambda_\pm
=\frac{1\pm s}{2}.
}
$$

Therefore the input entanglement entropy is

$$
\boxed{
E_{\rm in}
=h_2\left(\frac{1+s}{2}\right),
}
$$

where $h_2$ is binary entropy.

As

$$
|\delta|\to0,
$$

$$
s\to1,
$$

and

$$
\boxed{E_{\rm in}\to0.}
$$

---

## 3. Small-separation asymptotic

For small

$$
d\equiv|\delta|,
$$

$$
s
=e^{-d^2/2}
=1-\frac{d^2}{2}+O(d^4).
$$

Thus the small Schmidt eigenvalue is

$$
\lambda_-
=\frac{1-s}{2}
=\frac{d^2}{4}+O(d^4).
$$

Hence

$$
\boxed{
E_{\rm in}
\sim
\frac{d^2}{4}
\log_2\frac{4e}{d^2}
}
$$

as

$$
d\to0.
$$

The input entanglement can therefore be made arbitrarily small continuously.

---

## 4. Output remains NPT for every finite nonzero separation

For the phase-insensitive canonical channel, the direct theorem states that **every** finite nontrivial coherent pair has NPT output whenever the channel is non-EB.

Therefore for every

$$
d>0,
$$

no matter how small,

$$
\boxed{
\Phi_{\tau,m}\text{ non-EB}
\Longrightarrow
(I\otimes\Phi_{\tau,m})(|\Psi_d\rangle\langle\Psi_d|)
\text{ NPT}.
}
$$

Pulling the branches back through the common input Gaussian unitary preserves both

1. input Schmidt coefficients;
2. output NPT after undoing the local output unitary.

Hence the same statement holds for every regular non-EB one-mode Gaussian channel.

---

## 5. Singular $B_1$ class

For $B_1$, choose one finite regularization parameter $y<1$ and the corresponding finite matched squeeze from `CONSTRUCTIVE_B1_FINITE_PROBE.md`.

The regularized non-EB channel admits every finite nonzero canonical coherent separation.

Choose

$$
d>0
$$

arbitrarily small.

The post-regularized output is NPT. Since the regularization is local post-processing, the pre-regularization $B_1$ output must already be NPT.

Thus the $B_1$ witness input can also have arbitrarily small branch entanglement.

---

## 6. Corollary

For every non-entanglement-breaking one-mode Gaussian channel $\mathcal N$ and every

$$
\epsilon>0,
$$
there exists a finite Schmidt-rank-two pure Gaussian-branch probe satisfying

$$
\boxed{
0<E_{\rm in}<\epsilon
}
$$

such that

$$
\boxed{
(I\otimes\mathcal N)(|\Psi_G\rangle\langle\Psi_G|)
\text{ is NPT}.
}
$$

Therefore

$$
\boxed{
\text{arbitrarily weak Schmidt-rank-two entanglement suffices to witness non-EB one-mode Gaussian channels.}
}
$$

---

## 7. Relation to finite-TMSV prior art

De Pasquale et al. already show that arbitrarily weak but finite two-mode squeezing can test Gaussian EB behavior.

For TMSV,

$$
E_{\rm in}\to0
$$

as

$$
r\to0^+,
$$

but every finite $r>0$ still gives infinite Schmidt rank.

Thus the new candidate reduction is not “arbitrarily weak entanglement suffices.”

It is

$$
\boxed{
\text{arbitrarily weak entanglement suffices even with Schmidt rank fixed to }2.
}
$$

This is the appropriate novelty wording if the rank-two theorem itself survives literature review.

---

## 8. Energy nuance

The entanglement can be arbitrarily weak, but the **bosonic branch energy** need not approach vacuum for a general channel.

For a regular anisotropic channel, the common matched Gaussian unitary may require a fixed amount of squeezing. The two branches can be brought arbitrarily close on top of that squeezed covariance baseline.

Thus distinguish:

- arbitrarily small bipartite entanglement: yes;
- arbitrarily small displacement energy above the matched Gaussian baseline: yes;
- arbitrarily small total bosonic energy relative to vacuum: not necessarily for a channel requiring strong covariance matching.

For the phase-insensitive family, no squeezing baseline is required and both branch displacement energy and entanglement can approach zero.

---

## 9. Why this matters for the gravity application

The gravitational receiver channel is expected to lie extremely close to a replacer/EB boundary in practical regimes.

The theorem says that mathematical non-EB capability does not require a large source cat. An arbitrarily weak rank-two branch encoding can reveal the sign of the channel resource in principle.

But the absolute output NPT weight simultaneously tends to zero.

This reinforces the distinction already made in Experiment 01 between

1. mathematical channel capability;
2. finite experimental certification strength.

The weak-link absolute witness law

$$
G_{\rm abs}^{\rm opt}
\simeq
\frac12W(e^{-1})(\tau-m)
$$

is the practical companion to the arbitrarily weak-input theorem.