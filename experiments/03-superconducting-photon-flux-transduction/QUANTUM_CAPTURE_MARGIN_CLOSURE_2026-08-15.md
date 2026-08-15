# Quantum Initial-State / Basin-Margin Closure — 2026-08-15

## Purpose

Connect three quantities that had previously been treated separately:

```text
cold harmonic quantum width
<-> cold barrier/action scale
<-> finite-time capture-basin margin.
```

The first identity below is exact inside the harmonic approximation to the cold metastable well. The mapping to a dark-count target uses the existing provisional cubic-MQT diagnostic and is therefore not an exact dissipative rf-SQUID result.

## 1. Cold harmonic phase mode

Let `x` be the dimensionless rf-SQUID phase coordinate and let

```math
\bar\Phi=\frac{\Phi_0}{2\pi}.
```

Near the cold left minimum `x_c`, write

```math
U(x)\simeq U(x_c)+\frac12\frac{\bar\Phi^2}{L}\kappa_c(x-x_c)^2.
```

The phase kinetic energy is

```math
K=\frac12 C\bar\Phi^2\dot x^2,
```

so

```math
\boxed{\omega_c=\sqrt{\frac{\kappa_c}{LC}}.}
```

For the harmonic thermal Wigner state,

```math
\sigma_x^2
=\frac{\hbar}{2C\bar\Phi^2\omega_c}
\coth\!\left(\frac{\hbar\omega_c}{2k_BT_0}\right),
```

and

```math
\sigma_v^2
=\frac{\hbar\omega_c}{2C\bar\Phi^2}
\coth\!\left(\frac{\hbar\omega_c}{2k_BT_0}\right).
```

Define normalized velocity

```math
u\equiv\dot x/\omega_c.
```

Then

```math
\boxed{\sigma_u=\sigma_x.}
```

Thus the cold harmonic Wigner distribution is isotropic in the normalized phase plane `(x,u)`.

For the current Experiment-03 cases the numerical workflow gives

```text
rDelta=0.8: sigma_x = 0.11559 rad, hbar omega_c/(k_B T0) = 76.9
rDelta=0.6: sigma_x = 0.11499 rad, hbar omega_c/(k_B T0) = 65.4.
```

Hence the initial distribution is overwhelmingly zero-point rather than thermal at `T0=20 mK`.

## 2. Exact barrier/action–quantum-width identity

Let the cold barrier be

```math
\Delta U_c
=\frac{\bar\Phi^2}{L}u_b,
```

where `u_b` is the dimensionless barrier of the normalized phase potential.

Define the simple barrier-to-harmonic-quantum ratio

```math
S\equiv\frac{\Delta U_c}{\hbar\omega_c}.
```

Multiplying the Wigner variance by `S` and using `LC\omega_c^2=\kappa_c` gives

```math
\boxed{
\sigma_x^2 S
=\frac{u_b}{2\kappa_c}
\coth\!\left(\frac{\hbar\omega_c}{2k_BT_0}\right).
}
```

Equivalently,

```math
\boxed{
\sigma_x^2
=\frac{u_b}{2\kappa_c S}
\coth\!\left(\frac{\hbar\omega_c}{2k_BT_0}\right).
}
```

At `T0 << hbar omega_c/k_B`,

```math
\boxed{\sigma_x^2 S=\frac{u_b}{2\kappa_c}.}
```

This is independent of `L` and `C` separately.

Interpretation: increasing the cold barrier/action that suppresses quantum escape also localizes the initial phase state relative to the same normalized potential. Dark stability and initial quantum capture blur are therefore not independent design problems.

## 3. Local finite-time basin boundary

Let the full pulse dynamics pull the final cold separatrix back to the initial phase plane. Near the physical initial point `(x_c,0)`, approximate the relevant branch of that pulled-back basin boundary by

```math
u=a+s(x-x_c).
```

Here `a` is the signed velocity-axis intercept in units of `omega_c`, and `s` is the local slope in the normalized `(x,u)` plane.

Because the initial harmonic Wigner Gaussian is isotropic, the signed normal distance from the distribution center to this local line is

```math
d_n=\frac{-a}{\sqrt{1+s^2}}
```

with sign chosen positive into the target basin.

For a single locally planar boundary and no nearby competing basin strips,

```math
\boxed{
P_{cap}^{(local)}
=\Phi\!\left(\frac{d_n}{\sigma_x}\right),
}
```

where `Phi` is the standard normal CDF.

Therefore a target capture probability `p` requires

```math
\boxed{
d_n\ge z_p\sigma_x,}
\qquad
z_p=\Phi^{-1}(p).
```

With the present `sigma_x~0.115`, the required inward normal margins are approximately

| target p | z_p | required d_n |
|---:|---:|---:|
| 0.90 | 1.282 | 0.147 |
| 0.95 | 1.645 | 0.189 |
| 0.99 | 2.326 | 0.268 |
| 0.999 | 3.090 | 0.355 |
| 0.9999 | 3.719 | 0.428 |

The deterministic switching boundary `d_n=0` is therefore a **50% quantum-capture contour** in the local single-boundary approximation, not a high-efficiency detector threshold.

## 4. Connection to the existing dark-count diagnostic

Retain only as the present provisional MQT diagnostic

```math
D
=\frac{\omega_c}{2\pi}
\exp[-\alpha_Q S],
```

with `alpha_Q~7.2`.

Using

```math
\omega_c=\frac{\Delta U_c}{\hbar S},
```

the equality `Gamma_Q=D` gives

```math
\alpha_Q S\,e^{\alpha_Q S}
=\frac{\alpha_Q\Delta U_c}{2\pi\hbar D}.
```

Thus

```math
\boxed{
S=\frac1{\alpha_Q}
W\!\left(
\frac{\alpha_Q\Delta U_c}{2\pi\hbar D}
\right)
\equiv\frac{W_D}{\alpha_Q}.
}
```

Substituting into the harmonic identity yields

```math
\boxed{
\sigma_x^2
=\frac{\alpha_Q u_b}{2\kappa_c W_D}
\coth\!\left(\frac{\hbar\omega_c}{2k_BT_0}\right).
}
```

At low temperature the local target-capture margin becomes

```math
\boxed{
 d_{n,p}
\ge
 z_p
\sqrt{\frac{\alpha_Q u_b}{2\kappa_c W_D}}.
}
```

This removes explicit `L` and `C` from the combined initial-quantum-spread / diagnostic-dark-target condition.

For small target `D`, `W_D` grows only logarithmically, so the minimum quantum blur decreases only roughly as

```math
 d_{n,p}\propto[\ln(1/D)]^{-1/2}
```

up to the slowly varying barrier argument and topology factors.

## 5. Check against the current basin-section data

The existing finite-time topology workflow shows why deterministic center labels are insufficient.

### rDelta=0.6, rise=20 ps, R=75 ohm

At `x=x_c`, the central target-basin interval ends at

```text
u_edge ~ +0.09225.
```

With `sigma_u~0.11499`, a one-dimensional single-edge estimate gives a margin of only

```text
~0.80 sigma,
```

corresponding to a capture probability near `0.79` before accounting for `x` dependence and other strips. The full two-dimensional order-5 Wigner quadrature gave

```text
P_R ~0.821.
```

This is consistent with the local-margin interpretation.

### rDelta=0.8, rise=5 ps, R=185 ohm

The section is strongly multistrip. Near `u=0` the first positive edge is only

```text
u_edge ~ +0.01477,
```

or about `0.13 sigma_u`, but additional right-basin strips occur nearby. The order-5 two-dimensional quadrature gave

```text
P_R ~0.705,
```

while lower-order quadrature differed strongly.

This case is **outside a reliable single-boundary approximation**. The full pulled-back basin geometry must be integrated.

## 6. Consequence for detector optimization

The deterministic design objective

```text
make the center trajectory land in the right basin
```

is too weak.

The correct probability-level objective is

```math
\boxed{
\text{maximize the Wigner probability mass contained in the target pulled-back basin.}
}
```

For a locally simple basin this reduces to maximizing

```math
\boxed{\mathcal M_Q=d_n/\sigma_x,}
```

with

```math
P_{cap}=\Phi(\mathcal M_Q).
```

For folded/multistrip basins, `M_Q` is insufficient and the full basin integral is required.

This reframes damping optimization. A deterministic capture window can contain regions with poor stochastic fidelity because the physical initial point lies too close to a folded basin boundary. The best `R` or more general environment should maximize basin **probability volume under the initial quantum distribution**, not merely produce deterministic capture.

## 7. Immediate numerical requirement

The current tensor Gauss-Hermite integration is poorly matched to a discontinuous folded basin indicator. Its order dependence is already material.

Next use geometry-aware integration:

1. at selected `x` values, locate **all** relevant basin transitions in normalized velocity;
2. integrate the conditional Gaussian in `u` analytically between those boundaries;
3. integrate the resulting smooth(er) conditional target probability over the Gaussian `x` distribution;
4. validate against direct Monte Carlo / quasi-Monte-Carlo only as a secondary check.

This should provide converged `P_capture^(init)` for the current `rDelta=0.8` multistrip and `rDelta=0.6` simpler families.

## 8. Status

**GO for continued theory. NO-GO for manuscript.**

The new analytical object is the dark-action / quantum-width / basin-margin closure. It may become useful in a later detector-specific theorem, but no novelty claim is authorized before the full stochastic environment and prior-art audit.
