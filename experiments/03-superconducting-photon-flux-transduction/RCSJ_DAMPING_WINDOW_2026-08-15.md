# Exact Linear RCSJ Damping Window — 2026-08-15

## Purpose

Correct and sharpen the earlier one-sided damping condition

```math
2R_{hot}C<t_>
```

by solving the complete linearized RCSJ relaxation problem about a stable recovered flux basin.

The earlier expression is the **underdamped envelope branch only**. Very small resistance is not arbitrarily fast: it produces overdamped slow relaxation. The correct linearized result is a finite resistance interval around a critical-damping optimum.

This calculation is exact for the linearized scalar RCSJ equation with a frequency-independent Ohmic resistance. It does not yet solve nonlinear basin capture, retrapping, colored/environmental admittance or dissipative MQT.

## 1. Linearized rf-SQUID/RCSJ dynamics

Let

```math
\bar\Phi=\frac{\Phi_0}{2\pi}.
```

The deterministic phase equation has the form

```math
C\bar\Phi\,\ddot\phi
+\frac{\bar\Phi}{R}\dot\phi
+I_s(\phi,T)
+\frac{\bar\Phi}{L}(\phi-\phi_x)=0.
```

Using the Experiment-03 dimensionless phase force `F`, linearize about a stable recovered minimum `x_m`:

```math
F(x_m)=0,
\qquad
\kappa=\left.\frac{\partial F}{\partial x}\right|_{x_m}>0,
\qquad
y=x-x_m.
```

Then

```math
\boxed{
LC\,\ddot y+\frac{L}{R}\dot y+\kappa y=0.
}
```

After division by `LC`,

```math
\ddot y+\frac1{RC}\dot y+\frac{\kappa}{LC}y=0.
```

Define

```math
\boxed{\omega_0=\sqrt{\frac{\kappa}{LC}}}
```

and damping ratio

```math
\boxed{
\zeta
=\frac{1}{2RC\omega_0}
=\frac1{2R}\sqrt{\frac{L}{C\kappa}}.
}
```

## 2. Critical resistance and fastest passive settling

Critical damping is `zeta=1`, hence

```math
\boxed{
R_*=\frac12\sqrt{\frac{L}{C\kappa}}.
}
```

At this point the repeated pole is

```math
s=-\omega_0.
```

Therefore the minimum possible linearized e-fold settling time over all positive Ohmic `R` is

```math
\boxed{
\tau_{settle,min}=\frac1{\omega_0}
=\sqrt{\frac{LC}{\kappa}}.
}
```

This yields an exact linearized impossibility statement:

```math
\boxed{
t_{avail}<\sqrt{\frac{LC}{\kappa}}
\quad\Rightarrow\quad
\text{no positive scalar resistance can settle the linear mode in }t_{avail}.
}
```

## 3. Both damping branches

Define normalized resistance

```math
r\equiv\frac{R}{R_*}.
```

Then

```math
\zeta=1/r.
```

### Underdamped branch: `r >= 1`

The oscillation envelope decays with rate

```math
\frac1{2RC},
```

so

```math
\boxed{
\tau_s=2RC=\frac{r}{\omega_0}.
}
```

This is the origin of the earlier `2RC` condition.

### Overdamped branch: `0 < r <= 1`

The slow pole has time constant

```math
\boxed{
\tau_s
=\frac1{\omega_0}
\left[
\frac1r+\sqrt{\frac1{r^2}-1}
\right].
}
```

As `R -> 0`,

```math
\tau_s\sim\frac{L}{R\kappa}\to\infty.
```

Thus reducing resistance indefinitely makes the phase relaxation slower, not faster.

## 4. Exact allowed resistance interval for a given time budget

Let

```math
a\equiv\omega_0t_{avail}.
```

A solution exists only if

```math
\boxed{a\ge1.}
```

For `a>=1`, solving `tau_s <= t_avail` on both damping branches gives

```math
\boxed{
\frac{2a}{a^2+1}
\le
\frac{R}{R_*}
\le
a.
}
```

Therefore

```math
\boxed{
R_-
=R_*\frac{2a}{a^2+1},
\qquad
R_+=R_*a.
}
```

The old upper limit is recovered exactly:

```math
R_+=\frac{t_{avail}}{2C}.
```

The missing result was the overdamped lower limit `R_-`.

## 5. Eliminate capacitance at the provisional quantum-stability optimum

From `DARK_CAPTURE_ELIMINATION_2026-08-15.md`, define

```math
\tau_Q(D)
=\frac{\hbar\sqrt{\kappa}}
{\alpha_Q\Delta U_c}
W\!\left(
\frac{\alpha_Q\Delta U_c}{2\pi\hbar D}
\right),
```

with

```math
LC_{min,Q}=\tau_Q^2.
```

Set `C=C_min,Q`. Then

```math
\boxed{
\omega_0=\frac{\sqrt\kappa}{\tau_Q},
}
```

```math
\boxed{
R_*=\frac{L}{2\tau_Q\sqrt\kappa},
}
```

and

```math
\boxed{
a=\frac{t_{avail}\sqrt\kappa}{\tau_Q}.}
```

The no-resistance-can-rescue condition becomes

```math
\boxed{
t_{avail}<\frac{\tau_Q}{\sqrt\kappa}.}
```

For `a>=1`,

```math
\boxed{
R_-
=\frac{L}{2\tau_Q\sqrt\kappa}
\frac{2a}{a^2+1},
\qquad
R_+
=\frac{L}{2\tau_Q\sqrt\kappa}a.
}
```

Again,

```math
R_+=\frac{t_{avail}}{2C_{min,Q}}.
```

So the previous `R_crit` values were not wrong; they were the **upper edge of the underdamped-compatible interval**, not a complete damping criterion.

## 6. Conditional Huang-calibrated numerical window

Use the same conditional clean-graphene thermal calibration as `HUANG_THERMAL_DWELL_CALIBRATION_2026-08-15.md`, with `t_avail=t_>,max` and the current retuned family.

The cold curvatures implied by the retained provisional MQT checkpoints are approximately `kappa~0.69–0.72`.

| `r_Delta` | `T_f` | `kappa` | `tmax` | `R_*` critical | `R_-` | `R_+` |
|---:|---:|---:|---:|---:|---:|---:|
| 1.0 | 0.905 K | 0.716 | 73.3 ps | 13.8 ohm | 1.67 ohm | 228 ohm |
| 0.8 | 0.813 K | 0.711 | 90.8 ps | 13.7 ohm | 1.50 ohm | 251 ohm |
| 0.6 | 0.695 K | 0.702 | 124.2 ps | 13.6 ohm | 1.28 ohm | 289 ohm |
| 0.5 | 0.623 K | 0.698 | 154.6 ps | 13.4 ohm | 1.14 ohm | 317 ohm |
| 0.4 | 0.540 K | 0.690 | 205.8 ps | 13.3 ohm | 0.99 ohm | 358 ohm |

The corresponding dimensionless margins `a=omega0 tmax` are about `16.5–26.9`, so the linearized recovered-basin mode has a broad allowable Ohmic-resistance window under this conditional model.

## 7. Important interpretation change

The previous statement

```text
R_hot must be below roughly 0.23–0.36 kOhm
```

was incomplete.

The corrected statement is

```text
For a frequency-independent scalar R in the linearized recovered-basin model,
R must lie inside a finite interval.
```

For the conditional retuned family above, that interval is approximately

```text
1–2 ohm < R < 0.23–0.36 kOhm,
```

with fastest linearized relaxation near

```text
R ~13–14 ohm.
```

These numbers are **not device predictions** because the physical environment is frequency dependent and the relevant hot-state admittance has not been calibrated.

## 8. Why this matters for the zero-Johnson-noise motivation

A dissipative element can speed the write/retrapping dynamics, but fluctuation-dissipation couples any real part of the admittance to current fluctuations. The correct optimization is therefore not

```text
make R as small as possible.
```

It is closer to

```text
provide sufficient damping in the write-state dynamical band
while minimizing dissipative coupling in the cold storage/dark-count band.
```

This points naturally to a **temperature- and frequency-dependent admittance** rather than a permanent broadband resistor.

A frequency-selective environment may therefore be useful, but it cannot be treated as a noiseless free parameter; its equilibrium and quantum noise must be included through fluctuation-dissipation.

## 9. Next required model

Replace scalar `R` by a causal admittance

```math
Y(\omega,T_e)=Y_1(\omega,T_e)+iY_2(\omega,T_e).
```

The phase equation then becomes nonlocal in time through a damping kernel. The next calculation should determine whether one can simultaneously obtain

```text
fast hot-state basin capture
low cold-state dissipative noise
suppressed cold MQT
a persistent superconducting storage state.
```

The dissipative MQT action must use the same environmental spectral density; the damping environment cannot be optimized independently for classical capture and quantum dark switching.

## Status

**GO for continued theory. NO-GO for manuscript.**
