# Finite-Time Basin-Section Topology Checkpoint — 2026-08-15

## Purpose

Record the first full-resolution topology of the pulled-back finite-time basin boundary on the physical initial section

```math
x=x_c,
```

where `x_c` is the cold metastable phase coordinate and initial velocity is varied.

This checkpoint follows `FINITE_TIME_BASIN_BOUNDARY_CLOSURE_2026-08-15.md` and the shooting implementation in

```text
calculations/finite_time_basin_slice.py
calculations/finite_time_basin_validation.py
calculations/finite_time_basin_topology.py.
```

It resolves an important issue discovered by the first shooting test: in an underdamped regime, the pulled-back basin boundary can intersect a one-dimensional initial-velocity section **multiple times**, producing alternating final-basin strips. A single nearest edge is therefore not generally a valid robustness metric.

## 1. Validated computational state

Dedicated workflow:

```text
.github/workflows/experiment03-basin-topology.yml
```

Focused full-resolution run:

```text
run ID: 31906683219
check/job: 95065383949
conclusion: SUCCESS
```

The topology calculation uses the full CPR grid and a `0.6 ns` final classification horizon, matching the established moderate-resistance full-dynamic boundary calculations.

The earlier larger topology scan hit the Actions time limit; that was a computational-cost issue, not a physical contradiction. The focused run restricts the velocity range to the neighborhood relevant to the cold initial quantum state and refines every detected basin transition by bisection.

## 2. `r_Delta=0.6`: comparatively simple section

For one absorbed `14 um` photon and `20 ps` energy-deposition rise:

### `R=55 ohm`

Physical initial state:

```text
v=0 -> left basin
```

Resolved edges in normalized velocity `v/omega_c`:

```text
-0.116223   right -> left
+0.942786   left  -> right
```

### `R=64 ohm`

```text
v=0 -> left basin
```

Edges:

```text
-0.012805   right -> left
+0.997314   left  -> right
```

### `R=75 ohm`

```text
v=0 -> right basin
```

Edges:

```text
+0.091809   right -> left
+1.054407   left  -> right
```

Cold mode scale:

```text
omega_c/(2 pi) ~27.081 GHz.
```

### Interpretation

In the neighborhood of the physical `v=0` state, this family behaves as a relatively simple broad basin strip. The lower edge moves continuously through `v=0` between roughly `64` and `75 ohm`, consistent with the independently established physical capture boundary near `~64 ohm` for this `20 ps` pulse.

Thus for this operating family, a **single local finite-time basin branch** is a plausible first approximation to initial-state robustness.

## 3. `r_Delta=0.8`: strongly folded / multistrip section

For the same absorbed `14 um` photon but `5 ps` rise:

Cold mode scale:

```text
omega_c/(2 pi) ~31.966 GHz.
```

### `R=150 ohm`

Physical initial state:

```text
v=0 -> left basin
```

Resolved edges:

```text
-0.014885   right -> left
+0.509961   left  -> right
+1.019812   right -> left
```

### `R=166 ohm`

Physical initial state:

```text
v=0 -> left basin
```

Resolved edges:

```text
-0.542261   right -> left
-0.002698   left  -> right
+0.526245   right -> left
+1.037805   left  -> right
```

### `R=185 ohm`

Physical initial state:

```text
v=0 -> right basin
```

Resolved edges:

```text
-0.483777   right -> left
+0.773718   left  -> right
```

## 4. Critical caveat: the listed `r_Delta=0.8` edge sequence is not complete

The physical basin label and the coarse ordered transition list cannot always be reconstructed by simply alternating labels between the listed edges. For example, the `R=166 ohm` section reports `v=0 -> left`, even though a naive interpretation of the four detected transitions can imply otherwise depending on the starting interval label.

This is **not evidence that the physical v=0 full integration is wrong**. It indicates that the uniform velocity scan is still missing one or more sufficiently narrow basin strips / closely spaced manifold crossings between sample points.

Therefore the correct statement is:

```text
The r_Delta=0.8 pulled-back finite-time basin section is strongly folded and contains unresolved narrow substructure near the physical initial state.
```

Do **not** claim:

```text
fractal basin boundary
chaotic scattering
Wada basins
or any stronger dynamical classification
```

without dedicated convergence/refinement analysis.

## 5. Consequence for deterministic robustness

A binary deterministic statement

```text
(x_c,0) -> right
```

is insufficient to characterize robustness in the strongly folded regime.

Small initial phase-space perturbations can cross nearby alternating basin strips even when the nominal deterministic trajectory captures successfully.

Thus the useful detector metric is no longer only

```text
capture / no capture for a single point.
```

It must become

```text
probability mass of the cold initial quantum state lying in the target pulled-back basin(s).
```

This moves Experiment 03 naturally from deterministic trajectory mapping into a quantum/semi-classical initial-state probability calculation.

## 6. Cold phase state's quantum spread is relevant

The retained cold harmonic estimates in `QUANTUM_INITIAL_BASIN_MARGIN_2026-08-15.md` give approximately

```text
r_Delta=0.8:
  f_c ~32 GHz
  hbar omega/(k_B T0) ~77
  sigma_x ~0.116 rad
  sigma_v/omega_c ~0.116

r_Delta=0.6:
  f_c ~27 GHz
  hbar omega/(k_B T0) ~65
  sigma_x ~0.115 rad
  sigma_v/omega_c ~0.115.
```

The phase degree of freedom is therefore strongly in the quantum harmonic regime at `20 mK`, and its zero-point Wigner spread is not negligible compared with the normalized basin-edge positions above.

Example:

```text
rDelta=.8, R=150 ohm:
nearest detected edge |v|/omega_c ~0.015 << sigma_v/omega_c ~0.116.
```

So a single deterministic initial point is plainly not a high-fidelity approximation at this operating point.

## 7. Local single-boundary approximation survives only in simple sections

If one smooth basin branch dominates the support of the initial Wigner distribution, approximate

```math
v-v_b-s_b(x-x_c)=0
```

and use the covariance-normalized distance

```math
Z_B
=-\frac{v_b}
{\sqrt{\sigma_v^2+s_b^2\sigma_x^2}}
```

with

```math
P_R^{(init)}\simeq\Phi(Z_B).
```

This may be useful for the current `r_Delta=0.6` family.

For the strongly multistrip `r_Delta=0.8` family, this one-boundary approximation is not justified unless adaptive topology refinement shows that all other branches lie outside the appreciable Wigner support.

The correct expression is

```math
\boxed{
P_R^{(init)}
=\int_{\Omega_R^0}\rho_W(x,v)\,dx\,dv,
}
```

where `Omega_R^0` is the full union of target-basin regions in the pulled-back initial phase plane.

## 8. Preferred next calculation

Do **not** spend large computational effort tracing every deterministic manifold filament before asking the probability question.

Instead evaluate the initial-state probability directly:

1. use the harmonic cold Wigner distribution as the first controlled initial-state model;
2. integrate the full deterministic pulse for quadrature / quasi-Monte-Carlo samples in `(x,v)`;
3. estimate

```text
P_R^(init)
P_L^(init)=1-P_R^(init)
```

for selected points below, near and above the deterministic `R_min` boundary;
4. compare `r_Delta=0.6` simple-strip and `r_Delta=0.8` multistrip cases;
5. quantify convergence with sample number / quadrature order;
6. only afterward add noise acting *during* the pulse.

A useful initial target is to determine how far beyond the deterministic capture threshold one must move to obtain

```text
P_R^(init) > 0.9
P_R^(init) > 0.99
```

from initial zero-point uncertainty alone.

## 9. Current interpretation

The deterministic nonadiabatic mechanism survives, but the `r_Delta=0.8` operating region is substantially less robust than a binary full-trajectory result suggested.

The lower-gap `r_Delta=0.6` family currently has three simultaneous advantages at `14 um`:

```text
larger finite-rise margin
lower required launch resistance
simpler local pulled-back basin topology.
```

Its disadvantages remain

```text
smaller cold barrier
larger provisional C_min,Q
and therefore potentially worse quantum dark stability / circuit cost.
```

This sharpens the actual optimization problem rather than resolving it.

## Status

**FINITE-TIME BASIN SECTION: VALIDATED AND NONTRIVIAL.**

**r_Delta=0.6: locally simple single-strip approximation appears plausible in tested range.**

**r_Delta=0.8: strongly folded / multistrip topology with unresolved narrow substructure; single-edge robustness metric rejected.**

**GO for continued theory. NO-GO for manuscript.**
