# Microcausal Replacer Theorem for the Source-Controlled Receiver Channel

**Timestamp:** 2026-08-07 18:08 EDT  
**Status:** General local-QFT causal statement; intended to justify the light-cone lower bound on the channel-capability front without excluding spacelike vacuum entanglement/harvesting.

## 1. The conceptual problem

A relativistic quantum field can possess correlations between spacelike-separated regions. Two local systems can sometimes harvest pre-existing field entanglement even though neither can signal to the other.

Therefore the statement

> “the source and receiver cannot be entangled before $R/c$”

is not generally correct.

Experiment 01 needs a narrower causal statement:

> **Before causal contact, a controllable source encoding cannot alter the receiver's local state.**

That statement is enough to prove that the source-controlled communication channel to the receiver is a replacer channel and hence entanglement breaking.

---

## 2. Local source encoding

Let $G$ denote the quantum input register whose state is locally encoded into the source/gravitational field in spacetime region $\mathcal O_A$.

Let

$$
V_A
$$

be the local encoding isometry/unitary acting on

- $G$;
- source-local degrees of freedom;
- field degrees of freedom in $\mathcal O_A$.

The rest of the field may be in an arbitrary state, including one with long-range vacuum correlations.

Let $C$ denote the accessible receiver register obtained from local receiver interactions and readout in region $\mathcal O_B$.

Suppose the complete receiver operation up to time $t$ is localized in $\mathcal O_B$.

---

## 3. Spacelike separation and microcausality

If

$$
\mathcal O_A
$$

and

$$
\mathcal O_B
$$

are spacelike separated, local observables commute:

$$
\boxed{
[O_A,O_B]=0
}
$$

for all physical local observables/operators belonging to the two regions.

In particular, the local source encoding commutes with every Heisenberg receiver observable $M_C$ supported in $\mathcal O_B$:

$$
\boxed{
[V_A,M_C]=0.
}
$$

---

## 4. Receiver expectation values are source-input independent

Let the initial total state be

$$
\rho_G\otimes\rho_{\rm rest},
$$

where $\rho_{\rm rest}$ may contain arbitrary field correlations but is initially independent of the controllable input register $G$.

After the source encoding,

$$
\rho'
=V_A
(\rho_G\otimes\rho_{\rm rest})
V_A^\dagger.
$$

For any receiver observable $M_C$,

$$
\langle M_C\rangle_{\rho'}
=
\operatorname{Tr}
\left[
V_A
(\rho_G\otimes\rho_{\rm rest})
V_A^\dagger M_C
\right].
$$

Using

$$
[V_A,M_C]=0,
$$

cyclicity of trace gives

$$
\langle M_C\rangle_{\rho'}
=
\operatorname{Tr}
\left[
(\rho_G\otimes\rho_{\rm rest})M_C
\right].
$$

Since $M_C$ acts trivially on the independent input register $G$,

$$
\boxed{
\langle M_C\rangle_{\rho'}
=
\operatorname{Tr}(\rho_{\rm rest}M_C),
}
$$

independent of $\rho_G$.

Because this holds for **every** receiver observable, the complete receiver reduced state is independent of the source input.

---

## 5. The pre-light-cone channel is a replacer

Define the source-controlled accessible channel

$$
\mathcal A_{R,t}:
\rho_G\mapsto\rho_C(t).
$$

For spacelike-separated source encoding and receiver region,

$$
\rho_C(t)
=\sigma_C(t)
$$

for every input $\rho_G$.

Hence

$$
\boxed{
\mathcal A_{R,t}(\rho_G)
=\sigma_C(t)
\operatorname{Tr}\rho_G.
}
$$

This is exactly a **replacer channel**.

Therefore

$$
\boxed{
\mathcal A_{R,t}\in\mathrm{EB}
}
$$

and

$$
\boxed{
R_{\rm EB}(\mathcal A_{R,t})=0.
}
$$

For an idealized source operation beginning at $t=0$ and receiver distance $R$,

$$
\boxed{
R_{\rm EB}(\mathcal A_{R,t})=0
\qquad t<R/c.
}
$$

---

## 6. Causal capability-front theorem

Define

$$
T_{\rm cap}(R)
=
\inf\{t:R_{\rm EB}(\mathcal A_{R,t})>0\}.
$$

The replacer result gives

$$
\boxed{
T_{\rm cap}(R)\ge R/c.
}
$$

This is the exact causal lower bound needed for Experiment 01.

It does **not** rely on Newtonian retardation inserted by hand; it follows from local commutativity/no-signalling.

---

## 7. Why vacuum entanglement does not contradict the theorem

Suppose the field state has spacelike correlations before the source operation. A remote receiver may therefore possess background correlations with field degrees of freedom near the source.

A local source operation can change

- source-local correlations;
- joint source-field correlations;
- the global entanglement structure.

But it cannot change the receiver's local reduced state outside the future light cone.

Therefore background entanglement harvesting and source-controlled communication are different operational resources.

The theorem constrains only the latter.

This is why Experiment 01 should use a **control-subtracted/source-controlled channel definition** rather than defining the causal front as the first appearance of any source-receiver entanglement whatsoever.

---

## 8. Reference-system version

Let the controllable source input $G$ be entangled with an external untouched reference $S$:

$$
\rho_{SG}.
$$

Apply the pre-light-cone replacer channel to $G$:

$$
(I_S\otimes\mathcal A_{R,t})(\rho_{SG}).
$$

Because

$$
\mathcal A_{R,t}(X)
=\operatorname{Tr}(X)\sigma_C,
$$

we obtain

$$
\boxed{
(I_S\otimes\mathcal A_{R,t})(\rho_{SG})
=ho_S\otimes\sigma_C.
}
$$

Thus **no entanglement carried by the controllable input register can reach the receiver outside the light cone**, even when the underlying field state itself is spatially entangled.

This is the clean communication-theoretic statement.

---

## 9. Application to the binary coherent branch mode

Take the source/reference state

$$
|\Psi\rangle_{SG}
=
\sqrt p|0\rangle|\alpha\rangle
+e^{i\phi}\sqrt{1-p}|1\rangle|\beta\rangle.
$$

Before causal contact,

$$
(I_S\otimes\mathcal A_{R,t})(|\Psi\rangle\langle\Psi|)
=ho_S\otimes\sigma_C.
$$

After causal contact, the receiver channel may cease to be EB.

For the phase-insensitive Gaussian receiver family, the binary coherent probe is front faithful, so the source-accessible state becomes NPT exactly when the channel leaves the EB set.

Therefore the exact Gaussian front obeys

$$
\boxed{
T_{\rm binary}^{\rm NPT}(R)
=T_{\rm cap}(R)
\ge R/c.
}
$$

---

## 10. Relation to the original retained-source Gedanken experiment

The original experiment often treats the source branch degree of freedom itself as the retained reference. In a complete local field theory, one must distinguish

1. entanglement generated from pre-existing field correlations;
2. entanglement resulting from source-controlled branch information propagating to the receiver.

The channel formulation isolates (2) by introducing a controllable branch-mode input and comparing against the corresponding control protocol.

The retained source can still be used experimentally as the reference system; the causal interpretation should be tied to the source-controlled channel rather than to the mere presence of joint entanglement.

---

## 11. Strongest conceptual statement

> **Vacuum correlations can exist across spacelike distances, but a local choice made at the source cannot modify the receiver's state outside the light cone. In channel language, the controllable source-to-receiver map is therefore a replacer channel before causal contact. Only after the future light cone arrives can that map leave the entanglement-breaking set and become capable of transporting quantum branch information.**

This is the rigorous relativistic backbone of the causal quantum-capability front.
