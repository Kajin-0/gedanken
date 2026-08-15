# CONTEXT_HANDOFF.md — Live Agent Continuity Pointer

**Repository:** `Kajin-0/gedanken`  
**Active research experiment:** `experiments/03-superconducting-photon-flux-transduction/`  
**Updated:** 2026-08-15  
**Mode:** exploratory theory / falsification-first

> **LIVE `main` ALWAYS WINS.** Before every write, fetch current HEAD, inspect intervening commits, fetch the exact target blob, and never overwrite a stale SHA.

## Recovery order

1. root `AGENTS.md`;
2. Experiment 03 `AGENTS.md`;
3. `CURRENT_STATE.md`;
4. `FEASIBILITY_CLOSURE_2026-08-15.md`;
5. `DERIVATION_LOG.md`;
6. `CLAIM_LEDGER.md`;
7. `ASSUMPTIONS.md`;
8. `LITERATURE_LEDGER.md`;
9. `NOVELTY_GATES.md`;
10. `calculations/`.

## One-sentence current state

The preferred Generation-A model is a **single-LWIR-photon calorimetric rf-SQUID fold latch**: photon heating changes the full Josephson current-phase relation until the metastable CPR/load-line intersection disappears, after which the phase should settle into the externally favored basin and remain as persistent superconducting flux when the CPR recovers.

Generation A is externally flux tilted and is not photovoltaic.

## Strongest current mathematics

For arbitrary CPR

```math
I_* = \Phi_0/(2\pi L),
\qquad
\mathcal I(x,T)=I_s(x,T)/I_*,
```

```math
F(x,T)=x-\delta-\mathcal I(x,T).
```

Fold condition:

```math
\boxed{\mathcal I(x_f,T_f)=x_f-\delta,}
\qquad
\boxed{\partial_x\mathcal I(x_f,T_f)=1.}
```

Near any smooth nondegenerate fold:

```math
\Delta U\propto|p-p_f|^{3/2},
\qquad
\omega_m\propto|p-p_f|^{1/4},
\qquad
\Delta U/(\hbar\omega_m)\propto|p-p_f|^{5/4}.
```

This is the fundamental trigger-vs-dark-stability tradeoff.

## Current compact feasibility closure

Static photon threshold:

```math
\boxed{
E_{fold}=\eta_{th}^{-1}\int_{T_0}^{T_f}C_e(T)dT.
}
```

Time above fold under lumped cooling:

```math
\boxed{
t_>(E_\gamma)=
\int_{T_f}^{T_{pk}(E_\gamma)}
\frac{C_e(T)}{P_{cool}(T)}dT.
}
```

Cold provisional quantum-stability capacitance:

```math
\boxed{
C_{min,Q}
=
\frac{\hbar^2\kappa_c}
{\alpha_Q^2\Delta U_c^2L}
\left[
W\left(\frac{\alpha_Q\Delta U_c}{2\pi\hbar D}\right)
\right]^2
}
```

inside the current cubic MQT-rate diagnostic only.

Define

```math
\boxed{
t_{req}^*=
\max\left[
t_{diff},\ g\sqrt{LC_{min,Q}},\ 2R_{hot}C_{min,Q}
\right].
}
```

Necessary chain:

```math
\boxed{E_\gamma\ge E_{fold},}
```

```math
\boxed{t_>(E_\gamma)\ge t_{req}^*,}
```

```math
\boxed{\Delta U_c\gtrsim k_BT_0\ln(\Omega_T/D).}
```

The full derivation and status are in `FEASIBILITY_CLOSURE_2026-08-15.md`.

## First model-level impossibility condition

For the idealized clean-graphene lumped laws

```math
C_e=\gamma_SAT,
\qquad
P_{e-ph}=\Sigma A(T^4-T_0^4),
```

the maximum possible time above a fixed fold, even as `T_pk -> infinity`, is

```math
\boxed{
t_{>,max}
=\frac{\gamma_S}{4\Sigma T_0^2}
\ln\left(\frac{T_f^2+T_0^2}{T_f^2-T_0^2}\right)
\simeq\frac{\gamma_S}{2\Sigma T_f^2}.
}
```

Thus `t_req >= t_>,max` means **no photon energy can rescue the design within that cooling model**.

## Important numerical checkpoints

Sinusoidal illustrative circuit:

```text
delta                     = 0.05
beta_cold                 = 1.5
Ic                        = 3 uA
beta_fold                 = 1.14712
required scalar Ic drop   = 23.53 %
L                         = 164.55 pH
cold barrier/k_B          = 9.443 K
state separation          = 0.4753 Phi0 = 5.97 uA
phase crossing diagnostic ~20 ps.
```

Published graphene thermal characteristic values imply `D~0.705 m^2/s`; a `15.5 um^2` square absorber has a cross-device diffusion scale near `22 ps`.

## Short-graphene CPR warning and toy optimization

The 2026 MoRe/graphene photon detector has `L_JJ~0.6 um`; the quoted `Delta~1.3 meV` gives `hbar v_F/Delta~0.51 um` for `v_F~1e6 m/s`, so `L_JJ/xi~1.2`. **Do not use the Titov-Beenakker short-junction CPR as a final model.** Arbitrary-length theory or measured CPR is required.

The short-CPR calculation is retained only as a sensitivity example. It produces the coupled tradeoff:

```text
beta   T_fold   eta_th,min   barrier/k_B   C_min,Q
0.60   0.787 K    0.099       0.454 K       30.3 pF
0.70   1.506 K    0.363       2.048 K        2.10 pF
0.80   2.172 K    0.755       4.409 K        0.520 pF
0.85   2.480 K    0.984       5.805 K        0.314 pF
0.90   2.769 K    1.227       7.309 K        0.206 pF
```

This demonstrates an interior optical-trigger / quantum-stability corridor in the toy model, not a device design.

## Prior-art boundary

Broad novelty routes already closed include:

```text
LWIR superconducting single-photon detection
infrared photon -> hot graphene -> Josephson switching
photon heating -> proximity-JJ Ic suppression -> SQUID detection
single photon -> persistent superconducting single-flux memory
optical heating -> permanent superconducting flux/vortices
transient Ic suppression -> rf-SQUID tipping/freeze
field-free Josephson directionality
illumination-driven superconducting phase battery/vorticity switching
non-sinusoidal temperature-dependent graphene CPRs.
```

Important collisions: Walsh/Huang; Solinas-Giazotto-Pepe; Onen; Rochet; Zhou/Habif/Bocko/Feldman; Mironov/Mel'nikov/Buzdin; measured graphene CPR literature.

No novelty claim is authorized.

## Immediate next task

The next decisive calculation is **arbitrary-length proximity-JJ physics**:

```text
I_s(phi,T)
-> exact fold curve T_f
-> cold barrier/curvature
-> improved dissipative MQT
-> photon thermal pulse with contact + E-Ph loss
-> finite-rate stochastic basin capture
-> P_capture, P_wrong, P_no-switch.
```

Do not spend more time optimizing the short-junction toy model except as a regression/sensitivity check.

## Reproducible scripts currently present

```text
calculations/rfsquid_bifurcation_scan.py
calculations/general_cpr_fold.py
calculations/thermal_bifurcation_margin.py
calculations/thermal_diffusion_margin.py
calculations/dynamic_margin.py
calculations/short_dirac_cpr_fold.py
calculations/capacitance_stability_window.py
```

These are exploratory calculations, not validated CI.

## Publication state

**GO for continued theory. NO-GO for manuscript.** The most plausible surviving contribution is now a quantitative feasibility/optimality or impossibility closure, not the broad device concept.

Experiments 01 and 02 remain frozen/submission tracks.
