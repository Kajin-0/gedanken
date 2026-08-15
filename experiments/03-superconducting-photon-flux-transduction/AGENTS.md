# AGENTS.md — Experiment 03 Recovery Protocol

**Experiment:** `03-superconducting-photon-flux-transduction`  
**Mode:** active exploratory theory / falsification-first  
**Manuscript status:** none; do not create one until `NOVELTY_GATES.md` is passed.

## Recovery order

Read in order:

1. `CURRENT_STATE.md`
2. `FEASIBILITY_CLOSURE_2026-08-15.md`
3. `DERIVATION_LOG.md`
4. `CLAIM_LEDGER.md`
5. `ASSUMPTIONS.md`
6. `LITERATURE_LEDGER.md`
7. `NOVELTY_GATES.md`
8. `THERMAL_DYNAMIC_CHECKPOINT_2026-08-15.md`
9. `README.md`
10. `calculations/`

Conversation history is non-authoritative when it conflicts with repository state.

## Current objective

Determine whether a **single absorbed LWIR photon** can drive a full temperature-dependent Josephson CPR through a directionally tilted rf-SQUID fold, settle into the favored flux basin, and retain a persistent superconducting readout state while meeting a very low cold false-switch target.

Generation A uses external flux tilt and is not photovoltaic. Generation B is reserved for later zero-external-flux directionality.

## Strongest current closure

General CPR/load-line fold:

```math
F(x,T)=x-\delta-\mathcal I(x,T),
\qquad
\mathcal I=I_s/I_*,
\qquad
I_*=\Phi_0/(2\pi L),
```

```math
\boxed{\mathcal I(x_f,T_f)=x_f-\delta,}
\qquad
\boxed{\partial_x\mathcal I(x_f,T_f)=1.}
```

Static optical fold energy:

```math
\boxed{
E_{fold}=\eta_{th}^{-1}\int_{T_0}^{T_f}C_e(T)dT.
}
```

Time above fold:

```math
\boxed{
t_>(E_\gamma)=
\int_{T_f}^{T_{pk}(E_\gamma)}
\frac{C_e(T)}{P_{cool}(T)}dT.
}
```

Provisional MQT capacitance floor:

```math
\boxed{
C_{min,Q}
=\frac{\hbar^2\kappa_c}{\alpha_Q^2\Delta U_c^2L}
\left[
W\left(\frac{\alpha_Q\Delta U_c}{2\pi\hbar D}\right)
\right]^2.
}
```

Optimized necessary settling scale:

```math
\boxed{
t_{req}^*=
\max[t_{diff},\ g\sqrt{LC_{min,Q}},\ 2R_{hot}C_{min,Q}].
}
```

Necessary chain:

```math
E_\gamma\ge E_{fold},
\qquad
t_>(E_\gamma)\ge t_{req}^*,
\qquad
\Delta U_c\gtrsim k_BT_0\ln(\Omega_T/D).
```

Inside the idealized clean-graphene `T^4` cooling model,

```math
\boxed{
t_{>,max}
=\frac{\gamma_S}{4\Sigma T_0^2}
\ln\left(\frac{T_f^2+T_0^2}{T_f^2-T_0^2}\right),
}
```

so `t_req >= t_>,max` is a model-level impossibility condition regardless of photon energy.

## Current quantitative lessons

- Sinusoidal benchmark: `delta=0.05`, `beta=1.5`, `I_c=3 uA` gives 23.53% scalar suppression, `L=164.55 pH`, cold barrier `9.443 k_B K`, state separation `0.4753 Phi0`, ~20-ps deterministic phase passage.
- Cross-device graphene thermal diffusion estimate for a 15.5-um^2 square absorber is ~22 ps using Huang's `l_D~230 um`, `tau_ep~75 ns` characteristic scales.
- A measured/microscopic CPR is mandatory. The 600-nm MoRe/graphene device is not safely in the Titov-Beenakker short-junction limit (`L_JJ/xi~1.2` using the quoted gap scale).
- The short-Dirac calculation is only a sensitivity model. It nevertheless exposes an interior optical-trigger / MQT-capacitance corridor rather than a monotonic optimum.
- Example toy point `beta=0.8`: `T_fold~2.17 K`, cold barrier `~4.41 K`, provisional `C_min,Q~0.52 pF`; a 10-ns useful hot interval then requires `R_hot<~9.6 kOhm` under the simple damping envelope.

## Mandatory discipline

1. Separate established background, model derivation, extrapolation and novelty.
2. Every important advance/correction/collision goes into `DERIVATION_LOG.md`.
3. Synchronize claim status to `CLAIM_LEDGER.md` and live equations/next task to `CURRENT_STATE.md`.
4. Add primary literature to `LITERATURE_LEDGER.md`; do not cite conversation memory as evidence.
5. Do not use priority language before a dedicated paper-and-patent collision audit.
6. Do not equate zero DC resistance with zero total noise/dark counts.
7. Do not treat the cubic `7.2 DeltaU/(hbar omega)` MQT form as an exact DCR.
8. Do not use a sinusoidal or short-junction graphene CPR for the final design without justification.
9. Do not assume measured flux-state separation equals `Phi0`.
10. Do not call Generation A photovoltaic.
11. Do not start a manuscript because an idealized corridor is nonempty.

## Major prior-art collisions already found

Do not claim novelty for:

```text
LWIR superconducting single-photon detection
infrared photon -> hot graphene -> Josephson switching
photon heating -> proximity-JJ Ic suppression -> SQUID electrical detection
single photon -> persistent superconducting single-flux memory
optically generated persistent superconducting flux/vortices
transient Ic suppression -> rf-SQUID barrier lowering/freeze
field-free Josephson/superconducting diode effects
illumination-driven superconducting phase battery/vorticity switching
non-sinusoidal temperature-dependent graphene CPRs.
```

Particularly important: Walsh/Huang, Solinas-Giazotto-Pepe, Onen, Rochet, Zhou/Habif/Bocko/Feldman, Mironov/Mel'nikov/Buzdin, Nanda et al.

## Immediate work queue

1. Build an arbitrary-length `I_s(phi,T)` for a realistic graphene/SNS photon-sensitive weak link using the Hagymasi/Kormanyos/Cserti-type secular/Matsubara route or equivalent validated theory.
2. Obtain the exact fold curve `T_f(delta,L,geometry,doping,interfaces)`.
3. Compute cold barrier/curvature from that CPR and replace the provisional MQT model with dissipative escape theory.
4. Couple the fold to a spatial/thermal pulse with diffusion to contacts and E-Ph cooling.
5. Solve finite-rate stochastic fold passage, damping, retrapping and basin selection to obtain `P_capture`, `P_wrong`, `P_no-switch`.
6. Add realistic 8–14-um optical coupling, readout/backaction and reset.
7. Only after a realistic region survives, perform the narrow paper-and-patent collision audit of the feasibility closure.

## Reproducible calculations

```text
rfsquid_bifurcation_scan.py       exact sinusoidal roots/barriers + tipping diagnostic
general_cpr_fold.py               general fold + CPR-shape sensitivity
thermal_bifurcation_margin.py     static photon-energy threshold scaling
thermal_diffusion_margin.py       diffusion timescale cross-check
dynamic_margin.py                 phase/damping write-time margins
short_dirac_cpr_fold.py           short-graphene CPR sensitivity only
capacitance_stability_window.py   provisional Lambert-W MQT capacitance floor
```

These are exploratory regressions, not validated CI.

## Stop conditions

Stop or reformulate if robust analysis shows any of:

- one LWIR photon cannot drive a realistic CPR through the fold at usable absorption;
- `t_req >= t_>,max` for all plausible thermal/circuit parameters;
- dissipative MQT/thermal dark rates close the capacitance/operating window;
- finite-rate capture gives unacceptable wrong-way/retrapping probability;
- reset/readout removes the operating distinction;
- narrow prior art contains the same mechanism and no independent closure survives.

A negative bound is a valid research result. Do not force the device to survive.
