# Experiment 03 — 14-um Mahalanobis Basin Checkpoint — 2026-08-15

## Question

The fully stationary-history linear-FDT state at the original `14 um`, `A=100 um^2` operating point has a very long, thin covariance ellipse at cooling-side reformation. Its coordinate-only margin `(x-x_s)/sigma_x` is below one, but that alone cannot prove poor basin robustness if the finite-time target basin happens to align with the covariance filament.

A conditional finite-time basin scan was therefore performed in covariance-whitened `(x,u)` coordinates.

Canonical calculation:

```text
calculations/mahalanobis_basin_margin14.py
.github/workflows/experiment03-mahalanobis-basin14.yml
run 31914295908
```

This is a conditional geometry screen, not a physical efficiency calculation: future bath noise is omitted, bath-memory variables are fixed to the deterministic reformation values, and the covariance itself comes from linear symmetrized-FDT response.

---

## 1. Construction

At cooling-side reformation define reduced state

```math
z=(x,u),
\qquad u=\dot x/\omega_c,
```

with deterministic mean `mu` and stationary-history covariance `Sigma`.

Whiten perturbations using

```math
\delta z=r\,\Sigma^{1/2}e_\theta.
```

For each direction `theta`, propagate the full nonlinear causal-filter recovery with the same deterministic thermal/filter-memory state and classify the future target basin.

The minimum standardized radius at which a non-right trajectory is found is a conditional approximation to the nearest Mahalanobis basin boundary.

---

## 2. Results

### alpha = 0.20

```text
principal rms widths = [0.01516, 1.14427]
deterministic reformation state = (+0.61220,+0.38079)
nearest non-target radius r_M ~0.1924
boundary label = left
```

### alpha = 0.35

```text
principal rms widths = [0.01751, 1.21624]
deterministic state = (+0.49869,+0.35512)
nearest non-target radius r_M ~0.2490
boundary label = left
```

### alpha = 0.50

```text
principal rms widths = [0.01969, 1.23851]
deterministic state = (+0.42135,+0.33060)
nearest non-target radius r_M ~0.4287
boundary label = left
```

The nearest failure direction is not simply the negative-x projection. The folded finite-time basin cuts across the long covariance filament in phase space.

---

## 3. Gaussian-disk comparison

For a 2D Gaussian, if an entire Mahalanobis disk of radius `r_*` lies inside the target basin,

```math
P_T\ge1-e^{-r_*^2/2}.
```

A sufficient radius for a 99% lower bound is

```math
r_*=3.035.
```

The current conditional nearest-boundary radii

```text
0.192, 0.249, 0.429
```

are orders of magnitude smaller in probability-space terms.

This does **not** imply that the physical target probability equals the mass of such a small disk; the basin is highly nonconvex and can contain large regions outside the nearest boundary. It does prove that there is no large isotropic Gaussian safety ball around the mean at the original 14-um point.

---

## 4. Interpretation

The earlier concern

```text
coordinate-only <1-sigma margin may be a harmless projection artifact
```

is rejected for the original `14 um`, `A=100 um^2` point.

The failure basin genuinely approaches the high-probability stationary-history region along the elongated phase-space direction.

This is consistent with the stronger nonlinear causal-FDT TWA result, which gives only roughly `0.88` final target fraction for this operating point in the current alpha~0.5 environment.

Therefore the original 14-um/A100 state should now be classified as

```text
fragile / near-no-go operating point
```

rather than merely

```text
ambiguous because of covariance orientation.
```

---

## 5. Architecture implication

The route forward is not to reinterpret the original 14-um state more favorably. It is to move the detector to a different absorbed-energy-density / environment lobe, using the thermal similarity

```math
A\lambda=\mathrm{const}
```

where valid.

The strongest current candidate is the higher-energy-density branch corresponding to approximately `8 um` at `A=100 um^2`, which maps thermally to `14 um` at `A~57.1 um^2` inside the reduced calorimetric model.

That branch now needs direct nonlinear stationary-bath optimization in `Y(omega)`, external tilt and circuit retuning; tangent/Mahalanobis geometry alone is no longer sufficient.

---

## Status

**Derived conditional basin-geometry result.**

No physical efficiency claim. No novelty claim.

**Original 14-um/A100 point: strongly disfavored. Architecture overall: still GO for continued theory. NO-GO for manuscript.**
