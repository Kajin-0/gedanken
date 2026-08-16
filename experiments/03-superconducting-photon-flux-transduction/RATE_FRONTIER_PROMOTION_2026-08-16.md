# Experiment 03 — Rate-Constrained Frontier Promotion — 2026-08-16

## Purpose

This checkpoint promotes the completed safe-side capture evidence after the strict paired `delta=.212-.213` plateau analysis, records the exact-root correction for the `.213` capture screen, and separates the newly opened `.214` finite-amplitude branch from the canonical safe design.

This is still an exploratory reduced-model checkpoint. It is **not** a physical detector efficiency or complete dark-count claim.

## 1. Canonical reduced-model representative

The strict common-random-number comparison found no statistically resolved fine-tilt winner over

```text
delta = .21200, .21225, .21250, .21275, .21300
```

at `A=490,495,500 um^2` with `N=2048` per candidate and exact paired McNemar comparisons. The reduced-model optimum is therefore a **plateau/Pareto band**, not a fifth-decimal optimum.

The engineering representative remains

```text
delta_rep = .212
```

because capture is statistically tied across the plateau while `.212` has lower compensated capacitance, higher phase clock, lower local flux-bias dark-rate sensitivity, and greater distance from the high-tilt periodic-instanton fold.

## 2. Exact `.212` dark operating point used for certification

The high-stat certification used

```text
delta       = .212
r_Gamma     = 10.6229699624
C           = 24.262211 pF
R           = 7.5308506 ohm
fc          = 1.9844267 GHz
T_fold      = 0.2785303 K
Gamma_per   = 9.976990612e-7 /s
Gamma_th    = 2.304378181e-9 /s
Gamma_total = 1.000003439e-6 /s
```

The dark-rate quantity is the reduced same-environment phase-escape model only. Quasiparticle, vortex, stray-photon, cosmic/environmental and technical-noise dark channels are not included.

## 3. `.212` high-stat capture certification

Workflow:

```text
.github/workflows/experiment03-delta212-certification.yml
run 31926948721
head e3bbd791dbb48b97dc3da43247fc2e7c3723e42b
N = 8192 per area
lambda = 14 um
rise = 20 ps
post-pulse classification = 2 ns
dt = .125 ps
```

Results:

| area (`um^2`) | `P_final` | Wilson 95% CI | failures | Wilson lower >= .99 |
|---:|---:|---:|---:|---:|
| 470 | 0.99645996 | [0.99492055, 0.99753399] | 29 | yes |
| 475 | 0.99438477 | [0.99251878, 0.99578731] | 46 | yes |
| 480 | 0.99230957 | [0.99017354, 0.99398410] | 63 | yes |
| 485 | 0.99365234 | [0.99168607, 0.99515586] | 52 | yes |
| 490 | 0.99243164 | [0.99031039, 0.99409128] | 62 | yes |

All five jobs passed.

### Promotion

Define separately:

```text
A99_point    = largest tested area whose central P_final >= .99
A99_95lower  = largest tested area whose Wilson 95% lower bound >= .99
```

On the tested certification grid,

```text
A99_point   >= 490 um^2
A99_95lower >= 490 um^2
```

The inequalities are deliberate: `490 um^2` was the largest area in this certification matrix, so this run does **not** locate the upper crossing beyond 490. Do not rewrite either result as an exact `A99=490 um^2` boundary.

The non-monotonic central estimates between 480, 485 and 490 are compatible with finite Monte Carlo sampling and are another reason to report confidence-qualified grid statements rather than interpolate a false sharp threshold.

## 4. `.213` capture-screen provenance correction

The first accepted `.213` capture workflow used

```text
RSC = 11.19986413
```

in `one_loop_rate_capture_213.py` and produced the historical `N=4096` screen:

| area (`um^2`) | `P_final` | Wilson 95% CI |
|---:|---:|---:|
| 455 | 0.99829102 | [0.99647634, 0.99917191] |
| 465 | 0.99755859 | [0.99551147, 0.99867331] |
| 475 | 0.99682617 | [0.99457710, 0.99814421] |
| 485 | 0.99438477 | [0.99158779, 0.99625529] |
| 495 | 0.99096680 | [0.98757435, 0.99343919] |
| 505 | 0.98315430 | [0.97873636, 0.98666683] |

However, the later exact total-dark-rate solve established

```text
r_Gamma(.213) = 11.2051409652
```

with `Gamma_per + Gamma_th ~= 1e-6 /s` and converged basis behavior. The relative difference in the old capture scale is only about `4.71e-4`, but the capture screen must still be tied to the exact dark manifold before it is used for a canonical cross-tilt comparison.

Therefore the old `.213` capture matrix is **historical/superseded for exact-frontier purposes**, not discarded evidence.

On 2026-08-16 the capture script was corrected to

```text
RSC = 11.2051409652
commit d3c60d2bb50aa36a153304dee560e80a2f6b7345
```

which triggered exact-root rerun

```text
workflow run 31972394510
```

The rerun result must replace the historical matrix in any future canonical `.213` frontier table.

## 5. `.214` branch status

The old statement that `.214` cannot reach the dark target on the ordinary Gaussian branch is obsolete as a physical branch-topology conclusion. Direct continuation established a distinct finite-amplitude one-negative periodic branch and a later first-order action crossing/fold.

The current topology numbers are approximately

```text
r_x(.214) = 11.61108
r_c(.214) = 11.88538
r_f(.214) = 12.0069623
```

with fold scaling consistent with

```text
Delta B ~ mu^(3/2)
|lambda_f| ~ mu^(1/2)
```

for `mu = p_f-p`.

Commit

```text
f31b9563ef541c39a374568f90184980539e85f7
```

added

```text
calculations/large_branch_one_loop_rate_214.py
```

which explicitly seeds and continues the finite-amplitude one-negative branch and evaluates the existing UV-corrected, cubic-calibrated Gaussian one-loop determinant.

This code was **not** accompanied by a workflow/result at that commit. A dedicated CI gate was added at

```text
commit 08ac06b1751489cafee24fa9a84a95da3f117cc0
workflow experiment03-delta214-large-branch-rate.yml
run 31972398816
```

The `.214` branch remains **research-only / not canonical** until the CI result is inspected and an independent branch/rate regression confirms that the target root is sufficiently separated from the finite-amplitude fold for the Gaussian saddle approximation being used.

Do not allow `.214` to displace `.212` merely because a formal large-branch root exists.

## 6. Current interpretation

The strongest safe-side reduced-model statement is now:

> The fixed-dark-rate capture frontier rises into a broad plateau over approximately `delta=.212-.213`. Strict paired stochastic comparisons do not resolve a unique fine-tilt winner. At the lower edge, `delta=.212` has a high-statistics `N=8192` capture certification with the Wilson 95% lower bound above 0.99 through the largest tested area, `490 um^2`. The lower edge remains the engineering representative because its capture is statistically tied while its electrical and robustness margins are better. Higher tilt `.214+` is a separate finite-amplitude-instanton research branch and is not yet part of the canonical design frontier.

## 7. Immediate continuation

1. Read exact-root `.213` rerun 31972394510 and replace the historical `.213` matrix with its result.
2. Read `.214` large-branch CI run 31972398816.
3. If `.214` passes, add an independent convergence/branch-identity regression at the resulting root before any capture screen.
4. Only after that regression passes should `.214` receive the same 2-ns capture test.
5. Independently continue the repaired phase-DVR and passive work/noise regressions.
6. Do not refine tilt inside `.212-.213` further unless robust uncertainty analysis makes that resolution physically meaningful.
