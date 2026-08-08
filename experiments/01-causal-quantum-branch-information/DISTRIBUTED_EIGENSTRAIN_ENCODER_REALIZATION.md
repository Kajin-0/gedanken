# Distributed Eigenstrain Realization of the Sign-Controlled Source Encoder

**Date:** 2026-08-07  
**Status:** **CONTINUUM REALIZATION — THE NORMAL-MODE ENCODER ARISES FROM A LOCAL ELASTIC ENERGY FUNCTIONAL WITH POINTWISE BRANCH-EVEN ACTUATOR ENERGY**

## 1. Purpose

`EXACT_LOCAL_GAUSSIAN_SOURCE_ENCODER.md` closes the controller-factorization problem at the normal-mode level using

$$
H_{\rm enc}
=\hbar g\sigma_z(a^\dagger c+a c^\dagger).
$$

A remaining physical question is whether such a coupling can arise from the same internally conserved four-spoke elastic source rather than from an abstract external force acting directly on a normal coordinate.

It can.

The required interaction appears directly by allowing a dynamical internal actuator mode to modulate the preferred longitudinal eigenstrain of the four spokes with the plus-mode sign pattern.

---

# 2. Four-spoke geometry

Label the four spokes by $a$ and define

$$
\epsilon_a
=\begin{cases}
+1,&\text{$x$-axis spokes},\\
-1,&\text{$y$-axis spokes}.
\end{cases}
$$

The mechanical plus displacement field is

$$
\boxed{
\xi_a(x)
=\epsilon_a u f_q(x),
}
$$

with

$$
f_q(x)=\frac{\sin(qx/L)}{\sin q}.
$$

Thus

$$
\partial_x\xi_a
=\epsilon_a u f_q'(x).
$$

---

# 3. Dynamical actuator eigenstrain

Introduce one internal actuator collective coordinate

$$
\boxed{X_c}
$$

with its own conjugate momentum and autonomous Hamiltonian

$$
H_c(X_c,P_c).
$$

Let the actuator produce the signed eigenstrain field

$$
\boxed{
\epsilon_{a,0}(x)
=\epsilon_a\sigma_z
\lambda X_c\chi(x),
}
$$

where

- $\lambda$ converts actuator displacement to strain;
- $\chi(x)$ is a dimensionless spatial actuator profile;
- $\sigma_z$ is the retained source-reference/control degree of freedom.

The local elastic energy of spoke $a$ is

$$
\boxed{
H_{{\rm el},a}
=\frac12EA
\int_0^Ldx\,
\left[
\partial_x\xi_a
-\epsilon_a\sigma_z
\lambda X_c\chi(x)
\right]^2.
}
$$

This is a standard eigenstrain structure: the actuator changes the local preferred strain rather than applying a nonconserved external point force.

---

# 4. Projection onto the plus mode

Substitute

$$
\partial_x\xi_a
=\epsilon_a u f_q'(x).
$$

Then

$$
H_{{\rm el},a}
=\frac12EA
\int_0^Ldx\,
\left[
\epsilon_a u f_q'
-\epsilon_a\sigma_z
\lambda X_c\chi
\right]^2.
$$

Since

$$
\epsilon_a^2=1,
$$

$$
H_{{\rm el},a}
=\frac12EA
\int_0^Ldx\,
\left[
 u f_q'
-\sigma_z\lambda X_c\chi
\right]^2.
$$

Expand:

$$
H_{{\rm el},a}
=
\frac12EAu^2
\int(f_q')^2dx
-EA\sigma_z\lambda X_cu
\int\chi f_q'dx
+
\frac12EA\lambda^2X_c^2
\int\chi^2dx.
$$

All four spokes contribute the same projected expression.

Define the overlap

$$
\boxed{
\mathcal J
\equiv
\int_0^Ldx\,
\chi(x)f_q'(x).
}
$$

Then the total cross interaction is

$$
\boxed{
H_{\rm cross}
=-4EA\lambda\mathcal J\,
\sigma_zX_cu.
}
$$

This is the desired bilinear source/controller coupling.

---

# 5. Branch-independent actuator self-energy

The eigenstrain-squared term is

$$
\boxed{
H_{c,{\rm el}}
=2EA\lambda^2X_c^2
\int_0^Ldx\,\chi^2(x).
}
$$

It contains

$$
\sigma_z^2=1
$$

and is therefore branch independent.

It simply renormalizes the autonomous controller potential/frequency.

No branch-dependent external work term is required by the effective elastic Hamiltonian.

---

# 6. Pointwise branch-even elastic energy

For branch

$$
\sigma_z=s=\pm1,
$$

and the mirrored source solution

$$
u_s=su_+,
$$

the local strain mismatch is

$$
\partial_x\xi_a^{(s)}
-\epsilon_a s\lambda X_c\chi
=
\epsilon_as
\left[
 u_+f_q'-\lambda X_c\chi
\right].
$$

Therefore the elastic energy density is

$$
\boxed{
\mathcal E_{{\rm el},a}^{(s)}(x)
=
\frac12EA
\left[
 u_+f_q'(x)
-\lambda X_c\chi(x)
\right]^2,
}
$$

which is **pointwise independent of $s$**.

Likewise the source kinetic energy density is branch even because

$$
(\dot\xi_a^{(s)})^2
=(\dot\xi_a^{(+)})^2.
$$

If the actuator coordinate $X_c$ follows the same quantum trajectory in both branches, its own kinetic and potential energy densities are also branch common.

Thus the intended branch difference in leading $T^{00}$ remains the mirrored spatial redistribution of the source rest mass already included in the conserved quadrupole calculation.

---

# 7. Quantization

Quantize

$$
\boxed{
u
=u_{\rm zpf}(a+a^\dagger),}
$$

and

$$
\boxed{
X_c
=X_{\rm zpf}(c+c^\dagger).
}
$$

Then

$$
H_{\rm cross}
=-\hbar g_0\sigma_z
(a+a^\dagger)(c+c^\dagger),
$$

with

$$
\boxed{
g_0
=
\frac{4EA\lambda\mathcal J
u_{\rm zpf}X_{\rm zpf}}
{\hbar}.}
$$

For resonant source and controller modes with

$$
g_0\ll\omega,
$$

the rotating-wave approximation gives

$$
\boxed{
H_{\rm cross}^{\rm RWA}
=-\hbar g_0\sigma_z
(a^\dagger c+a c^\dagger).
}
$$

This is precisely the encoder Hamiltonian of

- `EXACT_LOCAL_GAUSSIAN_SOURCE_ENCODER.md`.

The overall sign can be absorbed into the controller phase convention.

---

# 8. Uniform eigenstrain special case

If

$$
\chi(x)=1,
$$

then

$$
\mathcal J
=
\int_0^L f_q'(x)dx
=f_q(L)-f_q(0)
=1.
$$

Hence

$$
\boxed{
H_{\rm cross}
=-4EA\lambda\sigma_zX_cu.
}
$$

and

$$
\boxed{
g_0
=
\frac{4EA\lambda
u_{\rm zpf}X_{\rm zpf}}
{\hbar}.}
$$

No endpoint force has been inserted by hand; the coupling comes from the distributed local strain energy of the spokes.

---

# 9. More realistic actuator profile

A physical actuator need not impose uniform eigenstrain.

For arbitrary

$$
\chi(x),
$$

only the overlap

$$
\mathcal J
=
\int\chi f_q'dx
$$

enters the leading normal-mode coupling.

Thus the controller can be

- distributed piezoelectric-like strain;
- an internal active-material mode;
- another longitudinal collective mode;
- a spatially localized strain region with nonzero overlap with the source normal mode.

The modal encoder survives with the replacement

$$
g_0\propto\mathcal J.
$$

A detailed material implementation is not required for the conservation argument.

---

# 10. Local force balance

The source force density follows from the divergence of the local elastic stress associated with

$$
\partial_x\xi_a-\epsilon_{a,0}.
$$

Endpoint acceleration is supplied by the corresponding internal boundary traction.

Opposite spokes have equal and opposite vector tractions at the central junction.

Therefore the ideal plus encoder preserves

$$
\boxed{
\mathbf F_{\rm hub}=0,
\qquad
\boldsymbol\tau_{\rm hub}=0.
}
$$

No external center-of-mass support force is needed.

This is the same local-conservation structure used in

- `CONSERVED_SOURCE_ACTUATOR_AUDIT.md`.

---

# 11. Stress does not add a separate hidden radiation term

The branch-dependent elastic stress is essential for local momentum conservation.

For the complete conserved source,

$$
\boxed{
\ddot I_{ij}
=2\int d^3x\,T^{ij}.
}
$$

Thus the stress representation and total-energy-quadrupole representation are not independent radiation sources that must be summed separately.

Any cancellation must appear in the complete branch-difference

$$
T^{00}
$$
quadrupole.

Because the actuator elastic/kinetic energy above is branch even pointwise in the ideal mirrored solution, it does not generate a leading branch-odd energy quadrupole that cancels the source rest-mass term.

---

# 12. Distributed actuator versus compact-hub bound

A uniform or extended eigenstrain actuator occupies a region of order $L$, so one should **not** apply the compact-hub estimate

$$
|\Delta Q^{\rm ctrl}|
\lesssim r_h^2E_{\rm ctrl}/c^2
$$

to that distributed portion.

Instead its leading protection is stronger: in the ideal controlled-parity solution its local energy density is branch identical, so

$$
\boxed{
\Delta T^{00}_{\rm actuator}(x)=0
}
$$

at the retained nonrelativistic order.

The compact-hub bound remains appropriate only for residual localized electronics/junction structure that does not obey the exact distributed symmetry.

---

# 13. Causality inside the finite source

The effective collective coordinate $X_c$ must arise from a causal physical actuator field or internal mode.

The continuum Hamiltonian above should therefore be interpreted as a projection of a local finite-speed actuator dynamics, not as an instruction that a pointlike qubit instantaneously changes the rest strain everywhere along a macroscopic spoke.

For the Gedanken protocol it is sufficient to take the encoder support to be the complete compact source worldtube of size $L$.

Any finite internal propagation time is then part of the local preparation duration.

The remote causal bound is measured from the earliest spacetime support of that source operation.

A microscopic actuator-field model would refine the internal timing but does not introduce a conservation obstruction.

---

# 14. Counter-rotating correction

The exact continuum coupling before RWA is

$$
H_{\rm cross}
=-\hbar g_0\sigma_z
(a+a^\dagger)(c+c^\dagger).
$$

The state-swap solution assumes

$$
\boxed{g_0\ll\omega.}
$$

Counter-rotating corrections are therefore controlled parametrically by

$$
O(g_0/\omega)
$$

at the Hamiltonian/amplitude level, with detailed coefficients depending on pulse duration and detuning.

The desired hierarchy remains

$$
\boxed{
\kappa_A\ll g_0\ll\omega.
}
$$

Because the gravitational linewidth is extremely weak in the intended regime, this hierarchy is formally broad.

---

# 15. Relation to the earlier autonomous force Hamiltonian

`CONSERVED_SOURCE_ACTUATOR_AUDIT.md` introduced the projected form

$$
H
=H_m+H_c-\sigma_zg(q_c)u.
$$

The present construction supplies an explicit elastic origin for a bilinear version of that coupling:

$$
\boxed{
g(q_c)u
\longleftrightarrow
4EA\lambda\mathcal J\,X_cu.}
$$

Thus the exact Gaussian swap encoder is not disconnected from the conserved finite-spoke source. It is the resonant quantum version of the same branch-controlled internal eigenstrain mechanism.

---

# 16. What remains unmodeled

This note still does not specify

- a particular material that realizes the sign-controlled eigenstrain;
- the microscopic interaction that couples a localized two-level reference to a distributed actuator field;
- finite-temperature actuator noise;
- nonlinear elasticity at large strain;
- a fully covariant relativistic active-material stress tensor.

Those are implementation refinements.

The present result is narrower and sufficient for the current theoretical source audit:

> a local conserved elastic energy functional exists whose normal-mode projection yields the exact sign-controlled Gaussian encoder while keeping the ideal actuator energy density branch common.

---

# 17. Adversarial verdict

The normal-mode encoder no longer relies on an unexplained force directly applied to the abstract plus coordinate.

Within the controlled elastic model, it can be realized by distributed internal eigenstrain with

$$
\boxed{
H_{\rm cross}
=-4EA\lambda\mathcal J\,
\sigma_zX_cu,
}
$$

and

$$
\boxed{
\mathcal E_{\rm actuator}^{(+)}(x)
=
\mathcal E_{\rm actuator}^{(-)}(x)
}
$$

pointwise for the mirrored source solution.

The strongest remaining source-side uncertainties are therefore microscopic implementation and relativistic active-material completion, not a leading-order missing actuator force or unavoidable controller branch record.
