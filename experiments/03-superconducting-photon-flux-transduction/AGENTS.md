# AGENTS.md — Experiment 03 Recovery Protocol

**Experiment:** `03-superconducting-photon-flux-transduction`  
**Mode:** active exploratory theory / falsification-first  
**Manuscript status:** none; do not create one until `NOVELTY_GATES.md` is passed.

## Recovery order

Read in order:

1. `CURRENT_STATE.md`
2. `ARBITRARY_LENGTH_CPR_CHECKPOINT_2026-08-15.md`
3. `FEASIBILITY_CLOSURE_2026-08-15.md`
4. `DERIVATION_LOG.md`
5. `CLAIM_LEDGER.md`
6. `ASSUMPTIONS.md`
7. `LITERATURE_LEDGER.md`
8. `NOVELTY_GATES.md`
9. `THERMAL_DYNAMIC_CHECKPOINT_2026-08-15.md`
10. `calculations/`

Conversation history is non-authoritative when it conflicts with repository state.

## Current objective

Determine whether a **single absorbed LWIR photon** can drive a realistic arbitrary-length Josephson CPR through a directionally tilted rf-SQUID fold, settle into the favored flux basin, and retain a persistent superconducting readout state while meeting a very low cold false-switch target.

Generation A uses external flux tilt and is not photovoltaic. Generation B is reserved for later zero-external-flux directionality.

## Strongest current closure

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

Static optical fold energy:

```math
\boxed{E_{fold}=\eta_{th}^{-1}\int_{T_0}^{T_f}C_e(T)dT.}
```

Time above fold:

```math
\boxed{
t_>(E_\gamma)=\int_{T_f}^{T_{pk}(E_\gamma)}\frac{C_e(T)}{P_{cool}(T)}dT.
}
```

Inside the current provisional MQT diagnostic:

```math
\boxed{
C_{min,Q}=\frac{\hbar^2\kappa_c}{\alpha_Q^2\Delta U_c^2L}
\left[W\left(\frac{\alpha_Q\Delta U_c}{2\pi\hbar D}\right)\right]^2.
}
```

Necessary write-time scale:

```math
\boxed{t_{req}^*=\max[t_{diff},g\sqrt{LC_{min,Q}},2R_{hot}C_{min,Q}].}
```

Necessary chain:

```math
E_\gamma\ge E_{fold},
\qquad
t_>(E_\gamma)\ge t_{req}^*,
\qquad
\Delta U_c\gtrsim k_BT_0\ln(\Omega_T/D).
```

For idealized clean-graphene `T^4` cooling, `t_>` has a finite maximum. If `t_req >= t_>,max`, no larger photon energy rescues the design within that thermal model.

## Arbitrary-length CPR checkpoint — now current

The short-junction toy has been superseded by an ideal arbitrary-length ballistic graphene SNS model using the Titov–Beenakker secular equation plus Hagymási–Kormányos–Cserti Matsubara evaluation.

Validation/status:

```text
short-limit regression: sub-percent-to-percent normalized CPR agreement at ell=0.01
current intermediate-length checkpoint: ell=1.1, delta=0.05, T0=20 mK
cold normalized fold: mu/Delta0=0 ->0.463; 10 ->0.325; 20 ->0.200
Qmax~30 required for stable finite-doping fold values.
```

Strong illustrative point:

```text
ell=1.1
mu/Delta0=20
beta_cold=0.8
Ic0 scale=3 uA
T_fold~1.118 K
reference heat fraction~0.200
cold barrier/k_B~16.70 K
L~87.76 pH
provisional C_min,Q~71 fF
state separation~0.2535 Phi0 = ~5.97 uA.
```

At `beta=0.8`, increasing `mu/Delta0` from 0 to 20 leaves ideal `T_fold` near 1.1 K but raises the cold barrier from ~7.0 K to ~16.7 K and lowers provisional `C_min,Q` from ~262 fF to ~71 fF. Within the ideal model, doping mainly improves cold stability.

**Do not treat these as calibrated device parameters.** The model assumes ballistic graphene, rigid pair potential, ideal SG interfaces, equilibrium `T`, and no disorder/contact/inverse-proximity corrections.

Canonical model:

```text
ARBITRARY_LENGTH_CPR_CHECKPOINT_2026-08-15.md
calculations/arbitrary_length_graphene_cpr.py
```

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

## Major prior-art collisions

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

## Immediate work queue

1. Quantitatively validate the arbitrary-length CPR implementation against published CPR/skewness curves, not only the short-limit regression.
2. Introduce finite/nonideal SG interface transparency and realistic contact doping; determine how the fold corridor moves.
3. Calibrate `ell`, `mu/Delta0`, `Delta(T)`, `Ic` and geometry to a plausible photon-sensitive weak link.
4. Determine whether the first tens of ps after LWIR absorption justify a local Fermi `T_e`; otherwise use a nonequilibrium distribution in the Josephson current.
5. Replace the provisional cubic MQT rate with dissipative quantum escape for the full-CPR potential.
6. Solve finite-rate stochastic fold passage, damping, retrapping and basin selection to obtain `P_capture`, `P_wrong`, `P_no-switch`.
7. Add realistic 8–14-um optical coupling, readout/backaction and reset.
8. Only after a realistic region survives, perform the narrow paper-and-patent collision audit of the feasibility closure.

## Reproducible calculations

```text
rfsquid_bifurcation_scan.py       sinusoidal roots/barriers + tipping diagnostic
general_cpr_fold.py               general fold + CPR-shape sensitivity
thermal_bifurcation_margin.py     static photon-energy threshold scaling
thermal_diffusion_margin.py       diffusion timescale cross-check
dynamic_margin.py                 phase/damping write-time margins
short_dirac_cpr_fold.py           superseded short-graphene sensitivity
capacitance_stability_window.py   provisional Lambert-W MQT capacitance floor
arbitrary_length_graphene_cpr.py  current ideal arbitrary-length graphene CPR/fold model
```

These are exploratory regressions, not validated CI.

## Stop conditions

Stop or reformulate if robust analysis shows any of:

- one LWIR photon cannot drive a realistic CPR through the fold at usable absorption;
- interface/contact nonidealities eliminate the ideal corridor;
- `t_req >= t_>,max` for all plausible thermal/circuit parameters;
- dissipative MQT/thermal dark rates close the capacitance/operating window;
- finite-rate capture gives unacceptable wrong-way/retrapping probability;
- reset/readout removes the operating distinction;
- narrow prior art contains the same mechanism and no independent closure survives.

A negative bound is a valid result. Do not force the device to survive.
