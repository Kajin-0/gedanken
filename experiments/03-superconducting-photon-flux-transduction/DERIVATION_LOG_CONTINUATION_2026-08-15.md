# Experiment 03 — Derivation Log Continuation — 2026-08-15

This file continues `DERIVATION_LOG.md` after Step 38. It exists because the active research branch is moving rapidly and the recovery trail must remain readable without relying on conversation history. `CURRENT_STATE.md` remains the compact live state; `CLAIM_LEDGER.md` plus the claim continuation control scientific claim status.

## Step 39: two-gap area window and static spectral Pareto frontier

The induced weak-link gap and parent-electrode gap were separated:

```text
Delta_ind -> ABS spectrum / Ic(T) / CPR / fold
Delta_s   -> parent-electrode quasiparticle escape / thermal confinement.
```

For graphene-like `C_e=gamma A T`, simultaneous static fold crossing and conservative contact confinement give

```math
T_f\le T_{pk}\lesssim\Delta_s/k_B
```

and therefore

```math
\frac{2\eta E_\gamma}
{\gamma[(\Delta_s/k_B)^2-T_0^2]}
\le A\le
\frac{2\eta E_\gamma}
{\gamma(T_f^2-T_0^2)}.
```

Using the Huang `100 um^2`, 1550-nm, `T_1p~2.5 K` thermal calibration as an energy-ratio reference showed that a `~100 um^2` absorber, not the earlier `15.5 um^2` estimate, remains statically capable of an absorbed 10-um photon crossing the current sub-kelvin fold.

The retuned `A=100 um^2` static Pareto family gave approximate absorbed-photon thermal reach

```text
rDelta=1.0 ->11.8 um
0.8 ->14.7 um
0.6 ->20.1 um
0.5 ->25.0 um
0.4 ->33.3 um,
```

while cold barriers and provisional MQT capacitance floors worsen as wavelength reach increases.

Records:

```text
TWO_GAP_LWIR_AREA_MAP_2026-08-15.md
SPECTRAL_STABILITY_PARETO_2026-08-15.md
```

## Step 40: eliminate capacitance through a quantum-stability time

Inside the retained provisional MQT diagnostic,

```math
\Gamma_Q
=\frac{\omega}{2\pi}
\exp[-\alpha_Q\Delta U_c/(\hbar\omega)],
\qquad
\omega=\sqrt{\kappa_c/(LC)},
```

define

```math
\boxed{
\tau_Q(D)
=\frac{\hbar\sqrt{\kappa_c}}
{\alpha_Q\Delta U_c}
W\!\left(
\frac{\alpha_Q\Delta U_c}{2\pi\hbar D}
\right).
}
```

Then

```math
\boxed{LC_{min,Q}=\tau_Q^2.}
```

This removes explicit `C` from the phase-limited dynamic branch. For the earlier phase-time convention,

```math
\boxed{t_{\phi,Q}=g\tau_Q.}
```

A target capture interval can be inverted into a provisional dark-rate floor:

```math
\boxed{
D_{min,\phi}(t_c)
=\frac{g\sqrt{\kappa_c}}{2\pi t_c}
\exp\!\left[-
\frac{\alpha_Q\Delta U_c t_c}
{\hbar g\sqrt{\kappa_c}}
\right].
}
```

Combining this with the smooth-fold `3/2` barrier law and graphene `E~T^2` calorimetry gives the conditional low-`T0` scaling

```math
\boxed{
\lambda_{max}\propto
\left[
\frac{t_c}{\ln(1/Dt_c)}
\right]^{4/3}.
}
```

This is a candidate mathematical object for later novelty collision testing, not a priority claim.

Record: `DARK_CAPTURE_ELIMINATION_2026-08-15.md`.

## Step 41: Huang thermal fit was reinterpreted conservatively

Huang et al. fit a clean-graphene (`delta=4`) thermal model with `tau_ep~75 ns` at `T0=20 mK` and use `tau_ep propto T0^-2` in their base-temperature efficiency model.

An earlier intuition treated `75 ns` too much like a temperature-independent hot-state dwell. That is not justified.

A conditional mapping was therefore made:

```math
\tau_{ep}^{loc}(T_0=20mK)=75ns,
```

inside the Experiment-03 continuous `C_e~T`, `P~T^4` cooling law. This gives much shorter local sub-kelvin times and conditional infinite-energy dwell ceilings of order `70–200 ps` across the retuned family.

This mapping is **explicitly conditional** because the published fitted `tau_ep` is not a direct measurement of `gamma/(4 Sigma T^2)` at every hot-electron temperature.

Record: `HUANG_THERMAL_DWELL_CALIBRATION_2026-08-15.md`.

## Step 42: generic dark-count/timing tradeoff collided with recent detector thermodynamics

Schwarzhans et al., PRX Quantum 7, 033001 (2026), analyze autonomous quantum detectors and explicitly find that reducing detection jitter or dead time increases dark counts in their model.

Therefore Experiment 03 must not claim the **generic** statement

```text
faster detector / shorter recovery <-> more dark counts
```

as new.

Any surviving paper claim must be specific to the superconducting fold/calorimetric closure, its constitutive coefficients, or a sharper architecture-level impossibility/optimality result.

## Step 43: scalar RCSJ damping has a finite window, not a one-sided upper bound

The linearized recovered-basin RCSJ equation is

```math
LC\ddot y+\frac{L}{R}\dot y+\kappa y=0.
```

Critical damping occurs at

```math
\boxed{
R_*=\frac12\sqrt{\frac{L}{C\kappa}}.
}
```

The fastest scalar-Ohmic linear relaxation is

```math
\boxed{
\tau_{min}=\sqrt{LC/\kappa}.
}
```

For `a=omega_0 t_avail`, a solution exists only if `a>=1`, and the exact resistance interval is

```math
\boxed{
\frac{2a}{a^2+1}
\le\frac{R}{R_*}\le a.
}
```

Thus the previous `R<t/(2C)` result is the high-R underdamped boundary only. A low-R overdamped boundary also exists.

Under the conditional Huang dwell mapping and current provisional `C_min,Q` family:

```text
R_* ~13–14 ohm
R_- ~1–2 ohm
R_+ ~0.23–0.36 kOhm.
```

A real device requires `Y(omega,T)`, not a scalar resistor.

Record: `RCSJ_DAMPING_WINDOW_2026-08-15.md`.

## Step 44: static fold crossing is not sufficient because of saddle-node critical slowing

Near the thermal fold let

```math
q=x-x_f,
\qquad
\theta=T-T_f.
```

The normal form can be oriented as

```math
-F\simeq A\theta+\frac{B}{2}q^2.
```

Since `omega_m~|theta|^(1/4)`, any finite damping gives

```math
\zeta\propto|\theta|^{-1/4}\to\infty
```

as the fold is approached. Thus the asymptotically soft region is overdamped even if the cold recovered basin is underdamped.

The fixed-step full-ghost passage scales as

```math
\boxed{
 t_{ghost}^{full}
=\frac{\pi\sqrt2 L/R}{\sqrt{AB\theta}}
\propto\theta^{-1/2}.
}
```

Using the cold curvature to estimate the fold-normal-form product gives

```math
\boxed{
 t_{ghost}^{full}
\simeq
\frac{2\pi L}{R\kappa_c}
\sqrt{\frac{T_f-T_0}{T_{pk}-T_f}}.
}
```

Balancing this local passage scale against the recovered-basin underdamped envelope gives the optimistic diagnostic

```math
\boxed{
 t_{dyn,min}
=2\sqrt{\frac{\pi LC}{\kappa_c}}
\left(\frac{T_f-T_0}{T_{pk}-T_f}\right)^{1/4}.
}
```

At `C=C_min,Q`,

```math
\boxed{
 t_{dyn,min}
=2\sqrt{\frac{\pi}{\kappa_c}}\tau_Q
\left(\frac{T_f-T_0}{T_{pk}-T_f}\right)^{1/4}.
}
```

Therefore a finite thermal overshoot above the static fold is required.

Under the **conditional** Huang thermal mapping for `A=100 um^2` and one absorbed 14-um photon (`Tpk~0.832 K`):

```text
rDelta=0.8: theta~0.019 K, t_>~4.1 ps, optimized dynamic diagnostic~44.7 ps -> fails strongly
rDelta=0.6: theta~0.137 K, t_>~37.6 ps, diagnostic~30.9 ps -> marginally survives
rDelta=0.5: larger dynamic margin.
```

The numbers are not detector cutoffs because the thermal calibration and ghost prefactor are not yet calibrated. The robust result is qualitative but important:

```text
barely crossing a static saddle-node can be dynamically useless.
```

Record: `DYNAMIC_FOLD_GHOST_2026-08-15.md`.

## Current frontier after Step 44

Static photon energy is no longer the main uncertainty. The dominant unresolved problem is the coupled finite-rate phase dynamics:

```text
full time-dependent CPR
+ realistic T_e(t)
+ nonlinear fold passage
+ frequency-dependent admittance / damping kernel
+ fluctuation-dissipation noise
+ dissipative MQT
+ retrapping / wrong-basin capture.
```

The next work should integrate the actual phase equation rather than continue expanding equilibrium parameter tables.

Broad device novelty remains heavily collided. The strongest potential paper route is now a **specific dynamic feasibility/optimality/impossibility closure** for photon-triggered persistent superconducting flux capture, if it survives exact dynamics and a narrow patent/paper audit.
