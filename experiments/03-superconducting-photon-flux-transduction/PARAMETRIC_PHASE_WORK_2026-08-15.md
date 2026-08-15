# Parametric Phase-Work / Separatrix-Energy Closure — 2026-08-15

## Purpose

Extract an exact energy-balance identity from the full time-dependent scalar-R RCSJ model and use it to unify:

```text
sudden-quench switching
finite thermal-rise dependence
damping-window behavior
post-crossing retrapping.
```

This identity is elementary mechanics for a time-dependent potential and is **not** a novelty claim. Its value is organizational: it identifies the physically correct energy bookkeeping for Experiment 03 and replaces several misleading one-parameter intuitions.

## 1. Time-dependent phase equation

The current deterministic scalar-R model is

```math
\boxed{
LC\ddot x+\frac{L}{R}\dot x+F[x,T(t)]=0,
}
```

with

```math
F(x,T)=\partial_xU(x,T).
```

Multiply by `xdot`:

```math
LC\ddot x\dot x
+\frac{L}{R}\dot x^2
+\partial_xU\,\dot x=0.
```

Because

```math
\frac{dU}{dt}
=\partial_xU\,\dot x+\partial_TU\,\dot T,
```

the exact phase-energy balance is

```math
\boxed{
\frac{d}{dt}
\left[
\frac12LC\dot x^2+U(x,T)
\right]
=
\partial_TU(x,T)\dot T
-\frac{L}{R}\dot x^2.
}
```

Define

```math
E_\phi
=\frac12LC\dot x^2+U(x,T),
```

```math
W_T(t)
=\int_0^t\partial_TU[x(t'),T(t')]\dot T(t')dt',
```

and

```math
Q_R(t)
=\int_0^t\frac{L}{R}\dot x^2(t')dt'.
```

Then

```math
\boxed{
E_\phi(t)-E_\phi(0)
=W_T(t)-Q_R(t).
}
```

The optical/thermal pulse does not simply "lower a barrier." It performs path-dependent **parametric work on the phase degree of freedom** while dissipation removes phase energy.

## 2. Instantaneous separatrix-relative energy

While the selected saddle exists, let `x_s(T)` satisfy

```math
\partial_xU[x_s(T),T]=0.
```

Define the instantaneous separatrix-relative energy

```math
\boxed{
\mathcal E_s(t)
=\frac12LC\dot x^2
+U[x,T]
-U[x_s(T),T].
}
```

Since `U_x(x_s,T)=0`,

```math
\frac{d}{dT}U[x_s(T),T]
=\partial_TU[x_s(T),T].
```

Therefore

```math
\boxed{
\dot{\mathcal E}_s
=
\left[
\partial_TU(x,T)
-\partial_TU(x_s,T)
\right]\dot T
-\frac{L}{R}\dot x^2.
}
```

This is the most useful current energy identity.

Interpretation:

```text
first term  = parametric change of the trajectory's energy relative to the moving saddle;
second term = irreversible scalar-R phase-energy loss.
```

## 3. Sudden-quench threshold recovered exactly

Suppose the phase is initially at the cold metastable minimum `x_c` with zero velocity and the potential is changed instantaneously from `T0` to `T_h` before `x` can move.

Immediately after the quench,

```math
\mathcal E_s(0^+)
=U(x_c,T_h)-U[x_s(T_h),T_h].
```

Using the quench-barrier definition from `SUDDEN_QUENCH_BOUND_2026-08-15.md`,

```math
\mathcal B_q(T)
=U[x_s(T),T]-U(x_c,T),
```

we have

```math
\boxed{
\mathcal E_s(0^+)
=-\mathcal B_q(T_h).
}
```

Thus

```math
\boxed{
T_h=T_q
\iff
\mathcal E_s(0^+)=0.
}
```

The sudden-quench threshold is therefore exactly the point where the parametric potential change places the frozen cold coordinate on the hot separatrix energy.

This gives a direct energetic meaning to `T_q<T_f`.

## 4. Why finite rise changes the threshold

For finite rise, the phase coordinate moves while the potential changes.

Therefore the work input is not simply

```math
U(x_c,T_{peak})-U(x_c,T_0).
```

Instead it is the path integral

```math
\boxed{
W_T
=\int\partial_TU[x(t),T(t)]\dot Tdt.
}
```

Two pulses with the same deposited photon energy and same nominal final/peak temperature can transfer different amounts of energy into the **phase coordinate** if their rise times produce different `x(t)` trajectories.

This is why `tau_rise` is an independent dynamical control parameter rather than merely a correction to `T_peak`.

## 5. Damping has opposite roles before and after basin crossing

The dissipative term is always

```math
-\frac{L}{R}\dot x^2\le0.
```

But whether phase-energy loss is beneficial depends on the stage of the trajectory.

### Stage A — launch / barrier crossing

Before the trajectory has crossed the relevant separatrix, dissipation generally reduces `mathcal E_s` and can prevent crossing.

This explains the full-solver observation that excessive damping at small `R` suppresses the nonadiabatic kick.

### Stage B — capture / retrapping

After the trajectory has entered the target side, excess kinetic energy can carry it back across a restoring barrier or through additional oscillations.

Dissipation can now be beneficial because it removes kinetic energy and traps the phase in the desired recovered basin.

This explains the appearance of an upper weak-damping / oscillatory-retrapping boundary in the full `r_Delta=0.6` scalar-R simulations.

Therefore

```text
less damping is not always better,
and more damping is not always better.
```

The two-stage requirement is

```text
preserve enough phase energy during launch
+
remove enough phase energy during capture.
```

## 6. Consequence for environmental engineering

A single broadband constant resistor is unlikely to be the natural optimum.

The desired environment is qualitatively closer to

```text
weak effective dissipation in the launch-relevant dynamical band/state
stronger effective damping during capture/retrapping
weak dissipative coupling in the final cold storage state.
```

Possible implementations could involve frequency-, temperature-, or state-dependent admittance. This is a **design direction only**, not a claim that such shaping is noiseless or easy.

Any real admittance

```math
Y(\omega,T)=Y_1+iY_2
```

with `Y_1>0` carries fluctuation noise through fluctuation-dissipation and also modifies dissipative MQT. The same environment must be used consistently in

```text
classical phase capture
cold equilibrium fluctuations
quantum escape.
```

There is no free damping knob.

## 7. A useful phase-conversion efficiency definition

The photon energy is initially deposited in the electronic/thermal subsystem. Only some fraction performs work on the phase coordinate.

Define the positive launch-stage parametric work

```math
W_{T,+}
=\int_{launch}\max(\partial_TU\dot T,0)dt.
```

A useful conditional transduction metric is

```math
\boxed{
\eta_{\gamma\to\phi}
=\frac{W_{T,+}}{E_\gamma}.
}
```

This is not a thermodynamic efficiency of the entire detector; it measures how effectively absorbed photon energy is converted into useful phase-potential work during launch.

A better full trajectory metric will likely compare the maximum separatrix-energy margin reached,

```math
\boxed{
\mathcal E_{s,max}
=\max_t\mathcal E_s(t),
}
```

against the dissipative loss accumulated before first separatrix crossing.

## 8. Candidate deterministic accounting criterion

For trajectories while a saddle exists, integrate the exact identity:

```math
\boxed{
\mathcal E_s(t)
=\mathcal E_s(0)
+\int_0^t
[U_T(x,T)-U_T(x_s,T)]\dot Tdt'
-\int_0^t\frac{L}{R}\dot x^2dt'.
}
```

A necessary energetic event for frozen-potential crossing is that the trajectory reach

```math
\mathcal E_s\ge0.
```

In the actual time-dependent problem this is not by itself sufficient for permanent capture, because the separatrix moves/disappears/reforms and the trajectory can retrap.

Nevertheless it is a substantially better scalar diagnostic than `T_peak/T_f`.

## 9. What is exact vs approximate

### Exact within scalar-R time-dependent RCSJ

- total phase-energy balance;
- separatrix-relative energy derivative while the saddle exists;
- sudden-quench identity `E_s(0+)=-B_q`;
- nonnegative dissipative loss `Q_R`.

### Not established

- that `E_s,max` alone predicts final basin;
- an optimal causal admittance;
- stochastic capture probabilities;
- dissipative MQT with the same environment;
- a universal phase-work efficiency independent of the chosen material/CPR.

## 10. Next numerical test

Extend `full_dynamic_rfsquid.py` or a dedicated diagnostic to record

```text
W_T(t)
Q_R(t)
E_s(t)
first separatrix crossing
final-basin capture.
```

Then compare capture and noncapture trajectories at the same photon energy while varying `R` and `tau_rise`.

The important question is whether the basin boundary becomes simple when represented by a small number of energy quantities such as

```text
max separatrix-energy margin
pre-crossing dissipative loss
post-crossing dissipative loss.
```

If so, that may provide the correct reduced dynamic closure before moving to a causal environmental admittance.

## Status

**GO for continued theory. NO-GO for manuscript.**
