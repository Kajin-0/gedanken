# Reduced Dynamic Diagnostic Audit — 2026-08-15

## Purpose

Record several attempted scalar reductions of the full nonadiabatic capture dynamics, including the cases where they initially looked successful and the broader tests that falsified them.

This file is important recovery provenance: future agents should not rediscover these same attractive but incomplete one-number criteria and mistake a small test set for a universal collapse.

## 1. Phase-energy exposure / traversal index — rejected as universal

Starting from the instantaneous separatrix-relative energy

```math
\mathcal E_s
=\frac12LC\dot x^2+U(x,T)-U[x_s(T),T],
```

an exploratory phase-traversal index was formed from the intervals with `E_s>0`, schematically

```math
\mathcal J_s
\sim
\frac{
\int_{\mathcal E_s>0}
\sqrt{2\mathcal E_s/(LC)}\,dt
}
{\Delta x_{sep}}.
```

Four hand-picked boundary-near trajectories looked encouraging:

```text
noncapture: J~0.14, 0.64
capture:    J~1.10, 1.88.
```

A wider grid destroyed a universal threshold. In particular, the relationship between positive separatrix energy and actual coordinate traversal depends on the time-dependent potential and the phase velocity inherited from earlier portions of the pulse.

**Disposition:** useful intuition only; rejected as a capture classifier.

## 2. Instantaneous unstable e-fold exposure — initially promising, then rejected alone

At the instantaneous saddle, define

```math
\lambda_+(t)
=-\frac{1}{2RC}
+\sqrt{
\frac{1}{4R^2C^2}
+\frac{|\kappa_s(t)|}{LC}
}.
```

An instability-exposure integral was tested:

```math
\mathcal G_s
=\int_{\mathcal E_s>0}\lambda_+(t)dt.
```

### Small test set

The first four examples separated well:

```text
rDelta=.8: failure ~1.87, capture ~4.03
rDelta=.6: failure ~0.71, capture ~4.22.
```

### First mistake caught

Integrating after physical separatrix crossing is partly circular because a captured trajectory can accumulate additional unstable exposure *because it has already crossed*.

The integral was therefore truncated at first physical saddle crossing for capture trajectories.

### Broader pre-crossing test

For `rDelta=.8`, pre-crossing exposure still separated the retained sub-fold grid:

```text
captures: min ~1.82
failures: max ~1.63.
```

But for `rDelta=.6` it did not:

```text
captures: min ~0.95
failures: max ~1.49.
```

A strongly damped failure can spend substantial time in a formally unstable energetic region but lose the trajectory-level phase-space displacement needed for actual basin crossing.

**Disposition:** `G_s` is a useful finite-time instability descriptor but not sufficient alone.

## 3. Moving-minimum harmonic tracking ratio — rejected alone

Before tipping, approximate the potential around the moving metastable minimum `x_m(T)`:

```math
LC\ddot x+\frac{L}{R}\dot x
+\kappa_m(T)[x-x_m(T)]\simeq0.
```

Compare the harmonic tracking error with the instantaneous basin width

```math
\mathcal R_m(t)
=\frac{x(t)-x_m(T)}{x_s(T)-x_m(T)}.
```

This correctly captures the rate-induced idea that the stable state moves relative to a shrinking basin.

On selected examples, captures had larger maximum `R_m` than nearby failures.

Across the wider grid, however, a strongly damped `rDelta=.6` failure produced a very large positional lag while lacking the momentum/energy required for nonlinear crossing. Some captures occurred at smaller harmonic lag.

**Disposition:** positional tracking deficit is necessary information but not sufficient without phase velocity / phase-space geometry.

## 4. Instantaneous saddle stable-manifold coordinate — locally correct, globally insufficient

For the frozen damped saddle, the eigenvalues are

```math
\lambda_\pm
=-\frac{1}{2RC}
\pm
\sqrt{
\frac{1}{4R^2C^2}
+\frac{|\kappa_s|}{LC}
}.
```

In moving-saddle coordinates `y=x-x_s(t)`, a natural local signed unstable-mode coordinate is

```math
\boxed{
\Sigma(t)
=[\dot x-\dot x_s]
-\lambda_-(t)[x-x_s].
}
```

For a frozen linear saddle, `Sigma=0` is the tangent stable manifold and the sign of `Sigma` distinguishes the local unstable branch.

Selected capture/failure cases separated strongly.

A broader nonautonomous test showed that a strongly damped failure can transiently acquire positive instantaneous `Sigma` yet later return to the original basin because the saddle/manifold continues to move and the potential recovers.

**Disposition:** the instantaneous stable manifold is not the correct global basin boundary for a finite pulse.

## 5. Why all four reductions fail in the same way

The detector is a nonautonomous second-order dynamical system:

```math
LC\ddot x+\frac{L}{R}\dot x+F[x,T(t)]=0.
```

The final outcome is a **basin question in phase space**, not merely an instantaneous energy or position question.

During the optical pulse:

```text
the stable minimum moves;
the saddle moves;
the basin boundary moves;
the saddle can disappear and reappear;
phase velocity carries memory of earlier potential motion;
damping changes both launch and retrapping;
final classification occurs after the drive has substantially changed again.
```

Therefore no local scalar evaluated against the instantaneous frozen saddle is expected to be globally exact.

## 6. Correct reduced object: finite-time/nonautonomous basin boundary

The appropriate object is the time-dependent codimension-one stable manifold that separates trajectories ending in the left and right recovered basins.

In the current 2D phase space

```text
(x, v)
```

for a prescribed thermal pulse `T(t)`, this boundary is a curve at each time.

A rigorous reduced description should therefore determine a signed finite-time basin coordinate

```math
\boxed{
\mathcal B_{FT}(x,v,t;\,T(\cdot),R)=0
}
```

such that

```text
B_FT < 0 -> left recovered basin
B_FT > 0 -> right recovered basin.
```

The instantaneous saddle stable manifold is only the frozen/adiabatic approximation to this finite-time object.

## 7. Practical computational route

For the scalar-R deterministic model, construct the finite-time basin boundary by backward/edge tracking:

1. choose a final time after the thermal pulse has essentially recovered;
2. use the cold saddle's stable manifold as the terminal local basin boundary;
3. integrate that boundary **backward through the full time-dependent phase equation**;
4. compare the actual cold initial condition `(x_c,0)` with the pulled-back boundary.

Equivalently, at fixed pulse parameters, use bisection/edge tracking in initial phase-space conditions to find the trajectory that asymptotically lies on the left/right basin separator.

This provides the correct deterministic switching criterion without pretending that a frozen-system energy or saddle coordinate is exact during a fast pulse.

## 8. Relation to rate-induced tipping literature

This conclusion is consistent with the established nonautonomous tipping literature, where loss of tracking and basin instability are organized by time-dependent basin boundaries / edge states rather than only frozen bifurcations.

Therefore the finite-time stable-manifold concept itself is **not** an Experiment-03 novelty route.

The detector-specific question remains whether the pulled-back boundary can be compressed into a useful wavelength / rise-time / damping / dark-stability closure for persistent superconducting flux capture.

## 9. Result retained from the failed reductions

Although no one-number local classifier survived, the exercise established that any useful reduced model must preserve at least:

```text
phase position
phase velocity
moving basin geometry
time dependence of the thermal drive
damping history.
```

This sharply constrains future simplifications.

## Status

**SCALAR LOCAL CAPTURE CRITERION: NO-GO.**

**FINITE-TIME PHASE-SPACE BOUNDARY: preferred deterministic reduction.**

**EXPERIMENT 03: GO for continued theory; NO-GO for manuscript.**
