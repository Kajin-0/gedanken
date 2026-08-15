# Scale-Covariant Spectral / Stability / Signal Closure — 2026-08-15

## Purpose

Record an analytical elimination that emerged from the retuned induced-gap family. It explains why the numerical spectral-stability Pareto table follows an approximate square law.

This is a **conditional scaling result**, not a universal detector theorem and not a novelty claim.

## 1. One-energy-scale proximity family

Assume a Josephson weak-link family can be written approximately as

```math
I_s(\phi,T;\Delta_{ind})
=I_0(\Delta_{ind})
f\!\left(\phi,\frac{k_BT}{\Delta_{ind}}\right),
```

with

```math
I_0\propto\Delta_{ind},
```

and approximately invariant normalized CPR/load-line topology as the induced energy scale is varied.

Retune loop inductance so the cold normalized screening point remains fixed:

```math
\beta_L\propto L I_0=\text{constant}.
```

Therefore

```math
\boxed{L\propto\Delta_{ind}^{-1}.}
```

If the normalized fold occurs at a fixed reduced temperature,

```math
\frac{k_BT_f}{\Delta_{ind}}=\text{constant},
```

then

```math
\boxed{T_f\propto\Delta_{ind}.}
```

## 2. Spectral reach

For the current graphene calorimetric model

```math
C_e=\gamma A T,
```

with `gamma`, absorber area and retained thermal-energy fraction held fixed,

```math
E_{fold}\propto T_f^2.
```

Since an absorbed photon has

```math
E_\gamma=hc/\lambda,
```

the quasistatic photon threshold gives

```math
\boxed{\lambda_{fold}\propto T_f^{-2}\propto\Delta_{ind}^{-2}.}
```

The same scaling applies to any spectral threshold that remains tied to a fixed reduced-temperature point of the same scale-covariant family.

## 3. Cold barrier scale

For fixed normalized potential topology, let the dimensionless cold barrier be `u_b`. Then

```math
\Delta U_c
=\frac{\bar\Phi^2}{L}u_b.
```

Because `L~Delta_ind^-1`,

```math
\boxed{\Delta U_c\propto\Delta_{ind}.}
```

Combining with the spectral scaling gives

```math
\boxed{\lambda_{fold}(\Delta U_c)^2\approx\text{constant}.}
```

Equivalently,

```math
\boxed{\Delta U_c\propto\lambda_{fold}^{-1/2}.}
```

Thus extending wavelength by reducing the induced energy scale necessarily lowers the physical cold barrier in this model class.

## 4. Persistent circulating-current signal

Let the cold state separation be

```math
\Delta\Phi=\zeta\Phi_0
```

with approximately invariant normalized separation `zeta`. Then

```math
\Delta I=\frac{\Delta\Phi}{L}
=\frac{\zeta\Phi_0}{L}
\propto\Delta_{ind}.
```

Therefore

```math
\boxed{\lambda_{fold}(\Delta I)^2\approx\text{constant},}
```

or

```math
\boxed{\Delta I\propto\lambda_{fold}^{-1/2}.}
```

Longer spectral reach and circulating-current state separation are therefore not independent under simple inductance retuning.

## 5. Direct barrier-current elimination

At fixed normalized topology,

```math
\Delta U_c
=\frac{u_b\bar\Phi^2}{L},
\qquad
\Delta I=\frac{\zeta\Phi_0}{L}.
```

Eliminating `L` gives

```math
\boxed{
\Delta U_c
=\frac{u_b\Phi_0}{4\pi^2\zeta}\,\Delta I.
}
```

Thus physical cold barrier and circulating-current separation scale linearly together for a fixed normalized potential.

## 6. Numerical check against current retuned family

Current realistic-skewness family:

| `rDelta` | `Tf` [K] | barrier/kB [K] | `lambda_fold` [um] |
|---:|---:|---:|---:|
| 1.0 | 0.905 | 9.10 | 11.8 |
| 0.8 | 0.813 | 8.12 | 14.7 |
| 0.6 | 0.695 | 6.87 | 20.1 |
| 0.5 | 0.623 | 6.10 | 25.0 |
| 0.4 | 0.540 | 5.22 | 33.3 |

The thermal invariant

```math
\lambda_{fold}T_f^2
```

is approximately `9.7 um K^2` across the table, as expected from the fixed graphene heat-capacity calibration.

The ratio

```math
\frac{\Delta U_c/k_B}{T_f}
```

changes only from about `10.1` to `9.7` across `rDelta=1 ->0.4`.

Consequently

```math
\lambda_{fold}(\Delta U_c/k_B)^2
```

remains within roughly ten percent of a constant across the current family. The residual drift is the expected signature that the real numerical family is not perfectly scale covariant: CPR shape, reduced doping/length and normalized topology evolve somewhat with `rDelta`.

## 7. Scope and failure modes

The square law can fail if any of the following vary materially with induced scale:

```text
normalized CPR shape / fold location,
Ic not proportional to Delta_ind,
electronic heat-capacity coefficient gamma,
absorber area or thermalization fraction,
normalized state separation zeta,
normalized cold barrier u_b,
contact/interface regime,
additional independent energy scales.
```

It is therefore best treated as a **model-class scaling law** and a diagnostic for numerical families, not a universal superconducting-detector bound.

## 8. Relation to the current quantum closure

The square-law result constrains the static spectral/stability/readout axis, while

```text
QUANTUM_CAPTURE_MARGIN_CLOSURE_2026-08-15.md
QUANTUM_SPEED_SIGNAL_CLOSURE_2026-08-15.md
```

constrain quantum localization, finite-time basin margin and phase speed.

A later paper-worthy object, if one survives, would likely require combining these with a causal environment and dark-count target rather than presenting the square law alone.

## Status

**DERIVED WITHIN SCALE-COVARIANT MODEL CLASS. NO NOVELTY CLAIM.**
