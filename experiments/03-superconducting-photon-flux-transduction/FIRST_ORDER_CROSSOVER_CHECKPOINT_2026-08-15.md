# Experiment 03 — First-Order Quantum/Thermal Crossover Checkpoint

**Date:** 2026-08-15 late-session continuation  
**Status:** canonical correction; publication remains **NO-GO**

## 1. Core correction

The finite-temperature dissipative instanton program originally identified the temperature where the sphaleron's first nonzero Matsubara eigenvalue vanishes,

\[
\Lambda_1(T_\times)=0,
\]

with the physical quantum-to-thermal crossover. That identification is **rejected** in the high-directional-tilt region relevant to the current detector optimum.

The reduced model exhibits a finite-amplitude **first-order periodic-instanton topology**:

- a one-negative-mode periodic decay saddle survives through and above local `T_x`;
- its action crosses the static sphaleron action at a later scale `T_c`;
- the finite-amplitude periodic branch then terminates at a still later saddle-node/fold `T_f` where it collides with a two-negative companion branch.

Thus

\[
\boxed{T_x\neq T_c\neq T_f}
\]

and equivalently along the electrical similarity family

\[
\boxed{r_x\neq r_c\neq r_f}.
\]

This structure is consistent with established periodic-instanton bifurcation / negative-mode theory, but the detector-specific numbers below are model results.

## 2. Rejected continuous sphaleron soft-mode model

The physical branch was tested against an O(2) quartic center-manifold ansatz

\[
B=B_{sph}+\frac{\lambda}{2}(a^2+b^2)+\frac{g}{4}(a^2+b^2)^2+\cdots.
\]

If the physical branch merged continuously into the sphaleron at `T_x`, then

\[
B_{sph}-B_{per}\to0,
\qquad
\sqrt{a^2+b^2}\to0
\]

as `T -> T_x^-`, with finite limiting `g`.

Workflow `experiment03-soft-mode-uniform-landau.yml` falsified these requirements at `.212` and `.213`:

- `B_sph-B_per` remains finite close to `T_x`;
- the periodic first harmonic remains finite;
- `g_eff=lambda^2/[4(B_sph-B_per)]` collapses rather than converging.

Therefore the proposed continuous-crossover factor

\[
\frac12\left[1+\operatorname{erf}\sqrt{B_{sph}-B_{per}}\right]
\]

is **rejected for the physical finite-amplitude branch**.

## 3. First-order action crossing

Workflow:

```text
experiment03-first-order-crossover-branch.yml
run 31924930674
```

continues the same finite-amplitude one-negative periodic saddle above local `T_x`.

Define the leading-exponent crossing by

\[
\boxed{B_{per}(T_c)=B_{sph}(T_c)}.
\]

Results:

| delta | `r_x=T_x/T0` | `r_c=T_c/T0` | `T_c/T_x` |
|---:|---:|---:|---:|
| .212 | 11.6766035 | 12.1820793 | 1.04329 |
| .213 | 11.6482372 | 12.0334859 | 1.03307 |
| .214 | 11.6110848 | 11.8853808 | 1.02362 |
| .215 | 11.5648468 | 11.7373599 | 1.01492 |

At every action crossing the periodic path retains finite amplitude of order `0.1`; this is not a numerically blurred continuous bifurcation.

## 4. Periodic saddle-node/fold is established

The prior checkpoint treated the finite-amplitude fold as a hypothesis. It is now numerically established.

### Pseudo-arclength topology

Workflow:

```text
experiment03-periodic-fold-pseudo.yml
run 31925235420
```

promotes the electrical scale to a continuation unknown and passes through the turning point.

Across the fold:

- the physical periodic branch has one negative even mode;
- an additional even Hessian mode tends to zero;
- after the turn, the companion finite-amplitude periodic branch has two negative even modes;
- the odd translation zero mode is separate and remains the expected collective-coordinate mode.

This is the expected Morse-index exchange for a fold of periodic stationary paths.

### Universal fold scaling

Fine workflow:

```text
experiment03-fold-scaling.yml
```

uses an orthonormal cosine-coordinate Hessian and matched points on the one- and two-negative branches.

Let

\[
\mu=p_f-p,\qquad p=r/r_x.
\]

A saddle-node catastrophe requires

\[
\Delta B_{12}\propto\mu^{3/2},
\qquad
|\lambda_f|\propto\mu^{1/2}.
\]

Measured results:

| delta | `r_f` | action exponent | soft-eigenvalue exponent |
|---:|---:|---:|---:|
| .213 | 12.16227131 | 1.5060 | 0.4859 |
| .214 | 12.0069623 | 1.5022 | 0.4840 |
| .215 | 11.85159085 | 1.5125 | 0.5284 |

The `.213` action-splitting prefactor varies only ~1.4% over the fitted near-fold range; the eigenvalue prefactor varies ~4.6%. Neighboring `.214` is similarly clean.

Thus the finite-amplitude high-tilt singularity is quantitatively in the **fold universality class** within the reduced Euclidean model.

For canonical phase

\[
\Phi(q)=q^3/3-\zeta q,
\]

the stationary-action splitting is

\[
\Delta B=\frac{4}{3}\zeta^{3/2},
\]

so the measured saddle pair defines a natural fold coordinate

\[
\boxed{\zeta=(3\Delta B/4)^{2/3}}.
\]

This does **not** by itself determine the metastable imaginary-part contour or absolute uniform rate.

## 5. Consequence for the Gaussian prefactor

The calibrated regular periodic-instanton rate is

\[
\Gamma_{per}=A_{1\ell}e^{-B_{per}},
\qquad
A_{1\ell}=\omega_c\sqrt{\frac{I_s}{2\pi}}D_{raw,corr}.
\]

As `r -> r_f^-`, the additional stable fold eigenvalue tends to zero. The isolated Gaussian integral over that mode therefore diverges.

This divergence is **not a physical divergent DCR**. It is a nonuniform saddle approximation at coalescing stationary points.

Likewise, simply continuing and adding a higher-action two-negative periodic saddle to the thermal sphaleron after the first-order action crossing is not justified without the correct steepest-descent / thimble structure.

The `.214+` region therefore remains a separate upside branch requiring a fold-uniform or model-specific center-manifold treatment.

## 6. Thermal channel correction

The static thermal action

\[
B_{sph}=\Delta U/(k_BT_0)
\]

is an exponent ceiling, **not an absolute rate ceiling**.

The same-environment generalized memory-friction thermal screen is

\[
\boxed{
\Gamma_{th}
=\frac{\omega_m}{2\pi}\frac{\lambda_b}{\omega_b}
 e^{-\Delta U/(k_BT_0)}
}
\]

with

\[
\boxed{C\lambda_b^2+\lambda_bY_L(\lambda_b)+F_s/L=0}.
\]

Under electrical similarity, the thermal exponent is fixed by the static barrier at fixed bath temperature while dynamical frequencies continue to fall with increasing inertia. Hence electrical scaling can still reduce the thermal rate algebraically.

Any earlier statement that no capacitance can help once `B_sph` reaches the target exponent is too strong and is retired.

## 7. Exact safe-side delta=.213 dark root

The `.213` target is reached before the periodic fold and can therefore be calculated without fold uniformization.

High-basis result:

\[
\boxed{r_\Gamma=11.2051409652}.
\]

```text
C = 26.994365 pF
R = 7.1395800 ohm
fc = 1.8741430 GHz
B_per = 39.114084737
Gamma_per = 9.926942995e-7 /s
Gamma_th  = 7.328188266e-9 /s
Gamma_total = 1.000022488e-6 /s
```

The 72->88 basis change in total rate is only `3.6e-6` of the target.

The correct Gaussian-validity margin is distance to the periodic fold:

\[
\boxed{r_f(.213)=12.16227131}
\]

so

\[
\boxed{r_\Gamma/r_f\approx0.9213}.
\]

The operating root is therefore about 7.9% below the actual fold in electrical scale. The old heuristic rejection criterion based on `T0/Tx~.962` is obsolete.

## 8. Safe-side photon capture has already turned over

All values below are 14-um, 20-ps-rise, 2-ns, N=1024 sym-FDT/TWA screening results at their corresponding reduced dark-rate designs.

Approximate point-estimate `P=.99` area frontier:

```text
delta=.200   A99 ~420 um^2
delta=.205   A99 ~458 um^2
delta=.2075  A99 ~472 um^2
delta=.210   A99 ~485 um^2
delta=.211   A99 ~485 um^2
delta=.212   A99 ~500 um^2
delta=.213   A99 ~489 um^2
```

At `.213` specifically:

```text
A=480 um^2 -> P=0.993164
A=500       -> P=0.986328
A=510       -> P=0.979492
```

Thus the capture screen begins to degrade between `.212` and `.213` **before** the dark fold is approached.

This is an important simplification: the leading reduced-model operating point is an interior photon-dynamics optimum, not a design artificially pinned to the unresolved instanton catastrophe.

Active workflow:

```text
experiment03-safe-tilt-optimum.yml
```

is resolving `.21225`, `.21250`, `.21275`; every point solves its own `Gamma_per+Gamma_th=1e-6/s` dark root before capture.

## 9. Statistical interpretation of current A99 values

The quoted `A99` values are point-estimate crossings from coarse binomial screens, not yet confidence-qualified efficiency boundaries.

For `N=1024`, four failures gives

\[
\hat P=0.99609375
\]

but the 95% Wilson lower bound is only approximately

\[
0.9899994.
\]

Thus a coarse `N=1024` point needs at most three failures for the Wilson lower bound itself to exceed 0.99.

After the narrow optimum is located, the winner must receive a higher-stat focused screen and report at least two quantities separately:

1. point-estimate `A_99`;
2. confidence-qualified maximum area for which the chosen lower confidence bound remains `>=.99`.

## 10. Current claim boundary

Supported within the reduced model:

- finite-T electrical action similarity;
- calibrated regular periodic-instanton determinant and one-loop prefactor away from folds;
- first-order high-tilt periodic-instanton topology;
- distinct local instability, action crossing and periodic-fold scales;
- one-negative -> two-negative Morse-index exchange at the periodic fold;
- canonical `3/2` action-splitting and `1/2` soft-eigenvalue fold scaling across `.213-.215`;
- exact `.213` reduced dark-rate root and its finite margin to the fold;
- a capture turnover between `.212` and `.213` before the fold.

Not supported:

- complete physical DCR;
- exact nonlinear quantum photon efficiency;
- absolute fold-uniform dark rate in `.214+` region;
- broadband optical reach inferred from the lumped thermal similarity;
- final optimized device;
- novelty or manuscript claim.

## 11. Recovery instruction

If resuming here:

1. read `AGENTS.md` and `CURRENT_STATE.md`;
2. read `experiment03-safe-tilt-optimum.yml` run and select the best `.212-.213` point;
3. run a high-stat focused capture refinement at that point's exact dark root;
4. update `CURRENT_STATE.md` and `CLAIM_LEDGER.md`/finite-T ledger extension;
5. keep `.214+` separate until the fold's metastable thimble/uniform rate is derived;
6. after safe reduced optimization, return to the major physics blocker: detailed-balance-preserving nonlinear open-system quantum capture plus realistic spatial thermal/optical physics.
