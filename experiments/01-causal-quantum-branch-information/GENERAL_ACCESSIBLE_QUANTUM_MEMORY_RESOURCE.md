# General Accessible Quantum-Memory Resource

**Timestamp:** 2026-08-07 18:04 EDT  
**Status:** Channel-theoretic generalization of the capture→readout accessibility idea. The basic resource-theory ingredients are established quantum-information concepts; the gravity-specific use is the research contribution under investigation.

## 1. Why the Gaussian quantum excess is not universal

For a gauge-covariant phase-insensitive Gaussian channel,

$$
\Phi_{\tau,m},
$$

the sign

$$
\Delta_Q=\tau-m
$$

exactly separates the non-entanglement-breaking region from the entanglement-breaking region.

For a capture channel followed by a readout channel,

$$
\Delta_{\rm acc}
=\tau_r(\tau_c-m_c)-m_r
$$

therefore gives an exact scalar accessibility criterion.

But $\tau-m$ is tied to one Gaussian parameterization. A relativistic field receiver, a compact object, a non-Gaussian memory, or a heralded readout generally has no preferred pair $(\tau,m)$.

The universal structure is instead the distance of a channel from the set of **entanglement-breaking channels**.

---

## 2. Entanglement-breaking robustness of a receiver channel

Let $\mathrm{EB}$ denote the convex set of entanglement-breaking channels from an incoming branch mode to a receiver register.

Define the generalized EB robustness

$$
\boxed{
R_{\rm EB}(\mathcal N)
=
\inf\left\{
 s\ge0:
 \frac{\mathcal N+s\mathcal M}{1+s}
 \in\mathrm{EB}
 \text{ for some channel }\mathcal M
\right\}.
}
$$

Then

$$
\boxed{
R_{\rm EB}(\mathcal N)=0
\iff
\mathcal N\in\mathrm{EB}.
}
$$

A convenient logarithmic version is

$$
\boxed{
E_{\rm mem}(\mathcal N)
=\log[1+R_{\rm EB}(\mathcal N)].
}
$$

This can be interpreted as a channel-level **quantum-memory resource**: it vanishes exactly when the receiver channel is incapable of preserving entanglement with any reference system.

The exact choice of robustness is not unique. The point is that the free set is the EB set, which is the operationally correct boundary for whether a receiver can carry quantum correlations from the branch mode into an accessible register.

---

## 3. Post-processing monotonicity

Let $\mathcal R$ be any deterministic readout channel applied after $\mathcal N$.

Suppose

$$
\frac{\mathcal N+s\mathcal M}{1+s}
=\mathcal E
$$

is entanglement breaking.

Post-compose with $\mathcal R$:

$$
\frac{\mathcal R\circ\mathcal N
+s\,\mathcal R\circ\mathcal M}{1+s}
=
\mathcal R\circ\mathcal E.
$$

Because post-processing an EB channel remains EB,

$$
\mathcal R\circ\mathcal E\in\mathrm{EB}.
$$

Therefore the same $s$ is feasible for the composed channel and

$$
\boxed{
R_{\rm EB}(\mathcal R\circ\mathcal N)
\le
R_{\rm EB}(\mathcal N).
}
$$

Thus **accessibility processing cannot increase the quantum-memory resource already captured internally.**

---

## 4. Pre-processing monotonicity

Now let $\mathcal C$ be any deterministic channel applied before $\mathcal N$.

If

$$
(\mathcal N+s\mathcal M)/(1+s)
$$

is EB, then

$$
\frac{\mathcal N\circ\mathcal C
+s\,\mathcal M\circ\mathcal C}{1+s}
$$

is also EB because pre-processing cannot make an EB channel preserve input-reference entanglement.

Hence

$$
\boxed{
R_{\rm EB}(\mathcal N\circ\mathcal C)
\le
R_{\rm EB}(\mathcal N).
}
$$

---

## 5. General bottleneck theorem for capture→readout

Let

$$
\mathcal C:
\text{incoming gravitational branch mode}
\to
\text{internal receiver mode}
$$

be the capture channel, and let

$$
\mathcal R:
\text{internal receiver mode}
\to
\text{accessible register}
$$

be the readout channel.

The accessible channel is

$$
\boxed{
\mathcal A
=\mathcal R\circ\mathcal C.
}
$$

Applying the two monotonicity statements gives

$$
\boxed{
R_{\rm EB}(\mathcal A)
\le
\min\left\{
R_{\rm EB}(\mathcal C),
R_{\rm EB}(\mathcal R)
\right\}.
}
$$

Equivalently,

$$
\boxed{
E_{\rm mem}(\mathcal A)
\le
\min\left\{
E_{\rm mem}(\mathcal C),
E_{\rm mem}(\mathcal R)
\right\}.
}
$$

This is the general **accessible quantum-memory bottleneck law**.

No receiver can be a better accessible quantum memory than either

1. its gravitational capture stage, or
2. its readout/accessibility stage.

---

## 6. Important asymmetry: two non-EB stages can still compose to EB

The bottleneck upper bound is not an equality in general.

Even if

$$
R_{\rm EB}(\mathcal C)>0
$$

and

$$
R_{\rm EB}(\mathcal R)>0,
$$

the composition

$$
\mathcal R\circ\mathcal C
$$

can still be entanglement breaking.

The Gaussian cascade already gives an explicit example. Capture and readout may each be individually non-EB while their accumulated noise satisfies

$$
\tau_r(\tau_c-m_c)\le m_r,
$$

making the accessible channel EB.

Therefore the general receiver problem cannot be reduced to checking each stage separately. The **complete composed channel** matters.

---

## 7. Arbitrary-channel entanglement data processing

Let $E$ be any bipartite entanglement monotone nonincreasing under local deterministic channels. For any source–incoming-mode state $\rho_{SA}$,

$$
\rho_{SB}^{\rm cap}
=(I_S\otimes\mathcal C)(\rho_{SA}),
$$

and

$$
\rho_{SC}^{\rm acc}
=(I_S\otimes\mathcal R)(\rho_{SB}^{\rm cap}).
$$

Then

$$
\boxed{
E(\rho_{SC}^{\rm acc})
\le
E(\rho_{SB}^{\rm cap}).
}
$$

For negativity in particular,

$$
\boxed{
\mathcal N_{S:C}^{\rm acc}
\le
\mathcal N_{S:B}^{\rm cap}.
}
$$

This gives the state-level counterpart of the channel bottleneck law.

A strongly gravitating absorber may generate large internal source–receiver entanglement while exposing only a tiny or zero accessible fraction after readout.

---

## 8. General branch-history witness after arbitrary readout

For a balanced source branch qubit and any accessible output register $C$, write

$$
\rho_{SC}
=
\frac12
\begin{pmatrix}
\rho_C^L&\Xi_C\\
\Xi_C^\dagger&\rho_C^R
\end{pmatrix}.
$$

Define

$$
\boxed{
C_C=\|\Xi_C\|_1,
}
$$

and

$$
\boxed{
D_C=\frac12\|\rho_C^L-\rho_C^R\|_1.
}
$$

Every separable source-accessible state obeys

$$
\boxed{
C_C^2+D_C^2\le1.
}
$$

Therefore

$$
\boxed{
C_C^2+D_C^2>1
}
$$

is a completely non-Gaussian accessible-entanglement witness.

This is the operational generalization of the Gaussian quantity $\Delta_{\rm acc}$.

It requires no Gaussianity, no bosonic canonical form, and no identification of a separate gravitational-field Hilbert space.

---

## 9. Complementary-channel meaning

Suppose the complete source-to-accessible evolution has a Stinespring dilation with conditional pure global outputs

$$
|\Phi_L\rangle_{CE},
\qquad
|\Phi_R\rangle_{CE}.
$$

Then

$$
\Xi_C
=\operatorname{Tr}_E
|\Phi_L\rangle\langle\Phi_R|.
$$

The trace-norm/Uhlmann identity gives

$$
\boxed{
C_C
=F(\rho_E^L,\rho_E^R).
}
$$

Thus the accessible coherence is exactly the indistinguishability of **everything that was not delivered to the accessible register**.

This is the general capture–coherence–accessibility statement:

> The source and accessible register can retain strong history coherence only when the discarded complement fails to obtain a sufficiently distinguishing branch record.

No special language about “the gravitational field subsystem” is required.

---

## 10. Gaussian cascade recovered as a special case

For phase-insensitive Gaussian capture and readout,

$$
\mathcal C=\Phi_{\tau_c,m_c},
\qquad
\mathcal R=\Phi_{\tau_r,m_r},
$$

the composition is

$$
\tau_{\rm tot}=\tau_c\tau_r,
$$

$$
m_{\rm tot}=\tau_rm_c+m_r.
$$

The binary coherent theorem makes the EB boundary exactly

$$
\tau_{\rm tot}>m_{\rm tot},
$$

or

$$
\boxed{
\tau_r(\tau_c-m_c)>m_r.
}
$$

Therefore

$$
\boxed{
\Delta_{\rm acc}
=\tau_r(\tau_c-m_c)-m_r
}
$$

is not the universal resource definition; it is the exact Gaussian coordinate whose sign agrees with the universal statement

$$
R_{\rm EB}(\mathcal A)>0.
$$

This distinction should be retained in the paper.

---

## 11. Strong-gravity interpretation

The receiver problem can now be stated without assuming oscillator dynamics.

### Capture channel

$$
\mathcal C_G:
\text{incoming gravitational branch mode}
\to
\text{internal gravitationally active degrees of freedom}.
$$

### Readout channel

$$
\mathcal R_A:
\text{internal degrees of freedom}
\to
\text{accessible controllable register}.
$$

The experiment can demonstrate accessible quantum mediation only if

$$
\boxed{
\mathcal A
=\mathcal R_A\circ\mathcal C_G
\notin\mathrm{EB}.
}
$$

Equivalently,

$$
R_{\rm EB}(\mathcal A)>0.
$$

This is meaningful for

- laboratory oscillators;
- relativistic QFT modes;
- compact stars;
- horizon/black-hole absorbers;
- non-Gaussian memories;
- distributed receiver arrays.

The model details only determine the actual channel $\mathcal A$.

---

## 12. Strongest conceptual compression

> **A quantum gravitational receiver is not defined by how much gravitational energy it absorbs. It is defined by whether the complete map from the incoming branch-dependent gravitational state to a controllable output register is non-entanglement-breaking. Capture, storage, scrambling, and readout are all parts of that one channel. Any discarded stage can only reduce the resource, and two individually quantum-capable stages can still compose into a classicalizing channel.**

This is the most general current formulation of the coupling–coherence–accessibility tradeoff.

---

## 13. Novelty status

Resource theories in which entanglement-breaking channels are the free set and channel robustness/distance measures quantify quantum-memory capability are established neighboring quantum-information ideas. The monotonicity proofs above are therefore not claimed as new mathematics.

The potentially distinctive physics is their use to reformulate the gravitational Gedanken experiment as a **complete accessible-channel test**, with the exact Gaussian front as a solvable special case and strong-gravity systems interpreted through capture→readout composition rather than absorption alone.

---

## 14. Strongest next step

The new generalization shifts the next target again:

1. Define a **time-resolved accessible channel** $\mathcal A_{R,t}$ for the gravitational experiment.
2. Define the general quantum front as
   $$
   T_{\rm Q}(R)
   =\inf\{t:R_{\rm EB}(\mathcal A_{R,t})>0\}.
   $$
3. Prove the light-cone constraint
   $$
   T_{\rm Q}(R)\ge R/c
   $$
   from locality/microcausality for the source-controlled channel.
4. Show that the Gaussian receiver theorem reduces this general definition exactly to the logarithmic front already derived.
5. Investigate whether a relativistic/strong-gravity receiver can produce a nonzero accessible $R_{\rm EB}$ without assuming an oscillator memory.
