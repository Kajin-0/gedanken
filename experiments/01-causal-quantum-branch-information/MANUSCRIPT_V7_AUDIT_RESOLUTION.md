# Manuscript V7 — Audit Resolution

**Date:** 2026-08-08  
**Status:** **THEORY GATES CLOSED AT CURRENT WORKING ORDER — PROCEED TO VISUAL/EDITORIAL/SUBMISSION POLISH**

This note closes the medium-risk items identified in `MANUSCRIPT_V7_REFEREE_AUDIT.md`.

---

## 1. Passive quadrupole EWSR provenance — RESOLVED

The manuscript now explicitly credits the established energy-weighted-sum-rule / double-commutator machinery:

- Lu and Johnson, *Phys. Rev. C* **97**, 034330 (2018), including E2 sum-rule applications;
- Hinohara, *Phys. Rev. C* **100**, 024310 (2019), coordinate-multipole EWSRs.

It also cites prior graviton-absorption limitations:

- Boughn and Rothman (2006);
- Palessandro and Sloth (2020).

The manuscript no longer presents the EWSR method as new.

The retained candidate corollary is the gravity-specific passive-response bound

$$
\frac{\kappa_g}{\omega}
\lesssim
\frac23\mathcal C\beta^3,
$$

obtained by combining the passive mass-quadrupole spectral-weight budget with the graviton transition rate.

Targeted literature search did not find this exact branching-bound formulation, but absence from the search is not treated as proof of novelty.

Status:

$$
\boxed{\text{resolved for manuscript scope}}
$$

---

## 2. Equal-Poincare-charge dressing condition — RESOLVED

A full-system audit was added:

`EQUAL_POINCARE_CHARGE_AUDIT_V7.md`

The audited system includes

- reference doublet;
- endpoints;
- elastic spokes;
- hub;
- compact work system;
- propagating controller field;
- elastic--controller interaction;
- graviton field;
- all other linear output ports.

The manuscript now uses the stronger code-subspace statement

$$
\boxed{
V_{\mathcal C}^\dagger P^\mu V_{\mathcal C}
=p^\mu I_{\mathcal C},
}
$$

$$
\boxed{
V_{\mathcal C}^\dagger M^{\mu\nu}V_{\mathcal C}
=m^{\mu\nu}I_{\mathcal C}
}
$$

at the retained order, not merely equality of classical expectation values.

This is the condition used to motivate a common first-order asymptotic gravitational dressing, consistent with the scoped Donnelly--Giddings gravitational-splitting result.

No exact nonperturbative locality claim is made.

Status:

$$
\boxed{\text{resolved at first perturbative / working-model order}}
$$

---

## 3. Encoder precursor / handoff timing — RESOLVED

The paper now distinguishes

1. causal intervention start $t_s$;
2. encoder interval;
3. physical controller-clear handoff;
4. post-handoff fixed virtual bosonic channel.

Encoder precursor radiation is retained in the complete gravitational waveform.

At small separation, the receiver may respond to precursor radiation before handoff. That early interval is treated as a direct qubit-to-multimode controlled-state problem, not incorrectly labeled a fixed-input one-mode channel.

After handoff, the global branch-distance norm is fixed and the virtual difference-mode reduction applies to all branch-carrying coherent modes, including precursor modes already emitted or in flight.

Status:

$$
\boxed{\text{resolved}}
$$

---

## 4. Locality of the distributed encoder — RESOLVED

The initial distributed eigenstrain shorthand could be misread as placing the hub operator $\sigma_z$ at every spoke point.

This has been replaced by a literal local controller-field completion:

`LOCAL_CONTROLLER_FIELD_COMPLETION_V7.md`

Introduce a controller bus field $\Phi_a(x,t)$ with propagation speed

$$
v_c\le c.
$$

The qubit/work system couples to the controller field only at the hub.

Each spoke couples only to its local controller field:

$$
\boxed{
\mathcal E_a(x,t)
=\frac12EA
\left[
\partial_x\xi_a
-\epsilon_a\lambda\chi(x)\Phi_a(x,t)
\right]^2.
}
$$

The branch-conditioned retarded solution is

$$
\Phi_a^{(s)}(x,t)
=sX_C(t-x/v_c).
$$

Projection onto the elastic plus mode gives the causal control form factor

$$
\boxed{
F_c(\omega)
=\int_0^Ldx\,w(x)e^{i\omega x/v_c}.
}
$$

For

$$
q_c=\omega L/v_c\ll1,
$$

$$
\boxed{
|F_c|^2
=1-q_c^2\operatorname{Var}_w(x/L)
+O(q_c^4),
}
$$

while the leading phase is a propagation delay.

For uniform overlap,

$$
F_c=e^{iq_c/2}\operatorname{sinc}(q_c/2),
$$

$$
|F_c|^2
=1-q_c^2/12+O(q_c^4).
$$

A physical cleared handoff has

$$
T_*^{\rm local}
=T_*^{\rm modal}+O(L/v_c).
$$

The modal sign-controlled beam-splitter Hamiltonian is therefore explicitly a low-frequency normal-mode reduction of a local causal controller, not an instantaneous distributed operation.

If controller excitations are not coherently cleared, they become explicit source loss/dephasing channels.

Status:

$$
\boxed{\text{resolved in the controlled }q_c\ll1\text{ regime}}
$$

---

## 5. Serial link factorization — RESOLVED / INDEPENDENTLY CHECKED

The central post-handoff coherent link remains

$$
\boxed{
\tau_c(t)
=\beta_{g,A}
\eta_{\rm store}(R)
\beta_{g,B}
\mathcal T_f(t).
}
$$

It has been checked independently through

1. gravitational Green-function/input-output normalization;
2. reciprocal critical-coupling/Friis interpretation of propagation;
3. explicit cascaded bosonic network factorization.

No double counting has been found.

The local-controller completion changes the physical source waveform, handoff, and possibly source port structure, but it does not introduce a new serial gravitational propagation factor.

Status:

$$
\boxed{\text{resolved at the retained linear narrowband order}}
$$

---

## 6. Memory versus accessible readout — RESOLVED

The manuscript explicitly distinguishes

$$
\Delta_{\rm mem}=\tau_c-m_c
$$

from accessible readout:

$$
\boxed{
\Delta_{\rm acc}
=\tau_r\Delta_{\rm mem}-m_r.
}
$$

Thus the paper no longer equates strong absorption or a non-EB memory with an accessible quantum receiver.

Status:

$$
\boxed{\text{resolved}}
$$

---

## 7. Quantitative entanglement strength — RESOLVED

For vacuum pure loss the exact reference--receiver negativity is included, with weak-link optimum

$$
\boxed{
\mathcal N_{\max}(\eta)
=\eta
-2\eta^{3/2}
+\frac{13}{3}\eta^2
+O(\eta^{5/2}).
}
$$

This was independently numerically checked down to

$$
\eta=10^{-6}.
$$

The ordinary/ordinary benchmark therefore has deliverable entanglement of the same asymptotic order as its

$$
O(10^{-42})
$$
coherent link.

Status:

$$
\boxed{\text{resolved}}
$$

---

## 8. Current manuscript status

Current manuscript:

`manuscript_v7/`

It is modular, has automated LaTeX CI, and includes

- source geometry figure;
- serial link-budget figure;
- charge-audit appendix;
- EWSR derivation appendix;
- exact pure-loss PT appendix;
- passive broadening appendix.

A pre-local-controller-field modular version successfully compiled in GitHub CI with no unresolved references/citations. The locality-complete version is being compiled through the same workflow.

---

# 9. Remaining work category

No known unresolved structural theory objection remains within the stated approximation class.

The remaining work is now

1. rendered-PDF visual QA;
2. editorial compression;
3. journal-format decision;
4. final bibliography metadata check;
5. optional supplementary-material split;
6. final adversarial external-style referee read.

New theoretical branches should be opened only if one of those reviews identifies a concrete gap.
