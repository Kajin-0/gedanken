# Experiment 03 — Interior Safe-Optimum Balance Condition

**Date:** 2026-08-15  
**Status:** exact within the reduced lumped thermal similarity; dynamical factor remains model-dependent

## 1. Why the safe optimum is analytically meaningful

The dark-rate-constrained capture screen rises with directional tilt through roughly `delta=.212` and then falls by `.213`. The turnover occurs before the finite-temperature periodic-instanton fold, so it is not a dark-topology boundary artifact.

The reduced thermal similarity makes the balance condition transparent.

For `C_e=gamma A T`, fixed photon energy, fixed absorption efficiency and fixed normalized pulse/cooling law,

\[
T_{ad}^2-T_0^2\propto\frac{1}{A\lambda}.
\]

Define the probability-`p` dynamical headroom relative to the static photon-trigger fold,

\[
\boxed{
\chi_p(\delta)
=\frac{T_{ad,p}^2-T_0^2}
       {T_f^2(\delta)-T_0^2}.
}
\]

At fixed wavelength and absorption model,

\[
\boxed{
A_p(\delta)
=\frac{K}
 {\chi_p(\delta)\,[T_f^2(\delta)-T_0^2]},
}
\]

where `K` is independent of `delta` for the present thermal model.

The important point is that `chi_p` is evaluated **after** every tilt has been electrically rescaled onto the same dark-rate manifold

\[
\Gamma_{dark}(T_0;\delta,r(\delta))=\Gamma_\star.
\]

Thus `chi_p` includes the complete dynamical consequences of directional bias, capacitance, damping, phase speed, stochastic basin selection, etc., within the retained capture model.

## 2. Exact first-order condition for an interior maximum

Take the total derivative along the fixed-dark-rate manifold:

\[
\frac{d\ln A_p}{d\delta}
=-\frac{d\ln\chi_p}{d\delta}
-\frac{d}{d\delta}\ln[T_f^2-T_0^2].
\]

At a smooth interior optimum `delta_opt`,

\[
\boxed{
\left.\frac{d\ln\chi_p}{d\delta}\right|_{opt}
=
-\left.\frac{d}{d\delta}
\ln[T_f^2-T_0^2]\right|_{opt}.
}
\]

This is the exact reduced-model statement of the observed design competition:

```text
marginal dynamical/write-speed penalty
=
marginal static fold-threshold benefit.
```

If the left side is smaller, increasing tilt still improves `A_p`. If it is larger, the electrical/inertial penalty has overtaken the static sensitivity gain.

## 3. Dark-manifold contribution to phase slowing

Let

\[
F(\delta,r)
=\ln\Gamma_{dark}(\delta,r)-\ln\Gamma_\star=0.
\]

Where the regular dark rate is smooth,

\[
\boxed{
\frac{dr}{d\delta}
=-\frac{F_\delta}{F_r}.
}
\]

The electrically compensated cold phase frequency is

\[
\omega_c(\delta,r)
=\frac{\omega_{c0}(\delta)}{r}.
\]

For fixed physical optical rise time,

\[
\rho=\omega_c\tau_{rise},
\]

so

\[
\boxed{
\frac{d\ln\rho}{d\delta}
=
\frac{d\ln\omega_{c0}}{d\delta}
-
\frac{d\ln r}{d\delta}.
}
\]

The second term is the direct speed cost of restoring the dark rate as static tilt lowers the barrier.

`chi_p` is not assumed to be a function of `rho` alone: tilt also changes directional basin topology. However, if a local neighborhood is empirically well described by `chi_p=chi_p(rho)`, then the optimum condition becomes

\[
\boxed{
-\frac{d\ln\chi_p}{d\ln\rho}
=
\frac{-d\ln(T_f^2-T_0^2)/d\delta}
     {-d\ln\rho/d\delta}.
}
\]

This form gives a dimensionless local elasticity criterion for the speed-versus-threshold trade.

## 4. Current `.212 -> .213` diagnostic

Using the present coarse point-estimate screens:

```text
delta=.212:
    Tf ~ 0.278530 K
    fc ~ 1.98465 GHz
    A99_point ~ 500 um^2

delta=.213:
    Tf ~ 0.275732 K
    fc ~ 1.87414 GHz
    A99_point ~ 489 um^2
```

The static fold factor `Tf^2-T0^2` improves by about 2% as tilt rises, but `A99` falls. Hence the total dynamical headroom factor is already worsening faster than the static threshold is improving over this interval.

The harmonic cold phase width simultaneously narrows slightly with increasing capacitance, so the turnover cannot be attributed to a broader initial zero-point cloud. It is a finite-pulse dynamical/basin-selection penalty.

The exact location of the maximum is still being resolved with a strict paired common-random-number calculation. The analytical balance condition above does not depend on that statistical refinement.

## 5. Scope

This balance equation is exact only within the retained lumped thermal similarity and whatever capture dynamics define `chi_p`. It is not yet a theorem about a real device because realistic wavelength-dependent absorption, spatial thermalization, and exact nonlinear open-system quantum dynamics remain absent.

Its value is architectural: it explains why more directional tilt cannot provide unlimited photon sensitivity at fixed dark rate even before the Euclidean fold is reached.
