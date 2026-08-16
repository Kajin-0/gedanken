# Experiment 03 — Finite-T / Fold Derivation Continuation — 2026-08-15

This file continues the dynamic/open-system derivation trail into the finite-temperature dissipative-instanton and high-tilt optimization stage. `CURRENT_STATE.md` remains the compact live state; `FIRST_ORDER_CROSSOVER_CHECKPOINT_2026-08-15.md` is the detailed crossover checkpoint.

## Step 57 — exact barrier shape invalidates cubic MQT surrogate

The live low-tilt barrier is not adequately represented by the standard cubic metastable potential. For the retained `.8/.05` neighborhood the exact isolated zero-energy bounce gives

\[
B_{iso}=25.033050,
\]

whereas the old cubic surrogate gave approximately `38`.

The same-environment two-pole dissipative bounce gives

\[
B_{diss}=29.765636.
\]

Thus the original `C=215 fF, R=80 ohm` point is not dark-stable under the actual barrier shape. The apparent prior dark closure was a shape-model artifact.

## Step 58 — exact electrical dark-action similarity

At fixed static potential, loop inductance, and normalized passive bath topology, apply

\[
C\to r^2C,\qquad R\to R/r,\qquad \omega_D\to\omega_D/r.
\]

Then

\[
\omega_c\to\omega_c/r,
\]

while the normalized real-time damping topology is unchanged.

At zero temperature the full nonlocal Euclidean action scales exactly:

\[
\boxed{B\to rB}.
\]

At finite temperature the period rescales as well, giving the stronger identity

\[
\boxed{B(T;r)=rB_0(rT)}.
\]

This was numerically verified on the full finite-period nonlocal saddle to machine precision.

The finite-T periodic one-loop prefactor away from bifurcation singularities obeys

\[
\boxed{A_{1\ell}(T;r)=r^{-1/2}A_{1\ell,0}(rT)}.
\]

The same transformation therefore supplies an exact reduced map of dark action, phase speed and bath frequencies along the electrical rescue family.

## Step 59 — high tilt plus electrical compensation dominates low tilt and barrier shaping

Low tilt increases the dark action but weakens one-sided basin bias so strongly that photon capture degrades. Mild `beta` barrier shaping buys action but raises the photon fold and loses calorimetric headroom.

The opposite direction performs better:

```text
increase positive directional tilt
then increase C / reduce R by exact electrical similarity
until the dark constraint is restored.
```

Higher tilt lowers the photon-trigger fold and strengthens directionality; electrical compensation restores dark suppression but slows the phase coordinate.

This transforms the design problem into a controlled sensitivity-versus-write-speed Pareto line rather than separate ad hoc rescue branches.

## Step 60 — finite-period dissipative escape replaces zero-T action as dark constraint

At `T0=20 mK`, the correct same-environment Euclidean saddle has physical Matsubara period

\[
P_s=\hbar\omega_c/(k_BT_0).
\]

The solver retains the constant mode plus cosine harmonics and the exact positive-real two-pole kernel.

The static sphaleron action is recovered exactly as

\[
B_{sph}=\Delta U/(k_BT).
\]

The physical periodic decay saddle has one negative even mode and an odd translation zero mode.

Finite temperature reduces the exponent before the thermal crossover, so holding a fixed zero-T action does not hold the actual dark rate fixed.

## Step 61 — UV-converged determinant and cubic absolute normalization

The periodic Hessian determinant initially converged only as `O(1/N)` because the leading high-Matsubara difference is the time-averaged curvature shift.

An analytic high-frequency curvature-tail sum removes this term. In hard cases the corrected `N=80->96` change in `log D` falls to a few `1e-6`.

Because the Hessians are Hessians of dimensionless action `B=S/hbar`, removal of the translation zero mode leaves one unmatched `sqrt(A_k)` factor. The physical operator determinant is

\[
\boxed{D_{op}=D_{raw}/\sqrt{A_k}}.
\]

This was calibrated against the canonical cubic metastable bounce:

\[
D_{op}^{exact}=\sqrt{60}=7.74596669,
\]

numerical

\[
D_{op}^{num}=7.74565249,
\]

relative error about `4.1e-5`.

The calibrated periodic one-loop prefactor is therefore

\[
\boxed{A_{1\ell}=\omega_c\sqrt{I_s/(2\pi)}D_{raw,corr}},
\]

and

\[
\boxed{\Gamma_{per}=A_{1\ell}e^{-B_{per}}}.
\]

The dark design problem no longer uses an arbitrary GHz attempt frequency.

## Step 62 — local sphaleron instability is not the physical crossover

The first nonzero Matsubara eigenvalue of the sphaleron changes sign at local `T_x`. A continuous O(2) quartic center-manifold hypothesis would imply the physical periodic branch shrinks into the sphaleron there.

Direct tests rejected this:

- periodic amplitude remains finite as `T->T_x^-`;
- `B_sph-B_per` remains finite;
- inferred quartic coefficient fails to approach a finite constant.

Therefore the earlier simple error-function uniformization about the sphaleron is invalid for the relevant high-tilt branch.

## Step 63 — direct continuation reveals a first-order action crossing

The same finite-amplitude one-negative periodic saddle was continued through and above local `T_x`.

The leading-exponent quantum/thermal crossing occurs where

\[
B_{per}(T_c)=B_{sph}(T_c),
\]

not where the sphaleron first becomes locally unstable.

Representative electrical scales:

```text
delta=.212: r_x=11.67660, r_c=12.18208
delta=.213: r_x=11.64824, r_c=12.03349
delta=.214: r_x=11.61108, r_c=11.88538
delta=.215: r_x=11.56485, r_c=11.73736.
```

The periodic path remains finite-amplitude at every action crossing.

## Step 64 — the finite-amplitude periodic branch ends in a genuine fold catastrophe

Direct continuation in `r` eventually fails because the physical one-negative periodic saddle does not simply disappear numerically. Pseudo-arclength continuation passes through a turning point and recovers a companion finite-amplitude periodic stationary branch with two negative even modes.

The additional even mode crosses zero at the turning point. This is separate from the odd translation zero mode.

Fine orthonormal-Hessian regressions yield:

### delta=.213

\[
r_f=12.16227131,
\]

\[
\Delta B_{12}\propto\mu^{1.5060},
\qquad
|\lambda_f|\propto\mu^{0.4859}.
\]

### delta=.214

\[
r_f=12.0069623,
\]

\[
\Delta B_{12}\propto\mu^{1.5022},
\qquad
|\lambda_f|\propto\mu^{0.4840}.
\]

### delta=.215

\[
r_f=11.85159085,
\]

\[
\Delta B_{12}\propto\mu^{1.5125},
\qquad
|\lambda_f|\propto\mu^{0.5284}.
\]

where

\[
\mu=p_f-p,\qquad p=r/r_x.
\]

These reproduce the canonical saddle-node exponents `3/2` and `1/2`.

Therefore the blow-up of the isolated Gaussian determinant near `r_f` is a **catastrophe-uniformization problem**, not a physical divergent DCR.

## Step 65 — thermal action is not an absolute rate ceiling

The static exponent is

\[
B_{sph}=\Delta U/(k_BT_0).
\]

However the same-environment classical memory-friction rate is

\[
\Gamma_{th}
=\frac{\omega_m}{2\pi}\frac{\lambda_b}{\omega_b}
 e^{-\Delta U/(k_BT_0)},
\]

with

\[
C\lambda_b^2+\lambda_bY_L(\lambda_b)+F_s/L=0.
\]

Electrical inertia can therefore continue reducing the thermal **prefactor** even when the exponent itself no longer increases.

The prior interpretation of `DeltaU/kBT` as an absolute no-compensation rate ceiling is rejected.

## Step 66 — exact `.213` reduced dark root is below the actual fold

Solving

\[
\Gamma_{per}(r)+\Gamma_{th}(r)=10^{-6}\ \mathrm{s}^{-1}
\]

on the regular one-negative periodic branch gives

\[
\boxed{r_\Gamma(.213)=11.2051409652}.
\]

At this point:

```text
C = 26.994365 pF
R = 7.1395800 ohm
fc = 1.8741430 GHz
B_per = 39.114084737
Gamma_per = 9.926942995e-7 /s
Gamma_th  = 7.328188266e-9 /s
Gamma_total = 1.000022488e-6 /s.
```

The 72->88 basis change moves the total rate by only `3.6e-6` of the target.

The actual periodic fold is

\[
r_f(.213)=12.16227131,
\]

so

\[
\boxed{r_\Gamma/r_f\approx0.9213}.
\]

The design root is about 7.9% below the Gaussian catastrophe. The old `T0/T_x>.94` safety rule is therefore retired.

## Step 67 — safe-side photon-capture frontier turns over before the fold

On the same reduced dark target, 14-um / 20-ps / 2-ns / N=1024 screens give approximate point-estimate `P=.99` crossings

```text
delta=.200   A99 ~420 um^2
delta=.205   A99 ~458 um^2
delta=.2075  A99 ~472 um^2
delta=.210   A99 ~485 um^2
delta=.211   A99 ~485 um^2
delta=.212   A99 ~500 um^2
delta=.213   A99 ~489 um^2.
```

The important conclusion is not the exact coarse area. It is that the capture metric begins falling before the instanton fold is encountered.

Therefore a safe interior optimum exists and can be selected without solving the `.214+` fold-uniform absolute rate.

## Step 68 — physical decomposition of the `.212 -> .213` turnover

At `.212`:

```text
Tf = 0.278530 K
C  = 24.2567 pF
fc = 1.98465 GHz
point-estimate A99 ~500.4 um^2.
```

At `.213`:

```text
Tf = 0.275732 K
C  = 26.9944 pF
fc = 1.87414 GHz
point-estimate A99 ~489.3 um^2.
```

The static threshold factor

\[
T_f^2-T_0^2
\]

falls by about 2.0%, which alone would improve the allowable area by about 2.0%.

Instead the measured point-estimate `A99` falls by about 2.2%.

Define the fold-normalized dynamic factor

\[
Q_{99}=A_{99}(T_f^2-T_0^2).
\]

It changes approximately

```text
Q99(.212) ~38.62
Q99(.213) ~37.00,
```

a deterioration of about 4.2%.

Hence the turnover is a real **static-threshold versus inertial-write-speed** competition: the increasingly large capacitance required by the dark-rate constraint is now degrading basin selection faster than the lower photon fold helps.

## Step 69 — statistical criterion for final A99

The current `N=1024` scans locate the design neighborhood but are not sufficient for a confidence-qualified `P>=.99` boundary.

For `N=1024`, four observed failures gives

\[
\hat P=0.99609375
\]

but a 95% Wilson lower bound of only about

\[
0.9899994.
\]

Therefore the final optimized point must distinguish:

```text
A99_point      interpolation / estimate where central P crosses .99
A99_95lower    largest area whose selected 95% lower confidence bound is >=.99.
```

A coarse N=1024 point can tolerate at most three failures for the Wilson lower bound itself to exceed .99.

## Current active computation after Step 69

Workflow

```text
experiment03-safe-tilt-optimum.yml
```

solves the exact reduced dark root and matched 2-ns capture grid at

```text
delta=.21225, .21250, .21275.
```

This should bracket the interior safe-side maximum.

Once the best tilt is found:

1. rerun it at higher capture statistics (`N>=4096`) around its `P=.99` boundary;
2. report both point and confidence-qualified areas;
3. update `CURRENT_STATE.md` and the claim ledgers;
4. then move to the larger unresolved physics: detailed-balance-preserving nonlinear quantum/open-system capture, spatial thermalization, realistic optical absorption, and missing dark channels.

The `.214+` fold branch is scientifically interesting but is not required to select the current safe reduced-model optimum. Its absolute dark rate remains **NO-CLAIM** until a thimble-aware fold-uniform contribution is derived.
