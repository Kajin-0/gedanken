# Initial-Wigner Capture Checkpoint — 2026-08-15

## Purpose

Replace deterministic center-trajectory capture with a probability obtained by averaging the cold harmonic initial-state Wigner distribution over the finite-time pulled-back target basin.

This is a **semiclassical initial-state calculation**, not exact nonlinear quantum evolution. The initial harmonic Wigner state is exact for the assumed cold quadratic well, but each sample is then propagated with the classical nonlinear RCSJ map.

## 1. Cold quantum width

For the current retuned families at `T0=20 mK`:

```text
rDelta=.8:
  sigma_x = sigma_(v/omega_c) ~0.11559 rad
  hbar omega_c/(k_B T0) ~76.9

rDelta=.6:
  sigma_x = sigma_(v/omega_c) ~0.11499 rad
  hbar omega_c/(k_B T0) ~65.4.
```

Thus the initial width is overwhelmingly zero-point rather than thermal.

## 2. Why deterministic capture is insufficient

The pulled-back finite-time target basin is folded in the normalized initial phase plane

```math
(x,u),\qquad u=\dot x/\omega_c.
```

At fixed `x=x_c` there can be several alternating target/non-target velocity strips. Therefore

```text
center trajectory -> right basin
```

does not imply nearly unit probability once the physical initial state occupies a finite phase-space region.

The correct current figure of merit is

```math
\boxed{
P_{cap}^{init}
=\iint_{\Omega_R^0}\rho_W(x,u)\,dx\,du,
}
```

where `Omega_R^0` is the pulled-back target basin at the initial time.

## 3. Numerical integration progression

### Raw tensor Gauss-Hermite

The first implementation sampled the discontinuous basin indicator directly at tensor Gauss-Hermite nodes. It showed the effect qualitatively but had strong order dependence, especially in the folded `rDelta=.8` family.

### Geometry-aware velocity integration

The second implementation conditions on `x`, locates every velocity-basin transition, integrates the Gaussian velocity mass analytically between those transitions, then integrates over `x`.

Canonical code:

```text
calculations/quantum_basin_integral.py
```

This removed most of the discontinuity error.

### Nested standard-normal x grid

The remaining `x` dependence can also change sharply when folded basin branches enter/leave the relevant velocity range. A nested uniform grid in

```math
z=(x-x_c)/\sigma_x
```

was therefore used with composite Simpson integration. The interval `|z|<=4.5` leaves total Gaussian tail mass only

```text
6.795e-6.
```

Canonical code/workflow:

```text
calculations/quantum_basin_xgrid.py
.github/workflows/experiment03-quantum-xgrid.yml
```

Workflow run:

```text
31908931322
```

completed successfully.

## 4. Converged / near-converged results

At one absorbed `14 um` photon under the current pulse models:

### `rDelta=.6`, rise `20 ps`, `R=75 ohm`

```text
nx=9  -> Pcentral=0.801775
nx=17 -> Pcentral=0.814275
nx=33 -> Pcentral=0.813771
```

Tail-bounded result:

```math
\boxed{0.813771\le P_{cap}^{init}\le0.813778.}
```

This point is numerically converged at the current grid resolution.

### `rDelta=.6`, rise `20 ps`, `R=120 ohm`

```text
nx=9  -> 0.947483
nx=17 -> 0.962966
nx=33 -> 0.966397
```

Tail-bounded current result:

```math
\boxed{0.966397\le P_{cap}^{init}\le0.966404}
```

from omitted Gaussian tails alone. The `17 -> 33` discretization shift is about `0.0034`, so one additional x refinement is desirable before treating the fourth decimal place as converged.

### `rDelta=.8`, rise `5 ps`, `R=300 ohm`

```text
nx=9  -> 0.766456
nx=17 -> 0.768290
nx=33 -> 0.767736
```

Tail-bounded result:

```math
\boxed{0.767736\le P_{cap}^{init}\le0.767743.}
```

This point is numerically converged at the current resolution.

### `rDelta=.8`, rise `5 ps`, `R=185 ohm`

```text
nx=9  -> 0.634453
nx=17 -> 0.669465
nx=33 -> 0.683999.
```

The tail bound is tiny, but the x-discretization has not converged. A finer x grid is required for this highly topology-sensitive point.

## 5. Strong current comparison

At representative interior scalar-R points,

```text
rDelta=.6, R=120 ohm -> initial-state capture ~0.966
rDelta=.8, R=300 ohm -> initial-state capture ~0.768.
```

Thus the lower-induced-gap `rDelta=.6` family is presently favored not only by its deterministic rise-time margin but also by substantially greater robustness to the cold phase mode's zero-point spread.

This is a model comparison, not a fabricated-device efficiency prediction.

## 6. Quantum localization / action closure

Let the cold barrier be

```math
\Delta U_c=(\bar\Phi^2/L)u_b,
```

and

```math
S=\Delta U_c/(\hbar\omega_c).
```

The harmonic Wigner variance obeys exactly

```math
\boxed{
\sigma_x^2 S
=\frac{u_b}{2\kappa_c}
\coth\left(\frac{\hbar\omega_c}{2k_BT_0}\right).
}
```

At the current 20-mK operating point the `coth` factor is essentially one.

For a locally planar single basin boundary at signed normal distance `d_n`,

```math
P_{cap}^{local}=\Phi(d_n/\sigma_x).
```

Thus a deterministic boundary is locally a 50% probability contour. High fidelity requires several zero-point widths of basin margin.

Detailed derivations:

```text
QUANTUM_CAPTURE_MARGIN_CLOSURE_2026-08-15.md
QUANTUM_SPEED_SIGNAL_CLOSURE_2026-08-15.md
```

## 7. Critical model correction: this is truncated-Wigner/classical propagation

For a closed Hamiltonian phase degree of freedom

```math
H=\frac{p^2}{2m}+U(x,t),
```

the exact Wigner evolution contains

```math
\partial_t W
=-\frac{p}{m}\partial_xW
+U'\partial_pW
-\frac{\hbar^2}{24}U'''\partial_p^3W
+O(\hbar^4).
```

The present sampled-trajectory calculation keeps the classical Liouville terms and omits the Moyal corrections. Therefore it is a truncated-Wigner / semiclassical initial-state treatment.

The current cold action scale is only roughly

```text
DeltaU/(hbar omega_c) ~5.3
```

for both retained `rDelta=.8` and `.6` families using the rounded barrier/frequency values. That is not parametrically enormous, and the hot transient barrier is smaller still.

**Consequently:** this checkpoint is adequate for exposing deterministic-boundary smearing and comparing basin robustness, but not for certifying `99%+` quantum detector efficiency.

## 8. Prior-art collision

Pashin, Satanin, and Kim, Phys. Rev. E 99, 062223 (2019), studied classical and quantum dissipative Josephson dynamics and explicitly treated probability of capture into either basin of attraction.

Therefore neither

```text
quantum Josephson basin capture
```

nor

```text
probability rather than deterministic basin labeling
```

is a novelty claim for Experiment 03.

## 9. Immediate next tasks

1. finish the scalar-R probability scan and identify probability-optimal interior points;
2. refine only those points with the nested x-grid method;
3. benchmark the semiclassical Wigner propagation against an explicitly quantum nonlinear phase calculation;
4. introduce a fluctuation-dissipation-consistent Ohmic bath before quoting physical capture efficiency;
5. then replace the Ohmic bath by causal `Y(omega)` and use the same spectral density in dissipative MQT.

## Status

**GO for continued theory. NO-GO for manuscript.**
