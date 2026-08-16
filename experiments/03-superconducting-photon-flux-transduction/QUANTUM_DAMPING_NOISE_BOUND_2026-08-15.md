# Experiment 03 — Quantum Damping–Noise Bound — 2026-08-15

## Statement

For any passive equilibrium linear environment coupled through the junction/loop electrical coordinate, quantum fluctuation-dissipation gives the symmetrized current-noise spectrum

```math
S_I^{sym}(\omega)
=
\hbar|\omega|
\coth\!\left(\frac{\hbar|\omega|}{2k_BT_{bath}}\right)
\operatorname{Re}Y(\omega).
```

Since `coth(z)>=1` for positive `z`, immediately

```math
\boxed{
S_I^{sym}(\omega)
\ge
\hbar|\omega|\operatorname{Re}Y(\omega)
}.
```

This is the zero-temperature quantum floor associated with dissipative loading.

## Phase-frequency form

At the cold phase frequency `omega_c`, define the local dissipative rate

```math
\gamma_c
=\frac{\operatorname{Re}Y(\omega_c)}{C}
```

and corresponding local quality factor

```math
Q_c=\frac{\omega_c}{\gamma_c}.
```

Then

```math
\boxed{
S_I^{sym}(\omega_c)
\ge
\hbar\omega_c C\gamma_c
=\frac{\hbar C\omega_c^2}{Q_c}.
}
```

Therefore stronger dissipative capture assistance (`smaller Q_c`) necessarily raises the minimum finite-frequency current-noise spectral density.

## Phase-acceleration form

For `q=Phi_bar*x`, with `Phi_bar=Phi0/(2pi)`, current noise enters the phase equation as `I_N/(C Phi_bar)`. Hence

```math
S_{\ddot x}(\omega_c)
=\frac{S_I(\omega_c)}{C^2\Phi_{bar}^2}
```

and the FDT floor becomes

```math
\boxed{
S_{\ddot x}(\omega_c)
\ge
\frac{\hbar\omega_c\gamma_c}{C\Phi_{bar}^2}.
}
```

Using the isolated zero-point phase variance

```math
\sigma_{x,0}^2
=\frac{\hbar}{2C\Phi_{bar}^2\omega_c},
```

this can also be written

```math
\boxed{
S_{\ddot x}(\omega_c)
\ge
2\sigma_{x,0}^2\omega_c^2\gamma_c.
}
```

This form makes the connection between cold quantum localization and required dynamical damping explicit.

## Detector interpretation

The earlier deterministic calculation found a finite damping window because damping has two opposing roles:

```text
launch/crossing: too much damping removes useful phase energy;
capture/retrapping: sufficient damping helps lock the target well.
```

The quantum FDT bound adds a third role:

```text
any dissipative loading that assists capture also injects irreducible zero-point fluctuations.
```

Thus `R` or `ReY` cannot be optimized from deterministic basin geometry alone.

The true operating problem must maximize a probability functional subject to both persistent capture and cold escape/noise:

```math
\mathcal O
=
\{\theta:
P_{cap}(\theta)\ge p_*,
\Gamma_{dark}(\theta)\le D_*
\},
```

where the same `Y(omega)` enters both conditions.

## Critical temperature distinction

Do not substitute the weak-link electronic temperature `T_e(t)` into FDT automatically.

```text
T_e(t)      controls CPR / Josephson potential / calorimetric response;
T_bath(t)   controls environmental equilibrium fluctuations.
```

Only when the dissipative element thermalizes with the photon-heated weak link is `T_bath~T_e` justified.

For an external cold shunt or electromagnetic environment, `T_bath` may remain close to the refrigerator temperature even while the weak link reaches `~0.6–0.8 K`.

At `f~27–32 GHz` and `T_bath=20 mK`, the quantum-to-classical FDT factor

```math
\mathcal Q
=\frac{\hbar\omega}{2k_BT}
\coth\!\left(\frac{\hbar\omega}{2k_BT}\right)
```

is about `32–38`. Classical Johnson noise is therefore not a valid finite-frequency approximation for a cold bath at the phase frequency.

If the dissipative bath itself were at `0.6–0.8 K`, the same factor would fall to roughly `1.2–1.5`.

## Status / novelty

This is an application of standard quantum fluctuation-dissipation physics, not a novelty claim by itself.

Its Experiment-03 value is that it closes a loophole in the architecture optimization: **damping strong enough to shape the capture basin has an irreducible quantum noise cost even at zero temperature.**

The next stochastic model must obey this bound automatically by deriving both damping and noise from the same causal admittance.

**GO for continued theory. NO-GO for manuscript.**
