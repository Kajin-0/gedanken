# Experiment 03 — Damping–Noise–Persistent-Signal Identity — 2026-08-15

## Result

For the local harmonic cold mode, define

```math
\omega_c^2=\frac{\kappa_c}{LC},
```

where `kappa_c` is the dimensionless curvature of the normalized rf-SQUID force. Let the persistent-state flux separation be

```math
\Delta\Phi=\zeta\Phi_0,
```

so the circulating-current separation is

```math
\Delta I=\frac{\zeta\Phi_0}{L}.
```

For a general passive environment, define the local dissipative quality factor at the phase frequency by

```math
Q_c
\equiv
\frac{\omega_c C}{\operatorname{Re}Y(\omega_c)}.
```

Quantum fluctuation-dissipation gives

```math
S_I^{sym}(\omega_c)
=
\hbar\omega_c
\coth\!\left(\frac{\hbar\omega_c}{2k_BT_{bath}}\right)
\operatorname{Re}Y(\omega_c).
```

Eliminate `ReY`, `C`, and `L` using the definitions above:

```math
\operatorname{Re}Y(\omega_c)
=\frac{\omega_c C}{Q_c},
```

```math
C=\frac{\kappa_c}{L\omega_c^2},
```

```math
L=\frac{\zeta\Phi_0}{\Delta I}.
```

Then

```math
S_I^{sym}(\omega_c)
=
\frac{\hbar\kappa_c\Delta I}{\zeta\Phi_0Q_c}
\coth\!\left(\frac{\hbar\omega_c}{2k_BT_{bath}}\right).
```

Since

```math
\Phi_0=\frac{\pi\hbar}{e},
```

the final identity is

```math
\boxed{
\frac{S_I^{sym}(\omega_c)}{\Delta I}
=
\frac{e\kappa_c}{\pi\zeta Q_c}
\coth\!\left(\frac{\hbar\omega_c}{2k_BT_{bath}}\right)
}.
```

## Deep-quantum limit

For

```math
\hbar\omega_c\gg k_BT_{bath},
```

`coth -> 1`, giving

```math
\boxed{
\frac{S_I^{sym}(\omega_c)}{\Delta I}
\to
\frac{e\kappa_c}{\pi\zeta Q_c}.
}
```

At fixed normalized topology (`kappa_c`, `zeta`) and fixed local quality factor, this ratio is independent of

```text
L,
C,
omega_c,
and the overall Josephson energy scale.
```

That independence is the key elimination.

## Detector implication

The persistent-state current signal and the dissipative bath noise cannot be scaled independently once the normalized topology and the required phase-frequency damping are fixed.

If successful capture requires

```math
Q_c\le Q_{max},
```

then in the quantum regime

```math
\boxed{
\frac{S_I^{sym}(\omega_c)}{\Delta I}
\ge
\frac{e\kappa_c}{\pi\zeta Q_{max}}.
}
```

Thus a deterministic upper bound on acceptable `Q_c` immediately implies a minimum bath-noise spectral density per unit persistent-current separation.

This is stronger than the generic statement `more damping -> more noise`: the loop and harmonic-mode variables have been eliminated.

## Scope discipline

This is **not** a detector NEP or readout-SNR formula. `S_I(omega_c)` is the bath fluctuation spectrum that perturbs the phase dynamics near the phase mode, while `Delta I` is the persistent current-state separation. Their ratio is therefore a dynamic noise-to-latched-signal scale, not directly an output current-noise PSD at DC.

The result assumes:

```text
1. a locally harmonic cold mode;
2. a passive equilibrium linear environment at T_bath;
3. FDT applies to that environment;
4. Q_c is defined from ReY at omega_c;
5. state separation DeltaPhi=zeta Phi0.
```

No scalar-R or Drude form is required.

## Relation to the existing quantum localization identity

The separately derived low-temperature harmonic identity

```math
\sigma_x^2\tau_0\Delta I
=\frac{2\pi e\zeta}{\kappa_c}
```

connects localization, phase timescale and current separation.

The present identity connects current separation, damping and irreducible bath fluctuations.

Together they show that circuit rescaling cannot independently optimize

```text
quantum localization,
phase speed,
persistent-state current signal,
and dissipative noise.
```

## Novelty discipline

The algebra follows standard circuit quantization plus quantum fluctuation-dissipation. No broad novelty claim is authorized. Its possible value is as one component of an Experiment-03 detector-specific feasibility/optimality closure once the nonlinear capture requirement supplies a quantitative bound on `Q_c`.

**GO for continued theory. NO-GO for manuscript.**
