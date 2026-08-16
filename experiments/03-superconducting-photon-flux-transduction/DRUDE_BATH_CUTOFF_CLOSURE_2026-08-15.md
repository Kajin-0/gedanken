# Experiment 03 — Causal Drude-Bath Cutoff Closure — 2026-08-15

## Why this checkpoint exists

The scalar-resistance RCSJ model was useful for deterministic basin discovery, but it is not a physically complete quantum environment. A strictly infinite-bandwidth Ohmic bath gives a convergent phase-coordinate variance but a logarithmically divergent velocity/momentum variance. The next minimal bath therefore needs a finite ultraviolet rolloff.

Use the one-pole causal admittance

```math
Y(\omega)=\frac{G_0}{1-i\omega/\omega_D},
\qquad
\operatorname{Re}Y(\omega)
=\frac{G_0}{1+(\omega/\omega_D)^2}.
```

With the `exp(-i omega t)` convention, this is equivalent to the auxiliary-current dynamics

```math
LC\ddot x+Lj+F(x,T)=0,
```

```math
\tau_D\dot j+j=G_0\dot x,
\qquad
\tau_D=\omega_D^{-1}.
```

This is the smallest causal colored environment currently retained for Experiment 03.

## Quantum fluctuation-dissipation requirement

The same admittance must set the symmetrized current-noise spectrum,

```math
S_I^{sym}(\omega)
=\hbar|\omega|
\coth\!\left(\frac{\hbar|\omega|}{2k_BT}\right)
\operatorname{Re}Y(\omega).
```

No independent noiseless damping knob is allowed.

The current phase frequencies are roughly `27–32 GHz`, so `h f_c / k_B ~1.3–1.5 K`. The hot/fold temperatures are only about `0.6–0.8 K`. Therefore the bath is not safely in a classical white-Johnson regime over the phase dynamics.

## Exact damping-retention rule

Define

```math
\eta_c
\equiv
\frac{\operatorname{Re}Y(\omega_c)}{G_0}
=\frac{1}{1+(\omega_c/\omega_D)^2}.
```

Solving for the cutoff gives

```math
\boxed{
\frac{\omega_D}{\omega_c}
\ge
\sqrt{\frac{\eta_c}{1-\eta_c}}
}.
```

Examples:

```text
eta_c = 0.80 -> omega_D/omega_c >= 2.00
eta_c = 0.95 -> >= 4.36
eta_c = 0.99 -> >= 9.95.
```

For the current `27–32 GHz` phase-frequency scale, retaining 95–99% of the scalar-R damping at `omega_c` therefore corresponds to a first-pass cutoff range of roughly

```text
f_D ~ 130–320 GHz.
```

This is a model/design scale, not a fabricated-circuit specification.

## Cold covariance calculation

Canonical calculation:

```text
calculations/drude_bath_variance.py
.github/workflows/experiment03-drude-bath.yml
```

For the current favored semiclassical neighborhood

```text
rDelta=0.6
R0=250 ohm,
```

the equilibrium linearized quantum-FDT calculation gives:

| `omega_D/omega_c` | `ReY(omega_c)/G0` | `var(x)/isolated` | `var(v)/isolated` | `sigma_x` [rad] |
|---:|---:|---:|---:|---:|
| 2 | 0.8000 | 0.97839 | 1.05870 | 0.11374 |
| 5 | 0.9615 | 0.97328 | 1.09859 | 0.11344 |
| 10 | 0.9901 | 0.97066 | 1.13563 | 0.11329 |
| 20 | 0.9975 | 0.96900 | 1.17689 | 0.11319 |

The isolated harmonic width is about `0.11499 rad`.

## Interpretation

A physically regularized bath does **not** simply shrink the entire initial phase-space cloud.

In this reduced linear model:

```text
coordinate fluctuations decrease modestly,
velocity fluctuations increase,
and the redistribution depends on the cutoff.
```

Thus the basin probability must eventually be integrated against the **bath-consistent joint state**, not against the isolated harmonic Wigner Gaussian with a damping term added only during propagation.

The high-frequency cutoff is therefore a genuine detector design variable:

```text
higher omega_D
 -> scalar-R-like damping over a broader band
 -> larger ultraviolet velocity fluctuations;

lower omega_D
 -> less high-frequency bath noise
 -> weaker damping and larger reactive modification near the phase frequency.
```

Within a one-pole Drude family, the natural first optimization is to choose the **lowest cutoff that still supplies the required damping over the dynamically relevant phase spectrum**.

## Reactive loading

The Drude bath is not purely dissipative. Since

```math
\frac{\operatorname{Im}Y}{\operatorname{Re}Y}
=\frac{\omega}{\omega_D},
```

a cutoff only a few times `omega_c` also modifies the phase-mode reactive response. This must be retained in the nonlinear trajectory model rather than treating `ReY` alone as an effective resistance.

## Literature boundary

Frequency-dependent damping in Josephson dynamics is established prior art; it is not a novelty claim. The current role of the Drude model is to make Experiment 03 physically self-consistent enough to test whether a persistent-flux photon latch survives a causal noisy environment.

Recent quantum-Brownian-motion work also reinforces that non-Markovian stochastic phase-space descriptions can be exact for quadratic systems, while nonlinear potentials require additional control/approximation. Therefore the cold harmonic covariance can be treated more cleanly than the nonlinear switching event itself.

## Next calculation

1. Replace scalar `R` in the full nonlinear deterministic pulse solver by the auxiliary-current Drude dynamics.
2. Map whether the scalar-R capture region survives for `omega_D/omega_c ~ 4–10`.
3. Construct a bath-consistent correlated initial state for `(x,v,bath)` rather than reusing the isolated Wigner distribution.
4. Add the same Drude spectral density to stochastic pulse dynamics.
5. Use that identical spectral density in dissipative quantum escape/MQT.

Only after these steps can a probability such as `P_capture > 0.99` be treated as a physical detector-fidelity statement.

## Status

**GO for continued theory. NO-GO for manuscript.**
