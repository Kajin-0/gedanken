# Experiment 03 — Tilt / directionality / dark-action monotonicity lemma — 2026-08-15

## Status

**Exact one-coordinate potential result under the stated assumptions. Generic metastable-potential mathematics; not novelty-audited and not by itself a detector claim.**

This result explains why simply increasing the static directional flux tilt is not a free way to make photon-triggered capture more one-sided.

## 1. Setup

Let the cold rf-SQUID phase potential be

\[
V(x;\delta)=V_0(x)-E_L\delta x,
\]

where

- `V0(x)` contains the inductive/Josephson potential at zero directional tilt;
- `delta` is a dimensionless static tilt;
- `E_L=Phi_bar^2/L>0` sets the physical energy scale.

Assume that over the interval considered the potential has

- a metastable left minimum `x_m(delta)`;
- a separating saddle `x_s(delta)>x_m`;
- a favored right minimum `x_r(delta)>x_s`;
- a zero-energy bounce turning point `x_t(delta)>x_s` satisfying
  \[
  V(x_t;\delta)=V(x_m;\delta).
  \]

All derivatives below are taken while this topology persists smoothly.

## 2. Barrier height decreases monotonically with positive tilt

The metastable barrier is

\[
\Delta U_b(\delta)
=V(x_s;\delta)-V(x_m;\delta).
\]

Because `dV/dx=0` at both stationary points, their implicit coordinate shifts do not contribute to the total derivative:

\[
\frac{d\Delta U_b}{d\delta}
=rac{\partial V}{\partial\delta}(x_s)
-\frac{\partial V}{\partial\delta}(x_m).
\]

Since

\[
\frac{\partial V}{\partial\delta}=-E_Lx,
\]

we obtain

\[
\boxed{
\frac{d\Delta U_b}{d\delta}
=-E_L(x_s-x_m)<0.
}
\]

Thus increasing positive tilt necessarily lowers the dark barrier for escape toward the favored side.

## 3. Well-energy directionality increases monotonically

Define the cold energetic preference of the right well as

\[
\Delta E_{LR}
=V(x_m)-V(x_r).
\]

Again the stationary-coordinate terms vanish, giving

\[
\boxed{
\frac{d\Delta E_{LR}}{d\delta}
=E_L(x_r-x_m)>0.
}
\]

So the same tilt that increases right-well energetic preference necessarily lowers the left metastable barrier.

## 4. Exact isolated bounce action also decreases monotonically

For phase mass

\[
M=C\bar\Phi^2,
\]

the zero-temperature isolated zero-energy bounce exponent is

\[
B(\delta)
=\frac{2}{\hbar}
\int_{x_m}^{x_t}
\sqrt{2M\,[V(x;\delta)-V(x_m;\delta)]}\,dx.
\]

The integrand vanishes at both endpoints, so endpoint derivatives do not contribute. At fixed integration coordinate,

\[
\frac{d}{d\delta}
\left[V(x;\delta)-V(x_m;\delta)\right]
=-E_L(x-x_m),
\]

because `V_x(x_m)=0`.

Therefore

\[
\boxed{
\frac{dB}{d\delta}
=-\frac{2ME_L}{\hbar}
\int_{x_m}^{x_t}
\frac{x-x_m}
{\sqrt{2M[V(x)-V(x_m)]}}\,dx
<0.
}
\]

The exact isolated tunneling action toward the favored side therefore decreases monotonically with increasing positive tilt.

## 5. Direct directionality–action tradeoff

Since

\[
\frac{d\Delta E_{LR}}{d\delta}>0,
\qquad
\frac{dB}{d\delta}<0,
\]

we have

\[
\boxed{
\frac{dB}{d\Delta E_{LR}}<0
}
\]

along the one-parameter tilt family.

Thus **static energetic directionality and metastable dark-action protection are antagonistic control objectives** when directionality is generated solely by a linear potential tilt.

## 6. Detector interpretation

This result does not say that a directional photon latch is impossible. It says that directionality should not be optimized by tilt alone.

Potential escape routes include

- changing normalized loop/Josephson topology (`beta_cold`) to widen the metastable barrier while retaining required tilt;
- changing CPR shape/harmonics;
- using an intrinsically nonreciprocal / `phi_0` element whose directional dynamics are not reducible to the same simple linear tilt;
- using time-dependent directional control rather than a large static bias.

The current `barrier_shape_action_scan.py` tests the first option numerically.

## 7. Limitations

- This is an **isolated one-coordinate** bounce statement. A dissipative environment adds a nonlocal action term whose tilt derivative need not be given only by the local expression above because the stationary bounce path also changes.
- The sign result for barrier height and well-energy bias remains exact for the static local potential.
- `Delta E_LR` is only one measure of directionality. Actual photon-capture directionality is dynamical and depends on the finite pulse and environment.

No novelty claim is authorized.
