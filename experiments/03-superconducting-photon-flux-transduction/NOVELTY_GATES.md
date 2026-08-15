# Experiment 03 — NOVELTY_GATES

No manuscript directory should be created until these gates are explicitly reviewed.

## Gate 1 — quantitative survival

The exact time-dependent stochastic model must produce a physically plausible nonempty parameter region where all of the following can hold simultaneously:

```text
single-photon detection probability     high (initial target > 0.9)
preferred-direction capture             high (initial target > 0.9)
intrinsic false-switch rate             low (exploratory target < 1e-6 s^-1)
persistent post-event flux state        stable over useful readout time
reset/readout                            physically consistent
LWIR absorption                         realistic for 8–14 µm coupling
```

If the region vanishes when exact barrier actions, damping, quasiparticles, vortices, optical coupling and readout are included, the architecture fails unless the failure itself yields a general bound.

## Gate 2 — architecture collision audit

Search papers and patents for the exact conjunction:

```text
single absorbed photon
+ Josephson/phase-triggered switching
+ persistent fluxoid capture
+ directional or self-biased capture
+ superconducting readout/storage
```

Individual ingredients are already prior art. Novelty cannot be inferred from assembling them in prose.

## Gate 3 — theoretical contribution

At least one nontrivial theoretical result should survive beyond standard textbook formulas. Candidate forms include:

- a rigorous efficiency–dark-count feasibility bound for persistent photon-to-flux transduction;
- a scaling law showing how heat capacity, plasma frequency, inductance and asymmetry jointly determine the achievable operating region;
- an impossibility bound showing that a fully passive zero-bias architecture cannot reach a target efficiency/DCR combination;
- a controlled asymptotic regime in which detector-added equilibrium noise is parametrically suppressed while photon-trigger probability remains finite;
- a new optimization principle specific to persistent fluxoid storage rather than ordinary Josephson switching.

Rewriting Kramers/MQT formulas with detector symbols is insufficient.

## Gate 4 — matched benchmark

Compare against at least:

- WSi/MoSi/NbN-family SNSPDs in relevant MIR/LWIR wavelengths;
- KIDs/MKIDs with single-photon sensitivity;
- graphene/SNS Josephson bolometers/calorimeters;
- Josephson escape detectors / photomultipliers;
- TES/calorimetric infrared photon detectors where relevant.

Use comparable metrics: absorbed-photon efficiency, system efficiency, DCR, timing jitter, reset/dead time, energy resolution, operating temperature, optical bandwidth, dynamic range and readout burden.

## Gate 5 — terminology

Only call the final device `photovoltaic` if the modeled mechanism really produces a directed zero-bias electrical/phase response attributable to optical excitation rather than merely a biased threshold latch.

Possible eventual terminology, depending on physics:

```text
persistent superconducting photon-to-flux transducer
single-photon fluxoid latch
photogalvanic superconducting flux detector
superconducting photovoltaic flux memory detector
```

Do not choose the most dramatic term before the mechanism warrants it.

## Manuscript GO criterion

A paper becomes justified only if **both** of the following are true:

1. the model survives quantitative falsification with realistic parameters; and
2. a hostile literature/patent audit leaves either a genuinely distinct architecture or a genuinely new theorem/performance result.

Current status:

```text
QUANTITATIVE GATE: OPEN
COLLISION AUDIT:    INCOMPLETE
THEORY NOVELTY:     UNKNOWN
MANUSCRIPT:         NO-GO
```
