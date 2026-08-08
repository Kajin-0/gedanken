# Equal-Charge Gravitational Code and the Pre-Arrival Replacer Map

**Date:** 2026-08-08  
**Status:** **PERTURBATIVE CHANNEL FORMULATION — PRE-ARRIVAL REPLACER CLAIM RESTRICTED TO THE V6 EQUAL-CHARGE CODE SUBSPACE**

## 1. Purpose

`GRAVITATIONAL_DRESSING_CAUSALITY_REFINEMENT.md` corrects the overly strong idea that gravity admits the same exact compactly localized commuting subalgebras as nongravitational local QFT.

However, the V6 protocol still needs a channel-level causal statement:

> Before the branch-dependent retarded disturbance reaches the receiver, can the locally encoded reference qubit influence the receiver output?

For the specific equal-Poincare-charge code used by V6, the answer is no to the working perturbative order.

The correct statement is a **code-subspace replacer result**, not a theorem for arbitrary gravitational inputs.

---

# 2. Encoded source subspace

Let

$$
\mathcal H_Q
$$

be the two-dimensional logical/reference input space with orthonormal basis

$$
|+\rangle_Q,
\qquad
|-\rangle_Q.
$$

Let

$$
V_{\mathcal C}:\mathcal H_Q\to\mathcal H_{\rm phys}
$$

be the physical local encoding isometry that includes

- the finite-spoke source;
- branch-common controller/work degrees of freedom;
- the chosen first-order gravitational dressing.

Define the encoded physical states

$$
\boxed{
|\Psi_\pm\rangle
=V_{\mathcal C}|\pm\rangle_Q.}
$$

The V6 branch pair is engineered so that

$$
\boxed{
\Delta P^\mu=0,
\qquad
\Delta M^{\mu\nu}=0
}
$$

to the working order.

Thus the two basis states belong to one common first-order gravitational-splitting sector labelled by the same total Poincare charges and standard asymptotic dressing.

---

# 3. Exterior-indistinguishability condition

The first-order gravitational-splitting structure implies that, for physical observables supported outside the dressed source neighborhood before the controlled radiative disturbance arrives, matrix elements on the encoded equal-charge subspace take the form

$$
\boxed{
\langle\Psi_i|O_B|\Psi_j\rangle
=c_B(O_B)\,\delta_{ij}
+O(\kappa^2),
}
$$

for

$$
i,j\in\{+,-\},
$$

where

$$
\kappa=\sqrt{32\pi G}
$$

is the perturbative gravitational coupling convention and

$$
c_B(O_B)
$$

is independent of the logical state.

Equivalently, as an operator on the logical code space,

$$
\boxed{
V_{\mathcal C}^\dagger O_BV_{\mathcal C}
=c_B(O_B)I_Q
+O(\kappa^2).}
$$

The off-diagonal matrix elements vanish for orthogonal logical basis states, while the diagonal matrix elements agree.

This is the observable-level statement needed for a replacer map.

---

# 4. Heisenberg characterization of the induced channel

Let

$$
\mathcal A_t
$$

denote the physical map from the logical source input to the accessible receiver register at a pre-arrival time

$$
t.
$$

Its Heisenberg adjoint satisfies

$$
\Tr\left[
\mathcal A_t(\rho_Q)O_B
\right]
=
\Tr\left[
\rho_Q\mathcal A_t^\dagger(O_B)
\right].
$$

The encoded exterior-indistinguishability relation gives

$$
\boxed{
\mathcal A_t^\dagger(O_B)
=c_B(O_B)I_Q
+O(\kappa^2).}
$$

A channel whose adjoint maps every receiver observable to a scalar multiple of the input identity is a replacer channel.

Therefore, on the equal-charge encoded subspace,

$$
\boxed{
\mathcal A_t(\rho_Q)
=\sigma_B(t)\,\Tr\rho_Q
+O(\kappa^2)
}
$$

before the receiver lies in the causal future of the branch-dependent intervention.

Hence, to the working perturbative order,

$$
\boxed{
\mathcal A_t\in\mathrm{EB}
}
$$

on that encoded subspace before causal arrival.

---

# 5. Reference-entangled input

Let the logical input be entangled with an untouched reference

$$
S,
$$

with arbitrary code-state density operator

$$
\rho_{SQ}.
$$

Applying the pre-arrival code-restricted map gives

$$
\boxed{
(I_S\otimes\mathcal A_t)(\rho_{SQ})
=\rho_S\otimes\sigma_B(t)
+O(\kappa^2).}
$$

Thus no entanglement initially encoded in the equal-charge logical source subspace can be transferred to the receiver before the retarded controlled signal arrives, within the stated perturbative model.

This is the properly scoped version of the earlier ``microcausal replacer'' statement.

---

# 6. Why equal charges are essential

The result fails if the logical states themselves encode different asymptotic gravitational charges.

For example, if

$$
\Delta P^0\ne0,
$$

then the two states have different total energy/mass and necessarily different long-range gravitational fields.

Likewise differences in

$$
P^i
\quad\text{or}\quad
M^{\mu\nu}
$$

can be visible through the asymptotic dressing.

Therefore V6 must not claim a pre-arrival replacer theorem for an arbitrary source alphabet.

Its input alphabet is deliberately chosen to satisfy

$$
\boxed{
\Delta P^\mu=\Delta M^{\mu\nu}=0.}
$$

The quantum information is encoded in internal/multipolar degrees of freedom rather than in distinct global charges.

---

# 7. Retarded dynamics after encoding begins

The gravitational-splitting argument fixes the common initial/asymptotic dressing structure.

The later branch-dependent dynamics are governed by the conserved difference stress tensor

$$
\Delta T^{\mu\nu}(x).
$$

The linearized controlled difference field has retarded support,

$$
\Delta\bar h_{\mu\nu}(x)
\sim
G_{\rm ret}*\Delta T_{\mu\nu},
$$

and the physical receiver responds to the resulting gauge-invariant tidal/curvature field.

Thus there are two logically distinct ingredients:

### initial localization / dressing

same-charge code states can be given the same exterior standard dressing to first order;

### later causal response

branch-dependent multipole dynamics reach the receiver only through the retarded difference field.

Together they give the pre-arrival code-restricted replacer result.

---

# 8. Relation to the bosonic link budget

After causal arrival, the source branch information is compressed into the selected radiative bosonic mode and propagated through the V6 link

$$
\boxed{
\tau_{A\to B}(t)
=\beta_{g,A}\eta_{\rm store}\beta_{g,B}\mathcal T_f(t).}
$$

Before arrival,

$$
\boxed{
\mathcal T_f(t)=0
}
$$

for the controlled retarded source waveform at the receiver.

Therefore the bosonic reduced model and the gravitationally dressed code-subspace statement agree:

$$
\boxed{
\text{pre-arrival: replacer/EB},
\qquad
\text{post-arrival: potentially non-EB if signal exceeds noise}.}
$$

The bosonic model is the radiative channel description after the gravitational dressing/charge issue has been fixed at the source level.

---

# 9. Scope and perturbative order

The notation

$$
O(\kappa^2)
$$

in this note is deliberately conservative.

The gravitational-splitting literature constructs the localization structure at first order in the perturbative gravitational coupling. The V6 radiation calculation itself is also a weak-field calculation whose observable transition probabilities/rates appear at higher powers of the coupling after squaring amplitudes.

Therefore the manuscript should avoid mixing perturbative-amplitude order and rate order casually.

Recommended wording:

> ``The equal-charge code admits a common first-order gravitational dressing, so outside observables are logical-state independent at that order before the retarded controlled response arrives. The subsequent radiative channel is then computed within the same weak-field expansion.''

Do not write a nonperturbative exact equality unless explicitly referring only to the reduced linear bosonic model.

---

# 10. Strongest safe theorem-style statement

### Perturbative equal-charge causal-code statement

Let

$$
\mathcal C
$$

be a finite-dimensional source code whose dressed basis states share the same total Poincare charges to the working order. Choose a common standard first-order gravitational dressing, and let the branch-dependent conserved stress history begin only in a compact source intervention region.

Then for receiver observables evaluated before their causal past intersects that branch-dependent history,

$$
\boxed{
V_{\mathcal C}^\dagger O_BV_{\mathcal C}
=c_B(O_B)I_{\mathcal C}
+O(\kappa^2).}
$$

Consequently the induced source-code→receiver map is a replacer, and therefore entanglement breaking, on

$$
\mathcal C
$$

to the working perturbative order before causal arrival.

This is the strongest channel-level causal statement that V6 currently needs.

---

# 11. Manuscript recommendation

The main text need not reproduce the full proof.

A compact paragraph is sufficient:

> Because gravitational dressing obstructs exact compact subsystem factorization, we restrict the source alphabet to an equal-Poincare-charge code. The two mirrored branches have the same total energy, momentum, angular momentum, and center-of-energy charges to the working order. The first-order gravitational-splitting construction then permits a common standard exterior dressing for the code states. Before the retarded branch-dependent stress history reaches the receiver, physical receiver observables are proportional to the identity on this code subspace, so the induced pre-arrival code→receiver map is input independent/replacer to the same perturbative order.

Cite Donnelly and Giddings rather than invoking ordinary local-QFT microcausality as if gravity had strictly local dressed matter operators.
