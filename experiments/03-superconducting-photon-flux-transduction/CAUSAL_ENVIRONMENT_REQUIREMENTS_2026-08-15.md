# Causal Environment / Fluctuation-Dissipation Requirements — 2026-08-15

## Purpose

Replace the conceptual use of a freely adjustable scalar damping resistance by the minimal physically consistent environment model required for stochastic capture and dissipative quantum escape.

This note does **not** yet solve the stochastic dynamics. It defines the model that the next solver must satisfy.

## 1. Circuit coordinate and linear environment

Let

```math
\bar\Phi=\frac{\Phi_0}{2\pi},
\qquad
q=\bar\Phi x,
\qquad
V=\dot q=\bar\Phi\dot x.
```

For a causal linear electromagnetic environment with admittance kernel `y(t)` / frequency-domain admittance `Y(omega)`, the phase-coordinate equation can be written in current units as

```math
\boxed{
C\ddot q(t)
+\int_{-\infty}^{t}y(t-t')\dot q(t')dt'
+\frac{\partial U(q,T)}{\partial q}
=I_N(t).
}
```

Equivalently in the dimensionless phase coordinate,

```math
\boxed{
C\bar\Phi^2\ddot x
+\bar\Phi^2\int_{-\infty}^{t}y(t-t')\dot x(t')dt'
+\partial_xU(x,T)
=\bar\Phi I_N(t).
}
```

For a frequency-independent resistor,

```math
Y=1/R,
```

this reduces to the scalar-R damping term used in the current deterministic solver.

## 2. Fluctuation-dissipation constraint

The dissipative part of the same admittance that damps the phase also determines equilibrium current fluctuations.

Using a two-sided symmetrized angular-frequency PSD convention,

```math
\boxed{
S_I^{sym}(\omega)
=\hbar|\omega|\
\coth\!\left(\frac{\hbar|\omega|}{2k_BT_b}\right)
\operatorname{Re}Y(\omega),
}
```

where `T_b` is the relevant environment temperature.

The phase-force noise is therefore

```math
\boxed{
S_{\xi}^{sym}(\omega)
=\bar\Phi^2 S_I^{sym}(\omega),
\qquad
\xi=\bar\Phi I_N.
}
```

In the classical low-frequency limit this convention gives

```math
S_I^{sym}\to2k_BT_b\operatorname{Re}Y,
```

which corresponds to the usual one-sided Johnson current PSD `4 k_B T_b ReY` after convention conversion.

**Consequence:** Experiment 03 may not optimize `Re Y` for deterministic capture while independently setting the corresponding bath noise to zero.

## 3. Current operating regime is not safely classical

The current cold mode frequencies from the finite-time basin calculations are approximately

```text
rDelta=.8: f_c ~32.0 GHz
rDelta=.6: f_c ~27.3 GHz.
```

These correspond to

```math
\frac{hf_c}{k_B}\approx1.54\,K
```

and

```math
\frac{hf_c}{k_B}\approx1.31\,K,
```

respectively.

The relevant fold/hot temperatures in the current two-gap family are only about `0.6–0.8 K`.

Therefore

```math
\frac{hf_c}{k_BT}=O(1),
```

not `<<1`.

A purely classical white-Johnson Langevin source is therefore not a controlled approximation over the phase-mode band. The stochastic environment should retain the quantum `coth` spectrum, or a demonstrably equivalent reduced model.

At the 20-mK cold state the mode is much deeper in the quantum regime, consistent with the existing harmonic-Wigner results `hbar omega_c/(k_B T0)~65–77`.

## 4. The same bath must enter quantum escape

Caldeira and Leggett showed that linear dissipation changes the quantum tunneling problem itself rather than merely adding classical noise after a tunneling rate is computed. Ambegaokar, Eckern and Schoen derived analogous dissipative quantum phase dynamics microscopically for Josephson tunneling.

Primary references:

```text
A. O. Caldeira and A. J. Leggett,
Influence of Dissipation on Quantum Tunneling in Macroscopic Systems,
Phys. Rev. Lett. 46, 211 (1981), DOI 10.1103/PhysRevLett.46.211.

V. Ambegaokar, U. Eckern, and G. Schoen,
Quantum Dynamics of Tunneling between Superconductors,
Phys. Rev. Lett. 48, 1745 (1982), DOI 10.1103/PhysRevLett.48.1745.
```

Thus the final model must use one environment spectral function consistently in

```text
deterministic memory/friction kernel,
pulse-time environmental fluctuations,
cold dissipative quantum escape,
and any equilibrium/dephasing calculation.
```

The present cubic `alpha_Q=7.2` MQT diagnostic remains useful only as a screening surrogate until this replacement is made.

## 5. Why frequency dependence may help but is not free

The full deterministic dynamics revealed a two-stage conflict:

```text
launch/crossing: strong damping can remove useful phase energy;
post-crossing capture: damping can suppress return/retrapping.
```

A frequency-dependent environment could in principle shape those stages differently. But causality couples the reactive and dissipative parts of `Y(omega)` and fluctuation-dissipation couples `Re Y` to noise.

Therefore the admissible optimization variable is not an arbitrary time-dependent friction coefficient. It is a **causal passive (or explicitly active, if later allowed) admittance** with its associated fluctuations and reactive loading.

Generation A should remain passive unless the research question is deliberately broadened.

## 6. Minimum next stochastic model

The next probability calculation should progress in two levels.

### Level 1 — controlled Ohmic bath

Retain scalar `R` but add a quantum-consistent Ohmic bath. This isolates how much the current initial-Wigner-only capture probabilities change once pulse-time bath fluctuations are included.

The comparison should be

```text
P_init only
vs
P_init + bath noise
```

at the same `(R,L,C,T_b)` and identical deterministic pulse.

### Level 2 — causal colored admittance

Replace `1/R` by a low-order realizable `Y(omega)`, for example one or more passive RC/RL poles, and optimize

```text
capture probability
subject to dark escape target,
settling time,
and passive FDT noise.
```

The same `Y(omega)` must then be used in the dissipative Euclidean-action / quantum-escape calculation.

## 7. New operating-set definition

Deterministic capture is no longer an adequate criterion. For target capture probability `p_*` and dark-event target `D_*`, define the model operating set

```math
\boxed{
\mathcal O(p_*,D_*)
=\{\theta:
P_{cap}(\theta)\ge p_*,
\;\Gamma_{dark}(\theta)\le D_*\},
}
```

where `theta` contains at minimum

```text
photon energy / wavelength,
rise/transport parameters,
CPR/material parameters,
L and C,
environment Y(omega),
environment temperature,
flux tilt.
```

The research question becomes whether `O(p_*,D_*)` is nonempty for useful LWIR targets after all noise channels are treated consistently.

## Status

**GO for continued theory. NO-GO for manuscript.**

The next mandatory physical correction is a fluctuation-dissipation-consistent environment. The initial-Wigner basin integration should be numerically converged first so the incremental effect of bath noise can be isolated cleanly.
