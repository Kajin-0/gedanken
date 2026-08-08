# Closed Four-Mass Plus-Quadrupole Source

**Timestamp:** 2026-08-07 20:04 EDT  
**Status:** Explicit nonrelativistic mechanical realization of the branch quadrupole used in Experiment 01. The endpoint-mass geometry fixes the leading mass quadrupole exactly; an exact conserved stress-energy source must also include the internal actuator/support stresses.

## 1. Goal

We want a source with all of the following properties:

1. zero moving center of mass;
2. no time-dependent mass dipole;
3. one clean plus-type quadrupole branch difference;
4. branches coincide before and after the protocol;
5. smooth enough switching that
   $$
   N_\Delta
   \propto
   \int d\omega\,\omega^5|\Delta\widetilde Q(\omega)|^2
   $$
   is ultraviolet finite;
6. a simple enough geometry that the branch quadrupole can be written analytically.

A four-mass cross achieves this.

---

## 2. Geometry

Take four equal endpoint masses $\mu$ in the plane.

For branch

$$
s=\pm1,
$$

place the two $x$-axis masses at

$$
(\pm X_s(t),0,0),
$$

and the two $y$-axis masses at

$$
(0,\pm Y_s(t),0).
$$

Define

$$
\boxed{
X_s^2(t)=L^2+s\,d(t),
}
$$

$$
\boxed{
Y_s^2(t)=L^2-s\,d(t).
}
$$

Require

$$
|d(t)|<L^2
$$

so all radii remain real.

The center of mass is exactly at the origin in both branches for all time.

Also,

$$
\boxed{
X_s^2+Y_s^2=2L^2
}
$$

is constant and branch independent.

---

## 3. Trace-free mass quadrupole

Use the reduced STF mass quadrupole

$$
Q_{ij}
=\sum_A m_A
\left(
x_{A,i}x_{A,j}
-\frac13\delta_{ij}r_A^2
\right).
$$

The pair on the $x$ axis contributes

$$
Q_{xx}^{(x)}
=\frac43\mu X_s^2,
$$

$$
Q_{yy}^{(x)}
=Q_{zz}^{(x)}
=-\frac23\mu X_s^2.
$$

The pair on the $y$ axis contributes

$$
Q_{yy}^{(y)}
=\frac43\mu Y_s^2,
$$

$$
Q_{xx}^{(y)}
=Q_{zz}^{(y)}
=-\frac23\mu Y_s^2.
$$

Therefore

$$
Q_{xx}^{(s)}
=\frac{\mu}{3}
(4X_s^2-2Y_s^2),
$$

$$
Q_{yy}^{(s)}
=\frac{\mu}{3}
(4Y_s^2-2X_s^2),
$$

$$
Q_{zz}^{(s)}
=-\frac{2\mu}{3}
(X_s^2+Y_s^2).
$$

Substituting the branch geometry gives

$$
\boxed{
Q_{xx}^{(s)}
=\frac23\mu L^2+2\mu s\,d(t),
}
$$

$$
\boxed{
Q_{yy}^{(s)}
=\frac23\mu L^2-2\mu s\,d(t),
}
$$

and

$$
\boxed{
Q_{zz}^{(s)}
=-\frac43\mu L^2,
}
$$

which is constant.

---

## 4. Exact branch-difference quadrupole

Subtract branch $s=-1$ from branch $s=+1$:

$$
\boxed{
\Delta Q_{xx}(t)
=4\mu d(t),
}
$$

$$
\boxed{
\Delta Q_{yy}(t)
=-4\mu d(t),
}
$$

$$
\boxed{
\Delta Q_{zz}(t)=0.
}
$$

Thus the time-dependent branch difference is exactly the plus-type quadrupole assumed throughout Experiment 01:

$$
\boxed{
\Delta Q_{xx}=q(t),
\qquad
\Delta Q_{yy}=-q(t),
}
$$

with

$$
\boxed{q(t)=4\mu d(t).}
$$

No time-dependent monopole or dipole is required.

---

## 5. Closed smooth branch excursion

Choose

$$
\boxed{
d(t)
=d_0g(t)\cos(\omega_0t),
}
$$

where

$$
\boxed{
g(t)
=\sin^4\left(\frac{\pi t}{T}\right),
\qquad 0<t<T,
}
$$

and

$$
g(t)=0
$$

outside the pulse.

Near either endpoint,

$$
g(t)\propto t^4.
$$

Hence

$$
g,\ \dot g,\ \ddot g,\ g^{(3)}
$$

all vanish at the endpoints.

Therefore

$$
d(0)=\dot d(0)=0,
$$

and

$$
d(T)=\dot d(T)=0.
$$

The two branches begin in the same mass configuration with the same velocity and return to the same mass configuration with the same velocity.

This makes the protocol naturally compatible with a later source-path recombination/eraser operation.

---

## 6. Why $\sin^4$ rather than a hard $\sin^2$ quadrupole envelope

A compactly supported quadrupole with only

$$
Q=\dot Q=0
$$

at the endpoints but discontinuous $\ddot Q$ has a Fourier tail too slow for the idealized coherent-graviton norm

$$
N_\Delta
\propto
\int d\omega\,
\omega^5|\Delta\widetilde Q(\omega)|^2
$$

to be safely ultraviolet finite.

The $\sin^4$ envelope makes the quadrupole $C^3$ across the pulse boundaries. Its Fourier transform therefore decays sufficiently rapidly that the $\omega^5$-weighted norm converges.

A $C^\infty$ bump would be even cleaner but would sacrifice the elementary finite-Fourier-component algebra of $\sin^4$.

The earlier `SMOOTH_SIN2_SOURCE_QUANTUM_WINDOW.md` remains valid as an **abstract emitted temporal-mode benchmark**, but a hard compact $\sin^2$ envelope should not be identified literally with the physical quadrupole history without additional smoothing.

---

## 7. Small-excursion mechanical coordinates

For

$$
|d|\ll L^2,
$$

$$
X_s
=L\sqrt{1+s d/L^2}
\simeq
L+s\frac{d}{2L},
$$

and

$$
Y_s
\simeq
L-s\frac{d}{2L}.
$$

Thus branch $s=+1$ expands the $x$ pair while contracting the $y$ pair, and branch $s=-1$ does the opposite.

The characteristic endpoint speed is

$$
\boxed{
v_{\rm end}
\sim
\frac{|\dot d|}{2L}.
}
$$

A sufficient nonrelativistic condition is

$$
\boxed{
\frac{d_0}{2L}
\left(
\omega_0+\frac{4\pi}{T}
\right)
\ll c.
}
$$

The exact numerical envelope derivative bound can be inserted if needed; this expression is a conservative scale estimate.

---

## 8. Narrowband emitted branch mode

The branch quadrupole difference is

$$
q(t)
=4\mu d_0
\sin^4\left(\frac{\pi t}{T}\right)
\cos(\omega_0t).
$$

Define

$$
\boxed{q_0=4\mu d_0.}
$$

If

$$
\omega_0T\gg1,
$$

the positive-frequency radiative spectrum is concentrated near $\omega_0$.

The outgoing coherent graviton difference-mode amplitude carries the factor

$$
\omega^{5/2}\Delta\widetilde Q_{ij}(\omega).
$$

Across a narrow bandwidth,

$$
\omega^{5/2}
=\omega_0^{5/2}
[1+O((\omega-\omega_0)/\omega_0)],
$$

so the normalized temporal graviton envelope is, to leading order,

$$
\boxed{
f_S(t)
=\sqrt{\frac{128}{35T}}
\sin^4\left(\frac{\pi t}{T}\right),
\qquad 0<t<T.
}
$$

The normalization follows from

$$
\int_0^Tdt\,
\sin^8\left(\frac{\pi t}{T}\right)
=\frac{35T}{128}.
$$

Thus this mechanical source produces exactly the smooth finite temporal-mode family analyzed in the companion receiver calculation, up to controlled narrowband corrections.

---

## 9. Branch-mode coherent-state distance

The general quadrupole result is

$$
N_\Delta
=\frac{G}{5\pi\hbar c^5}
\int_0^\infty d\omega\,
\omega^5
|\Delta\widetilde Q_{ij}(\omega)|^2.
$$

For a narrowband plus quadrupole

$$
\Delta Q_{xx}=q_0g(t)\cos\omega_0t,
$$

$$
\Delta Q_{yy}=-\Delta Q_{xx},
$$

the previously derived narrowband relation gives

$$
N_\Delta
\simeq
\frac{Gq_0^2\omega_0^5}{5\hbar c^5}
\int_0^Tdt\,g^2(t).
$$

For

$$
g(t)=\sin^4(\pi t/T),
$$

$$
\int_0^Tdt\,g^2(t)
=\frac{35T}{128}.
$$

Using

$$
q_0=4\mu d_0,
$$

gives

$$
\boxed{
N_\Delta
\simeq
\frac{7}{8}
\frac{G\mu^2d_0^2\omega_0^5T}
{\hbar c^5},
}
$$

within the stated narrowband convention.

This is the first direct expression in the project connecting a closed mechanical branch excursion to the emitted coherent graviton branch distance.

---

## 10. Conservation caveat and how to formulate it correctly

Four prescribed accelerated point masses by themselves do **not** define a conserved stress-energy tensor. External forces would violate

$$
\partial_\mu T^{\mu\nu}=0
$$

for the point-mass subsystem.

The physical source must include the internal stresses/actuator degrees of freedom that drive the symmetric motion.

The correct Gedanken source is therefore:

> **a closed four-mass mechanical system whose internal elastic/actuator stress-energy generates the stated endpoint trajectories, with the total source stress tensor conserved.**

In the nonrelativistic long-wavelength limit, the leading TT radiation of a conserved isolated system is determined by its total mass quadrupole. The four heavy endpoint masses are a constructive realization of the desired leading quadrupole pattern; actuator/stress contributions must be included in any exact microscopic source model.

To avoid overclaiming, the paper should phrase the result as an explicit **leading-order conserved quadrupole realization**, not as a complete exact point-particle stress tensor.

---

## 11. Why this geometry is unusually useful

The relation

$$
X_s^2+Y_s^2=2L^2
$$

removes the time-dependent axisymmetric quadrupole component automatically.

The two branches differ only by the sign of the plus deformation.

Thus the source is a mechanical analogue of a single plus-polarized quadrupole oscillator placed into a coherent sign superposition:

$$
\boxed{
|+q(t)\rangle+|-q(t)\rangle.
}
$$

The branch difference is twice the deformation, while the branch-average radiative quadrupole vanishes.

This is conceptually cleaner than moving one center of mass back and forth because it respects zero dipole and isolates the radiative quadrupole from the start.

---

## 12. Strongest next step

Insert the normalized emitted mode

$$
f_S(t)
=\sqrt{128/(35T)}\sin^4(\pi t/T)
$$

into the noisy receiver exactly, optimize the receiver linewidth $\kappa T$, and derive the source-specific EB/non-EB and absolute-certification spacetime bubbles.