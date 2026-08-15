# Experiment 03 — Deposition-Efficiency Thermal Similarity — 2026-08-15

## Correction to the area-wavelength similarity

The retained lumped electronic thermal model is driven by the energy that actually reaches the modeled electronic subsystem on the write timescale, not by incident photon energy automatically.

Let

```math
E_{dep}=\eta_{dep}\frac{hc}{\lambda},
```

where `eta_dep` includes the net fast-path energy fraction relevant to the modeled electronic temperature excursion. It can include optical absorptance, antenna/cavity delivery, and ultrafast partition losses, but it must not double-count processes already represented in the thermal model.

Since

```math
C_e=\gamma A T,
```

the photon-induced increment in `u=T^2` scales as

```math
\Delta u
\propto
\frac{E_{dep}}{A}
\propto
\boxed{
\frac{\eta_{dep}}{A\lambda}
}.
```

Thus the correct reduced-model similarity variable is

```math
\boxed{
\Xi=\frac{\eta_{dep}}{A\lambda}.
}
```

The earlier `A lambda = const` closure is the special case of fixed `eta_dep`.

## Mapping the favorable energy-density lobe to 14 um

The current strongest thermal trajectory is the one produced in the model by

```text
lambda_ref = 8 um
A_ref = 100 um^2
eta_dep,ref = 1
```

under the original full-deposition calibration.

To reproduce that trajectory at `lambda=14 um`, require

```math
\frac{\eta_{dep}}{A_{14}(14)}
=
\frac{1}{100(8)}.
```

Therefore

```math
\boxed{
A_{14}
=100\frac{8}{14}\eta_{dep}
\simeq57.14\eta_{dep}\;\mu m^2.
}
```

Examples:

```text
eta_dep = 1.0  -> A14 ~57.1 um^2
eta_dep = 0.8  -> A14 ~45.7 um^2
eta_dep = 0.5  -> A14 ~28.6 um^2
eta_dep = 0.2  -> A14 ~11.4 um^2
eta_dep = 0.1  -> A14 ~5.7 um^2.
```

These are thermal-active areas, not necessarily optical collection areas. Antenna/cavity concentration can in principle decouple collection aperture from electronic heat capacity.

## Spatial-delivery consequence

Using only the retained cross-device orientation scale

```math
D_{char}\sim0.705\;m^2/s,
```

and a square active region heated near its center,

```math
t_{diff}\sim\frac{A}{4D}.
```

Along the 14-um similarity line,

```math
\boxed{
t_{diff}\propto A\propto\eta_{dep}.}
```

So reduced fast deposition efficiency forces a smaller thermal volume, which also shortens the crude diffusion distance/time. This does not make low efficiency free: concentrating the photon into a smaller electronic subsystem becomes an increasingly stringent optical/geometric requirement.

## Design interpretation

The current 14-um candidate should therefore be described by the required **fast deposited energy density** rather than by a single fixed area:

```text
favorable write trajectory
<=>
eta_dep/A ~ 1/(57.1 um^2)
for a 14-um photon
```

inside the retained thermal model.

A future optical calculation must provide `eta_dep` on the same ~10–30 ps write timescale. A large eventual absorptance is insufficient if substantial energy leaves the electronic weak-link subsystem before it can reshape the CPR.

## Status

**Exact scaling inside the retained lumped calorimetric model.**

No absorptance value is assumed or claimed. The optical/deposition gate is now quantitative rather than deferred.

**GO for continued theory. NO-GO for manuscript.**
