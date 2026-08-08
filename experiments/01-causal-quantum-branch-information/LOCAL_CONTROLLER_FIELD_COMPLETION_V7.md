# Local Controller-Field Completion of the V7 Encoder

**Date:** 2026-08-08  
**Status:** **LOCAL FIELD COMPLETION — REMOVES REMOTE APPEARANCE OF THE HUB OPERATOR FROM THE DISTRIBUTED ACTUATOR**

## 1. Why this refinement is needed

The modal encoder

$$
H_{\rm enc}=\hbar g\sigma_z(a^\dagger w+a w^\dagger)
$$

is useful, but its distributed elastic shorthand

$$
\frac12EA
\left[
\partial_x\xi_a
-\epsilon_a\sigma_z\lambda X_C\chi(x)
\right]^2
$$

must not be interpreted as a microscopic Hamiltonian density containing the hub qubit operator $\sigma_z$ at every remote material point.

A literal local completion introduces controller/bus field degrees of freedom that carry the branch command away from the hub.

---

# 2. Local controller bus

Introduce one local controller field $\Phi_a(x,t)$ on each spoke. A minimal lossless continuum model is

$$
\boxed{
H_{\Phi}
=\sum_a\int_0^Ldx
\left[
\frac{\Pi_a^2}{2\rho_c}
+\frac{\rho_cv_c^2}{2}(\partial_x\Phi_a)^2
\right],
}
$$

with

$$
v_c\le c.
$$

The reference qubit and compact work mode couple to the controller field only at the hub, $x=0$, through some local Hamiltonian

$$
H_{S w\Phi}^{\rm hub}.
$$

Its detailed microscopic form is not needed for the propagation argument; what matters is that in the two logical branches it launches opposite controller-field amplitudes.

For an outgoing narrowband command, the branch-conditioned classical/coherent solution is

$$
\boxed{
\Phi_a^{(s)}(x,t)
=sX_C\!\left(t-\frac{x}{v_c}\right),
\qquad s=\pm1,
}
$$

up to the chosen boundary/reflection geometry.

The branch sign has therefore been transported by a physical local field. No remote material element couples directly to the hub operator $\sigma_z$.

---

# 3. Local spoke coupling

The elastic eigenstrain density is now

$$
\boxed{
\mathcal E_a(x,t)
=\frac12EA
\left[
\partial_x\xi_a(x,t)
-\epsilon_a\lambda\chi(x)\Phi_a(x,t)
\right]^2,
}
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

The interaction is manifestly local: at $(x,t)$ the elastic medium couples only to the controller field at the same $(x,t)$.

For the mirrored branch trajectory

$$
\xi_a^{(s)}(x,t)
=\epsilon_asu(t)f_q(x),
$$

and the retarded controller solution above,

$$
\partial_x\xi_a^{(s)}
-\epsilon_a\lambda\chi\Phi_a^{(s)}
=
\epsilon_as
\left[
u f_q'
-\lambda\chi X_C(t-x/v_c)
\right].
$$

Hence

$$
\boxed{
\mathcal E_a^{(+)}(x,t)
=\mathcal E_a^{(-)}(x,t)
}
$$

pointwise even after finite controller propagation is restored.

Thus the equal-energy part of the charge audit survives the local field completion.

---

# 4. Projection onto the elastic plus mode

Expand

$$
\xi_a(x,t)=\epsilon_a u(t)f_q(x).
$$

The bilinear elastic--controller interaction becomes

$$
\boxed{
H_{u\Phi}(t)
=-4EA\lambda u(t)
\int_0^Ldx\,
\chi(x)f_q'(x)\Phi(x,t),
}
$$

where the four identical spoke controller fields have been written as one symmetric plus-sector field $\Phi$.

This Hamiltonian is local before mode projection; the apparent globality enters only after selecting the collective normal modes $u$ and $\Phi$.

For branch $s$,

$$
H_{u\Phi}^{(s)}(t)
=-4EA\lambda s u(t)
\int_0^Ldx\,
\chi(x)f_q'(x)
X_C(t-x/v_c).
$$

This is the branch-conditioned retarded expression used in the earlier finite-speed audit, now derived from a genuinely local field model.

---

# 5. Causal form factor

Define

$$
h(x)=\chi(x)f_q'(x),
$$

$$
\mathcal J_0=\int_0^Ldx\,h(x),
$$

and for $h(x)\ge0$,

$$
w(x)=h(x)/\mathcal J_0.
$$

For

$$
X_C(t)=X_0e^{-i\omega t},
$$

the projected local controller amplitude is multiplied by

$$
\boxed{
F_c(\omega)
=\int_0^Ldx\,w(x)e^{i\omega x/v_c}.
}
$$

Therefore the mode-reduced coupling has

$$
\boxed{
g_{\rm eff}=g_0F_c.}
$$

Let

$$
q_c=\omega L/v_c.
$$

Then

$$
\boxed{
\arg F_c
=\omega\frac{\bar x}{v_c}+O(q_c^3),
}
$$

and

$$
\boxed{
|F_c|^2
=1-q_c^2\operatorname{Var}_w(x/L)+O(q_c^4).
}
$$

For a uniform overlap,

$$
\boxed{
F_c
=e^{iq_c/2}\operatorname{sinc}(q_c/2),
}
$$

$$
\boxed{
|F_c|^2
=1-\frac{q_c^2}{12}+O(q_c^4).
}
$$

Thus the same finite-speed form-factor result survives the local field completion.

---

# 6. Emergence of the modal sign-controlled beam splitter

The local hub interaction prepares opposite coherent amplitudes of the relevant controller-bus normal mode in the two logical sectors.

Project the controller bus onto the dominant narrowband work mode $w$ and the elastic displacement onto $a$.

After the finite propagation phase is absorbed into the definition/timing of the work mode and after the resonant RWA, the effective two-mode dynamics take the form

$$
\boxed{
H_{\rm enc}^{\rm eff}
=\hbar g_{\rm eff}\sigma_z
(a^\dagger w+a w^\dagger)
+H_{\rm corr}.
}
$$

The factor $\sigma_z$ appears here because this is the **projected code-sector Hamiltonian after the local hub interaction and controller-field propagation have been reduced to their dominant coherent work mode**.

It is not a microscopic operator acting at every spoke point.

The correction $H_{\rm corr}$ contains

- higher controller-bus modes;
- higher elastic modes;
- finite-bandwidth dispersion;
- counter-rotating terms;
- controller losses.

In the controlled narrowband regime these are perturbative corrections or additional explicit source ports.

---

# 7. Controller field as part of the branch record

During encoding the bus field can carry branch information.

That is not a problem: the controller is allowed to be entangled/correlated with the logical branch during the local operation.

For the post-handoff virtual-mode channel construction, however, the controller bus must be returned to a branch-common state.

A closed implementation can accomplish this by

1. a standing-wave/cavity-like controller mode;
2. reflection and coherent reabsorption at the hub;
3. another lossless state-transfer architecture.

The minimum clearing overhead is architecture dependent but scales as

$$
\boxed{
T_{\rm clear}=O(L/v_c)
}
$$

for one-way clearing and potentially

$$
O(2L/v_c)
$$

for a round-trip reabsorption architecture.

If some branch-dependent controller field is instead lost irreversibly, it becomes an additional which-branch environment. In the linear amplitude-damping model it is simply another source loss port and reduces

$$
\beta_{g,A}.
$$

If it causes non-Gaussian dephasing, it belongs to the separate source-coherence channel already distinguished in V7.

Thus controller cleanup is not hidden from the link budget.

---

# 8. Charge audit with the controller field

The two controller-field branch solutions satisfy

$$
\Phi_-=-\Phi_+
$$

after common fields are removed.

The free controller-field energy, momentum, angular momentum, and center-of-energy generators are quadratic in $\Phi$ and $\Pi$.

Therefore their diagonal Poincare charges are identical between branches.

The elastic--controller interaction energy is also branch common pointwise, as shown above.

The controller field therefore fits the full-system equal-charge audit:

$$
\boxed{
\Delta P_\Phi^\mu=0,
\qquad
\Delta M_\Phi^{\mu\nu}=0
}
$$

to the working linear order, even while it temporarily carries distinguishable branch information.

---

# 9. Causality

A controller disturbance launched at source center $\mathbf x_0$ reaches source point $\mathbf x$ no earlier than

$$
t_s+\frac{|\mathbf x-\mathbf x_0|}{v_c}.
$$

The earliest gravitational signal from that point can reach receiver point $\mathbf y$ only after

$$
t_{\rm arr}
\ge
 t_s
+\frac{|\mathbf x-\mathbf x_0|}{v_c}
+\frac{|\mathbf y-\mathbf x|}{c}.
$$

Because

$$
v_c\le c,
$$

$$
\boxed{
 t_{\rm arr}-t_s
\ge
\frac{|\mathbf y-\mathbf x_0|}{c}.
}
$$

The explicit local controller therefore strengthens, rather than threatens, the retarded causal-front statement.

---

# 10. Relation to the spoke long-wavelength limit

If

$$
v_c\sim c_s,
$$

then

$$
q_c=\omega L/v_c
\sim
q=\omega L/c_s.
$$

The source already assumes

$$
q\ll1.
$$

Hence the same long-wavelength regime controls

- finite spoke-mass corrections;
- finite controller-propagation corrections;
- validity of the simple projected beam-splitter encoder.

If

$$
v_c>c_s,
$$

the controller locality error is smaller still.

---

# 11. Final interpretation

The strongest local statement is now:

> **The V7 sign-controlled normal-mode encoder is the narrowband reduction of a strictly local hub-to-controller-field-to-elastic-source architecture. The logical branch is injected into the controller bus only at the hub; it propagates at finite speed $v_c\le c$; each spoke couples only to its local controller field; and projection onto the dominant controller/source normal modes yields the effective $\sigma_z$ beam-splitter Hamiltonian. Finite propagation produces a delay and an $O(q_c^2)$ coupling correction, plus an $O(L/v_c)$ cleanup overhead, but does not alter the serial gravitational link factorization.**

This removes the remaining appearance of instantaneous distributed action from the V7 source model.
