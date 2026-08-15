# Experiment 03 — Dynamical Capture Lobes — 2026-08-15

## Purpose

A full-CPR tangent scan versus photon wavelength was performed after the stationary-history FDT calculation showed that the marginal `14 um` operating point is extremely susceptible to amplified quantum uncertainty.

The initial hypothesis was simple:

```text
shorter wavelength / more absorbed energy
 -> deeper quench past the fold
 -> less time in the soft near-fold region
 -> monotonically better standardized write margin.
```

The calculation rejects that monotonic hypothesis for the current underdamped causal environment.

The relevant response is **lobed in absorbed energy**, because changing photon energy also changes the hot-state dwell and therefore the dynamical phase at which the double-well landscape reforms.

This checkpoint concerns deterministic tangent propagation of the initial phase-mode covariance. It is not a physical capture probability and does not include the full stationary bath history.

---

## 1. Calculation

Canonical script/workflow:

```text
calculations/initial_quantum_tangent_scan.py
.github/workflows/experiment03-tangent-wavelength.yml
run 31913696689
```

Model:

```text
rDelta = 0.6
R = 250 ohm
rise = 20 ps
A = 100 um^2
full CPR interpolation extended to Tmax=0.95 K
```

For the cold phase-mode covariance, propagate the deterministic tangent map from `t=0` to cooling-side left-well reformation.

If the terminal observable is `x(t_reform)` and the adjoint at `t=0` is

```math
\lambda(0)=
(\lambda_x,\lambda_v,\ldots),
```

then the contribution from the initial reduced phase ellipse is

```math
\boxed{
\sigma_{x,f}^{2}
=
(\lambda_x\sigma_{x0})^2
+(\lambda_v\omega_c\sigma_{u0})^2.
}
```

Define the coordinate-standardized reformation margin

```math
M_x
=
\frac{x_{det}(t_f)-x_s(t_f)}{\sigma_{x,f}}.
```

This is only a tangent diagnostic; it is not the full basin Mahalanobis distance and not a probability.

---

## 2. Thermal pulse depth

Current finite-rise thermal model gives approximately

```text
lambda  T_peak
8 um    0.88581 K
9       0.84551
10      0.81069
11      0.78018
12      0.75312
13      0.72890
14      0.70704
15      0.68716
16      0.66898 K
```

with

```text
Tf ~0.6944 K.
```

Thus `8–14 um` remove the static left well in this pulse model while `15–16 um` do not. This statement is only about static fold removal; nonadiabatic sub-fold switching can still exist elsewhere in parameter space.

---

## 3. Strong non-monotonicity

### `alpha = omega_D/omega_c = 0.50`

The phase-only tangent margin is

```text
lambda   M_x     sigma_x,f [rad]   x_reform
8 um     26.17       0.0489        +0.9853
9         6.13       0.1928        +0.8872
10        4.62       0.1829        +0.5488
11        6.29       0.0836        +0.2304
12        1.96       0.2929        +0.2791
13        2.33       0.5169        +0.9092
14        0.67       1.0678        +0.4214.
```

Most strikingly, at `8 um`

```math
\sigma_{x,f}\approx0.049\;rad,
```

which is **smaller** than the cold phase width `~0.115 rad`: the deterministic tangent map has focused the initial phase ellipse into the coordinate direction at the instant of reformation.

At `11 um`, a similar coordinate focusing occurs with

```text
A_phase ~0.73,
sigma_x,f ~0.084 rad.
```

This does not violate uncertainty conservation: the full phase-space ellipse can rotate/stretch while one coordinate projection narrows. The full open-system covariance must be checked.

### `alpha = 0.35`

```text
lambda   M_x
8        0.27
9        0.39
10       1.09
11       2.78
12       1.63
13       1.90
14       0.71.
```

### `alpha = 0.20`

```text
lambda   M_x
8        +0.22
9        -2.03
10       -0.06
11       +0.63
12       +1.28
13       +1.59
14       +0.81.
```

At `9–10 um`, the deterministic center itself reforms on the wrong side of the saddle despite the stronger photon.

Therefore more absorbed energy is **not** a monotonic fidelity improvement in the current underdamped environment.

---

## 4. Physical interpretation

Changing photon energy changes at least two things simultaneously:

```text
quench depth
+
hot-state dwell / reformation time.
```

The phase/filter system evolves coherently during that interval. Reformation therefore samples different positions and velocities as absorbed energy changes.

Schematically,

```text
photon energy
 -> thermal trajectory T(t)
 -> time-dependent Josephson potential
 -> phase-space rotation/stretching
 -> double-well reformation at a particular dynamical phase
 -> capture lobe.
```

The reformation time shifts monotonically with wavelength in the current model,

```text
8 um  -> ~107.2 ps
9     -> ~100.1 ps
10    -> ~92.8 ps
11    -> ~85.3 ps
12    -> ~77.3 ps
13    -> ~68.6 ps
14    -> ~57.7 ps,
```

but the reformation phase-space point and tangent covariance do not vary monotonically.

This is why the response forms lobes rather than a simple threshold.

---

## 5. Wavelength is not the fundamental control variable

The retained graphene calorimetric mapping has approximately

```math
T_{pk}^2-T_0^2
\propto
\frac{E_\gamma}{A}
\propto
\frac{1}{A\lambda}
```

at fixed absorptance and rise model.

Therefore the observed fixed-area wavelength lobes are more fundamentally **absorbed-energy-density lobes**.

Changing active area, optical concentration or absorptance shifts the corresponding wavelength locations.

Do not report the lobe locations as material-intrinsic spectral resonances.

---

## 6. Replace a scalar fidelity cutoff by an acceptance set

If capture probability is non-monotonic in wavelength, a scalar definition

```math
\lambda_\epsilon
=\sup\{\lambda:P_{cap}(\lambda)\ge1-\epsilon\}
```

can hide internal failure bands.

The more correct object is

```math
\boxed{
\Lambda_\epsilon
=
\{\lambda:
P_{cap}(\lambda;Y,\tau_r,A,\ldots)
\ge1-\epsilon\}.
}
```

For an underdamped coherent latch, `Lambda_epsilon` may be a union of disconnected intervals.

A single detector cutoff becomes meaningful only if the response has been made sufficiently monotonic by design, damping/dephasing, control shaping, or an explicitly defined lower-envelope criterion.

---

## 7. Relation to unstable-gain closure

The tangent amplification itself is not a fidelity metric. As shown in

```text
UNSTABLE_GAIN_FIDELITY_CLOSURE_2026-08-15.md
```

an unstable linear stage amplifies directional mean displacement and incoming uncertainty through the same propagator.

The relevant quantity is standardized distance to the actual finite-time basin boundary, not raw gain.

The current tangent scan only uses the instantaneous saddle coordinate as the denominator reference. Because the full stationary covariance at `14 um` is a long, thin phase-space filament, the next geometry calculation must use the basin boundary in the covariance/Mahalanobis metric.

---

## 8. Immediate falsification target

The `alpha=.50`, `8–11 um` region is the strongest current escape route from the marginal-14-um no-go signal.

A stationary-history FDT wavelength screen is now required:

```text
same causal Y(omega)
+ fully equilibrated cold prehistory
+ pulse-time linear FDT history
+ shorter-wavelength thermal trajectories.
```

If the multi-sigma short-wavelength tangent margins survive that stronger calculation, Experiment 03 has a **spectral-fidelity window** rather than an architecture-level failure.

If the stationary bath again produces order-basin-scale uncertainty throughout `8–11 um`, the causal-environment branch moves substantially closer to a no-go conclusion.

Canonical next workflow:

```text
.github/workflows/experiment03-stationary-fdt-wavelength.yml
```

---

## Status

**Derived numerical model result / architecture insight.**

No novelty claim. No physical efficiency claim.

**GO for continued theory. NO-GO for manuscript.**
