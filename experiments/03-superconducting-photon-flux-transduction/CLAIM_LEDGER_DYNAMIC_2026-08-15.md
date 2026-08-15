# Experiment 03 — Dynamic Claim Ledger — 2026-08-15

This ledger covers the full-nonlinear / nonadiabatic stage after `CLAIM_LEDGER_CONTINUATION_2026-08-15.md`. Until consolidation, all Experiment-03 claim ledgers together are authoritative.

| Claim | Status | Notes |
|---|---|---|
| Static fold disappearance `T_peak >= T_f` is necessary for photon-triggered switching | REJECTED | full nonlinear solver produces successful trajectories with `T_peak < T_f` |
| Static fold disappearance is sufficient for persistent capture | REJECTED | capture also depends on rise time, damping, inertia, cooling and retrapping |
| The local overdamped saddle-node ghost estimate is the final capture criterion | REJECTED / ASYMPTOTIC ONLY | full solver shows inertia acquired before the soft region can reverse its pessimistic verdict |
| Full deterministic scalar-R solver reproduces the retained static folds near 0.812 K (`rDelta=0.8`) and 0.694 K (`rDelta=0.6`) | NUMERICAL REGRESSION | full-CPR interpolation is consistent with static branch |
| At 14 um instantaneous deposition, current scalar-R model has lower capture boundary near 111 ohm for `rDelta=0.8` | DERIVED NUMERICAL MODEL RESULT | not fabricated-device specification |
| At 14 um instantaneous deposition, current scalar-R model has lower capture boundary near 32.7 ohm for `rDelta=0.6` | DERIVED NUMERICAL MODEL RESULT | not fabricated-device specification |
| `rDelta=0.6` scalar-R model develops an upper weak-damping/retrapping boundary near 1.13 kOhm | DERIVED NUMERICAL MODEL RESULT / CLASSIFICATION-SENSITIVE | depends on finite observation time and scalar-R model |
| Faster thermal/electronic rise materially improves nonadiabatic capture | DERIVED NUMERICAL MODEL RESULT | now a first-order control variable |
| Current 14-um model retains ordinary capture for `rDelta=0.8` through roughly 9-ps rise but becomes weak-damping/settling sensitive near 9.5–10 ps | CONDITIONAL NUMERICAL MODEL RESULT | depends on thermal model, scalar R and CPR envelope |
| Current 14-um model retains capture for `rDelta=0.6` through roughly 30-ps rise and loses it broadly around 32 ps | CONDITIONAL NUMERICAL MODEL RESULT | same limitations |
| Sub-fold fast switching is a new general dynamical phenomenon | COLLIDED / PRIOR ART | general rate-induced tipping / loss-of-tracking under fast parameter changes is established |
| Sudden-quench threshold satisfies `B_q(T_q)=U(x_s,T_q)-U(x_c,T_q)=0` | DERIVED EXACTLY FOR FIXED-HOT CONSERVATIVE QUENCH | detector-specific use; novelty untested |
| Current full-CPR quench thresholds are `T_q~0.718 K` (`rDelta=.8`) and `~0.615 K` (`rDelta=.6`) | DERIVED NUMERICAL MODEL RESULT | same CPR/interface model as full solver |
| For current 100-um2 calibration, `lambda_fold~14.7 um`, `lambda_q~18.8 um` at `rDelta=.8` | DERIVED MODEL RESULT | `lambda_q` is ideal held-hot quench scale, not detector cutoff |
| For current 100-um2 calibration, `lambda_fold~20.1 um`, `lambda_q~25.6 um` at `rDelta=.6` | DERIVED MODEL RESULT | same caveat |
| The useful model hierarchy is `lambda_fold < lambda_dynamic < lambda_quench` | DERIVED FOR CURRENT FAMILIES | not asserted universal for arbitrary drive/control |
| Full finite-cooling capture extends beyond quasistatic fold wavelength | DERIVED NUMERICAL MODEL RESULT | due nonadiabatic/inertial barrier crossing |
| Intrinsic graphene electronic redistribution is necessarily slower than the current 9–30 ps rise windows | REJECTED BY LITERATURE AS GENERAL CLAIM | primary literature contains sub-ps to few-ps response regimes; cryogenic GJJ calibration still missing |
| Large optical collection area implies the full absorber must become spatially isothermal before the CPR responds | REJECTED | local weak-link temperature/distribution is the relevant control; geometry matters |
| Characteristic Huang diffusion scale gives `D_char~0.705 m^2/s` | DERIVED CROSS-DEVICE SCALE | from `l_D^2/tau`; not calibrated transient diffusivity |
| Current rise windows correspond to rough diffusion distances `~2.5 um` (`r=.8`) and `~4.6 um` (`r=.6`) | CONDITIONAL GEOMETRY SCALE | assumes simple `d^2/D` and current model rise thresholds |
| Exact scalar-R phase energy satisfies `dE_phi/dt=U_T dotT-(L/R)xdot^2` | DERIVED EXACTLY | elementary time-dependent mechanics identity |
| Instantaneous separatrix-relative energy satisfies `E_s(0+)=-B_q(T_h)` | DERIVED EXACTLY | recovers sudden-quench threshold energetically |
| Damping is always beneficial to capture | REJECTED | hurts launch energy before crossing, can help target retrapping after crossing |
| Damping is always harmful to capture | REJECTED | insufficient post-crossing damping can permit oscillatory return/retrapping |
| A single broadband constant resistor is the likely optimal environment | UNKNOWN / CURRENTLY DISFAVORED | full dynamics points toward stage/frequency/state-dependent admittance; FDT/MQT must be included |
| Frequency/state-dependent dissipation can be optimized without added fluctuations | REJECTED | fluctuation-dissipation and dissipative MQT must use the same environment |
| Generic rate-induced tipping is novel to Experiment 03 | COLLIDED / PRIOR ART | Ashwin, Wieczorek and subsequent theory |
| The detector-specific three-threshold / phase-work / dark-stability closure is novel | UNKNOWN / ACTIVE COLLISION TARGET | no priority language authorized |
| Current full nonlinear deterministic model is a calibrated device prediction | REJECTED | CPR interfaces, thermal rise, spatial transport, causal admittance, stochastic noise and dissipative MQT remain incomplete |
| A publishable manuscript is justified now | NO-GO | novelty and quantitative gates remain open |
