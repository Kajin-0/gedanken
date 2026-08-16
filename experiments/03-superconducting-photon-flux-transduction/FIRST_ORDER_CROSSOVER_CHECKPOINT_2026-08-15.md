# Experiment 03 — First-Order Quantum/Thermal Crossover Checkpoint

**Date:** 2026-08-15 / late-session continuation  
**Status:** canonical correction; publication remains **NO-GO**

## 1. Why this checkpoint exists

The finite-temperature dissipative instanton program originally identified the
temperature where the sphaleron's first nonzero Matsubara eigenvalue vanishes,

\[
\Lambda_1(T_\times)=0,
\]

with the physical quantum-to-thermal crossover.  That identification has now
been falsified in the high-directional-tilt region relevant to the current
photon-capture optimum.

The actual reduced model exhibits a **first-order-like escape crossover**: a
finite-amplitude one-negative-mode periodic instanton survives through and
above the local sphaleron instability.  The leading exponential crossover is
instead determined by the intersection of the periodic and static Euclidean
actions.

This is consistent with the classic metastable-decay literature in which a
first-order quantum/classical crossover is identified from the crossing of the
low-temperature periodic-instanton action and high-temperature sphaleron action,
not from a perturbative instability of the sphaleron alone.

## 2. Rejected second-order soft-mode model

A direct test was made of the O(2) quartic center-manifold normal form

\[
B=B_{sph}+\frac{\lambda}{2}(a^2+b^2)+\frac{g}{4}(a^2+b^2)^2+\cdots.
\]

If the physical periodic branch merged continuously into the sphaleron at
`T_x`, then as `T -> T_x^-` one would require

\[
B_{sph}-B_{per}\to0,
\qquad
\sqrt{a^2+b^2}\to0,
\]

with finite limiting `g`.

Workflow:

```text
experiment03-soft-mode-uniform-landau.yml
```

falsified all three expectations at `delta=.212` and `.213`:

- `B_sph-B_per` remains finite near `.996 T_x`;
- the first harmonic remains finite;
- `g_eff=lambda^2/[4(B_sph-B_per)]` collapses instead of converging.

Therefore the proposed continuous-crossover correction

\[
\frac12\left[1+\operatorname{erf}\sqrt{B_{sph}-B_{per}}\right]
\]

is **rejected** for the relevant physical periodic branch.

Do not resurrect this formula without a new branch-topology argument.

## 3. Direct continuation proves a first-order action crossing

Workflow:

```text
experiment03-first-order-crossover-branch.yml
run 31924930674
```

continues the same finite-amplitude, one-negative-mode periodic instanton above
`T_x` rather than hard-switching to the sphaleron.

The physical leading-exponent crossover is defined by

\[
\boxed{B_{per}(T_c)=B_{sph}(T_c)}.
\]

Results:

| delta | local `r_x=T_x/T0` | action-crossing `r_c=T_c/T0` | `T_c/T_x` |
|---:|---:|---:|---:|
| .212 | 11.6766035 | 12.1820793 | 1.04329 |
| .213 | 11.6482372 | 12.0334859 | 1.03307 |
| .214 | 11.6110848 | 11.8853808 | 1.02362 |
| .215 | 11.5648468 | 11.7373599 | 1.01492 |

At every crossing the periodic path retains finite amplitude of order `0.10` in
the normalized L2 measure.  This is not a nearly continuous bifurcation hidden
by discretization.

The finite-amplitude branch subsequently terminates/folds slightly above the
action crossing.  Near that fold direct continuation in `r` fails and an
additional even Hessian mode approaches zero.

## 4. Important distinction among three scales

Future work must distinguish:

1. **Local sphaleron instability** `T_x` / `r_x`:
   first nonzero Matsubara sphaleron eigenvalue crosses zero.
2. **First-order action crossing** `T_c` / `r_c`:
   `B_per=B_sph`; this determines the dominant exponential in the usual
   semiclassical first-order classification.
3. **Finite-amplitude periodic-branch fold** `T_fold` / `r_fold`:
   the physical one-negative periodic branch coalesces with another periodic
   stationary branch and ordinary Gaussian determinants become singular.

They are not interchangeable.

## 5. Branch-aware absolute-rate screen

The calibrated periodic-instanton one-loop rate is

\[
\Gamma_{per}=A_{1\ell}e^{-B_{per}},
\qquad
A_{1\ell}=\omega_c\sqrt{\frac{I_s}{2\pi}}D_{raw,corr}.
\]

The independent thermal memory-friction screen is

\[
\Gamma_{th}
=\frac{\omega_m}{2\pi}\frac{\lambda_b}{\omega_b}
 e^{-\Delta U/(k_BT_0)},
\]

with

\[
C\lambda_b^2+\lambda_bY_L(\lambda_b)+F_s/L=0.
\]

Workflow:

```text
experiment03-first-order-total-rate.yml
run 31925043718
```

shows the following qualitative split.

### delta=.213 — crossover-independent target

The first descending `1e-6 /s` crossing occurs at approximately

\[
\boxed{r_{target}\simeq11.206},
\]

well below both

```text
r_x = 11.648
r_c = 12.034.
```

The thermal rate there is only of order `7e-9 /s`.  Therefore `.213` can be
screened without any first-order-crossover uniformization.

### delta=.214 and above — fold-controlled absolute rate

For `.214` the regular periodic Gaussian rate reaches a minimum of only about
`1.7e-6 /s`, then rises as the finite-amplitude periodic branch approaches its
fold.  The independent thermal rate is already only about `2e-8 /s`.

At still larger tilts this separation becomes stronger.  Examples near the
first-order region:

```text
delta=.215: thermal ~ 8e-8 /s, periodic Gaussian ~ several e-6 /s
delta=.216: thermal ~ 2.5e-7 /s, periodic Gaussian ~ 2e-5 /s
delta=.217: thermal ~ 8e-7 /s, periodic Gaussian ~ 1e-4 /s
delta=.218: thermal ~ 2.5e-6 /s, periodic Gaussian ~ 2e-4 /s
```

The large periodic prefactor close to the fold must **not** be interpreted as a
physical divergent dark rate.  Gaussian steepest descent is failing because an
additional fluctuation eigenvalue is approaching zero.

Likewise, blindly adding the continued periodic Gaussian saddle to the thermal
saddle after the first-order action crossing is not yet justified: saddle
selection / steepest-descent contour topology changes in a first-order
transition.

## 6. Current mathematical task at the high-tilt boundary

A periodic-instanton bifurcation should possess an additional zero mode beyond
time translation.  The current hypothesis is that the finite-amplitude physical
periodic saddle undergoes a saddle-node/fold collision with a companion periodic
stationary solution carrying one additional negative mode.

Active workflow:

```text
experiment03-periodic-fold-pseudo.yml
```

uses pseudo-arclength continuation in cosine-coefficient space plus electrical
scale `r/r_x` to pass through the fold.

Acceptance requires:

- turning point in `r`;
- an additional even Hessian eigenvalue approaching zero;
- recovery of a companion finite-amplitude periodic branch;
- negative-mode count changing from one to two.

If confirmed, the local coalescing-saddle contribution should be treated with a
fold/Airy uniform approximation rather than two independent Gaussian
prefactors.

## 7. Current capture frontier

On dark-rate-constrained, crossover-independent designs, the 14-um, 2-ns,
N=1024 sym-FDT/TWA screen currently gives approximately

```text
delta=.200   A99 ~420 um^2
delta=.205   A99 ~458 um^2
delta=.2075  A99 ~472 um^2
delta=.210   A99 ~485 um^2
delta=.211   A99 ~485 um^2
delta=.212   A99 ~500 um^2
```

A dedicated `.213` screen is active at the branch-aware target locator
`r~=11.20596`.  If it exceeds the `.212` frontier, `.213` becomes the strongest
**crossover-independent** reduced-model candidate.

Do not optimize photon capture at `.214+` until the periodic fold contribution
has been uniformized or otherwise rigorously bounded.

## 8. Claim boundary

The following are now supported **within the reduced model**:

- the high-tilt finite-T escape topology is first-order-like rather than the
  previously assumed continuous sphaleron bifurcation;
- `T_x`, `T_c`, and the periodic-branch fold are distinct scales;
- `.213` reaches the provisional absolute dark target before entering the
  first-order crossover region;
- `.214+` cannot be ranked by the current separate Gaussian periodic and thermal
  prefactors.

Still not supported:

- a complete physical dark-count rate;
- exact quantum photon efficiency;
- a final optimized device;
- any novelty or manuscript claim.

## 9. Recovery instruction

If resuming from this file:

1. read the `experiment03-periodic-fold-pseudo.yml` logs;
2. read the `.213` capture workflow;
3. if the fold topology is confirmed, derive/validate the coalescing-saddle
   uniform contribution before ranking `.214+`;
4. keep `.213` as the safe optimization frontier until that is done;
5. update `CURRENT_STATE.md`, `agent.md`, the claim ledger and derivation log.
