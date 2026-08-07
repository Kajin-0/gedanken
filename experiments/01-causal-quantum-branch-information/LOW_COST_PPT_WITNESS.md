# Low-Cost PPT Witness at the Thermal Boundary

**Timestamp:** 2026-08-07 15:31 EDT  
**Status:** Active derivation for Experiment 01

This note closes the gap, in the weak-source-cat limit, between the true thermal entanglement boundary and the stronger but less sensitive fidelity-history witness.

---

## 1. Starting point

For a weak wave-zone source cat,

$$
|\Psi\rangle
=|+\rangle|0\rangle+a|-\rangle|1\rangle+O(a^2),
$$

with

$$
|+\rangle=\frac{|L\rangle+|R\rangle}{\sqrt2},
\qquad
|-\rangle=\frac{|L\rangle-|R\rangle}{\sqrt2}.
$$

After a thermal attenuator, the partially transposed source-receiver state contains independent $2\times2$ principal blocks.

The $k=0$ block uses the basis

$$
\{|+,1\rangle,|-,0\rangle\}.
$$

Its entries can be measured directly from the original, non-transposed state.

---

## 2. Three measured quantities

Define

$$
P_{+,1}=\langle +,1|\rho|+,1\rangle,
$$

$$
P_{-,0}=\langle -,0|\rho|-,0\rangle,
$$

and the joint source-receiver coherence

$$
Z_0=\langle -,1|\rho|+,0\rangle.
$$

After partial transpose on the source, the relevant principal block is

$$
M_0=
\begin{pmatrix}
P_{+,1}&Z_0^*\\
Z_0&P_{-,0}
\end{pmatrix}.
$$

Every separable state is PPT, so every principal minor of $\rho^{T_A}$ must be positive semidefinite. Therefore separability requires

$$
\boxed{
|Z_0|^2\le P_{+,1}P_{-,0}.
}
$$

Hence

$$
\boxed{
|Z_0|^2>P_{+,1}P_{-,0}
}
$$

certifies source-receiver entanglement.

This is simply a targeted NPT witness; the matrix-positivity principle is standard and is not itself a novelty claim.

---

## 3. Observable implementation

The complex coherence $Z_0$ can be obtained from two Hermitian observables,

$$
X_0
=|-,1\rangle\langle+,0|
+|+,0\rangle\langle-,1|,
$$

$$
Y_0
=-i|-,1\rangle\langle+,0|
+i|+,0\rangle\langle-,1|.
$$

Then

$$
\langle X_0\rangle=2\operatorname{Re}Z_0,
$$

$$
\langle Y_0\rangle=2\operatorname{Im}Z_0,
$$

so

$$
\boxed{
|Z_0|^2
=\frac14
\left(
\langle X_0\rangle^2+
\langle Y_0\rangle^2
\right).
}
$$

Thus the nonlinear witness needs only

1. the population $P_{+,1}$;
2. the population $P_{-,0}$;
3. two quadratures of one joint coherence.

No full receiver tomography is required.

---

## 4. Equivalent linear witness family

For any $\lambda>0$ and phase $\theta$, positivity of $M_0$ implies

$$
\boxed{
W_{0}(\lambda,\theta)
=
\lambda P_{+,1}
+\lambda^{-1}P_{-,0}
-2\operatorname{Re}(e^{-i\theta}Z_0)
\ge0.
}
$$

A negative value certifies NPT entanglement.

Optimizing over

$$
\theta=\arg Z_0
$$

and

$$
\lambda=\sqrt{P_{-,0}/P_{+,1}}
$$

reduces the condition to

$$
2\sqrt{P_{+,1}P_{-,0}}-2|Z_0|<0,
$$

which is equivalent to the principal-minor criterion.

This gives a conventional linear entanglement-witness family if one prefers a single expectation-value bound.

---

## 5. Thermal attenuator values

Define

$$
m=(1-\eta)\bar n,
\qquad
G=1+m.
$$

For the weak source cat,

$$
P_{+,1}
=\frac{m}{G^2}+O(|a|^2),
$$

$$
P_{-,0}
=|a|^2\frac{G-\eta}{G^2}+O(|a|^4),
$$

and

$$
Z_0
=a\frac{\sqrt\eta}{G^2}+O(|a|^3).
$$

Therefore

$$
|Z_0|^2-P_{+,1}P_{-,0}
=
\frac{|a|^2}{G^4}
\left[
\eta-m(G-\eta)
\right]
+O(|a|^4).
$$

The bracket factors as

$$
\eta-m(G-\eta)
=
[\eta(\bar n+1)-\bar n]
[\bar n+1-\eta\bar n].
$$

Thus the low-cost PPT witness turns on exactly when

$$
\boxed{
\eta>\frac{\bar n}{\bar n+1}.
}
$$

This is the thermal attenuator's exact entanglement-breaking boundary.

---

## 6. Why this is important for the Gedanken experiment

The earlier fidelity-history witness requires

$$
\eta>
\frac{2\bar n+1}{2\bar n+2}.
$$

The targeted $0/1$-sector PPT witness instead reaches

$$
\eta>
\frac{\bar n}{\bar n+1}
$$

in the weak-cat limit.

So the previous gap was not a fundamental inability to certify the transferred entanglement; it was a consequence of choosing a particularly simple global history-coherence witness.

The price of reaching the true boundary is measurement specificity: one must resolve the receiver's lowest Fock sectors and one source-receiver coherence rather than measuring only global history fidelity/distinguishability.

---

## 7. Matched-memory form

Using

$$
\eta=\frac{\kappa_g}{\kappa_g+\kappa_i},
$$

the weak-cat PPT witness can certify entanglement whenever

$$
\boxed{
\kappa_g>\bar n_i\kappa_i.
}
$$

This is the same as the fundamental thermal entanglement-transfer condition.

Thus, at least in the weak-cat Gaussian channel limit, the thermal boundary is operationally accessible without full tomography.

---

## 8. Causal interpretation

Before the gravitational difference mode arrives,

$$
Z_0=0
$$

for the source-controlled contribution and the receiver cannot violate the witness.

After causal arrival, coherent capture builds $Z_0$ while thermal occupation contributes the competing populations $P_{+,1}$ and $P_{-,0}$.

The first spacetime point where

$$
|Z_0|^2>P_{+,1}P_{-,0}
$$

therefore defines a **causal NPT front** for this weak-wavepacket experiment.

This is sharper than simply measuring when a classical gravitational-wave signal arrives.

---

## 9. Novelty discipline

The use of a negative principal minor of a partial transpose as an entanglement witness is standard. The thermal attenuator's entanglement-breaking boundary is also established.

The potentially distinctive element is the **causal gravitational implementation**:

$$
\text{spatial source cat}
\to
\text{retarded graviton difference mode}
\to
\text{matched quantum receiver}
$$

with a minimal Fock-sector witness whose onset tracks the arrival of gravitationally transported entanglement.

No novelty claim should be made until this exact protocol is checked against current gravity-mediated communication and graviton-detection literature.

---

## 10. Immediate next step

The next theoretical task is to derive the **time-dependent** $P_{+,1}(T)$, $P_{-,0}(T)$, and $Z_0(T)$ for a finite gravitational wavepacket and matched receiver. That will give an explicit formula for the causal NPT-onset time

$$
T_{\rm NPT}(R)
$$

including both light-travel delay and thermal capture dynamics.