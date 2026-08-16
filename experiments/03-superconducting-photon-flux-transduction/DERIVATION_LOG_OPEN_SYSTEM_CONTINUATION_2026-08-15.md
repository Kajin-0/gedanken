# Experiment 03 — Open-system / dark-action derivation continuation — 2026-08-15

This file continues the Experiment-03 derivation trail beyond `DERIVATION_LOG_DYNAMIC_2026-08-15.md`. It records the causal-environment, exact-bounce and constant-dark-action design shift. `CURRENT_STATE.md` must remain the compact live frontier.

## Step 57 — scalar resistor replaced by a causal passive two-pole environment

The strongest passive capture network is

\[
Z(s)=sL_f+\frac{R}{1+sRC_f},
\]

with

\[
L_f=\frac{\sqrt2R}{\omega_D},
\qquad
C_f=\frac{1}{\sqrt2R\omega_D}.
\]

Its dissipative spectrum is

\[
\boxed{\operatorname{Re}Y(\omega)=\frac{1/R}{1+(\omega/\omega_D)^4}}.
\]

Compared with a one-pole Drude environment, the quartic rolloff can retain useful phase-band damping while reducing ultraviolet coupling. Generic frequency-selective Josephson damping is prior art; novelty is not assigned to this network choice.

The deterministic extended-system energy balance is exact and passive. The environment redistributes dissipation across the launch and capture stages, but a simple stage-selectivity ratio is not a universal probability predictor.

## Step 58 — symmetrized-FDT TWA established as a stress model, not exact quantum dynamics

A real Gaussian current record with the symmetrized quantum-FDT spectrum can reproduce the cold harmonic Wigner covariance when thermalized from the past. The stationarity regression was tightened until the linear covariance agreed at the percent/sub-percent level.

However the same classicalized zero-point record allows unphysical vacuum-driven activation in a nonlinear metastable system because it does not preserve quantum absorption/emission asymmetry.

Therefore

```text
sym-FDT TWA capture = harsh semiclassical screening model
sym-FDT TWA dark switching != physical quantum DCR.
```

A detailed-balance-preserving nonlinear open-quantum treatment remains mandatory before publication.

## Step 59 — exact optical similarity of the reduced thermal problem

For the retained lumped graphene model

\[
C_e=\gamma AT
\]

with fixed cooling/rise/material/circuit parameters, one absorbed photon enters the temperature history through

\[
\frac{\eta_{abs}}{A\lambda}.
\]

Hence

\[
\boxed{P_{cap}(\lambda,A,\eta_{abs})
=\mathcal P\left(\frac{\eta_{abs}}{A\lambda}\right)}
\]

within the reduced model.

At fixed absorption efficiency,

\[
\boxed{A_p\lambda=\text{constant}}
\]

for every target screening probability `p`.

This is a model symmetry, not a statement that real optical absorptance or spatial thermalization remains wavelength-independent.

## Step 60 — old cubic MQT dark model fails for the actual CPR barrier

For the live cold `rDelta=.6`, `beta=.80`, `delta=.05` potential, the textbook cubic estimate gives roughly

\[
B_{cubic}\approx38.04.
\]

The exact isolated zero-energy bounce of the actual non-sinusoidal CPR potential instead gives

\[
\boxed{B_{iso}\approx25.033}.
\]

Thus the effective shape factor is only

\[
\boxed{\beta_U\approx4.74},
\]

not 7.2.

The dark-stability problem was therefore a barrier-shape problem hidden by the cubic approximation.

## Step 61 — full same-environment nonlocal bounce closes the zero-T action

The passive two-pole environment was integrated into the Euclidean action through its full positive-real admittance. A spectral stationary-bounce solver was built and converged in basis size.

For the live R80 point:

\[
\boxed{B_{diss}=29.765636}.
\]

The environment adds only

\[
\Delta B_{env}\approx4.728
\]

over the exact isolated action, and the converged Hessian has exactly one negative even mode.

Thus the original `C=215 fF` point is rejected as a final dark-stable design under the current zero-temperature action screen.

## Step 62 — exact electrical similarity produces a dark-action / speed invariant

At fixed loop inductance, static potential and normalized two-pole topology,

\[
\boxed{C'=r^2C,\quad R'=R/r,\quad \omega_D'=\omega_D/r}.
\]

Then

\[
\omega_c'=\omega_c/r,
\qquad g'=g,
\qquad\alpha'=\alpha.
\]

Under `tau=r tau'`, every term in the zero-temperature Euclidean action scales by `r`, giving

\[
\boxed{B'=rB}.
\]

For fixed physical photon-rise time,

\[
\rho=\omega_c\tau_{rise}\to\rho/r,
\]

so

\[
\boxed{B\rho=\text{constant}}
\]

along the pure electrical-rescaling family.

The same scaling gives the cold harmonic phase width

\[
\boxed{\sigma_x^2\to\sigma_x^2/r}.
\]

Thus capacitance compensation simultaneously raises dark action, slows the phase mode, and narrows the absolute cold phase cloud.

## Step 63 — pure electrical rescue preserves capture

Choosing

\[
r\approx1.2635
\]

raises the baseline action to

\[
B\approx37.61
\]

with approximately

```text
C=343.3 fF
R=63.3 ohm
fc=21.57 GHz.
```

The current 14-um/20-ps sym-TWA screen retains `P~.99` through roughly `83–84 um^2`, equivalent by the reduced optical similarity to a fixed-100 scale near `11.7 um`.

Thus the architecture survives the first exact dark-action correction; the price is finite but modest.

## Step 64 — low tilt and beta-shaping rescues are falsified

Reducing positive directional tilt raises dark action, as required by the exact envelope-theorem sign

\[
\boxed{\frac{dB_{diss}}{d\delta}
=-\frac{E_L}{\hbar}\int[x_b(\tau)-x_m]d\tau<0}
\]

for a bounce toward larger phase.

But `delta=.035` loses the one-sided basin margin: at 14 um, `A=80 um^2`, the sym-TWA capture probability falls to about `.922`. The low-tilt rescue is rejected.

Increasing `beta_cold` raises the exact action efficiently but also raises the photon fold. Even a mild `beta=.825` equal-action hybrid has `A99~75–76 um^2`, worse than the pure electrical benchmark. The beta-shape family is rejected as the preferred current rescue.

## Step 65 — constant-dark-action high-tilt manifold discovered

The opposite strategy is more effective:

```text
increase positive tilt -> lower photon fold + stronger directionality
then increase C / scale R,omega_D -> restore the lost zero-T dark action.
```

For each tilt define

\[
\boxed{r(\delta)=B_\star/B_0(\delta)},
\qquad B_\star=37.61.
\]

The compensated phase clock is

\[
\boxed{\omega_{c,\star}(\delta)
=\omega_{c,0}(\delta)\frac{B_0(\delta)}{B_\star}}.
\]

The physical optimization becomes

\[
\boxed{A_{99}(\delta\mid B=B_\star)}
\]

with speed and finite-temperature dark stability retained as separate objectives.

## Step 66 — equal-action capture frontier rises strongly through delta=.14

The same 14-um/20-ps sym-TWA screen gives approximate `A99` values

```text
delta=.05 -> 83–84 um2
delta=.07 -> 103–104
delta=.09 -> ~126
delta=.10 -> ~139–140
delta=.11 -> ~152–153
delta=.12 -> ~167
delta=.13 -> high-180s
delta=.14 -> ~210.
```

The fixed-100 reduced-model equivalent therefore rises from about `11.7 um` to about `29.4 um` while holding the same zero-T action target.

This is not a real detector cutoff. It is a reduced-model Pareto result under constant absorption and lumped calorimetry.

## Step 67 — fold-normalized decomposition shows most gain is static threshold reduction

Define

\[
Q_{99}=A_{99}(T_f^2-T_0^2).
\]

Across the equal-action sweep, `Q99` rises only from roughly `40.2` at `delta=.05` to roughly `44.4` at `.14`, whereas `A99` rises by a factor about 2.5.

Therefore most of the spectral/area gain is the engineered fall of the static fold energy. Stronger directionality contributes by preventing the slower compensated phase coordinate from losing excessive dynamic basin margin.

## Step 68 — generic saddle-node asymptotic guarantees eventual critical slowing

Let

\[
\epsilon=\delta_c-\delta\to0^+.
\]

For a generic fold,

\[
\Delta U\propto\epsilon^{3/2},
\qquad
\omega_{c,0}\propto\epsilon^{1/4},
\qquad
B_0\propto\epsilon^{5/4}.
\]

Holding `B=B_star` requires

\[
r\propto\epsilon^{-5/4},
\qquad C\propto\epsilon^{-5/2},
\]

and therefore

\[
\boxed{\omega_{c,\star}\propto\epsilon^{3/2}}.
\]

Finite-time capture must therefore turn over or become impractically slow before the critical point, even though the static trigger energy continues to fall.

Under the same compensation,

\[
\sigma_{q,\star}\propto\epsilon^{1/2}
\]

while the minimum-saddle distance also scales as `epsilon^(1/2)`, so relative quantum localization does not improve parametrically without bound.

Detailed record: `CONSTANT_ACTION_TILT_ASYMPTOTIC_2026-08-15.md`.

## Step 69 — cold metastability and Euclidean-saddle limits mapped separately

Static cold topology remains bistable through approximately `delta=.26` and is absent by `.27`.

The full nonlocal spectral bounce retains one negative mode through `.25`; at `.26` the current solver produces two negative modes/poor stationarity, so `.26` is not an accepted action point.

This separates

```text
static bistability boundary
from
accepted one-negative-mode Euclidean bounce continuation boundary.
```

## Step 70 — finite-temperature dark stability becomes an independent high-tilt constraint

Equal zero-temperature action does not hold the cold barrier height fixed. As tilt increases, `DeltaU` falls while capacitance restores only the tunneling action.

At `T0=20 mK`, classical activation is fantastically suppressed through the moderate-tilt region (`DeltaU/kBT0 >265` through `.085`). Farther toward the fold the thermal exponent must eventually approach the logarithm required by the dark-rate target.

An extended diagnostic through `.22` is being used as a falsification screen. It is deliberately not treated as a physical Kramers DCR.

## Current active calculation after Step 70

Sparse equal-action capture is running at

```text
delta=.15 -> compensated fc ~7.25 GHz
delta=.16 -> ~6.33 GHz
delta=.18 -> ~4.66 GHz
```

to locate the onset of finite-time critical slowing. The numerical frontier must then be intersected with the finite-temperature dark-stability constraint before any new Generation-A operating point is named.

**Publication status remains NO-GO.**
