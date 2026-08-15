# CONTEXT_HANDOFF.md — Live Agent Continuity Pointer

**Repository:** `Kajin-0/gedanken`  
**Active research experiment:** `experiments/03-superconducting-photon-flux-transduction/`  
**Updated:** 2026-08-15  
**Mode:** exploratory theory / falsification-first

> **LIVE `main` ALWAYS WINS.** Before every write, fetch current HEAD, inspect intervening commits, fetch the exact target blob, and never overwrite a stale SHA.

## Recovery order

1. root `AGENTS.md`;
2. Experiment 03 `AGENTS.md`;
3. Experiment 03 `CURRENT_STATE.md`;
4. `SPECTRAL_STABILITY_PARETO_2026-08-15.md`;
5. `TWO_GAP_LWIR_AREA_MAP_2026-08-15.md`;
6. `THERMAL_CONFINEMENT_GAP_CLOSURE_2026-08-15.md`;
7. `RETUNED_DWELL_CLOSURE_2026-08-15.md`;
8. `INDUCTANCE_RETUNING_CLOSURE_2026-08-15.md`;
9. `INDUCED_GAP_SENSITIVITY_2026-08-15.md`;
10. `INTERFACE_SKEWNESS_SENSITIVITY_2026-08-15.md`;
11. `HAGYMASI_CPR_VALIDATION_2026-08-15.md`;
12. `DERIVATION_LOG.md`;
13. `CLAIM_LEDGER.md`;
14. `LITERATURE_LEDGER.md`;
15. `NOVELTY_GATES.md`.

## One-sentence state

Generation A is a **single-LWIR-photon calorimetric rf-SQUID fold latch**: photon heating changes a realistic proximity-JJ CPR until a metastable load-line intersection disappears, then the phase should settle into the externally favored basin and remain as persistent superconducting flux after thermal recovery.

Generation A is externally flux tilted and is not photovoltaic.

## Major conceptual update: use a two-gap model

Do not identify

```text
Delta_ind  induced/minigap scale controlling ABS spectrum, Ic(T), CPR and fold
Delta_s    parent-electrode gap controlling hot-electron escape into contacts.
```

The preferred materials direction is potentially

```text
smaller engineered Delta_ind for thermal CPR sensitivity
+
high parent Delta_s for calorimetric confinement
+
retuned L/C for cold phase stability and write dynamics.
```

Nanda-type realistic interface physics allows `Delta_ind < Delta_s`; Huang's MoRe calorimeter uses the high parent gap to confine electronic heat.

## Current strongest closures

General fold:

```math
\boxed{\mathcal I(x_f,T_f)=x_f-\delta,}
\qquad
\boxed{\partial_x\mathcal I(x_f,T_f)=1.}
```

Static photon threshold:

```math
\boxed{E_{fold}=\eta_{th}^{-1}\int_{T_0}^{T_f}C_e(T)dT.}
```

For clean graphene `C_e=gamma AT`, `P_e-ph=Sigma A(T^4-T0^4)`:

```math
\boxed{t_{>,max}\simeq2\tau_{ep}(T_f),}
\qquad
\tau_{ep}(T_f)=\gamma/(4\Sigma T_f^2)
```

and necessary dynamics require

```math
\boxed{
\max[t_{diff},g\sqrt{LC_{min,Q}},2R_{hot}C_{min,Q}]
<2\tau_{ep}(T_f).
}
```

Conservative parent-gap confinement requires

```math
\boxed{T_f\le T_{pk}\lesssim\Delta_s/k_B.}
```

For graphene heat capacity this gives

```math
\boxed{
\frac{2\eta E_\gamma}{\gamma[(\Delta_s/k_B)^2-T_0^2]}
\le A\le
\frac{2\eta E_\gamma}{\gamma(T_f^2-T_0^2)}.
}
```

A nonempty area interval requires `Delta_s > k_B T_f`.

## Current realistic static envelope

The ideal high-doping point (`beta=0.8`, `Ic=3 uA`) gave `T_f~1.118 K`, barrier `~16.7 K`, provisional `Cmin~71 fF`.

Realistic graphene-superconductor CPR skewness (`S~0.19–0.27`) reduces the same broad region to roughly

```text
T_f ~0.79–0.91 K
cold barrier ~5.9–9.1 K
Cmin,Q ~160–307 fF
state separation ~0.22–0.24 Phi0.
```

Reducing `Delta_ind` at fixed `L` collapses the cold barrier; retuning `L` restores `beta` but not physical barrier energy:

```math
L\propto1/I_c,
\qquad
\Delta U\propto I_c,
\qquad
C_{min,Q}\sim L\times(\text{log corrections}).
```

Retuned examples:

```text
rDelta=1.0: L~87.8 pH, Tf~0.905 K, barrier~9.10 K, Cmin~161 fF
rDelta=0.8: L~96.8 pH, Tf~0.813 K, barrier~8.12 K, Cmin~181 fF
rDelta=0.6: L~111.5 pH, Tf~0.695 K, barrier~6.87 K, Cmin~215 fF
rDelta=0.4: L~140.3 pH, Tf~0.540 K, barrier~5.22 K, Cmin~287 fF.
```

## Thermal correction that must not regress

The earlier `L^2/D~22 ps` graphene scale is a **temperature-uniformization** time, not automatically an energy-decay time. Huang et al. report `l_D~230 um` much larger than the sample and identify direct heat leakage into MoRe contacts when `k_BT_e` approaches the parent gap `Delta_s~1.3 meV`.

At the reference `T_pk~2.5 K`, `k_BT_pk~0.215 meV <<1.3 meV`; MoRe parent contacts therefore provide strong calorimetric confinement in the current regime.

## New LWIR area/spectral map

Using the Huang absorbed-photon calibration (`100 um^2`, `1.55 um`, `T_pk~2.5 K`) as a ratio reference, the current MoRe-parent baseline at 10 um has the static area window

```math
\boxed{0.43\lesssim A\lesssim118~\mu m^2}
```

for `Tf~0.905 K`.

Therefore the earlier `15.5 um^2` estimate was only the area needed to reach **2.5 K**; it is not the maximum triggerable absorber area. A `~100 um^2` graphene absorber can cross the current 10-um fold in the model.

For a fixed `100 um^2` absorber, the retuned realistic-skewness family gives absorbed-photon thermal wavelength reach

```text
rDelta=1.0 -> lambda_max~11.8 um, barrier~9.1 K, Cmin~161 fF
rDelta=0.8 -> lambda_max~14.7 um, barrier~8.1 K, Cmin~181 fF
rDelta=0.6 -> lambda_max~20.1 um, barrier~6.9 K, Cmin~215 fF
rDelta=0.4 -> lambda_max~33.3 um, barrier~5.2 K, Cmin~287 fF.
```

This is the current **spectral-reach / cold-stability Pareto frontier**. It is absorbed-photon thermal reach only, not system detection cutoff.

A useful current working bracket for further falsification is roughly

```text
rDelta ~0.6–0.8
A ~100 um^2
high-gap MoRe-class parent electrodes
L ~0.10 nH
provisional Cmin,Q ~0.18–0.22 pF.
```

This is not a device recommendation; it is the region that currently survives the most constraints while thermally spanning 14 um.

## Prior-art boundary

Do not claim novelty for superconducting LWIR single-photon detection, graphene Josephson calorimetric switching, proximity-JJ thermal sensing/ABS engineering, optimization with length/transparency/density/material/induced gap, persistent single-photon flux memory, optical flux writing, rf-SQUID tipping by transient `Ic` suppression, field-free Josephson directionality, illumination-driven phase batteries, or thermally evolving graphene CPRs.

Jung et al., Phys. Rev. Applied 26, 014078 (2026), is particularly important: it closes the broad route of claiming engineered `Delta_ind`/ABS thermal sensitivity itself.

No novelty claim is authorized.

## Immediate next task

Do **not** return to ideal short-junction algebra. The current next falsification sequence is:

```text
1. map the simultaneous two-gap feasible region in (Delta_ind, Delta_s, A, L, C);
2. replace the empirical skewness envelope with realistic contact/transparency or calibrated TB-BdG CPR;
3. replace provisional cubic MQT with dissipative full-CPR quantum escape;
4. test early-time local-Fermi Te assumption;
5. solve stochastic fold passage/retrapping and directionality;
6. add actual 8–14 um absorptance, readout/backaction and reset;
7. only after survival, perform narrow paper-and-patent collision audit.
```

A particularly promising theory target is elimination of internal parameters to obtain a bound/tradeoff between

```text
maximum detectable wavelength
cold false-switch requirement
persistent-state signal
capture time.
```

## Publication state

**GO for continued theory. NO-GO for manuscript.** The strongest surviving candidate contribution is a quantitative persistent-capture feasibility/optimality or impossibility closure, not the broad device concept.

Experiments 01 and 02 remain frozen/submission tracks.
