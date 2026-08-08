# Exact $O(\beta^2)$ Finite-Size Form Factor for the Four-Spoke Plus Mode

**Date:** 2026-08-07  
**Status:** **QUANTITATIVE REFINEMENT — GENERIC $O(\beta^2)$ FIELD BOUND SHARPENED FOR THE IDEAL SLENDER-SPOKE NORMAL MODE**

## 1. Purpose

`FINITE_SIZE_FIELD_ERROR_BOUND.md` proves that inversion symmetry removes the linear internal-retardation correction and leaves

$$
\delta h/h=O(\beta^2),
\qquad
\beta\equiv kL=\frac{\omega L}{c}.
$$

This note calculates the actual quadratic coefficient for the explicit four-spoke longitudinal plus mode used in the conserved source model.

The result is

$$
\boxed{
\kappa_g(q,\beta)
=
\kappa_g^{(Q)}(q)
\left[
1-\frac{2a(q)}{7}\beta^2
+O(\beta^4)
\right],
}
$$

where

$$
\boxed{
a(q)
=\frac12+\frac{\cot q}{q}-\frac1{q^2},
}
$$

and

$$
q=\frac{\omega L}{c_s}.
$$

In the endpoint-dominated limit,

$$
a(q)=\frac16-\frac{q^2}{45}+O(q^4),
$$

so

$$
\boxed{
\kappa_g
=
\kappa_g^{(Q)}
\left[
1-\frac{\beta^2}{21}
+O(q^2\beta^2,\beta^4)
\right].
}
$$

Thus the first finite-source correction to the total radiative linewidth is not only quadratic; its coefficient is small and negative for the explicit slender-spoke mode.

---

## 2. Scope

The calculation assumes

- the linear longitudinal spoke mode of `CONSERVED_SOURCE_ACTUATOR_AUDIT.md`;
- four slender spokes with negligible transverse thickness;
- a compact hub/controller whose separate correction is controlled by `HUB_CONTROLLER_RESIDUAL_BOUND.md`;
- weak gravity and linearized radiation;
- the free normal mode, or a narrowband driven source whose carrier is dominated by the same mode shape;
- far-zone radiation.

It is a finite-source radiation correction **in addition to** the finite-support inertia correction already encoded in

$$
\mathcal C_\kappa(q).
$$

---

## 3. Longitudinal stress profile

For one spoke use material coordinate

$$
x\in[0,L]
$$

and the normalized normal-mode shape

$$
\boxed{
f_q(x)
=\frac{\sin(qx/L)}{\sin q}.
}
$$

For harmonic endpoint displacement amplitude $u$, the linear axial stress resultant is proportional to

$$
EA\,u\,f_q'(x).
$$

Since

$$
Lf_q'(x)
=\frac{q\cos(qx/L)}{\sin q},
$$

the spatial profile relevant to the radiative stress Fourier transform is known analytically.

The two opposite spokes on one axis add with a cosine phase factor. Normalize the axis stress form factor to its zero-wave-number value:

$$
\boxed{
\mathcal F_q(z)
\equiv
\frac{q}{\sin q}
\int_0^1 ds\,
\cos(qs)\cos(zs).
}
$$

Here

$$
z=\beta n_x
$$

for an $x$-directed spoke pair, with $\mathbf n$ the radiation direction.

The integral is exact:

$$
\boxed{
\mathcal F_q(z)
=
\frac{q}{2\sin q}
\left[
\frac{\sin(q-z)}{q-z}
+
\frac{\sin(q+z)}{q+z}
\right].
}
$$

The apparent singularities at $z=\pm q$ are removable.

By construction,

$$
\boxed{\mathcal F_q(0)=1.}
$$

---

## 4. Small-$\beta$ expansion

Expand

$$
\cos(zs)=1-\frac{z^2s^2}{2}+O(z^4).
$$

Then

$$
\boxed{
\mathcal F_q(z)
=1-a(q)z^2+O(z^4),
}
$$

with

$$
a(q)
=\frac12\frac{q}{\sin q}
\int_0^1ds\,s^2\cos(qs).
$$

Carrying out the integral gives

$$
\boxed{
a(q)
=\frac12+\frac{\cot q}{q}-\frac1{q^2}.
}
$$

For small $q$,

$$
\boxed{
a(q)
=\frac16
-\frac{q^2}{45}
-\frac{2q^4}{945}
+O(q^6).
}
$$

For $q\to0$, the spoke strain is uniform and

$$
\mathcal F_0(z)=\frac{\sin z}{z},
$$

as expected.

---

## 5. Direction-dependent plus stress tensor

Factor out the common zero-wave-number stress amplitude. The dimensionless radiative source tensor is

$$
\boxed{
S_{ij}(\mathbf n)
=\operatorname{diag}
\left(
\mathcal F_q(\beta n_x),
-\mathcal F_q(\beta n_y),
0
\right).
}
$$

The relative minus sign is the plus-mode $x/y$ pattern.

Let

$$
P_{ij}=\delta_{ij}-n_in_j
$$

and

$$
\Lambda_{ij,kl}
=P_{ik}P_{jl}
-\frac12P_{ij}P_{kl}
$$

be the TT projector.

The angular power kernel is

$$
\boxed{
\mathcal W(\mathbf n)
=S_{ij}\Lambda_{ij,kl}S_{kl}.
}
$$

For a symmetric tensor $S$ this can be written

$$
\mathcal W
=
\operatorname{tr}(S^2)
-2\,\mathbf n^TS^2\mathbf n
+(\mathbf n^TS\mathbf n)^2
-\frac12
\left[
\operatorname{tr}S-\mathbf n^TS\mathbf n
\right]^2.
$$

---

## 6. Angular integration

At $\beta=0$,

$$
S^{(0)}=\operatorname{diag}(1,-1,0),
$$

and

$$
\boxed{
\int d\Omega\,\mathcal W_0
=\frac{16\pi}{5}.
}
$$

Using

$$
\mathcal F_q(\beta n_x)
=1-a(q)\beta^2n_x^2+O(\beta^4),
$$

$$
-\mathcal F_q(\beta n_y)
=-1+a(q)\beta^2n_y^2+O(\beta^4),
$$

and the standard isotropic angular moments, the integrated kernel becomes

$$
\boxed{
\int d\Omega\,\mathcal W
=
\frac{16\pi}{5}
\left[
1-\frac{2a(q)}{7}\beta^2
+O(\beta^4)
\right].
}
$$

Equivalently, the unnormalized quadratic correction is

$$
-\frac{32\pi}{35}a(q)\beta^2.
$$

Since the spontaneous graviton linewidth is proportional to the total angle-integrated radiated power,

$$
\boxed{
\kappa_g(q,\beta)
=
\kappa_g^{(Q)}(q)
\left[
1-\frac{2a(q)}{7}\beta^2
+O(\beta^4)
\right].
}
$$

Here

$$
\kappa_g^{(Q)}(q)
=
\frac{8G\mu L^2\omega^4}{5c^5}
\mathcal C_\kappa(q)
$$

is the already-corrected compact-source linewidth from the finite-spoke audit.

---

## 7. Endpoint-dominated limit

Using

$$
a(0)=\frac16,
$$

gives

$$
\boxed{
\kappa_g(0,\beta)
=
\kappa_g^{(Q)}(0)
\left[
1-\frac{\beta^2}{21}
+O(\beta^4)
\right].
}
$$

More generally,

$$
-\frac{2a(q)}{7}
=-\frac1{21}
+\frac{2q^2}{315}
+O(q^4).
$$

Thus the support-mode correction and the finite-source field correction remain parametrically distinct:

- support inertia changes the compact-source linewidth by
  $$
  +\frac{q^2}{3}+O(q^4);
  $$
- finite wavelength changes the total angular radiation by
  $$
  -\frac{\beta^2}{21}+O(q^2\beta^2,\beta^4).
  $$

Because causality gives

$$
\beta\le q,
$$

the finite-wavelength coefficient is also substantially smaller numerically in the endpoint-dominated regime.

---

## 8. Why the sign is negative

Finite transverse size introduces destructive phase interference away from the symmetry axis.

The on-axis field does not suffer this phase reduction for an ideal planar source, but generic oblique directions do.

Therefore the total radiated power decreases slightly relative to the point-quadrupole approximation at fixed zero-wave-number quadrupole normalization.

The effect is a weak directivity enhancement rather than a loss of the desired on-axis signal.

---

## 9. Exact on-axis result in the Fraunhofer limit

For

$$
\mathbf n=\hat z,
$$

the source lies in the $xy$ plane and

$$
n_x=n_y=0.
$$

Therefore

$$
\boxed{
\mathcal F_q(\beta n_x)
=\mathcal F_q(\beta n_y)
=1
}
$$

for every $\beta$ within the slender-planar model.

Hence the leading $1/R$ on-axis far-zone amplitude has **no transverse $kL$ form-factor correction at all**.

The remaining geometric corrections are instead controlled by

$$
\frac{kL^2}{R},
\qquad
\frac{L^2}{R^2},
$$

from wavefront curvature and amplitude variation, plus finite thickness, hub extent, and higher internal structure.

This sharpens the qualitative statement in `FINITE_SIZE_FIELD_ERROR_BOUND.md`.

---

## 10. Consequence for normalized storage

At leading Fraunhofer order, the aligned planar source-to-receiver cross amplitude keeps its point-quadrupole on-axis value, while each mode's total spontaneous linewidth acquires the angular correction above.

Write

$$
\kappa_{g,A}
=
\kappa_{g,A}^{(Q)}
\left[
1-c_A\beta_A^2+O(\beta_A^4)
\right],
$$

$$
\kappa_{g,B}
=
\kappa_{g,B}^{(Q)}
\left[
1-c_B\beta_B^2+O(\beta_B^4)
\right],
$$

with

$$
\boxed{
c_X=\frac{2a(q_X)}7.}
$$

The normalized storage amplitude therefore becomes

$$
\boxed{
t_{AB}^{\rm store}
=
t_{AB}^{(Q)}
\left[
1+
\frac{a(q_A)}7\beta_A^2
+
\frac{a(q_B)}7\beta_B^2
+\cdots
\right],
}
$$

where the omitted terms include

$$
O(\beta^4),
\qquad
O(kL^2/R),
$$

finite-thickness effects, and hub/controller corrections.

Squaring gives

$$
\boxed{
\eta_{\rm store}
=
\frac{25\mathcal O}{16(kR)^2}
\left[
1+
\frac{2}{7}
\left(
 a(q_A)\beta_A^2
+a(q_B)\beta_B^2
\right)
+\cdots
\right].
}
$$

In the endpoint-dominated limit,

$$
\boxed{
\eta_{\rm store}
=
\frac{25\mathcal O}{16(kR)^2}
\left[
1+
\frac{\beta_A^2+\beta_B^2}{21}
+\cdots
\right].
}
$$

For equal source and receiver sizes,

$$
\eta_{\rm store}
=
\frac{25\mathcal O}{16(kR)^2}
\left[
1+\frac{2\beta^2}{21}+\cdots
\right].
$$

So the previously audited $25/16$ coefficient is the exact compact-source limit, while the first explicit finite-aperture correction for this geometry is a small positive directivity correction.

---

## 11. Numerical regression check

Direct Gauss-Legendre integration of the exact TT angular kernel agrees with the expansion.

Representative ratios

$$
\frac{\kappa_g^{\rm exact}}{\kappa_g^{(Q)}}
$$

at $\beta=0.2$ are

- $q=0.05$: exact $0.99809855$, quadratic prediction $0.99809587$;
- $q=0.30$: exact $0.99812092$, quadratic prediction $0.99811829$;
- $q=0.70$: exact $0.99822816$, quadratic prediction $0.99822579$.

The residual is $O(\beta^4)$ as expected.

---

## 12. Adversarial verdict

The generic finite-size concern is now quantitatively controlled for the ideal four-spoke normal mode.

There is no hidden $O(\beta)$ correction.

For the total gravitational linewidth,

$$
\boxed{
\frac{\delta\kappa_g}{\kappa_g}
=-\frac{\beta^2}{21}
+\cdots
}
$$

in the endpoint-dominated limit.

For the aligned planar far-zone signal, the transverse source form factor is exactly unity on axis at leading $1/R$ order.

Thus finite size slightly increases normalized directional storage efficiency rather than threatening the source-to-receiver link.

The remaining geometric corrections are smaller Fraunhofer/near-field terms and finite hub/thickness effects already separated in the source error budget.

---

## 13. What this does not claim

This coefficient is not universal for arbitrary extended quadrupoles.

It depends on

- the four-spoke plus geometry;
- longitudinal slender-spoke stress profiles;
- the aligned planar configuration;
- the linear normal-mode approximation.

For another source geometry the generic result remains only

$$
O(\beta^2).
$$

---

## 14. Background references

The use of the conserved stress Fourier transform and systematic multipole expansion is standard in gravitational-radiation theory; see, for example, L. Blanchet, arXiv:gr-qc/9801101. A covariant hyperelastic stress-energy completion is available in relativistic elasticity; see J. D. Brown, arXiv:2004.03641.

The coefficient derived above is specific to the repository's explicit finite-spoke normal mode and is not attributed to those references.
