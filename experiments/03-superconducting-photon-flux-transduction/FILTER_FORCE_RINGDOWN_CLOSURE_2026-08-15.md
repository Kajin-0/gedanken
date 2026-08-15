# Experiment 03 — Filter Force–Ringdown Closure — 2026-08-15

## Purpose

The quartic-rolloff passive environment has two different time scales:

1. the filter memory envelope `tau_D=sqrt(2)/omega_D`;
2. the much longer damping/equilibration time of the **phase mode itself** when `Re Y(omega_c)` is strongly suppressed.

The second scale is the one that caused the first 2-ns stationary-history regression to fail for low cutoff. This checkpoint derives the asymptotic relation between integrated bath-force scale and passive phase-mode ringdown.

This is a closure for the retained passive filter family and weak-damping phase-mode regime, not a universal theorem for arbitrary environments.

---

## 1. Dissipation seen by the phase mode

For

```math
\operatorname{Re}Y(\omega)
=\frac{1/R}{1+(\omega/\omega_D)^4},
```

define

```math
\alpha=\omega_D/\omega_c.
```

At the cold phase frequency,

```math
\boxed{
\operatorname{Re}Y(\omega_c)
=\frac{1/R}{1+\alpha^{-4}}
=\frac{1}{R}\frac{\alpha^4}{1+\alpha^4}.
}
```

For a weakly damped harmonic phase mode, the amplitude-decay rate is approximately

```math
\Gamma_\phi
\simeq
\frac{\operatorname{Re}Y(\omega_c)}{2C},
```

so

```math
\boxed{
\tau_\phi
\equiv\Gamma_\phi^{-1}
\simeq
2RC(1+\alpha^{-4}).
}
```

In the strong-filtering limit `alpha << 1`,

```math
\boxed{
\tau_\phi\simeq2RC\,\alpha^{-4}.
}
```

This is much longer than the filter-memory time `tau_D~alpha^-1`.

---

## 2. Integrated zero-point force scale

For the same filter at `T->0`,

```math
\langle I_N^2\rangle
=\frac{\hbar\omega_D^2}{4R}.
```

For the dimensionless phase-force noise `n=L I_N/barPhi`, the earlier cold-harmonic reduction is

```math
\boxed{
r_n
\equiv
\frac{\sigma_n}{\kappa_c\sigma_x}
=\alpha\sqrt{\frac{g}{2}},
}
```

where

```math
g=\frac{1}{RC\omega_c}.
```

Thus the integrated force scale decreases only linearly with cutoff:

```math
r_n\propto\alpha.
```

---

## 3. Eliminate the cutoff

In the `alpha << 1` weak-damping limit,

```math
\omega_c\tau_\phi
\simeq
\frac{2}{g}\alpha^{-4}.
```

Since

```math
r_n^4=\alpha^4\frac{g^2}{4},
```

we obtain

```math
\boxed{
r_n^4(\omega_c\tau_\phi)
\simeq\frac{g}{2}.
}
```

Equivalently,

```math
\boxed{
r_n
\simeq
\left[
\frac{g}{2\omega_c\tau_\phi}
\right]^{1/4}.
}
```

This is a much steeper practical penalty than the simple bath-memory product:

```text
reduce integrated cold force by factor 2
 -> passive phase ringdown grows by about 2^4 = 16.
```

The physical reason is that the desired phase mode sits far above the low-pass dissipative band: `ReY(omega_c)` is suppressed as `alpha^4`, whereas the integrated zero-point current scale falls only as `alpha`.

---

## 4. Current numerical scale

For the retained `rDelta=.6`,

```text
R = 250 ohm
C = 215 fF
f_c ~27.25 GHz
```

so

```text
g ~0.109
2 R C ~107.5 ps.
```

The weak-damping estimate gives approximately

```text
alpha=.20 -> tau_phi ~67 ns
alpha=.35 -> tau_phi ~7.3 ns
alpha=.50 -> tau_phi ~1.83 ns.
```

Direct eigenvalues of the full cold augmented state give approximately

```text
alpha=.20 -> tau_phi ~69 ns
alpha=.35 -> tau_phi ~7.7 ns
alpha=.50 -> tau_phi ~2.0 ns,
```

confirming the scaling.

This explains the failed first stationary-history regression using only 2 ns of prehistory:

```text
alpha=.20 -> only ~25% of equilibrium rms recovered
alpha=.35 -> ~64%
alpha=.50 -> ~93%.
```

That failure was a finite-history test-design error, not a physical reduction of equilibrium zero-point width.

---

## 5. Important distinction: energetic lock vs full equilibration

A long `tau_phi` does **not** imply that a valid persistent-flux detection state cannot form quickly.

Define two distinct times:

```text
t_lock   = time after which the driven state is energetically confined to the
           favored basin under the recovered tilted potential;

tau_phi  = passive amplitude-decay/equilibration time inside that basin.
```

The detector can in principle become topologically/directionally protected at `t_lock << tau_phi`, while residual oscillation continues inside the target well.

However, any repeated-detection or reset protocol that assumes a stationary cold initial state must either

```text
wait for equilibration,
```

or

```text
actively reset/cool the phase mode and analyze that nonequilibrium preparation explicitly.
```

Thus the low-cutoff environment may improve single-event write robustness at the price of passive repetition rate.

---

## 6. Design implication

The environment optimization now contains at least three coupled objectives:

```text
1. low high-frequency dissipation/noise during nonadiabatic launch;
2. sufficient low-frequency damping to prevent return after capture;
3. acceptable post-event equilibration/reset time.
```

No single scalar `R` captures this structure.

The remaining question is whether directional barrier recovery allows `t_lock` to remain short even when `tau_phi` becomes long. The corrected energetic-lock diagnostic and stationary-history FDT calculation directly test that separation.

**Status: derived filter-family scaling; GO for continued theory; NO-GO for manuscript.**
