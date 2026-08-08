# Complete One-Mode Gaussian Two-Branch Probe Theorem

**Date:** 2026-08-07  
**Status:** Candidate theorem obtained by combining the direct phase-insensitive binary-coherent result with established one-mode Gaussian canonical classification and a finite-noise regularization argument for the singular $B_1$ class. Novelty is unverified.

## 1. Statement

Let $\mathcal N$ be an arbitrary one-mode bosonic Gaussian channel.

Then

$$
\boxed{
\mathcal N\text{ is non-entanglement-breaking}
}
$$

if and only if there exists a **finite** hybrid qubit–bosonic pure state of the form

$$
\boxed{
|\Psi_G\rangle
=
\sqrt p\,|0\rangle|\psi_0\rangle
+e^{i\phi}\sqrt{1-p}\,|1\rangle|\psi_1\rangle,
}
$$

with

$$
0<p<1,
$$

where $|\psi_0\rangle$ and $|\psi_1\rangle$ are two distinct displaced copies of one **finite-covariance pure Gaussian state**, such that

$$
\boxed{
(I\otimes\mathcal N)(|\Psi_G\rangle\langle\Psi_G|)
\text{ is NPT}.
}
$$

Thus a qubit reference plus only **two pure Gaussian branches of equal covariance** is sufficient to expose every non-EB one-mode Gaussian channel.

The converse is immediate: an EB channel produces a separable output for every bipartite input.

The nontrivial content is sufficiency of this restricted two-branch probe family.

---

## 2. Established canonical classification used

One-mode Gaussian channels are classified up to Gaussian input/output unitaries into the canonical classes commonly denoted

$$
A_1,\ A_2,\ B_1,\ B_2,\ C,\ D.
$$

This classification is established work of Holevo and Caruso–Giovannetti–Holevo.

The present proof proceeds class by class.

---

## 3. Rank-zero / rank-one signal classes $A_1,A_2$

For a one-mode Gaussian channel with

$$
\det X=0,
$$

we have

$$
X\Omega X^T
=(\det X)\Omega
=0.
$$

The Gaussian complete-positivity condition reduces to the requirement that the output noise itself satisfies the quantum uncertainty lower bound.

The general Gaussian entanglement-breaking criterion requires a decomposition

$$
Y=Y_1+Y_2,
$$

with

$$
Y_1
$$

a valid output-state covariance contribution and

$$
Y_2
$$
large enough to account for the transformed input symplectic form.

When

$$
X\Omega X^T=0,
$$

choose simply

$$
Y_1=Y,
\qquad
Y_2=0.
$$

Thus every physical $\det X=0$ one-mode Gaussian channel is EB.

Therefore the $A_1/A_2$ classes require no non-EB probe.

---

## 4. Orientation-reversing class $D$

For one mode,

$$
X\Omega X^T
=(\det X)\Omega.
$$

Let

$$
\tau=\det X<0.
$$

The complete-positivity noise threshold contains the sum

$$
1+|\tau|.
$$

Equivalently, after canonical Gaussian unitaries the phase-conjugating class has precisely the minimum noise required to satisfy the Gaussian EB decomposition.

Hence physical one-mode orientation-reversing / gauge-contravariant canonical channels are entanglement breaking.

This is consistent with Holevo's general Gaussian EB criterion and the standard one-mode canonical classification.

Thus class $D$ also requires no non-EB probe.

---

## 5. Regular orientation-preserving classes $B_2$ and $C$

For

$$
\det X>0,
\qquad
Y>0,
$$

the channel is Gaussian-unitarily equivalent to a phase-insensitive canonical channel

$$
\Phi_{\tau,m}.
$$

The construction is explicit.

Choose a symplectic $S_{\rm out}$ such that

$$
S_{\rm out}YS_{\rm out}^T
=yI.
$$

Let

$$
\tau=\det X>0.
$$

Then choose

$$
S_{\rm in}
=\sqrt\tau X^{-1}S_{\rm out}^{-1}.
$$

Since

$$
\det S_{\rm in}=1,
$$

it is symplectic in one mode, and

$$
S_{\rm out}XS_{\rm in}
=\sqrt\tau I.
$$

Therefore

$$
\mathcal U_{\rm out}
\circ\mathcal N
\circ\mathcal U_{\rm in}
=\Phi_{\tau,m}
$$

for the corresponding canonical noise parameter $m$.

The direct theorem in `DIRECT_GAUSSIAN_BINARY_PROBE_PROOF.md` gives, for **every** finite nontrivial coherent pair,

$$
(I\otimes\Phi_{\tau,m})(|\Psi_{\alpha\beta}\rangle\langle\Psi_{\alpha\beta}|)
\text{ NPT}
\iff
\Phi_{\tau,m}\text{ non-EB}.
$$

Pulling the coherent branches back through the common input Gaussian unitary produces two equal-covariance pure Gaussian states for the original channel.

Local output Gaussian unitaries preserve NPT.

Therefore every non-EB regular orientation-preserving one-mode Gaussian channel has the required finite two-branch probe.

---

## 6. Gaussian unitary case

If

$$
\det X=1,
\qquad
Y=0,
$$

the channel itself is a Gaussian unitary.

Choose any two distinct finite coherent states and any nonzero branch weights:

$$
|\Psi\rangle
=
\sqrt p|0\rangle|\alpha\rangle
+e^{i\phi}\sqrt{1-p}|1\rangle|\beta\rangle.
$$

The input is a pure entangled state.

A local unitary preserves its Schmidt coefficients, so the output remains pure entangled and therefore NPT.

Thus the noiseless boundary is included trivially.

---

## 7. Singular one-quadrature-noise class $B_1$

The remaining nontrivial singular class has

$$
\det X=1
$$

but rank-one noise.

In suitable canonical quadratures it can be viewed as identity transmission plus finite Gaussian noise in only one quadrature.

Denote this channel

$$
\mathcal B_1.
$$

We do **not** obtain it by taking an infinite-squeezing limit of the regular theorem.

Instead, add a finite arbitrarily weak Gaussian noise channel $\mathcal A_\epsilon$ in the previously noiseless quadrature:

$$
\boxed{
\mathcal N_\epsilon
=\mathcal A_\epsilon\circ\mathcal B_1.
}
$$

For every finite original $B_1$ noise strength, choose

$$
\epsilon>0
$$

small enough that the full-rank anisotropic additive-noise channel $\mathcal N_\epsilon$ remains non-EB.

This is always possible because its canonical isotropic noise scale is proportional to the geometric mean of the two quadrature-noise strengths and can be made arbitrarily small as $\epsilon\to0^+$.

Since $\mathcal N_\epsilon$ is regular and non-EB, Section 5 gives a **finite** equal-covariance two-branch pure-Gaussian input $|\Psi_{G,\epsilon}\rangle$ such that

$$
(I\otimes\mathcal N_\epsilon)
(|\Psi_{G,\epsilon}\rangle\langle\Psi_{G,\epsilon}|)
$$

is NPT.

But

$$
\mathcal N_\epsilon
=\mathcal A_\epsilon\circ\mathcal B_1
$$

is only local post-processing of the $B_1$ output.

If the $B_1$ output had positive partial transpose, applying the local CP map $\mathcal A_\epsilon$ could not make it NPT.

Therefore

$$
\boxed{
(I\otimes\mathcal B_1)
(|\Psi_{G,\epsilon}\rangle\langle\Psi_{G,\epsilon}|)
\text{ is already NPT}.
}
$$

The probe is finite because $\epsilon$ is chosen finite.

Thus the singular $B_1$ class is covered without an infinite-energy limiting state.

---

## 8. Exhaustion of one-mode canonical classes

The canonical classes are now exhausted:

### $A_1,A_2$

EB.

### $D$

EB.

### $B_2,C$

Regular orientation-preserving; finite equal-covariance two-branch pure-Gaussian probe exists.

### Gaussian unitary boundary

Trivial finite probe exists.

### $B_1$

Finite probe exists by regularization plus PPT monotonicity under local post-processing.

Therefore every non-EB one-mode Gaussian channel is detected by some finite probe of the claimed restricted form.

---

## 9. Final theorem

We obtain the candidate theorem

$$
\boxed{
\mathcal N\text{ non-EB}
\iff
\exists\ |\Psi_G\rangle
\text{ with two finite equal-covariance pure-Gaussian branches such that}
(I\otimes\mathcal N)(|\Psi_G\rangle\langle\Psi_G|)
\text{ is NPT}.
}
$$

The reference system needs only be a qubit.

The bosonic probe needs only two displaced branches.

No infinite squeezing or infinite coherent amplitude is required.

---

## 10. Stronger phase-insensitive specialization

For the gauge-covariant phase-insensitive family, the theorem is substantially stronger:

$$
\boxed{
\Phi_{\tau,m}\text{ non-EB}
\iff
\text{the output is NPT for every finite nontrivial binary coherent hybrid input}.
}
$$

Thus the general one-mode theorem is an **existence** statement, while the phase-insensitive theorem is an **all-nontrivial-probes** statement.

This distinction should remain explicit.

---

## 11. Why this result could matter beyond gravity

The EB definition normally quantifies over arbitrary ancilla dimensions and arbitrary entangled inputs.

This theorem says that for the entire one-mode Gaussian channel class, testing EB versus non-EB never requires that enormous input space:

> **A qubit plus two finite pure-Gaussian branches is always enough.**

The matched branch covariance may depend on the channel, but the probe structure is minimal.

This is potentially a useful standalone continuous-variable quantum-information result if it is not already known.

---

## 12. Novelty warning

The following ingredients are established:

- Holevo's one-mode Gaussian canonical classification;
- the general Gaussian entanglement-breaking criterion;
- Gaussian-unitary equivalence;
- monotonicity of PPT under local completely positive maps.

The potentially new result is only their combination with the project's direct binary-coherent theorem to obtain a universal **finite two-branch pure-Gaussian probe sufficiency** statement.

A broad literature search is still required before any originality claim.

---

## 13. Strongest next step

Search specifically for prior results stating that the entanglement-breaking property of an arbitrary one-mode Gaussian channel can be tested with

- a qubit ancilla;
- only two displaced pure-Gaussian branches;
- finite squeezing/energy;
- NPT as the output criterion.

If no equivalent result is found, this theorem may be cleaner and more publishable as a standalone mathematical paper than the gravity application itself.