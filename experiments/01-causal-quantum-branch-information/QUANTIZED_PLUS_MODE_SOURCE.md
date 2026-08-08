# Quantized Plus-Mode Source

**Timestamp:** 2026-08-07 20:04 EDT  
**Status:** Explicit leading-order Hamiltonian source model for the four-mass quadrupole geometry. This converts the prescribed branch trajectory into a standard state-dependent driven normal mode.

## 1. Small-deformation plus coordinate

Start from the four equal endpoint masses $\mu$ in `CONSERVED_FOUR_MASS_QUADRUPOLE_SOURCE.md`.

For a small deformation define one plus normal coordinate $u$ by

$$
X=L+u,
$$

$$
Y=L-u,
$$

to leading order in

$$
|u|/L\ll1.
$$

The exact constant-$X^2+Y^2$ geometry differs only at $O(u^2/L^2)$.

Two masses move on the $x$ axis and two on the $y$ axis. Each endpoint has speed magnitude $|\dot u|$ to leading order.

Therefore the total kinetic energy is

$$
T
=4\left(\frac12\mu\dot u^2\right)
=2\mu\dot u^2.
$$

Write this as

$$
T
=\frac12M_{\rm eff}\dot u^2.
$$

Hence

$$
\boxed{M_{\rm eff}=4\mu.}
$$

---

## 2. Quadrupole operator of the normal coordinate

From the exact four-mass quadrupole,

$$
Q_{xx}
=\frac23\mu L^2+2\mu d,
$$

$$
Q_{yy}
=\frac23\mu L^2-2\mu d,
$$

and in the small-deformation limit

$$
d\simeq2Lu.
$$

Therefore the time-dependent quadrupole of one mechanical configuration is

$$
\boxed{
\delta Q_{xx}=4\mu L\,u,
}
$$

$$
\boxed{
\delta Q_{yy}=-4\mu L\,u,
}
$$

$$
\delta Q_{zz}=0.
$$

Thus $u$ is directly a plus-polarized quadrupole normal coordinate.

---

## 3. Internal harmonic Hamiltonian

Let the symmetric internal elastic system have plus-mode frequency

$$
\omega_s.
$$

At quadratic order,

$$
\boxed{
H_s
=\frac{p_u^2}{2M_{\rm eff}}
+\frac12M_{\rm eff}\omega_s^2u^2.
}
$$

Quantize with

$$
[u,p_u]=i\hbar.
$$

Define

$$
\boxed{
u_{\rm zpf}
=\sqrt{\frac{\hbar}{2M_{\rm eff}\omega_s}}
=\sqrt{\frac{\hbar}{8\mu\omega_s}}.
}
$$

Then

$$
\boxed{
u
=u_{\rm zpf}(a+a^\dagger).
}
$$

The Hamiltonian is

$$
H_s
=\hbar\omega_s
\left(a^\dagger a+\frac12\right).
$$

---

## 4. Quadrupole transition matrix element

The plus quadrupole operator is

$$
\delta Q_{xx}
=4\mu L u_{\rm zpf}(a+a^\dagger),
$$

$$
\delta Q_{yy}
=-\delta Q_{xx}.
$$

For the single-phonon transition,

$$
q_{01}
\equiv
\langle0|\delta Q_{xx}|1\rangle
=4\mu L u_{\rm zpf}.
$$

Therefore

$$
\boxed{
q_{01}
=L\sqrt{\frac{2\mu\hbar}{\omega_s}}.
}
$$

The intrinsic spontaneous graviton linewidth of the plus mode is

$$
\kappa_g
=\frac{4G\omega_s^5|q_{01}|^2}
{5\hbar c^5}.
$$

Substitution gives

$$
\boxed{
\kappa_g
=\frac{8G\mu L^2\omega_s^4}
{5c^5}.
}
$$

This is a fully explicit gravitational linewidth for the ideal four-mass plus mode.

---

## 5. Consistency with the passive oscillator-strength ceiling

The four endpoint masses have characteristic moment of inertia

$$
I\sim4\mu L^2.
$$

The general passive nonrelativistic ceiling derived earlier is

$$
\kappa_g
\le
\frac{4G}{3c^5}I\omega_s^4.
$$

Using

$$
I=4\mu L^2
$$

gives

$$
\kappa_g
\le
\frac{16G\mu L^2\omega_s^4}{3c^5}.
$$

The explicit plus-mode value

$$
\frac{8}{5}
\frac{G\mu L^2\omega_s^4}{c^5}
$$

lies comfortably below this ceiling.

Thus the source model is consistent with the earlier oscillator-strength analysis.

---

## 6. Source branch qubit

Introduce a two-level internal control degree of freedom with basis

$$
|+\rangle_S,
\qquad
|-\rangle_S,
$$

represented by

$$
\sigma_z|s\rangle=s|s\rangle.
$$

Couple it to the plus mode through a state-dependent internal force

$$
\boxed{
H_F(t)
=-\sigma_zF(t)u.
}
$$

For a source-qubit superposition

$$
|+x\rangle_S
=\frac{|+\rangle_S+|-\rangle_S}{\sqrt2},
$$

the force creates the entangled mechanical cat

$$
\boxed{
\frac{
|+\rangle_S|\alpha(t)\rangle
+|-\rangle_S|-\alpha(t)\rangle
}{\sqrt2}
}
$$

up to branch-common phases, provided the oscillator begins near its ground state.

The two branches therefore have equal and opposite plus quadrupole expectation values.

---

## 7. Coherent-state dynamics under the state-dependent force

In the oscillator interaction picture,

$$
H_F^{I}(t)
=-\sigma_zF(t)u_{\rm zpf}
\left(
a e^{-i\omega_st}
+a^\dagger e^{i\omega_st}
\right).
$$

A linear force maps the oscillator vacuum to a coherent state.

The conditional coherent displacement is

$$
\boxed{
\alpha_s(t)
=s\,\frac{i u_{\rm zpf}}{\hbar}
\int_0^t dt'\,
F(t')e^{i\omega_st'},
}
$$

up to the chosen interaction-picture phase convention.

Thus

$$
\alpha_+(t)=-\alpha_-(t).
$$

No nonlinear mechanical interaction is required to create the branch-dependent coherent quadrupole once the source control is quantum.

---

## 8. Inverse-engineered closed trajectory

Instead of choosing $F(t)$ first, prescribe the desired branch coordinate

$$
\boxed{
u_s(t)=s\,u_c(t).}
$$

The classical normal-mode equation is

$$
M_{\rm eff}\ddot u_s
+M_{\rm eff}\omega_s^2u_s
=sF(t).
$$

Therefore

$$
\boxed{
F(t)
=M_{\rm eff}
[\ddot u_c(t)+\omega_s^2u_c(t)].
}
$$

Choose

$$
\boxed{
u_c(t)
=u_0
\sin^4\left(\frac{\pi t}{T}\right)
\cos(\omega_st),
\qquad0<t<T,
}
$$

and $u_c=0$ outside the pulse.

Since the $\sin^4$ envelope and its first three derivatives vanish at the endpoints,

$$
u_c(0)=\dot u_c(0)=0,
$$

$$
u_c(T)=\dot u_c(T)=0,
$$

and the inverse-engineered force also switches on/off without an impulse.

At the end of the protocol the mechanical plus mode returns to the same phase-space point in both branches.

Thus the oscillator can, ideally, disentangle from the source qubit after having emitted a branch-dependent gravitational wavepacket.

---

## 9. Resonant slowly varying force

For

$$
u_c(t)=u_0g(t)\cos(\omega_st),
$$

with

$$
g(t)=\sin^4(\pi t/T),
$$

$$
\ddot u_c+\omega_s^2u_c
=u_0
\left[
\ddot g(t)\cos(\omega_st)
-2\omega_s\dot g(t)\sin(\omega_st)
\right].
$$

Hence

$$
\boxed{
F(t)
=M_{\rm eff}u_0
\left[
\ddot g\cos(\omega_st)
-2\omega_s\dot g\sin(\omega_st)
\right].
}
$$

For

$$
\omega_sT\gg1,
$$

the dominant term scales as

$$
F\sim
2M_{\rm eff}\omega_su_0|\dot g|.
$$

The drive is purely internal to the source model in the idealization: equal-and-opposite forces act on the quadrupolar mechanical degree of freedom and produce no net center-of-mass force.

---

## 10. Branch quadrupole difference

One branch has

$$
\delta Q_{xx}^{(+)}
=4\mu L u_c(t),
$$

while the other has

$$
\delta Q_{xx}^{(-)}
=-4\mu L u_c(t).
$$

Therefore

$$
\boxed{
\Delta Q_{xx}(t)
=8\mu L u_c(t),
}
$$

$$
\boxed{
\Delta Q_{yy}(t)
=-8\mu L u_c(t).
}
$$

The branch-difference amplitude is therefore

$$
\boxed{q_0=8\mu L u_0.}
$$

---

## 11. Emitted coherent graviton distance

For the narrowband $\sin^4$ pulse,

$$
N_\Delta
\simeq
\frac{Gq_0^2\omega_s^5}{5\hbar c^5}
\int_0^Tdt\,
\sin^8\left(\frac{\pi t}{T}\right).
$$

Since

$$
\int_0^Tdt\,\sin^8(\pi t/T)
=\frac{35T}{128},
$$

and

$$
q_0=8\mu L u_0,
$$

we obtain

$$
\boxed{
N_\Delta
\simeq
\frac72
\frac{G\mu^2L^2u_0^2\omega_s^5T}
{\hbar c^5}.
}
$$

This is the gravitational branch-distance produced by the explicit quantum normal-mode excursion.

---

## 12. Independent input-output consistency check

The mechanical coherent-state coordinate satisfies, in a slowly varying rotating-frame description,

$$
\langle u\rangle
\simeq2u_{\rm zpf}\operatorname{Re}\alpha.
$$

For branch amplitudes $\pm u_c$, the mechanical coherent-state difference is therefore

$$
|\Delta\alpha_m(t)|
\simeq
\frac{u_0g(t)}{u_{\rm zpf}}.
$$

A mechanical mode with graviton linewidth $\kappa_g$ radiates a gravitational output field with branch-difference norm

$$
N_\Delta
=\kappa_g
\int_0^Tdt\,
|\Delta\alpha_m(t)|^2
$$

in the Markov narrowband input-output picture.

Thus

$$
N_\Delta
=\kappa_g
\frac{u_0^2}{u_{\rm zpf}^2}
\frac{35T}{128}.
$$

Using

$$
\kappa_g
=\frac{8G\mu L^2\omega_s^4}{5c^5}
$$

and

$$
u_{\rm zpf}^2
=\frac{\hbar}{8\mu\omega_s},
$$

gives

$$
\boxed{
N_\Delta
=\frac72
\frac{G\mu^2L^2u_0^2\omega_s^5T}
{\hbar c^5},
}
$$

exactly matching the quadrupole-spectrum calculation.

This is a valuable independent normalization check linking

1. the mechanical quantum mode;
2. the classical quadrupole formula;
3. the graviton input-output description.

---

## 13. Source returns but the field does not

At

$$
t=T,
$$

the source mechanical mode can return to the same state in both branches.

But the emitted gravitational field has already carried away branch information:

$$
\frac{
|+\rangle_S|g_+\rangle
+|-\rangle_S|g_-\rangle
}{\sqrt2}.
$$

Thus the source can close its local mechanical trajectory while the remote gravitational wavepacket retains the branch record.

This is exactly the information-flow structure needed for Experiment 01.

If the remote receiver captures part of the difference mode coherently, the source can become entangled with that receiver even though the local source oscillator has returned to its starting point.

---

## 14. Conservation and control

The Hamiltonian above describes the plus normal coordinate plus a state-dependent internal force.

A strictly autonomous total model can promote the time-dependent control $F(t)$ to an internal clock/work-reservoir degree of freedom. That refinement is not necessary for the leading radiative calculation provided that

1. all mechanical forces are internal and equal/opposite;
2. the total stress-energy, including the actuator/control subsystem, is conserved;
3. branch-dependent actuator radiation is either included or designed to be parametrically smaller/branch common.

The important improvement over prescribed accelerated point masses is that the radiating degree of freedom is now a legitimate internal normal mode with zero net force and an explicit quantum Hamiltonian.

---

## 15. Current complete source-to-receiver chain

The project can now write

$$
\boxed{
|+x\rangle_S|0\rangle_m
\xrightarrow{\ H_F(t)\ }
\frac{|+\rangle|+\alpha(t)\rangle
+|-\rangle|-\alpha(t)\rangle}{\sqrt2}
}
$$

$$
\boxed{
\xrightarrow{\ \text{graviton emission}\ }
\frac{|+\rangle|g_+\rangle
+|-\rangle|g_-\rangle}{\sqrt2}
}
$$

$$
\boxed{
\xrightarrow{\ R/c\ }
\text{noisy receiver channel}
}
$$

with every link parameterized by explicit quantities.

This is substantially closer to a genuine Gedanken experiment than the earlier abstract source-cat picture.

---

## 16. Strongest next step

Use the four-mass plus mode as **both source and receiver**, so that

$$
\kappa_{g,A},
\quad
\kappa_{g,B},
\quad
N_\Delta,
\quad
\eta_{\rm store}(R),
\quad
\tau_f(t,R)
$$

are all expressed in masses, sizes, frequencies, source displacement amplitude, receiver damping, temperature, and distance. Then determine the resulting absolute certification scale numerically and identify which parameter dominates the impossibility/practicality.