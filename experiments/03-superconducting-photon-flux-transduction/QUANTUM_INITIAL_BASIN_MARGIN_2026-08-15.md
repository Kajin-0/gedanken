# Quantum Initial-State / Finite-Time Basin Margin — 2026-08-15

## Purpose

Connect the preferred deterministic capture object — the pulled-back finite-time basin boundary — to the first controlled approximation for capture probability arising from the **cold phase state's initial quantum fluctuations**.

This checkpoint does **not** yet include noise during the optical pulse, dissipative MQT, environmental quantum noise, or a fully quantum time-dependent phase evolution. It only establishes the harmonic cold-state covariance and the local Gaussian geometry needed for the next stochastic layer.

## 1. Cold harmonic phase Hamiltonian

Let

```math
\bar\Phi=\frac{\Phi_0}{2\pi}.
```

Near the cold metastable minimum `x_c`, write

```math
U(x,T_0)
\simeq
U_c
+\frac12\frac{\bar\Phi^2}{L}\kappa_c(x-x_c)^2.
```

The phase kinetic energy is

```math
K
=\frac12C\bar\Phi^2\dot x^2.
```

Therefore the harmonic phase mode has effective mass

```math
\boxed{m_x=C\bar\Phi^2}
```

and frequency

```math
\boxed{
\omega_c
=\sqrt{\frac{\kappa_c}{LC}}.
}
```

## 2. Quantum thermal covariance

For a harmonic oscillator in equilibrium at `T0`, the Wigner covariance is Gaussian with

```math
\boxed{
\sigma_x^2
=\frac{\hbar}{2C\bar\Phi^2\omega_c}
\coth\!\left(\frac{\hbar\omega_c}{2k_BT_0}\right),
}
```

and

```math
\boxed{
\sigma_v^2
=\frac{\hbar\omega_c}{2C\bar\Phi^2}
\coth\!\left(\frac{\hbar\omega_c}{2k_BT_0}\right).
}
```

The equilibrium cross covariance vanishes in this harmonic basis.

A useful identity is

```math
\boxed{
\frac{\sigma_v}{\omega_c}=\sigma_x.
}
```

In the ground-state limit,

```math
\hbar\omega_c\gg k_BT_0,
```

the `coth` factor tends to one.

## 3. Current illustrative quantum scale

Using the current retuned illustrative `C=C_min,Q` values and cold curvatures inferred consistently within the provisional MQT checkpoint:

### `r_Delta=0.8`

```text
L      ~96.8 pH
C      ~181 fF
kappa  ~0.711
f_c    ~32.1 GHz
hbar omega / (k_B T0) ~76.9 at T0=20 mK
sigma_x ~0.116 rad
sigma_v/omega_c ~0.116.
```

### `r_Delta=0.6`

```text
L      ~111.5 pH
C      ~215 fF
kappa  ~0.702
f_c    ~27.2 GHz
hbar omega / (k_B T0) ~65.4
sigma_x ~0.115 rad
sigma_v/omega_c ~0.115.
```

Thus the current cold harmonic phase degree of freedom is strongly quantum rather than classically thermally broadened.

These numbers remain conditional because the capacitance is inherited from the **provisional cubic-MQT optimization**, not a calibrated fabricated device.

## 4. Local finite-time basin boundary

Let the exact pulled-back finite-time basin boundary be

```math
\mathcal B_0.
```

Near the cold mean state, approximate its section by

```math
\boxed{
v-v_b-s_b(x-x_c)=0.
}
```

Here

```text
v_b  finite-time edge velocity at x=x_c
s_b  local slope dv_edge/dx.
```

Choose orientation so the target basin satisfies

```math
v-s_b(x-x_c)>v_b.
```

The random variable normal to the boundary is then

```math
Y=v-s_b(x-x_c).
```

For the harmonic Gaussian cold state,

```math
\boxed{
\sigma_Y^2
=\sigma_v^2+s_b^2\sigma_x^2.
}
```

## 5. Initial-state capture probability — local Gaussian approximation

The mean cold state is

```math
(x_c,0).
```

Therefore the signed covariance-normalized basin distance is

```math
\boxed{
Z_B
=-\frac{v_b}
{\sqrt{\sigma_v^2+s_b^2\sigma_x^2}}.
}
```

The target-basin probability arising **only from the initial Gaussian phase-state spread**, with subsequent evolution treated deterministically, is approximately

```math
\boxed{
P_R^{(init)}
\simeq
\Phi(Z_B),
}
```

where `Phi` is the standard normal CDF.

Consequences:

```text
v_b = 0  -> P_R ~1/2 in the local symmetric Gaussian approximation;
Z_B >> 1 -> initial state lies robustly on target side;
Z_B << -1 -> robustly on original-basin side.
```

Thus a deterministic pulse-parameter boundary is naturally a **50% probability contour** once an initially centered quantum Gaussian spread is included, provided the local linear-boundary approximation is valid and pulse noise is neglected.

## 6. Why the boundary slope matters

Using only `v_edge(x_c)` is not sufficient for quantum robustness.

If the pulled-back manifold is steep in the `(x,v)` plane, position zero-point fluctuations can dominate even when the velocity intercept looks large.

Therefore the next finite-time basin calculation should extract at least

```text
v_b
dv_edge/dx
```

near `x_c`.

The correct uncertainty scale is the boundary-normal covariance, not a raw phase or velocity rms separately.

## 7. Relation to classical thermal covariance

The classical limit would give

```math
\sigma_x^2
=\frac{k_BT_0L}{\bar\Phi^2\kappa_c},
\qquad
\sigma_v^2
=\frac{k_BT_0}{C\bar\Phi^2}.
```

But for the current illustrative points

```text
hbar omega / kBT ~65–77,
```

so this classical approximation is inappropriate for the cold phase degree of freedom.

Do not use classical Johnson/equipartition fluctuations to estimate the initial phase-state width in this regime.

## 8. What this does not include

The formula `P_R~Phi(Z_B)` omits:

```text
noise injected during the optical pulse
dissipative quantum fluctuations from the environment
MQT before/during the pulse
non-Gaussian cold-state corrections
quantum coherence/interference across the moving barrier
measurement backaction
spatial thermal stochasticity.
```

It is a bridge from deterministic basin geometry to a first semiclassical/phase-space probability estimate, not the final detector efficiency.

## 9. Next calculation

Once `finite_time_basin_slice.py` has validated the pulled-back boundary section:

1. compute `v_edge(x)` at several `x` values near `x_c`;
2. fit local slope `s_b`;
3. evaluate `Z_B` for pulses on both sides of the deterministic capture boundary;
4. determine how far pulse parameters must move beyond deterministic threshold to obtain, e.g., `P_R^(init)>0.9`, `0.99`, `0.999` from initial-state uncertainty alone;
5. then add stochastic forcing during the pulse using the same causal environment used for damping/MQT.

## Status

**HARMONIC QUANTUM INITIAL-STATE COVARIANCE: ESTABLISHED WITHIN CURRENT CIRCUIT PARAMETERS.**

**LOCAL GAUSSIAN BASIN PROBABILITY: NEXT-ORDER APPROXIMATION, NOT FINAL DETECTOR EFFICIENCY.**

**EXPERIMENT 03: GO for continued theory; NO-GO for manuscript.**
