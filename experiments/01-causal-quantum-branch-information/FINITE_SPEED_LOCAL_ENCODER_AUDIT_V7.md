# Finite-Speed Local Encoder Audit for V7

**Date:** 2026-08-08  
**Status:** **CAUSAL LOCAL-CONTROL CORRECTION — GLOBAL MODAL ENCODER RECOVERED AS A CONTROLLED NARROWBAND LIMIT**

## 1. Problem

The manuscript uses the effective normal-mode Hamiltonian

$$
\boxed{
H_{\rm enc}
=\hbar g\sigma_z(a^\dagger w+a w^\dagger).
}
$$

The elastic realization is written as a distributed eigenstrain interaction

$$
\mathcal E_a
=\frac12EA
\left[
\partial_x\xi_a
-\epsilon_a\sigma_z\lambda X_C\chi(x)
\right]^2.
$$

Taken literally with the same controller coordinate $X_C(t)$ at every $x$ at the same laboratory time, this is a projected/modal description rather than a microscopic local switching law.

A real branch-control command originating near the hub must propagate through the finite source at a speed

$$
\boxed{v_c\le c.}
$$

For a mechanical/electromechanical actuator bus one may have

$$
v_c\sim c_s
$$

or another material/control propagation speed.

The question is whether restoring this finite propagation invalidates the V7 source construction or only produces a controlled delay/form-factor correction.

The answer is the latter in the narrowband regime.

---

# 2. Causal distributed controller kernel

Let the branch-control signal originate at the hub, $x=0$, and propagate outward along each spoke.

Replace the instantaneous controller field by the retarded local value

$$
\boxed{
X_C(x,t)
=X_C\!\left(t-\frac{x}{v_c}\right).
}
$$

The local eigenstrain interaction density becomes

$$
\boxed{
\mathcal E_a(x,t)
=\frac12EA
\left[
\partial_x\xi_a(x,t)
-\epsilon_a\sigma_z\lambda\chi(x)
X_C\!\left(t-\frac{x}{v_c}\right)
\right]^2.
}
$$

This has strictly retarded support: the actuator at material point $x$ cannot know the branch command before

$$
t-t_s\ge x/v_c.
$$

Project the elastic displacement onto the plus mode,

$$
\xi_a(x,t)=\epsilon_a u(t)f_q(x).
$$

The bilinear interaction is then

$$
H_{\rm int}(t)
=-4EA\lambda\sigma_z u(t)
\int_0^L dx\,
\chi(x)f_q'(x)
X_C\!\left(t-\frac{x}{v_c}\right).
$$

Define

$$
h(x)\equiv\chi(x)f_q'(x),
$$

$$
\mathcal J_0\equiv\int_0^L dx\,h(x).
$$

For the fundamental endpoint-dominated spoke mode $0<q<\pi/2$, $f_q'(x)>0$. Choosing a nonnegative actuator profile $\chi(x)$ therefore permits

$$
h(x)\ge0.
$$

Define the normalized control-overlap weight

$$
\boxed{
w(x)=\frac{h(x)}{\mathcal J_0},
\qquad
\int_0^Ldx\,w(x)=1.
}
$$

Then

$$
\boxed{
H_{\rm int}(t)
=-4EA\lambda\mathcal J_0\,\sigma_z u(t)X_{\rm eff}(t),
}
$$

where

$$
\boxed{
X_{\rm eff}(t)
=\int_0^Ldx\,w(x)
X_C\!\left(t-\frac{x}{v_c}\right).
}
$$

Thus the only change is that the source mode responds to a causal weighted convolution of the controller field rather than its instantaneous hub value.

---

# 3. Frequency-domain form factor

For a narrowband controller component

$$
X_C(t)=X_0e^{-i\omega t},
$$

one has

$$
X_{\rm eff}(t)
=X_0e^{-i\omega t}F_c(\omega),
$$

with the exact causal form factor

$$
\boxed{
F_c(\omega)
=\int_0^Ldx\,w(x)
e^{i\omega x/v_c}.
}
$$

Define

$$
\boxed{
q_c\equiv\frac{\omega L}{v_c}.}
$$

The original instantaneous distributed coupling corresponds to

$$
F_c\to1.
$$

The finite-speed effective beam-splitter coupling is therefore

$$
\boxed{
g(\omega)=g_0F_c(\omega),}
$$

where $g_0$ is the coupling obtained from the static overlap $\mathcal J_0$.

---

# 4. Controlled small-$q_c$ expansion

Define moments of the normalized overlap profile,

$$
\bar x
=\int_0^Ldx\,w(x)x,
$$

$$
\sigma_x^2
=\int_0^Ldx\,w(x)(x-\bar x)^2.
$$

Expanding the exact form factor gives

$$
F_c(\omega)
=1+i\frac{\omega\bar x}{v_c}
-\frac{\omega^2}{2v_c^2}
\langle x^2\rangle_w
+O(q_c^3).
$$

Since $F_c(-\omega)=F_c^*(\omega)$ for real $w(x)$, its magnitude squared is even in frequency. Therefore

$$
\boxed{
|F_c(\omega)|^2
=1-rac{\omega^2\sigma_x^2}{v_c^2}
+O(q_c^4).
}
$$

Equivalently,

$$
\boxed{
|F_c|^2
=1-q_c^2\,
\operatorname{Var}_w(x/L)
+O(q_c^4).
}
$$

The phase is

$$
\boxed{
\arg F_c
=\omega\frac{\bar x}{v_c}
+O(q_c^3).
}
$$

Therefore finite-speed actuation has two leading effects:

1. a **group/command delay**
   $$
   \boxed{\tau_c^{\rm ctrl}=\bar x/v_c;}
   $$
2. a **coupling-strength reduction only at second order**,
   $$
   \boxed{
   \frac{|g(\omega)|^2}{g_0^2}
   =1-q_c^2\operatorname{Var}_w(x/L)+O(q_c^4).
   }
   $$

This is the main locality result.

---

# 5. General bound on the amplitude correction

For any normalized nonnegative weight supported on

$$
0\le x/L\le1,
$$

Popoviciu's variance bound gives

$$
\operatorname{Var}_w(x/L)\le\frac14.
$$

Hence

$$
\boxed{
1-|F_c|^2
\le\frac{q_c^2}{4}+O(q_c^4).
}
$$

Thus no detailed actuator profile is required to guarantee a controlled local-coupling limit when

$$
\boxed{q_c\ll1.}
$$

---

# 6. Uniform-overlap control

In the long-wavelength spoke limit,

$$
q=\frac{\omega L}{c_s}\ll1,
$$

one has approximately

$$
f_q'(x)\simeq1/L.
$$

For a nearly uniform actuator profile,

$$
w(x)\simeq1/L.
$$

Then the form factor is elementary:

$$
F_c(\omega)
=\frac1L\int_0^Ldx\,e^{i\omega x/v_c}.
$$

Therefore

$$
\boxed{
F_c
=e^{iq_c/2}
\operatorname{sinc}\!\left(\frac{q_c}{2}\right),
}
$$

where

$$
\operatorname{sinc}z=\frac{\sin z}{z}.
$$

Thus

$$
\boxed{
|F_c|^2
=\operatorname{sinc}^2\!\left(\frac{q_c}{2}\right)
=1-\frac{q_c^2}{12}+O(q_c^4),
}
$$

and

$$
\boxed{
\tau_c^{\rm ctrl}=\frac{L}{2v_c}.
}
$$

This provides a concrete benchmark correction.

---

# 7. Time-domain slow-envelope expansion

The exact local control seen by the plus mode is

$$
X_{\rm eff}(t)
=\int_0^Ldx\,w(x)X_C(t-x/v_c).
$$

Define

$$
\bar\tau=\bar x/v_c,
$$

$$
\sigma_\tau^2=\sigma_x^2/v_c^2.
$$

Expanding around the mean delay gives

$$
\boxed{
X_{\rm eff}(t)
=X_C(t-\bar\tau)
+\frac{\sigma_\tau^2}{2}
\ddot X_C(t-\bar\tau)
+\cdots.
}
$$

The first-derivative distortion vanishes by expansion about the mean.

Hence for any controller envelope whose characteristic bandwidth is

$$
B_c\ll v_c/L,
$$

the distributed local actuator is equivalent to

1. a fixed time delay;
2. a small $O[(B_cL/v_c)^2]$ waveform distortion.

---

# 8. Recovery of the modal beam-splitter Hamiltonian

Quantize the mechanical plus coordinate and the branch-common work/controller coordinate,

$$
u=u_{\rm zpf}(a+a^\dagger),
$$

$$
X_C=X_{\rm zpf}(w+w^\dagger).
$$

After absorbing the control-form-factor phase into the definition of $w$ or into the interaction timing, the resonant RWA gives

$$
\boxed{
H_{\rm enc}^{\rm eff}
=\hbar g_{\rm eff}\sigma_z
(a^\dagger w+a w^\dagger)
+H_{\rm corr},
}
$$

with

$$
\boxed{
|g_{\rm eff}|^2
=g_0^2
\left[
1-q_c^2\operatorname{Var}_w(x/L)
+O(q_c^4)
\right].
}
$$

The correction Hamiltonian $H_{\rm corr}$ contains

- higher controller/spoke modes;
- finite-bandwidth temporal distortion;
- counter-rotating terms;
- any residual actuator-profile mismatch.

Therefore the global beam-splitter Hamiltonian used in V7 is not interpreted as a fundamental instantaneous action at a distance. It is the **normal-mode low-frequency reduction of a causal distributed controller**.

---

# 9. Relation to the existing spoke parameter $q$

If the control signal propagates at approximately the longitudinal sound speed,

$$
v_c\simeq c_s,
$$

then

$$
\boxed{q_c\simeq q.}
$$

The V7 source already assumes

$$
q=\omega L/c_s\ll1.
$$

Thus the same endpoint-dominated, long-wavelength elastic regime that controls the spoke quadrupole correction also controls the locality error of a mechanically propagated actuator command.

If the control bus is faster than the mechanical sound speed,

$$
v_c>c_s,
$$

then

$$
q_c<q
$$

and the local-control approximation is even better.

---

# 10. Handoff-time correction

A physical distributed controller cannot be declared fully branch common until all branch-sensitive controller excitations inside the source have been cleared or coherently reabsorbed.

If the last hub control change occurs at time $T$, a one-way distributed field cannot have cleared a spoke before roughly

$$
T+L/v_c.
$$

A reflected/reabsorbed bus may require an architecture-dependent round-trip overhead of order

$$
2L/v_c.
$$

Thus the exact modal handoff time $T_*$ should be interpreted as the leading low-frequency handoff time, with a physical local implementation satisfying schematically

$$
\boxed{
T_*^{\rm local}
=T_*^{\rm modal}
+O(L/v_c).
}
$$

This does not imply an $O(L/v_c)$ change in the integrated branch-distance efficiency. It shifts and slightly reshapes the waveform.

In the RWA regime

$$
g\ll\omega
$$

and for

$$
q_c=\omega L/v_c\ll1,
$$

one has

$$
\frac{L/v_c}{T_*^{\rm modal}}
\sim
O\!\left(q_c\frac{g}{\omega}\right)
\ll1.
$$

Therefore the local-control clearing time is parametrically short compared with the resonant encoder duration in the same regime where the modal Hamiltonian is valid.

---

# 11. Causal arrival bound

Let the local branch command originate at source center $\mathbf x_0$ at time $t_s$.

A material/source point $\mathbf x$ can become branch dependent no earlier than

$$
t_s+rac{|\mathbf x-\mathbf x_0|}{v_c}.
$$

A gravitational disturbance emitted there reaches receiver point $\mathbf y$ no earlier than

$$
t_{\rm arr}
\ge
 t_s
+\frac{|\mathbf x-\mathbf x_0|}{v_c}
+\frac{|\mathbf y-\mathbf x|}{c}.
$$

Since

$$
v_c\le c,
$$

$$
\frac{|\mathbf x-\mathbf x_0|}{v_c}
\ge
\frac{|\mathbf x-\mathbf x_0|}{c}.
$$

Therefore by the triangle inequality,

$$
\boxed{
 t_{\rm arr}-t_s
\ge
\frac{|\mathbf y-\mathbf x_0|}{c}.
}
$$

Thus restoring finite-speed local actuation can only delay the signal relative to the center-origin light-cone bound; it cannot create an earlier gravitational front.

---

# 12. Consequence for the V7 quantum-link budget

The complete V7 link budget depends on the actual normalized source waveform

$$
f(t).
$$

Replacing an instantaneous distributed controller by a finite-speed local controller changes

1. the source waveform phase/time origin;
2. the exact encoder precursor;
3. the controller-empty handoff time;
4. the temporal loading factor $\mathcal T_f$;
5. the effective source coupling by the small form factor $F_c$.

It does **not** introduce a new serial free-space efficiency factor.

After the complete waveform is renormalized and the source branching is computed using the actual physical port rates, the post-handoff link retains the same structure:

$$
\boxed{
\tau_c(t)
=\beta_{g,A}\eta_{\rm store}\beta_{g,B}\mathcal T_f(t),
}
$$

with the finite-speed actuator dependence absorbed into

- the physical $\beta_{g,A}$ if the actuator changes source loss channels;
- the actual normalized waveform $f$;
- the corrected $\mathcal T_f$;
- controlled $O(q_c^2)$ changes of the encoder coupling/handoff.

No new power of distance, compactness, or gravitational coupling appears.

---

# 13. Strongest manuscript statement

The V7 modal encoder should be described as follows:

> The sign-controlled beam-splitter Hamiltonian is a projected low-frequency normal-mode model of a local distributed controller. If the controller command propagates at finite speed $v_c\le c$, the modal coupling acquires a causal form factor $F_c(\omega)$. For $q_c=\omega L/v_c\ll1$, the leading effect is a fixed control delay, while the coupling-strength correction begins at $O(q_c^2)$. A complete local handoff additionally carries an $O(L/v_c)$ clearing-time overhead. These changes reshape the source waveform but leave the serial gravitational link factorization unchanged.

This closes the concern that the global normal-mode notation itself assumes instantaneous branch control across the source.

---

# 14. Remaining scope

A fully microscopic quantum controller field that is explicitly launched, reflected, and reabsorbed could be constructed if needed, but it is not required for the present leading-order paper once the modal Hamiltonian is explicitly presented as the narrowband projection of a causal local controller.

Such a microscopic completion would be useful only if a referee requires exact controller-field state trajectories beyond the current

$$
O(q_c^2)
$$
locality control.
