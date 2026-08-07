# Vacuum Capture Optimization and the Weak-Coupling Entanglement Rate

**Timestamp:** 2026-08-07 15:44 EDT  
**Status:** Active derivation for Experiment 01

This note asks whether an arbitrarily strong branch-dependent gravitational wave can compensate for an extremely small coherent capture efficiency. The answer is no for entanglement transfer: increasing the branch separation also increases the which-branch record left in the uncaptured field.

---

## 1. Exact pure-loss wave-zone state

Let the outgoing gravitational difference mode carry branch coherent states

$$
|+a\rangle,
\qquad
|-a\rangle,
$$

with

$$
N_\Delta=4|a|^2.
$$

Let the receiver coherently capture fraction $\eta$ of this mode. The exact pure global state after the capture beamsplitter is

$$
|\Psi\rangle_{ABE}
=
\frac{1}{\sqrt2}
\left(
|L\rangle
|+\sqrt\eta\,a\rangle_B
|+\sqrt{1-\eta}\,a\rangle_E
+
|R\rangle
|-\sqrt\eta\,a\rangle_B
|-\sqrt{1-\eta}\,a\rangle_E
\right).
$$

Define

$$
s_B=e^{-\eta N_\Delta/2},
\qquad
s_E=e^{-(1-\eta)N_\Delta/2}.
$$

The exact source-receiver negativity is

$$
\boxed{
\mathcal N(\eta,N_\Delta)
=
\frac14
\left[
\sqrt{(1+s_E)^2-4s_Es_B^2}
-(1-s_E)
\right].
}
$$

---

## 2. Why arbitrarily large branch radiation does not help

At fixed imperfect capture $0<\eta<1$,

$$
N_\Delta\to\infty
$$

implies

$$
s_E\to0.
$$

The uncaptured field then contains an essentially perfect record of the source branch. Consequently

$$
\boxed{
\mathcal N(\eta,N_\Delta)\to0
\qquad
(N_\Delta\to\infty,\ \eta<1).
}
$$

Thus a huge classical branch-dependent gravitational-wave signal is not automatically a good quantum-information carrier. If most of that wave remains outside the receiver, it classicalizes the source alternative by leaving an orthogonal environmental record.

This is the central tradeoff:

$$
\boxed{
\text{stronger branch signal}
\quad\leftrightarrow\quad
\text{stronger uncaptured which-path record}.
}
$$

---

## 3. Weak-capture asymptotics

Take

$$
\eta=\epsilon^2,
\qquad
\epsilon\ll1,
$$

and allow the branch-radiation strength to scale as

$$
N_\Delta=c\epsilon.
$$

Expanding the exact negativity gives

$$
\boxed{
\mathcal N
=
\epsilon^2
-
\frac{c^2+16}{4c}\epsilon^3
+O(\epsilon^4).
}
$$

Since

$$
\epsilon^2=\eta,
$$

this is

$$
\mathcal N
=
\eta
-
\left(
\frac{c}{4}+\frac{4}{c}
\right)
\eta^{3/2}
+O(\eta^2).
$$

The correction is minimized at

$$
\boxed{c=4.}
$$

Therefore the optimal branch-difference occupation is

$$
\boxed{
N_\Delta^{\rm opt}
=4\sqrt\eta+O(\eta).
}
$$

At this optimum,

$$
\boxed{
\mathcal N_{\max}(\eta)
=
\eta-2\eta^{3/2}+O(\eta^2).
}
$$

So, to leading order,

$$
\boxed{
\mathcal N_{\max}\sim\eta.
}
$$

---

## 4. Consequence for a weak gravitational receiver

For an ideal lossless matched receiver at short times after causal arrival,

$$
\eta(\tau)
=1-e^{-\kappa_g\tau}
\simeq\kappa_g\tau,
\qquad
\kappa_g\tau\ll1.
$$

Hence the optimized branch strength is

$$
\boxed{
N_\Delta^{\rm opt}(\tau)
\simeq
4\sqrt{\kappa_g\tau},
}
$$

and the maximum source-receiver negativity grows as

$$
\boxed{
\mathcal N_{\max}(\tau)
\simeq
\kappa_g\tau.
}
$$

Therefore an $O(1)$ amount of source-receiver entanglement requires a time of order

$$
\boxed{
\tau\sim\kappa_g^{-1}.
}
$$

This result is stronger than simply observing that the receiver coupling is weak. It shows that **even unlimited coherent branch-wave amplitude cannot parametrically beat the gravitational quantum-capture rate when the goal is to transfer entanglement.**

---

## 5. Contrast with stimulated classical detection

A strong coherent gravitational wave can stimulate transitions in a resonant detector at a rate much faster than its spontaneous graviton-emission rate. This is the basis of stimulated single-graviton sensing proposals.

But the present task is different.

For ordinary detection, a huge coherent field is useful because only the receiver response matters.

For entanglement transfer, the source remains part of the quantum state. The portion of the branch-dependent gravitational field that is **not** coherently captured is an environment carrying source-branch information.

Thus increasing the coherent field amplitude simultaneously increases

1. the receiver's branch-dependent displacement;
2. the environmental which-branch record.

At tiny capture efficiency, the second effect prevents arbitrarily strong stimulation from producing large source-receiver entanglement.

This yields an important distinction:

$$
\boxed{
\text{large classical signal rate}
\not\Rightarrow
\text{large quantum entanglement-transfer rate}.
}
$$

---

## 6. Why the optimum becomes a weak source cat

As

$$
\eta\to0,
$$

the optimum satisfies

$$
N_\Delta^{\rm opt}\to0.
$$

This may look counterintuitive. The reason is that, when the receiver captures almost none of the wave, a large branch separation makes the uncaptured environment distinguish $L$ from $R$ essentially perfectly.

The optimal strategy is therefore to make the two gravitational wave histories only weakly distinguishable, so the tiny captured portion can carry some coherent correlation without the much larger uncaptured portion fully measuring the source.

---

## 7. Gravity-specific implication

Since

$$
\kappa_g
=\frac{2G\omega_B^5}{5\hbar c^5}
Q_{ij}^{10}Q_{ij}^{01},
$$

the initial optimized entanglement-transfer rate is

$$
\boxed{
\frac{d\mathcal N_{\max}}{dt}
\simeq
\frac{2G\omega_B^5}{5\hbar c^5}
Q_{ij}^{10}Q_{ij}^{01}.
}
$$

Thus the spontaneous-graviton linewidth has acquired a second operational meaning:

> **it is also the leading maximum rate at which an ideally matched weakly coupled receiver can acquire source entanglement from a branch-dependent gravitational wave.**

This statement is within the ideal coherent pure-loss difference-mode model.

---

## 8. Literature boundary

Optimization of entangled coherent states under bosonic loss is an established quantum-optics topic, and cat-state encodings are known to exhibit an amplitude-versus-loss tradeoff. Therefore no novelty is claimed for the mathematical fact that coherent-state entanglement has an optimal amplitude under loss.

The potentially distinctive gravity-specific interpretation is:

$$
\boxed{
\text{stimulated gravitational response can be large,}
\quad
\text{while entanglement transfer remains }O(\kappa_g).
}
$$

That distinction is highly relevant to the Gedanken experiment because it separates **detecting a gravitational wave** from **demonstrating that the gravitational channel coherently transported a quantum alternative**.

---

## 9. Immediate next step

The next step is to test whether a comparable rate bound survives finite thermal occupation. In particular, optimize the weak-cat negativity over $N_\Delta$ near the thermal channel boundary and determine how the maximum entanglement-growth rate scales with

$$
\delta=\kappa_g-\bar n_i\kappa_i.
$$

A result of the form

$$
\mathcal N_{\max}\propto\delta\,t
$$

would make the critical slowing of the causal entanglement front an information-transfer rate law rather than only an onset-time statement.