# Dynamic Saddle-Node / Fold-Ghost Stress — 2026-08-15

## Purpose

Test the assumption that thermally crossing the **static** rf-SQUID/CPR fold is sufficient for persistent capture.

It is not. Near a saddle-node the restoring curvature vanishes, producing critical slowing. A photon can therefore push the electronic temperature above `T_f` while the phase remains trapped in the saddle-node bottleneck long enough for the CPR to recover and the metastable basin to reappear.

This checkpoint derives the universal local scaling and applies it as a **conditional stress test** to the current 8–14-um retuned family. It is not yet a full time-dependent CPR/RCSJ simulation.

## 1. Local fold normal form

Let

```math
q=x-x_f,
\qquad
\theta=T-T_f.
```

At a nondegenerate thermal fold,

```math
F(x_f,T_f)=0,
\qquad
F_x(x_f,T_f)=0.
```

Choose coordinate orientation so that just beyond the fold (`theta>0`) the local deterministic force can be written

```math
\boxed{
-F(q,\theta)
\simeq
A\theta+\frac{B}{2}q^2,
\qquad A>0,\;B>0.
}
```

The local RCSJ equation becomes

```math
\boxed{
LC\,\ddot q+\frac{L}{R}\dot q
\simeq
A\theta+\frac{B}{2}q^2.
}
```

## 2. Why any finite damping becomes overdamped near the fold

On the metastable side, the local minimum/saddle displacement scales as

```math
|q|\propto |\theta|^{1/2},
```

and the curvature scales as

```math
\kappa\propto|\theta|^{1/2}.
```

Therefore the local oscillation frequency obeys

```math
\omega_m\propto|\theta|^{1/4}.
```

For finite Ohmic damping,

```math
\zeta\sim\frac{1}{2RC\omega_m}
\propto|\theta|^{-1/4}.
```

Hence

```math
\boxed{\zeta\to\infty\quad\text{as the fold is approached}.}
```

Even a circuit that is underdamped in the recovered cold basin becomes locally overdamped sufficiently close to the saddle-node.

This is the dynamical reason that a static fold crossing cannot be treated as an instantaneous write.

## 3. Overdamped ghost-passage scaling

Neglect inertia in the asymptotically near-fold region:

```math
\frac{L}{R}\dot q
=A\theta+\frac{B}{2}q^2.
```

For a fixed step overshoot `theta>0`, the idealized full ghost passage from `q=-infinity` to `+infinity` is

```math
 t_{ghost}
=\frac{L}{R}
\int_{-\infty}^{\infty}
\frac{dq}{A\theta+(B/2)q^2}.
```

Thus

```math
\boxed{
 t_{ghost}^{(full)}
=\frac{\pi\sqrt2\,L/R}
{\sqrt{AB\theta}}.
}
```

The exact order-one prefactor required for physical basin capture depends on where the full nonlinear trajectory enters and exits the local normal-form region. The robust result is the divergence

```math
\boxed{t_{ghost}\propto\theta^{-1/2}.}
```

A barely supercritical photon is therefore dynamically unfavorable even though the static metastable well has disappeared.

## 4. Relate the ghost coefficient to cold curvature

On the metastable side let

```math
\mu_c=T_f-T_0>0.
```

Within the same local normal form, the cold stable-point curvature is

```math
\kappa_c\simeq\sqrt{2AB\mu_c}.
```

Hence

```math
\sqrt{AB}\simeq\frac{\kappa_c}{\sqrt{2\mu_c}}.
```

The full-ghost estimate becomes

```math
\boxed{
 t_{ghost}^{(full)}
\simeq
\frac{2\pi L}{R\kappa_c}
\sqrt{\frac{\mu_c}{\theta}}.
}
```

This uses the cold curvature to estimate the local normal-form product `AB`; it is only quantitatively controlled if the current operating point remains inside the useful fold-normal-form range.

## 5. Combine ghost passage with recovered-basin damping

For an underdamped recovered basin, the linear envelope time is

```math
 t_{set}=2RC.
```

A necessary write interval must be at least as large as both the saddle-node passage scale and the recovered-basin damping scale. Therefore use the optimistic diagnostic

```math
 t_{dyn}(R)
=\max\!\left[
\frac{2\pi L}{R\kappa_c}
\sqrt{\frac{\mu_c}{\theta}},
\;2RC
\right].
```

Minimizing this maximum by equating the two branches gives

```math
\boxed{
R_{opt}
=\sqrt{\frac{\pi L}{C\kappa_c}}
\left(\frac{\mu_c}{\theta}\right)^{1/4}.
}
```

and

```math
\boxed{
 t_{dyn,min}
=2\sqrt{\frac{\pi LC}{\kappa_c}}
\left(\frac{\mu_c}{\theta}\right)^{1/4}.
}
```

At the provisional quantum-stability optimum `LC=tau_Q^2`,

```math
\boxed{
 t_{dyn,min}
=2\sqrt{\frac{\pi}{\kappa_c}}\;\tau_Q
\left(\frac{T_f-T_0}{T_{pk}-T_f}\right)^{1/4}.
}
```

This result is useful because it eliminates both `L` and `C` separately from the optimized dynamic bottleneck.

### Interpretation

The divergence has softened from `theta^-1/2` to

```math
\boxed{t_{dyn,min}\propto\theta^{-1/4}}
```

after optimizing `R`, because increasing `R` speeds the overdamped fold passage but eventually slows recovered-basin damping.

## 6. Conditional self-consistency criterion

The actual temperature is cooling during the write, so replacing the entire pulse by a constant `T_pk` makes the fold force **larger** than it really is after the peak. The fixed-peak estimate is therefore intentionally optimistic about the available drive.

A necessary-style stress test is

```math
\boxed{
 t_>(T_{pk},T_f)
\gtrsim
 t_{dyn,min}(T_{pk}-T_f).
}
```

Because the local ghost prefactor and entry/exit definition are not yet calibrated to the full CPR trajectory, this inequality is currently a **diagnostic**, not a rigorous device theorem.

## 7. Conditional Huang-calibrated 14-um stress

Use the same conditional thermal mapping as `HUANG_THERMAL_DWELL_CALIBRATION_2026-08-15.md`.

For a `100 um^2` absorber, the retained Huang energy scaling gives one absorbed `14 um` photon

```text
T_pk(14 um) ~0.8321 K.
```

The current retuned realistic-skewness family then gives:

| `r_Delta` | `T_f` | overshoot `theta=Tpk-Tf` | conditional `t_>` | optimized `t_dyn,min` | margin `t_>/t_dyn` | `R_opt` |
|---:|---:|---:|---:|---:|---:|---:|
| 1.0 | 0.905 K | no static crossing | — | — | — | — |
| 0.8 | 0.813 K | 0.0191 K | 4.11 ps | 44.7 ps | 0.092 | 123 ohm |
| 0.6 | 0.695 K | 0.1371 K | 37.6 ps | 30.9 ps | 1.22 | 71.8 ohm |
| 0.5 | 0.623 K | 0.2091 K | 67.9 ps | 30.3 ps | 2.24 | 62.1 ohm |
| 0.4 | 0.540 K | 0.2921 K | 119 ps | 31.3 ps | 3.81 | 54.5 ohm |

### Strong conditional lesson

The old static statement

```text
r_Delta~0.8 barely reaches the 14-um fold
```

is not dynamically robust.

Under the current conditional thermal calibration and local fold diagnostic, its `19 mK` overshoot produces far too little above-fold dwell. The `r_Delta~0.6` point is approximately the first retained coarse point that passes this **optimistic** dynamic stress at 14 um.

This is not yet a detector cutoff because:

1. the Huang thermal coefficient identification is conditional;
2. the full-ghost order-one prefactor is not the exact basin-capture prefactor;
3. the real temperature and CPR evolve continuously, not as a constant peak step;
4. the full RCSJ trajectory can retain inertia away from the asymptotically soft region;
5. noise can either assist correct capture or induce wrong-basin capture.

Nevertheless, the result establishes that **static spectral reach is an upper envelope, not a sufficient spectral criterion**.

## 8. Dynamic spectral frontier

The static absorbed-photon frontier was

```math
T_{pk}(\lambda,A)\ge T_f.
```

The corrected concept is

```math
\boxed{
T_{pk}>T_f
\quad\text{and}\quad
\mathcal M_{fold}
\equiv
\frac{t_>(T_{pk},T_f)}
{t_{dyn,min}(T_{pk}-T_f)}
\gtrsim1.
}
```

This introduces a **finite overshoot requirement** above the static fold.

The spectral boundary should therefore be defined by the implicit equation

```math
\boxed{
 t_>[T_{pk}(\lambda),T_f]
=
2\sqrt{\frac{\pi}{\kappa_c}}\tau_Q
\left[
\frac{T_f-T_0}{T_{pk}(\lambda)-T_f}
\right]^{1/4}
}
```

inside the present approximations.

This is a materially stronger object than the previous static `lambda_max(T_f)` relation because it couples photon energy, thermal decay, cold quantum-stability capacitance and saddle-node critical slowing.

## 9. Immediate next calculation

The local fold stress is now strong enough that more static parameter scanning is low value.

The next decisive calculation should integrate the **full time-dependent CPR/RCSJ equation**:

```math
LC\ddot x
+\int_{-\infty}^{t}K(t-t';T_e)\dot x(t')dt'
+F[x,T_e(t)]
=\xi(t),
```

first deterministically with scalar `R`, then stochastically / with a causal admittance.

Required outputs:

```text
P_capture
P_wrong
P_return-to-original-basin
capture-time distribution
minimum Tpk overshoot
sensitivity to R / Y(omega)
```

The static fold map should be retained only as the zero-rate limit of this dynamic problem.

## Status

**GO for continued theory. NO-GO for manuscript.**
