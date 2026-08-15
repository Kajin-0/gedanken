# Inductance-Retuning Closure — 2026-08-15

## Question

If a reduced induced superconducting gap lowers the physical critical current and therefore the loop screening parameter `beta_L`, can the architecture simply compensate by increasing loop inductance?

The answer is **partly**. Retuning can restore the normalized potential topology, but it cannot restore the physical barrier energy for free and it worsens the minimum dynamical/MQT capacitance scales.

## Exact scaling at fixed normalized CPR shape

For a target cold screening parameter

```math
\beta=\frac{2\pi L I_c}{\Phi_0},
```

restoring the same `beta` after `I_c` falls requires

```math
\boxed{L=\frac{\beta\Phi_0}{2\pi I_c}\propto I_c^{-1}.}
```

Let the dimensionless cold barrier of the normalized CPR/load-line potential be `u_b`. The physical barrier is

```math
\Delta U = E_L u_b,
\qquad
E_L=\frac1L\left(\frac{\Phi_0}{2\pi}\right)^2.
```

Therefore, if the normalized shape is held fixed,

```math
\boxed{\Delta U\propto L^{-1}\propto I_c.}
```

This is the central result: **retuning `L` restores beta but cannot restore the physical barrier lost with `I_c`.**

Inside the current provisional MQT diagnostic,

```math
C_{min,Q}
=\frac{\hbar^2\kappa}{\alpha_Q^2\Delta U^2L}
\left[W\left(\frac{\alpha_Q\Delta U}{2\pi\hbar D}\right)\right]^2.
```

At fixed normalized shape (`u_b`, `kappa`, beta approximately fixed), `Delta U=A u_b/L`, where `A=(Phi0/2pi)^2`. Hence

```math
\boxed{C_{min,Q}\propto L\,W^2,}
```

and

```math
\boxed{\sqrt{LC_{min,Q}}\propto L\,W.}
```

The Lambert-W factor varies only logarithmically. Thus the dominant compensation penalty is approximately linear in the added inductance.

## Numerical retuning family

Use the same empirically anchored realistic-skewness (`S~0.27`) induced-gap sensitivity family, but instead of holding `L=87.76 pH` fixed, retune `L` so that

```text
beta_cold = 0.8
```

for every induced-gap ratio.

Cold-state results:

| r_Delta | Ic [uA] | retuned L [pH] | barrier/kB [K] | provisional C_min,Q [fF] | sqrt(L Cmin) [ps] | state separation [Phi0] |
|---:|---:|---:|---:|---:|---:|---:|
| 1.00 | 3.000 | 87.76 | 9.10 | 161 | 3.75 | 0.2401 |
| 0.80 | 2.721 | 96.76 | 8.12 | 181 | 4.18 | 0.2396 |
| 0.60 | 2.361 | 111.51 | 6.87 | 215 | 4.90 | 0.2390 |
| 0.50 | 2.138 | 123.13 | 6.10 | 244 | 5.48 | 0.2385 |
| 0.40 | 1.877 | 140.30 | 5.22 | 287 | 6.35 | 0.2378 |
| 0.30 | 1.563 | 168.43 | 4.19 | 363 | 7.81 | 0.2368 |
| 0.25 | 1.381 | 190.60 | 3.60 | 425 | 9.00 | 0.2361 |

Canonical regression:

```text
calculations/inductance_retuning_scaling.py
```

## Comparison with fixed-L failure

At `r_Delta=0.6`:

```text
fixed L=87.76 pH:
    beta_cold ~0.630
    barrier   ~3.29 K

retuned beta=0.8:
    L         ~111.5 pH
    barrier   ~6.87 K
    Cmin,Q    ~215 fF
```

So inductance compensation recovers a large fraction of the cold barrier, but not all of it.

At `r_Delta=0.4`:

```text
fixed L:
    barrier <1 K

retuned beta=0.8:
    L ~140 pH
    barrier ~5.22 K
    Cmin,Q ~287 fF.
```

Thus the sharp fixed-loop metastability threshold near `r_Delta~0.23–0.24` is **not an architecture-level impossibility**. It is a fixed-inductance threshold and can be moved substantially by circuit retuning.

## What remains invariant-ish under retuning

The stored-state separation in units of `Phi0` stays close to

```text
~0.236–0.240 Phi0
```

through this family because beta is restored and the normalized CPR shape changes only moderately.

However, the physical circulating-current separation scales approximately as

```math
\Delta I\sim \Delta\Phi/L,
```

so increasing `L` reduces the current readout signal even when the fractional-flux separation remains stable.

## New necessary tradeoff

Inductance compensation now exposes a three-way constraint:

```text
weaker induced gap / Ic
 -> larger L needed to preserve metastability
 -> smaller physical barrier and current-state signal
 -> larger Cmin,Q and slower minimum phase dynamics.
```

Therefore the correct optimization variable is not `beta_L` alone.

A useful dimensionless/circuit objective must simultaneously retain

```text
cold barrier / DCR margin,
optical fold temperature,
state-readout separation,
MQT capacitance floor,
finite hot-state dwell time.
```

## Strongest conclusion

**Inductance is a compensation knob, not a free cure.**

The induced-gap sensitivity does not yet yield an impossibility theorem because retuning `L` can preserve the fold and recover part of the barrier. But the scaling

```math
L\propto1/I_c,
\qquad
\Delta U\propto I_c,
\qquad
C_{min,Q}\sim L\times(\text{log corrections})
```

shows why proximity weakening inevitably consumes both stability and dynamical margin even after topology is restored.

## Next step

Combine this retuned family with the finite-hot-dwell closure. For each `r_Delta`, evaluate whether there exists any capacitance satisfying

```math
C_{min,Q}<C<\min\left(\frac{t_>}{2R_{hot}},\frac{t_>^2}{g^2L}\right).
```

Equivalently, compare

```math
t_>(E_\gamma)
```

to

```math
t_{req}^*=\max[t_{diff},g\sqrt{LC_{min,Q}},2R_{hot}C_{min,Q}].
```

That is the point at which reduced gap + retuning can become an actual feasibility boundary rather than a static sensitivity result.

## Status

**GO for continued theory. NO-GO for manuscript.**
