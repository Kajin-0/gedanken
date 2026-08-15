# Sudden-Quench Energy Threshold and Three Spectral Regimes — 2026-08-15

## Purpose

Explain analytically why the full deterministic solver can switch **below the quasistatic fold temperature** and organize the current spectral limits into three distinct thresholds.

The core observation is simple:

> A rapid photon pulse changes the potential before the phase coordinate has time to follow its moving local minimum.

Therefore the initial phase after a sudden thermal quench is the **cold equilibrium coordinate**, not the hot metastable minimum.

That displaced state can carry enough potential energy in the hot landscape to cross a barrier that still exists.

## 1. General sudden-quench energy criterion

Let

```text
x_c      cold metastable minimum at T0
x_s(T)   saddle separating the left and right basins at a hotter T<T_f
F(x,T)   Experiment-03 dimensionless phase force.
```

Define the hot-potential energy difference between the saddle and the *cold phase point*

```math
\boxed{
\mathcal B_q(T)
\equiv
U[x_s(T),T]-U[x_c,T]
=\int_{x_c}^{x_s(T)}F(x,T)\,dx.
}
```

This is different from the ordinary hot metastable barrier

```math
U[x_s(T),T]-U[x_m(T),T]
```

because `x_c != x_m(T)` after a nonadiabatic quench.

For an instantaneous quench followed by a fixed hot potential, zero initial phase velocity and conservative phase dynamics:

```text
B_q(T) > 0 : initial phase energy lies below the hot saddle;
B_q(T) = 0 : quench-energy threshold;
B_q(T) < 0 : initial phase point is energetically above the hot saddle.
```

Define

```math
\boxed{\mathcal B_q(T_q)=0.}
```

In general

```math
\boxed{T_q<T_f}
```

whenever the hot metastable minimum moves appreciably before the fold disappears.

`T_q` is **not** a universal detection threshold. It is the ideal conservative sudden-quench energy threshold for the specified CPR/load-line family.

## 2. Current full-CPR values

Using the same arbitrary-length / realistic-skewness retuned models as the full dynamic solver:

### `r_Delta=0.8`

```text
T_q ~0.7183 K
T_f ~0.8119 K.
```

### `r_Delta=0.6`

```text
T_q ~0.6151 K
T_f ~0.6944 K.
```

Thus there is a broad interval

```math
\boxed{T_q<T<T_f}
```

where the static well still exists but an ideal sudden quench can place the cold phase point above the remaining saddle energy.

This is the analytical origin of the sub-fold switching observed in `FULL_DYNAMIC_RCSJ_CHECKPOINT_2026-08-15.md`.

## 3. Convert to photon-wavelength scales

For the retained `A=100 um^2` Huang-ratio calorimetric reference,

```math
T_{ad}^2-T_0^2
=\frac{1.55\,um}{\lambda}
[(2.5\,K)^2-T_0^2].
```

The corresponding wavelength at a temperature threshold `T_*` is

```math
\boxed{
\lambda_*(T_*)
=1.55\,um
\frac{(2.5\,K)^2-T_0^2}
{T_*^2-T_0^2}.
}
```

### `r_Delta=0.8`

Quasistatic fold:

```math
\lambda_{fold}\approx14.70\;um.
```

Ideal sudden-quench energy threshold:

```math
\boxed{\lambda_q\approx18.79\;um.}
```

### `r_Delta=0.6`

Quasistatic fold:

```math
\lambda_{fold}\approx20.10\;um.
```

Ideal sudden-quench energy threshold:

```math
\boxed{\lambda_q\approx25.63\;um.}
```

The quench threshold is therefore materially less restrictive than the quasistatic fold threshold.

## 4. Full finite-cooling dynamics lies between the two limits

Direct scalar-R, instantaneous-deposition simulations with the same CPR and conditional cooling law produce capture to wavelengths longer than the static fold limit, but shorter than the ideal held-hot quench threshold.

A coarse scan gives approximately:

### `r_Delta=0.8`

```text
static fold limit                    ~14.7 um
capture with R <=1 kOhm             survives to ~16.2 um
very-weak-damping tested capture    survives to ~16.7 um
ideal held-hot quench threshold      ~18.8 um.
```

### `r_Delta=0.6`

```text
static fold limit                    ~20.1 um
capture with R <=1 kOhm             survives to ~22.5 um
very-weak-damping tested capture    survives to ~23.0 um
ideal held-hot quench threshold      ~25.6 um.
```

The very-high-R values are not practical detector cutoffs: settling becomes slow and finite-time basin classification becomes sensitive. They are retained only to show the approach toward the conservative/inertial limit.

## 5. Three spectral regimes

For the current model class it is useful to distinguish

### Regime I — quasistatic fold accessible

```math
\lambda<\lambda_{fold}.
```

The photon can remove the selected metastable well in the static limit.

### Regime II — nonadiabatic barrier-crossing only

```math
\boxed{
\lambda_{fold}<\lambda<\lambda_q.
}
```

The hot potential still contains the metastable well, but sufficiently rapid heating can displace/energize the phase enough to cross the residual barrier.

This regime has no counterpart in the original static detector picture.

### Regime III — below ideal sudden-quench phase-energy threshold

```math
\lambda>\lambda_q.
```

The cold phase point remains below the saddle energy in the instantaneously quenched **fixed-hot conservative** potential.

This does not constitute a universal impossibility theorem for arbitrary time-dependent control or noise-assisted switching. It means that the simplest lossless sudden-quench mechanism no longer has enough initial phase energy to cross the hot saddle.

## 6. A new useful dimensionless quench margin

Define

```math
\boxed{
\mathcal M_q(T)
\equiv
-\frac{\mathcal B_q(T)}{\Delta U_{hot}(T)},
}
```

when a finite hot barrier exists.

Interpretation:

```text
M_q < 0  : cold phase point below the hot saddle;
M_q = 0  : sudden-quench threshold;
M_q > 0  : phase starts above the hot saddle energy.
```

This ratio may be more predictive of fast-pulse switching than the binary question of whether the static fold has disappeared.

A finite-damping capture map should use both

```text
quench energy margin M_q
and
thermal rise / phase timescale.
```

## 7. Why this matters for the mechanism name

The broad operating principle is no longer accurately described as only a

```text
fold latch.
```

The fold remains the organizing catastrophe and controls the quasistatic limit, but the fast-photon mechanism includes a distinct nonadiabatic regime.

A more accurate internal description is

```text
photon-triggered nonadiabatic metastable superconducting flux latch
```

with a quasistatic fold branch.

## 8. Next theoretical compression

The full deterministic phase diagram should be reorganized around three dimensionless controls:

```text
quench-energy margin             M_q
thermal-rise / phase-time ratio  rho = tau_rise/tau_phi
phase damping ratio              zeta.
```

Cooling adds a fourth ratio

```text
chi = tau_cool/tau_phi.
```

If capture boundaries from different material points collapse approximately in

```math
(M_q,\rho,\zeta,\chi),
```

that would be a substantially more general theoretical result than a table of graphene device parameters.

## Status

**GO for continued theory. NO-GO for manuscript.**
