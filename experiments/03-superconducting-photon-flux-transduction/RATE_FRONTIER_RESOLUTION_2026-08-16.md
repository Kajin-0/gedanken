# Experiment 03 — Rate-Frontier Resolution — 2026-08-16

## Purpose

Close the two rate-frontier gates left open in `RATE_FRONTIER_PROMOTION_2026-08-16.md`:

1. replace the historical `.213` capture matrix with the exact-total-dark-root rerun;
2. classify the `.214` large-periodic-branch rate search on the controlled pre-action-crossing Gaussian branch.

This checkpoint concerns the reduced same-environment model only. It is not a complete physical detector DCR or exact quantum efficiency claim.

## 1. Exact-root `.213` capture rerun — COMPLETE

Canonical dark scale:

```text
delta   = .213
r_Gamma = 11.2051409652
C       = 26.994365 pF
R       = 7.139580 ohm
fc      = 1.874143 GHz
```

Workflow:

```text
.github/workflows/experiment03-one-loop-213-capture.yml
run 31972394510
head d3c60d2bb50aa36a153304dee560e80a2f6b7345
N = 4096 per area
lambda = 14 um
rise = 20 ps
post-pulse classification = 2 ns
```

Results:

| area (`um^2`) | `P_final` | Wilson 95% CI | failures |
|---:|---:|---:|---:|
| 455 | 0.99829102 | [0.99647634, 0.99917191] | 7 |
| 465 | 0.99731445 | [0.99519722, 0.99849974] | 11 |
| 475 | 0.99560547 | [0.99306381, 0.99721838] | 18 |
| 485 | 0.99218750 | [0.98899217, 0.99446049] | 32 |
| 495 | 0.98876953 | [0.98505361, 0.99156952] | 46 |
| 505 | 0.98315430 | [0.97873636, 0.98666683] | 69 |

The exact-root rerun completed successfully.

Define

```text
A99_point    = largest tested area with central P_final >= .99
A99_95lower  = largest tested area with Wilson 95% lower bound >= .99
```

Then on this tested `.213` grid,

```text
A99_point   >= 485 um^2 and < 495 um^2 on the tested points
A99_95lower >= 475 um^2 and < 485 um^2 on the tested points
```

The inequalities are grid statements. They do not imply an interpolated exact crossing.

The previous `.213` matrix at `RSC=11.19986413` is now historical/superseded for exact-frontier use.

## 2. Consequence for the `.212-.213` plateau

The `.212` high-stat certification remains

```text
N = 8192 per area
A99_point   >= 490 um^2 on tested grid
A99_95lower >= 490 um^2 on tested grid
```

whereas the exact-root `.213` independent run gives the weaker confidence-qualified grid statement above.

This strengthens the engineering choice `delta_rep=.212`, but it does **not** by itself overturn the strict common-random-number result that no statistically significant fine-tilt winner was resolved over `.212-.213`. The `.212` and `.213` certification runs use different sample sizes/seeds and are not an exact paired hypothesis test.

Therefore the canonical interpretation remains:

```text
reduced-model optimum = broad plateau/Pareto band over approximately .212-.213
engineering representative = .212
```

with stronger empirical certification now available at the lower edge.

## 3. `.214` controlled Gaussian safe-side gate — COMPLETE NEGATIVE RESULT

The `.214` finite-amplitude one-negative periodic branch is real and survives through the local sphaleron Matsubara instability. The relevant topology scales are approximately

```text
r_x = 11.611084804
r_c = 11.885380810
r_f = 12.0069623
```

The dedicated large-branch rate workflow was repaired to search the regular dominant branch through `0.998 r_c`, while preserving branch identity (`nneg=1`, translation-zero overlap approximately unity) and checking the high-basis safe edge.

Canonical successful workflow:

```text
.github/workflows/experiment03-delta214-large-branch-rate.yml
run 31972574115
head dd020a387ad87321d23bfb1d96e08b6e7d48160d
```

The rate decreases after the local instability, reaches an interior minimum, and rises again before the action crossing. The resolved minimum is

```text
r_min          = 11.787962959
Gamma_per,min  = 1.700777e-6 /s
B_min          = 38.753236410
A1_min         = 1.150705e11 /s
periodic amp   = 0.07757984
n_negative     = 1
zero overlap   = 1.000000000
r_min/r_c      = 0.991803557
```

At the conservative safe edge

```text
r_safe = 0.998 r_c = 11.861610048
Gamma_per(r_safe) = 1.737132e-6 /s
```

so the entire controlled pre-action-crossing regular periodic branch remains above the target

```text
Gamma_target = 1.0e-6 /s.
```

The workflow therefore passes with the scientific classification

```text
NO_SAFE_ROOT_BEFORE_ACTION_CROSSOVER
```

rather than treating absence of a root as a software failure.

## 4. What the `.214` result establishes

Within the current cubic-calibrated Gaussian one-loop treatment of the regular one-negative periodic saddle,

```text
min_{regular branch, r < r_c} Gamma_per(.214) / Gamma_target = 1.700777.
```

Thus `.214` cannot satisfy the reduced `1e-6/s` target anywhere before the first-order action crossing, even before adding the positive thermal contribution.

This is stronger than the obsolete statement that `.214` merely failed on the small-amplitude/local-crossover branch.

## 5. What the `.214` result does NOT establish

Do not claim that `.214` is impossible under every treatment.

Any putative `.214` target solution must enter the first-order multi-saddle/Stokes/fold-uniform regime where separate Gaussian saddle contributions are nonuniform and cannot be naively ranked or summed. A thimble-aware or otherwise uniform rate treatment would be required before `.214+` can be reconsidered as a design frontier.

Accordingly:

```text
.212 = canonical safe engineering representative
.213 = accepted safe-side plateau member, exact-root capture now resolved
.214 = excluded from the controlled pre-crossing Gaussian design frontier
       but remains an open uniform-crossover research problem
```

## 6. Next frontier after this closure

The rate-constrained safe-side design frontier no longer needs additional `.214` capture work. Such a capture calculation would mix a controlled real-time screen with an unresolved first-order dark-rate model and is therefore not admissible as a canonical comparison.

Priority now moves to the exact/open-system quantum sequence already defined in `OPEN_SYSTEM_METHOD_GATE_2026-08-16.md` and `CLAIM_LEDGER_QUANTUM_FRONTIER_2026-08-16.md`:

```text
A. direct-port bath correlation              PASS
B. harmonic HEOM versus exact cold FDT       IN PROGRESS
C. nonlinear cold/metastable HEOM gate       NOT STARTED
D. finite-pulse nonlinear HEOM convergence   NOT STARTED
E. exact/open versus N=8192 TWA comparison   NOT STARTED
```

Do not bypass Gate B. If the harmonic hierarchy fails to reproduce the independently known FDT covariance, repair the bath mapping, counterterm, exponential decomposition or hierarchy convergence before nonlinear capture is attempted.
