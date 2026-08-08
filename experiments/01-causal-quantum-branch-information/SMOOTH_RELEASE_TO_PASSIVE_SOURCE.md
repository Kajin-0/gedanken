# Smooth Release from Held Static Branch State to Passive Free Emission

**Date:** 2026-08-07  
**Status:** **EXPLICIT FINITE-TIME CAUSAL INTERVENTION — SIGNAL/CONTROL QUADRUPOLE IS $C^2$ AND UV-FINITE**

## 1. Goal

`CAUSAL_SOURCE_INTERVENTION_PROTOCOL.md` proposes the causal comparison

- **control:** hold the static branch state;
- **signal:** smoothly release the plus mode and let it evolve freely.

The release must satisfy three requirements:

1. signal and control histories are identical before the intervention;
2. the release joins continuously onto a free normal-mode trajectory;
3. the signal-control quadrupole is smooth enough that ideal graviton-number/radiated-energy integrals are ultraviolet finite.

A compact quintic bridge is sufficient.

---

## 2. Held control trajectory

Let the branch label be

$$
s=\pm1.
$$

Before release and throughout the control run,

$$
\boxed{
u_{s,\rm ctrl}(t)=s u_0.}
$$

The source is held at a plus-mode turning point.

---

## 3. Release interval

Let the release begin at

$$
t=0
$$

and end at

$$
t=T_r.
$$

Define

$$
\boxed{x=t/T_r,}
$$

and

$$
\boxed{\lambda_r=(\omega T_r)^2.}
$$

Write the signal trajectory as

$$
\boxed{
u_{s,\rm sig}(t)
=s[u_0+\delta u(t)].}
$$

Choose

$$
\boxed{
\frac{\delta u(t)}{u_0}
=-\frac{\lambda_r}{2}
x^3(1-x)^2,
\qquad0\le x\le1.
}
$$

This is the unique quintic of the form

$$
a_3x^3+a_4x^4+a_5x^5
$$

that satisfies the desired six endpoint conditions below.

---

## 4. Start of release

At

$$
x=0,
$$

$$
\boxed{\delta u(0)=0,}
$$

$$
\boxed{\dot{\delta u}(0)=0,}
$$

$$
\boxed{\ddot{\delta u}(0)=0.}
$$

Therefore signal and control agree in

- position;
- velocity;
- acceleration

at the instant the intervention begins.

The source stress history can begin changing continuously rather than through an acceleration impulse.

---

## 5. End of release

At

$$
x=1,
$$

$$
\boxed{\delta u(T_r)=0,}
$$

$$
\boxed{\dot{\delta u}(T_r)=0,}
$$

but

$$
\boxed{\ddot{\delta u}(T_r)=-\omega^2u_0.}
$$

Thus the signal ends the release interval at

$$
\boxed{
u_{s,\rm sig}(T_r)=s u_0,}
$$

$$
\boxed{\dot u_{s,\rm sig}(T_r)=0,}
$$

with exactly the acceleration required for free harmonic motion about the origin.

---

## 6. Free tail

Ignoring the parametrically tiny damping during the release itself, the signal trajectory for

$$
t>T_r
$$

can be taken as

$$
\boxed{
u_{s,\rm sig}(t)
=s u_0\cos[\omega(t-T_r)]}
$$

for the lossless benchmark.

For passive damping, replace this by the underdamped free solution initialized at

$$
u(T_r)=s u_0,
\qquad
\dot u(T_r)=0.
$$

For a damping equation

$$
\ddot u+\kappa_A\dot u+\omega_0^2u=0,
$$

the exact continuation is

$$
\boxed{
u_{s,\rm sig}(t)
=s u_0e^{-\kappa_A\tau/2}
\left[
\cos(\Omega\tau)
+\frac{\kappa_A}{2\Omega}
\sin(\Omega\tau)
\right],
}
$$

where

$$
\tau=t-T_r,
$$

$$
\Omega=\sqrt{\omega_0^2-\kappa_A^2/4}.
$$

Its initial acceleration is

$$
\ddot u(T_r^+)
=-\omega_0^2u_0,
$$

so use $\omega=\omega_0$ in the release bridge.

---

## 7. Signal-control difference

Define

$$
\boxed{
\delta u_{\rm sc}(t)
=u_{\rm sig}(t)-u_{\rm ctrl}(t).
}
$$

Before release,

$$
\delta u_{\rm sc}=0.
$$

During release it is the quintic bridge above.

At the release endpoint,

$$
\delta u_{\rm sc}=0,
$$

$$
\dot{\delta u}_{\rm sc}=0,
$$

$$
\ddot{\delta u}_{\rm sc}=-\omega^2u_0,
$$

which matches the free signal minus static control exactly.

Therefore

$$
\boxed{
\delta u_{\rm sc}(t)
\text{ is }C^2
}
$$

across both intervention boundaries.

---

## 8. Corresponding conserved-source quadrupole

For the finite-spoke source,

$$
\Delta Q_{xx}
=8\mu L u
\frac{\tan q}{q}.
$$

Thus the branch-difference **signal-control** quadrupole is

$$
\boxed{
\delta\Delta Q_{xx}^{\rm sc}(t)
=8\mu L\frac{\tan q}{q}
\delta u_{\rm sc}(t),
}
$$

$$
\boxed{
\delta\Delta Q_{yy}^{\rm sc}(t)
=-\delta\Delta Q_{xx}^{\rm sc}(t).
}
$$

It is also $C^2$.

---

## 9. Ultraviolet behavior

If a compactly switched function and its first two derivatives are continuous while its third derivative has only finite jumps, then its Fourier transform decays asymptotically as

$$
\boxed{
|\widetilde Q(\omega')|
=O(\omega'^{-4}).
}
$$

Therefore the ideal graviton branch-distance integrand behaves as

$$
\omega'^5
|\widetilde Q|^2
=O(\omega'^{-3}),
$$

which is integrable.

The radiated-energy integrand carries one additional power of frequency,

$$
\omega'^6
|\widetilde Q|^2
=O(\omega'^{-2}),
$$

which is also integrable.

Thus the smooth release avoids the ultraviolet pathology of an instantaneous acceleration change.

---

## 10. Required generalized force

Let the free plus-mode equation be

$$
M_{\rm eff}\ddot u
+M_{\rm eff}\omega^2u
=F(t).
$$

The control run uses the static holding force

$$
\boxed{F_{\rm hold}=M_{\rm eff}\omega^2u_0.}
$$

For the signal release,

$$
F_{\rm sig}(t)
=M_{\rm eff}
[\ddot u_{\rm sig}+\omega^2u_{\rm sig}].
$$

Using

$$
y(x)=\delta u/u_0
=-\frac{\lambda_r}{2}x^3(1-x)^2,
$$

the normalized signal force is

$$
\boxed{
\frac{F_{\rm sig}(x)}{F_{\rm hold}}
=1-3x+12x^2-10x^3
-\frac{\lambda_r}{2}x^3(1-x)^2.
}
$$

It satisfies

$$
\boxed{F_{\rm sig}(0)=F_{\rm hold},}
$$

$$
\boxed{F_{\rm sig}(T_r)=0.}
$$

Thus the intervention is literally a smooth finite-time removal of the holding force.

---

## 11. Size of the release excursion

The shape

$$
x^3(1-x)^2
$$

is maximized at

$$
\boxed{x=3/5}
$$

with value

$$
\boxed{
\frac{108}{3125}
\simeq0.03456.
}
$$

Hence

$$
\boxed{
\max\frac{|\delta u|}{u_0}
=0.01728(\omega T_r)^2.
}
$$

For

$$
\omega T_r\lesssim1,
$$

the source barely moves during the release; the intervention mainly removes the holding acceleration smoothly before free oscillation begins.

---

## 12. Branch-common controller energy

For source branch $s$, the required generalized force changes sign:

$$
F_s(t)=sF_{\rm sig}(t).
$$

The branch trajectory also changes sign:

$$
u_s(t)=su_{\rm sig}(t).
$$

Therefore the instantaneous generalized coupling energy

$$
-F_su_s
$$

is branch independent:

$$
\boxed{-F_su_s=-F_{\rm sig}u_{\rm sig}.}
$$

Likewise the controller backreaction can be made branch common under the controlled-parity construction.

This does not replace a full microscopic actuator stress tensor, but it shows explicitly that the finite release profile does not require branch-dependent controller work at the mode level.

Any compact residual controller quadrupole is bounded by `HUB_CONTROLLER_RESIDUAL_BOUND.md`.

---

## 13. Causal timing

The intervention support begins at

$$
t=0
$$

and lasts until

$$
t=T_r.
$$

Therefore the earliest possible receiver dependence is

$$
\boxed{t=R/c,}
$$

not

$$
T_r+R/c.
$$

The release transient and later passive tail are both parts of the same retarded signal waveform.

---

## 14. Active versus passive content

The release interval requires a finite internal controller.

After

$$
t=T_r,
$$

the source evolves passively with no active shaping.

This is substantially weaker than assuming an actuator enforces an arbitrary waveform during the entire emission history.

The paper can therefore use

- a short smooth local intervention;
- followed by a long autonomous emission tail.

---

## 15. Adversarial verdict

A causal release-versus-hold protocol can be made

- local;
- finite in duration;
- continuous through acceleration;
- ultraviolet finite;
- exactly matched onto the passive normal mode;
- branch symmetric at the generalized-work level.

Thus the preparation/release transient no longer needs to be represented by an instantaneous kick or an unspecified discontinuous force.

---

## 16. Next calculation

The remaining quantitative refinement is to compute the relative graviton branch distance carried by

1. the finite release transient;
2. the passive free tail.

This would determine whether the release can be made spectrally negligible compared with the resonant tail for a suitable range of

$$
\omega T_r.
$$

Because the receiver is narrowband, the more relevant quantity may be the release transient's projection onto the receiver's normalized resonant temporal mode rather than its total broadband graviton number.
