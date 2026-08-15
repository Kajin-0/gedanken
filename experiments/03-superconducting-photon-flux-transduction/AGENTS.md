# AGENTS.md — Experiment 03 Recovery Protocol

**Experiment:** `03-superconducting-photon-flux-transduction`  
**Mode:** active exploratory theory / falsification-first  
**Manuscript status:** none; do not create one until `NOVELTY_GATES.md` is passed.

## Recovery order

Read in order:

1. `CURRENT_STATE.md`
2. `THERMAL_CONFINEMENT_GAP_CLOSURE_2026-08-15.md`
3. `RETUNED_DWELL_CLOSURE_2026-08-15.md`
4. `INDUCTANCE_RETUNING_CLOSURE_2026-08-15.md`
5. `INDUCED_GAP_SENSITIVITY_2026-08-15.md`
6. `INTERFACE_SKEWNESS_SENSITIVITY_2026-08-15.md`
7. `HAGYMASI_CPR_VALIDATION_2026-08-15.md`
8. `ARBITRARY_LENGTH_CPR_CHECKPOINT_2026-08-15.md`
9. `FEASIBILITY_CLOSURE_2026-08-15.md`
10. `DERIVATION_LOG.md`
11. `CLAIM_LEDGER.md`
12. `LITERATURE_LEDGER.md`
13. `ASSUMPTIONS.md`
14. `NOVELTY_GATES.md`
15. `calculations/`

Conversation history is non-authoritative when it conflicts with repository state.

## Current objective

Determine whether a **single absorbed LWIR photon** can drive a realistic proximity-Josephson CPR through a directionally tilted rf-SQUID fold, settle into the favored flux basin, and retain a persistent superconducting readout state while meeting a very low cold false-switch target.

Generation A uses external flux tilt and is not photovoltaic. Generation B is reserved for later zero-external-flux directionality.

## Current preferred physical model

Treat two superconducting gap scales separately:

```text
Delta_ind  induced/minigap scale controlling ABS spectrum, Ic(T), CPR and fold
Delta_s    parent-electrode quasiparticle gap controlling hot-electron confinement.
```

The preferred materials strategy is potentially

```text
smaller engineered Delta_ind for thermal sensitivity
+
high parent Delta_s for calorimetric confinement
+
L/C retuning for cold phase stability and dynamics.
```

Do not collapse `Delta_ind` and `Delta_s` into one parameter.

## Strongest current closures

General CPR/load-line fold:

```math
F=x-\delta-\mathcal I(x,T),
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

Static photon threshold:

```math
\boxed{E_{fold}=\eta_{th}^{-1}\int_{T_0}^{T_f}C_e(T)dT.}
```

For clean graphene `C_e=gamma AT`, `P_e-ph=Sigma A(T^4-T0^4)`:

```math
\boxed{t_{>,max}\simeq2\tau_{ep}(T_f),}
\qquad
\tau_{ep}(T_f)=\frac{\gamma}{4\Sigma T_f^2}
```

for `T0 << Tf`.

Inside the provisional MQT diagnostic:

```math
\boxed{
C_{min,Q}=\frac{\hbar^2\kappa_c}{\alpha_Q^2\Delta U_c^2L}
\left[W\left(\frac{\alpha_Q\Delta U_c}{2\pi\hbar D}\right)\right]^2.
}
```

Optimized necessary dynamic condition:

```math
\boxed{
\max[t_{diff},g\sqrt{LC_{min,Q}},2R_{hot}C_{min,Q}]
<2\tau_{ep}(T_f).
}
```

Parent-gap confinement + trigger condition:

```math
\boxed{T_f\le T_{pk}\lesssim \Delta_s/k_B.}
```

For `C_e=gamma AT`, this gives

```math
\boxed{
\frac{2\eta E_\gamma}{\gamma[(\Delta_s/k_B)^2-T_0^2]}
\le A\le
\frac{2\eta E_\gamma}{\gamma(T_f^2-T_0^2)}.
}
```

A conservative nonempty area interval requires

```math
\boxed{\Delta_s>k_BT_f.}
```

and has approximate width ratio

```math
\boxed{A_{max}/A_{min}\simeq(\Delta_s/k_BT_f)^2.}
```

## Current quantitative uncertainty envelope

The ideal high-doping intermediate-length point (`beta=0.8`, `Ic=3 uA`) gave

```text
T_fold~1.118 K
barrier~16.70 K
Cmin,Q~71 fF
state separation~0.2535 Phi0.
```

Realistic-interface skewness scales `S~0.19–0.27` reduce this to roughly

```text
T_fold~0.79–0.91 K
barrier~5.9–9.1 K
Cmin,Q~160–307 fF
state separation~0.22–0.24 Phi0.
```

At fixed loop inductance, reducing `Delta_ind` collapses cold stability rapidly; formal bistability vanishes near `r_Delta~0.23–0.24` in the current sensitivity model, but useful stability is lost much earlier.

Retuning `L` to restore `beta=0.8` rescues topology but not physical barrier energy:

```math
L\propto I_c^{-1},
\qquad
\Delta U\propto I_c,
\qquad
C_{min,Q}\sim L\times(\text{log corrections}).
```

Example retuned family:

```text
r_Delta=1.0: L~87.8 pH, barrier~9.10 K, Cmin~161 fF
r_Delta=0.6: L~111.5 pH, barrier~6.87 K, Cmin~215 fF
r_Delta=0.4: L~140.3 pH, barrier~5.22 K, Cmin~287 fF.
```

## Thermal correction that must not regress

The graphene diffusion time is **not** automatically the calorimetric decay time. Huang et al. report diffusion length much larger than the sample, so fast diffusion homogenizes `T_e`; superconducting MoRe contacts suppress direct electronic heat escape until `k_BT_e` approaches the parent gap scale `Delta_s~1.3 meV`.

At the current `T_pk~2.5 K`, `k_BT_pk~0.215 meV <<1.3 meV`, so the MoRe reference regime is strongly gap-confined.

Do not reintroduce ordinary normal-contact diffusion cooling below the parent gap without a specific subgap-leakage model.

## Mandatory discipline

1. Separate established background, model derivation, extrapolation and novelty.
2. Every important advance/correction/collision goes into `DERIVATION_LOG.md`.
3. Synchronize claim status to `CLAIM_LEDGER.md` and live equations/next task to `CURRENT_STATE.md`.
4. Add primary literature to `LITERATURE_LEDGER.md`; do not cite conversation memory as evidence.
5. Do not use priority language before a dedicated paper-and-patent collision audit.
6. Do not equate zero DC resistance with zero total noise/dark counts.
7. Do not treat the cubic `7.2 DeltaU/(hbar omega)` MQT form as an exact DCR.
8. Do not use the short-junction graphene CPR for the final design.
9. Do not assume measured flux-state separation equals `Phi0`.
10. Do not call Generation A photovoltaic.
11. Do not start a manuscript because an idealized corridor is nonempty.
12. Do not equate `Delta_ind` with parent `Delta_s` unless a device model justifies it.

## Major prior-art collisions

Do not claim novelty for:

```text
LWIR superconducting single-photon detection
infrared photon -> hot graphene -> Josephson switching
proximity-JJ thermal sensing / ABS thermal-sensitivity engineering
optimizing JJ thermal response with length, transparency, density, material or induced gap
single photon -> persistent superconducting flux memory
optically generated persistent superconducting flux/vortices
transient Ic suppression -> rf-SQUID barrier lowering/freeze
field-free Josephson/superconducting diode effects
illumination-driven superconducting phase battery/vorticity switching
non-sinusoidal temperature-dependent graphene CPRs.
```

Particularly important current sources: Walsh/Huang, Jung et al. 2026, Nanda et al., Solinas/Giazotto/Pepe, Onen, Rochet, Zhou/Habif/Bocko/Feldman, Mironov/Mel'nikov/Buzdin.

## Immediate work queue

1. Map the **two-gap feasible region** in `(Delta_ind, Delta_s, A, L, C)` using the fold, area-confinement and dwell inequalities.
2. Replace the phenomenological skewness envelope with a realistic contact/transparency model or calibrated TB-BdG CPR.
3. Determine whether the first tens of ps after LWIR absorption justify a local Fermi `T_e`; otherwise use a nonequilibrium distribution in the Josephson current.
4. Replace the provisional cubic MQT rate with dissipative quantum escape for the full-CPR potential.
5. Solve finite-rate stochastic fold passage, damping, retrapping and basin selection to obtain `P_capture`, `P_wrong`, `P_no-switch`.
6. Add realistic 8–14-um optical coupling, readout/backaction and reset.
7. Only after a realistic region survives, perform the narrow paper-and-patent collision audit of the feasibility closure.

## Reproducible calculations

```text
rfsquid_bifurcation_scan.py            sinusoidal roots/barriers + tipping diagnostic
general_cpr_fold.py                    general fold + CPR-shape sensitivity
thermal_bifurcation_margin.py          static photon-energy threshold scaling
thermal_diffusion_margin.py            diffusion timescale cross-check
dynamic_margin.py                      phase/damping write-time margins
short_dirac_cpr_fold.py                superseded short-graphene sensitivity
capacitance_stability_window.py        provisional Lambert-W MQT capacitance floor
arbitrary_length_graphene_cpr.py       ideal arbitrary-length graphene CPR/fold
validate_hagymasi_intermediate_cpr.py  intermediate-junction validation regression
interface_skewness_sensitivity.py      empirical CPR-shape uncertainty envelope
inductance_retuning_scaling.py         retuning tradeoff regression
```

These are exploratory regressions, not validated CI.

## Stop conditions

Stop or reformulate if robust analysis shows any of:

- one LWIR photon cannot drive a realistic CPR through the fold at usable absorption;
- realistic interface/contact physics eliminates the remaining corridor;
- `Delta_s <= k_BT_f` across the usable thermally sensitive designs;
- `t_req >= t_>,max` for all plausible thermal/circuit parameters;
- dissipative MQT/thermal dark rates close the capacitance/operating window;
- finite-rate capture gives unacceptable wrong-way/retrapping probability;
- reset/readout removes the operating distinction;
- narrow prior art contains the same mechanism and no independent closure survives.

A negative bound is a valid result. Do not force the device to survive.
