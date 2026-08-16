# Experiment 03 — Finite-T / Fold Claim-Ledger Extension

**Date:** 2026-08-15 late-session  
**Purpose:** authoritative extension to `CLAIM_LEDGER.md` for the same-environment finite-temperature escape / optimization continuation.

This file records claims added after the older canonical ledger became dominated by the open-system finite-T calculation. It does **not** authorize novelty claims.

| Claim | Status | Notes |
|---|---|---|
| Under `C->r^2 C`, `R->R/r`, `omega_D->omega_D/r`, the finite-T Euclidean action obeys `B(T;r)=r B0(rT)` | DERIVED EXACT WITHIN MODEL / NUMERICALLY VERIFIED | full nonlocal finite-period saddle; machine-precision regression |
| The regular periodic one-loop prefactor obeys `A_1l(T;r)=r^(-1/2) A_1l,0(rT)` away from bifurcation singularities | DERIVED WITHIN MODEL | follows action-Hessian scaling plus translation collective coordinate |
| Raw dimensionless-action determinant is the physical operator determinant without rescaling | REJECTED | one unmatched `sqrt(A_k)` remains after zero-mode removal |
| `D_op=D_raw/sqrt(A_k)` | CALIBRATED NUMERICAL / ANALYTICAL NORMALIZATION | cubic benchmark reproduces `sqrt(60)` to ~`4e-5` relative |
| `A_1l=omega_c sqrt(I_s/(2pi)) D_raw,corr` is a calibrated absolute periodic-instanton prefactor within the reduced model | DERIVED + BENCHMARKED | still excludes competing physical dark channels |
| UV divergence/slow convergence of the determinant prevents quantitative use | REJECTED | analytic curvature tail reduces hard-case residual `log D` truncation error to few `1e-6` |
| The local sphaleron first-Matsubara instability `T_x` is the physical high-tilt quantum/thermal crossover | REJECTED | finite-amplitude one-negative periodic branch survives above `T_x` |
| The high-tilt finite-T escape topology is first-order-like | DERIVED NUMERICAL MODEL RESULT / CONSISTENT PRIOR THEORY | periodic/sphaleron action crossing occurs above local `T_x` with finite periodic amplitude |
| `r_x`, `r_c`, and `r_f` are the same scale | REJECTED | local instability, action crossing, and periodic fold are numerically distinct |
| At `.212`, `.213`, `.214`, `.215`, first-order action crossings occur at approximately `r_c=12.1821,12.0335,11.8854,11.7374` | DERIVED NUMERICAL MODEL RESULT | one-negative periodic branch continued directly above local `T_x` |
| The physical periodic branch merges continuously into the sphaleron through an O(2) quartic bifurcation | REJECTED | amplitude and `B_sph-B_per` remain finite as `T->T_x`; inferred quartic coefficient does not converge |
| `0.5[1+erf(sqrt(B_sph-B_per))]` is a valid uniform correction for the physical high-tilt branch | REJECTED | based on the falsified continuous quartic sphaleron normal form |
| The finite-amplitude periodic decay saddle collides with a companion branch at a saddle-node/fold | ESTABLISHED NUMERICAL MODEL RESULT | pseudo-arclength passes turning point and recovers companion periodic stationary branch |
| Periodic fold changes even-sector Morse index from one negative mode to two | ESTABLISHED NUMERICAL MODEL RESULT / CONSISTENT PRIOR THEORY | additional even eigenvalue crosses zero; odd translation zero mode remains separate |
| Fold action splitting follows `Delta B ~ mu^(3/2)` | ESTABLISHED NUMERICAL MODEL RESULT | exponents: `.213=1.5060`, `.214=1.5022`, `.215=1.5125` |
| Fold soft eigenvalue follows `|lambda_f| ~ mu^(1/2)` | ESTABLISHED NUMERICAL MODEL RESULT | exponents: `.213=.4859`, `.214=.4840`, `.215=.5284` |
| Fine periodic fold locations are `r_f(.213)=12.16227`, `r_f(.214)=12.00696`, `r_f(.215)=11.85159` | DERIVED NUMERICAL MODEL RESULT | orthonormal-Hessian fold regression |
| Gaussian periodic prefactor divergence near `r_f` is a physical divergent dark-count rate | REJECTED | extra fold eigenvalue tends to zero; ordinary Gaussian steepest descent is nonuniform |
| Naively adding all continued periodic Gaussian saddles and the thermal saddle through the first-order/fold region gives the final physical rate | REJECTED / DIAGNOSTIC ONLY | contributing steepest-descent contour changes; uniform/thimble treatment unresolved |
| `DeltaU/(kBT)` is an absolute rate ceiling that cannot be improved electrically | REJECTED | exponent saturates but generalized thermal attempt dynamics still scale with electrical inertia |
| Same-environment thermal memory-friction diagnostic uses `Gamma_th=(omega_m/2pi)(lambda_b/omega_b) exp(-DeltaU/kBT)` with `C lambda_b^2+lambda_b Y_L(lambda_b)+F_s/L=0` | DERIVED/ESTABLISHED MODEL FORM | reduced-model thermal channel; not complete DCR |
| The `.213` reduced dark target is numerically solved at `r=11.205140965` | DERIVED NUMERICAL MODEL RESULT | `C=26.9944 pF`, `R=7.13958 ohm`, `fc=1.87414 GHz` |
| At that `.213` point, `B_per=39.1140847`, `Gamma_per=9.92694e-7/s`, `Gamma_th=7.32819e-9/s`, total `1.0000225e-6/s` | DERIVED NUMERICAL MODEL RESULT | 72->88 basis shift only `3.6e-6` of target |
| `.213` should be rejected because `T0/Tx~.962` is close to 1 | REJECTED CRITERION | actual Gaussian singularity is later periodic fold; `r_gamma/r_f~.9213` |
| `.213` is approximately 7.9% below its actual periodic fold in electrical scale | DERIVED NUMERICAL MODEL RESULT | `(r_f-r_gamma)/r_f ~ .0787` |
| The safe capture frontier continues increasing through `.213` | REJECTED BY SCREEN | `.212` coarse `A99~500 um^2`; `.213` coarse `A99~489 um^2` |
| The reduced-model capture optimum is interior and occurs somewhere between `.212` and `.213` | CURRENT NUMERICAL CONCLUSION | active narrow scan `.21225/.21250/.21275` will refine it |
| `A99*lambda=const` similarity implies the device has a real optical cutoff of tens of microns | REJECTED INTERPRETATION | only a lumped thermal similarity; realistic wavelength-dependent optics absent |
| `.214+` is physically impossible because the regular Gaussian periodic root disappears | UNKNOWN / DO NOT CLAIM | fold-uniform metastable rate unresolved; those points are simply not rankable yet |
| The fold/Airy universality itself proves an absolute uniform dark rate | REJECTED | topology/scaling fix the catastrophe class, not the metastable integration contour/normalization |
| A publishable detector result now exists | NO-GO | exact nonlinear open-system capture, realistic optics/thermal transport, competing dark channels and novelty audit remain open |

## Immediate interpretation

The most robust design conclusion at this checkpoint is not that the architecture should be pushed arbitrarily toward high tilt. The safe-side capture screen already turns over before the Euclidean fold becomes relevant. Therefore the leading reduced-model operating point can be optimized without using the unresolved fold-uniform rate.

The high-tilt fold remains scientifically valuable because it exposes a nontrivial finite-temperature instanton catastrophe in the same passive detector environment, but it must remain separated from the safe detector optimization until the contributing thimble/uniform rate is derived.
