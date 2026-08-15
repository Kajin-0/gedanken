# Experiment 03 — CLAIM_LEDGER

This ledger is authoritative for claim status. Do not infer novelty from the existence of a derivation.

| Claim | Status | Notes |
|---|---|---|
| An ideal superconducting storage channel with Re Z = 0 lacks the ordinary finite-frequency resistive Johnson contribution | ESTABLISHED BACKGROUND | fluctuation-dissipation statement; not novel |
| Zero resistance implies zero total detector noise | REJECTED | photon statistics, quasiparticles, phase slips, MQT, vortices, stray photons, readout and reset remain |
| A strictly lossless photon-current response naturally accumulates state rather than passively resetting | DERIVED / ELEMENTARY | motivates a latching/integrating architecture |
| Internal superconducting gain alone cannot beat Poisson photon-arrival NEP | DERIVED / STANDARD CONSEQUENCE | signal and photon noise scale together |
| One 10-µm photon has ~124 meV energy | ESTABLISHED | numerical constant |
| Photon-only ideal loop energetic scale L >= Phi0^2/(2 eta_E h nu) is about 108 pH at 10 µm for eta_E=1 | DERIVED SCALE | not a switching criterion; exact rf-SQUID well energies differ |
| Practical 10-µm absorption is generally above the pair-breaking threshold of conventional superconductors | ESTABLISHED PHYSICAL REGIME | weak-coupling sub-gap requirement would demand unrealistically high Tc |
| Brief dissipative absorption followed by persistent superconducting storage is preferable to requiring dissipationless LWIR absorption | WORKING DESIGN CONCLUSION | subject to exact-device analysis |
| A graphene-like calorimeter area near 15.5 µm^2 preserves the simple 100-µm^2-at-1.55-µm heat-capacity scaling | EXTRAPOLATION | ignores wavelength-dependent absorption, heat capacity, doping and diffusion |
| Graphene Josephson single-photon switching can reach ~87% intrinsic efficiency at <1 s^-1 dark count and ~75% at <1/week in the published 1550-nm device | ESTABLISHED PRIOR ART | Huang et al. 2026; corrects earlier one-per-hour statement |
| Photon -> hot graphene -> Josephson escape is a new transduction principle | COLLIDED / PRIOR ART | demonstrated by Huang et al. 2026; earlier GJJ detector proposals also exist |
| Single photon -> persistent superconducting single-flux memory is a new architecture | COLLIDED / PRIOR ART | Onen et al. 2020 experimentally demonstrated single-photon-to-single-flux conversion with multilevel superconducting memory |
| Optical heating -> persistent quantized superconducting flux is new in broad form | COLLIDED / PRIOR ART | Rochet et al. 2020 generated permanent optically written single vortices |
| Transient I_c suppression -> lower rf-SQUID barrier -> refreeze flux state is new in broad form | COLLIDED / PRIOR ART | rf-SQUID tipping-pulse scheme proposed in 2001 |
| For u=0.5(x-delta)^2+beta cos x, the metastable saddle-node obeys delta=tan(a)-a and beta_c=sec(a) | DERIVED WITHIN SINUSOIDAL RF-SQUID MODEL | exact static bifurcation condition |
| Small-delta saddle-node scaling beta_c-1 ~ 0.5(3 delta)^(2/3) | DERIVED ASYMPTOTIC | follows from tan(a)-a expansion |
| Photon-trigger condition beta_cold > beta_c > beta_hot converts the hot event from barrier hopping to metastable-well annihilation | DERIVED DESIGN CONDITION | deterministic only in quasistatic/noiseless idealization |
| Required fractional I_c suppression exceeds 1-beta_c/beta_cold | DERIVED WITHIN MODEL | static threshold; dynamic finite-rate effects remain |
| Near the saddle node Delta U_- ~ (2^(5/2)/3) E_L sin(a) sqrt(cos(a)) (beta-beta_c)^(3/2) | DERIVED ASYMPTOTIC | numerically checked against exact potential near threshold |
| Near the saddle node omega_m scales as (beta-beta_c)^(1/4) and Delta U/(hbar omega_m) as (beta-beta_c)^(5/4) | DERIVED ASYMPTOTIC | exposes cold-stability penalty of operating too close to threshold |
| Benchmark delta=0.05, beta_cold=1.5, I_c=3 uA requires ~23.5% I_c suppression | DERIVED NUMERICAL | gives L=164.6 pH in the sinusoidal model |
| Benchmark cold metastable barrier is ~9.44 k_B K and favored-well reverse barrier ~16.57 k_B K | DERIVED NUMERICAL | exact stationary-point calculation |
| Adjacent rf-SQUID fluxoid wells necessarily differ in measured loop flux by exactly Phi0 | REJECTED | benchmark separation is ~0.475 Phi0; early Phi0/L estimate was only an idealized scale |
| Benchmark measured-state separation is ~0.475 Phi0 or ~5.97 uA circulating-current difference | DERIVED NUMERICAL | for L=164.6 pH |
| With C=200 fF the benchmark metastable-well plasma frequency is ~24.8 GHz | DERIVED NUMERICAL | local small-oscillation value |
| Cubic-form MQT diagnostic exponent is ~57 at the benchmark | PROVISIONAL DIAGNOSTIC | not an absolute DCR; exact dissipative bounce/prefactor still required |
| A beta_hot=1.05 pulse drives deterministic phase crossing on ~20-ps scale in the benchmark RCSJ diagnostic | NUMERICAL MODEL RESULT | robust across tested weak/moderate damping; not yet a device prediction |
| Phase tipping can be much faster than the ~75-ns graphene hot-electron pulse benchmark | PLAUSIBILITY RESULT | conditional on realistic I_c(T_e) crossing beta_c |
| Hot quasiparticle conductance could provide write-time damping while cold storage remains low-loss | RESEARCH HYPOTHESIS | must be modeled/validated; no permanent shunt assumed |
| Lowering plasma frequency through larger C can suppress MQT while remaining fast compared with ns thermal dynamics | PROVISIONAL DESIGN INSIGHT | quantitative optimum not established |
| A small external flux tilt is the cleanest Generation-A proof architecture | WORKING DESIGN CHOICE | not a novelty claim |
| A phi0 / Josephson-diode element could replace external flux bias for self-directed capture | RESEARCH HYPOTHESIS | requires independent collision and quantitative audit |
| The exact single-LWIR calorimetric bifurcation architecture is novel | UNKNOWN / DO NOT CLAIM | several major components already collide; dedicated audit not complete |
| A new general bifurcation/dark-count performance bound exists | UNKNOWN / ACTIVE TARGET | possible surviving theory route |
| The architecture is superior to SNSPDs, KIDs or existing single-photon single-flux detectors | UNKNOWN / DO NOT CLAIM | requires matched performance comparison |
| The architecture is legitimately photovoltaic at zero external bias | UNKNOWN | terminology depends on final physical mechanism |
| A publishable theorem or paper exists | NO-GO AT PRESENT | see NOVELTY_GATES.md |
