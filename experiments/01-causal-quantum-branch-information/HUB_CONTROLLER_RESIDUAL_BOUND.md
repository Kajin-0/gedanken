# Finite Hub / Controller Residual Bound

**Date:** 2026-08-07  
**Status:** **SOURCE ERROR-BUDGET RESULT — IDEAL CONTROLLER CONTRIBUTION VANISHES; IMPERFECTIONS ADMIT A COMPACT-SUPPORT QUADRUPOLE BOUND**

## 1. Remaining source question

`CONSERVED_SOURCE_ACTUATOR_AUDIT.md` closes the leading actuator loophole for an explicit four-spoke elastic source:

- endpoint forces are supplied internally;
- spoke rest mass is included;
- total stress-energy is conserved;
- the support contribution reinforces rather than cancels the plus quadrupole;
- an autonomous controlled-parity Hamiltonian allows the work reservoir to remain branch common.

The remaining source-level question is the finite central hub/control region.

Could a compact controller carry enough branch-dependent energy density to modify or cancel the desired source quadrupole?

This note gives a direct bound.

---

## 2. Total quadrupole is the correct object

For the complete isolated source define

$$
I_{ij}
=\frac1{c^2}
\int d^3x\,T^{00}_{\rm tot}x_ix_j.
$$

The STF quadrupole is

$$
\boxed{
Q_{ij}
=\frac1{c^2}
\int d^3x\,T^{00}_{\rm tot}
\left(x_ix_j-\frac13\delta_{ij}r^2\right).
}
$$

For a conserved compact source,

$$
\ddot I_{ij}
=2\int T^{ij}_{\rm tot}d^3x.
$$

Therefore the far-zone leading quadrupole can be audited directly from the total branch difference

$$
\Delta T^{00}_{\rm tot}.
$$

A stress contribution cannot secretly cancel the radiation without producing the corresponding effect in the total energy quadrupole.

---

## 3. Ideal controlled-parity controller

Use the autonomous Hamiltonian

$$
H
=H_m(u,p_u)
+H_c(q_c,p_c)
-\sigma_zg(q_c)u.
$$

With mechanical parity $P_u$ define

$$
U_P
=|+\rangle\langle+|\otimes I
+|-\rangle\langle-|\otimes P_u.
$$

Then

$$
U_P^\dagger H U_P
=H_m+H_c-g(q_c)u.
$$

In this transformed description the controller Hamiltonian and controller trajectory are independent of the source branch.

If the internal source-qubit basis is energy degenerate and has the same local rest-energy density, the controller sector can satisfy

$$
\boxed{
T^{00}_{{\rm ctrl},+}(t,\mathbf x)
=T^{00}_{{\rm ctrl},-}(t,\mathbf x)
}
$$

throughout the nongravitational source preparation.

Therefore

$$
\boxed{
\Delta Q^{\rm ctrl}_{ij}=0
}
$$

exactly in the ideal projected model.

This is stronger than merely saying the controller energy is small.

---

## 4. Hub elastic energy is branch even at leading order

The plus-mode spoke displacements reverse sign between branches:

$$
\xi^{(-)}=-\xi^{(+)}
$$

up to the $x/y$ sign pattern.

Kinetic energy density is quadratic:

$$
\mathcal E_{\rm kin}
\propto\dot\xi^2.
$$

For a symmetric branch-controlled eigenstrain, elastic energy density is also quadratic in the signed strain difference:

$$
\mathcal E_{\rm el}
=\frac12EA
(\partial_x\xi-s\epsilon_c)^2.
$$

On the branch-correlated solutions the factor of $s$ cancels inside the square.

Hence the leading internal kinetic/strain energy stored near the hub is branch even.

The dominant branch-odd $T^{00}$ term at linear order is therefore the **spatial displacement of rest mass in the spokes**, which is already included explicitly in the finite-spoke quadrupole.

---

## 5. Generic compact-support bound for controller imperfections

Now allow a nonideal branch-dependent controller energy density

$$
\Delta T^{00}_{\rm ctrl}
=T^{00}_{{\rm ctrl},+}
-T^{00}_{{\rm ctrl},-}.
$$

Assume it is supported inside

$$
|\mathbf x|\le r_h.
$$

Define its energy total-variation norm

$$
\boxed{
E_{\rm TV}^{\rm ctrl}(t)
\equiv
\int_{|\mathbf x|\le r_h}
 d^3x\,
|\Delta T^{00}_{\rm ctrl}(t,\mathbf x)|.
}
$$

For every Cartesian STF component,

$$
\left|
x_ix_j-\frac13\delta_{ij}r^2
\right|
\le r^2
\le r_h^2.
$$

Therefore

$$
\boxed{
|\Delta Q^{\rm ctrl}_{ij}(t)|
\le
\frac{r_h^2}{c^2}
E_{\rm TV}^{\rm ctrl}(t).
}
$$

This bound requires no detailed controller microphysics.

---

## 6. Compare with the desired four-spoke plus quadrupole

The main branch-difference source quadrupole is

$$
|\Delta Q_{xx}^{\rm src}|
=8\mu L|u|
\frac{\tan q}{q}.
$$

Thus the fractional controller contamination obeys

$$
\boxed{
\epsilon_Q^{\rm ctrl}
\equiv
\frac{|\Delta Q^{\rm ctrl}_{ij}|}
{|\Delta Q_{xx}^{\rm src}|}
\le
\frac{E_{\rm TV}^{\rm ctrl}}
{8\mu c^2}
\frac{r_h^2}{L|u|}
\frac{q}{\tan q}.
}
$$

This makes the possible cancellation requirement explicit.

To compete with the source quadrupole, a compact controller must carry a sufficiently large **branch-antisymmetric energy redistribution**, not merely a large branch-common internal energy.

---

## 7. If controller mismatch is linear in source displacement

Suppose imperfections produce

$$
E_{\rm TV}^{\rm ctrl}
\le
\chi_1 E_c\frac{|u|}{L},
$$

where

- $E_c$ is a characteristic controller/hub internal energy;
- $\chi_1$ is a dimensionless branch-asymmetry coefficient.

Then

$$
\boxed{
\epsilon_Q^{\rm ctrl}
\le
\frac{\chi_1}{8}
\frac{E_c}{\mu c^2}
\left(\frac{r_h}{L}\right)^2
\frac{q}{\tan q}.
}
$$

The small source amplitude cancels out.

Thus even a linear controller imperfection is parametrically suppressed by

1. the controller energy relative to endpoint rest energy;
2. the squared hub-to-source size ratio.

---

## 8. If the ideal symmetry removes all linear mismatch

For the controlled-parity architecture, the natural expectation is stronger:

$$
E_{\rm TV}^{\rm ctrl}
\le
\chi_2 E_c
\left(\frac{u}{L}\right)^2
$$

for the first nonvanishing branch-dependent energy mismatch.

Then

$$
\boxed{
\epsilon_Q^{\rm ctrl}
\le
\frac{\chi_2}{8}
\frac{E_c}{\mu c^2}
\left(\frac{r_h}{L}\right)^2
\frac{|u|}{L}
\frac{q}{\tan q}.
}
$$

The residual controller quadrupole is now suppressed by an additional deformation factor

$$
|u|/L\ll1.
$$

---

## 9. Exactly degenerate internal branch states

A particularly clean Gedanken implementation uses an internal two-level degree of freedom whose two basis states

$$
|+\rangle,\qquad|-\rangle
$$

are exactly degenerate and related by an internal symmetry.

If their local stress-energy densities are identical before coupling to the mechanical coordinate, then

$$
\Delta T^{00}_{\rm qubit}=0.
$$

The branch label itself carries no mass-energy multipole.

Its only physical effect is to reverse the sign of the internal mechanical generalized force.

This prevents the control qubit from becoming an alternative gravitational branch source at the same order as the mechanical plus mode.

---

## 10. Stress differences versus energy-density differences

The hub may experience different **signed stresses** in the two branches even when its energy density is branch common.

This is not a contradiction.

The source pieces are not separately conserved: momentum flows between spokes and hub. Therefore one should not assign a separate radiation field to the hub stress tensor in isolation.

For the complete conserved source,

$$
2\int T^{ij}_{\rm tot}d^3x
=\ddot I_{ij}^{\rm tot}.
$$

The branch-common hub energy density contributes no leading direct quadrupole to

$$
I_{ij}^{\rm tot}.
$$

The signed stresses are already part of the internal momentum balance that produces the time dependence of the total spoke+endpoint quadrupole.

---

## 11. Relativistic kinetic and elastic corrections

The mechanical kinetic/internal elastic energies scale relative to rest energy as

$$
O(v^2/c^2)
$$

and the analogous strain-energy fraction.

Under exact branch mirroring,

$$
v_-=-v_+,
$$

so

$$
v_-^2=v_+^2.
$$

These terms are branch even at leading order.

Any branch-odd relativistic correction requires an asymmetry beyond the ideal mirrored source and can be included in

$$
E_{\rm TV}^{\rm ctrl}.
$$

---

## 12. Gravitational binding-energy correction

The source is assumed weakly self-gravitating, with compactness

$$
\mathcal C
=\frac{2GM}{c^2L}
\ll1.
$$

Corrections from gravitational binding energy and nonlinear gravitational field energy are therefore parametrically

$$
O(\mathcal C)
$$

relative to the matter-sector source normalization.

They cannot cancel an $O(1)$ fraction of the leading matter quadrupole in the weak-field limit without violating the assumed expansion.

---

## 13. Practical error-budget criterion

A sufficient source-validity requirement is

$$
\boxed{
\epsilon_Q^{\rm ctrl}
\ll1,
}
$$

along with

$$
q\ll1,
$$

$$
\beta\ll1,
$$

$$
\mathcal C\ll1.
$$

For a linear controller mismatch this becomes

$$
\boxed{
\frac{\chi_1}{8}
\frac{E_c}{\mu c^2}
\left(\frac{r_h}{L}\right)^2
\ll1.
}
$$

For an exactly parity-symmetric controller,

$$
\chi_1=0
$$

and the leading residual is still smaller.

---

## 14. Adversarial verdict

The finite central controller does not reopen the source cancellation loophole provided one of the following holds:

### Ideal case

Its branch energy density is exactly common under the controlled-parity symmetry:

$$
\Delta T^{00}_{\rm ctrl}=0.
$$

Then

$$
\Delta Q^{\rm ctrl}=0.
$$

### Imperfect case

Its branch-antisymmetric energy density is compact and obeys

$$
\frac{r_h^2}{c^2}E_{\rm TV}^{\rm ctrl}
\ll
8\mu L|u|\frac{\tan q}{q}.
$$

Thus the controller contribution is now a **quantified source error term**, not an unspecified conceptual loophole.

---

## 15. Next step

The source model now has explicit error controls for

- finite spoke inertia;
- finite propagation speed in the support;
- finite hub/controller extent;
- controller branch-energy asymmetry;
- weak self-gravity.

The next theory audit should therefore return to the emitted gravitational field and receiver:

1. propagate the finite-spoke source normalization through the retarded cross response;
2. recheck the $25/16$ state-storage normalization with the corrected total quadrupole matrix elements;
3. build the next paper core around the conserved total source and explicit error parameters
   $$q_A,q_B,\epsilon_Q^{\rm ctrl},\beta,\mathcal C.$$
