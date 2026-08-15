# Full Nonlinear CPR/RCSJ Pulse Checkpoint — 2026-08-15

## Purpose

Replace the local saddle-node/ghost estimate with a direct deterministic integration of the full nonlinear phase force through a finite photon-heating/cooling pulse.

This is the strongest dynamical checkpoint so far. It changes the interpretation of the architecture.

The solver integrates

```math
\boxed{
LC\ddot x+\frac{L}{R}\dot x+F[x,T_e(t)]=0
}
```

with

```math
F=x-\delta-\mathcal I(x,T),
```

where `I_s(phi,T)` is precomputed from the arbitrary-length Titov–Beenakker / Hagymasi Matsubara graphene CPR, parameterized by `r_Delta`, and then de-skewed with the same `lambda=0.590` realistic-interface shape envelope that reproduces approximately `S~0.27` at the baseline.

Canonical implementation:

```text
calculations/full_dynamic_rfsquid.py
```

## 1. Thermal pulse model

Use

```math
u(t)=T_e^2(t),
```

and the retained clean-graphene cooling law

```math
\dot u
=S_u(t)
-\frac{u^2-u_0^2}{2\tau_0u_0}.
```

For finite energy-deposition rise time `tau_r`,

```math
S_u(t)
=\frac{\Delta u}{\tau_r}e^{-t/\tau_r}.
```

The integrated source deposits the same calorimetric photon energy that, without simultaneous cooling, would produce the Huang-ratio reference temperature

```math
T_{ad}^2
=T_0^2
+\frac{1.55\,\mu m}{\lambda}
\frac{100\,\mu m^2}{A}
[(2.5\,K)^2-T_0^2].
```

The retained `tau_0=75 ns` coefficient is the **conditional Huang mapping** already documented in `HUANG_THERMAL_DWELL_CALIBRATION_2026-08-15.md`. It remains a stress-test model, not a calibrated hot-state lifetime.

## 2. Static regression of the full interpolated force

The interpolated full-CPR model reproduces the current retuned static fold temperatures closely:

```text
r_Delta=0.8 -> Tf ~0.812 K
r_Delta=0.6 -> Tf ~0.694 K.
```

These agree with the current static checkpoints (`~0.813 K` and `~0.695 K`) to the retained interpolation/grid precision.

This validates that the dynamical solver is acting on the same static branch rather than a different toy potential.

## 3. First major correction: local fold-ghost diagnostic is too pessimistic when inertia survives

The previous local analysis assumed the phase dynamics sufficiently near the fold are overdamped and estimated a ghost-passage delay.

That asymptotic statement remains mathematically correct:

```math
\zeta\to\infty
```

as the instantaneous curvature goes to zero.

But the full photon problem does **not** start with the phase sitting at the fold. It starts at the **cold metastable minimum**, and the optical pulse rapidly changes the entire potential.

Therefore the phase can acquire finite velocity before entering the soft saddle-node region. That momentum can carry it across even when the local constant-peak ghost estimate predicts failure.

This is a physically important correction.

## 4. Instantaneous-deposition 14-um result

Take

```text
A = 100 um^2
lambda = 14 um
T_ad ~0.8321 K.
```

### `r_Delta=0.8`

Current parameters:

```text
L ~96.8 pH
C ~181 fF (provisional Cmin,Q)
Tf ~0.812 K.
```

Direct integration gives a lower deterministic capture boundary approximately

```math
\boxed{R_{lower}\approx111\;\Omega.}
```

Below this, damping suppresses the phase excursion and the system returns to the original left basin. Above it, over the tested range, the phase enters the favored right basin.

The local ghost diagnostic had predicted strong failure because the above-fold thermal interval was only a few ps. The full inertial result therefore **reverses that local conclusion** for sufficiently weak damping.

### `r_Delta=0.6`

Current parameters:

```text
L ~111.5 pH
C ~215 fF
Tf ~0.694 K.
```

The lower capture boundary is approximately

```math
\boxed{R_{lower}\approx32.7\;\Omega.}
```

However, the deterministic scalar-R model also develops an upper retrapping / oscillatory boundary near

```math
\boxed{R_{upper}\approx1.13\;k\Omega}
```

for the instantaneous 14-um pulse under the current 2-ns classification window.

Thus capture is a **finite dynamical resistance window**, not a monotonic function of decreasing or increasing damping.

The exact upper boundary is sensitive to the finite-time basin-classification convention and must not be promoted as a fabricated-device specification.

## 5. Finite thermal-rise time is now a decisive variable

A finite deposition rise suppresses the nonadiabatic kick and allows cooling to occur during energy deposition.

### `r_Delta=0.8`, 14 um

Representative direct integrations:

```text
rise 0 ps:   lower capture R ~111 ohm
rise 5 ps:   lower capture R ~166 ohm
rise 9 ps:   lower capture R ~1.14 kOhm
rise 9.25 ps: capture only at still weaker damping in tested grid
rise 9.5–10 ps: no capture in the ordinary tested R range; very-high-R trajectories become settling-sensitive.
```

The modeled peak temperature falls with rise time because cooling occurs during deposition:

```text
rise 5 ps  -> Tpeak ~0.775 K
rise 9 ps  -> Tpeak ~0.751 K
rise 10 ps -> Tpeak ~0.745 K.
```

These are **below the static fold temperature** `Tf~0.812 K`.

Yet the 5- and 9-ps pulses can still switch because a rapid change in a finite barrier launches a nonadiabatic phase excursion.

### `r_Delta=0.6`, 14 um

Representative results:

```text
rise 0 ps:   lower capture R ~32.7 ohm
rise 20 ps:  lower capture R ~64 ohm
rise 30 ps:  lower capture R ~559 ohm
rise ~32 ps: no capture across a very broad tested range up to ~15 kOhm.
```

Modeled peaks:

```text
rise 20 ps -> Tpeak ~0.707 K
rise 30 ps -> Tpeak ~0.681 K
rise 32 ps -> Tpeak ~0.676 K.
```

Again, the 30-ps successful trajectories can have

```math
T_{peak}<T_f.
```

## 6. Strong conceptual consequence

The detector should no longer be described, even internally, as purely

```text
photon heats above fold -> well disappears -> phase switches.
```

That is only the **slow/quasistatic limiting mechanism**.

The more general operating principle is

```text
rapid optical heating reshapes the metastable Josephson potential
-> phase is displaced / accelerated
-> trajectory may cross the transient barrier or pass through a vanished well
-> cooling reforms the potential
-> trajectory is captured in one basin.
```

Therefore

```math
\boxed{T_{peak}\ge T_f}
```

is neither necessary nor sufficient for switching in the nonadiabatic regime.

A better classification is

```text
photon-triggered nonadiabatic metastable flux latch
```

with the rf-SQUID fold providing the quasistatic organizing structure.

## 7. New dimensionless control problem

The deterministic capture boundary depends jointly on at least

```text
thermal rise time / phase time
thermal cooling time / phase time
damping ratio
pulse energy
cold distance from fold
CPR shape and temperature susceptibility.
```

Schematically,

```math
P_{capture}^{det}
=P[
\tau_{rise}/\tau_\phi,
\tau_{cool}/\tau_\phi,
\zeta,
E_\gamma/E_{fold},
\text{CPR geometry}
].
```

This is a stronger and more general formulation than the previous static spectral Pareto map.

## 8. What this invalidates

The following earlier interpretations must not be used as final design rules:

1. `T_pk >= T_f` as a necessary detector criterion;
2. time-above-fold alone as the dynamic capture criterion;
3. the local constant-peak ghost estimate as the final dynamic boundary;
4. monotonic improvement from either increasing or decreasing scalar damping;
5. a wavelength cutoff inferred only from static calorimetric fold energy.

The static fold and ghost analysis remain valuable asymptotic/regression limits.

## 9. What remains conditional

This full deterministic calculation is still not a device prediction because:

- the graphene CPR is ideal arbitrary-length theory plus an empirical shape-only interface stress;
- the thermal coefficient uses the conditional Huang mapping;
- the energy deposition rise is represented by a one-parameter exponential source;
- the environment is a scalar, frequency-independent `R`;
- `C` comes from provisional nondissipative/cubic MQT diagnostics;
- no stochastic force, dissipative MQT, readout backaction or spatially resolved absorber coupling is included.

Most importantly, the actual electron thermalization / energy-deposition rise time for an LWIR photon in the proposed geometry is now a **first-order design parameter** and must be calculated or bounded independently.

## 10. Next decisive calculation

The deterministic problem should now be generalized from scalar `R` to a causal admittance

```math
Y(\omega,T_e)=Y_1+iY_2,
```

but before that, extract a dimensionless deterministic phase diagram from the scalar-R solver:

```text
pulse rise time
x
pulse energy / wavelength
x
damping ratio
-> final basin.
```

This will identify which features are universal enough to carry into the expensive environmental/noise calculation.

The physical next input to research is the fastest credible `tau_rise` for thermalization of an absorbed 8–14-um photon into the graphene electronic distribution seen by the Josephson CPR.

## Status

**GO for continued theory. NO-GO for manuscript.**

The full deterministic integration strengthens the case for continued study but changes the mechanism from a purely static-fold latch to a nonadiabatic metastable switching problem organized by the fold.
