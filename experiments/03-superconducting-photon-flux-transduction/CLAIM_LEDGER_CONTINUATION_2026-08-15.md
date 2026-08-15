# Experiment 03 — Claim Ledger Continuation — 2026-08-15

This file continues `CLAIM_LEDGER.md` for Steps 39 onward. Until the ledgers are consolidated, **both files together are authoritative**. A derivation is not a novelty claim.

| Claim | Status | Notes |
|---|---|---|
| `Delta_ind` and parent `Delta_s` must be treated as the same material parameter | REJECTED | induced weak-link spectrum and parent-electrode heat-escape scale are physically distinct |
| Conservative fold/confinement gives `T_f <= T_pk <= Delta_s/k_B` | DERIVED CONDITIONAL DESIGN CONDITION | upper inequality is a conservative parent-gap heat-leak screen, not a sharp transport threshold |
| For `C_e=gamma A T`, simultaneous fold/confinement yields the two-sided absorber-area window recorded in the two-gap checkpoint | DERIVED WITHIN MODEL | exact algebra for the stated calorimetric/confinement assumptions |
| `A~15.5 um^2` is the uniquely required 10-um absorber area | REJECTED / SUPERSEDED | it only reproduced the 2.5-K reference pulse; current sub-kelvin folds allow much larger area |
| For `A=100 um^2`, the current retuned family has static absorbed-photon thermal reach from ~11.8 to 33 um as `r_Delta` falls from 1 to 0.4 | DERIVED STATIC MODEL RESULT | not a detector spectral cutoff; ignores finite-rate capture |
| Inside the provisional cubic-MQT diagnostic, `LC_min,Q=tau_Q^2` with `tau_Q=(hbar sqrt(kappa)/(alpha DeltaU)) W(alpha DeltaU/(2 pi hbar D))` | DERIVED EXACTLY WITHIN PROVISIONAL MODEL | algebraic elimination of capacitance |
| At `C=C_min,Q`, the old phase-time convention becomes `t_phi=g tau_Q` independent of `L` and `C` separately | DERIVED WITHIN MODEL | useful reduction, not exact nonlinear capture time |
| A phase-capture budget gives the explicit provisional dark-rate floor `D_min,phi(t_c)` recorded in `DARK_CAPTURE_ELIMINATION_2026-08-15.md` | DERIVED WITHIN PROVISIONAL MODEL | depends on cubic MQT diagnostic and phase-time convention |
| Near a smooth thermal fold with graphene `E~T^2`, the provisional low-`T0` spectral scaling is `lambda_max ~ [t_c/ln(1/(D t_c))]^(4/3)` | DERIVED ASYMPTOTIC / NOVELTY UNKNOWN | candidate theory object only; coefficients/model scope must survive exact dynamics and collision audit |
| The generic statement that reducing detector jitter/dead time increases dark counts is new | COLLIDED / PRIOR ART | Schwarzhans et al., PRX Quantum 7, 033001 (2026), derive this tradeoff in an autonomous detector model |
| Huang's fitted `tau_ep~75 ns` at 20 mK is a directly measured temperature-independent hot-state dwell | REJECTED | it is a fitted clean-graphene thermal-model quantity; mapping it to local `gamma/(4 Sigma T^2)` is conditional |
| Identifying Huang's 75-ns fit with the local clean-model coefficient gives sub-kelvin `t_>,max` of order 70–200 ps across the retained family | CONDITIONAL MODEL CALIBRATION | useful stress test, not a calibrated hot-state lifetime |
| The simple scalar damping requirement is only `R < t/(2C)` | SUPERSEDED / INCOMPLETE | this is the underdamped high-R edge only |
| Linearized scalar-R RCSJ settling has critical resistance `R*=0.5 sqrt[L/(C kappa)]` and minimum time `sqrt(LC/kappa)` | DERIVED EXACTLY WITHIN LINEAR RCSJ | frequency-independent Ohmic model |
| For `a=omega0 t_avail>=1`, exact scalar-R settling requires `2a/(a^2+1) <= R/R* <= a` | DERIVED EXACTLY WITHIN LINEAR RCSJ | includes overdamped lower and underdamped upper boundaries |
| Under the conditional Huang mapping, current retuned points give `R*~13–14 ohm`, `R_-~1–2 ohm`, `R_+~0.23–0.36 kOhm` | CONDITIONAL NUMERICAL MODEL RESULT | not a physical shunt recommendation; actual GJJ admittance is frequency dependent |
| Making the scalar damping resistance arbitrarily small always speeds capture | REJECTED | sufficiently small `R` is overdamped and slow |
| Static saddle-node crossing `T_pk>=T_f` guarantees flux capture | REJECTED | critical slowing can allow the fold to recover before the phase exits the bottleneck |
| Near a smooth saddle-node, any finite Ohmic damping becomes locally overdamped as the fold is approached | DERIVED ASYMPTOTIC | `omega_m~theta^(1/4)` implies `zeta~theta^(-1/4)` |
| Fixed-step overdamped saddle-node ghost passage scales as `(T_pk-T_f)^(-1/2)` | DERIVED NORMAL-FORM RESULT | full-ghost order-one prefactor depends on entry/exit convention |
| Balancing the local ghost scale against recovered-basin `2RC` gives optimized diagnostic `t_dyn,min ~ tau_Q [(T_f-T0)/(T_pk-T_f)]^(1/4)` | DERIVED CONDITIONAL NORMAL-FORM CLOSURE | optimistic local diagnostic; full time-dependent CPR required |
| Under the conditional Huang mapping, an absorbed 14-um photon at `r_Delta~0.8`, `A=100 um^2` is dynamically robust | REJECTED WITHIN CURRENT STRESS TEST | static overshoot only ~19 mK; conditional dwell ~4 ps vs ~45-ps optimized local dynamic diagnostic |
| Under the same conditional stress, `r_Delta~0.6` is the first retained coarse 14-um point with dynamic margin above one | CONDITIONAL MODEL RESULT | not a detector cutoff; depends on thermal mapping and local fold prefactor |
| Current static spectral Pareto frontier is sufficient to select a final material point | REJECTED | finite-rate fold dynamics can materially shift the boundary |
| Frequency-selective damping can be added without a noise penalty | REJECTED AS ASSUMPTION | any dissipative real admittance must be paired with fluctuations through fluctuation-dissipation |
| The current dynamic fold/calorimetric closure is publication-novel | UNKNOWN / ACTIVE COLLISION TARGET | requires exact dynamics, dissipative MQT and narrow paper/patent audit |
| A publishable Experiment-03 paper exists now | NO-GO | manuscript remains gated by `NOVELTY_GATES.md` |
