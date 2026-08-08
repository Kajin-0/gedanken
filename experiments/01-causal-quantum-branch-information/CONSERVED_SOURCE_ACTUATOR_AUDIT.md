# Conserved Source + Actuator Audit for the Four-Mass Plus Mode

**Date:** 2026-08-07  
**Status:** **LEADING-ORDER ACTUATOR LOOPHOLE CLOSED FOR AN EXPLICIT ELASTIC-SPOKE ARCHITECTURE**

## 1. Problem being attacked

The four endpoint trajectories in `CONSERVED_FOUR_MASS_QUADRUPOLE_SOURCE.md` produce the desired branch quadrupole, but prescribed accelerated point masses are not by themselves a conserved source:

$$
\partial_\mu T^{\mu\nu}_{\rm endpoints}\ne0.
$$

A referee can therefore ask whether the missing actuator/support stress-energy

1. carries its own branch record;
2. modifies the radiative quadrupole;
3. cancels the endpoint contribution once total stress-energy is conserved.

This note builds an explicit closed mechanical architecture in which those questions can be answered analytically at leading nonrelativistic order.

The result is favorable but should be stated with its scope:

> **For an endpoint-dominated four-spoke elastic plus mode, the conserved support/actuator does not cancel the branch quadrupole. Its leading rest-mass contribution reinforces the endpoint quadrupole by a controlled factor $1+O[(\omega L/c_s)^2]$, while kinetic/elastic drive energies are branch-even to first order.**

A full exact relativistic hyperelastic stress tensor is still a possible refinement, but it is no longer necessary to leave the leading-order actuator effect unspecified.

---

# Part I — conserved-source identity

## 2. Total stress-energy, not endpoint masses alone

Let

$$
T^{\mu\nu}_{\rm tot}
=T^{\mu\nu}_{\rm end}
+T^{\mu\nu}_{\rm spokes}
+T^{\mu\nu}_{\rm hub}
+T^{\mu\nu}_{\rm ctrl}.
$$

The complete isolated source satisfies

$$
\boxed{
\partial_\mu T^{\mu\nu}_{\rm tot}=0.
}
$$

Define the total energy quadrupole moment

$$
\boxed{
I_{ij}(t)
=\frac1{c^2}
\int d^3x\,
T^{00}_{\rm tot}(t,\mathbf x)
x_i x_j.
}
$$

For compact support and vanishing surface terms, two integrations by parts using stress-energy conservation give

$$
\boxed{
\ddot I_{ij}(t)
=2\int d^3x\,T^{ij}_{\rm tot}(t,\mathbf x).
}
$$

This is the key structural fact.

The far-zone linearized field can be written as

$$
\boxed{
h_{ij}^{TT}(t,R)
=\frac{2G}{Rc^4}
\Lambda_{ij,kl}
\ddot I_{kl}(t-R/c)
+	ext{higher multipoles}.
}
$$

Therefore internal stresses are not an independent radiative term that should be appended to a point-mass quadrupole calculation. In a **conserved** source they are precisely what makes the stress representation and the total-energy-quadrupole representation equivalent.

Any real cancellation must appear in the total

$$
T^{00}_{\rm tot}
$$
quadrupole itself.

That is what we compute below.

---

# Part II — explicit four-spoke mechanical source

## 3. Geometry

Use

- one central hub at the origin;
- four identical slender elastic spokes of reference length $L$;
- one endpoint mass $\mu$ on each spoke;
- one spoke pair on the $x$ axis and one pair on the $y$ axis.

Let the rest mass of **one spoke** be

$$
\boxed{m_r.}
$$

Let its longitudinal sound speed be

$$
\boxed{c_s.}
$$

The hub need not be externally clamped. Opposite spokes exert equal and opposite forces, so the hub has zero net force and zero net torque in the plus mode.

A finite hub mass may therefore remain at the center of mass as part of the isolated source.

---

## 4. Exact longitudinal mode of one spoke plus endpoint mass

Let $x\in[0,L]$ denote the material coordinate along one spoke, with

$$
x=0
$$

at the hub and

$$
x=L
$$

at the endpoint mass.

For linear longitudinal elasticity,

$$
\rho A\,\ddot\xi
=EA\,\partial_x^2\xi,
$$

with

$$
\boxed{c_s^2=E/\rho.}
$$

For a harmonic mode at frequency $\omega$ define

$$
\boxed{
q\equiv\frac{\omega L}{c_s}.
}
$$

With the hub fixed by symmetry,

$$
\xi(0,t)=0.
$$

Normalize the spoke shape to unit endpoint displacement:

$$
\boxed{
f_q(x)
=\frac{\sin(qx/L)}{\sin q},
\qquad
f_q(L)=1.
}
$$

Then

$$
\xi(x,t)=u(t)f_q(x)
$$

for the reference spoke.

At the endpoint, axial stress accelerates the mass. The boundary condition is

$$
EA f_q'(L)
=\mu\omega^2 f_q(L).
$$

Using

$$
EA
=\frac{m_r}{L}c_s^2
$$

gives the exact eigenfrequency relation

$$
\boxed{
\frac{m_r}{\mu}
=q\tan q.
}
$$

For the endpoint-dominated fundamental mode,

$$
0<q\ll1,
$$

so

$$
\boxed{
\frac{m_r}{\mu}
=q^2+\frac{q^4}{3}+O(q^6).
}
$$

This makes precise what “light support” means. A strictly massless rod is not required or assumed.

---

## 5. Plus-mode branch pattern

Let

$$
s=\pm1
$$

label the source branch.

Choose the longitudinal displacement fields

### $x$ spokes

$$
\boxed{
\xi_x^{(s)}(x,t)
=s\,u_c(t)f_q(x),
}
$$

### $y$ spokes

$$
\boxed{
\xi_y^{(s)}(x,t)
=-s\,u_c(t)f_q(x).
}
$$

Thus the $x$ pair expands while the $y$ pair contracts in one branch, and the pattern reverses in the other branch.

At the endpoints,

$$
X_s=L+s u_c,
$$

$$
Y_s=L-s u_c
$$

to first order in

$$
|u_c|/L\ll1.
$$

The source has zero time-dependent dipole exactly by pair symmetry.

---

# Part III — total quadrupole including spoke mass

## 6. Endpoint contribution

For one branch, the time-dependent STF plus component from the endpoint masses is

$$
\delta Q_{xx,\rm end}^{(s)}
=4s\mu L u_c,
$$

$$
\delta Q_{yy,\rm end}^{(s)}
=-4s\mu L u_c.
$$

Therefore the endpoint branch difference is

$$
\boxed{
\Delta Q_{xx,\rm end}
=8\mu L u_c,
}
$$

$$
\boxed{
\Delta Q_{yy,\rm end}
=-8\mu L u_c.
}
$$

This is the result already used in `QUANTIZED_PLUS_MODE_SOURCE.md`.

---

## 7. Spoke rest-mass contribution

Let

$$
\lambda_r=\frac{m_r}{L}
$$

be the rest mass per reference length of one spoke.

To first order in $u_c/L$, the branch-odd shift of the $x^2$ moment of the two $x$ spokes is

$$
\delta I_{xx,\rm spokes}^{(s)}
=4s u_c
\int_0^L dx\,\lambda_r x f_q(x).
$$

Define

$$
\boxed{
j(q)
\equiv
\frac{1-q\cot q}{q^2}.
}
$$

Then

$$
\int_0^L dx\,\lambda_r x f_q(x)
=m_rL j(q).
$$

Because the $y$ spokes carry the opposite deformation, the trace change vanishes to linear order, and

$$
\delta Q_{xx,\rm spokes}^{(s)}
=4s m_rL j(q)u_c,
$$

$$
\delta Q_{yy,\rm spokes}^{(s)}
=-4s m_rL j(q)u_c.
$$

Therefore

$$
\boxed{
\Delta Q_{xx,\rm spokes}
=8m_rL j(q)u_c.
}
$$

---

## 8. Exact total branch quadrupole of the elastic-spoke mode

Add endpoints and spoke rest mass:

$$
\Delta Q_{xx}
=8Lu_c
\left[
\mu+m_rj(q)
\right].
$$

Use the exact endpoint boundary relation

$$
\frac{m_r}{\mu}=q\tan q.
$$

Since

$$
1+q\tan q\,j(q)
=\frac{\tan q}{q},
$$

we obtain the compact result

$$
\boxed{
\Delta Q_{xx}
=8\mu L u_c
\frac{\tan q}{q},
}
$$

$$
\boxed{
\Delta Q_{yy}
=-8\mu L u_c
\frac{\tan q}{q}.
}
$$

For the fundamental endpoint-dominated mode,

$$
0<q\ll1,
$$

$$
\boxed{
\frac{\tan q}{q}
=1+rac{q^2}{3}
+\frac{2q^4}{15}
+O(q^6).
}
$$

### Main adversarial result

The support mass does **not** cancel the endpoint quadrupole in this closed architecture.

It reinforces it:

$$
\boxed{
\frac{\Delta Q_{xx}}
{\Delta Q_{xx,\rm end}}
=rac{\tan q}{q}>1
\qquad(0<q<\pi/2).
}
$$

Thus an exact conservation completion exists whose leading support correction has a definite sign.

---

# Part IV — mode inertia and quantization

## 9. Exact generalized mode mass

The rod kinetic-energy shape factor is

$$
\boxed{
I_2(q)
=\frac1L
\int_0^Ldx\,f_q^2(x)
=
\frac{2q-\sin2q}
{4q\sin^2q}.
}
$$

The total kinetic energy is

$$
T
=4\left[
\frac12\mu\dot u^2
+\frac12m_r I_2(q)\dot u^2
\right].
$$

Therefore

$$
\boxed{
M_{\rm eff}
=4\left[
\mu+m_rI_2(q)
\right].
}
$$

Using

$$
m_r/\mu=q\tan q
$$

gives

$$
\boxed{
M_{\rm eff}
=4\mu
\left[
\frac12+
\frac{q}{\sin2q}
\right].
}
$$

For $q\ll1$,

$$
\boxed{
M_{\rm eff}
=4\mu
\left[
1+rac{q^2}{3}
+\frac{7q^4}{45}
+O(q^6)
\right].
}
$$

Thus the endpoint-only value

$$
M_{\rm eff}=4\mu
$$

is the controlled $q\to0$ limit of a fully finite-mass support model.

---

## 10. Corrected quadrupole matrix element

The one-branch linear quadrupole operator is

$$
\delta Q_{xx}
=4\mu L
\frac{\tan q}{q}\,u.
$$

Quantize

$$
\boxed{
u
=u_{\rm zpf}(a+a^\dagger),
}
$$

with

$$
\boxed{
u_{\rm zpf}
=\sqrt{\frac{\hbar}{2M_{\rm eff}\omega}}.
}
$$

Hence

$$
\boxed{
q_{01}^{\rm tot}
=4\mu L
\frac{\tan q}{q}
\sqrt{\frac{\hbar}{2M_{\rm eff}\omega}}.
}
$$

Relative to the endpoint-only matrix element, the correction factor is

$$
\boxed{
\mathcal C_Q(q)
=\frac{\tan q/q}
{\sqrt{\frac12+q/\sin2q}}.
}
$$

For $q\ll1$,

$$
\boxed{
\mathcal C_Q(q)
=1+rac{q^2}{6}+O(q^4).
}
$$

Therefore the gravitational spontaneous linewidth receives only an

$$
O(q^2)
$$
relative correction in the endpoint-dominated regime.

---

# Part V — causality and how light the supports may be

## 11. Sound-speed constraint

Define the compact-source velocity parameter

$$
\boxed{
\beta\equiv\frac{\omega L}{c}.
}
$$

Because a causal material obeys

$$
\boxed{c_s\le c,}
$$

we have

$$
q=\frac{\omega L}{c_s}
\ge\beta.
$$

Using

$$
\frac{m_r}{\mu}=q\tan q,
$$

the lightest possible causal spoke at fixed $\omega,L,\mu$ corresponds parametrically to the largest allowed sound speed.

For

$$
\beta\ll1,
$$

a near-maximally stiff causal support gives

$$
\boxed{
\frac{m_r}{\mu}
\gtrsim
\beta^2,
}
$$

and the unavoidable support correction to the classical branch quadrupole is only

$$
\boxed{
\frac{\Delta Q_{xx}}
{\Delta Q_{xx,\rm end}}-1
\gtrsim
\frac{\beta^2}{3}
}
$$

at the causal stiffness limit.

More generally the relevant control parameter is

$$
q=\omega L/c_s.
$$

The endpoint approximation requires

$$
\boxed{q\ll1,}
$$

not an unphysical massless actuator.

Relativistic elasticity provides consistent causal rod/string models, including the limiting case in which the longitudinal signal speed approaches $c$.

---

# Part VI — branch-controlled actuation without a hidden branch record

## 12. Branch-dependent rest-strain architecture

Introduce a central two-level control with

$$
\sigma_z|s\rangle=s|s\rangle.
$$

Let the controller impose opposite eigenstrains on the $x$ and $y$ spokes.

Schematically, for a spoke with sign

$$
\epsilon_a=
\begin{cases}
+1,&x\text{ spokes},\\
-1,&y\text{ spokes},
\end{cases}
$$

use elastic energy density

$$
\boxed{
\mathcal E_{\rm el}^{(s)}
=\frac12EA
\left[
\partial_x\xi_a
-\epsilon_a s\,\epsilon_c(q_c)
\right]^2.
}
$$

For the branch-correlated plus mode

$$
\xi_a^{(s)}
=\epsilon_a s\,u_c f_q,
$$

we get

$$
\boxed{
\mathcal E_{\rm el}^{(s)}
=\frac12EA
\left[
u_c f_q'-\epsilon_c(q_c)
\right]^2,
}
$$

which is **independent of $s$**.

Likewise

$$
\dot\xi_a^{\,2}
$$

is branch even.

Thus, in material coordinates,

- elastic strain energy;
- kinetic energy;
- controller work required to produce the mirrored trajectories

are branch common to this order.

The branch difference in $T^{00}$ is therefore dominated by the mirrored **spatial redistribution of rest mass**, which is exactly what was included in the spoke quadrupole calculation above.

---

## 13. Projected autonomous Hamiltonian

At the normal-mode level, the same architecture has the form

$$
\boxed{
H
=H_m(u,p_u)
+H_c(q_c,p_c)
-\sigma_z g(q_c)u,
}
$$

where

$$
H_m(-u,-p_u)=H_m(u,p_u).
$$

This is an autonomous Hamiltonian; no external prescribed time dependence is required in principle. The control coordinate $q_c$ may be an internal clock/work-reservoir degree of freedom whose branch-common trajectory generates the desired pulse.

For branch $s$, the mechanical equation has the mirrored solution

$$
\boxed{
u_s(t)=s\,u_c(t).}
$$

The force exerted back on the controller contains

$$
\sigma_z u_s
=s^2u_c
=u_c,
$$

and is therefore branch independent.

### Controlled-parity proof

Let $P_u$ be mechanical parity,

$$
P_u u P_u=-u,
$$

$$
P_u p_u P_u=-p_u.
$$

Define

$$
\boxed{
U_P
=|+\rangle\langle+|\otimes I
+|-\rangle\langle-|\otimes P_u.
}
$$

Then

$$
U_P^\dagger u U_P
=\sigma_z u,
$$

so

$$
U_P^\dagger
(-\sigma_z g(q_c)u)
U_P
=-g(q_c)u.
$$

Because $H_m$ is parity even,

$$
\boxed{
U_P^\dagger H U_P
=H_m+H_c-g(q_c)u,
}
$$

with no source-qubit operator remaining.

Therefore, **before gravitational coupling is included**, the controller/work reservoir can follow exactly the same quantum dynamics in both source branches. The apparent branch-dependent drive is related by a controlled parity transformation to one branch-independent autonomous drive.

This directly removes the concern that the actuator must inevitably acquire a classical which-branch record.

Gravitational coupling to the plus quadrupole breaks this trivialization in the intended way: in the parity-transformed frame it becomes branch controlled and transfers branch information to the gravitational field.

---

# Part VII — local conservation and hub stresses

## 14. Endpoint forces are internal boundary tractions

For each spoke, local elastic stress supplies the endpoint acceleration through the boundary condition

$$
EA\,\partial_x\xi(L,t)
\leftrightarrow
\mu\,\ddot u(t)
$$

plus any projected active eigenstrain force.

At the hub, the $+x$ and $-x$ spoke tractions cancel vectorially, as do the $+y$ and $-y$ tractions.

Therefore

$$
\boxed{
\mathbf F_{\rm hub}=0,
\qquad
\boldsymbol\tau_{\rm hub}=0
}
$$

for the ideal plus mode.

A finite central hub carries internal branch-dependent stress, but no center-of-mass acceleration is required.

If the hub/control energy distribution is localized within radius

$$
r_h\ll L
$$

and its total energy is branch common under the controlled-parity symmetry, its direct branch quadrupole is zero at leading order; any residual spatial correction is suppressed by its small support size.

---

## 15. What the stress terms do in the far field

The spoke stresses are branch odd and are essential to local momentum conservation.

They do **not** represent a new independent leading TT amplitude that must be added to the total mass quadrupole.

For the conserved complete source,

$$
2\int T^{ij}_{\rm tot}d^3x
=\ddot I_{ij}.
$$

Thus the stress representation and the total-energy quadrupole representation are the same leading radiative source.

The actuator can only cancel the endpoint radiation if its contribution to the total energy quadrupole has the required opposite sign.

For the explicit four-spoke mode derived here, the leading support rest-mass contribution has the **same** sign and yields

$$
\Delta Q_{xx}
=8\mu Lu_c\tan q/q.
$$

There is therefore no leading-order conservation cancellation.

---

# Part VIII — error budget

## 16. Controlled approximations

The explicit source is accurate in the regime

$$
\boxed{
\frac{|u_c|}{L}\ll1,
}
$$

$$
\boxed{
q=\frac{\omega L}{c_s}\ll1,
}
$$

$$
\boxed{
\beta=\frac{\omega L}{c}\ll1,
}
$$

and weak self-gravity

$$
\boxed{
\mathcal C
=\frac{2GM}{c^2L}\ll1.
}
$$

Leading corrections are:

### finite spoke inertia

Explicitly included; endpoint-only formulas differ by

$$
O(q^2).
$$

### kinetic/internal elastic energy in $T^{00}$

Relative size is

$$
O(v^2/c^2)
$$

or elastic-energy/rest-energy order. Under the mirrored branch symmetry these energy densities are branch even at first order, so they do not generate the leading branch-difference quadrupole.

### finite source retardation / higher multipoles

The source has inversion symmetry and purely radial motion. Odd mass multipoles and leading current multipoles vanish by symmetry. The first finite-size radiative corrections are therefore expected beyond the leading quadrupole at parametrically higher order in

$$
\beta.
$$

### gravitational binding energy

Neglected at relative order controlled by

$$
\mathcal C.
$$

### finite hub size

Controlled by

$$
r_h/L
$$

and the branch dependence of hub energy. In the ideal symmetric controller, total hub/control energy is branch common.

---

## 17. Consequence for the previously derived source formulas

The endpoint-only formulas in `QUANTIZED_PLUS_MODE_SOURCE.md` should now be interpreted as the

$$
q\to0
$$
limit of this finite-support conserved source.

For classical prescribed outer displacement $u_c$,

$$
\boxed{
\Delta Q_{xx}^{\rm exact\,spoke}
=
\Delta Q_{xx}^{\rm endpoint}
\frac{\tan q}{q}.
}
$$

For the quantized transition matrix element, replace the endpoint-only value by

$$
\boxed{
q_{01}^{\rm tot}
=4\mu L
\frac{\tan q}{q}
\sqrt{\frac{\hbar}{2M_{\rm eff}\omega}},
}
$$

with

$$
M_{\rm eff}
=4\mu\left[
\frac12+rac{q}{\sin2q}
\right].
$$

The earlier formulas remain valid to relative accuracy

$$
O(q^2)
$$

in the endpoint-dominated regime.

---

# Part IX — adversarial verdict

## 18. Can the actuator cancel the claimed gravitational radiation?

For a generic unspecified actuator: **possibly**. That was a real loophole.

For the explicit isolated four-spoke elastic architecture constructed here: **not at leading order**.

The complete support rest-mass contribution is calculable and has the same plus-quadrupole sign as the endpoint contribution:

$$
\boxed{
\Delta Q_{xx}
=8\mu L u_c\frac{\tan q}{q}.
}
$$

The central control/work reservoir can be exactly branch common under the controlled-parity symmetry of

$$
H=H_m+H_c-\sigma_z g(q_c)u.
$$

The stress tensor is required for conservation, but conservation converts its integrated radiative effect into the second derivative of the **same total energy quadrupole** rather than producing an extra cancellation term.

Thus the strongest source-level objection identified in the previous audit is closed at the level needed for a controlled nonrelativistic quadrupole Gedanken source.

---

## 19. What is still not claimed

This note does not claim

- a complete microscopic material realization;
- a fully relativistic exact hyperelastic solution for the driven four-spoke source;
- negligible actuator corrections for arbitrary materials or arbitrary mode frequency;
- experimental feasibility.

A fully covariant version can be built from a relativistic hyperelastic action; relativistic elasticity provides consistent stress-energy tensors and causal longitudinal propagation. The present derivation is the controlled low-velocity/weak-field limit needed to decide the **cancellation question**.

---

## 20. Next step

Update the source and gravity-paper core to use the finite-support parameter

$$
q=\omega L/c_s
$$

and replace endpoint-only quadrupole/linewidth expressions by either

1. the exact four-spoke factors above; or
2. endpoint formulas explicitly labeled as the controlled $q\ll1$ limit.

Then re-audit the emitted coherent-graviton norm and source→receiver coupling with the corrected transition matrix element.
