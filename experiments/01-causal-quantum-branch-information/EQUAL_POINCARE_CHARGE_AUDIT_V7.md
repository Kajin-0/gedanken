# Equal-Poincare-Charge Audit for the V7 Gravitational Code

**Date:** 2026-08-08  
**Status:** **FULL-SYSTEM FIRST-ORDER CHARGE AUDIT — REFERENCE + MECHANICS + CONTROLLER + RADIATION + LOSS PORTS**

## 1. Question

The V7 manuscript uses the perturbative gravitational-splitting idea that internal information can be hidden from exterior first-order gravitational observables when the code states have the same total Poincare charges.

The required statement is stronger than

$$
\langle Q\rangle_+=\langle Q\rangle_-.
$$

For a two-dimensional code with encoding isometry

$$
V_{\mathcal C}|0\rangle
=|0\rangle_S|\Phi_+\rangle,
$$

$$
V_{\mathcal C}|1\rangle
=|1\rangle_S|\Phi_-\rangle,
$$

the useful first-order condition is

$$
\boxed{
V_{\mathcal C}^\dagger Q_A V_{\mathcal C}
=q_A I_{\mathcal C}
}
$$

for each total Poincare generator $Q_A$.

This note audits that condition for the explicit V7 source architecture to the same linear-elastic / linearized-gravity order as the rest of the calculation.

---

# 2. Charge conventions

Use

$$
P^0
=\frac1c\int d^3x\,T^{00},
$$

$$
P^i
=\frac1c\int d^3x\,T^{0i},
$$

$$
J^{ij}
=\frac1c\int d^3x\,
\left(x^iT^{0j}-x^jT^{0i}\right).
$$

Instead of fixing a sign convention for the boost generators, define the center-of-energy first moment

$$
\boxed{
D^i
=\frac1{c^2}\int d^3x\,x^iT^{00}.
}
$$

At fixed total momentum, equality of $D^i$ is equivalent to equality of the boost charges $M^{0i}$ up to the conventional overall sign/time term.

Thus it is sufficient to audit

$$
P^0,
\qquad
P^i,
\qquad
J^{ij},
\qquad
D^i.
$$

---

# 3. Codewords and the off-diagonal matrix elements

The full branch codewords have the form

$$
|\mathsf 0\rangle
=|0\rangle_S|\Phi_+\rangle,
$$

$$
|\mathsf 1\rangle
=|1\rangle_S|\Phi_-\rangle,
$$

where

- $S$ is the degenerate reference qubit;
- $|\Phi_\pm\rangle$ contains the endpoint masses, spokes, hub, work/controller, gravitational field, and all other linear output ports.

By design, the reference stress-energy is proportional to the identity on the logical doublet to the working accuracy:

$$
T_S^{\mu\nu}ig|_{\mathcal C}
\propto I_S.
$$

The remaining Poincare generators act trivially on the reference label. Therefore for every total charge $Q_A$,

$$
\langle\mathsf 0|Q_A|\mathsf 1\rangle
\propto
\langle0|1\rangle_S
=0.
$$

Hence the only nontrivial part of the code condition is equality of the two diagonal charge matrix elements:

$$
\langle\mathsf 0|Q_A|\mathsf 0\rangle
=
\langle\mathsf 1|Q_A|\mathsf 1\rangle.
$$

This is important: the bosonic branch states need not be exact energy eigenstates. Orthogonality of the degenerate reference label kills the off-diagonal code matrix elements, while the branch symmetry below makes the diagonal elements equal.

---

# 4. Reference qubit

Assumptions already built into V7:

1. the logical doublet is degenerate;
2. the two internal states have the same local stress-energy to the working order;
3. the reference is localized in the compact central hub;
4. no branch-dependent spin/angular-momentum label is used.

Therefore

$$
\Delta P_S^0=0,
$$

$$
\Delta\mathbf P_S=0,
$$

$$
\Delta\mathbf J_S=0,
$$

$$
\Delta\mathbf D_S=0.
$$

---

# 5. Endpoint masses

For branch $s=\pm1$, use the plus deformation

$$
X_s=L+s u,
$$

$$
Y_s=L-su.
$$

Each axis contains a pair at opposite positions. The corresponding velocities also occur in opposite pairs.

## 5.1 Energy

Endpoint rest energy is trivially branch common.

Kinetic energy is quadratic in the velocities:

$$
K_{\rm end}
=\sum_a\frac12\mu v_a^2,
$$

so the branch sign flip leaves it unchanged.

The two branch geometries are also related by a $\pi/2$ rotation of the symmetric four-spoke apparatus. Any rotationally invariant internal/Newtonian self-energy is therefore equal between the two branches to the working order.

Thus

$$
\boxed{\Delta P^0_{\rm end}=0.}
$$

## 5.2 Linear momentum

For every endpoint at $+\mathbf r$ with momentum $+\mathbf p$ along its spoke there is an opposite endpoint at $-\mathbf r$ with momentum $-\mathbf p$.

Hence at every time

$$
\boxed{\mathbf P_{\rm end}=0}
$$

in both branches.

## 5.3 Angular momentum

The endpoint motion is radial:

$$
\mathbf p_a\parallel\mathbf r_a.
$$

Therefore

$$
\mathbf r_a\times\mathbf p_a=0
$$

for each endpoint separately, and

$$
\boxed{\mathbf J_{\rm end}=0}
$$

in both branches.

## 5.4 Center of energy

Opposite endpoint pairs have equal energy and opposite position, so their energy first moments cancel pairwise:

$$
\boxed{\mathbf D_{\rm end}=0}
$$

in both branches.

---

# 6. Elastic spokes

For one spoke let

$$
\xi^{(s)}_a(x,t)
=\epsilon_a s\,u(t) f_q(x),
$$

where

$$
\epsilon_a=+1
$$

for the $x$ spokes and

$$
\epsilon_a=-1
$$

for the $y$ spokes.

The finite-spoke eigenmode satisfies

$$
\frac{m_r}{\mu}=q\tan q.
$$

## 6.1 Energy

The spoke kinetic energy density is quadratic in

$$
\dot\xi_a^{(s)},
$$

and the ordinary elastic strain energy density is quadratic in

$$
\partial_x\xi_a^{(s)}.
$$

Both are invariant under

$$
s\to-s.
$$

Thus the spoke contribution to total energy is branch common.

## 6.2 Momentum

Longitudinal momentum densities on opposite spokes have equal magnitude and opposite vector direction.

Therefore their integrated momenta cancel pairwise:

$$
\boxed{\mathbf P_{\rm spokes}=0}
$$

in both branches.

## 6.3 Angular momentum

Each spoke's motion is collinear with its radial coordinate. Therefore

$$
\mathbf r\times\mathbf p=0
$$

pointwise in the ideal longitudinal model, so

$$
\boxed{\mathbf J_{\rm spokes}=0.}
$$

## 6.4 Center of energy

The $+x$ and $-x$ spokes have identical energy density profiles at opposite positions, as do the $+y$ and $-y$ spokes. Hence

$$
\boxed{\mathbf D_{\rm spokes}=0}
$$

in both branches.

The finite $q$ correction changes the radial weighting of the mass and strain but does not alter any of these parity statements.

---

# 7. Hub

The compact hub remains at the origin by pair symmetry.

Opposite spokes exert equal and opposite forces and zero net torque in the plus mode.

The hub is assumed to remain in the same internal state in both branches to the working order.

Therefore

$$
\boxed{
\Delta P^0_{\rm hub}
=\Delta\mathbf P_{\rm hub}
=\Delta\mathbf J_{\rm hub}
=\Delta\mathbf D_{\rm hub}
=0.}
$$

---

# 8. Work/controller and eigenstrain interaction

The modal encoder is

$$
H_{\rm enc}
=\hbar g\sigma_z(a^\dagger w+a w^\dagger).
$$

The work-mode coherent amplitude is branch common:

$$
\gamma_w(t)
=\zeta e^{-\kappa_A t/4}
\left[
\cos(\Omega t)
+\frac{\kappa_A}{4\Omega}\sin(\Omega t)
\right].
$$

Thus the work-mode free energy, proportional to

$$
|\gamma_w(t)|^2,
$$

is identical in the two branches.

The distributed elastic implementation uses

$$
\boxed{
\mathcal E_a
=\frac12EA
\left[
\partial_x\xi_a
-\epsilon_a\sigma_z\lambda X_C\chi(x)
\right]^2.
}
$$

For branch $s$,

$$
\xi_a^{(s)}
=\epsilon_a s u f_q,
$$

so

$$
\partial_x\xi_a^{(s)}
-\epsilon_a s\lambda X_C\chi
=
\epsilon_a s
\left[u f_q'-\lambda X_C\chi\right].
$$

Therefore

$$
\boxed{
\mathcal E_a^{(+)}(x)
=\mathcal E_a^{(-)}(x)
}
$$

pointwise:

$$
[\epsilon_a s u f_q'-\epsilon_a s\lambda X_C\chi]^2
=
[u f_q'-\lambda X_C\chi]^2.
$$

The interaction energy is therefore branch common, not merely equal after spatial integration.

The actuator is taken compactly at the hub, with no branch-dependent translational momentum or internal angular momentum.

The mirrored four-spoke actuation has zero net force and torque.

Hence

$$
\boxed{
\Delta P^0_{\rm ctrl}
=\Delta\mathbf P_{\rm ctrl}
=\Delta\mathbf J_{\rm ctrl}
=\Delta\mathbf D_{\rm ctrl}
=0
}
$$

to the working encoder order.

---

# 9. Gravitational radiation already emitted during the encoder

This contribution is essential because the charge audit must cover the full encoded system, not only the matter remaining near the source.

In the linearized free graviton field, after removing any branch-common displacement, the two conditional coherent amplitudes are related by

$$
\alpha_{\mathbf k\lambda}^{(-)}
=-\alpha_{\mathbf k\lambda}^{(+)}.
$$

Equivalently, the branch transformation is field parity on the branch-carrying graviton modes:

$$
a_{\mathbf k\lambda}	o-a_{\mathbf k\lambda}.
$$

Free-field Poincare generators are quadratic in the field variables, or equivalently bilinear in creation/annihilation operators. Therefore they are invariant under this global sign reversal.

For example, the energy and momentum distributions depend on

$$
|\alpha_{\mathbf k\lambda}|^2,
$$

which are exactly branch common.

Thus

$$
\Delta P_g^0=0,
$$

$$
\Delta\mathbf P_g=0.
$$

Angular momentum and the center-of-energy/boost charges are likewise quadratic free-field generators and are invariant under the common sign reversal of the branch-dependent coherent amplitude vector.

Therefore

$$
\boxed{
\Delta J_g^{ij}=0,
\qquad
\Delta D_g^i=0.
}
$$

The individual field charges need not vanish for a generic directional pulse. The required statement is only that they are **the same in both branches**.

For the symmetric plus-quadrupole source the integrated linear momentum is additionally expected to vanish by angular symmetry, but that stronger statement is not needed for the code argument.

---

# 10. Other linear output ports

The same argument applies to every branch-carrying linear loss port.

Conditional bath coherent amplitudes have the form

$$
\alpha_{j,-}(t)
=-\alpha_{j,+}(t)
$$

after common displacements are removed.

Free bath energy, momentum, angular momentum, and center-of-energy generators are quadratic.

Hence

$$
\boxed{
\Delta P^\mu_{\rm baths}=0,
\qquad
\Delta M^{\mu\nu}_{\rm baths}=0.
}
$$

This remains true even though those baths can carry a large which-branch record: **which-branch distinguishability does not require different total Poincare charges.**

That distinction is important.

---

# 11. Interaction/recoil bookkeeping

The full isolated source-plus-field system conserves total Poincare charges to the working order.

The encoder interaction is branch even because the source coordinate and $\sigma_z$ change sign together.

The distributed eigenstrain energy is pointwise branch common as shown above.

Radiation recoil is also branch common because the radiation momentum distribution is invariant under the coherent-amplitude sign reversal.

Thus no hidden branch-odd recoil charge is required to restore total momentum conservation.

---

# 12. Full-system charge table

| subsystem | $P^0$ branch difference | $\mathbf P$ branch difference | $\mathbf J$ branch difference | $\mathbf D$ branch difference | reason |
|---|---:|---:|---:|---:|---|
| reference qubit | 0 | 0 | 0 | 0 | degenerate, branch-common stress-energy |
| endpoint pairs | 0 | 0 | 0 | 0 | energy quadratic; inversion pairs; radial motion |
| elastic spokes | 0 | 0 | 0 | 0 | strain/kinetic energy even; opposite-spoke cancellation |
| hub | 0 | 0 | 0 | 0 | central, zero net force/torque, common state |
| work/controller | 0 | 0 | 0 | 0 | common work state; eigenstrain energy pointwise branch common |
| graviton field | 0 | 0 | 0 | 0 | free charges quadratic under $\alpha\to-\alpha$ |
| other linear ports | 0 | 0 | 0 | 0 | same quadratic sign invariance |
| full encoded system | **0** | **0** | **0** | **0** | sum + branch-even interactions |

Therefore

$$
\boxed{
\Delta P^\mu=0,
\qquad
\Delta M^{\mu\nu}=0
}
$$

to the working order.

---

# 13. Stronger code-subspace statement

Because the reference labels are orthogonal and branch independent in stress-energy,

$$
\langle\mathsf0|Q_A|\mathsf1\rangle=0.
$$

Because the diagonal charges are equal,

$$
\langle\mathsf0|Q_A|\mathsf0\rangle
=
\langle\mathsf1|Q_A|\mathsf1\rangle
=q_A.
$$

Hence

$$
\boxed{
V_{\mathcal C}^\dagger Q_A V_{\mathcal C}
=q_A I_{\mathcal C}
}
$$

for every Poincare generator at the audited order.

This is the form that should be quoted in the gravitational-dressing discussion.

It is more precise than saying only that the two classical branches have the same energy or momentum expectation.

---

# 14. Scope and limitations

The audit is exact only within the sign-reversal and spatial symmetries of the working linear model.

Potential violations include

1. branch-dependent fabrication or environmental asymmetry;
2. a reference doublet with measurably different stress-energy or spin;
3. branch-dependent controller nonlinearities;
4. asymmetric radiation reaction beyond the one-mode/linearized treatment;
5. gravitational self-interaction beyond the retained perturbative order;
6. a microscopic material completion that breaks the assumed mirrored eigenstrain symmetry.

The Donnelly--Giddings gravitational-splitting argument used by V7 is itself first-order perturbative gravity. Therefore this audit justifies

$$
\boxed{
\text{common first-order asymptotic dressing on the encoded code subspace,}
}
$$

not exact nonperturbative gravitational locality.

---

# 15. Referee-level conclusion

The equal-charge assumption in V7 can be upgraded from a prose symmetry claim to the explicit code statement

$$
\boxed{
V_{\mathcal C}^\dagger P^\mu V_{\mathcal C}
=p^\mu I_{\mathcal C},
}

$$
\boxed{
V_{\mathcal C}^\dagger M^{\mu\nu} V_{\mathcal C}
=m^{\mu\nu} I_{\mathcal C},
}

at the working order.

The most important point is that the audit includes **radiation already emitted during local encoding** and all other linear output ports. Equal Poincare charges therefore apply to the full encoded state, not merely to the residual mechanical source.
