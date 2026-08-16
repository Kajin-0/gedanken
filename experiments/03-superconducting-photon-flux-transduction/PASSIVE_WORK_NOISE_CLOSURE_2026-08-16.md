# Experiment 03 — Passive Work / Noise Closure — 2026-08-16

## Purpose

Close the outstanding same-environment consistency check between:

1. the spectral dissipated work computed from the positive-real admittance used throughout Experiment 03;
2. the explicit Joule loss in the resistor of the two-pole state-space realization; and
3. the symmetrized fluctuation-dissipation work variance for the same prescribed capture trajectory.

This is a **linear-bath, prescribed-trajectory consistency test**. It is not an exact nonlinear capture-error probability.

## Identity under test

For phase-node voltage

```math
V(t)=\bar\Phi\,\dot x(t),
```

with

```math
\operatorname{Re}Y(\omega)=\frac{1/R}{1+(\omega/\omega_D)^4},
```

the spectral dissipated work is

```math
E_{\rm diss}
=\int\frac{d\omega}{2\pi}
\operatorname{Re}Y(\omega)|V(\omega)|^2.
```

The explicit resistor realization gives

```math
E_R=\int dt\,\frac{V_R(t)^2}{R}.
```

For the project's symmetrized quantum-FDT convention,

```math
\langle W_n^2\rangle_{\rm sym}
=\int\frac{d\omega}{2\pi}
\hbar|\omega|\coth\!\left(\frac{\hbar|\omega|}{2k_BT}\right)
\operatorname{Re}Y(\omega)|V(\omega)|^2.
```

Therefore

```math
\epsilon_{\rm eff}
\equiv
\frac{\langle W_n^2\rangle_{\rm sym}}{E_{\rm diss}}
\ge 2k_BT.
```

## Historical regression failure and repair

The first two workflow generations compared independently propagated 4-ns and 6-ns trajectories. They failed an imposed `<2%` 4→6 ns energy-tail criterion even though the 6-ns spectral-vs-resistor mismatch was already sub-percent.

For example, at `delta=.2125`:

```text
6 ns spectral/resistor mismatch = 3.997e-3
4->6 ns dissipated-energy tail  = 6.457e-2
```

and at `delta=.213`:

```text
6 ns spectral/resistor mismatch = 2.407e-3
4->6 ns dissipated-energy tail  = 7.829e-2
```

Thus the failure was insufficient horizon, not a violation of passivity or FDT.

The repaired calculation propagates each deterministic four-state trajectory once to 10 ns and evaluates nested 4, 6, 8 and 10 ns prefixes. The acceptance gates are:

```text
8->10 ns dissipated-energy tail < 2%
|E_diss-E_R|/E_R              < 2%
epsilon_eff/(2 k_B T0)        >= 1
```

## Validation workflow

```text
workflow: .github/workflows/experiment03-passive-work-noise.yml
run:      31972863217
head:     b6ef9daa6e066c23c21d59f515c42456679507b5
status:   SUCCESS
matrix:   delta=.21200,.21250,.21300
area:     500 um^2
lambda:   14 um
T0:       20 mK
```

All three jobs passed.

## 10-ns results

| delta | `E_diss/k_B` (K) | `sigma_W/k_B` (K) | `epsilon_eff/k_B` (K) | `epsilon_eff/(2k_BT0)` | diss.-weighted `f` (GHz) | 8→10 ns tail | spectral/resistor mismatch |
|---:|---:|---:|---:|---:|---:|---:|---:|
| .21200 | 22.0386825 | 1.6461479 | 0.1229567 | 3.07392 | 2.47180 | 8.413e-3 | 1.182e-3 |
| .21250 | 22.0694727 | 1.6285330 | 0.1201714 | 3.00429 | 2.40918 | 7.539e-3 | 1.105e-3 |
| .21300 | 22.0690705 | 1.6082881 | 0.1172043 | 2.93011 | 2.34667 | 1.156e-2 | 4.484e-4 |

At the engineering representative `.212`, the final filter energy is only

```text
E_filter(10 ns)/k_B = 2.555e-3 K,
```

and the spectral/time-domain energy mismatch is about `0.118%`.

At `.213`, the mismatch is only `0.0448%`.

## Physical interpretation

The result confirms two independent facts.

### 1. Same-environment realization is energetically consistent

The frequency-domain positive-real admittance and the explicit two-pole resistor network compute the same dissipated energy to approximately `10^-3` fractional accuracy on the converged trajectory.

The earlier CI failure therefore did **not** expose an inconsistency between the Euclidean/capture admittance and the state-space circuit realization.

### 2. Passive damping is not fluctuation-free

Across the safe plateau,

```text
epsilon_eff/(2 k_B T0) = 2.93 ... 3.07.
```

Hence the actual trajectory-weighted symmetrized work variance is about three times the universal classical FDT floor in energy-per-dissipated-work units. The excess is expected because the relevant dissipative spectral weight is centered near `2.35-2.47 GHz`, where zero-point fluctuations are substantial at `T0=20 mK`.

This supports the conceptual statement:

> eliminating ordinary transport-resistor Johnson noise from a superconducting storage path does not produce a fluctuation-free passive detector. Any passive environment strong enough to provide capture/recovery damping carries the corresponding FDT fluctuations.

## Claim boundary

This closure does **not** compute:

- exact nonlinear quantum capture probability;
- the probability that bath work itself changes the final basin;
- a complete detector noise-equivalent power or dark-count rate;
- readout noise;
- non-equilibrium quasiparticle or technical noise.

It validates only the passive linear-bath energy/noise identity on the deterministic capture trajectory.

## Disposition

```text
PASSIVE WORK/NOISE CONSISTENCY: CLOSED / PASS
```

The next quantum step should therefore preserve this same reaction-coordinate/bath realization and replace the symmetrized truncated-Wigner capture screen with a detailed-balance-preserving nonlinear open-system benchmark rather than inventing a different damping model.
