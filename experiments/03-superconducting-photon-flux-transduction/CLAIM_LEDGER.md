# Experiment 03 — CLAIM_LEDGER

This ledger is authoritative for claim status. A derivation is not a novelty claim.

| Claim | Status | Notes |
|---|---|---|
| An ideal cold superconducting storage channel with `Re Z = 0` lacks the ordinary finite-frequency resistive Johnson contribution | ESTABLISHED BACKGROUND | fluctuation-dissipation statement; not novel |
| Zero resistance implies zero total detector noise | REJECTED | photon statistics, quasiparticles, phase slips, MQT, vortices, stray photons, readout and reset remain |
| A strictly lossless photon-current response naturally accumulates state rather than passively resetting | DERIVED / ELEMENTARY | motivates latching/integrating architecture |
| Internal superconducting gain alone cannot beat Poisson photon-arrival NEP | DERIVED / STANDARD CONSEQUENCE | signal and photon noise scale together |
| One 10-um photon carries about 124 meV | ESTABLISHED | numerical constant |
| Brief dissipative absorption followed by persistent superconducting storage is physically allowed | WORKING DESIGN CONCLUSION | LWIR photon need not be sub-gap |
| Graphene Josephson single-photon switching can reach ~87% intrinsic efficiency at <1 s^-1 dark count and ~75% at <1/week | ESTABLISHED PRIOR ART | Huang et al. 2026 |
| Photon -> hot graphene -> Josephson escape is new | COLLIDED / PRIOR ART | Walsh et al. 2021 / Huang et al. 2026 |
| Photon heating -> proximity-JJ `I_c` suppression -> SQUID electrical detection is new | COLLIDED / PRIOR ART | Solinas, Giazotto, Pepe 2017/2018 proposal |
| Single photon -> persistent superconducting single-flux memory is new | COLLIDED / PRIOR ART | Onen et al. 2020 |
| Optical heating -> persistent quantized superconducting flux is new in broad form | COLLIDED / PRIOR ART | Rochet et al. 2020 |
| Transient `I_c` suppression -> lower rf-SQUID barrier -> refreeze flux state is new | COLLIDED / PRIOR ART | Zhou/Habif/Bocko/Feldman 2001 |
| Field-free Josephson directionality / superconducting diode effect is new | COLLIDED / PRIOR ART | established before this project |
| Illumination-driven superconducting phase battery / loop vorticity switching is new | COLLIDED / PRIOR ART | Mironov et al. 2024 |
| For sinusoidal `u=0.5(x-delta)^2+beta cos x`, the metastable fold obeys `delta=tan(a)-a`, `beta_c=sec(a)` | DERIVED WITHIN MODEL | exact static bifurcation condition |
| Small-delta sinusoidal fold scaling `beta_c-1 ~ 0.5(3 delta)^(2/3)` | DERIVED ASYMPTOTIC | local expansion |
| General CPR fold satisfies `Ical(x_f,T_f)=x_f-delta`, `dIcal/dx=1` | DERIVED / STANDARD LOAD-LINE FOLD | preferred formulation; not assumed novel |
| General smooth-fold barrier scales as distance-to-fold^(3/2) | DERIVED / STANDARD CATASTROPHE STRUCTURE | coefficient written explicitly for current model |
| Near fold, local mode frequency scales as distance^(1/4) and basic quantum-action scale as distance^(5/4) | DERIVED ASYMPTOTIC | exposes trigger-vs-MQT tradeoff |
| Sinusoidal benchmark `delta=0.05`, `beta_cold=1.5`, `I_c=3 uA` needs 23.53% scalar `I_c` suppression | DERIVED NUMERICAL | gives L=164.55 pH |
| Sinusoidal benchmark cold metastable barrier is 9.443 `k_B K` | DERIVED NUMERICAL | exact stationary-point calculation |
| Adjacent rf-SQUID fluxoid labels imply measured flux difference exactly `Phi0` | REJECTED | benchmark separation is 0.4753 Phi0 |
| Sinusoidal benchmark readout separation is ~0.4753 Phi0 or 5.97 uA | DERIVED NUMERICAL | for L=164.55 pH |
| With C=200 fF sinusoidal benchmark local plasma frequency is ~24.8 GHz | DERIVED NUMERICAL | small oscillation value |
| Cubic-form MQT exponent ~57 at sinusoidal benchmark is an absolute DCR prediction | REJECTED | only provisional diagnostic; dissipative bounce/prefactor absent |
| `beta_hot=1.05` gives ~20-ps deterministic central phase crossing in the sinusoidal RCSJ diagnostic | NUMERICAL MODEL RESULT | not device prediction |
| Published graphene thermal scales imply `D ~0.705 m^2/s` from `l_D~230 um`, `tau_ep~75 ns` | DERIVED CROSS-DEVICE SCALE | inference from Huang et al. characteristic values |
| A 15.5-um^2 square absorber has `L^2/D ~22 ps` under that cross-device diffusion scale | DERIVED CROSS-DEVICE SCALE | comparable to current phase-tipping time |
| The simple damping envelope requires `R_hot < t_hot/(2C)` | DERIVED WITHIN RCSJ ENVELOPE | necessary, not sufficient |
| A graphene-like 15.5-um^2 absorber reproduces the simple 100-um^2-at-1.55-um equal-peak-temperature scaling at 10 um | EXTRAPOLATION | ignores actual optical absorption, proximity effects and diffusion |
| Conditional sinusoidal thermal benchmark gives `eta_th,min ~0.23` to reach 1.2 K at 10 um | CONDITIONAL PLAUSIBILITY | assumes comparable monotonic nonequilibrium `I_c(T_e)` |
| Graphene/proximity CPR can be treated as sinusoidal for final design | REJECTED | measured ballistic graphene CPR is forward-skewed and temperature dependent |
| Titov-Beenakker short-junction CPR is controlled for the 600-nm MoRe/Huang device | REJECTED / MODEL LIMIT | `L_JJ/xi` is order unity using quoted gap scale; arbitrary-length theory required |
| Short ballistic Dirac CPR calculation is a valid final prediction for Experiment 03 | REJECTED | sensitivity model only |
| Short-Dirac sensitivity model shows an interior trigger-vs-stability tradeoff as `beta_cold` is varied | DERIVED MODEL RESULT | optical threshold rises with beta while cold barrier grows |
| In short-Dirac sensitivity model, beta=0.8 gives `T_fold~2.17 K`, cold barrier ~4.41 K, `C_min,Q~0.52 pF` | SUPERSEDED SENSITIVITY RESULT | arbitrary-length model gives materially different values |
| In same short toy model beta=0.7 gives lower fold energy but `C_min,Q~2.1 pF`; beta=0.9 exceeds the 15.5-um^2 10-um energy scaling | SUPERSEDED SENSITIVITY RESULT | preserved only as evidence CPR regime matters |
| Hagymasi-type Matsubara evaluation of the Titov-Beenakker secular equation is valid for arbitrary junction length within the ideal ballistic/rigid-boundary model | ESTABLISHED PRIOR THEORY | primary theoretical basis of current model |
| The implemented arbitrary-length solver converges toward Titov-Beenakker Eq.20 in the controlled short-junction Dirac-point limit | NUMERICAL VALIDATION | normalized CPR sub-percent-to-percent agreement at ell=0.01 with finite grids |
| At ell=1.1, delta=0.05, the ideal cold normalized fold decreases from ~0.463 at mu/Delta0=0 to ~0.200 at mu/Delta0=20 | DERIVED NUMERICAL MODEL RESULT | reflects strongly skewed doped CPR |
| At ell=1.1, mu/Delta0=20, beta_cold=0.8, ideal equilibrium fold occurs near 1.118 K | DERIVED NUMERICAL MODEL RESULT | ballistic rigid-boundary model, not calibrated device |
| The same beta=0.8, mu/Delta0=20 ideal point has cold barrier ~16.70 `k_B K`, `L~87.76 pH`, and state separation ~0.2535 Phi0 / 5.97 uA for Ic0=3 uA | DERIVED NUMERICAL MODEL RESULT | exact full-CPR cold potential within model |
| The same point gives provisional `C_min,Q~71 fF` for D=1e-6 s^-1 | PROVISIONAL MODEL RESULT | relies on cubic MQT diagnostic; not exact DCR |
| At beta=0.8, increasing mu/Delta0 from 0 to 20 leaves ideal T_fold near 1.1 K but raises cold barrier from ~7.0 K to ~16.7 K | DERIVED NUMERICAL MODEL RESULT | doping buys cold stability more than threshold reduction in this model |
| The arbitrary-length ideal model is materially more favorable than the short-junction toy model for the same broad parameter region | DERIVED MODEL COMPARISON | supports continuing; does not imply fabricated-device feasibility |
| The arbitrary-length ballistic/rigid-boundary model is calibrated to the 2026 MoRe/graphene photon detector | REJECTED | interface transparency, contact doping, disorder, inverse proximity and nonequilibrium distribution are not calibrated |
| For arbitrary heat capacity, static photon fold energy is `E_fold=eta_th^-1 int C_e dT` up to `T_f` | DERIVED GENERAL NECESSARY CONDITION | `T_f` determined by full CPR fold |
| Time above fold for lumped monotonic cooling is `int_{T_f}^{T_pk} C_e/P_cool dT` | DERIVED GENERAL NECESSARY CONDITION | finite-rate capture must use this, not just peak T |
| Clean-graphene model `C_e=gamma A T`, `P=Sigma A(T^4-T0^4)` gives an analytic above-fold dwell time | DERIVED WITHIN THERMAL MODEL | recorded in `FEASIBILITY_CLOSURE_2026-08-15.md` |
| The same `T^4` cooling model has a finite maximum dwell time above a fixed fold even as `T_pk -> infinity` | DERIVED MODEL RESULT | `t_max=gamma/(4 Sigma T0^2) ln[(Tf^2+T0^2)/(Tf^2-T0^2)]` |
| If required settling time exceeds that `t_max`, no photon energy can satisfy the dwell condition within the lumped `T^4` model | DERIVED MODEL IMPOSSIBILITY CONDITION | model-specific, potentially useful negative bound |
| Thermal cold stability requires approximately `Delta U_c >= k_B T0 ln(Omega_T/D)` | STANDARD APPROXIMATION | prefactor must be justified for final device |
| Within the provisional cubic MQT model, target DCR gives a closed Lambert-W minimum capacitance `C_min,Q` | DERIVED WITHIN PROVISIONAL MODEL | exact algebra for assumed rate, not exact rf-SQUID MQT physics |
| Dynamic latching gives upper capacitance scales `C<t_>/(2R_hot)` and `C<t_>^2/(g^2 L)` | DERIVED NECESSARY CONDITIONS | damping and phase-passage approximations |
| A necessary capacitance window is `C_min,Q < min(C_max,R,C_max,phi)` | DERIVED MODEL CLOSURE | combines cold quantum stability with write dynamics |
| Subject only to these monotonic constraints, choosing `C~C_min,Q` minimizes write-time burden | DERIVED CONDITIONAL OPTIMUM | readout/parasitic constraints can shift optimum |
| A compact necessary feasibility chain couples photon fold energy, above-fold dwell, cold thermal stability and the capacitance window | DERIVED EXPLORATORY CLOSURE | strongest current theory object; novelty untested |
| The exact single-LWIR calorimetric fold architecture is novel | UNKNOWN / DO NOT CLAIM | major component collisions already found |
| The feasibility closure above is publication-novel | UNKNOWN / ACTIVE COLLISION TARGET | must audit papers and patents after realistic model survives |
| The architecture is superior to SNSPDs, KIDs, graphene-JJ or existing single-photon single-flux detectors | UNKNOWN / DO NOT CLAIM | matched benchmark required |
| Generation A is legitimately photovoltaic | REJECTED TERMINOLOGY | externally flux tilted |
| A zero-external-flux Generation B can be legitimately photovoltaic/photogalvanic | UNKNOWN | depends on final mechanism |
| A publishable paper exists | NO-GO AT PRESENT | see `NOVELTY_GATES.md` |
