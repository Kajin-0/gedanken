# Experiment 03 — Robust CPR Write Window — 2026-08-15

## Purpose

Convert CPR-shape uncertainty into a **robust design inequality** for the photon-triggered fold.

The previous ideal-interface optimum at `beta_cold~0.8` is not robust to realistic CPR rounding. This checkpoint shows that the architecture may survive by operating at a larger cold loop parameter, approximately `beta_cold~1.2` in the present envelope, and using **thermal CPR reshaping plus modest amplitude suppression** to trigger the fold.

This is an exploratory robustness result, not a novelty claim.

## 1. CPR uncertainty sets

For any normalized CPR shape `c`, let

```math
B_f[c]\equiv\beta_{fold}[c;\delta]
```

be its static normalized fold threshold at the chosen external tilt.

Let the possible cold CPRs form a set `C_0` and the possible hot CPRs form `C_h`.

Define

```math
\boxed{
B_{0,max}=\sup_{c\in\mathcal C_0} B_f[c]
}
```

and

```math
\boxed{
B_{h,min}=\inf_{c\in\mathcal C_h} B_f[c].
}
```

`B_0,max` is the most conservative cold fold in the uncertainty set; `B_h,min` is the hardest hot CPR to unfold.

## 2. Guaranteed cold bistability

If the cold circuit amplitude is

```math
\beta_{cold},
```

then robust cold bistability for **every** CPR in `C_0` requires

```math
\boxed{
\beta_{cold}>B_{0,max}.
}
```

## 3. Guaranteed hot unfolding

Let the hot critical-current amplitude ratio be

```math
g_h=I_{c,hot}/I_{c,cold}.
```

The actual hot loop amplitude is

```math
\beta_{hot}=g_h\beta_{cold}.
```

Guaranteed loss of the metastable well for **every** hot CPR in `C_h` requires

```math
\boxed{
g_h\beta_{cold}<B_{h,min}.}
```

## 4. Robust write window

Combining cold and hot requirements gives

```math
\boxed{
B_{0,max}
<\beta_{cold}
<\frac{B_{h,min}}{g_h}.
}
```

A robustly nonempty window exists only if

```math
\boxed{
g_h<\frac{B_{h,min}}{B_{0,max}}.}
```

This is the cleanest current way to separate CPR uncertainty from circuit design.

It also shows that the photon can trigger through either or both of:

```text
1. amplitude suppression: g_h < 1
2. harmonic/tail reshaping: B_h > B_0.
```

The earlier scalar-`I_c` picture included only mechanism 1.

## 5. Cold envelope from measured/self-consistent skewness

Using the admissible three-harmonic CPR construction in `cpr_skewness_envelope.py` at `delta=0.05`:

```text
S=0.27 -> beta_fold = 0.751 – 0.867
S=0.23 -> beta_fold = 0.777 – 0.956
S=0.15 -> beta_fold = 0.792 – 1.128
S=0.10 -> beta_fold = 0.803 – 1.266.
```

The broadening of the fold interval as skewness decreases is another manifestation of the fact that `S` alone does not constrain the near-`pi` tail.

For a conservative cold envelope based on the self-consistent-skewness scale

```text
S_cold ~0.15,
```

the current three-harmonic uncertainty set gives

```math
\boxed{B_{0,max}\approx1.128.}
```

Thus `beta_cold=0.8` is not robust.

## 6. Hot approximately sinusoidal limit

Nanda et al. report that the graphene CPR becomes approximately sinusoidal at sufficiently high temperature. For a sinusoidal CPR and `delta=0.05`,

```math
\boxed{B_{h,sine}=1.14712.}
```

If the hot CPR is genuinely close enough to sinusoidal that this is an adequate lower fold bound, then using the conservative cold `S=0.15` envelope:

```math
B_{0,max}=1.128,
\qquad
B_{h,min}\approx1.147.
```

Even with **no current-amplitude suppression** (`g_h=1`), the robust shape-only window is formally

```text
1.128 < beta_cold < 1.147.
```

It is very narrow, but it shows that thermal harmonic reshaping alone can in principle remove a metastable well.

With only 5% current-amplitude suppression,

```math
g_h=0.95,
```

the window becomes

```text
1.128 < beta_cold < 1.207.
```

This includes

```text
beta_cold = 1.20.
```

For `beta_cold=1.20`, a fully sinusoidal hot CPR requires only

```math
g_h<\frac{1.14712}{1.20}=0.95593,
```

or

```math
\boxed{\Delta I_c/I_c>4.41\%.}
```

This is much less demanding than the 23.5% scalar suppression of the old sinusoidal `beta=1.5` checkpoint.

## 7. Cold stability at `beta_cold=1.2`

The equal-skewness low-order CPR envelope gives the following exact cold-potential ranges for a physical `I_c=3 uA` scale.

### Measured strong-n-doping skewness scale `S=0.27`

All accepted CPRs are bistable at `beta=1.2`:

```text
DeltaU_c/k_B       = 9.64 – 13.35 K
provisional Cmin_Q = 71 – 135 fF.
```

### Conservative self-consistent skewness scale `S=0.15`

All accepted CPRs are also bistable at `beta=1.2`, but the tail uncertainty matters much more:

```text
DeltaU_c/k_B       = 1.42 – 11.46 K
provisional Cmin_Q = 86 fF – 2.28 pF.
```

Thus `beta=1.2` repairs the **existence** of cold bistability across these low-order envelopes, but the worst-case quantum-stability burden can still move by more than an order of magnitude.

The tail slope remains the quantity that must be measured/calibrated.

## 8. Revised design interpretation

The earlier ideal-interface result suggested:

```text
strongly skewed CPR
+ beta_cold ~0.8
-> low fold temperature + large ideal cold barrier.
```

The interface envelope changes the preferred strategy to something more robust:

```text
moderately larger beta_cold ~1.2
+ realistic rounded cold CPR
+ thermal reduction of higher harmonics toward sinusoidal
+ modest Ic amplitude suppression
-> hot fold crossing.
```

This design no longer depends on retaining the extreme near-`pi` slope of the rigid-boundary high-doping model.

## 9. New uncertainty that dominates the hot state

The hot condition is only robust if `B_h,min` is known.

Saying that the hot CPR has small skewness is **not enough**, because the equal-skewness envelope shows that the same `S` can have very different fold thresholds.

Therefore the next required empirical/theoretical input is not merely

```text
S(T)
```

but

```text
chi_pi(T) = -I_s'(pi,T)/Ic(T)
zeta_pi(T) = I_s'''(pi,T)/Ic(T)
```

or the full CPR tail.

The practical calibration workflow should be

```text
full CPR vs T
-> chi_pi(T), zeta_pi(T), Ic(T)
-> B_f(T,delta)
-> robust hot/cold window
-> only then choose beta_cold and L.
```

## 10. Connection to the photon-energy problem

Once a robust target `beta_cold` is selected, define `T_f` as the earliest temperature at which

```math
g(T)\beta_{cold}<B_f[T].
```

The optical threshold remains

```math
E_{fold}=\eta_{th}^{-1}\int_{T_0}^{T_f}C_e(T)dT.
```

Thus thermal harmonic reshaping can **lower `T_f` and optical energy** even when `I_c(T)` has not fallen dramatically.

This is the correct next extension of the feasibility closure.

## 11. Reproducibility

```text
calculations/cpr_skewness_envelope.py
calculations/cpr_robust_write_window.py
```

## Status

**GO for continued theory.** The `beta=0.8` high-doping ideal optimum is no longer trusted; a more robust `beta~1.2` strategy emerges under the present CPR envelopes. **NO-GO for manuscript.**
