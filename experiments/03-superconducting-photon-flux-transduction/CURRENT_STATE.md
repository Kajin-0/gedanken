# Experiment 03 — CURRENT_STATE

**Updated:** 2026-08-15  
**Mode:** exploratory theory / falsification-first  
**Publication status:** **NO-GO for manuscript**.

## 1. Current physical question

Can one absorbed LWIR photon drive a temperature-dependent Josephson/rf-SQUID circuit through a directionally selected fold, after which the circuit recovers into a persistent superconducting flux state, while cold false switching remains extremely low?

Generation A uses a small external flux tilt and is **not photovoltaic**. Generation B is reserved for later zero-external-flux directionality.

Preferred chain:

```text
8–14 um photon
 -> rapid electronic thermalization/spreading
 -> temperature-dependent full CPR changes
 -> metastable CPR/load-line intersection reaches a fold
 -> phase enters favored basin
 -> CPR recovers
 -> persistent superconducting flux remains.
```

## 2. Noise interpretation

An ideal cold superconducting storage channel with `Re Z -> 0` lacks the ordinary finite-frequency resistive Johnson contribution of that channel. This does **not** imply zero detector noise or zero dark counts.

Relevant limits are thermal phase escape, MQT, residual quasiparticles, vortices, stray photons, readout backaction, reset errors and photon statistics.

Primary metrics: `P_capture`, `P_wrong`, DCR, stored-state SNR, reset time/energy and system optical efficiency.

## 3. Canonical fold formulation

Define

```math
I_* = \frac{\Phi_0}{2\pi L},
\qquad
\mathcal I(x,T)=\frac{I_s(x,T)}{I_*},
\qquad
F=x-\delta-\mathcal I.
```

A static fold satisfies

```math
\boxed{\mathcal I(x_f,T_f)=x_f-\delta,}
\qquad
\boxed{\partial_x\mathcal I(x_f,T_f)=1.}
```

For a smooth nondegenerate fold,

```math
\Delta U\propto|p-p_f|^{3/2},
\qquad
\omega_m\propto|p-p_f|^{1/4},
\qquad
\Delta U/(\hbar\omega_m)\propto|p-p_f|^{5/4}.
```

## 4. Arbitrary-length graphene CPR — validated ideal baseline

The ideal static model uses the Titov–Beenakker ballistic graphene SNS secular equation and the Hagymasi–Kormanyos–Cserti Matsubara construction for arbitrary junction length.

```math
\ell=\frac{L_{JJ}}{\xi_0}=\frac{\Delta_{ind}L_{JJ}}{\hbar v_F},
\qquad
\mu_r=\mu/\Delta_{ind}.
```

Canonical code/checkpoints:

```text
calculations/arbitrary_length_graphene_cpr.py
calculations/validate_hagymasi_intermediate_cpr.py
ARBITRARY_LENGTH_CPR_CHECKPOINT_2026-08-15.md
HAGYMASI_CPR_VALIDATION_2026-08-15.md
```

Validation now covers both:

1. the analytic Titov–Beenakker short-junction Dirac-point limit;
2. the exact intermediate-length Hagymasi parameter set `xi/L=0.91`, `mu/Delta0=0,20`, `T/Tc=0,0.18,0.35`.

The implementation reproduces the published trend ordering and strong low-temperature high-doping skewness, with numerical results stable to the retained `q` and Matsubara cutoffs.

## 5. Realistic-interface CPR-shape stress

Nanda et al. show that realistic graphene-superconductor interfaces reduce the very large ideal CPR skewness. Representative measured/interface-model low-T skewness scales are approximately `S~0.19–0.28`, versus `S~0.55` for the ideal high-doping intermediate-length model.

A controlled shape-only deformation gives, at `beta_cold=0.8`, `Ic=3 uA`:

| cold S | T_fold | cold barrier/kB | state separation | provisional C_min,Q |
|---:|---:|---:|---:|---:|
| 0.548 ideal | 1.118 K | 16.70 K | 0.2535 Phi0 | 71 fF |
| 0.270 | 0.905 K | 9.12 K | 0.2401 Phi0 | 160 fF |
| 0.220 | 0.841 K | 7.14 K | 0.2303 Phi0 | 230 fF |
| 0.190 | 0.794 K | 5.89 K | 0.2225 Phi0 | 307 fF |

Thus realistic harmonic suppression primarily damages **cold stability**, not state separation.

Record:

```text
INTERFACE_SKEWNESS_SENSITIVITY_2026-08-15.md
```

## 6. Reduced induced-gap stress

Interpret the gap entering the graphene ABS/CPR spectrum as an **induced/proximity scale** `Delta_ind`, not automatically the parent-electrode gap.

At fixed physical junction geometry, physical gate doping and fixed loop `L=87.76 pH`, reducing

```math
r_\Delta=\Delta_{ind}/\Delta_{ind,0}
```

causes `Ic` and `beta_L` to fall. Under the realistic-skewness envelope the cold barrier collapses well before formal bistability disappears:

| r_Delta | Ic [uA] | beta_cold | cold barrier/kB |
|---:|---:|---:|---:|
| 1.00 | 3.000 | 0.800 | 9.10 K |
| 0.60 | 2.361 | 0.630 | 3.29 K |
| 0.40 | 1.877 | 0.500 | 0.94 K |
| 0.30 | 1.563 | 0.417 | 0.21 K |
| 0.24 | 1.343 | 0.358 | ~0.002 K |
| 0.22 | 1.262 | 0.337 | no selected cold metastable well |

The formal fixed-loop topology threshold near `r_Delta~0.23–0.24` is model/grid dependent; the useful cold-stability threshold is substantially higher.

Record:

```text
INDUCED_GAP_SENSITIVITY_2026-08-15.md
```

## 7. Inductance retuning — compensation with a cost

Restoring a target screening parameter after `Ic` falls requires

```math
\boxed{L=\frac{\beta\Phi_0}{2\pi I_c}\propto I_c^{-1}.}
```

At fixed normalized CPR shape,

```math
\boxed{\Delta U\propto L^{-1}\propto I_c.}
```

Thus increasing `L` can restore the normalized potential topology but cannot restore the physical barrier for free.

Inside the provisional MQT diagnostic,

```math
C_{min,Q}\sim L\times [\text{Lambert-W log corrections}],
```

so the minimum phase scale also grows roughly with `L`.

Retuning to `beta_cold=0.8` gives:

| r_Delta | retuned L [pH] | barrier/kB | C_min,Q [fF] | sqrt(L Cmin) [ps] |
|---:|---:|---:|---:|---:|
| 1.0 | 87.8 | 9.10 K | 161 | 3.75 |
| 0.8 | 96.8 | 8.12 K | 181 | 4.18 |
| 0.6 | 111.5 | 6.87 K | 215 | 4.90 |
| 0.5 | 123.1 | 6.10 K | 244 | 5.48 |
| 0.4 | 140.3 | 5.22 K | 287 | 6.35 |

So the fixed-L gap threshold is not an architecture-level impossibility; circuit retuning moves it, while consuming barrier/readout/dynamic margin.

Record:

```text
INDUCTANCE_RETUNING_CLOSURE_2026-08-15.md
calculations/inductance_retuning_scaling.py
```

## 8. Thermal-dwell closure

For the clean graphene model

```math
C_e=\gamma AT,
\qquad
P_{e-ph}=\Sigma A(T^4-T_0^4),
```

the local E-Ph time at the fold is

```math
\tau_{ep}(T_f)=\frac{\gamma}{4\Sigma T_f^2}.
```

The exact maximum time above the fold tends, for `T0 << Tf`, to

```math
\boxed{t_{>,max}\simeq2\tau_{ep}(T_f).}
```

Therefore the optimized necessary dynamic condition becomes

```math
\boxed{
\max[t_{diff},g\sqrt{LC_{min,Q}},2R_{hot}C_{min,Q}]
<2\tau_{ep}(T_f).
}
```

Equivalently, the damping branch requires

```math
\boxed{R_{hot}C_{min,Q}<\tau_{ep}(T_f).}
```

Define the screening metric

```math
\boxed{
\mathcal M_{dwell}=
\frac{2\tau_{ep}(T_f)}
{\max[t_{diff},g\sqrt{LC_{min,Q}},2R_{hot}C_{min,Q}]}
}
```

with necessary condition `M_dwell>1` in this thermal model.

Record:

```text
RETUNED_DWELL_CLOSURE_2026-08-15.md
```

## 9. Major thermal correction: diffusion spreads heat; it does not automatically remove it

Huang et al. report `l_D=sqrt(D tau_ep)~230 um`, much longer than their graphene sample. The corresponding fast electronic diffusion primarily makes `T_e` spatially uniform before E-Ph loss.

They identify direct heat leakage into MoRe superconducting contacts when

```math
k_BT_e\gtrsim\Delta_s,
```

with parent-electrode gap scale `Delta_s~1.3 meV`.

For the reference `T_pk~2.5 K`,

```text
k_B T_pk ~0.215 meV << 1.3 meV,
```

so the MoRe-based reference device is strongly gap-confined. The earlier `L^2/D~22 ps` scale is therefore a thermal **uniformization** timescale, not a 22-ps calorimetric decay time.

## 10. Two-gap architecture — current preferred materials formulation

Do not identify the two superconducting gap scales:

```text
Delta_ind : induced/minigap scale controlling ABS spectrum, Ic(T), CPR and fold
Delta_s   : parent-electrode quasiparticle gap controlling above-gap heat escape.
```

Nanda et al. explicitly allow the induced graphene gap to be smaller than the bulk MoRe gap. Therefore an architecture with

```math
\boxed{\Delta_{ind}<\Delta_s}
```

is physically plausible and potentially desirable.

For `C_e=gamma A T`, the conservative requirements

```math
T_f\le T_{pk}\lesssim T_\Delta,
\qquad
T_\Delta=\Delta_s/k_B
```

give an absorber-area window

```math
\boxed{
\frac{2\eta_{th}E_\gamma}{\gamma(T_\Delta^2-T_0^2)}
\le A\le
\frac{2\eta_{th}E_\gamma}{\gamma(T_f^2-T_0^2)}.
}
```

A nonempty conservative window exists iff

```math
\boxed{\Delta_s>k_BT_f.}
```

Its area-margin ratio is

```math
\boxed{
\frac{A_{max}}{A_{min}}
=\frac{T_\Delta^2-T_0^2}{T_f^2-T_0^2}
\simeq\left(\frac{\Delta_s}{k_BT_f}\right)^2.
}
```

Define

```math
\boxed{\mathcal H_\Delta=\Delta_s/(k_BT_f).}
```

For the MoRe-parent baseline `Delta_s~1.3 meV`, `T_Delta~15.1 K`; at `T_f~0.905 K`, `H_Delta~16.7` and `Amax/Amin~278`. Parent-gap confinement is therefore not near the limiting constraint in that baseline.

Record:

```text
THERMAL_CONFINEMENT_GAP_CLOSURE_2026-08-15.md
```

## 11. Prior-art boundary

No novelty claim is authorized.

Broad collisions already include superconducting MIR/LWIR photon detection, graphene Josephson calorimetric switching, proximity-JJ thermal sensing, single-photon-to-flux memory, optical writing of superconducting flux, rf-SQUID tipping by transient `Ic` suppression, field-free Josephson directionality, illumination-driven phase batteries, and thermally evolving non-sinusoidal graphene CPRs.

Jung et al., Phys. Rev. Applied 26, 014078 (2026), additionally close any broad novelty route based on optimizing proximity-JJ thermal sensitivity through channel length, transparency, carrier density, superconducting material or induced gap.

The plausible surviving paper route is increasingly a **persistent-capture feasibility/optimality or impossibility closure** linking independently the induced-gap trigger, parent-gap thermal confinement, cold phase stability, capacitance/damping, photon energy and stored-state readout.

## 12. Immediate next falsification step

The next model should treat `Delta_ind` and `Delta_s` as independent axes and map the simultaneous inequalities

```math
T_f(\Delta_{ind},L,\ldots)
\le T_{pk}(A,E_\gamma)
\lesssim\Delta_s/k_B,
```

```math
C_{min,Q}<C<C_{max,dyn},
```

plus the cold barrier target and `M_dwell>1`.

Priority order:

1. map the two-gap / absorber-area / retuned-inductance feasible region;
2. replace the provisional cubic MQT model with dissipative full-CPR escape;
3. justify or replace equilibrium `T_e` during the early photon pulse;
4. solve stochastic fold passage/retrapping;
5. add realistic 8–14-um absorptance and reset/readout;
6. only after survival, perform dedicated paper-and-patent collision audit.

## 13. Current verdict

**GO for continued theory. NO-GO for manuscript.**

The branch has survived the first realistic CPR-shape and reduced-induced-gap stresses, but the ideal stability margin has shrunk substantially. The strongest new design principle is to separate a thermally responsive `Delta_ind` from a high parent-electrode `Delta_s`, rather than using one gap to serve both triggering and calorimetric confinement.