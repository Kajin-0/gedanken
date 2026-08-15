# Experiment 03 — NOVELTY_GATES

No manuscript directory should be created until these gates are explicitly reviewed.

## Gate 1 — quantitative survival

The coupled thermal + stochastic circuit model must produce a physically plausible nonempty parameter region where all of the following can hold simultaneously:

```text
single-photon capture probability       high (initial target > 0.9)
preferred-direction capture             high (initial target > 0.9)
intrinsic false-switch rate             low (exploratory target < 1e-6 s^-1)
persistent post-event flux state        stable over useful readout time
reset/readout                            physically consistent
LWIR absorption                         realistic for 8–14 µm coupling
```

For Generation A the preferred trigger is now a photon-driven saddle-node:

```math
\beta_{\rm cold}>\beta_c(\delta)>\beta_{\rm hot},
\qquad
\delta=\tan a-a,
\qquad
\beta_c=\sec a.
```

The gate is not passed until a realistic `T_e(t)` and `I_c[T_e(t)]` actually drive this condition with adequate settling and cold-state dark stability.

If the region vanishes when exact barrier actions, damping, quasiparticles, vortices, optical coupling and readout are included, the architecture fails unless the failure itself yields a general bound.

## Gate 2 — architecture collision audit

Several initially plausible novelty routes are already closed:

```text
LWIR superconducting single-photon detection                     PRIOR ART
photon -> hot graphene -> Josephson switching                    PRIOR ART
single photon -> persistent superconducting single-flux memory   PRIOR ART
optical heating -> permanent superconducting flux/vortex         PRIOR ART
transient I_c suppression -> rf-SQUID barrier lowering/freeze    PRIOR ART
field-free Josephson/superconducting diode directionality        PRIOR ART
illumination -> superconducting phase battery/vorticity          PRIOR ART
```

Particularly important collisions are Onen et al. 2020 for single-photon-to-single-flux persistent memory and Zhou/Habif/Bocko/Feldman 2001 for rf-SQUID control through transient critical-current suppression.

The remaining architecture audit must search papers **and patents** for the narrower conjunction:

```text
single absorbed LWIR photon
+ calorimetric modulation of Josephson I_c
+ saddle-node / bifurcation flux capture
+ directional basin selection
+ persistent superconducting readout/storage
```

and separately for the Generation-B zero-external-flux version using a phi0/diode/inversion-breaking element.

## Gate 3 — theoretical contribution

At least one nontrivial theoretical result must survive beyond standard rf-SQUID/Josephson formulas and their direct combination.

The exact saddle-node relation

```math
\delta=\tan a-a,
\qquad
\beta_c=\sec a
```

is useful but is standard bifurcation mathematics applied to the rf-SQUID potential; do **not** assume it is publication novelty.

Current candidate theory routes are:

- a closed absorbed-photon-energy threshold connecting calorimeter heat capacity and `I_c(T)` to `beta_c(delta)`;
- a rigorous efficiency/dark-count closure combining bifurcation threshold with the cold metastable barrier and dissipative MQT;
- a scaling law optimizing distance from bifurcation, capacitance, heat capacity, flux tilt and readout-state separation;
- a finite-rate stochastic saddle-node capture law specific to photon-triggered persistent flux storage;
- an impossibility or optimality bound for zero-external-flux self-directed operation.

The near-threshold static results

```math
\Delta U_-\propto(\beta-\beta_c)^{3/2},
\qquad
\omega_m\propto(\beta-\beta_c)^{1/4},
\qquad
\Delta U_-/\hbar\omega_m\propto(\beta-\beta_c)^{5/4}
```

are presently **derived model structure, not a novelty claim**.

Rewriting standard Kramers/MQT formulas with detector symbols is insufficient.

## Gate 4 — matched benchmark

Compare against at least:

- WSi/MoSi/NbN-family SNSPDs in relevant MIR/LWIR wavelengths;
- KIDs/MKIDs with single-photon sensitivity;
- graphene/SNS Josephson bolometers/calorimeters;
- Onen-type single-photon single-flux coupled detectors;
- Josephson escape detectors / photomultipliers;
- TES/calorimetric infrared photon detectors where relevant.

Use comparable metrics: absorbed-photon efficiency, system efficiency, DCR, timing jitter, reset/dead time, energy resolution, operating temperature, optical bandwidth, dynamic range, stored-state lifetime and readout burden.

## Gate 5 — terminology

Generation A is externally flux tilted and should not be called photovoltaic.

Only call a later device `photovoltaic`, `photogalvanic`, or equivalent if the modeled mechanism really produces a directed zero-external-bias electrical/phase response attributable to optical excitation rather than merely a biased threshold latch.

Conservative working terminology remains:

```text
superconducting photon-to-flux transducer
calorimetric rf-SQUID photon latch
persistent photon-triggered flux transducer
```

## Manuscript GO criterion

A paper becomes justified only if **both** of the following are true:

1. the model survives quantitative falsification with realistic parameters; and
2. a hostile literature/patent audit leaves either a genuinely distinct architecture or a genuinely new theorem/performance result.

Current status:

```text
QUANTITATIVE GATE: OPEN — static bifurcation survives; thermal/dynamic/DCR closure incomplete
COLLISION AUDIT:    MAJOR COLLISIONS FOUND; narrower audit still incomplete
THEORY NOVELTY:     UNKNOWN
MANUSCRIPT:         NO-GO
```
