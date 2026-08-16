# Experiment 03 — Quantum-Frontier Claim Ledger — 2026-08-16

This continuation ledger governs the post-rate-frontier / open-system claims. It supplements `CLAIM_LEDGER.md`; where an older statement conflicts with this file, the newer disposition below controls.

| Claim | Status | Evidence / boundary |
|---|---|---|
| The reduced fixed-dark capture optimum has a unique fifth-decimal tilt inside `.212-.213` | REJECTED | strict common-random-number pairwise tests resolve no statistically significant fine-tilt winner |
| The reduced fixed-dark optimum is a broad plateau/Pareto band over approximately `.212-.213` | ESTABLISHED WITHIN REDUCED MODEL | strict paired stochastic comparison |
| `.212` should be retained as the engineering representative of that plateau | SUPPORTED DESIGN CHOICE | capture statistically tied while `.212` has lower C, higher phase speed, better flux-noise margin and greater distance from high-tilt catastrophe |
| At `.212`, the Wilson-95%-qualified 99% capture frontier equals exactly `490 um^2` | REJECTED | certification tests only through 490; correct statement is `A99_95lower >= 490 um^2` on tested grid |
| At `.212`, `A99_95lower >= 490 um^2` on the tested 14-um, 2-ns screen | ESTABLISHED WITHIN TWA SCREEN | N=8192 at 470–490 um^2; all Wilson lower bounds >.99 |
| `.214` cannot reach the target merely because the small-amplitude branch approaches local `T_x` | REJECTED | finite-amplitude one-negative periodic branch survives through local sphaleron instability |
| `.214` has a regular pre-action-crossing Gaussian periodic root at `1e-6/s` | REJECTED | bounded high-resolution search finds `min Gamma_per=1.700777e-6/s` at `r=11.787962959` before `r_c` |
| `.214` is impossible in every uniform first-order treatment | NOT ESTABLISHED / DO NOT CLAIM | current exclusion applies only to regular single-saddle Gaussian branch before `r_c`; multi-saddle/thimble/fold-uniform rate remains open |
| The repaired phase-DVR basis is converged across `.212-.213` | ESTABLISHED NUMERICAL GATE | shift-invert spectra; left-well transition-domain shifts ~1.29e-5 K; residuals ~1e-13 K |
| The global cold Gibbs ground state is the correct prepared detector state | REJECTED | global tilted ground state localizes in deeper right well; detector preparation requires metastable left-well conditioned state |
| At 14 um / 490–500 um2 the photon-hot static left well survives | REJECTED WITHIN REDUCED THERMAL MODEL | actual thermal trajectory exceeds the full-CPR left-well fold; hot stationary search has no left minimum |
| The same positive-real environment gives mutually consistent spectral and explicit-circuit dissipated work | ESTABLISHED NUMERICAL GATE | at 10 ns mismatch 4.5e-4–1.18e-3 across `.212-.213` |
| Passive damping can be made fluctuation-free while retaining the same dissipation | REJECTED | same-environment symmetrized FDT work scale is 2.93–3.07 times `2 k_B T0` floor on representative trajectories |
| A 500-ps isolated-phase snapshot `P_R~.9992` establishes a quantum latch | REJECTED | unitary finite-pulse evolution recrosses to `P_R~.0149` by 800 ps; post-reformation span .98431 |
| The isolated nonlinear phase coordinate latches persistently under the photon pulse alone | REJECTED | exact finite-pulse unitary benchmark |
| Environmental dissipation/decoherence is constitutive of basin selection in this architecture | ESTABLISHED LOGICAL REQUIREMENT | without environment there is order-unity coherent recrossing after barrier reformation |
| The historical fixed-hot exact-quench TWA discrepancy was caused by using a pure finite-T broadened Gaussian | REJECTED | repaired thermal Fock-mixture initialization leaves max discrepancies 3.938 and 2.648 percentage points in historical `.8/.6` cases |
| The current symmetrized-FDT TWA `P>=.99` can be called exact quantum efficiency | REJECTED / DO NOT CLAIM | exact closed-quench differences are percentage-scale and finite-pulse latching is fundamentally open-system |
| A local Lindblad model on the auxiliary filter is quantitatively controlled at `.212` | REJECTED AS FINAL MODEL | filter `zeta=0.707`, coupled mode `gamma/omega` up to .640; no weak residual damping parameter |
| A secular global-Davies master equation is quantitatively controlled at `.212` | REJECTED AS FINAL MODEL | mode splitting/(gamma1+gamma2)=.845, not parametrically large; optical rise strongly nonadiabatic |
| Bare Gibbs of the coupled phase+filter Hamiltonian exactly reproduces the damped equilibrium | REJECTED | UV-safe `[x,y,u]` covariance Frobenius mismatch .160; filter-coordinate width differs 7.91% |
| An explicit reaction coordinate plus an ideal Ohmic resistor defines a cutoff-independent quantum state for every auxiliary variable | REJECTED | filter-velocity variance grows linearly with `ln omega_max`; slope 3.781061935e-3 with 1.79e-13 linear-tail residual |
| The phase coordinate itself suffers the same UV divergence | REJECTED | `sigma_x`, `sigma_y`, and phase `sigma_u` are converged to ~1e-12 or better under the same cutoff sweep |
| The direct effective port bath is UV regular for the phase coordinate | ESTABLISHED | `ReY~omega^-4`, hence `J_x~omega^-3`; direct correlation integral finite |
| The direct port equilibrium correlation has a controlled exponential decomposition | ESTABLISHED NUMERICAL/ANALYTIC GATE | two circuit poles + Matsubara poles; independent quadrature max relative error 9.311e-7; KMS error 2.023e-16 |
| Sixteen plain Matsubara terms exactly resolve the correlation at `t=0` | REJECTED | t=0 relative truncation error 8.974e-4 |
| Sixteen plain Matsubara terms resolve the direct-port correlation at one 20-ps optical rise time to ~1e-6 relative error | ESTABLISHED | relative error 9.990e-7 at 20 ps |
| A non-Markovian HEOM / Feynman-Vernon treatment of the direct port is the currently selected quantitative route | CURRENT METHOD DECISION | survives weak-coupling, secular, UV and isolated-latch gates; harmonic-equilibrium validation required before nonlinear use |
| Direct-port HEOM already establishes detector quantum efficiency | NOT YET / DO NOT CLAIM | harmonic Gate B is still pending at time of this ledger |
| A publishable detector-performance paper is now justified | NO-GO | exact nonlinear open-system capture, realistic optics/thermal transport, missing dark channels, reset/readout and novelty remain unresolved |

## Mandatory ordering

Do not bypass the following sequence:

```text
A. direct-port bath correlation              PASS
B. harmonic HEOM versus exact cold FDT       IN PROGRESS
C. nonlinear cold/metastable HEOM gate       NOT STARTED
D. finite-pulse nonlinear HEOM convergence   NOT STARTED
E. exact/open versus N=8192 TWA comparison   NOT STARTED
```

If Gate B fails, repair the bath mapping/counterterm/hierarchy before proceeding. A nonlinear capture number obtained from an unvalidated hierarchy is not admissible evidence.
