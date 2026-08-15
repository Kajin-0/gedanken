# Ohmic Quantum-Bath Cold-State Checkpoint — 2026-08-15

## Purpose

Test the consistency of treating the scalar damping resistance `R` as an equilibrium quantum bath before adding pulse-time stochastic dynamics.

The result sharpens the requirement for a causal frequency-dependent environment.

## 1. Linearized cold phase mode

Let

```math
q=\bar\Phi x,
\qquad
\bar\Phi=\Phi_0/(2\pi),
```

and linearize the cold well with stiffness

```math
K=\kappa_c/L.
```

For an Ohmic shunt,

```math
C\ddot q+\frac1R\dot q+Kq=I_N.
```

The susceptibility is

```math
\chi_q(\omega)
=\frac{1}{K-C\omega^2-i\omega/R}.
```

Using the two-sided symmetrized quantum-FDT spectrum

```math
S_I^{sym}(\omega)
=\frac{\hbar|\omega|}{R}
\coth\!\left(\frac{\hbar|\omega|}{2k_BT_0}\right),
```

the phase-coordinate variance is

```math
\langle\delta x^2\rangle
=\frac1{\bar\Phi^2}
\int_{-\infty}^{\infty}\frac{d\omega}{2\pi}
|\chi_q(\omega)|^2S_I^{sym}(\omega).
```

## 2. Dimensionless zero-temperature result

Define

```math
\omega_c=\sqrt{K/C},
\qquad
g=\frac{1}{RC\omega_c}=Q^{-1}.
```

At `T=0` the ratio of the Ohmic reduced coordinate variance to the isolated harmonic zero-point variance can be integrated exactly for `0<g<2`.

Let

```math
a=1-g^2/2,
\qquad
b=g\sqrt{1-g^2/4}.
```

Then

```math
\boxed{
\frac{\sigma_{x,Ohm}^2}{\sigma_{x,iso}^2}
=\frac{g}{\pi b}
\left[
\frac\pi2+\tan^{-1}\!\left(\frac{a}{b}\right)
\right].
}
```

The finite-20-mK numerical FDT integral agrees with this zero-temperature expression to the retained precision because the current modes are deep in the quantum regime.

Canonical calculation:

```text
calculations/ohmic_cold_variance.py
.github/workflows/experiment03-ohmic-variance.yml
run 31909680008
```

## 3. Current numerical values

### rDelta=.6

| R | Q | variance ratio | sigma isolated | sigma Ohmic |
|---:|---:|---:|---:|---:|
| 75 ohm | 2.76 | 0.8991 | 0.11499 | 0.10903 rad |
| 120 ohm | 4.42 | 0.9339 | 0.11499 | 0.11112 rad |
| 160 ohm | 5.89 | 0.9494 | 0.11499 | 0.11204 rad |
| 250 ohm | 9.21 | 0.9669 | 0.11499 | 0.11307 rad |
| 400 ohm | 14.73 | 0.9790 | 0.11499 | 0.11377 rad |

### rDelta=.8

| R | Q | variance ratio | sigma isolated | sigma Ohmic |
|---:|---:|---:|---:|---:|
| 185 ohm | 6.74 | 0.9554 | 0.11559 | 0.11298 rad |
| 300 ohm | 10.93 | 0.9719 | 0.11559 | 0.11396 rad |
| 400 ohm | 14.58 | 0.9788 | 0.11559 | 0.11436 rad |
| 600 ohm | 21.86 | 0.9857 | 0.11559 | 0.11476 rad |

Thus Ohmic coupling modestly changes the reduced cold coordinate width, but does not parametrically eliminate zero-point uncertainty.

## 4. Critical ultraviolet problem

The coordinate variance converges for a strictly Ohmic quantum bath, but the velocity/momentum variance does not.

At high frequency,

```math
S_I^{sym}(\omega)\sim\frac{\hbar|\omega|}{R},
```

and

```math
|\chi_q(\omega)|^2\sim\frac1{C^2\omega^4}.
```

Therefore the coordinate integrand behaves as

```math
S_q(\omega)\sim\omega^{-3},
```

which is integrable.

But

```math
S_{\dot q}(\omega)=\omega^2S_q(\omega)\sim\omega^{-1},
```

so

```math
\boxed{\langle\dot q^2\rangle_{Ohmic}\text{ is logarithmically UV divergent}.}
```

Equivalently, a strict infinite-bandwidth Ohmic model does not provide a finite physical two-dimensional `(x,xdot)` equilibrium distribution.

This is the standard ultraviolet pathology of an idealized Ohmic quantum bath, not a detector-specific novelty.

## 5. Consequence for Experiment 03

The current basin probability lives in a two-dimensional initial phase plane. Therefore it is **not physically consistent** to combine

```text
finite isolated harmonic sigma_x and sigma_v
+
strict infinite-bandwidth scalar-R damping
```

as if they represented one equilibrium quantum environment.

A real circuit must supply a high-frequency cutoff / colored admittance.

The next environment should therefore use a realizable passive form such as a low-order Drude / series-RL damping branch,

```math
Y(\omega)\sim\frac{1/R}{1+i\omega/\omega_D},
```

or another causal network whose `Re Y` decays at high frequency.

The same `Y(omega)` must determine

```text
cold equilibrium covariance,
real-time damping/memory,
FDT noise,
reactive loading,
and dissipative quantum escape.
```

## 6. Interpretation

This corrects an oversimplified statement that adding equilibrium damping must leave the isolated zero-point coordinate width exactly unchanged. It need not: coupling to an Ohmic bath changes the reduced oscillator variance modestly.

The stronger statement that survives is:

> dissipation cannot be used as a noiseless independent localization knob, and an infinite-bandwidth Ohmic bath is not sufficient to define the full quantum phase-space state required by the capture problem.

## 7. Next model

Introduce a finite-bandwidth passive `Y(omega)` and compute, in one framework,

```text
1. cold covariance in (x,xdot),
2. deterministic memory kernel,
3. symmetrized FDT spectrum,
4. semiclassical noisy capture probability,
5. dissipative quantum escape.
```

The first useful family is a one-pole Drude/series-RL bath because it adds only one physically interpretable cutoff frequency.

## Status

**GO for continued theory. NO-GO for manuscript.**
