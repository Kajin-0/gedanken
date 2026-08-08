# Quantized Plus-Mode Source — Conserved Finite-Spoke Version

**Updated:** 2026-08-07  
**Status:** Current quantized source model. The previous four-endpoint-mass formulas are recovered as the controlled $q\to0$ limit of the finite-mass conserved source in `CONSERVED_SOURCE_ACTUATOR_AUDIT.md`.

## 1. Source architecture

Use four endpoint masses $\mu$ connected to a central hub by four identical longitudinal elastic spokes of reference length $L$.

Define

$$
\boxed{
q\equiv\frac{\omega_sL}{c_s},
}
$$

where $c_s$ is the longitudinal sound speed of a spoke.

For one spoke, normalized to unit endpoint displacement,

$$
\boxed{
f_q(x)=\frac{\sin(qx/L)}{\sin q}.}
$$

The endpoint traction boundary condition gives

$$
\boxed{
\frac{m_r}{\mu}=q\tan q,
}
$$

where $m_r$ is the rest mass of one spoke.

The endpoint-dominated regime is

$$
\boxed{q\ll1.}
$$

---

## 2. Plus coordinate

Let $u$ be the outer endpoint displacement of the plus mode.

For branch

$$
s=\pm1,
$$

choose

$$
\xi_x^{(s)}(x)=suf_q(x),
$$

$$
\xi_y^{(s)}(x)=-suf_q(x).
$$

Thus one branch expands the $x$ pair and contracts the $y$ pair, while the other branch reverses the pattern.

The center of mass and mass dipole remain fixed by inversion symmetry.

---

## 3. Exact generalized mode mass

The spoke kinetic-energy shape factor is

$$
I_2(q)
=\frac1L\int_0^L f_q^2(x)dx
=\frac{2q-\sin2q}{4q\sin^2q}.
$$

The total generalized mode mass is

$$
M_{\rm eff}
=4\left[\mu+m_rI_2(q)\right].
$$

Using

$$
m_r/\mu=q\tan q,
$$

gives

$$
\boxed{
M_{\rm eff}(q)
=4\mu A(q),
}
$$

where

$$
\boxed{
A(q)
=\frac12+\frac{q}{\sin2q}.
}
$$

For $q\ll1$,

$$
\boxed{
A(q)
=1+\frac{q^2}{3}+\frac{7q^4}{45}+O(q^6).
}
$$

Hence

$$
M_{\rm eff}
=4\mu[1+O(q^2)].
$$

The endpoint-only result $M_{\rm eff}=4\mu$ is the $q\to0$ limit.

---

## 4. Total branch quadrupole including support mass

Including endpoint rest mass and spoke rest mass, the branch-difference STF plus quadrupole is

$$
\boxed{
\Delta Q_{xx}
=8\mu Lu\frac{\tan q}{q},
}
$$

$$
\boxed{
\Delta Q_{yy}
=-8\mu Lu\frac{\tan q}{q},
}
$$

$$
\Delta Q_{zz}=0.
$$

Therefore the one-branch time-dependent plus quadrupole operator is

$$
\boxed{
\delta Q_{xx}
=4\mu L\frac{\tan q}{q}\,u,
}
$$

$$
\delta Q_{yy}=-\delta Q_{xx}.
$$

For $q\ll1$,

$$
\boxed{
\frac{\tan q}{q}
=1+\frac{q^2}{3}+\frac{2q^4}{15}+O(q^6).
}
$$

The finite support reinforces rather than cancels the endpoint quadrupole.

---

## 5. Quantization

Use

$$
[u,p_u]=i\hbar
$$

and

$$
\boxed{
H_m
=\frac{p_u^2}{2M_{\rm eff}}
+\frac12M_{\rm eff}\omega_s^2u^2.
}
$$

The zero-point coordinate is

$$
\boxed{
u_{\rm zpf}(q)
=\sqrt{\frac{\hbar}{2M_{\rm eff}(q)\omega_s}}.
}
$$

Write

$$
\boxed{
u
=u_{\rm zpf}(a+a^\dagger).}
$$

The one-phonon quadrupole matrix element is

$$
\boxed{
q_{01}^{\rm tot}(q)
=4\mu L\frac{\tan q}{q}
\sqrt{\frac{\hbar}{2M_{\rm eff}(q)\omega_s}}.
}
$$

Relative to the endpoint-only matrix element,

$$
\boxed{
\mathcal C_Q(q)
\equiv
\frac{q_{01}^{\rm tot}(q)}{q_{01}^{\rm end}}
=
\frac{\tan q/q}{\sqrt{A(q)}}.
}
$$

For $q\ll1$,

$$
\boxed{
\mathcal C_Q(q)
=1+\frac{q^2}{6}+\frac{q^4}{24}+O(q^6).
}
$$

---

## 6. Correct spontaneous graviton linewidth

For a plus mode with

$$
Q_{xx}^{01}=q_{01},
\qquad
Q_{yy}^{01}=-q_{01},
$$

the quadrupole contraction gives

$$
Q_{ij}^{10}Q_{ij}^{01}=2|q_{01}|^2.
$$

Therefore

$$
\kappa_g
=\frac{4G\omega_s^5}{5\hbar c^5}|q_{01}|^2.
$$

Substituting the finite-spoke matrix element gives

$$
\boxed{
\kappa_g(q)
=
\frac{8G\mu L^2\omega_s^4}{5c^5}
\mathcal C_\kappa(q),
}
$$

where

$$
\boxed{
\mathcal C_\kappa(q)
=\frac{(\tan q/q)^2}{A(q)}.
}
$$

For $q\ll1$,

$$
\boxed{
\mathcal C_\kappa(q)
=1+\frac{q^2}{3}+\frac{q^4}{9}+O(q^6).
}
$$

Hence the previous endpoint-only linewidth

$$
\kappa_g^{\rm end}
=\frac{8G\mu L^2\omega_s^4}{5c^5}
$$

is correct at leading order.

---

## 7. Autonomous source branch control

Introduce a two-level source control with

$$
\sigma_z|s\rangle=s|s\rangle.
$$

A closed projected Hamiltonian is

$$
\boxed{
H
=H_m(u,p_u)
+H_c(q_c,p_c)
-\sigma_zg(q_c)u.
}
$$

For an initial source-qubit superposition, the plus mode develops mirrored coherent branches.

The controller need not acquire which-branch information before gravity acts. With mechanical parity $P_u$ define

$$
U_P
=|+\rangle\langle+|\otimes I
+|-\rangle\langle-|\otimes P_u.
$$

Since

$$
U_P^\dagger uU_P=\sigma_z u,
$$

and $H_m$ is parity even,

$$
\boxed{
U_P^\dagger H U_P
=H_m+H_c-g(q_c)u.
}
$$

Thus the nongravitational controller dynamics can be branch common.

---

## 8. Closed branch trajectory

Prescribe the mirrored outer displacement

$$
\boxed{
u_s(t)=s u_c(t).}
$$

For a smooth narrowband pulse use

$$
\boxed{
u_c(t)
=u_0
\sin^4\left(\frac{\pi t}{T}\right)
\cos(\omega_st),
\qquad 0<t<T,
}
$$

and $u_c=0$ outside the pulse.

The local mechanical mode begins and ends at the same phase-space point in both branches while the gravitational field carries away a branch-dependent wavepacket.

---

## 9. Correct emitted coherent graviton branch distance

For the prescribed outer displacement, the branch quadrupole amplitude is

$$
\boxed{
q_0(q)
=8\mu L u_0\frac{\tan q}{q}.
}
$$

For the narrowband $\sin^4$ pulse,

$$
N_\Delta
\simeq
\frac{Gq_0^2\omega_s^5}{5\hbar c^5}
\frac{35T}{128}.
$$

Therefore

$$
\boxed{
N_\Delta(q)
\simeq
\frac72
\frac{G\mu^2L^2u_0^2\omega_s^5T}
{\hbar c^5}
\left(\frac{\tan q}{q}\right)^2.
}
$$

The endpoint-only expression is multiplied by

$$
\boxed{
\left(\frac{\tan q}{q}\right)^2
=1+\frac{2q^2}{3}+\frac{17q^4}{45}+O(q^6).
}
$$

for fixed prescribed outer displacement $u_0$.

---

## 10. Independent input-output normalization check

For branch coordinates $\pm u_c$, the coherent-state amplitude difference of the mechanical mode is

$$
|\Delta\alpha_m|
\simeq
\frac{u_0g(t)}{u_{\rm zpf}}.
$$

The output-field branch distance is

$$
N_\Delta
=\kappa_g(q)
\int_0^Tdt\,|\Delta\alpha_m(t)|^2.
$$

Using

$$
\int_0^Tdt\,\sin^8(\pi t/T)
=\frac{35T}{128},
$$

the corrected $\kappa_g(q)$ and $u_{\rm zpf}(q)$ reproduce exactly

$$
N_\Delta(q)
=\frac72
\frac{G\mu^2L^2u_0^2\omega_s^5T}
{\hbar c^5}
\left(\frac{\tan q}{q}\right)^2.
$$

Thus the classical conserved quadrupole calculation and the quantized input-output normalization remain consistent after the actuator/support correction.

---

## 11. Causal-support constraint

Let

$$
\beta=\frac{\omega_sL}{c}.
$$

Since

$$
c_s\le c,
$$

$$
q\ge\beta.
$$

At the stiff causal limit with $\beta\ll1$,

$$
\frac{m_r}{\mu}\gtrsim\beta^2.
$$

The support corrections cannot be made identically zero at finite $\beta$, but they can be parametrically small in the compact nonrelativistic regime.

---

## 12. Current source chain

The current source model is

$$
\boxed{
\text{source qubit}
\to
\text{autonomous branch-common controller}
\to
\text{finite-spoke plus mode}
\to
\text{conserved total quadrupole}
\to
\text{quantized gravitational output mode}.
}
$$

The strongest former source loophole—unspecified external actuator stress-energy—is therefore closed at controlled leading order.

---

## 13. Next step

Propagate

$$
\mathcal C_\kappa(q)
$$

through the receiver loading and source→receiver formulas.

For a normalized incoming gravitational mode, the receiver loading rate should become

$$
\kappa_\Delta(R,q_B)
=\frac{25\mathcal O}{16(kR)^2}\kappa_{g,B}(q_B),
$$

while the emitted source strength $N_\Delta$ carries its independent source factor

$$
(\tan q_A/q_A)^2.
$$

Those corrections should be kept conceptually separate.
