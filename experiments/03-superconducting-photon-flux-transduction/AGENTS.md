# AGENTS.md — Experiment 03 Recovery Protocol

**Experiment:** `03-superconducting-photon-flux-transduction`  
**Mode:** active exploratory theory / falsification-first  
**Manuscript status:** none; do not create one until `NOVELTY_GATES.md` is passed.

Conversation history is non-authoritative when it conflicts with repository state.

## Recovery order — current

Read in order:

1. `CURRENT_STATE.md`
2. `DYNAMIC_FOLD_GHOST_2026-08-15.md`
3. `RCSJ_DAMPING_WINDOW_2026-08-15.md`
4. `DARK_CAPTURE_ELIMINATION_2026-08-15.md`
5. `HUANG_THERMAL_DWELL_CALIBRATION_2026-08-15.md`
6. `SPECTRAL_STABILITY_PARETO_2026-08-15.md`
7. `THERMAL_CONFINEMENT_GAP_CLOSURE_2026-08-15.md`
8. `RETUNED_DWELL_CLOSURE_2026-08-15.md`
9. `INDUCTANCE_RETUNING_CLOSURE_2026-08-15.md`
10. `INDUCED_GAP_SENSITIVITY_2026-08-15.md`
11. `INTERFACE_SKEWNESS_SENSITIVITY_2026-08-15.md`
12. `HAGYMASI_CPR_VALIDATION_2026-08-15.md`
13. `ARBITRARY_LENGTH_CPR_CHECKPOINT_2026-08-15.md`
14. `DERIVATION_LOG.md`
15. `DERIVATION_LOG_CONTINUATION_2026-08-15.md`
16. `CLAIM_LEDGER.md`
17. `CLAIM_LEDGER_CONTINUATION_2026-08-15.md`
18. `LITERATURE_LEDGER.md`
19. `LITERATURE_LEDGER_CONTINUATION_2026-08-15.md`
20. `ASSUMPTIONS.md`
21. `NOVELTY_GATES.md`
22. `calculations/`.

Until consolidation, each continuation file is part of the authoritative trail.

## Current objective

Determine whether a **single absorbed LWIR photon** can drive a realistic proximity-JJ/rf-SQUID through a finite-rate directionally tilted saddle-node, reach the favored basin before cooling restores the original metastable well, and retain persistent superconducting flux with very low cold false switching.

Generation A uses external flux tilt and is not photovoltaic. Generation B remains reserved for zero-external-flux directionality.

## Canonical static fold

```math
I_* = \Phi_0/(2\pi L),
\qquad
\mathcal I=I_s/I_*,
\qquad
F=x-\delta-\mathcal I.
```

```math
\boxed{\mathcal I(x_f,T_f)=x_f-\delta,}
\qquad
\boxed{\partial_x\mathcal I(x_f,T_f)=1.}
```

Near a smooth fold:

```math
\Delta U\propto|p-p_f|^{3/2},
\qquad
\omega_m\propto|p-p_f|^{1/4}.
```

Static fold crossing is **not sufficient** for detection.

## Current two-gap rule

Never collapse

```text
Delta_ind  weak-link induced/minigap controlling ABS/CPR/Ic(T)/fold
Delta_s    parent-electrode gap controlling hot-carrier escape/confinement.
```

Current materials picture:

```text
moderately reduced Delta_ind for thermal CPR sensitivity
+
high parent Delta_s for confinement
+
retuned L/C for cold stability
+
dynamical admittance compatible with finite-rate capture.
```

## Current static family

Realistic-skewness, retuned `beta~0.8`, `A~100 um^2` family:

```text
rDelta  Tf[K]  L[pH]  barrier/kB[K]  Cmin,Q[fF]  static thermal reach
1.0     0.905   87.8      9.10          161          11.8 um
0.8     0.813   96.8      8.12          181          14.7 um
0.6     0.695  111.5      6.87          215          20.1 um
0.5     0.623  123.1      6.10          244          25.0 um
0.4     0.540  140.3      5.22          287          33.3 um.
```

The wavelength column is a **static absorbed-photon upper envelope**, not a detector cutoff.

## Strongest algebraic reduction

Inside the provisional MQT diagnostic define

```math
\boxed{
\tau_Q(D)
=\frac{\hbar\sqrt{\kappa_c}}
{\alpha_Q\Delta U_c}
W\!\left(
\frac{\alpha_Q\Delta U_c}{2\pi\hbar D}
\right).
}
```

Then

```math
\boxed{LC_{min,Q}=\tau_Q^2.}
```

A phase-limited provisional dark/capture relation can therefore be written without explicit `L,C` and gives the conditional low-`T0` scaling

```math
\boxed{
\lambda_{max}
\propto
\left[
\frac{t_c}{\ln(1/Dt_c)}
\right]^{4/3}.
}
```

Do not call this novel until exact dynamics survive and the narrow collision audit is complete.

## Exact scalar-R damping correction

Linearized recovered-basin dynamics:

```math
LC\ddot y+\frac{L}{R}\dot y+\kappa y=0.
```

Critical damping:

```math
\boxed{R_*=\frac12\sqrt{\frac{L}{C\kappa}}.}
```

Fastest scalar-Ohmic e-fold time:

```math
\boxed{\tau_{min}=\sqrt{LC/\kappa}.}
```

For `a=omega0 t_avail>=1`:

```math
\boxed{
\frac{2a}{a^2+1}
\le\frac{R}{R_*}\le a.
}
```

The old `R<t/(2C)` result is only the high-R edge. Very small `R` is overdamped and slow.

## Dynamic saddle-node correction — current decisive point

Let

```math
q=x-x_f,
\qquad
\theta=T-T_f.
```

Locally

```math
-F\simeq A\theta+(B/2)q^2.
```

Any finite damping becomes asymptotically overdamped because

```math
\zeta\propto\theta^{-1/4}\to\infty.
```

The full local ghost-passage scale is

```math
 t_{ghost}^{full}
\simeq
\frac{2\pi L}{R\kappa_c}
\sqrt{\frac{T_f-T_0}{T_{pk}-T_f}}.
```

Balancing this with recovered-basin underdamped damping gives the optimistic dynamic diagnostic

```math
\boxed{
 t_{dyn,min}
=2\sqrt{\frac{\pi}{\kappa_c}}\tau_Q
\left(
\frac{T_f-T_0}{T_{pk}-T_f}
\right)^{1/4}.
}
```

Therefore `T_pk >= T_f` is only a static threshold; finite thermal overshoot is required.

Under the explicitly conditional Huang dwell mapping at `A=100 um^2`, one absorbed 14-um photon gives:

```text
rDelta~0.8: static crossing, but conditional dynamic margin <<1
rDelta~0.6: first retained coarse point with conditional dynamic margin slightly >1.
```

Do not promote these numbers to spectral cutoffs before full dynamic integration.

## Mandatory discipline

1. Separate established background, derivation, extrapolation, conditional calibration and novelty.
2. Every major result/correction/collision goes to the derivation trail and claim ledger/continuation.
3. Add primary literature to the literature ledger/continuation.
4. Do not use priority language before a dedicated paper-and-patent audit.
5. Do not equate zero DC resistance with zero total noise/dark counts.
6. Do not treat the cubic `7.2 DeltaU/(hbar omega)` MQT expression as exact dissipative MQT.
7. Do not treat Huang's fitted `75 ns` as a temperature-independent hot-state lifetime.
8. Do not use the short-junction graphene CPR for final design.
9. Do not identify `Delta_ind` with parent `Delta_s`.
10. Do not use static wavelength reach as the detection cutoff.
11. Do not model write damping as a freely adjustable noiseless resistor.
12. Do not call Generation A photovoltaic.
13. Do not start a manuscript because a model corridor remains open.

## Major novelty collisions already closed

Do not claim novelty for:

```text
superconducting MIR/LWIR single-photon detection
photon-heated graphene -> Josephson switching
thermal proximity-JJ Ic suppression -> SQUID detection
single photon -> persistent superconducting flux memory
optically written persistent flux/vortices
transient Ic suppression -> rf-SQUID tipping/freeze
field-free Josephson directionality
illumination-driven superconducting phase battery/vorticity switching
non-sinusoidal temperature-dependent graphene CPR
engineering proximity ABS / induced-gap thermal sensitivity
generic dark-count vs timing/dead-time tradeoffs
graphene thermal-propagation optimization.
```

## Immediate work queue

**Do not do more equilibrium Pareto scanning first.**

1. Build full deterministic time-dependent CPR/RCSJ trajectory with realistic `T_e(t)` and scalar `R`.
2. Compute exact dynamic overshoot and basin entry; compare against the local ghost diagnostic.
3. Replace scalar `R` with causal `Y(omega,T_e)` / memory kernel.
4. Use the same environment for fluctuation-dissipation noise and dissipative MQT; do not optimize them independently.
5. Add stochastic thermal/quantum force and compute `P_capture`, `P_wrong`, `P_return`, capture-time distribution.
6. Only after dynamics survive, restore wavelength-dependent 8–14-um absorptance and readout/reset.
7. Then perform a narrow paper + patent collision audit for the surviving closure.

## Reproducible calculations

Current high-value scripts:

```text
arbitrary_length_graphene_cpr.py
validate_hagymasi_intermediate_cpr.py
interface_skewness_sensitivity.py
induced_gap_sensitivity.py
eliminated_dark_capture_closure.py
rcsj_damping_window.py
dynamic_fold_ghost.py
```

Older sinusoidal/short-junction scripts remain regressions only.

## Stop / reformulate conditions

Stop or reformulate if robust analysis shows any of:

- full dynamic capture requires more overshoot than one desired LWIR photon can supply;
- no causal damping environment supports capture without unacceptable cold noise/MQT;
- realistic thermal transport makes the dynamic fold margin negative across the cold-stable region;
- dissipative MQT closes the dark-rate window;
- wrong-basin/retrapping probability remains unacceptable;
- reset/readout removes the operating distinction;
- narrow prior art contains the same mechanism and no independent mathematical closure survives.

A negative bound is a valid result. Do not force the device to survive.
