# Conditional Huang Thermal-Dwell Calibration — 2026-08-15

## Purpose

Use the 2026 Huang et al. graphene single-photon calorimeter as a **conditional calibration** of the clean-graphene thermal coefficient in Experiment 03, then test whether the current retuned fold family survives the finite-dwell constraint.

This checkpoint is deliberately conservative about interpretation. Huang et al. fit an effective electron-phonon decay time `tau_ep = 75 ns` at `T0 = 20 mK` in a clean-graphene (`delta=4`) thermal model and state that `tau_ep \propto T0^(2-delta) = T0^-2` when modeling base-temperature dependence. Mapping that fitted quantity onto the local coefficient in the Experiment-03 continuous-cooling model is an **identification assumption**, not a directly measured local lifetime at every hot-electron temperature.

Primary source:

```text
B. Huang et al., "Thermal detection of single photons using Dirac fermions",
Nature Communications 17, 3845 (2026)
DOI: 10.1038/s41467-026-70648-0
```

Relevant published facts:

```text
base temperature T0 ~20 mK
graphene area ~100 um^2
clean-graphene model delta=4
best-fit tau_ep ~75 ns at T0=20 mK
best-fit single-photon peak temperature ~2.5 K
MoRe parent gap scale ~1.3 meV
heat-diffusion length ~230 um, much longer than device.
```

## 1. Conditional coefficient identification

Experiment 03 uses

```math
C_e=\gamma A T,
\qquad
P_{e-ph}=\Sigma A(T^4-T_0^4).
```

The corresponding local small-signal relaxation scale is

```math
\tau_{ep}^{loc}(T)=\frac{\gamma}{4\Sigma T^2}.
```

For this checkpoint only, identify the Huang fitted 20-mK time with the low-temperature coefficient:

```math
\boxed{
\tau_{ep}^{loc}(T_0=20\,mK)=75\,ns.
}
```

Then

```math
\boxed{
\frac{\gamma}{4\Sigma}
=(75\,ns)(0.020\,K)^2
=3.0\times10^{-11}\;s\,K^2.
}
```

Therefore

```math
\boxed{
\tau_{ep}^{loc}(T)
=\frac{3.0\times10^{-11}}{T^2}\;s
}
```

under this conditional mapping.

This immediately corrects a previous intuition: `75 ns` must **not** be inserted as a temperature-independent dwell time at a `0.5–0.9 K` fold.

## 2. Maximum dwell above the fold

The exact clean-graphene infinite-energy dwell ceiling retained in Experiment 03 is

```math
 t_{>,max}(T_f)
=\frac{\gamma}{4\Sigma T_0^2}
\ln\!\left(\frac{T_f^2+T_0^2}{T_f^2-T_0^2}\right).
```

With the conditional calibration above,

```math
\boxed{
 t_{>,max}
=(75\,ns)
\ln\!\left(\frac{T_f^2+T_0^2}{T_f^2-T_0^2}\right).
}
```

For `T0 << Tf`,

```math
 t_{>,max}\simeq2\tau_{ep}^{loc}(T_f)
=150\,ns\left(\frac{0.020\,K}{T_f}\right)^2.
```

Thus sub-kelvin folds have maximum useful dwell in the **10^2-ps class**, not generically in the `75-ns` class.

## 3. Retuned family

Use the current realistic-skewness / induced-gap / retuned-inductance family and the provisional `D=1e-6 s^-1` capacitance floors.

Take the same illustrative phase-settling factor retained earlier,

```text
g=5.
```

At `C=C_min,Q`, define

```math
\tau_Q=\sqrt{LC_{min,Q}},
\qquad
t_{\phi,Q}=g\tau_Q.
```

The damping condition

```math
2R_{hot}C_{min,Q}<t_{>,max}
```

gives a maximum permitted effective hot-state damping resistance

```math
\boxed{
R_{crit}=\frac{t_{>,max}}{2C_{min,Q}}.
}
```

### Conditional numerical checkpoint

| `r_Delta` | `T_f` | `L` | `C_min,Q` | `t_phi,Q` (`g=5`) | `t_>,max` | phase margin `tmax/tphi` | `R_crit` |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.0 | 0.905 K | 87.8 pH | 161 fF | 18.8 ps | 73.3 ps | 3.90 | 228 ohm |
| 0.8 | 0.813 K | 96.8 pH | 181 fF | 20.9 ps | 90.8 ps | 4.34 | 251 ohm |
| 0.6 | 0.695 K | 111.5 pH | 215 fF | 24.5 ps | 124.2 ps | 5.07 | 289 ohm |
| 0.5 | 0.623 K | 123.1 pH | 244 fF | 27.4 ps | 154.6 ps | 5.64 | 317 ohm |
| 0.4 | 0.540 K | 140.3 pH | 287 fF | 31.7 ps | 205.8 ps | 6.49 | 358 ohm |

## 4. Main result

Under this conditional thermal calibration, **raw phase motion still survives comfortably** across the retained family:

```text
phase margin ~4–6.5.
```

The new bottleneck is the damping envelope.

For the current `D=1e-6 s^-1` provisional quantum-stability target, the passive write requires roughly

```math
\boxed{
R_{hot}\lesssim0.23-0.36\;k\Omega
}
```

across the current retuned family.

At the approximately 14-um boundary point (`r_Delta~0.8`),

```text
Tf        ~0.813 K
Cmin,Q    ~181 fF
tmax      ~90.8 ps
Rcrit     ~251 ohm.
```

At the more conservative `r_Delta~0.6` point,

```text
Tf        ~0.695 K
Cmin,Q    ~215 fF
tmax      ~124 ps
Rcrit     ~289 ohm.
```

This is the first current calculation in which a plausible nonideality threatens the architecture on the same scale as the candidate operating parameters.

## 5. Interpretation discipline

`R_hot` in the Experiment-03 envelope is an **effective phase-damping resistance during the write**, not automatically the measured dc normal-state junction resistance `R_n`.

A real GJJ can have:

```text
frequency-dependent quasiparticle admittance
self-heating
external electromagnetic damping
capacitively/inductively transformed environmental impedance
nonlocal graphene dissipation.
```

Therefore no fabricated-device verdict follows from comparing `R_crit` to an arbitrary quoted `R_n`.

The next model must compute or calibrate the relevant dynamical admittance.

## 6. A sharp falsification condition

Inside the combined assumptions

```text
clean graphene T^4 cooling
conditional Huang coefficient mapping
provisional cubic MQT rate
C optimized to C_min,Q
simple RCSJ damping envelope 2 R_hot C
```

if

```math
\boxed{
R_{hot}>R_{crit}(T_f,D)
}
```

throughout every cold-stable fold capable of the desired LWIR wavelength,
then

```text
no increase in photon energy can rescue passive capture.
```

This follows because `t_>,max` is already the infinite-photon-energy dwell ceiling.

That would be a genuine architecture-level negative result **within this model class**.

## 7. Possible escape routes if damping fails

If a realistic dynamical admittance gives `R_hot > R_crit`, possible modifications are:

1. increase the cold barrier so the target `D` can be met with smaller `C_min,Q`;
2. engineer a lower effective high-frequency damping resistance;
3. use a frequency-selective or switched damping environment;
4. alter the weak-link/cooling physics to increase `t_>`;
5. abandon passive fold capture in favor of an active reset/write protocol.

Every one of these changes modifies noise and/or MQT physics. In particular, adding a resistive shunt reintroduces dissipative fluctuation channels and invalidates the current undamped/cubic MQT diagnostic. It cannot be counted as a free fix.

## 8. Reproducibility

The table is reproduced by

```text
calculations/eliminated_dark_capture_closure.py
```

using the retuned checkpoint values already recorded in `SPECTRAL_STABILITY_PARETO_2026-08-15.md`.

## Status

**GO for continued theory. NO-GO for manuscript.**

The most important next physical quantity is now the **frequency-dependent effective phase-damping admittance during the hot fold crossing**, not additional static photon-energy optimization.
