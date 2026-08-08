# Four-Mass Plus-Quadrupole Geometry — Endpoint Benchmark

**Updated:** 2026-08-07  
**Status:** Geometric endpoint benchmark. The physically closed source is now the finite-spoke model in `CONSERVED_SOURCE_ACTUATOR_AUDIT.md`; the formulas below are its controlled $q\to0$ endpoint limit.

## 1. Purpose

Four equal endpoint masses provide an unusually clean realization of a plus-type quadrupole:

1. zero moving center of mass;
2. no time-dependent mass dipole;
3. branch-average radiative plus quadrupole zero;
4. equal and opposite plus deformation between branches;
5. closed source trajectories before and after the pulse.

Prescribed endpoint masses alone are **not** a complete conserved stress-energy tensor. They should be viewed as the geometry of the heavy endpoint sector of the explicit finite-spoke source.

Canonical conservation completion:

- `CONSERVED_SOURCE_ACTUATOR_AUDIT.md`
- `QUANTIZED_PLUS_MODE_SOURCE.md`

---

## 2. Exact endpoint geometry

Take four endpoint masses $\mu$ in the plane. For branch

$$
s=\pm1,
$$

put two masses at

$$
(\pm X_s,0,0)
$$

and two at

$$
(0,\pm Y_s,0).
$$

Define

$$
\boxed{X_s^2=L^2+s d(t),}
$$

$$
\boxed{Y_s^2=L^2-s d(t).}
$$

Then

$$
\boxed{X_s^2+Y_s^2=2L^2}
$$

is branch independent and the center of mass is exactly fixed.

---

## 3. Endpoint STF quadrupole

The endpoint mass quadrupole is

$$
Q_{ij}^{\rm end}
=\sum_A\mu
\left(x_{A,i}x_{A,j}
-\frac13\delta_{ij}r_A^2\right).
$$

The exact branch components are

$$
Q_{xx}^{(s)}
=\frac23\mu L^2+2\mu s d(t),
$$

$$
Q_{yy}^{(s)}
=\frac23\mu L^2-2\mu s d(t),
$$

$$
Q_{zz}^{(s)}
=-\frac43\mu L^2.
$$

Therefore

$$
\boxed{\Delta Q_{xx}^{\rm end}=4\mu d(t),}
$$

$$
\boxed{\Delta Q_{yy}^{\rm end}=-4\mu d(t),}
$$

$$
\Delta Q_{zz}^{\rm end}=0.
$$

---

## 4. Small-deformation plus coordinate

For

$$
|d|\ll L^2,
$$

define the endpoint displacement $u$ by

$$
X\simeq L+u,
$$

$$
Y\simeq L-u.
$$

Then

$$
d\simeq2Lu.
$$

Hence the endpoint-sector one-branch quadrupole is

$$
\delta Q_{xx}^{\rm end}
=4\mu Lu,
$$

$$
\delta Q_{yy}^{\rm end}
=-4\mu Lu,
$$

and the endpoint branch difference is

$$
\boxed{
\Delta Q_{xx}^{\rm end}=8\mu Lu,
}
$$

$$
\boxed{
\Delta Q_{yy}^{\rm end}=-8\mu Lu.
}
$$

---

## 5. How the conserved finite-spoke source modifies this result

For the explicit elastic support define

$$
\boxed{q=\frac{\omega L}{c_s}.}
$$

The exact spoke+endpoint normal mode obeys

$$
\boxed{
\frac{m_r}{\mu}=q\tan q,
}
$$

and the **total** leading branch-difference quadrupole is

$$
\boxed{
\Delta Q_{xx}^{\rm tot}
=8\mu Lu\frac{\tan q}{q},
}
$$

$$
\boxed{
\Delta Q_{yy}^{\rm tot}
=-8\mu Lu\frac{\tan q}{q}.
}
$$

Thus

$$
\boxed{
\Delta Q_{ij}^{\rm tot}
=\Delta Q_{ij}^{\rm end}
\frac{\tan q}{q}.
}
$$

For $q\ll1$,

$$
\boxed{
\frac{\tan q}{q}
=1+\frac{q^2}{3}+\frac{2q^4}{15}+O(q^6).
}
$$

The support correction therefore vanishes smoothly in the endpoint-dominated limit; it does not cancel the endpoint source.

---

## 6. Why conservation does not add a separate mysterious stress-radiation term

For the complete isolated source,

$$
\partial_\mu T^{\mu\nu}_{\rm tot}=0.
$$

Define

$$
I_{ij}
=\frac1{c^2}
\int d^3x\,T^{00}_{\rm tot}x_ix_j.
$$

Then

$$
\boxed{
\ddot I_{ij}
=2\int d^3x\,T^{ij}_{\rm tot}.
}
$$

The support stresses are essential for local momentum conservation, but at leading long wavelength the stress representation and total-energy-quadrupole representation are equivalent descriptions of the same radiation.

Any actuator cancellation would therefore have to appear as an opposite contribution to the **total energy quadrupole**. For the explicit four-spoke source, the support rest-mass contribution has the same plus sign and produces the factor $\tan q/q$ above.

---

## 7. Closed smooth pulse

A useful endpoint trajectory is

$$
\boxed{
u_c(t)
=u_0
\sin^4\left(\frac{\pi t}{T}\right)
\cos(\omega t),
\qquad0<t<T,
}
$$

with $u_c=0$ outside the pulse.

The $\sin^4$ envelope makes the compactly supported quadrupole sufficiently smooth for the idealized graviton branch norm

$$
N_\Delta
\propto
\int_0^\infty d\omega'
\,\omega'^5|\Delta\widetilde Q(\omega')|^2
$$

to be ultraviolet finite.

The mechanical mode starts and ends at the same endpoint position and velocity.

---

## 8. Correct emitted branch distance for fixed outer displacement

For the finite-spoke source the branch quadrupole amplitude is

$$
q_0
=8\mu Lu_0\frac{\tan q}{q}.
$$

In the narrowband $\sin^4$ approximation,

$$
\boxed{
N_\Delta(q)
\simeq
\frac72
\frac{G\mu^2L^2u_0^2\omega^5T}
{\hbar c^5}
\left(\frac{\tan q}{q}\right)^2.
}
$$

The endpoint-only result is recovered at $q\to0$.

---

## 9. Controlled regime

Use

$$
\boxed{|u|/L\ll1,}
$$

$$
\boxed{q=\omega L/c_s\ll1,}
$$

$$
\boxed{\beta=\omega L/c\ll1,}
$$

and weak self-gravity.

In this regime the endpoint formulas are leading terms of a finite-mass, causal support model rather than an externally forced point-particle idealization.

---

## 10. Current interpretation

The four-endpoint geometry remains valuable because it isolates the desired plus quadrupole exactly.

But the source used in the gravity paper should now be described as

> **a conserved four-spoke elastic plus mode whose heavy endpoint limit is represented by the four-mass geometry.**

This wording avoids the old actuator loophole while preserving the simple geometric intuition.
