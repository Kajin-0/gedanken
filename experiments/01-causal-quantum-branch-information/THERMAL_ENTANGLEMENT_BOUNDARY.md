# Weak-Branch Thermal Entanglement Boundary

**Timestamp:** 2026-08-07 15:28 EDT  
**Status:** Active derivation for Experiment 01

This note asks whether the thermal capture threshold derived from the fidelity witness is fundamental, or merely a witness threshold.

---

## 1. Setup

Use the wave-zone single difference mode. Before capture, write the source-field state as

$$
|\Psi\rangle
=\frac{|L\rangle|+a\rangle+|R\rangle|-a\rangle}{\sqrt2},
$$

with

$$
N_\Delta=4|a|^2.
$$

Send the field mode through a thermal attenuator with transmissivity $\eta$ and environment occupation $\bar n$.

The question is:

> For arbitrarily small branch separation $|a|\to0$, when does any source-receiver entanglement survive?

---

## 2. Small-branch expansion

Switch to the source basis

$$
|+\rangle=\frac{|L\rangle+|R\rangle}{\sqrt2},
\qquad
|-\rangle=\frac{|L\rangle-|R\rangle}{\sqrt2}.
$$

For $|a|\ll1$,

$$
|\Psi\rangle
=|+\rangle|0\rangle+a|-\rangle|1\rangle+O(a^2).
$$

Thus the channel only needs to be evaluated on

$$
|0\rangle\langle0|,
\qquad
|1\rangle\langle0|,
\qquad
|1\rangle\langle1|
$$

to determine the first nontrivial PPT behavior.

---

## 3. Useful thermal-attenuator decomposition

Define

$$
m=(1-\eta)\bar n,
\qquad
G=1+m.
$$

The thermal attenuator can be represented as a quantum-limited pure-loss channel followed by a quantum-limited amplifier with gain $G$ and effective loss transmissivity $\eta/G$.

The vacuum output is

$$
\Lambda(|0\rangle\langle0|)
=\sum_{k=0}^{\infty}p_k|k\rangle\langle k|,
$$

with

$$
\boxed{
p_k=\frac{m^k}{G^{k+1}}.
}
$$

The one-quantum coherence becomes

$$
\Lambda(|1\rangle\langle0|)
=\sum_{k=0}^{\infty}x_k|k+1\rangle\langle k|,
$$

with

$$
\boxed{
x_k
=\frac{\sqrt{\eta(k+1)}\,m^k}{G^{k+2}}.
}
$$

Finally,

$$
\Lambda(|1\rangle\langle1|)
=\sum_{k=0}^{\infty}y_k|k\rangle\langle k|,
$$

where

$$
y_0=\frac{G-\eta}{G^2},
$$

and for $k\ge1$,

$$
\boxed{
y_k
=\frac{\eta k m^{k-1}+(G-\eta)m^k}{G^{k+2}}.
}
$$

---

## 4. Partial transpose block structure

After partial transpose on the source qubit, each Fock sector contains a $2\times2$ block in the basis

$$
\{|+,k+1\rangle,|-,k\rangle\}
$$

of the form

$$
M_k
=\begin{pmatrix}
 p_{k+1} & a x_k\\
 a^*x_k & |a|^2y_k
\end{pmatrix}
+O(|a|^3).
$$

For sufficiently small $|a|$, this block has a negative eigenvalue iff

$$
x_k^2>p_{k+1}y_k.
$$

Direct substitution gives

$$
\boxed{
x_k^2-p_{k+1}y_k
=\frac{m^{2k}}{G^{2k+4}}
\left[\eta-(G-\eta)m\right].
}
$$

The important fact is that **the sign is independent of $k$**.

Thus every potentially negative Fock block turns on at the same threshold.

---

## 5. Exact weak-branch entanglement threshold

Using

$$
m=(1-\eta)\bar n,
\qquad
G=1+m,
$$

the sign condition becomes

$$
\eta>(G-\eta)m.
$$

The bracket factors as

$$
\eta-(G-\eta)m
=
[\eta(\bar n+1)-\bar n]
[\bar n+1-\eta\bar n].
$$

The second factor is positive for $0\le\eta\le1$, so the entanglement condition is

$$
\boxed{
\eta>\eta_{\rm ent}
=\frac{\bar n}{\bar n+1}.
}
$$

This is exactly the known entanglement-breaking boundary of the bosonic thermal attenuator.

Therefore, in the infinitesimal branch-separation limit, **our specific cat-source/difference-mode family becomes entangled immediately when the thermal channel ceases to be entanglement-breaking.**

---

## 6. Leading weak-branch negativity

For finite thermal occupation $\bar n>0$, the negative eigenvalue in each block is $O(|a|^2)$, and summing the blocks gives

$$
\boxed{
\mathcal N_{AB}
=
|a|^2
\frac{\eta-(G-\eta)m}{mG}
+O(|a|^4)
}
$$

whenever the bracket is positive.

Equivalently, since $N_\Delta=4|a|^2$,

$$
\boxed{
\mathcal N_{AB}
=\frac{N_\Delta}{4}
\frac{[\eta(\bar n+1)-\bar n][\bar n+1-\eta\bar n]}
{(1-\eta)\bar n[1+(1-\eta)\bar n]}
+O(N_\Delta^2).
}
$$

The vacuum limit $\bar n\to0$ is nonuniform. There the leading negativity scales as

$$
\mathcal N_{AB}\sim|a|\sqrt{\eta},
$$

consistent with entanglement surviving every nonzero pure-loss transmissivity.

---

## 7. Three thermal regimes

The fundamental weak-branch entanglement threshold is

$$
\boxed{
\eta_{\rm ent}=\frac{\bar n}{\bar n+1}.
}
$$

The simpler fidelity-history witness derived previously requires

$$
\boxed{
\eta_F=\frac{2\bar n+1}{2\bar n+2}.
}
$$

These satisfy

$$
\boxed{
\eta_F=\frac{1+\eta_{\rm ent}}{2}.
}
$$

Therefore the thermal channel separates into three regions:

### Region I — impossible

$$
\eta\le\frac{\bar n}{\bar n+1}.
$$

The thermal attenuator is entanglement-breaking. No source-receiver entanglement can survive for any input.

### Region II — entangled but not certified by the low-cost fidelity witness

$$
\frac{\bar n}{\bar n+1}
<\eta\le
\frac{2\bar n+1}{2\bar n+2}.
$$

The weak cat-source state is already entangled, but

$$
C_\Xi\le F_B
$$

is not violated.

### Region III — strong history witness

$$
\eta>
\frac{2\bar n+1}{2\bar n+2}.
$$

The simple fidelity-history witness certifies the entanglement directly.

---

## 8. Matched-memory form

For the input-output receiver

$$
\eta=\frac{\kappa_g}{\kappa_g+\kappa_i},
$$

with thermal internal bath occupation $\bar n_i$, the fundamental entanglement-transfer condition becomes

$$
\boxed{
\kappa_g>\bar n_i\kappa_i.
}
$$

The low-cost fidelity witness requires the stronger

$$
\boxed{
\kappa_g>(2\bar n_i+1)\kappa_i.
}
$$

Thus thermal loss produces a clear hierarchy:

$$
\boxed{
\text{entanglement possible: }\kappa_g>\bar n_i\kappa_i
}
$$

versus

$$
\boxed{
\text{simple history witness: }\kappa_g>(2\bar n_i+1)\kappa_i.
}
$$

At zero temperature, any nonzero gravitational capture can in principle transfer some entanglement, while the simple history witness still requires gravitational coupling to exceed internal loss.

---

## 9. Literature boundary

The thermal attenuator's entanglement-breaking transition is established Gaussian-channel theory. Mari, Zippilli, and Vitali (Phys. Rev. D 113, L021905, 2026) already formulate a gravity-induced thermal attenuator and use its entanglement-breaking/non-entanglement-breaking transition as a nonclassicality criterion.

Therefore **the threshold $\eta>\bar n/(\bar n+1)$ is not a new channel-theory result.**

The useful result for this project is narrower:

> the specific wave-zone source-cat / coherent gravitational difference-mode construction reaches that channel boundary already in the weak-branch limit, while the history-fidelity witness has a distinct, stricter threshold.

This gives an explicit separation between **fundamental entanglement transfer** and **low-measurement-cost history certification** in the causal gravitational-wave setting.

---

## 10. Immediate next step

The next target is the finite-$N_\Delta$ problem:

1. determine whether the exact cat-source state remains entangled throughout the entire non-entanglement-breaking region for arbitrary branch separation;
2. optimize branch separation $N_\Delta$ at finite temperature;
3. derive the lowest-complexity observable witness capable of closing the gap between $\eta_{\rm ent}$ and $\eta_F$.
