# Experiment 03 — Dynamic Derivation Continuation — 2026-08-15

This file continues the derivation trail after `DERIVATION_LOG_CONTINUATION_2026-08-15.md` Step 44. It records the mechanism change produced by the full nonlinear solver. `CURRENT_STATE.md` remains the compact live state.

## Step 45 — full nonlinear CPR/RCSJ integration reverses the local-ghost verdict

The local saddle-node analysis correctly found critical slowing arbitrarily near the fold, but it implicitly treated the phase as entering the soft region without substantial prior inertia.

A direct deterministic solver was built:

```text
calculations/full_dynamic_rfsquid.py
```

It precomputes the arbitrary-length graphene CPR over temperature, applies the current realistic-skewness interface envelope, constructs the full phase force, and integrates

```math
LC\ddot x+\frac{L}{R}\dot x+F[x,T_e(t)]=0.
```

The interpolated static force reproduces the retained fold values:

```text
rDelta=0.8 -> Tf~0.812 K
rDelta=0.6 -> Tf~0.694 K.
```

For one absorbed 14-um photon in the current `A=100 um^2` energy calibration and instantaneous deposition:

```text
rDelta=0.8: lower deterministic capture boundary ~111 ohm
rDelta=0.6: lower capture boundary ~32.7 ohm.
```

At `rDelta=0.6`, a high-R oscillatory/retrapping boundary appears near `~1.13 kOhm` under the retained finite-time classification.

The local ghost diagnostic had predicted the `rDelta=0.8` point would fail badly. The full solver showed that sufficiently weak damping lets the phase acquire momentum before the asymptotically soft region and carry through the transition.

**Correction:** the local ghost result is an asymptotic/regression limit, not the final capture criterion.

Record: `FULL_DYNAMIC_RCSJ_CHECKPOINT_2026-08-15.md`.

## Step 46 — finite optical/electronic rise time becomes first-order

Photon energy deposition was generalized from an instantaneous temperature jump to an exponential source in

```math
u=T_e^2,
```

with simultaneous clean-model cooling.

At 14 um:

### `rDelta=0.8`

```text
rise 0 ps  -> lower capture R ~111 ohm
rise 5 ps  -> ~166 ohm
rise 9 ps  -> ~1.14 kOhm
rise ~9.5–10 ps -> capture becomes very weak-damping/settling sensitive or disappears from ordinary tested range.
```

### `rDelta=0.6`

```text
rise 0 ps  -> lower capture R ~32.7 ohm
rise 20 ps -> ~64 ohm
rise 30 ps -> ~559 ohm
rise ~32 ps -> no capture over a broad tested R range.
```

Most importantly, successful trajectories can have

```math
T_{peak}<T_f.
```

Thus static fold disappearance is neither necessary nor sufficient for fast-pulse switching.

The mechanism was reclassified as

```text
photon-triggered nonadiabatic metastable superconducting flux switching
```

with the fold retained as the quasistatic limit.

## Step 47 — sudden-quench energy threshold explains sub-fold switching

Let `x_c` be the cold metastable phase coordinate and `x_s(T)` the hot saddle while it still exists. Define

```math
\mathcal B_q(T)
=U[x_s(T),T]-U(x_c,T)
=\int_{x_c}^{x_s(T)}F(x,T)dx.
```

For an instantaneous fixed-hot conservative quench, the threshold is

```math
\boxed{\mathcal B_q(T_q)=0.}
```

because the phase cannot move during the quench.

Full-CPR values:

```text
rDelta=0.8: Tq~0.718 K < Tf~0.812 K
rDelta=0.6: Tq~0.615 K < Tf~0.694 K.
```

For the same `100 um^2` energy calibration:

```text
rDelta=0.8: lambda_fold~14.7 um, ideal lambda_quench~18.8 um
rDelta=0.6: lambda_fold~20.1 um, ideal lambda_quench~25.6 um.
```

This produced a useful three-scale hierarchy:

```text
lambda_fold    quasistatic well-disappearance scale
lambda_dynamic actual finite-rate capture scale
lambda_quench  ideal sudden held-hot conservative energy scale.
```

For the retained scalar-R/cooling calculations,

```math
\lambda_{fold}<\lambda_{dynamic}<\lambda_{quench}.
```

These are model-defined scales, not universal detector cutoffs.

Record: `SUDDEN_QUENCH_BOUND_2026-08-15.md`.

## Step 48 — ultrafast graphene transport makes spatial geometry a new constraint

Primary graphene literature was checked because the solver's `tau_rise` threshold became decisive.

Current literature scales:

```text
Mihnev et al. 2016: hot Fermi-Dirac distribution can form on ~100–200 fs scales in studied graphene regimes.
Yadav et al. 2019: excitation near ~100 meV can enter a picosecond electron-phonon thermalization bottleneck.
Pettinger et al. 2026 preprint: room-temperature mid-IR graphene-junction relaxation ~2–3 ps.
```

These are not cryogenic GJJ calibrations, but they make a few-ps intrinsic response physically plausible.

Using Huang's characteristic `l_D~230 um`, `tau~75 ns` only as a cross-device diffusion scale gives

```math
D_{char}\sim0.705 m^2/s.
```

Then

```text
0.6 um -> ~0.5 ps
1.7 um -> ~4 ps
4 um   -> ~23 ps
25 um  -> ~0.9 ns
```

under the simple `d^2/D` estimate.

If diffusion dominates effective CPR rise,

```math
d_{max}\sim\sqrt{D\tau_{rise,max}},
```

giving rough current scales

```text
rDelta~0.8: tau_rise,max~9 ps  -> dmax~2.5 um
rDelta~0.6: tau_rise,max~30 ps -> dmax~4.6 um.
```

**New architecture requirement:** optical collection can be large, but useful absorption/energy delivery must be localized within a few micrometres of the Josephson-sensitive region in the current nonadiabatic regime.

Record: `THERMAL_RISE_GEOMETRY_CLOSURE_2026-08-15.md`.

## Step 49 — generic rate-induced tipping novelty route closed

The general dynamical mechanism of losing attractor tracking because a parameter changes too rapidly is established rate-induced tipping / nonautonomous basin-instability physics (Ashwin–Wieczorek and later work).

Therefore Experiment 03 must not claim that fast sub-fold switching itself is a new mathematical phenomenon.

The remaining possible distinction is detector-specific:

```text
single absorbed LWIR photon
+ proximity-JJ time-dependent potential
+ persistent flux capture
+ explicit cold-dark / wavelength / rise-time / damping closure.
```

Record: `RATE_INDUCED_TIPPING_COLLISION_2026-08-15.md`.

## Step 50 — exact parametric phase-work identity

For the scalar-R time-dependent phase equation,

```math
LC\ddot x+\frac{L}{R}\dot x+\partial_xU(x,T(t))=0,
```

multiplication by `xdot` gives the exact energy balance

```math
\boxed{
\frac{d}{dt}
\left[
\frac12LC\dot x^2+U(x,T)
\right]
=
U_T(x,T)\dot T
-\frac{L}{R}\dot x^2.
}
```

While a saddle `x_s(T)` exists, define

```math
\mathcal E_s
=\frac12LC\dot x^2+U(x,T)-U[x_s(T),T].
```

Since `U_x(x_s,T)=0`,

```math
\boxed{
\dot{\mathcal E}_s
=[U_T(x,T)-U_T(x_s,T)]\dot T
-\frac{L}{R}\dot x^2.
}
```

This unifies the sudden-quench threshold, finite-rise dependence and damping behavior:

```text
optical/thermal evolution performs path-dependent parametric work on the phase coordinate;
damping removes phase energy.
```

It also exposes a two-stage damping conflict:

```text
launch/crossing: excessive damping destroys useful phase energy;
capture/retrapping: some damping is useful to trap the target state.
```

Therefore a single broadband scalar resistance is unlikely to be the true optimum. A causal state/frequency-dependent environment is the correct next model, but it must obey fluctuation-dissipation and be used consistently in dissipative MQT.

Record: `PARAMETRIC_PHASE_WORK_2026-08-15.md`.

## Step 51 — dynamic CI introduced; coarse-boundary regression corrected

A pinned Experiment-03 numerical environment was added:

```text
Python 3.12.13
NumPy 2.5.1
SciPy 1.18.0.
```

Workflow:

```text
.github/workflows/experiment03-dynamic-rfsquid.yml
```

The first workflow failed because the deliberately coarse `quick` CPR grid was incorrectly asked to reproduce narrow full-resolution capture brackets. This was identified as a **test-design regression**, not a scientific contradiction.

The smoke test was separated into `calculations/full_dynamic_smoke.py`, which now guards numerical invariants rather than fine bifurcation locations. High-resolution crossover values remain scientific checkpoint outputs.

The workflow must be rechecked on the final current head before declaring the dynamic numerical stack validated.

## Current frontier after Step 51

The highest-value next work is no longer static materials optimization.

The theory now needs:

```text
1. dimensionless full-dynamic capture map;
2. spatial electronic heat transport into the Josephson-sensitive region;
3. causal Y(omega,T) instead of scalar R;
4. same environment in fluctuation-dissipation noise and dissipative MQT;
5. stochastic basin probabilities and timing;
6. only then detailed optical absorptance/readout/reset.
```

The exact parametric-work identity is the preferred reduction for analyzing the next full trajectories.

**GO for continued theory. NO-GO for manuscript.**
