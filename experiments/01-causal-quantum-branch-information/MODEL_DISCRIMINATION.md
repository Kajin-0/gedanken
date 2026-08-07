# Competing-Model Predictions in the History Plane

**Timestamp:** 2026-08-07 14:40 EDT

The enclosing wave-zone receiver makes the conceptual alternatives unusually sharp. Choose source branches with opposite quadrupole histories,

$$
q_L(t)=+q(t),
\qquad
q_R(t)=-q(t),
$$

so the balanced source state has vanishing branch-averaged quadrupole.

Use the operational coordinates

$$
C_\Xi=\|\Xi\|_1,
\qquad
D_B=\frac12\|\rho_L-\rho_R\|_1.
$$

Every balanced separable source-receiver state obeys

$$
C_\Xi^2+D_B^2\le1.
$$

The three simplest physical pictures populate different parts of this plane.

---

## 1. Semiclassical mean-field response

A semiclassical metric sourced only by the expectation value of the stress tensor responds to the branch average. For equal opposite quadrupoles,

$$
\langle q\rangle=0.
$$

The receiver therefore has one common gravitational history rather than branch-conditioned histories:

$$
\rho_L=\rho_R.
$$

Hence

$$
\boxed{D_B=0.}
$$

If the mean-field evolution itself introduces no additional decoherence,

$$
\boxed{C_\Xi=1.}
$$

Thus the ideal mean-field model sits at

$$
\boxed{(C_\Xi,D_B)=(1,0).}
$$

It preserves source coherence but communicates no branch information.

---

## 2. Classical branch-resolving response

Suppose instead a classical gravitational channel determines enough about the source branch to emit the corresponding classical waveform and drive the receiver conditionally.

The receiver can then have

$$
D_B>0,
$$

but acquisition of a classical branch record reduces the off-diagonal history coherence. In the fully branch-resolved limit,

$$
\boxed{C_\Xi=0.}
$$

The source-receiver state is then a separable mixture such as

$$
\rho_{AB}^{\rm cl}
=\frac12|L\rangle\langle L|\otimes\rho_B^L
+\frac12|R\rangle\langle R|\otimes\rho_B^R.
$$

More generally, partial classical branch acquisition remains constrained by

$$
\boxed{C_\Xi^2+D_B^2\le1.}
$$

This family trades recoverable source-history coherence for branch knowledge at the receiver.

---

## 3. Coherent quantum gravitational response

A coherent quantum mediator can condition the receiver on the source branch without selecting one. For perfect coherent capture of the outgoing branch-difference mode,

$$
|\Psi_{AB}\rangle
=\frac{|L\rangle|B_L\rangle+|R\rangle|B_R\rangle}{\sqrt2}.
$$

The off-diagonal block is

$$
\Xi=|B_L\rangle\langle B_R|,
$$

so

$$
\boxed{C_\Xi=1}
$$

regardless of how distinguishable the two normalized receiver states become.

For coherent receiver branches separated by difference-mode graviton number $N_\Delta$,

$$
\boxed{D_B^2=1-e^{-N_\Delta}.}
$$

Therefore

$$
\boxed{\mathcal W_\Xi=D_B^2>0}
$$

for any nonzero captured branch separation.

The quantum model can therefore occupy

$$
\boxed{C_\Xi^2+D_B^2>1,}
$$

a region forbidden to every separable source-receiver state.

---

## 4. Why force or waveform measurement alone is insufficient

A branch-resolving classical model and a coherent quantum model can both produce different receiver trajectories conditioned on $L$ and $R$. Thus observing

$$
D_B>0
$$

or observing the correct gravitational waveform is not enough.

The difference is whether coherence remains between those two conditional histories:

$$
\boxed{
\text{classicalized branch response: }D_B>0,\;C_\Xi\text{ reduced}
}
$$

versus

$$
\boxed{
\text{coherent quantum response: }D_B>0,\;C_\Xi\text{ can remain near }1.
}
$$

This is why the Gedanken experiment must contain an eraser-aligned joint coherence measurement rather than only a gravitational-force or wave measurement.

---

## 5. The clean idealized table

| Model | Branch signal at receiver | Recoverable history coherence | Ideal location |
|---|---:|---:|---:|
| Mean-field classical | $D_B=0$ | $C_\Xi=1$ | $(1,0)$ |
| Fully branch-resolving classical | $D_B>0$ | $C_\Xi=0$ | $(0,D_B)$ |
| Partially classicalized / separable | $D_B\ge0$ | reduced | inside $C_\Xi^2+D_B^2\le1$ |
| Coherent quantum, perfect capture | $D_B>0$ | $C_\Xi=1$ | outside separable disk |

The geometry of this plane provides a compact conceptual summary of the experiment.

---

## 6. Einstein/Feynman compression

> A mean classical field can preserve the superposition, but then it sees only the average mass distribution and carries no information about which branch exists. A classical field that does carry the branch must acquire a classical record, and the source pays for that knowledge with lost recoverable coherence. A quantum field has a third option: it can carry both branch-dependent waveforms coherently. The receiver can then learn the branch while the relation between the two histories remains available for an eraser. The experiment therefore measures two things, not one: how different the gravitational futures are, and whether quantum coherence still connects them.