# Finite-Size Field Error Bound Beyond the Point-Quadrupole Limit

**Date:** 2026-08-07  
**Status:** **PROPAGATION ERROR BUDGET — FIRST INTERNAL-RETARDATION CORRECTION IS QUADRATIC IN $\beta=kL$ BY INVERSION SYMMETRY**

## 1. Two independent small parameters

The conserved four-spoke source introduces the support-dynamics parameter

$$
\boxed{
q=\frac{\omega L}{c_s}.
}
$$

The gravitational field expansion has the distinct compact-source parameter

$$
\boxed{
\beta=kL=\frac{\omega L}{c}.
}
$$

Causality gives

$$
\boxed{q\ge\beta}
$$

because

$$
c_s\le c.
$$

The two effects must not be conflated:

- $q$ controls support inertia and elastic mode shape;
- $\beta$ controls retardation/multipole corrections of the gravitational field.

---

## 2. Fourier form of the radiative source

At linearized level the far-zone field in direction $\mathbf n$ depends on the spatial Fourier transform of the conserved source stress at wave vector

$$
\mathbf k=k\mathbf n.
$$

Schematically,

$$
\widetilde T^{ij}(\omega,k\mathbf n)
=\int d^3x\,
\widetilde T^{ij}(\omega,\mathbf x)
 e^{-ik\mathbf n\cdot\mathbf x}.
$$

For a compact source with

$$
kL\ll1,
$$

expand

$$
e^{-ik\mathbf n\cdot\mathbf x}
=1
-ik\mathbf n\cdot\mathbf x
-\frac{k^2}{2}(\mathbf n\cdot\mathbf x)^2
+O((kL)^3).
$$

The leading term is the usual point-quadrupole source after stress-energy conservation is used to replace the integrated stress by the second derivative of the energy quadrupole.

---

## 3. Inversion symmetry removes the $O(\beta)$ correction

The four-spoke plus mode is inversion symmetric:

$$
\mathbf x\to-\mathbf x.
$$

Opposite spokes have identical stress-energy profiles under inversion, so for the relevant branch-difference source

$$
\widetilde T^{ij}(\omega,\mathbf x)
=
\widetilde T^{ij}(\omega,-\mathbf x).
$$

Therefore

$$
\int d^3x\,
(\mathbf n\cdot\mathbf x)
\widetilde T^{ij}(\omega,\mathbf x)
=0.
$$

The linear retardation term vanishes exactly.

Hence the first internal-retardation correction is

$$
\boxed{O(\beta^2),}
$$

not $O(\beta)$.

This is the field-theory counterpart of the absence of odd mass multipoles in the inversion-symmetric source.

---

## 4. Simple absolute remainder bound

Assume the radiating source is supported inside

$$
|\mathbf x|\le L_s.
$$

Using

$$
|e^{-iy}-1+iy|
\le\frac{y^2}{2}
$$

for real $y$ near the origin and the exact cancellation of the odd term after integration,

$$
\left|
\widetilde T^{ij}(\omega,k\mathbf n)
-
\widetilde T^{ij}(\omega,0)
\right|
\le
\frac{k^2L_s^2}{2}
\int d^3x\,
|\widetilde T^{ij}(\omega,\mathbf x)|
+O(\beta^4).
$$

Thus the absolute source-form-factor error is explicitly quadratic in

$$
\beta_s=kL_s.
$$

A useful generic parametrization is

$$
\boxed{
\widetilde T^{ij}(\omega,k\mathbf n)
=\widetilde T^{ij}(\omega,0)
\left[1+c_2^{ij}(\mathbf n)\beta_s^2+O(\beta_s^4)
\right],
}
$$

where $c_2$ is geometry dependent and should not be set to unity without calculation.

---

## 5. Special aligned planar geometry is even cleaner on axis

The explicit source and receiver are planar in the $xy$ plane and the ideal line of sight is the $z$ axis.

For the exact far-zone direction

$$
\mathbf n=\hat z,
$$

all material points in an infinitesimally thin planar source satisfy

$$
\mathbf n\cdot\mathbf x=z=0.
$$

Therefore the leading far-zone phase factor is

$$
e^{-ik\mathbf n\cdot\mathbf x}=1
$$

across the source plane.

The usual transverse $kL$ phase dephasing is absent **on the symmetry axis** at leading $1/R$ order.

The first geometric wavefront-curvature correction instead comes from the next term in the large-$R$ distance expansion,

$$
|\mathbf R-\mathbf x|
=R-\mathbf n\cdot\mathbf x
+\frac{x^2-(\mathbf n\cdot\mathbf x)^2}{2R}
+\cdots,
$$

which on axis is controlled by

$$
\frac{kL^2}{R}
$$

and

$$
\frac{L^2}{R^2}.
$$

Thus the aligned planar geometry suppresses source-aperture phase error more strongly than a generic extended source.

---

## 6. Why $\kappa_g$ can still receive $O(\beta^2)$ corrections

The spontaneous linewidth

$$
\kappa_g
$$

is determined by radiation into **all directions**, not only the $z$ axis.

For generic emission direction

$$
\mathbf n\cdot\mathbf x\ne0.
$$

The inversion symmetry still removes the linear term, but the angularly integrated radiated power can acquire an

$$
O(\beta^2)
$$
finite-size correction.

Therefore the exact finite-size linewidth should be written schematically as

$$
\boxed{
\kappa_g^{\rm exact}
=
\kappa_g^{(Q)}(q)
\left[1+d_2\beta^2+O(\beta^4)
\right],
}
$$

where

$$
\kappa_g^{(Q)}(q)
$$

already contains the finite-spoke support factor

$$
\mathcal C_\kappa(q).
$$

The coefficient $d_2$ requires an explicit finite-size radiation calculation and is not fixed by the support audit.

---

## 7. Consequence for the $25/16$ storage coefficient

`FINITE_SPOKE_STORAGE_INVARIANCE.md` showed that the finite-spoke factors $\mathcal C_Q(q)$ cancel exactly from

$$
\frac{\Sigma_{AB}^R}
{\sqrt{\kappa_{g,A}\kappa_{g,B}}}
$$

at leading point-quadrupole order.

Finite-size field corrections are different. They can modify

- the directional source amplitude;
- the total source linewidth;
- the receiver's angular response;
- the cross Green-function form factor

in slightly different ways.

Therefore the conservative finite-size statement is

$$
\boxed{
\eta_{\rm store}
=
\frac{25\mathcal O}{16(kR)^2}
\left[
1+O(\beta_A^2)+O(\beta_B^2)
+O\left(\frac{kL_A^2}{R}\right)
+O\left(\frac{kL_B^2}{R}\right)
\right].
}
$$

For the exactly aligned planar far-zone geometry, some of these coefficients vanish or are further suppressed; the expression above is deliberately conservative.

---

## 8. Hierarchy of source errors

The current source has at least four independent small parameters:

### elastic support inertia

$$
q=\omega L/c_s;
$$

### gravitational finite-source retardation

$$
\beta=\omega L/c;
$$

### hub/controller contamination

$$
\epsilon_Q^{\rm ctrl};
$$

### self-gravity

$$
\mathcal C=2GM/(c^2L).
$$

Since

$$
q\ge\beta,
$$

a source satisfying

$$
q\ll1
$$

automatically satisfies

$$
\beta\ll1.
$$

Thus the endpoint-dominated elastic regime is already inside the gravitational compact-source regime.

This is useful: no separate contradictory limit is required.

---

## 9. Controlled leading model

A conservative source/receiver prediction should therefore be written as

$$
\boxed{
\text{observable}
=
\text{leading conserved-quadrupole result}
\left[
1+O(q_A^2)+O(q_B^2)
+O(\beta_A^2)+O(\beta_B^2)
+O(\epsilon_Q^{\rm ctrl})
+O(\mathcal C)
\right].
}
$$

The $q^2$ corrections already have explicit coefficients from the finite-spoke calculation. The $\beta^2$ terms remain geometry-specific field corrections.

---

## 10. Adversarial verdict

The finite-size propagation issue does not produce an $O(\beta)$ failure of the quadrupole model.

The first generic correction is quadratic because of inversion symmetry:

$$
\boxed{\delta h/h=O(\beta^2).}
$$

Moreover, the exactly aligned planar geometry removes the leading transverse phase variation on axis.

Thus the finite-source correction is parametrically controlled in the same regime already required by the endpoint-dominated elastic source.

---

## 11. Next calculation

A useful but nonessential refinement would calculate the actual coefficient $d_2$ for the explicit four-spoke stress-energy distribution by retaining the

$$
-\frac{k^2}{2}(\mathbf n\cdot\mathbf x)^2
$$

term in the conserved stress Fourier transform and integrating over radiation angles.

That would turn the current

$$
O(\beta^2)
$$
error estimate into a quantitative correction to $\kappa_g$ and the angular pattern.

For a paper-level leading-order Gedanken result, the present parametric bound may already be sufficient if all final claims are explicitly restricted to

$$
q\ll1,
\qquad
\beta\ll1.
