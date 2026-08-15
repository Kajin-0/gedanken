# Experiment 03 — NOVELTY_GATES

No manuscript directory should be created until these gates are explicitly reviewed.

## Gate 1 — quantitative survival

A realistic arbitrary-length CPR + thermal + stochastic circuit model must produce a physically plausible region with all of:

```text
single-photon capture probability       >0.9 target
preferred-direction capture             >0.9 target
intrinsic false-switch rate             <1e-6 s^-1 exploratory target
persistent state                        stable for useful readout
8–14 um system absorption               realistic
reset/readout                            physically consistent.
```

The current necessary closure is

```math
E_\gamma\ge E_{fold},
```

```math
t_>(E_\gamma)\ge
\max[t_{diff},g\sqrt{LC_{min,Q}},2R_{hot}C_{min,Q}],
```

with thermal cold stability and a nonempty MQT/dynamic capacitance window.

The gate fails if a realistic CPR/thermal model gives `t_req >= t_>,max`, if dissipative MQT closes the window, or if capture/retrapping remains poor for all plausible parameters.

## Gate 2 — collision audit

Already closed novelty routes:

```text
LWIR superconducting single-photon detection
infrared photon -> hot graphene -> Josephson switching
photon heating -> proximity-JJ Ic suppression -> SQUID electrical detection
single photon -> persistent superconducting single-flux memory
optical heating -> persistent superconducting flux/vortex
transient Ic suppression -> rf-SQUID barrier lowering/freeze
field-free Josephson/superconducting diode directionality
illumination -> superconducting phase battery/vorticity
non-sinusoidal temperature-dependent graphene CPR.
```

Important direct collisions include Walsh/Huang, Solinas-Giazotto-Pepe, Onen, Rochet, Zhou/Habif/Bocko/Feldman, Mironov/Mel'nikov/Buzdin and measured graphene-CPR work.

The remaining audit must search papers **and patents** for the narrow conjunction:

```text
single absorbed LWIR photon
+ arbitrary-length thermal evolution of a proximity-JJ CPR
+ directional rf-SQUID fold capture
+ persistent superconducting storage
```

and for any existing theorem/optimization law equivalent to the current photon/fold/MQT/capacitance/damping closure.

## Gate 3 — theoretical contribution

The sinusoidal fold equations and generic `3/2` saddle-node barrier exponent are not enough.

Candidate surviving theory objects are now:

1. a realistic closed feasibility region connecting photon heat capacity, **full CPR/load-line fold**, cold barrier, dissipative MQT, capacitance and write dynamics;
2. the finite-maximum-above-fold-dwell impossibility bound under superlinear electron-phonon cooling, if it survives more realistic thermal modeling;
3. a true optimization law for the interior optical-trigger / quantum-stability / damping corridor;
4. a finite-rate stochastic capture law for photon-driven fold passage;
5. a zero-external-flux optimality/impossibility result.

The Lambert-W `C_min,Q` expression is exact only inside the current provisional cubic MQT rate model and is not by itself sufficient for publication.

## Gate 4 — matched benchmark

Compare against at least:

- MIR/LWIR SNSPDs;
- single-photon KIDs/MKIDs;
- graphene/SNS Josephson photon detectors and proximity-SQUID calorimeters;
- Onen-type single-photon single-flux memory devices;
- Josephson escape/threshold detectors;
- TES/calorimetric IR detectors where relevant.

Use matched metrics: system/absorbed efficiency, DCR, timing, dead time, energy resolution, operating temperature, optical bandwidth, dynamic range, stored-state lifetime, reset energy and readout burden.

## Gate 5 — terminology

Generation A is externally flux tilted and **must not** be called photovoltaic.

Only a later zero-external-bias mechanism may earn `photovoltaic` / `photogalvanic` terminology after its microscopic mechanism and prior-art boundary are established.

## Manuscript GO criterion

A paper becomes justified only if:

1. realistic arbitrary-length CPR + thermal + dissipative escape + capture calculations leave a nonempty operating region or a strong impossibility bound;
2. a hostile paper/patent audit leaves a distinct theorem/performance result or architecture;
3. the result is materially more than standard formulas assembled around a hypothetical device.

Current status:

```text
QUANTITATIVE GATE: PARTIAL — idealized nonempty corridor found; real CPR/dissipative DCR/capture incomplete
COLLISION AUDIT:    MAJOR COLLISIONS FOUND; narrow theorem/patent audit not yet done
THEORY NOVELTY:     UNKNOWN
MANUSCRIPT:         NO-GO
```
