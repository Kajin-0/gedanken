# Nonlinear Quadrupole / Gaussianity Audit of the Four-Spoke Source

**Date:** 2026-08-07  
**Status:** **GAUSSIAN BRANCH MODE PROTECTED BY PLUS SYMMETRY — LEADING NONLINEAR REST-MASS QUADRUPOLE IS PARITY EVEN, LIES AT $2\omega$, AND IS PARAMETRICALLY SMALL**

## 1. Purpose

The source→graviton channel is treated as a linear bosonic Gaussian channel around the finite-spoke plus mode.

A natural objection is that the physical mass quadrupole depends on the **square** of particle positions. If

$$
r=L+u,
$$

one generically expects terms proportional to

$$
L^2,
\qquad
Lu,
\qquad
u^2.
$$

The $u^2$ term could in principle generate

- two-phonon gravitational transitions;
- radiation at $2\omega$;
- non-Gaussian source dynamics.

For the mirrored four-spoke plus source, the result is favorable:

1. the branch-carrying plus quadrupole is **exactly linear in $u$** in the geometrical rest-mass sector;
2. the quadratic term is parity even and axisymmetric;
3. in the harmonic/RWA regime it radiates in a separate $2\omega$ sector;
4. its two-phonon rate is suppressed by the squared zero-point strain.

---

# 2. Exact four-endpoint geometry

For one instantaneous value of the plus coordinate $u$, let

$$
\boxed{X=L+u,}
$$

$$
\boxed{Y=L-u.}
$$

There are two endpoint masses $\mu$ at

$$
(\pm X,0,0)
$$

and two at

$$
(0,\pm Y,0).
$$

Use the STF mass quadrupole

$$
Q_{ij}
=\sum_A m_A
\left(
 x_{A,i}x_{A,j}
-\frac13r_A^2\delta_{ij}
\right).
$$

---

# 3. Exact endpoint quadrupole through $u^2$

The four endpoint masses give

$$
\boxed{
Q_{xx}^{\rm end}
=\frac{2\mu}{3}L^2
+4\mu Lu
+\frac{2\mu}{3}u^2,
}
$$

$$
\boxed{
Q_{yy}^{\rm end}
=\frac{2\mu}{3}L^2
-4\mu Lu
+\frac{2\mu}{3}u^2,
}
$$

$$
\boxed{
Q_{zz}^{\rm end}
=-\frac{4\mu}{3}L^2
-\frac{4\mu}{3}u^2.
}
$$

The static $L^2$ terms do not radiate.

The linear and quadratic pieces have distinct tensor structures.

---

# 4. The branch-carrying plus quadrupole is exactly linear

Take the plus combination

$$
Q_+
\equiv
Q_{xx}-Q_{yy}.
$$

Then

$$
\boxed{
Q_+^{\rm end}
=8\mu Lu.
}
$$

This is an exact algebraic identity:

$$
X^2-Y^2
=(L+u)^2-(L-u)^2
=4Lu.
$$

The $u^2$ terms cancel exactly.

Therefore under branch reversal

$$
u\to-u,
$$

$$
\boxed{
Q_+(-u)=-Q_+(u).
}
$$

No geometrical $u^2$ correction contaminates the endpoint plus tensor.

---

# 5. Quadratic endpoint tensor is branch even

The $u^2$ piece is

$$
\boxed{
Q_{ij}^{(2),\rm end}
=
\mu u^2
\operatorname{diag}
\left(
\frac23,
\frac23,
-\frac43
\right).
}
$$

This is

- STF;
- axisymmetric about $z$;
- invariant under
  $$u\to-u.$$

Hence

$$
\boxed{
Q_{ij}^{(2)}(-u)=Q_{ij}^{(2)}(u).
}
$$

It does not carry the sign of the plus branch.

---

# 6. Exact slender-spoke rest-mass result

The same structure survives inclusion of finite spoke rest mass.

For one material point $x$ on an $x$ spoke,

$$
r_x=x+uf_q(x),
$$

while on a $y$ spoke

$$
r_y=x-uf_q(x).
$$

Because the plus combination compares $r_x^2$ and $r_y^2$,

$$
(r_x)^2-(r_y)^2
=4xu f_q(x)
$$

exactly.

Therefore the distributed spoke contribution to

$$
Q_{xx}-Q_{yy}
$$

is also exactly linear in $u$.

Including endpoints and spokes recovers

$$
\boxed{
Q_+(u)
=8\mu Lu\frac{\tan q}{q},
}
$$

for the one-branch dynamic plus amplitude convention of the current finite-spoke source.

Equivalently,

$$
Q_{xx}^{(1)}
=4\mu L\frac{\tan q}{q}u,
$$

$$
Q_{yy}^{(1)}=-Q_{xx}^{(1)}.
$$

---

# 7. Quadratic finite-spoke rest-mass tensor

Let

$$
I_2(q)
=\frac1L\int_0^Lf_q^2(x)dx.
$$

The four spoke rest masses contribute the same axisymmetric quadratic tensor as the endpoints with the replacement

$$
\mu
\to
m_rI_2(q).
$$

Therefore

$$
\boxed{
Q_{ij}^{(2),\rm rest}
=
\left[
\mu+m_rI_2(q)
\right]
 u^2
\operatorname{diag}
\left(
\frac23,
\frac23,
-\frac43
\right).
}
$$

Using

$$
M_{\rm eff}
=4[\mu+m_rI_2(q)]
=4\mu A(q),
$$

we obtain

$$
\boxed{
Q_{ij}^{(2),\rm rest}
=
\mu A(q)u^2
\operatorname{diag}
\left(
\frac23,
\frac23,
-\frac43
\right).
}
$$

Again this is branch even.

---

# 8. Quantized linear branch mode

Quantize

$$
u
=u_{\rm zpf}(a+a^\dagger).
$$

The one-phonon matrix element of the branch-carrying plus tensor is

$$
\boxed{
Q_{xx}^{01}
=4\mu L\frac{\tan q}{q}u_{\rm zpf},
}
$$

$$
Q_{yy}^{01}=-Q_{xx}^{01}.
$$

Its tensor norm is

$$
\boxed{
Q_{ij}^{10}Q_{ij}^{01}
=32\mu^2L^2
\left(\frac{\tan q}{q}\right)^2
u_{\rm zpf}^2.
}
$$

This produces the current gravitational linewidth

$$
\kappa_g(q).
$$

---

# 9. Quantized quadratic tensor

Use

$$
\langle0|u^2|2\rangle
=\sqrt2\,u_{\rm zpf}^2.
$$

The $|2\rangle\to|0\rangle$ quadratic quadrupole matrix element is

$$
\boxed{
Q_{ij}^{02,(2)}
=
\sqrt2\,\mu A(q)u_{\rm zpf}^2
\operatorname{diag}
\left(
\frac23,
\frac23,
-\frac43
\right).
}
$$

Its contraction is

$$
\boxed{
Q_{ij}^{20,(2)}Q_{ij}^{02,(2)}
=
\frac{16}{3}
\mu^2A(q)^2u_{\rm zpf}^4.
}
$$

---

# 10. Exact rest-mass two-phonon / one-phonon rate ratio

For a quadrupole transition of angular frequency $\Omega$,

$$
\Gamma
=\frac{2G\Omega^5}{5\hbar c^5}
Q_{ij}^{fi}Q_{ij}^{if}.
$$

The linear transition occurs at

$$
\Omega=\omega,
$$

while the quadratic two-phonon transition occurs at

$$
\Omega=2\omega.
$$

Therefore

$$
\frac{\Gamma_{2\to0}^{(2)}}
{\Gamma_{1\to0}^{(1)}}
=32
\frac{
Q_{ij}^{20,(2)}Q_{ij}^{02,(2)}
}{
Q_{ij}^{10,(1)}Q_{ij}^{01,(1)}
}.
$$

Substitution gives

$$
\boxed{
\frac{\Gamma_{2\to0}^{(2)}}
{\Gamma_{1\to0}^{(1)}}
=
\frac{16}{3}
\frac{A(q)^2}
{(\tan q/q)^2}
\left(
\frac{u_{\rm zpf}}{L}
\right)^2.
}
$$

In the endpoint-dominated limit

$$
q\to0,
$$

$$
A(q)\to1,
$$

$$
\tan q/q\to1,
$$

so

$$
\boxed{
\frac{\Gamma_{2\to0}^{(2)}}
{\Gamma_{1\to0}^{(1)}}
\to
\frac{16}{3}
\left(
\frac{u_{\rm zpf}}{L}
\right)^2.
}
$$

The leading nonlinear rest-mass radiation is therefore suppressed by the squared zero-point strain.

---

# 11. Frequency separation

In the interaction picture,

$$
u(t)
\propto
 a e^{-i\omega t}
+a^\dagger e^{i\omega t}.
$$

Thus

$$
u^2(t)
\propto
 a^2e^{-2i\omega t}
+a^{\dagger2}e^{2i\omega t}
+2a^\dagger a+1.
$$

Therefore the quadratic tensor contains

- a static/zero-frequency sector;
- a $2\omega$ two-phonon sector.

The branch-carrying linear plus tensor lies at

$$
\omega.
$$

In the narrowband rotating-wave regime these are distinct gravitational frequency modes.

---

# 12. Parity protection of branch information

Let mechanical parity satisfy

$$
P_a uP_a^\dagger=-u.
$$

Then

$$
P_aQ^{(1)}P_a^\dagger=-Q^{(1)},
$$

while

$$
\boxed{
P_aQ^{(2)}P_a^\dagger=Q^{(2)}.
}
$$

The two coherent source branches obey

$$
|-\alpha\rangle
=P_a|+\alpha\rangle
$$

up to the usual coherent-state phase convention.

Therefore an environment coupled **only** to the even quadratic operator $Q^{(2)}$ has identical reduced dynamics for the two parity-related branches.

The quadratic channel can produce branch-common radiation and source decoherence, but by itself it does not read out the sign of the plus branch.

The branch-distinguishing gravitational output is carried by the parity-odd $\omega$ sector.

---

# 13. Simultaneous linear and quadratic coupling

The exact gravitational interaction contains both sectors.

Schematically,

$$
H_g
=H_g^{(1)}+H_g^{(2)}+\cdots.
$$

In the harmonic narrowband limit,

$$
H_g^{(1)}
$$

couples resonantly to gravitational modes near

$$
\omega,
$$

while

$$
H_g^{(2)}
$$

couples to

$$
2\omega
$$

and zero-frequency sectors.

The leading source→receiver Gaussian model selects the normalized gravitational wavepacket near $\omega$.

The quadratic sector is therefore an orthogonal-frequency correction at leading RWA order.

---

# 14. Coherent source amplitude criterion

For a coherent source branch with

$$
\alpha\in\mathbb C,
$$

the typical physical displacement scale is

$$
\boxed{
U\sim2u_{\rm zpf}|\alpha|.
}
$$

The classical quadratic quadrupole amplitude is suppressed relative to the linear plus amplitude by

$$
O(U/L).
$$

Radiative power / transition probabilities are therefore suppressed parametrically by

$$
\boxed{O[(U/L)^2].}
$$

The same small-strain condition required for linear elasticity,

$$
\boxed{U/L\ll1,}
$$

also controls nonlinear gravitational emission from the rest-mass geometry.

---

# 15. Branch-distance consequence

For exactly mirrored classical coherent trajectories

$$
u_-(t)=-u_+(t),
$$

the quadratic rest-mass quadrupole histories are identical:

$$
\boxed{
Q_{ij}^{(2)}[u_-]
=Q_{ij}^{(2)}[u_+].
}
$$

Therefore the coherent displacement **difference** of the $2\omega$ gravitational radiation vanishes at this order:

$$
\boxed{
\Delta\alpha_{2\omega}^{(2)}=0.
}
$$

The $2\omega$ output may contain gravitons, but it does not contribute to the classical branch-distance norm

$$
N_\Delta
$$

between the two mirrored source histories.

This is stronger than simply saying its rate is small.

---

# 16. Why the rate estimate still matters

Although the branch-distance contribution vanishes for perfectly mirrored coherent histories, the quadratic coupling can still

- perturb source dynamics;
- create non-Gaussian phonon loss;
- matter for fluctuations around the coherent branches;
- contribute common gravitational radiation.

The two-phonon rate ratio above quantifies the scale of this backreaction.

Because it is suppressed by

$$
(u_{\rm zpf}/L)^2
$$

for low occupation, and by

$$
(U/L)^2
$$

at the classical amplitude level, it is consistent to neglect it in the leading Gaussian branch-information channel.

---

# 17. Relativistic/elastic energy corrections

The calculation above treats the dominant rest-mass quadrupole.

Kinetic and elastic internal energies also contribute to

$$
T^{00}/c^2.
$$

Their relative scale is already controlled by

$$
O(v^2/c^2)
$$

or elastic-energy/rest-energy order.

Under the mirrored controlled-parity solution those energy densities are branch even at leading order.

They can modify the common $0$/$2\omega$ sector without changing the leading parity-odd plus-mode result.

---

# 18. Consequence for Gaussian channel modeling

The exact physical gravitational interaction is not globally Gaussian to arbitrarily high order in source displacement.

The correct claim is narrower:

> In the small-strain, narrowband plus-mode sector, the **branch-carrying gravitational channel near $\omega$ is linear/Gaussian to leading order**, while the first geometrical rest-mass nonlinearity is a branch-even $2\omega$ correction suppressed by the squared strain.

This is the regime used throughout the source→receiver Gaussian calculations.

---

# 19. Controlled error hierarchy

The current source model should therefore carry the combined hierarchy

$$
\boxed{
\frac{U}{L}\ll1,
\qquad
q=\frac{\omega L}{c_s}\ll1,
\qquad
\beta=\frac{\omega L}{c}\ll1,
\qquad
\mathcal C\ll1.
}
$$

The respective corrections are

- nonlinear source geometry:
  $$O[(U/L)^2]$$
  in radiative strength;
- finite spoke inertia:
  $$O(q^2);$$
- finite gravitational source size:
  $$O(\beta^2);$$
- self-gravity:
  $$O(\mathcal C).$$

These are logically distinct and should not be combined into one unspecified “small correction.”

---

# 20. Adversarial verdict

The Gaussian source-channel approximation survives the first nonlinear geometry attack.

The four-spoke plus symmetry gives the exact identity

$$
\boxed{
Q_{xx}-Q_{yy}
\propto u
}
$$

in the rest-mass geometry, with no $u^2$ contamination.

The leading quadratic term is

$$
\boxed{
Q_{ij}^{(2)}
\propto u^2
\operatorname{diag}(1,1,-2),
}
$$

which is parity even and lies in the $0/2\omega$ sector.

Its low-occupation two-phonon rate is parametrically

$$
\boxed{
\frac{\Gamma_{2\to0}}
{\Gamma_{1\to0}}
\sim
\frac{16}{3}
\left(
\frac{u_{\rm zpf}}{L}
\right)^2
}
$$

up to the explicit finite-spoke factor derived above.

Thus the leading branch-information mode remains an exceptionally clean linear Gaussian sector of the source.
