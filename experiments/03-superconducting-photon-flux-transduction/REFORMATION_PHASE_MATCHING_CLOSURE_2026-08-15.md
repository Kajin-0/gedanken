# Experiment 03 — Reformation Phase-Matching Closure — 2026-08-15

## Purpose

The full-CPR energy-density scan produces strongly non-monotonic capture/tangent lobes. This checkpoint gives the minimal analytical mechanism: while the metastable left well is removed, the phase evolves in a displaced hot landscape. Cooling restores bistability at an energy-dependent time, so recovery samples a particular dynamical phase.

The result is elementary oscillator dynamics and is not a novelty claim. Its value is as a design coordinate for Experiment 03.

---

## 1. Minimal displaced-hot-well model

Let `q=0` denote the pre-photon occupied coordinate. During the hot single-well stage approximate the phase potential by a harmonic well centered toward the target at `q_h>0`:

```math
\ddot q+\omega_h^2(q-q_h)=0.
```

For

```math
q(0)=0,
\qquad
\dot q(0)=0,
```

we obtain

```math
\boxed{
q(t)=q_h[1-\cos(\omega_ht)].
}
```

The phase reaches maximum target-side displacement

```math
q_{max}=2q_h
```

at

```math
\boxed{
\omega_ht=(2n+1)\pi,
}
```

and returns to its initial coordinate at

```math
\boxed{
\omega_ht=2n\pi.
}
```

If the double-well potential reforms at time `t_h`, then whether the phase is favorably positioned depends on the **dynamical phase at reformation**, not simply on quench depth.

---

## 2. Energy-dependent hot dwell creates lobes

Photon energy changes the temperature trajectory and hence the time at which the left well/saddle reform:

```math
E_\gamma
\rightarrow T(t)
\rightarrow t_h(E_\gamma).
```

Therefore

```math
\boxed{
\Theta(E_\gamma)
=\omega_h t_h(E_\gamma)
}
```

in the minimal model.

As `Theta` moves through successive phases, the reformation coordinate alternates between favorable and unfavorable regions. Hence capture can be non-monotonic in photon energy even when greater energy always suppresses the static write barrier more strongly.

This explains the current numerical observation that stronger photons can produce worse deterministic reformation states.

---

## 3. Time-dependent real detector

In the full detector the hot curvature is not constant and the causal environment carries memory/reactive phase lag. The useful generalized phase coordinate is therefore schematically

```math
\boxed{
\Theta(E)
=\int_{t_{off}}^{t_{reform}}
\omega_{eff}[t;E,Y]dt
+\phi_Y(E),
}
```

where

```text
t_off       time the metastable left branch is lost / strong softening begins;
t_reform    cooling-side branch/saddle reformation;
omega_eff   local phase-space rotation frequency along the hot trajectory;
phi_Y       additional phase shift from the causal environment/memory.
```

This expression is an organizing diagnostic, not an exact scalar reduction of the full nonlinear dynamics.

The full tangent/monodromy matrix is the exact linear object if a scalar phase is insufficient.

---

## 4. Initial uncertainty also rotates

For an undamped harmonic hot well, initial fluctuations obey

```math
\delta q(t)
=\delta q_0\cos\theta
+\frac{\delta v_0}{\omega_h}\sin\theta,
\qquad
\theta=\omega_ht.
```

If the incoming cold harmonic state has

```math
\sigma_{v0}=\omega_c\sigma_{q0},
```

then

```math
\boxed{
\frac{\sigma_q^2(t)}{\sigma_{q0}^2}
=\cos^2\theta
+\left(\frac{\omega_c}{\omega_h}\right)^2\sin^2\theta.
}
```

Thus reformation phase controls not only the mean target displacement but also the orientation/projection of the incoming quantum ellipse.

This provides a minimal explanation for the coordinate focusing seen numerically at some favorable lobes: the full phase-space uncertainty is rotated/stretched, while the `x` projection can become smaller than its cold value at the instant of reformation.

No violation of uncertainty conservation is implied.

---

## 5. Robustness criterion

A detector cannot rely on exact phase matching. A useful lobe must remain favorable under variations in

```text
photon energy / active area
rise time
Ic / induced gap
L and C
R and filter cutoff
thermal cooling law.
```

Therefore the appropriate design target is not only

```math
\Theta\approx(2n+1)\pi,
```

but also small sensitivity

```math
\boxed{
\left|\frac{d\Theta}{d\ln E}\right|
\ll 1
}
```

through the intended operating band, together with equivalent derivatives with respect to circuit/material parameters.

In the full nonlinear system these derivatives should be replaced by singular values/condition numbers of the monodromy-plus-basin map.

---

## 6. Thermal dwell saturation helps high-energy robustness

The retained clean thermal model gives a finite high-energy fold-reformation time

```math
\boxed{
 t_{f,\infty}
=\tau_0
\ln\frac{T_f^2+T_0^2}{T_f^2-T_0^2}
\approx124.4\;ps
}
```

for the current `rDelta=.6` parameters.

Therefore

```math
\frac{dt_h}{dE}\rightarrow0
```

at high deposited energy in that model.

If the asymptotic dynamical phase lies in a favorable capture region, the high-energy lobe can become **less** sensitive to further photon-energy variation rather than increasingly fine-tuned.

Conversely, if the asymptotic phase is unfavorable, simply increasing energy cannot cure the architecture; the environment/cooling/phase dynamics must be retuned.

---

## 7. Connection to area-wavelength similarity

Since the current calorimetric trajectory depends on

```math
E_\gamma/A\propto1/(A\lambda),
```

phase matching is fundamentally an absorbed-energy-density condition.

A favorable lobe can therefore be moved in wavelength by changing the thermally active area while preserving the same `Theta` trajectory, subject to the assumptions documented in

```text
THERMAL_SIMILARITY_DWELL_CLOSURE_2026-08-15.md.
```

---

## 8. Current interpretation

The numerical lobe structure should now be viewed as a **reformation phase-matching problem** rather than a simple threshold problem.

This creates two competing detector strategies:

```text
coherent strategy:
  deliberately phase-match reformation and exploit a broad robust lobe;

damped/adiabatic strategy:
  suppress phase sensitivity and make capture monotonic, accepting the FDT/damping cost.
```

Which strategy wins must be decided by the full stationary-bath and nonlinear open-system calculations.

Canonical active screens:

```text
calculations/tangent_alpha_robustness.py
calculations/stationary_fdt_wavelength_screen.py
calculations/nonlinear_fdt_twa_screen.py
```

---

## Status

**Exact minimal-model mechanism; qualitative reduction of the full nonlinear system.**

No novelty claim. No efficiency claim.

**GO for continued theory. NO-GO for manuscript.**
