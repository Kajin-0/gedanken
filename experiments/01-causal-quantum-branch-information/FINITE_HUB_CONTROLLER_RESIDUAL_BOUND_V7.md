# Finite Hub / Controller Residual Bound for V7

**Date:** 2026-08-08  
**Status:** **EXPLICIT RESIDUAL BOUNDS — CLOSES THE LEADING UNQUANTIFIED SOURCE/CONTROLLER CAVEAT WITHOUT CLAIMING AN EXACT RELATIVISTIC MATERIAL MODEL**

## 1. Purpose

The V7 source is an explicit finite-support nonrelativistic elastic architecture, but it is not a microscopic relativistic hyperelastic body.

The remaining referee question is therefore not

> is the source exact to all orders?

It is the narrower and answerable question

> can the omitted finite hub/controller/internal-energy contributions be bounded relative to the retained branch quadrupole?

This note gives such bounds.

The main branch-difference plus quadrupole of the finite-spoke source is

$$
\boxed{
Q_0
\equiv
|\Delta Q_{xx}^{\rm main}|
=8\mu L|u|\frac{\tan q}{q},
\qquad
q=\frac{\omega L}{c_s}.
}
$$

For $q\ll1$,

$$
Q_0
=8\mu L|u|
\left[1+O(q^2)\right].
$$

All residuals below are compared with $Q_0$.

---

# 2. General compact branch-odd energy bound

Let an omitted component have branch-difference energy density

$$
\Delta T^{00}(\mathbf x)
=T^{00}_{+}(\mathbf x)-T^{00}_{-}(\mathbf x)
$$

supported inside radius

$$
r_c.
$$

Define the absolute branch-odd effective mass

$$
\boxed{
M_\Delta
\equiv
\frac{1}{c^2}
\int d^3x\,
|\Delta T^{00}(\mathbf x)|.
}
$$

Its STF quadrupole component obeys the conservative bound

$$
|\Delta Q^{\rm res}_{ij}|
\le
r_c^2M_\Delta.
$$

Therefore

$$
\boxed{
\frac{|\Delta Q^{\rm res}_{ij}|}{Q_0}
\le
\frac{M_\Delta}{8\mu}
\frac{r_c^2}{L|u|}
\frac{q}{\tan q}.
}
$$

This inequality is intentionally conservative. It requires no detailed internal geometry beyond compact support.

It also identifies exactly what a microscopic completion would have to control: **branch-odd energy**, not total controller or hub energy.

---

# 3. Compact work system and logical reference

The logical reference doublet is assumed degenerate with branch-independent local stress-energy to the retained order.

The compact work mode is branch common at the physical handoff, and during the ideal modal swap its coherent amplitude is the same in the two logical sectors.

Hence

$$
\boxed{
\Delta T^{00}_{S+w}=0
}
$$

at the working linear/coherent order.

Thus

$$
\boxed{
\Delta Q^{S+w}_{ij}=0
}
$$

at that order independent of their finite spatial extent.

A nonzero residual requires explicit branch asymmetry in the reference/work stress-energy and can then be bounded by the compact-support inequality above.

---

# 4. Propagating controller bus

The literal local controller completion uses branch-conditioned fields

$$
\Phi_-=-\Phi_+
$$

after branch-common fields are removed.

For the quadratic controller Hamiltonian

$$
H_\Phi
=\int d^3x
\left[
\frac{\Pi^2}{2\rho_c}
+\frac{\rho_cv_c^2}{2}(\nabla\Phi)^2
\right],
$$

the local free-field energy density is even under

$$
(\Phi,\Pi)\to(-\Phi,-\Pi).
$$

Therefore

$$
\boxed{
T^{00}_{\Phi,+}(\mathbf x,t)
=T^{00}_{\Phi,-}(\mathbf x,t)
}
$$

pointwise in the working controller model.

Likewise the local elastic--controller interaction

$$
\frac12EA_s
\left[
\partial_x\xi_a-
\epsilon_a\lambda\chi\Phi_a
\right]^2
$$

is pointwise branch common for the mirrored source/controller solution.

Hence

$$
\boxed{
\Delta Q^{\rm ctrl}_{ij}=0
}
$$

at the retained quadratic controller/linear-elastic order.

This is stronger than merely saying the controller is compact.

A lossy controller excitation that fails to clear is instead an explicit source environment and must be included in source branching/dephasing; it is not an omitted coherent quadrupole.

---

# 5. Internal kinetic and elastic energy carried by the moving source

The finite-spoke calculation already includes the **rest mass** of the spokes exactly within the longitudinal normal-mode model.

What is not included in the leading mass quadrupole is the relativistic mass-equivalent of the mechanical kinetic and elastic energies.

At displacement amplitude $u$, the characteristic mechanical mode energy is

$$
E_{\rm mech}
\sim
\frac12M_{\rm eff}\omega^2u^2.
$$

Its mass equivalent is

$$
M_{\rm mech}^{(E)}
\sim
\frac{E_{\rm mech}}{c^2}.
$$

Even if that internal energy is distributed over radius $O(L)$ and its spatial redistribution contributes with an order-unity quadrupole geometry factor, its branch-odd quadrupole scales as

$$
|\Delta Q_E|
\sim
C_E
\frac{E_{\rm mech}}{c^2}
L|u|,
$$

with

$$
C_E=O(1).
$$

Relative to the retained branch quadrupole,

$$
\frac{|\Delta Q_E|}{Q_0}
\lesssim
C_E
\frac{M_{\rm eff}}{16\mu}
\left(\frac{\omega u}{c}\right)^2
\frac{q}{\tan q}.
$$

Using

$$
\beta=\frac{\omega L}{c},
$$

this becomes

$$
\boxed{
\frac{|\Delta Q_E|}{Q_0}
\lesssim
C_E
\frac{M_{\rm eff}}{16\mu}
\beta^2
\left(\frac{u}{L}\right)^2
\frac{q}{\tan q}.
}
$$

For $q\ll1$,

$$
M_{\rm eff}\simeq4\mu,
$$

so parametrically

$$
\boxed{
\frac{|\Delta Q_E|}{Q_0}
=O\!\left[
\beta^2
\left(\frac{u}{L}\right)^2
\right].
}
$$

Thus kinetic/elastic energy corrections are suppressed by both the nonrelativistic velocity scale and the small deformation.

---

# 6. Generic compact controller-energy asymmetry

Suppose imperfections generate a branch-odd controller/hub energy bounded by

$$
\int d^3x\,|\Delta T^{00}_{\rm ctrl}|
\le
\delta_E E_{\rm mech},
$$

inside radius

$$
r_c.
$$

Here $\delta_E$ is a dimensionless asymmetry parameter; it may conservatively be taken as $O(1)$ if no better device model is available.

The compact-support bound gives

$$
\frac{|\Delta Q_{\rm ctrl}^{\rm asym}|}{Q_0}
\le
\delta_E
\frac{M_{\rm eff}}{16\mu}
\frac{\omega^2u\,r_c^2}{c^2L}
\frac{q}{\tan q}.
$$

Equivalently,

$$
\boxed{
\frac{|\Delta Q_{\rm ctrl}^{\rm asym}|}{Q_0}
\le
\delta_E
\frac{M_{\rm eff}}{16\mu}
\beta^2
\left(\frac{u}{L}\right)
\left(\frac{r_c}{L}\right)^2
\frac{q}{\tan q}.
}
$$

For $M_{\rm eff}\simeq4\mu$,

$$
\boxed{
\frac{|\Delta Q_{\rm ctrl}^{\rm asym}|}{Q_0}
\lesssim
\frac{\delta_E}{4}
\beta^2
\left(\frac{u}{L}\right)
\left(\frac{r_c}{L}\right)^2.
}
$$

This is already extremely small in the V7 regime

$$
\beta\ll1,
\qquad
u/L\ll1,
\qquad
r_c/L\ll1,
$$

unless the controller contains a branch-odd rest-energy reservoir much larger than the mechanical excitation energy. Such a reservoir is explicitly excluded by the equal-charge code assumption and would have to be modeled separately if introduced.

---

# 7. Finite hub deformation — the one nonautomatic residual

A finite hub at the origin has no branch-odd quadrupole merely because it has finite radius.

If its rest-mass distribution is unchanged between branches,

$$
\boxed{
\Delta Q_{ij}^{\rm hub}=0.
}
$$

The relevant possible correction is a **branch-dependent quadrupolar deformation of the hub itself** under the four spoke tractions.

Let

- $M_h$ be the hub mass;
- $r_h$ its radius;
- $u_h$ a bound on the branch-odd surface/internal displacement associated with the plus deformation.

For a compact body undergoing a small shape deformation, a conservative component-level estimate is

$$
|\Delta Q^{\rm hub}_{ij}|
\le
C_hM_hr_h|u_h|,
$$

where

$$
C_h=O(1)
$$

depends only on hub geometry and how $u_h$ is defined.

Therefore

$$
\boxed{
\frac{|\Delta Q^{\rm hub}_{ij}|}{Q_0}
\le
\frac{C_h}{8}
\frac{M_h}{\mu}
\frac{r_h}{L}
\frac{|u_h|}{|u|}
\frac{q}{\tan q}.
}
$$

This is the important finite-hub design inequality.

A sufficient condition for the hub correction to be negligible is

$$
\boxed{
\frac{M_h}{\mu}
\frac{r_h}{L}
\frac{|u_h|}{|u|}
\ll1
}
$$

up to the order-unity shape factor.

For the ideal rigid central hub used in the leading model,

$$
u_h=0
$$

and the correction vanishes.

For a real elastic hub, $u_h/u$ is a measurable/computable compliance parameter. No universal bound on that ratio exists without specifying the hub material and geometry; this is therefore correctly a **device-design parameter**, not a hidden universal gravitational uncertainty.

---

# 8. Hub center-of-mass recoil

Opposite spoke forces cancel exactly in the plus mode at the retained symmetric order.

Hence

$$
\mathbf F_{\rm hub}^{\rm net}=0,
$$

and the hub center of mass does not acquire a branch-dependent translation.

A manufacturing/actuation mismatch producing fractional force imbalance $\delta_F$ would give a center displacement $x_h$ and hence a dipole/translation correction. Such a mismatch is outside the ideal symmetric model and is experimentally characterizable.

The ideal theory therefore has

$$
\boxed{
\Delta\mathbf D_{\rm hub}=0
}
$$

rather than an uncontrolled $O(r_h/L)$ recoil.

---

# 9. Higher-order nonlinear material terms

The working elastic/controller model is invariant under the combined branch reversal

$$
s\to-s,
$$

$$
\xi\to-\xi,
$$

$$
\Phi\to-\Phi.
$$

Quadratic kinetic, elastic, and controller energies are therefore branch even.

A microscopic material completion can generate higher-order terms. If the constitutive law respects the geometric $x\leftrightarrow y$ branch symmetry, odd branch-energy terms remain forbidden by symmetry. If that symmetry is imperfect, the generic compact branch-odd energy bound of Sec. 2 applies.

Thus there is no universal unsuppressed controller quadrupole waiting at the next order; a nonzero residual requires either

1. finite hub deformation;
2. explicit branch-asymmetric constitutive/controller physics;
3. relativistic corrections to the mechanical energy budget;
4. higher-order gravitational self-interaction.

---

# 10. Residual hierarchy

The source-side branch quadrupole can now be organized as

$$
\Delta Q_{ij}=
\Delta Q_{ij}^{\rm main}
+\Delta Q_{ij}^{\rm hub}
+\Delta Q_{ij}^{E}
+\Delta Q_{ij}^{\rm asym}
+\cdots.
$$

The relative sizes are

$$
\boxed{
\frac{\Delta Q^{\rm main}}
{Q_0}=1,
}
$$

$$
\boxed{
\frac{|\Delta Q^{\rm hub}|}{Q_0}
\lesssim
\frac{C_h}{8}
\frac{M_h}{\mu}
\frac{r_h}{L}
\frac{u_h}{u},
}
$$

$$
\boxed{
\frac{|\Delta Q_E|}{Q_0}
=O\!\left[
\beta^2(u/L)^2
\right],
}
$$

and for compact controller asymmetry tied to the mechanical excitation energy,

$$
\boxed{
\frac{|\Delta Q_{\rm ctrl}^{\rm asym}|}{Q_0}
=O\!\left[
\delta_E\beta^2
(u/L)(r_c/L)^2
\right].
}
$$

The controller bus itself contributes

$$
\boxed{
\Delta Q_{ij}^{\rm ctrl}=0
}
$$

at the retained symmetric quadratic order.

---

# 11. What this does and does not prove

This note does **not** construct an exact relativistic hyperelastic material stress tensor.

It does establish the weaker statement actually required by V7:

> The leading actuator ambiguity is closed by an explicit conserved finite-support architecture, and the omitted source/controller terms either vanish by the branch symmetry of the working model or admit explicit small-parameter/design bounds.

The only generic finite-source residual not automatically parametrically suppressed is hub shape deformation, and it is controlled by the explicit dimensionless combination

$$
\boxed{
\epsilon_h
\equiv
\frac{M_h}{\mu}
\frac{r_h}{L}
\frac{u_h}{u}.
}
$$

A physical source design should require

$$
\boxed{
\epsilon_h\ll1.
}
$$

This is substantially stronger and more transparent than leaving “finite hub/controller extent” as an unquantified caveat.
