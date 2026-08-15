# Two-Gap LWIR Absorber-Area Map — 2026-08-15

## Purpose

Translate the two-gap confinement/fold inequalities into concrete 8–14-um graphene absorber sizes using the published single-photon thermal calibration, without introducing a separately fitted Sommerfeld coefficient.

## Reference thermal calibration

Use Huang et al.'s absorbed-photon thermal scale

```text
lambda_ref = 1.55 um
A_ref      = 100 um^2
T_pk,ref   ~2.5 K
T0         = 0.02 K.
```

For graphene-like `C_e=gamma A T`, holding the retained electronic energy fraction fixed gives

```math
A(\lambda,T)
=A_{ref}\frac{\lambda_{ref}}{\lambda}
\frac{T_{ref}^2-T_0^2}{T^2-T_0^2}.
```

Thus the calculation uses only ratios; `gamma` cancels.

## Parent-gap confinement

For MoRe parent electrodes with

```text
Delta_s ~1.3 meV
```

the contact-gap temperature is

```text
T_Delta = Delta_s/k_B ~15.09 K.
```

The lower absorber-area limit required to keep the peak electronic temperature below this conservative escape scale is

```math
A_{min}=A(\lambda,T_\Delta).
```

The upper area limit that still reaches the fold is

```math
A_{max}=A(\lambda,T_f).
```

## Current retuned fold cases

Use the realistic-skewness / inductance-retuned sensitivity values

```text
r_Delta=1.0 -> T_f ~0.905 K
r_Delta=0.6 -> T_f ~0.695 K
r_Delta=0.4 -> T_f ~0.540 K.
```

These are exploratory equilibrium fold temperatures, not calibrated device predictions.

## Area windows

### 8 um

| case | A for 2.5 K | A_min, parent gap | A_max, fold |
|---|---:|---:|---:|
| r_Delta=1.0 | 19.38 um^2 | 0.532 um^2 | 147.9 um^2 |
| r_Delta=0.6 | 19.38 um^2 | 0.532 um^2 | 250.9 um^2 |
| r_Delta=0.4 | 19.38 um^2 | 0.532 um^2 | 415.8 um^2 |

### 10 um

| case | A for 2.5 K | A_min, parent gap | A_max, fold |
|---|---:|---:|---:|
| r_Delta=1.0 | 15.50 um^2 | 0.426 um^2 | 118.3 um^2 |
| r_Delta=0.6 | 15.50 um^2 | 0.426 um^2 | 200.7 um^2 |
| r_Delta=0.4 | 15.50 um^2 | 0.426 um^2 | 332.7 um^2 |

### 12 um

| case | A for 2.5 K | A_min, parent gap | A_max, fold |
|---|---:|---:|---:|
| r_Delta=1.0 | 12.92 um^2 | 0.355 um^2 | 98.6 um^2 |
| r_Delta=0.6 | 12.92 um^2 | 0.355 um^2 | 167.3 um^2 |
| r_Delta=0.4 | 12.92 um^2 | 0.355 um^2 | 277.2 um^2 |

### 14 um

| case | A for 2.5 K | A_min, parent gap | A_max, fold |
|---|---:|---:|---:|
| r_Delta=1.0 | 11.07 um^2 | 0.304 um^2 | 84.5 um^2 |
| r_Delta=0.6 | 11.07 um^2 | 0.304 um^2 | 143.4 um^2 |
| r_Delta=0.4 | 11.07 um^2 | 0.304 um^2 | 237.6 um^2 |

Canonical regression:

```text
calculations/two_gap_absorber_window.py
```

## Major correction to the early 15.5-um^2 estimate

The earlier

```text
A~15.5 um^2 at 10 um
```

was the area required to reproduce a **2.5-K** peak from one absorbed 10-um photon.

It was never the maximum area that can trigger the detector.

Once the full CPR calculation places the fold near `0.8–0.9 K`, a much larger absorber can still cross the fold. For the current baseline

```math
\boxed{
10~\mu m:\quad
0.43\lesssim A\lesssim118~\mu m^2
}
```

from the static fold/contact-gap constraints alone.

Therefore the published `~100 um^2` graphene absorber scale is already compatible with a single 10-um photon crossing the `~0.905 K` fold in this model.

For `A=100 um^2`, the same ratio scaling gives a 10-um peak near

```text
T_pk ~0.98 K,
```

which is above the `0.905-K` baseline fold but far below the MoRe parent-gap temperature.

## Fixed-area wavelength reach

For fixed absorber area,

```math
\boxed{
\lambda_{max}
=\lambda_{ref}\frac{A_{ref}}{A}
\frac{T_{ref}^2-T_0^2}{T_f^2-T_0^2}.
}
```

At `A=100 um^2`:

```text
r_Delta=1.0, Tf~0.905 K -> lambda_max ~11.8 um
r_Delta=0.6, Tf~0.695 K -> lambda_max ~20.1 um
r_Delta=0.4, Tf~0.540 K -> lambda_max ~33.3 um.
```

These are **absorbed-photon thermal thresholds**, not system detection cutoffs. Optical absorptance, antenna/cavity coupling, stochastic capture and dark stability are not included.

## Interpretation

This changes the architecture assessment materially:

1. A 10-um detector need not shrink the graphene absorber to ~15 um^2 merely to obtain enough temperature rise.
2. The lower fold created by a realistic proximity-JJ CPR allows an absorber of order `100 um^2`, which is much friendlier to optical coupling and fabrication.
3. Reduced `Delta_ind` plus inductance retuning further lowers the fold and permits larger/longer-wavelength absorbers, but this comes at the already documented cost of reduced cold barrier and larger `C_min,Q`.
4. MoRe parent-gap confinement is extremely loose compared with the fold constraint in the present temperature range.

The useful optimization is therefore no longer “make the absorber as small as possible.” It is

```text
choose A large enough for optical coupling / heat capacity robustness
but small enough that one LWIR photon still crosses T_f,
while keeping T_pk below the parent-gap leakage scale.
```

## New tradeoff exposed

For fixed `A`, lowering `T_f` extends the thermal wavelength reach approximately as

```math
\lambda_{max}\propto T_f^{-2}
```

for `T0 << Tf`.

But the same changes that lower `T_f` can reduce the cold barrier. Thus spectral reach and dark stability are opposing design objectives.

This gives a natural optimization pair:

```text
maximize lambda_max(A)
subject to DeltaU_c >= required cold-stability barrier
and M_dwell > 1.
```

## Status

**GO for continued theory. NO-GO for manuscript.**
