# Thermal-Rise / Absorber-Geometry Closure — 2026-08-15

## Purpose

Connect the finite thermal-rise sensitivity discovered by the full deterministic RCSJ calculation to known ultrafast graphene carrier thermalization and spatial heat-transport scales.

The question is no longer merely

```text
Can one LWIR photon supply enough energy?
```

but

```text
Can that energy establish the electronic distribution seen by the Josephson CPR quickly enough to launch the required nonadiabatic phase trajectory?
```

This checkpoint separates

```text
energy/carrier thermalization
from
spatial delivery to the weak link.
```

## 1. Primary-literature ultrafast scales

### Mihnev et al., Nature Communications 7, 11617 (2016)

A combined experiment/microscopic theory of graphene hot-carrier dynamics finds that efficient carrier-carrier scattering maintains a thermalized carrier distribution. The paper states that the electron/hole populations merge into a single hot Fermi-Dirac distribution on approximately

```text
100–200 fs
```

after photoexcitation in the studied regime.

DOI: `10.1038/ncomms11617`.

### Yadav, Trushin, and Pauly, Phys. Rev. B 99, 155410 (2019)

A first-principles electron-phonon thermalization study finds a strong bottleneck as excitation energy is reduced from eV scale toward approximately `100 meV`: thermalization can move from femtosecond to picosecond scales once excitation energies become comparable to graphene optical-phonon energies.

DOI: `10.1103/PhysRevB.99.155410`.

This is directly relevant energetically because

```text
14 um -> ~88.6 meV
10 um -> ~124 meV.
```

The paper's `thermalization` observable is not identical to the effective rise time of a cryogenic proximity-Josephson CPR, so it is a scale/bound rather than a direct parameter substitution.

### Pettinger et al., arXiv:2603.13457 (2026 preprint)

Ultrafast mid-infrared graphene junction measurements report photo-thermoelectric relaxation times of roughly

```text
~2 ps below 8–9 um
~3 ps at longer mid-IR wavelengths
```

at room temperature.

This is recent primary preprint evidence that mid-IR graphene response remains ultrafast below the optical-phonon energy, but it is not a cryogenic GJJ calibration and must not be substituted directly for `tau_rise`.

## 2. Dynamic rise-time targets from the current full RCSJ model

For `A=100 um^2`, one absorbed `14 um` photon, scalar `R`, realistic-skewness CPR and the conditional clean-graphene cooling model, the full nonlinear deterministic solver gives approximately:

```text
rDelta=0.8:
  capture survives through ~9 ps rise in the ordinary tested damping region;
  capture becomes highly weak-damping / settling sensitive by ~9.5 ps;
  no ordinary tested capture at ~10 ps.

rDelta=0.6:
  capture survives through ~30 ps rise;
  no capture across a broad tested R range by ~32 ps.
```

These are model boundaries, not experimental requirements.

The key question is whether the effective electronic rise seen by the Josephson CPR can plausibly lie below these scales.

## 3. Characteristic diffusion estimate from the Huang device

Huang et al. report approximately

```text
heat-diffusion length l_D ~230 um
fitted tau_ep ~75 ns.
```

Using only the characteristic relation

```math
l_D\sim\sqrt{D\tau}
```

gives

```math
\boxed{
D_{char}\sim\frac{l_D^2}{\tau}
\approx0.705\;m^2/s.
}
```

This is a cross-device characteristic diffusion scale, not a guaranteed constant diffusivity at the exact transient energy/doping of Experiment 03.

For order-of-magnitude spatial propagation, use

```math
\boxed{t_{diff}\sim d^2/D_{char}.}
```

Representative scales are

| distance `d` | `d^2/D_char` |
|---:|---:|
| 0.6 um | ~0.51 ps |
| 1.7 um | ~4.1 ps |
| 4 um | ~22.7 ps |
| 25 um | ~0.89 ns |

Order-one factors depend on dimensionality, boundaries, source profile and the exact observable. The table is a scaling screen only.

## 4. Convert dynamic rise threshold into an absorption-distance requirement

If spatial diffusion dominates the effective CPR rise,

```math
\tau_{rise}\sim d^2/D.
```

Then a maximum acceptable rise time gives

```math
\boxed{d_{max}\sim\sqrt{D\tau_{rise,max}}.}
```

With the characteristic `D~0.705 m^2/s`:

### `rDelta~0.8`

Using the current approximate `tau_rise,max~9 ps` gives

```math
\boxed{d_{max}\sim2.5\;um.}
```

### `rDelta~0.6`

Using `tau_rise,max~30 ps` gives

```math
\boxed{d_{max}\sim4.6\;um.}
```

These distances are **conditional design scales**, not hard material constants.

## 5. Strong geometry implication

The full `100 um^2` absorber area need not be isothermal before the phase starts moving.

The relevant question is whether the energy density in the **Josephson-sensitive region** rises fast enough.

Therefore the old lumped model can fail in either direction:

```text
If it assumes the full 4 x 25 um graphene area equilibrates instantaneously,
it may be too optimistic for a photon absorbed far from the weak link.

If it requires the entire 25-um dimension to equilibrate before the CPR responds,
it may be far too pessimistic for a photon absorbed directly on/near the junction.
```

This identifies a concrete architecture constraint:

> Optical absorption should be concentrated within a few micrometres of the Josephson-sensitive weak link if the current nonadiabatic capture mechanism is to be used.

An antenna/cavity can in principle provide an optical collection area larger than the microscopic thermally active region, so optical aperture and calorimetric distance need not be identical.

## 6. Revised interpretation of the rise time

The effective `tau_rise` in the full dynamic solver should ultimately be decomposed into

```math
\boxed{
\tau_{rise,eff}
\sim
\max[
\tau_{ee/thermal},
\tau_{spread}(r_{abs}\to JJ),
\tau_{prox-response}
]
}
```

rather than treated as a generic photon pulse duration.

Current primary literature suggests:

```text
electronic distribution thermalization can be sub-ps in many graphene regimes;
~100-meV carrier relaxation can enter the ps regime;
spatial diffusion can be sub-ps across the 600-nm channel but tens of ps across a few-micron spot.
```

Thus geometry is likely at least as important as intrinsic electron-electron thermalization for the current detector concept.

## 7. Consequence for the theoretical model

The next thermal model should stop assuming a single spatially uniform `T_e(t)` from the instant of absorption.

The minimal extension is a 1D or 2D electronic heat equation

```math
C_e(T)\partial_tT
=\nabla\cdot[\kappa_e(T)\nabla T]
-P_{e-ph}(T)
+P_{abs}(r,t),
```

coupled to the Josephson phase through a local or junction-weighted electronic state

```math
T_{JJ}(t)
=\int w_{JJ}(r)T(r,t)\,d^2r
```

(or, ultimately, a nonequilibrium distribution rather than a scalar temperature).

Then

```math
F[x,T_e(t)]
```

is replaced by

```math
F[x,T_{JJ}(t)]
```

inside the first thermal approximation.

## 8. Current physical assessment

The new rise-time result does **not** kill the architecture.

The available literature contains sub-ps to few-ps electronic response scales that are shorter than the current approximately `9 ps` and `30 ps` deterministic rise thresholds, while the characteristic diffusion estimate shows that a weak link within a few micrometres of the absorbed photon can also satisfy those scales.

However, a large-area lumped absorber whose photon can land tens of micrometres from the weak link is no longer justified by the present theory.

The architecture has therefore acquired a new requirement:

```text
optical collection may be large,
but the thermal write must be spatially localized near the Josephson transducer.
```

## 9. Next step

Construct a spatial heat-transport + full-RCSJ model for at least two absorption locations:

```text
on-junction absorption
far-from-junction absorption.
```

Before that expensive step, the scalar full-dynamic solver should be used to build a dimensionless `(rise time, pulse energy, damping)` phase diagram and identify the minimum set of thermal quantities the spatial model must deliver.

## Status

**GO for continued theory. NO-GO for manuscript.**
