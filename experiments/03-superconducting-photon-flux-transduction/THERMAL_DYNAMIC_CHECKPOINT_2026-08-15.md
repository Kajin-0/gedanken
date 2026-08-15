# Experiment 03 — Thermal/Dynamic Checkpoint — 2026-08-15

## Purpose

Record the first joined optical-thermal-circuit timescale check after replacing the fixed-barrier photon model with rf-SQUID fold triggering.

This is an exploratory checkpoint, not a validated device design or novelty claim.

## Published graphene benchmark used

Huang et al., Nature Communications 17, 3845 (2026), DOI `10.1038/s41467-026-70648-0`, reports for its graphene single-photon bolometer:

```text
graphene area                  4 um x 25 um = 100 um^2
junction length                600 nm
junction width                 1.7 um
fit T_1p                       2.5 K
fit tau_ep                     75 ns
thermal diffusion length l_D   ~230 um
clean-graphene E-Ph exponent   delta = 4
```

The paper models heat transport through

```math
\partial_t T_e^2
=\mathcal D\,\partial_x^2T_e^2
-\tau_{ep}^{-1}(T_e^\delta-T_0^\delta),
```

and reports `l_D=sqrt(D tau_ep) ~ 230 um`. The device response is experimentally consistent with rapid heat diffusion across a 25-um-scale absorber before strong E-Ph loss.

## Inferred characteristic diffusivity

Using only the reported characteristic scales,

```math
\mathcal D\sim l_D^2/\tau_{ep}
```

gives

```text
D ~ 0.705 m^2/s.
```

This is a cross-device inference, not a measured value for the proposed device.

## Target-absorber diffusion scale

The earlier 10-um photon heat-capacity scaling produced a working absorber area

```text
A = 15.5 um^2,
```

corresponding to a square side

```text
L_abs = 3.94 um.
```

The characteristic diffusion time is then

```math
t_{diff}\sim L_{abs}^2/\mathcal D
```

or

```text
t_diff ~ 22 ps.
```

Thus

```text
tau_ep / t_diff ~ 3.4e3.
```

Under the published characteristic scaling, a few-micron absorber should become approximately electronically isothermal far faster than the E-Ph timescale.

## Comparison with phase dynamics

The present sinusoidal rf-SQUID benchmark has

```text
sqrt(LC)                  = 5.74 ps
first central phase pass  ~20 ps
```

for a square pulse from `beta_cold=1.5` to `beta_hot=1.05<beta_c` in the deterministic RCSJ diagnostic.

Therefore

```text
t_diff ~ t_phase ~ O(20 ps) << tau_ep ~75 ns.
```

The important consequence is that thermal spreading to a nearby Josephson weak link and phase response occur on comparable tens-of-picoseconds scales in the present cross-device estimate; neither is automatically a nanosecond bottleneck.

## Hot-state damping requirement

The simple RCSJ envelope scale is

```math
\tau_{damp}\sim2R_{hot}C.
```

With

```text
C=200 fF,
```

requiring damping within a useful hot interval `t_hot` gives

```math
\boxed{R_{hot}<t_{hot}/(2C).}
```

Representative bounds:

```text
t_hot = 75 ns   -> R_hot < 187.5 kOhm
t_hot = 30 ns   -> R_hot <  75.0 kOhm
t_hot = 10 ns   -> R_hot <  25.0 kOhm
t_hot =  3 ns   -> R_hot <   7.5 kOhm
t_hot =  1 ns   -> R_hot <   2.5 kOhm
```

The published 75-ns value is used only as an effective thermal benchmark. The actual time during which the proposed CPR lies beyond the fold must be derived from `T_e(t)` and `I_s(phi,T_e)`.

## Necessary dynamic-margin formulation

Define

```math
\mathcal M_{dyn}
=\frac{t_{>fold}}
{\max(t_{diff},t_{phase},t_{damp})}.
```

High-fidelity deterministic capture should require at least

```math
\mathcal M_{dyn}\gg1,
```

plus the correct sign of the external tilt and sufficiently low stochastic wrong-way capture during recovery.

This is a necessary timescale condition, not a sufficient switching theorem.

## Current interpretation

The first combined timescale check does **not** reveal an obvious dynamic contradiction. The likely bottleneck has moved to

```text
actual nonequilibrium I_s(phi,T_e)
+ exact time above the fold
+ hot-state damping/retrapping
+ cold dissipative MQT/thermal DCR.
```

The use of a few-micron absorber also means free-space optical collection should not be conflated with absorber area; realistic LWIR operation will likely require antenna/cavity concentration.

## Reproducibility

```text
calculations/thermal_diffusion_margin.py
calculations/dynamic_margin.py
```

## Status

**GO for continued theory. NO-GO for manuscript.**
