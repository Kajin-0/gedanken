# Gaussian-Unitary Extension of the Binary Probe Theorem

**Date:** 2026-08-07  
**Status:** Corollary of the binary coherent phase-insensitive theorem plus established one-mode Gaussian canonical-unitary equivalence. This broadens the theorem without changing its core proof.

## 1. General one-mode Gaussian channel

Write a one-mode Gaussian channel in quadrature form as

$$
\boxed{
d\mapsto Xd,
}
$$

$$
\boxed{
V\mapsto XVX^T+Y,
}
$$

where

- $X$ is a real $2\times2$ matrix;
- $Y=Y^T\ge0$ is the noise matrix;
- complete positivity imposes the usual uncertainty constraint.

Consider the **regular orientation-preserving** class

$$
\boxed{
\det X>0,
\qquad
Y>0.
}
$$

This excludes singular rank-deficient canonical classes from the present corollary.

---

## 2. Gaussian-unitary canonicalization

A one-mode Gaussian unitary acts by a real symplectic matrix $S$.

In two dimensions,

$$
\boxed{
S\in Sp(2,\mathbb R)
\iff
\det S=1.
}
$$

Since $Y>0$, Williamson's theorem gives a symplectic output transformation $S_{\rm out}$ such that

$$
\boxed{
S_{\rm out}YS_{\rm out}^T
=yI,
}
$$

with

$$
\boxed{
y=\sqrt{\det Y}.}
$$

Now define

$$
\tau=\det X>0.
$$

Choose

$$
\boxed{
S_{\rm in}
=\sqrt\tau\,X^{-1}S_{\rm out}^{-1}.
}
$$

Its determinant is

$$
\det S_{\rm in}
=
\frac{\tau}{\det X}=1,
$$

so $S_{\rm in}$ is symplectic.

Then

$$
\boxed{
S_{\rm out}XS_{\rm in}
=\sqrt\tau\,I.
}
$$

Thus, up to Gaussian input/output unitaries, every regular orientation-preserving one-mode Gaussian channel is equivalent to a phase-insensitive canonical channel with

$$
X_c=\sqrt\tau I,
$$

$$
Y_c=yI.
$$

In the channel convention used elsewhere in Experiment 01 this canonical channel can be written as

$$
\Phi_{\tau,m}
$$

for the corresponding vacuum-output occupation $m$.

This unitary-equivalence structure is established one-mode Gaussian-channel theory; it is not a new result of this project.

---

## 3. Entanglement-breaking status is invariant under Gaussian unitaries

Let the original channel be $\mathcal N$ and its canonicalized version be

$$
\Phi
=\mathcal U_{\rm out}
\circ\mathcal N
\circ\mathcal U_{\rm in}.
$$

Because $\mathcal U_{\rm in}$ and $\mathcal U_{\rm out}$ are reversible local unitaries,

$$
\boxed{
\mathcal N\text{ is EB}
\iff
\Phi\text{ is EB}.
}
$$

The canonical channel is non-EB exactly when

$$
\tau>m.
$$

---

## 4. Pull back the binary coherent probe

For the canonical channel, take any finite nontrivial binary coherent hybrid state

$$
|\Psi\rangle
=
\sqrt p|0\rangle|\alpha\rangle
+e^{i\phi}\sqrt{1-p}|1\rangle|\beta\rangle,
$$

with

$$
0<p<1,
\qquad
\alpha\neq\beta.
$$

The direct theorem gives

$$
\boxed{
(I\otimes\Phi)(|\Psi\rangle\langle\Psi|)
\text{ NPT}
\iff
\Phi\text{ non-EB}.
}
$$

Now define the corresponding input states for the original channel by applying the inverse canonicalizing input transformation:

$$
\boxed{
|\psi_\alpha\rangle
=\mathcal U_{\rm in}|\alpha\rangle,
}
$$

$$
\boxed{
|\psi_\beta\rangle
=\mathcal U_{\rm in}|\beta\rangle,
}
$$

with the exact placement of $\mathcal U_{\rm in}$ versus $\mathcal U_{\rm in}^{-1}$ fixed by the chosen composition convention above.

The key invariant statement is independent of that bookkeeping:

> the two original-basis probe states are obtained by applying the **same Gaussian unitary** to two distinct coherent states.

Therefore they are two distinct displaced copies of one pure Gaussian covariance state.

---

## 5. Extended probe theorem

For every regular orientation-preserving one-mode Gaussian channel

$$
\det X>0,
\qquad
Y>0,
$$

there exists a finite two-branch pure-Gaussian probe family

$$
\boxed{
\sqrt p|0\rangle|\psi_\alpha\rangle
+e^{i\phi}\sqrt{1-p}|1\rangle|\psi_\beta\rangle
}
$$

where $|\psi_\alpha\rangle$ and $|\psi_\beta\rangle$ have the **same covariance matrix** and different phase-space displacements, such that

$$
\boxed{
(I\otimes\mathcal N)(|\Psi_G\rangle\langle\Psi_G|)
\text{ is NPT}
\iff
\mathcal N\text{ is non-EB}.
}
$$

This follows because

1. the Gaussian-unitary canonicalization maps $\mathcal N$ to $\Phi_{\tau,m}$;
2. the binary coherent theorem detects the canonical EB boundary exactly;
3. local Gaussian unitaries preserve NPT/separability.

---

## 6. Interpretation

The coherent-state theorem is not tied to circular phase-space noise.

For a receiver with deterministic squeezing or anisotropic but full-rank Gaussian noise, the correct minimal probe is obtained by **pre-distorting the two branches with the same inverse Gaussian unitary**.

In ordinary language:

> **Match the covariance ellipse of the two branch states to the receiver's canonical squeezing. Then the only difference between the branches is displacement, and the same two-branch theorem detects the exact EB transition.**

This makes the theorem substantially more useful for realistic Gaussian receivers.

---

## 7. Relation to the earlier phase-sensitive discussion

The project previously noted that deterministic Gaussian pre/post unitaries cannot rescue an EB channel.

The present corollary strengthens that statement operationally:

- deterministic squeezing does not change EB status;
- but it does change the **shape of the front-faithful two-branch probe**;
- coherent branches in canonical coordinates become squeezed/displaced coherent branches in physical coordinates.

Thus phase-sensitive deterministic processing changes optimal mode matching, not the channel's fundamental quantum/classical boundary.

---

## 8. Singular and orientation-reversing cases

This note deliberately does not claim the same finite-probe construction for every one-mode Gaussian canonical class.

Open/special cases include

- rank-deficient noise $Y$;
- singular $X$;
- orientation-reversing $\det X<0$ phase-conjugating canonical classes.

Some such classes are entanglement breaking by their canonical structure; others, such as singular one-quadrature-noise limits, require separate treatment rather than an unbounded-squeezing limit.

Do not broaden the theorem beyond

$$
\det X>0,
\qquad
Y>0
$$

without an explicit proof.

---

## 9. Novelty interpretation

The canonical-unitary equivalence itself is established work by Holevo and by Caruso–Giovannetti–Holevo.

The only potentially new content is the combination with the binary coherent NPT/EB theorem:

$$
\boxed{
\text{regular one-mode Gaussian non-EB channel}
\Longleftrightarrow
\text{NPT output of a matched two-branch equal-covariance pure-Gaussian probe}.
}
$$

This remains a corollary of the project's Candidate A and inherits its unverified novelty status.

---

## 10. Strongest next theorem audit

Determine whether the remaining non-EB singular one-mode Gaussian class can also be detected by a finite two-branch pure-Gaussian probe, or whether finite squeezing fails and the regular theorem is genuinely maximal.