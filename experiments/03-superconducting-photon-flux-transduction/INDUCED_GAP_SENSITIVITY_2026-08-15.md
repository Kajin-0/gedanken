# Induced-Gap Sensitivity Checkpoint — 2026-08-15

## Purpose

Stress the surviving fold corridor against a physically important nonideality identified by the realistic graphene CPR literature: the superconducting gap induced in graphene can be smaller than the bulk MoRe gap.

This is more severe than the previous CPR-shape-only test because changing the induced gap changes simultaneously the coherence length, dimensionless doping, absolute Josephson-current scale and therefore the loop screening parameter.

## Physical sweep

Define

```math
r_\Delta=\Delta_{ind}(0)/\Delta_{0,baseline}.
```

Hold fixed:

```text
physical junction length
v_F
physical graphene chemical potential
loop inductance L_loop = 87.76 pH
external tilt delta = 0.05
baseline Ic = 3 uA at r_Delta=1
CPR shape envelope near realistic S~0.27.
```

Then the internally consistent dimensionless parameters change as

```math
\ell(r_\Delta)=r_\Delta\ell_0,
\qquad
\mu_r(r_\Delta)=\frac{\mu_{phys}}{\Delta_{ind}}=\frac{20}{r_\Delta}.
```

The cold physical `Ic` is recalibrated from the arbitrary-length Matsubara current, including its explicit energy scale, against `Ic=3 uA` at `r_Delta=1`. The loop inductance is **not** retuned as the gap changes, so

```math
\beta_L(r_\Delta)=2\pi L_{loop}I_c(r_\Delta)/\Phi_0
```

falls naturally when the induced gap weakens.

The CPR shape is simultaneously de-skewed using the empirically anchored `S~0.27` envelope from `INTERFACE_SKEWNESS_SENSITIVITY_2026-08-15.md`.

## Numerical sensitivity result

A converged cold-state check using approximately

```text
qmax=38
nq=450
wmax=15
nphi=301
Tref=30 mK
```

gives:

| r_Delta | Delta_ind [meV] | Ic,cold [uA] | beta_cold | beta_fold,cold | cold barrier/kB |
|---:|---:|---:|---:|---:|---:|
| 1.00 | 1.30 | 3.000 | 0.800 | 0.300 | 9.10 K |
| 0.60 | 0.78 | 2.361 | 0.630 | 0.313 | 3.29 K |
| 0.40 | 0.52 | 1.877 | 0.500 | 0.328 | 0.94 K |
| 0.30 | 0.39 | 1.563 | 0.417 | 0.342 | 0.21 K |
| 0.26 | 0.338 | 1.419 | 0.378 | 0.350 | 0.043 K |
| 0.24 | 0.312 | 1.343 | 0.358 | 0.355 | 0.0016 K |
| 0.22 | 0.286 | 1.262 | 0.337 | 0.360 | no cold metastable left well |

The exact critical ratio is grid/model dependent, but the qualitative threshold is clear:

```math
r_\Delta\sim0.23-0.24
```

is where the selected cold metastable well disappears for this fixed-loop, realistic-skewness illustrative point.

## Stronger result: barrier collapse precedes topology loss

The main failure is **not** the final disappearance of bistability.

Long before `beta_cold` crosses the fold threshold, the cold barrier becomes too small to plausibly support an ultra-low dark-count state:

```text
r_Delta=0.6 -> barrier ~3.3 k_B K
r_Delta=0.4 -> barrier <1 k_B K
r_Delta=0.3 -> barrier ~0.2 k_B K.
```

Thus the useful detector threshold will be substantially above the mathematical bistability threshold.

This is the first strong fragility result for the current architecture:

> A large reduction of the induced superconducting gap can preserve a formal fold while destroying useful cold-state stability.

## Coarse dynamic fold trend

A faster lower-resolution temperature sweep, using the same fixed-geometry/fixed-doping construction, gives the approximate fold-temperature trend

| r_Delta | T_fold |
|---:|---:|
| 1.0 | ~0.91 K |
| 0.8 | ~0.70 K |
| 0.6 | ~0.46 K |
| 0.4 | ~0.20 K |
| 0.3 | ~0.085 K |

These values are preliminary because the temperature sweep used a coarser integration grid than the cold barrier table. The trend, not the last digits, is the result: weakening the induced gap rapidly drives the optical fold toward the bath temperature while simultaneously removing the cold barrier.

## Interpretation

The previous ideal statement

```text
beta=0.8, mu/Delta=20 -> barrier ~16.7 K
```

has now undergone two successive realism stresses:

1. realistic-interface CPR skewness: `16.7 K -> ~9.1 K`;
2. reduced induced gap: `~9.1 K -> 3.3 K` already at `r_Delta=0.6`.

Therefore the architecture is **not** robust to arbitrary proximity weakening.

The key material/device parameter is no longer merely optical heat capacity or nominal bulk superconducting gap. It is the combination

```math
(\Delta_{ind},\;I_c,\;\text{CPR harmonics},\;L_{loop})
```

that determines whether a cold protected state and a photon-accessible fold coexist.

## Design consequence

There are two possible responses to a reduced induced gap:

1. **retune loop inductance upward** to restore `beta_cold`, at the cost of changing state separation, phase timescale and MQT/damping constraints;
2. require a sufficiently hard/high-transparency proximity interface so that `r_Delta` remains large.

This creates a new optimization problem rather than an immediate impossibility theorem.

The next calculation should ask whether inductance retuning can compensate the reduced-gap barrier collapse **without** violating the finite-dwell / MQT capacitance closure. If it can, the architecture has an engineering compensation mechanism. If it cannot, the induced-gap reduction becomes a genuine architecture-level bound.

## Status

**GO for continued theory; materially increased fragility. NO-GO for manuscript.**

This checkpoint is a sensitivity calculation within the same equilibrium ballistic/Matsubara framework, not a calibrated prediction for the Huang detector or another fabricated GJJ.
