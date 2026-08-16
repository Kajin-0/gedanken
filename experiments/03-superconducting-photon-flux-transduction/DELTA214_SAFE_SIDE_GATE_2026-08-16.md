# Experiment 03 — Delta .214 Safe-Side Dark-Rate Gate — 2026-08-16

## Question

Does the physically relevant finite-amplitude, one-negative periodic branch at `delta=.214` reach the reduced dark target

```text
Gamma_per = 1e-6 /s
```

while still on the regular single-saddle side of the first-order periodic/sphaleron action crossing?

This is deliberately a safe-side question. It does not attempt to assign a final absolute rate through the multi-saddle/Stokes/fold region by summing separate Gaussian contributions.

## Branch topology already established

For `delta=.214`:

```text
r_x = 11.611084804        local sphaleron Matsubara instability
r_c = 11.885380810        finite-amplitude periodic/sphaleron action crossing
r_f = 12.0069623          finite-amplitude periodic fold
```

The dominant periodic branch remains finite-amplitude and has exactly one negative mode through local `r_x`. Therefore the old conclusion that `.214` is unavailable merely because the ordinary small-amplitude branch approaches local crossover is obsolete.

## CI regression

Workflow:

```text
.github/workflows/experiment03-delta214-large-branch-rate.yml
run 31972574115
head dd020a387ad87321d23bfb1d96e08b6e7d48160d
conclusion: success
```

The production script is

```text
calculations/large_branch_one_loop_rate_214.py
```

It:

1. seeds the finite-amplitude one-negative branch at `0.94 T_x`;
2. continues that same branch to the physical `T0=20 mK` for each electrical scale `r`;
3. evaluates the UV-tail-corrected, cubic-calibrated Gaussian periodic one-loop determinant;
4. scans to `0.998 r_c`;
5. detects the nonmonotonic rate minimum rather than assuming monotonicity;
6. performs a bounded scalar minimization of `log Gamma_per(r)` around that minimum;
7. re-evaluates the minimum and safe-edge states at `nbasis=80`, `ngrid=10240`;
8. checks one negative mode and the odd translation zero-mode overlap.

## Result

The coarse scan decreases from

```text
r=11.450000000   Gamma_per=2.079588e-6 /s
```

to a shallow minimum near `r~11.79`, then rises again as the fluctuation determinant softens approaching the first-order region.

The high-resolution bounded minimum is

```text
r_min                 = 11.787962959
Gamma_per,min         = 1.700777e-6 /s
B_min                 = 38.753236410
A_1loop,min           = 1.150705e11 /s
periodic amplitude    = 0.07757984
negative modes        = 1
translation overlap   = 1.000000000
r_min / r_c           = 0.991803557
Gamma_per,min/target  = 1.700777
```

The high-resolution safe-edge point at `r=0.998 r_c` is

```text
r_safe        = 11.861610048
Gamma_per     = 1.737132e-6 /s
```

and remains on the one-negative finite-amplitude branch.

## Disposition

\[
\boxed{
\min_{r<r_c\;\text{(regular branch)}}\Gamma_{per}(\delta=.214,r)
\approx1.7008\times10^{-6}\ \mathrm{s}^{-1}
>10^{-6}\ \mathrm{s}^{-1}
}
\]

Therefore:

```text
NO_SAFE_ROOT_BEFORE_ACTION_CROSSOVER
```

for the calibrated Gaussian periodic contribution at `delta=.214`.

This is stronger than the earlier statement that the ordinary Gaussian branch did not expose a root. The actual dominant finite-amplitude branch has now been followed and its entire regular pre-action-crossing rate minimum remains about 70% above target.

## What this does and does not prove

It **does prove within the current reduced same-environment one-loop model** that `.214` has no target-rate operating point on the regular dominant periodic branch before the first-order action crossing.

It **does not prove** that the exact physical total escape rate has no `1e-6 /s` solution somewhere in the first-order/fold region. That region requires a uniform/thimble-aware treatment because multiple stationary saddles exchange dominance and the separate Gaussian determinant becomes nonuniform near the fold.

Accordingly, `.214` cannot enter the canonical safe design frontier unless a controlled first-order/fold-uniform rate calculation changes this conclusion.

## Design consequence

The safe reduced-model frontier is now cleanly separated:

```text
delta=.212-.213   accepted safe plateau/Pareto band
delta=.212        engineering representative; N=8192 Wilson-qualified A99 >=490 um^2 on tested grid
delta=.214        no safe pre-crossover Gaussian dark-rate root
delta>.214        deeper into the same first-order/fold-uniform problem
```

This strengthens the decision to retain `.212` rather than spend additional stochastic compute trying to make `.214` win the capture comparison under an inconsistent dark-rate validity class.
