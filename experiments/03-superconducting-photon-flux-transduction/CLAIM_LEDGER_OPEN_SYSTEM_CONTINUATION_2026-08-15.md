# Experiment 03 — Open-system / dark-action claim ledger continuation — 2026-08-15

This ledger continues `CLAIM_LEDGER_DYNAMIC_2026-08-15.md`. Both files remain part of the authoritative claim history until later consolidation.

| Claim | Status | Notes |
|---|---|---|
| The old cubic MQT exponent `7.2 DeltaU/(hbar omega_c)` accurately describes the live cold barrier | **REJECTED** | exact isolated actual-CPR bounce gives `B_iso~25.03` versus cubic `~38.04` |
| The live barrier shape factor is close to the textbook cubic value 7.2 | **REJECTED** | exact live `beta_U~4.74` |
| The passive two-pole environment adds an enormous dark-action correction that automatically rescues the baseline | **REJECTED** | full same-environment nonlocal bounce gives `B=29.765636`, only `+4.728` above isolated |
| The converged baseline nonlocal bounce has the correct one-negative-mode saddle signature | **NUMERICAL VALIDATION** | spectral basis converged and Hessian has exactly one negative even mode |
| The baseline `C=215 fF,R=80 ohm,alpha=.90` point is acceptable as the final dark-stable candidate | **REJECTED UNDER CURRENT ZERO-T ACTION SCREEN** | exact `B~29.77` is many action units below the provisional target region |
| Pure electrical similarity `C->r^2 C, R->R/r, omega_D->omega_D/r` at fixed static potential and normalized environment gives `B->rB` | **DERIVED EXACTLY WITHIN THE MODEL** | also `omega_c->omega_c/r`, `g` and `alpha` invariant |
| Along the same pure electrical similarity, `B rho` is invariant for fixed physical rise time | **DERIVED EXACTLY WITHIN THE MODEL** | exposes dark-action / phase-speed tradeoff |
| Electrical dark-action rescue necessarily destroys photon capture | **REJECTED IN CURRENT SCREEN** | `r~1.2635` retains high capture; post-rescue A99 only modestly below unscaled baseline |
| Pure strong `beta_cold` barrier shaping is the preferred rescue | **REJECTED / SPECTRALLY DOMINATED IN CURRENT SCREEN** | beta=.85/.90 raise action but raise fold and strongly reduce 14-um area margin |
| Mild beta=.825 plus smaller electrical compensation beats pure electrical rescue | **REJECTED** | equal-action hybrid A99 only ~75–76 um2 vs ~83–84 for beta=.80 pure electrical rescue |
| Reducing directional tilt is nearly a free dark-action lever | **REJECTED** | action rises but one-sided basin capture collapses; delta=.035 P(80 um2)~.922 |
| For a linearly tilted one-coordinate potential, increasing positive tilt toward the escape direction lowers the stationary dissipative bounce action for a tilt-independent linear environment | **DERIVED EXACTLY / ENVELOPE-THEOREM SIGN RESULT** | `dB_diss/delta=-(E_L/hbar) int[x_b-x_m]d tau <0` while the relevant bounce exists |
| Increasing positive tilt can never improve a jointly dark-constrained design | **REJECTED** | lost zero-T action can be restored with a distinct electrical control, creating a constant-action Pareto manifold |
| Constant-zero-T-action high-tilt compensation can improve the current 14-um capture area substantially | **DERIVED NUMERICAL MODEL RESULT** | A99 grows from ~83–84 um2 at delta=.05 to ~210 um2 by delta=.14 under the sym-FDT TWA screen |
| Equal zero-temperature bounce action means equal physical dark-count rate | **REJECTED** | finite-T activation/crossover, prefactor and other dark channels vary with tilt and remain unresolved |
| The fixed-100 equivalent wavelengths inferred from `A lambda=const` are physical detector cutoffs | **REJECTED** | they are reduced-model screening translations assuming constant absorption and lumped thermal similarity |
| The reduced optical capture model obeys `Pcap=P(eta_abs/(A lambda))` at fixed circuit/material/rise/cooling | **DERIVED EXACTLY WITHIN THE LUMPED MODEL** | therefore target-fidelity contours satisfy `A_p lambda/eta_abs=const` |
| The high-tilt spectral improvement through delta=.14 is mostly a new dynamic basin effect | **DISFAVORED / DECOMPOSED** | fold-normalized `Q99=A99(Tf^2-T0^2)` changes only ~10%; most gain is static fold reduction with directionality preventing dynamic loss |
| Electrical compensation narrows the cold harmonic phase width as `sigma_x->sigma_x/sqrt(r)` | **DERIVED EXACTLY WITHIN HARMONIC LOW-T APPROXIMATION** | compensation simultaneously raises action, slows clock and narrows absolute phase cloud |
| Constant-action compensation can approach the cold saddle-node with no speed penalty | **REJECTED BY ASYMPTOTIC** | generic fold gives `omega_c,* ~ epsilon^(3/2)` and response time `~epsilon^(-3/2)` |
| Near the saddle-node, constant-action compensation makes the phase cloud parametrically narrower relative to the basin width | **REJECTED BY ASYMPTOTIC** | both compensated sigma_q and minimum-saddle distance scale as `epsilon^(1/2)`, so ratio remains O(1) |
| The cold double well disappears near delta=.14 | **REJECTED** | static topology remains bistable through .26 and is absent by .27 |
| The accepted nonlocal one-negative-mode bounce continuation remains valid arbitrarily close to the cold fold | **REJECTED AS NUMERICAL CLAIM** | sparse solver retains one negative mode through .25 but gives two negative modes/poor stationarity at .26; do not use .26 action |
| Classical thermal activation at 20 mK is already the dominant constraint by delta=.085 | **REJECTED BY CRUDE SCREEN** | barrier exponent remains >265 through .085; higher-tilt finite-T boundary still being mapped |
| A physical efficiency or DCR can now be quoted | **NO-GO** | nonlinear detailed-balance quantum capture, normalized prefactor/finite-T tunneling, competing dark channels and optics remain blockers |
| A manuscript is justified now | **NO-GO** | frontier is still moving and physical quantum/dark/optical gates remain open |

## Active unresolved claim

The present numerical question is whether

\[
A_{99}(\delta\mid B_{T=0}=37.61)
\]

has an interior finite-time optimum before finite-temperature dark stability or the cold metastable fold terminates the useful branch. Sparse equal-action capture at `delta=.15,.16,.18` is the current falsification test.
