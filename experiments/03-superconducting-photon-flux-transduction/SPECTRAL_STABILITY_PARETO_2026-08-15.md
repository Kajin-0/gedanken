# Spectral-Reach / Cold-Stability Pareto Checkpoint — 2026-08-15

## Purpose

Combine the current realistic-skewness, induced-gap and inductance-retuning results into a simple design frontier for a fixed `100 um^2` graphene absorber.

This does not add optical absorptance or stochastic capture. It asks only:

> How far in wavelength can one absorbed photon thermally cross the equilibrium fold, and what cold-stability/capacitance price accompanies that reach?

## Fixed absorber thermal reach

From the Huang thermal calibration,

```math
\lambda_{max}(A)
=\lambda_{ref}\frac{A_{ref}}{A}
\frac{T_{ref}^2-T_0^2}{T_f^2-T_0^2}.
```

For

```text
A=100 um^2
A_ref=100 um^2
lambda_ref=1.55 um
T_ref=2.5 K
T0=20 mK,
```

the retuned realistic-skewness family gives:

| r_Delta | T_fold | lambda_max for A=100 um^2 | cold barrier/kB | provisional C_min,Q | retuned L |
|---:|---:|---:|---:|---:|---:|
| 1.0 | 0.905 K | 11.83 um | 9.10 K | 161 fF | 87.8 pH |
| 0.8 | 0.813 K | 14.66 um | 8.12 K | 181 fF | 96.8 pH |
| 0.6 | 0.695 K | 20.07 um | 6.87 K | 215 fF | 111.5 pH |
| 0.5 | 0.623 K | 24.98 um | 6.10 K | 244 fF | 123.1 pH |
| 0.4 | 0.540 K | 33.27 um | 5.22 K | 287 fF | 140.3 pH |

## Pareto structure

The family is monotonic in the expected opposing directions:

```text
lower Delta_ind
 -> lower T_fold
 -> longer absorbed-photon wavelength reach
```

but simultaneously

```text
lower Delta_ind
 -> lower Ic / larger retuned L
 -> lower physical cold barrier
 -> larger provisional C_min,Q.
```

Thus no single point dominates all objectives. This is a genuine multi-objective tradeoff rather than a one-parameter optimum.

## Full 8–14-um band observation

For a `100 um^2` absorber, one absorbed 14-um photon gives approximately

```text
T_pk(14 um) ~0.832 K
```

under the same ratio calibration.

Therefore:

```text
r_Delta=1.0: Tf~0.905 K -> does not reach fold at 14 um
r_Delta=0.8: Tf~0.813 K -> barely reaches fold
r_Delta=0.6: Tf~0.695 K -> substantial thermal margin.
```

The `r_Delta~0.8` point is therefore an interesting boundary: it is approximately the first retuned point in the current coarse family that thermally spans the full conventional 8–14-um band with a `100 um^2` absorber.

However its 14-um thermal headroom is small, so it should not be treated as a robust design point before absorption efficiency, parameter disorder and stochastic capture are included.

The `r_Delta~0.6` point sacrifices cold barrier from about `9.1 K` to `6.9 K` and raises the provisional capacitance floor from `161 fF` to `215 fF`, but extends absorbed-photon reach to about `20 um` and gives much larger 14-um trigger margin.

## Strong design consequence

The current theory no longer favors the earliest `15.5 um^2` 10-um absorber estimate.

A larger `~100 um^2` absorber is attractive because:

1. it is close to an already demonstrated graphene single-photon calorimeter scale;
2. the lower full-CPR fold means it can still be triggered by a single absorbed LWIR photon;
3. it provides more physical area for optical coupling;
4. the high MoRe parent gap still leaves a large thermal-confinement margin.

The penalty is that spectral reach must then be bought through lower fold temperature, which competes directly with cold stability.

## Candidate working region, not a final design

For further falsification, the current useful bracket is roughly

```text
r_Delta ~0.6–0.8
A ~100 um^2
parent Delta_s ~1.3 meV class
retuned L ~0.10 nH
provisional C_min,Q ~0.18–0.22 pF.
```

This bracket is selected because it spans 14 um thermally while retaining multi-kelvin cold barriers in the current equilibrium model.

It is **not** a fabricated-device parameter recommendation. The microscopic meaning of `r_Delta`, realistic `Ic(T)`, dissipative MQT, absorption, and capture dynamics remain unresolved.

## Potential future theorem form

The spectral side of the closure can be written

```math
\boxed{
\lambda\le
\lambda_{ref}\frac{A_{ref}}{A}
\frac{T_{ref}^2-T_0^2}{T_f^2-T_0^2},
}
```

subject simultaneously to

```math
\Delta U_c\ge\Delta U_{req},
\qquad
C_{min,Q}<C_{max,dyn},
\qquad
T_{pk}<\Delta_s/k_B.
```

If a realistic model allows elimination of internal device parameters to produce a closed upper bound on wavelength versus required dark stability and capture time, that could be more publication-relevant than the broad detector architecture itself.

## Status

**GO for continued theory. NO-GO for manuscript.**
