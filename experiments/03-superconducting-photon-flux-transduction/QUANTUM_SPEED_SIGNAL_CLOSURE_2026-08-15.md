# Quantum Localization / Speed / Circulating-Current Closure — 2026-08-15

## Purpose

Eliminate `L` and `C` from the cold harmonic quantum-width and response-time problem, then combine the result with a local finite-time basin-margin requirement.

This result does **not** use the provisional cubic-MQT rate. It follows from the harmonic cold rf-SQUID mode plus the definition of persistent-state current separation.

It is a model identity/necessary condition, not a novelty claim.

## 1. Harmonic cold mode

Let

```math
\bar\Phi=\frac{\Phi_0}{2\pi}.
```

Near the cold metastable minimum,

```math
U(x)\simeq U_c+\frac12\frac{\bar\Phi^2}{L}\kappa_c(x-x_c)^2,
```

with effective phase mass

```math
m_x=C\bar\Phi^2.
```

Therefore

```math
\omega_c=\sqrt{\frac{\kappa_c}{LC}},
\qquad
\tau_0\equiv\omega_c^{-1}.
```

The harmonic thermal Wigner variance is

```math
\sigma_x^2
=\frac{\hbar}{2C\bar\Phi^2\omega_c}
\coth\!\left(\frac{\hbar\omega_c}{2k_BT_0}\right).
```

Using `omega_c^2=kappa_c/(LC)` gives the exact harmonic identity

```math
\boxed{
\sigma_x^2\tau_0
=\frac{\hbar L}{2\bar\Phi^2\kappa_c}
\coth\!\left(\frac{\hbar\omega_c}{2k_BT_0}\right).
}
```

## 2. Barrier form

If

```math
\Delta U_c=\frac{\bar\Phi^2}{L}u_b,
```

then

```math
\boxed{
\sigma_x^2\tau_0
=\frac{\hbar u_b}{2\kappa_c\Delta U_c}
\coth\!\left(\frac{\hbar\omega_c}{2k_BT_0}\right).
}
```

This is equivalent to the action-width identity in `QUANTUM_CAPTURE_MARGIN_CLOSURE_2026-08-15.md`.

At `T0 << hbar omega_c/k_B`,

```math
\boxed{
\sigma_x^2\tau_0
=\frac{\hbar u_b}{2\kappa_c\Delta U_c}.
}
```

Thus narrower zero-point localization at fixed barrier/topology requires a slower harmonic mode, and a faster mode requires larger zero-point width.

## 3. Eliminate the barrier in favor of persistent-state current separation

Let the two cold persistent states have modeled flux separation

```math
\Delta\Phi=\zeta\Phi_0.
```

The corresponding circulating-current separation is

```math
\Delta I=\frac{\Delta\Phi}{L}
=\frac{\zeta\Phi_0}{L}.
```

Since

```math
\Delta U_c
=\frac{u_b\Phi_0^2}{4\pi^2L}
=\frac{u_b\Phi_0}{4\pi^2\zeta}\Delta I,
```

substitution eliminates both `u_b` and `L` from the width-time-current product:

```math
\boxed{
\sigma_x^2\tau_0\Delta I
=\frac{2\pi e\zeta}{\kappa_c}
\coth\!\left(\frac{\hbar\omega_c}{2k_BT_0}\right).
}
```

At low temperature,

```math
\boxed{
\sigma_x^2\tau_0\Delta I
=\frac{2\pi e\zeta}{\kappa_c}.
}
```

Units check: `e/DeltaI` has units of time, so the identity is dimensionally consistent.

### Interpretation

Within one normalized cold topology, the following cannot all be reduced independently by changing `L` and `C`:

```text
initial phase zero-point variance sigma_x^2,
intrinsic phase timescale tau_0,
circulating-current state separation DeltaI.
```

The flux separation `zeta Phi0` itself is a separate observable and may remain comparatively stable under inductance retuning; `DeltaI` is the circulating-current scale that generates that flux state.

## 4. Add a local target-basin fidelity requirement

For a locally planar pulled-back basin boundary at signed normal distance `d_n` from the initial-state center,

```math
P_{cap}^{local}=\Phi(d_n/\sigma_x).
```

A target probability `p` requires

```math
\sigma_x^2\le\frac{d_n^2}{z_p^2},
\qquad
z_p=\Phi^{-1}(p).
```

Suppose the pulse provides an effective dynamical interval `t_avail`, and successful motion requires

```math
t_{avail}\ge g\tau_0,
```

where `g>=O(1)` represents the required number of intrinsic phase times for the relevant trajectory/capture process.

Then

```math
\sigma_x^2\tau_0
\le
\frac{d_n^2 t_{avail}}{g z_p^2}.
```

Combining with the exact harmonic identity yields the necessary condition

```math
\boxed{
\Delta I\,t_{avail}
\ge
\frac{2\pi e\zeta\,g z_p^2}
{\kappa_c d_n^2}
\coth\!\left(\frac{\hbar\omega_c}{2k_BT_0}\right).
}
```

At low temperature,

```math
\boxed{
\Delta I\,t_{avail}
\ge
\frac{2\pi e\zeta\,g z_p^2}
{\kappa_c d_n^2}.
}
```

This is a **quantum localization-speed-current necessary condition** for a locally simple basin.

## 5. Equivalent fidelity ceiling

For fixed `DeltaI`, `t_avail`, local basin distance `d_n`, topology `(zeta,kappa_c)` and trajectory factor `g`,

```math
z_p^2
\le
\frac{\kappa_c d_n^2\Delta I t_{avail}}
{2\pi e\zeta g}
\tanh\!\left(\frac{\hbar\omega_c}{2k_BT_0}\right).
```

Therefore

```math
\boxed{
P_{cap}^{local}
\le
\Phi\!\left[
 d_n
 \sqrt{
 \frac{\kappa_c\Delta I t_{avail}}
 {2\pi e\zeta g}
 \tanh\!\left(\frac{\hbar\omega_c}{2k_BT_0}\right)
 }
\right].
}
```

This should be read only as a local single-boundary harmonic ceiling. Folded/multistrip basins require the full Wigner basin-volume integral and do not reduce to one `d_n`.

## 6. Current-family scale check

Using the retuned family and the current provisional capacitance points gives approximately

```text
rDelta=.8:
  zeta~0.2396
  L~96.8 pH
  DeltaI~5.12 uA
  f_c~32.0 GHz
  tau_0~4.97 ps
  kappa_c~0.71
  sigma_x~0.116 rad.

rDelta=.6:
  zeta~0.2390
  L~111.5 pH
  DeltaI~4.43 uA
  f_c~27.3 GHz
  tau_0~5.84 ps
  kappa_c~0.70
  sigma_x~0.115 rad.
```

These values satisfy the identity to the accuracy of the retained rounded inputs.

At the 20-mK cold state the `coth` correction is negligible because `hbar omega_c/(k_B T0)~65–77`.

## 7. What this does and does not establish

### Established within the harmonic/local-basin model

- exact `sigma_x^2 tau_0 DeltaI` identity;
- finite-temperature `coth` correction;
- necessary target-probability / response-time / circulating-current inequality when the relevant basin boundary is locally single-valued and approximately planar.

### Not established

- that the current folded basin can be represented by one `d_n` globally;
- that `g` is universal;
- that the current scalar-R environment is physically optimal;
- pulse-time open-system quantum dynamics;
- dissipative MQT for the same causal environment;
- novelty of this elimination.

## 8. Research significance

This identity sharpens the design problem beyond the provisional dark-count formula. Even before specifying MQT, a cold quantum phase mode presents an intrinsic three-way relation between

```text
localization,
response time,
and circulating-current state scale.
```

It is therefore impossible to suppress initial quantum blur arbitrarily by increasing capacitance without paying a phase-speed cost.

The correct next test is to combine this closure with the numerically converged finite-time Wigner basin probability and then replace scalar-R dynamics by a fluctuation-dissipation-consistent environment.

## Status

**GO for continued theory. NO-GO for manuscript.**

No novelty claim is authorized. Generic quantum Josephson basin-capture probability is already prior art; any publishable contribution would have to be the detector-specific closure/conjunction after the full open-system treatment survives.
