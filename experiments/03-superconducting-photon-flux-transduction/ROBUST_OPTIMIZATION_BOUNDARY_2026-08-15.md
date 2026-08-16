# Experiment 03 — Robust-Optimization Boundary

**Date:** 2026-08-15  
**Status:** methodological guardrail; no new detector claim

## 1. Numerical optimum precision is not physical optimum precision

The reduced simulator is now resolving the safe-side capture turnover on tilt increments of order

```text
Delta delta = 2.5e-4.
```

That numerical exercise is useful for determining whether an interior maximum exists and for testing stochastic convergence. It is **not** evidence that a real detector can be specified or optimized to `delta=.21250` rather than `.21225`.

The retained physical model still contains materially larger uncertainties / idealizations, including:

- `BETA_COLD` / CPR amplitude and shape;
- empirical interface-mixing parameter `LAMBDA_MIX`;
- induced-gap / junction-model uncertainty;
- lumped electron heat capacity and cooling law;
- photon absorption efficiency and spatial energy deposition;
- exact two-pole bath realization / parasitics;
- missing competing dark channels;
- sym-FDT TWA rather than exact nonlinear quantum capture.

Therefore the sub-`1e-3` tilt scan must be interpreted as a **reduced-model localization of the turnover**, not fabrication-level parameter metrology.

## 2. Correct robust design problem

Let `theta` denote uncertain physical/model parameters and let `Gamma_star` be the chosen dark-rate target.

A robust max-min formulation is

\[
\boxed{
\max_{\delta,r}
\ \min_{\theta\in\Theta}
A_{99}(\delta,r;\theta)
}
\]

subject to

\[
\boxed{
\Gamma_{dark}(T_0;\delta,r;\theta)\le\Gamma_\star
\quad\forall\theta\in\Theta.
}
\]

A probabilistic alternative is a chance-constrained formulation such as

\[
P_\theta[\Gamma_{dark}\le\Gamma_\star]\ge1-\epsilon_d,
\]

\[
P_\theta[P_{cap}\ge.99]\ge1-\epsilon_c.
\]

No prior should be invented merely to obtain a number; theoretical/literature uncertainty ranges must be documented parameter by parameter.

## 3. What the current strict paired scan can legitimately establish

The high-stat / common-random comparison across `.212-.213` can establish:

1. whether the turnover persists after eliminating avoidable Monte Carlo ranking noise;
2. whether the reduced-model optimum is broad or sharply localized;
3. a sensible central point for the next exact-quantum benchmark.

It cannot establish:

- that a physical device should be fabricated at the winning fifth decimal;
- that the same tilt wins after CPR/thermal/optical model perturbations;
- that the quoted `A99` is a physical quantum efficiency boundary.

The correct final language should therefore be approximately

```text
reduced-model optimum neighborhood / robust band
```

unless a subsequent uncertainty analysis demonstrates otherwise.

## 4. Minimum uncertainty axes for the next robust screen

After the safe reduced-model turnover is statistically confirmed, perturb at least:

### Static / Josephson topology

- `BETA_COLD`;
- `LAMBDA_MIX`;
- induced-gap scale / `rDelta` family;
- loop inductance `L` / external-flux calibration.

### Thermal pulse

- heat-capacity coefficient;
- absorption efficiency;
- rise time;
- cooling coefficient / effective thermal dwell;
- spatial thermalization correction.

### Passive environment

- `alpha=omega_D/omega_c`;
- realized `R,C,L_f,C_f` tolerances;
- dielectric loss / parasitic admittance;
- bath temperature.

### Dark physics

- one-loop semiclassical correction scale;
- quasiparticle / vortex / stray-photon channels;
- quasi-static flux bias noise.

### Capture physics

- exact detailed-balance-preserving quantum evolution versus sym-FDT TWA;
- Hilbert/bath truncation.

## 5. Design decision rule

If a narrow point optimum moves substantially under physically modest perturbations, report a **Pareto/robust band**, not a single optimized tilt.

If a broader neighborhood remains dominant under all justified perturbations, choose the point within that neighborhood that maximizes engineering margin (distance from periodic fold, component tolerances, lower capacitance, easier biasing) rather than the nominal central `A99` by a fraction of a percent.

This is particularly relevant here because lower tilt generally reduces required electrical inertia and increases distance from the finite-amplitude instanton fold. A statistically indistinguishable lower-tilt design may therefore be the stronger engineering choice even if its nominal reduced-model `A99` is microscopically smaller.

## 6. Immediate consequence

The current strict common-random-number calculation should be used to identify the **shape and breadth** of the `.212-.213` optimum. Once that is established, stop refining `delta` numerically unless the spread is large enough to survive the dominant physical-model uncertainties.
