# Gravitational-Splitting / Equal-Charge Code Audit for V7

**Date:** 2026-08-08  
**Status:** **SPECIALIST PRIMARY-SOURCE COMPARISON — V7 CODE CONDITION MATCHES THE MATRIX-ELEMENT STRUCTURE OF FIRST-ORDER GRAVITATIONAL SPLITTING**

## 1. Question

V7 uses a two-dimensional logical source code and the operator conditions

$$
\boxed{
V_{\mathcal C}^\dagger P^\mu V_{\mathcal C}
=p^\mu I_{\mathcal C},
}
$$

$$
\boxed{
V_{\mathcal C}^\dagger M^{\mu\nu}V_{\mathcal C}
=m^{\mu\nu}I_{\mathcal C}.
}
$$

It then invokes perturbative gravitational splitting to justify a common first-order asymptotic dressing whose exterior branch dependence is absent before the retarded branch-dependent disturbance reaches the receiver.

The important specialist question is:

> Does Donnelly--Giddings require equality of **charge matrix elements on the code**, or something stronger such as every codeword being a simultaneous Poincare-charge eigenstate?

The primary source answers this directly.

---

# 2. Primary source

William Donnelly and Steven B. Giddings,
**“Gravitational splitting at first order: Quantum information localization in gravity,”**
*Physical Review D* **98**, 086006 (2018),
arXiv:1805.11095,
DOI: 10.1103/PhysRevD.98.086006.

The paper works perturbatively to leading order in the gravitational coupling and explicitly rejects ordinary exact local tensor-factor / commuting-subalgebra localization as the correct gravity framework.

Their dressed-state calculation gives, for a point $\bar x$ outside a neighborhood containing the localized matter state, a first-order exterior metric matrix element of the form

$$
\langle\hat\psi_I|h_{\mu\nu}(\bar x)|\hat\psi_J\rangle=
\widetilde h^{S\lambda}_{\mu\nu}(\bar x;y)
\langle\psi_I|P_\lambda|\psi_J\rangle
+
\frac12\partial_y^\lambda
\widetilde h^{S\sigma}_{\mu\nu}(\bar x;y)
\langle\psi_I|M_{\lambda\sigma}|\psi_J\rangle
+O(\kappa^2).
$$

Thus the first-order exterior field depends on **matrix elements** of the total Poincare charges.

They then state that a subspace on which those matrix elements have fixed values gives identical exterior metric matrix elements, and define gravitational splitting so exterior operators are insensitive to the internal state within the corresponding subspace to the retained order.

They also explicitly note that a localized state need not, and in general cannot, be a simultaneous eigenstate of all Poincare charges.

That distinction is central to the V7 audit.

---

# 3. V7 condition is the correct operator form

Let

$$
Q_A\in\{P^\mu,M^{\mu\nu}\}
$$

denote any of the ten Poincare generators.

The V7 condition

$$
V_{\mathcal C}^\dagger Q_A V_{\mathcal C}
=q_A I_{\mathcal C}
$$

means that for any logical states

$$
|\chi\rangle,
|\chi'\rangle\in\mathcal C,
$$

one has

$$
\boxed{
\langle\chi|Q_A|\chi'\rangle
=q_A\langle\chi|\chi'\rangle.
}
$$

Therefore every charge matrix element on the code is fixed by the same scalar $q_A$.

For an orthonormal code basis $|0_L\rangle,|1_L\rangle$ this gives

$$
\langle0_L|Q_A|0_L\rangle=
\langle1_L|Q_A|1_L\rangle
=q_A,
$$

and

$$
\langle0_L|Q_A|1_L\rangle=0.
$$

This is exactly the type of fixed-matrix-element condition appearing in the Donnelly--Giddings first-order exterior-field formula.

It is stronger and more appropriate than merely imposing

$$
\langle0_L|Q_A|0_L\rangle=
\langle1_L|Q_A|1_L\rangle
$$

while leaving off-diagonal matrix elements uncontrolled.

---

# 4. Why the V7 reference qubit matters

The V7 codewords are

$$
|\mathsf0\rangle
=|0\rangle_S|\Phi_+\rangle,
$$

$$
|\mathsf1\rangle
=|1\rangle_S|\Phi_-\rangle.
$$

The reference doublet is assumed degenerate and branch common in stress-energy to the retained order.

The total Poincare generators therefore do not distinguish the logical reference label directly.

The orthogonality

$$
\langle0|1\rangle_S=0
$$

kills the off-diagonal charge matrix elements once the reference contributes only a common stress-energy operator on the logical doublet.

The separate full-system charge audit then establishes equality of the two diagonal charge matrix elements across

- endpoints;
- finite spokes;
- hub;
- compact work system;
- propagating controller bus;
- graviton field already emitted during encoding;
- other linear output ports.

Hence the complete encoded system realizes the scalar-code condition rather than only an equal-classical-energy condition.

---

# 5. Common dressing does not mean zero gravitational field

Donnelly--Giddings emphasize that gravitationally dressed states with nonzero Poincare charges possess long-range fields.

V7 therefore must **not** claim that the exterior receiver region contains no gravitational field before the signal arrives.

The correct statement is

$$
\boxed{
\text{the source-controlled branch dependence is absent outside the encoded region at the retained order,}
}
$$

while a branch-common asymptotic field associated with the fixed total charges may be present.

This is exactly the distinction already used in V7:

- common gravitational dressing/background is allowed;
- the logical branch is not encoded in that first-order exterior charge field;
- the later branch-sensitive quadrupole disturbance is the retarded signal.

---

# 6. The quadrupole is not an asymptotic Poincare charge

The two V7 branches differ in their internal plus quadrupole,

$$
\Delta Q_{xx}=-\Delta Q_{yy}\ne0,
$$

while their ten Poincare generators agree on the code.

The Donnelly--Giddings first-order splitting therefore does not require the quadrupole difference to vanish.

Instead, internal information beyond the fixed Poincare charges can be localized inside the chosen neighborhood at the initial stage.

When the source is later driven dynamically, that quadrupole can generate genuine outgoing gravitational radiation.

Thus there is no contradiction between

1. common first-order charge dressing before causal escape; and
2. later branch-dependent radiative multipole information.

---

# 7. Temporal scope is essential

The gravitational-splitting construction is not a theorem that branch information remains permanently inaccessible outside the source region under subsequent dynamics.

For V7 the appropriate sequence is

$$
\boxed{
\text{equal-charge dressed initial/local code}
\rightarrow
\text{local source evolution}
\rightarrow
\text{retarded branch-dependent radiation}
\rightarrow
\text{receiver}.
}
$$

Before the causal future of the branch-dependent source operation intersects the receiver, the code-dependent exterior response is absent at the retained order.

Once the radiative disturbance arrives, the receiver is **supposed** to become branch dependent.

Therefore the Donnelly--Giddings result is used only to control the initial/asymptotic dressing loophole, not to suppress the later physical signal.

---

# 8. Encoder precursor radiation

V7 permits real gravitational precursor radiation during the local encoder.

Once a branch-dependent radiation mode has physically propagated outside the chosen source neighborhood, that mode is no longer merely hidden internal information under the splitting construction.

This is not a problem.

The precursor is explicitly retained in the complete source waveform $f(t)$ and contributes to the receiver whenever its light cone reaches the receiver.

Accordingly, the strongest safe causal wording is:

> Before the receiver's causal past intersects any branch-dependent source/controller/radiation history, exterior receiver observables are branch independent to the retained first-order splitting/linearized-gravity order. Branch-dependent precursor or tail radiation becomes a genuine signal only after causal arrival.

This is more precise than saying simply “before handoff the receiver channel is a replacer.”

---

# 9. Existence versus dynamical preparation of the dressing

The Donnelly--Giddings construction establishes that one can choose standard perturbative dressings such that exterior field matrix elements depend only on the fixed Poincare-charge matrix elements.

It does **not** automatically prove that an arbitrary microscopic encoder dynamically produces exactly that standard dressing from an arbitrary bare-state convention.

V7 should therefore formulate the code as an **initial dressed code choice**:

$$
\boxed{
\text{choose the logical source states with a common first-order standard asymptotic dressing,}
}
$$

then apply the local physical encoder/controller dynamics within that dressed sector.

This is the natural perturbative interpretation of the present manuscript and avoids claiming that the controller itself dynamically manufactures the asymptotic dressing from nothing.

---

# 10. Higher-order limitation

The Donnelly--Giddings result used here is explicitly first order in the gravitational coupling.

The exterior metric formula carries corrections

$$
O(\kappa^2),
$$

and higher-point gravitational observables require higher-order analysis.

Therefore V7's safe statement is

$$
\boxed{
\text{common asymptotic dressing / exterior branch independence at first perturbative order on the equal-charge code.}
}
$$

It must not be promoted to

- exact nonperturbative locality;
- exact tensor factorization;
- all-orders equality of exterior observables.

The current manuscript already contains these restrictions.

---

# 11. Comparison table

| Donnelly--Giddings ingredient | V7 implementation | Verdict |
|---|---|---|
| perturbative gravitational dressing | weak linearized-gravity source code | aligned |
| exterior field depends on Poincare charge **matrix elements** | $V_C^\dagger Q_A V_C=q_AI_C$ | exact structural match at retained order |
| no need for simultaneous charge eigenstates | coherent mechanical/controller code allowed | aligned |
| fixed charge sector/subspace | equal-charge logical doublet | aligned |
| long-range common dressing allowed | branch-common asymptotic field allowed | aligned |
| internal information may differ beyond charges | branch quadrupole differs | aligned |
| localization only perturbative | V7 explicitly first-order/code-restricted | aligned |
| later dynamics may radiate information | V7 signal is retarded quadrupole radiation | aligned |

---

# 12. Referee-level verdict

No structural mismatch was found between the V7 equal-charge code condition and the primary Donnelly--Giddings first-order gravitational-splitting construction.

The strongest mathematical point is

$$
\boxed{
V_{\mathcal C}^\dagger Q_A V_{\mathcal C}
=q_A I_{\mathcal C}
\Longrightarrow
\langle\chi|Q_A|\chi'\rangle
=q_A\langle\chi|\chi'\rangle,
}
$$

which is precisely the fixed charge-matrix-element structure that controls their first-order exterior metric matrix elements.

The remaining qualifications are conceptual rather than unresolved algebraic loopholes:

1. the dressing is chosen as part of the initial perturbative code definition;
2. the result is first order in the gravitational coupling;
3. common long-range charge fields may remain;
4. later retarded branch-dependent radiation is not hidden and is the intended signal;
5. a nonperturbative quantum-gravity subsystem theorem is not claimed.

Within those restrictions, the V7 gravitational-splitting use should be regarded as **consistent with the cited primary result**.
