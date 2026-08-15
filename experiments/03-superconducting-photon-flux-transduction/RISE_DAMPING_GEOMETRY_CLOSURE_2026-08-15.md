# Rise-Time / Damping / Geometry Closure — 2026-08-15

## Purpose

Combine the near-critical full-dynamic rise/damping boundary with the spatial electronic-delivery estimate to obtain a compact design/falsification relation connecting

```text
intrinsic thermalization time
absorption distance from the Josephson-sensitive region
electronic diffusivity
damping resistance
nonadiabatic capture.
```

This is an **asymptotic current-model closure**, not a universal theorem and not a calibrated device formula.

## 1. Near-critical dynamic boundary

The full deterministic 14-um solver gives, near the zero-damping rise-time limit,

```math
\boxed{
R_{min}(\tau_r)
\simeq
\frac{K}{\tau_c-\tau_r}
}
```

to percent-level exponent accuracy for both retained material families.

Current fitted values:

```text
rDelta=0.8:
  tau_c ~9.6279 ps
  K     ~721.9 ohm ps

rDelta=0.6:
  tau_c ~31.2947 ps
  K     ~725.2 ohm ps.
```

Details: `RATE_DAMPING_CRITICAL_SCALING_2026-08-15.md`.

The inverse law is only expected close enough to the weak-damping critical boundary that the first-order expansion in `1/R` is valid.

## 2. Decompose the effective rise time

Use the minimal additive screen

```math
\boxed{
\tau_r
\simeq
\tau_{int}
+\tau_{spread}.
}
```

Here

```text
tau_int     local electronic redistribution / thermalization / proximity-response time
tau_spread  spatial delivery time from photon absorption location to the Josephson-sensitive region.
```

For a simple diffusive scaling,

```math
\boxed{
\tau_{spread}\sim\frac{d^2}{D}.
}
```

`d` is the relevant thermal-delivery distance, not necessarily the optical aperture size.

Therefore

```math
\boxed{
\tau_r
\simeq
\tau_{int}+\frac{d^2}{D}.
}
```

This decomposition is approximate; ballistic transport, finite geometry, boundaries and nonthermal distributions can change it.

## 3. Required damping resistance for a given absorption distance

Substitute the rise decomposition into the dynamic boundary:

```math
R
\gtrsim
\frac{K}
{\tau_c-\tau_{int}-d^2/D}.
```

Thus

```math
\boxed{
R_{req}(d)
\simeq
\frac{K}
{\tau_c-\tau_{int}-d^2/D}.
}
```

The denominator must be positive.

This gives an immediate no-solution condition within the near-critical model:

```math
\boxed{
\tau_{int}+\frac{d^2}{D}
\ge\tau_c
\quad\Rightarrow\quad
\text{no finite }R\text{ reaches the weak-damping capture branch.}
}
```

This is simply the dynamic rise-time limit translated into thermal geometry.

## 4. Maximum absorption distance for a given damping environment

Invert for `d`:

```math
\boxed{
 d_{max}(R)
\simeq
\sqrt{
D\left(
\tau_c-\tau_{int}-\frac{K}{R}
\right)
}.
}
```

A real solution requires

```math
\boxed{
\tau_c
>\tau_{int}+K/R.
}
```

Thus finite damping consumes part of the rise-time budget that could otherwise be spent on spatial heat delivery.

## 5. Zero-damping geometry ceiling

As `R -> infinity`,

```math
\boxed{
 d_{max,\infty}
\simeq
\sqrt{D(\tau_c-\tau_{int})}.
}
```

For `tau_int ->0` and the current characteristic graphene scale

```math
D_char~0.705 m^2/s,
```

this gives

```text
rDelta=0.8: dmax,inf ~2.61 um
rDelta=0.6: dmax,inf ~4.70 um.
```

These reproduce the previous few-micrometre localization result using the fitted dynamic `tau_c` values rather than rounded rise thresholds.

## 6. Finite-R examples with `tau_int=0`

Using `D=0.705 m^2/s`:

### `rDelta=0.8`

```text
R = 100 ohm:
  available spatial time ~2.41 ps
  dmax ~1.30 um

R = 200 ohm:
  available spatial time ~6.02 ps
  dmax ~2.06 um

R = 500 ohm:
  available spatial time ~8.18 ps
  dmax ~2.40 um

R -> infinity:
  dmax ~2.61 um.
```

### `rDelta=0.6`

```text
R = 50 ohm:
  available spatial time ~16.79 ps
  dmax ~3.44 um

R = 100 ohm:
  available spatial time ~24.04 ps
  dmax ~4.12 um

R = 500 ohm:
  available spatial time ~29.84 ps
  dmax ~4.59 um

R -> infinity:
  dmax ~4.70 um.
```

These are asymptotic design scales, not exact capture boundaries away from the fitted near-critical region.

## 7. Add a realistic intrinsic-response budget

If local carrier/proximity response consumes, for example, a few picoseconds, subtract it directly from the spatial budget.

Illustrative `tau_int=2 ps`:

### `rDelta=0.8`

At `d=2 um`,

```math
 d^2/D\approx5.67 ps.
```

The remaining damping margin is only

```text
tau_c - tau_int - d^2/D ~1.96 ps,
```

so the asymptotic relation demands roughly

```text
R >= 0.37 kOhm.
```

### `rDelta=0.6`

The same `tau_int=2 ps`, `d=2 um` leaves about

```text
23.6 ps
```

of damping margin and gives only about

```text
R >=31 ohm.
```

This makes clear why the lower-gap `rDelta=0.6` family is dynamically more robust at 14 um even though it has a smaller cold barrier and larger provisional capacitance.

## 8. Physical interpretation

The nonadiabatic detector has a finite **rise-time budget** `tau_c`.

That budget must be shared among

```text
intrinsic carrier redistribution
spatial thermal delivery
loss of phase launch energy to damping.
```

The closure can be read schematically as

```math
\boxed{
\tau_{int}
+\frac{d^2}{D}
+\frac{K}{R}
\lesssim
\tau_c.
}
```

This is currently the cleanest engineering interpretation of the full-dynamic near-critical result.

The three terms are not all fundamental constants: `K` and `tau_c` come from the detector's nonlinear phase dynamics, while `D` and `tau_int` come from the absorber/proximity material and geometry.

## 9. Important caveats

1. The `K/R` form is a local expansion near the weak-damping critical boundary.
2. Scalar `R` will ultimately be replaced by a causal frequency-dependent admittance.
3. `d^2/D` is only a diffusive scaling estimate.
4. `tau_int` is not yet calibrated for a cryogenic single-LWIR-photon graphene Josephson junction.
5. The conditional Huang cooling model remains in the underlying full dynamic calculation.
6. The current result is deterministic; stochastic basin crossing is absent.

## 10. Next generalization

When scalar `R` is replaced by an environment, the damping-budget term should become a functional of the dissipative kernel rather than `K/R`:

```math
\frac{K}{R}
\longrightarrow
\mathcal T_Y[Y_1(\omega,T),\text{trajectory}].
```

The finite-time basin-boundary calculation should determine that functional without assuming a broadband resistor.

## Status

**GO for continued theory. NO-GO for manuscript.**
