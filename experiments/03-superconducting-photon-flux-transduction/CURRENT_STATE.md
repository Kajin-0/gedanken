# Experiment 03 — CURRENT_STATE

**Updated:** 2026-08-15  
**Mode:** exploratory theory / falsification-first  
**Publication status:** **NO-GO for manuscript**.

## 1. Current question

Can one absorbed LWIR photon drive a proximity-Josephson/rf-SQUID circuit through a directionally selected **dynamic** fold transition, after which the phase is captured in a persistent superconducting flux state, while cold false switching remains extremely low?

Generation A uses a small external flux tilt and is **not photovoltaic**. Generation B remains reserved for a later zero-external-flux mechanism.

Current chain:

```text
absorbed 8–14 um photon
 -> rapid electronic thermalization/spreading
 -> temperature-dependent full CPR changes
 -> metastable CPR/load-line fold is crossed
 -> saddle-node bottleneck must be traversed before cooling restores the well
 -> phase enters favored basin
 -> CPR recovers
 -> persistent superconducting flux remains.
```

A static fold crossing is now treated only as the zero-rate limit of the problem.

## 2. Noise / dissipation interpretation

An ideal cold superconducting storage channel with `Re Z -> 0` lacks the ordinary finite-frequency resistive Johnson contribution of that channel. This does **not** imply zero detector noise or zero dark counts.

Relevant limits include

```text
thermal phase escape
macroscopic quantum tunneling (MQT)
quasiparticles and vortices
stray/background photons
write-state damping noise
readout backaction
reset errors
photon statistics.
```

Any dissipative admittance introduced to improve phase capture must ultimately be treated with fluctuation-dissipation. The long-term objective is not zero total fluctuation; it is low detector-added noise with a persistent superconducting storage state.

## 3. Canonical static fold

Define

```math
I_* = \frac{\Phi_0}{2\pi L},
\qquad
\mathcal I(x,T)=\frac{I_s(x,T)}{I_*},
\qquad
F=x-\delta-\mathcal I.
```

A static fold satisfies

```math
\boxed{\mathcal I(x_f,T_f)=x_f-\delta,}
\qquad
\boxed{\partial_x\mathcal I(x_f,T_f)=1.}
```

For a smooth nondegenerate fold,

```math
\Delta U\propto|p-p_f|^{3/2},
\qquad
\omega_m\propto|p-p_f|^{1/4},
\qquad
\Delta U/(\hbar\omega_m)\propto|p-p_f|^{5/4}.
```

## 4. Static material model retained

The ideal graphene CPR baseline uses the Titov–Beenakker secular equation plus the Hagymasi–Kormanyos–Cserti arbitrary-length Matsubara construction. It has been checked both in the controlled short-junction limit and at the intermediate `L/xi~1.1` parameter family used in the published arbitrary-length theory.

Realistic-interface CPR skewness from Nanda-type graphene/MoRe devices substantially reduces the ideal cold barrier. The useful static envelope at the illustrative `beta_cold=0.8`, `Ic~3 uA` scale is closer to

```text
T_f ~0.79–0.91 K
cold barrier ~5.9–9.1 k_B K
state separation ~0.22–0.24 Phi0
provisional C_min,Q ~0.16–0.31 pF.
```

The ideal `16.7 K` barrier is retained only as a regression, not as the defensible realistic value.

## 5. Two-gap model — mandatory

Do not identify the induced weak-link gap with the parent-electrode gap:

```text
Delta_ind -> ABS spectrum, Ic(T), CPR harmonics and fold temperature
Delta_s   -> parent-electrode quasiparticle escape / calorimetric confinement.
```

The preferred materials direction is potentially

```text
smaller engineered Delta_ind for thermal CPR sensitivity
+
high parent Delta_s for hot-electron confinement
+
retuned L/C for cold phase stability and write dynamics.
```

For graphene-like `C_e=gamma A T`, conservative parent-gap confinement and fold crossing require

```math
\boxed{T_f\le T_{pk}\lesssim\Delta_s/k_B,}
```

which gives

```math
\boxed{
\frac{2\eta E_\gamma}
{\gamma[(\Delta_s/k_B)^2-T_0^2]}
\le A\le
\frac{2\eta E_\gamma}
{\gamma(T_f^2-T_0^2)}.
}
```

A nonempty interval requires `Delta_s > k_B T_f`.

## 6. Retuned induced-gap Pareto family

With realistic-skewness shape stress and inductance retuned to keep the illustrative cold screening point near `beta=0.8`:

| `r_Delta` | `T_f` | `L` | cold barrier/kB | provisional `C_min,Q` | static thermal reach for `A=100 um^2` |
|---:|---:|---:|---:|---:|---:|
| 1.0 | 0.905 K | 87.8 pH | 9.10 K | 161 fF | 11.8 um |
| 0.8 | 0.813 K | 96.8 pH | 8.12 K | 181 fF | 14.7 um |
| 0.6 | 0.695 K | 111.5 pH | 6.87 K | 215 fF | 20.1 um |
| 0.5 | 0.623 K | 123.1 pH | 6.10 K | 244 fF | 25.0 um |
| 0.4 | 0.540 K | 140.3 pH | 5.22 K | 287 fF | 33.3 um |

These wavelengths are **static absorbed-photon thermal limits only**. They are no longer considered sufficient detection cutoffs.

## 7. Capacitance elimination: quantum-stability time

Inside the current provisional cubic MQT diagnostic,

```math
\Gamma_Q
=\frac{\omega}{2\pi}
\exp\left[-\alpha_Q\frac{\Delta U_c}{\hbar\omega}\right],
\qquad
\omega=\sqrt{\frac{\kappa_c}{LC}},
```

with target dark rate `D`, define

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

Then exactly inside this diagnostic,

```math
\boxed{LC_{min,Q}=\tau_Q^2,}
\qquad
\boxed{C_{min,Q}=\tau_Q^2/L.}
```

This removes explicit capacitance from several dynamic constraints.

For the old `g sqrt(LC)` phase-time convention,

```math
\boxed{t_{\phi,Q}=g\tau_Q.}
```

A phase-limited target capture interval `t_c` gives the provisional dark-rate floor

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

Near a smooth thermal fold, combining the `3/2` barrier law with graphene `E~T^2` calorimetry yields the conditional low-`T0` scaling

```math
\boxed{
\lambda_{max}
\propto
\left[
\frac{t_c}{\ln(1/Dt_c)}
\right]^{4/3}.
}
```

This is a candidate mathematical object for later novelty audit, not a novelty claim.

Canonical record: `DARK_CAPTURE_ELIMINATION_2026-08-15.md`.

## 8. Clean-graphene dwell ceiling

For the retained idealized cooling law

```math
C_e=\gamma AT,
\qquad
P_{e-ph}=\Sigma A(T^4-T_0^4),
```

the time above a fixed fold is

```math
\boxed{
t_>(T_{pk},T_f)
=\frac{\gamma}{4\Sigma T_0^2}
\ln\!\left[
\frac{(T_{pk}^2-T_0^2)(T_f^2+T_0^2)}
{(T_{pk}^2+T_0^2)(T_f^2-T_0^2)}
\right].
}
```

Even `T_pk -> infinity` gives a finite ceiling

```math
\boxed{
t_{>,max}
=\frac{\gamma}{4\Sigma T_0^2}
\ln\!\left(
\frac{T_f^2+T_0^2}{T_f^2-T_0^2}
\right).
}
```

For `T0 << Tf`,

```math
\boxed{t_{>,max}\simeq2\tau_{ep}^{loc}(T_f).}
```

If the required write time exceeds this ceiling, no larger photon energy rescues the design **within this cooling model**.

### Huang calibration is conditional

Huang et al. fit `tau_ep~75 ns` at `T0=20 mK` in their clean-graphene thermal model and use `tau_ep propto T0^-2` for the base-temperature dependence. Identifying that fitted quantity directly with the local coefficient `gamma/(4 Sigma T^2)` is an explicit modeling assumption, not a measured hot-state lifetime.

Under that conditional identification, the sub-kelvin fold dwell ceiling falls into the `~70–200 ps` range across the retuned family. These numbers are useful as a stress test but are **not promoted as calibrated device lifetimes**.

Canonical record: `HUANG_THERMAL_DWELL_CALIBRATION_2026-08-15.md`.

## 9. Exact scalar-R RCSJ damping window

The earlier `2RC` damping envelope was only the underdamped branch.

Linearizing about a recovered stable basin gives

```math
\boxed{
LC\ddot y+\frac{L}{R}\dot y+\kappa y=0.
}
```

Define

```math
\omega_0=\sqrt{\frac{\kappa}{LC}},
\qquad
R_*=\frac12\sqrt{\frac{L}{C\kappa}}.
```

`R=R_*` is critical damping and gives the fastest possible linearized scalar-Ohmic relaxation:

```math
\boxed{
\tau_{settle,min}=\sqrt{\frac{LC}{\kappa}}.
}
```

Very large `R` is weakly damped; very small `R` is overdamped and also slow.

For an allowed settling time `t_avail`, let

```math
a=\omega_0t_{avail}.
```

A scalar resistance solution exists only if `a>=1`, and then

```math
\boxed{
\frac{2a}{a^2+1}
\le\frac{R}{R_*}\le a.
}
```

The previous `R<t/(2C)` condition is exactly the high-`R` edge; a missing low-`R` edge also exists.

Under the conditional Huang dwell mapping and current provisional `C_min,Q` values, the retained family gives roughly

```text
R_* ~13–14 ohm
R_- ~1–2 ohm
R_+ ~0.23–0.36 kOhm.
```

These are model diagnostics, not a shunt recommendation. A real GJJ has frequency-dependent admittance.

Canonical record: `RCSJ_DAMPING_WINDOW_2026-08-15.md`.

## 10. Dynamic fold / saddle-node bottleneck — current frontier

Static fold crossing is insufficient because the local curvature vanishes at a saddle-node.

Write

```math
q=x-x_f,
\qquad
\theta=T-T_f.
```

Locally beyond the fold,

```math
-F\simeq A\theta+\frac{B}{2}q^2.
```

For any finite Ohmic damping the local damping ratio diverges as the fold is approached:

```math
\boxed{\zeta\propto\theta^{-1/4}\to\infty.}
```

Thus the asymptotically near-fold passage is overdamped even if the recovered basin is underdamped.

For a fixed step overshoot, the full local ghost-passage estimate is

```math
\boxed{
t_{ghost}^{full}
=\frac{\pi\sqrt2\,L/R}{\sqrt{AB\theta}}
\propto\theta^{-1/2}.
}
```

Using the cold curvature to estimate the local normal-form product,

```math
\boxed{
t_{ghost}^{full}
\simeq
\frac{2\pi L}{R\kappa_c}
\sqrt{\frac{T_f-T_0}{T_{pk}-T_f}}.
}
```

Balancing this against the recovered-basin underdamped envelope gives the optimistic optimized diagnostic

```math
\boxed{
R_{opt}
=\sqrt{\frac{\pi L}{C\kappa_c}}
\left(
\frac{T_f-T_0}{T_{pk}-T_f}
\right)^{1/4},
}
```

```math
\boxed{
t_{dyn,min}
=2\sqrt{\frac{\pi LC}{\kappa_c}}
\left(
\frac{T_f-T_0}{T_{pk}-T_f}
\right)^{1/4}.
}
```

At `C=C_min,Q`,

```math
\boxed{
t_{dyn,min}
=2\sqrt{\frac{\pi}{\kappa_c}}\tau_Q
\left(
\frac{T_f-T_0}{T_{pk}-T_f}
\right)^{1/4}.
}
```

Therefore a finite temperature overshoot above the fold is required. The static relation `T_pk>=T_f` is only an upper-envelope criterion.

### Conditional 14-um stress

For `A=100 um^2`, the retained Huang energy scaling gives `T_pk(14 um)~0.832 K`.

Inside the **conditional** Huang dwell mapping and local fold diagnostic:

```text
rDelta=1.0: no static 14-um crossing
rDelta=0.8: theta~0.019 K, t_>~4.1 ps, optimized dynamic scale~44.7 ps -> strongly fails stress
rDelta=0.6: theta~0.137 K, t_>~37.6 ps, dynamic scale~30.9 ps -> marginally passes stress
rDelta=0.5: substantially larger margin.
```

This does **not** establish a detector cutoff. The order-one ghost prefactor, the conditional thermal calibration, evolving CPR, inertia away from the fold, noise-assisted capture and retrapping remain unresolved.

But it does establish the strongest current falsification lesson:

```text
A point that barely crosses the static fold can be dynamically unusable.
```

Canonical record: `DYNAMIC_FOLD_GHOST_2026-08-15.md`.

## 11. Prior-art boundary

No novelty claim is authorized. Broad ingredients already collided with prior work, including

```text
superconducting MIR/LWIR single-photon detection
photon-heated graphene Josephson switching
thermal Ic suppression used as SQUID readout
single-photon -> persistent superconducting flux memory
optically written persistent flux/vortices
transient Ic suppression -> rf-SQUID tipping/freeze
field-free Josephson directionality
illumination-driven superconducting phase batteries/vorticity
engineering ABS / induced-gap thermal sensitivity
generic detector dark-count vs timing/dead-time tradeoffs.
```

The remaining possible publication route is a narrower quantitative superconducting-fold feasibility/optimality/impossibility closure if it survives the full dynamic and dissipative model plus paper/patent collision audit.

## 12. Immediate next calculation

Stop expanding the static Pareto map.

The next decisive model is the full time-dependent phase equation

```math
LC\ddot x
+\int_{-\infty}^{t}K(t-t';T_e)\dot x(t')dt'
+F[x,T_e(t)]
=\xi(t),
```

with the same causal environmental admittance controlling both damping and fluctuation noise.

Work sequence:

1. deterministic full-CPR trajectory with scalar `R` and realistic `T_e(t)`;
2. extract exact dynamic overshoot and capture basin instead of the local ghost approximation;
3. replace scalar `R` by `Y(omega,T_e)` / damping kernel;
4. compute dissipative MQT using that same environment;
5. add stochastic thermal/quantum force and obtain `P_capture`, `P_wrong`, `P_return` and capture-time distribution;
6. only then restore 8–14-um optical absorptance and readout/reset constraints.

## 13. Current verdict

**GO for continued theory. NO-GO for manuscript.**

The dominant uncertainty has moved from photon energy and static fold existence to **finite-rate saddle-node passage plus dissipative phase dynamics**. The branch is still alive, but the static 14-um margin is substantially less informative than it appeared one checkpoint ago.
