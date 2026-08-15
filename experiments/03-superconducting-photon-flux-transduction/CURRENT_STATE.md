# Experiment 03 — CURRENT_STATE

**Updated:** 2026-08-15  
**Mode:** exploratory theory / falsification-first  
**Publication status:** **NO-GO for manuscript**.

## 1. Current physical question

Can one absorbed LWIR photon rapidly reshape a proximity-Josephson/rf-SQUID metastable potential so that the phase is transferred into a directionally favored basin and retained as persistent superconducting flux, while cold false switching remains extremely low?

Generation A uses a small external flux tilt and is **not photovoltaic**. Generation B remains reserved for a future zero-external-flux mechanism if one survives collision review.

The preferred internal description is now

```text
photon-triggered nonadiabatic metastable superconducting flux latch
```

rather than a purely quasistatic “fold latch.”

## 2. Mechanism hierarchy

Current sequence:

```text
absorbed LWIR photon
 -> electronic thermalization / spatial energy delivery to the weak link
 -> full Josephson CPR and metastable phase potential change rapidly
 -> phase is displaced and accelerated
 -> trajectory may cross a finite transient barrier or a vanished fold
 -> thermal recovery reforms the cold double-well landscape
 -> trajectory is captured in the favored basin
 -> persistent superconducting flux remains.
```

The rf-SQUID fold is still the organizing catastrophe and controls the slow/quasistatic limit, but **static fold disappearance is neither necessary nor sufficient for fast-pulse switching**.

## 3. Noise / dissipation interpretation

An ideal cold superconducting storage channel with `Re Z -> 0` lacks the ordinary finite-frequency resistive Johnson contribution of that channel. This does not imply zero detector noise or zero dark counts.

Relevant limits remain

```text
thermal phase escape
macroscopic quantum tunneling (MQT)
quasiparticles / vortices
stray and background photons
write-state dissipation and fluctuation-dissipation noise
readout backaction
reset errors
photon statistics.
```

A damping environment cannot be optimized independently of its noise or dissipative-MQT effect.

## 4. Static fold retained as quasistatic limit

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

Near a smooth nondegenerate fold,

```math
\Delta U\propto|p-p_f|^{3/2},
\qquad
\omega_m\propto|p-p_f|^{1/4}.
```

These remain useful asymptotic checks, but the full detector must be solved dynamically.

## 5. Static material baseline

The graphene CPR baseline uses the Titov–Beenakker secular equation plus the Hagymasi–Kormanyos–Cserti arbitrary-length Matsubara construction. It has passed both the controlled short-limit regression and an intermediate `L/xi~1.1` trend check.

Realistic interface/skewness stress reduces the ideal high-doping static result to an illustrative envelope near

```text
T_f ~0.79–0.91 K
cold barrier ~5.9–9.1 k_B K
state separation ~0.22–0.24 Phi0
provisional C_min,Q ~0.16–0.31 pF.
```

The old ideal `16.7 K` barrier is regression-only.

## 6. Two-gap model — mandatory

Do not identify

```text
Delta_ind  weak-link induced/minigap controlling ABS spectrum, Ic(T), CPR and thermal sensitivity
Delta_s    parent-electrode gap controlling hot-carrier escape / calorimetric confinement.
```

A plausible design direction is

```text
moderately reduced Delta_ind for thermal sensitivity
+
high parent Delta_s for confinement
+
retuned L/C for cold stability
+
localized fast optical-to-electronic energy delivery near the weak link.
```

For graphene-like `C_e=gamma A T`, the conservative quasistatic fold/confinement screen is

```math
T_f\le T_{pk}\lesssim\Delta_s/k_B,
```

but `T_pk>=T_f` is no longer a necessary condition for the nonadiabatic mechanism.

## 7. Retuned static family

Realistic-skewness, retuned `beta~0.8`, `A=100 um^2` family:

| `r_Delta` | `T_f` | `L` | cold barrier/kB | provisional `C_min,Q` | quasistatic thermal reach |
|---:|---:|---:|---:|---:|---:|
| 1.0 | 0.905 K | 87.8 pH | 9.10 K | 161 fF | 11.8 um |
| 0.8 | 0.813 K | 96.8 pH | 8.12 K | 181 fF | 14.7 um |
| 0.6 | 0.695 K | 111.5 pH | 6.87 K | 215 fF | 20.1 um |
| 0.5 | 0.623 K | 123.1 pH | 6.10 K | 244 fF | 25.0 um |
| 0.4 | 0.540 K | 140.3 pH | 5.22 K | 287 fF | 33.3 um |

The wavelength column is now explicitly only

```text
lambda_fold = quasistatic well-disappearance scale.
```

It is not the detector cutoff.

## 8. Provisional quantum-stability time

Inside the retained cubic-MQT diagnostic,

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

Then exactly inside this diagnostic,

```math
\boxed{LC_{min,Q}=\tau_Q^2.}
```

This reduction remains useful, but the `alpha_Q~7.2` expression is not exact dissipative rf-SQUID MQT.

## 9. Exact scalar-R recovered-basin damping result

Linearized cold/recovered dynamics obey

```math
LC\ddot y+\frac{L}{R}\dot y+\kappa y=0.
```

Critical damping:

```math
\boxed{R_*=\frac12\sqrt{\frac{L}{C\kappa}}.}
```

Fastest scalar-Ohmic e-fold time:

```math
\boxed{\tau_{min}=\sqrt{LC/\kappa}.}
```

For `a=omega_0 t_avail>=1`, the exact linearized scalar-resistance interval is

```math
\boxed{
\frac{2a}{a^2+1}\le\frac{R}{R_*}\le a.
}
```

The old one-sided `R<t/(2C)` criterion was only the high-R underdamped edge. Too-small `R` is overdamped and slow.

## 10. Full nonlinear deterministic RCSJ checkpoint — current strongest dynamics

Canonical solver:

```text
calculations/full_dynamic_rfsquid.py
FULL_DYNAMIC_RCSJ_CHECKPOINT_2026-08-15.md
```

It directly integrates

```math
\boxed{
LC\ddot x+\frac{L}{R}\dot x+F[x,T_e(t)]=0
}
```

using the arbitrary-length temperature-dependent CPR, the realistic-skewness envelope, inertia, barrier re-formation and a finite photon-energy deposition rise.

### Static regression

The interpolated force reproduces

```text
rDelta=0.8 -> Tf ~0.812 K
rDelta=0.6 -> Tf ~0.694 K,
```

consistent with the retained static family.

### 14-um instantaneous-deposition result

For `A=100 um^2`:

```text
rDelta=0.8: deterministic capture begins near R~111 ohm.

rDelta=0.6: deterministic capture begins near R~32.7 ohm;
            an upper oscillatory/retrapping boundary appears near ~1.13 kOhm
            under the retained finite-time classification.
```

Thus full capture is again a dynamical window, not monotonic in scalar damping.

## 11. Finite rise time — decisive new control parameter

The photon deposition was generalized in `u=T_e^2` using an exponential energy source and the retained conditional clean-graphene cooling model.

At `14 um`, the current scalar-R model gives approximately

### `rDelta=0.8`

```text
rise 0 ps   -> lower capture R ~111 ohm
rise 5 ps   -> lower capture R ~166 ohm
rise 9 ps   -> lower capture R ~1.14 kOhm
rise 9.5–10 ps -> capture becomes very-high-R/settling sensitive or disappears from ordinary tested range.
```

### `rDelta=0.6`

```text
rise 0 ps   -> lower capture R ~32.7 ohm
rise 20 ps  -> lower capture R ~64 ohm
rise 30 ps  -> lower capture R ~559 ohm
rise ~32 ps -> no capture across a broad tested R range up to many kOhm.
```

Some successful finite-rise trajectories have

```math
\boxed{T_{peak}<T_f.}
```

Therefore static fold disappearance is **not necessary** for fast switching.

The mechanism is a nonadiabatic potential quench / metastable barrier-crossing process, with the fold as its quasistatic limit.

## 12. Sudden-quench energy threshold

Let `x_c` be the cold metastable minimum and `x_s(T)` the hot saddle below `T_f`. Define

```math
\boxed{
\mathcal B_q(T)
=U[x_s(T),T]-U[x_c,T]
=\int_{x_c}^{x_s(T)}F(x,T)dx.
}
```

The conservative held-hot sudden-quench threshold satisfies

```math
\boxed{\mathcal B_q(T_q)=0.}
```

Current full-CPR values:

```text
rDelta=0.8: Tq~0.718 K < Tf~0.812 K
rDelta=0.6: Tq~0.615 K < Tf~0.694 K.
```

For the same 100-um2 energy calibration:

```text
rDelta=0.8: lambda_fold~14.7 um; ideal lambda_quench~18.8 um
rDelta=0.6: lambda_fold~20.1 um; ideal lambda_quench~25.6 um.
```

This creates three conceptually different regimes:

```text
lambda < lambda_fold:
  quasistatic well disappearance energetically available.

lambda_fold < lambda < lambda_quench:
  well remains, but nonadiabatic inertial barrier crossing can be possible.

lambda > lambda_quench:
  cold phase point lies below the saddle in the fixed-hot conservative sudden-quench model.
```

`lambda_quench` is not a universal time-dependent detector impossibility bound.

Full finite-cooling scalar-R capture lies between `lambda_fold` and `lambda_quench`. Coarse scans give approximately

```text
rDelta=0.8: capture with R<=1 kOhm survives to ~16.2 um;
            very-weak-damping tested capture to ~16.7 um.

rDelta=0.6: capture with R<=1 kOhm survives to ~22.5 um;
            very-weak-damping tested capture to ~23.0 um.
```

These are model frontiers, not final spectral specifications.

Canonical records:

```text
SUDDEN_QUENCH_BOUND_2026-08-15.md
calculations/quench_energy_bound.py
```

## 13. Thermalization / geometry constraint

The finite-rise result makes the electronic rise time a first-order quantity.

Primary graphene literature gives useful scales:

```text
single hot Fermi-Dirac distribution can form on ~100–200 fs scales in established ultrafast regimes;
~100-meV excitation can enter a picosecond electron-phonon thermalization bottleneck;
2026 mid-IR graphene preprint reports ~2–3 ps photocurrent relaxation at room temperature.
```

These are not direct cryogenic GJJ rise-time calibrations.

Using the Huang characteristic `l_D~230 um`, `tau~75 ns` gives the cross-device scale

```math
D_{char}\sim0.705\;m^2/s.
```

Then

```text
0.6 um -> d^2/D ~0.5 ps
1.7 um -> ~4 ps
4 um   -> ~23 ps
25 um  -> ~0.9 ns.
```

If diffusion dominates the effective CPR rise,

```math
d_{max}\sim\sqrt{D\tau_{rise,max}}.
```

Current conditional design scales are roughly

```text
rDelta~0.8: tau_rise,max~9 ps  -> d_max~2.5 um
rDelta~0.6: tau_rise,max~30 ps -> d_max~4.6 um.
```

Thus a large optical collection area is compatible with the mechanism only if absorbed energy is delivered within a few micrometres of the Josephson-sensitive region, e.g. by localized antenna/cavity coupling.

Canonical record: `THERMAL_RISE_GEOMETRY_CLOSURE_2026-08-15.md`.

## 14. Prior-art boundary

No novelty claim is authorized.

Broad collisions already include

```text
superconducting MIR/LWIR single-photon detection
photon-heated graphene Josephson switching
thermal Ic suppression -> SQUID detection
single photon -> persistent superconducting flux memory
optically written persistent flux/vortices
transient Ic suppression -> rf-SQUID tipping/freeze
field-free Josephson directionality
illumination-driven phase batteries/vorticity
engineered proximity ABS / induced-gap thermal sensitivity
graphene thermal-transport optimization
generic dark-count vs timing/dead-time tradeoffs.
```

The general fast-parameter-change / rate-induced-tipping literature also needs a dedicated collision check before treating sub-fold nonadiabatic switching as mathematically new.

The only plausible paper route is a **specific superconducting photon-to-persistent-flux dynamic feasibility/optimality/impossibility closure** that survives the remaining physics and narrow patent/paper audit.

## 15. Immediate next work

Do not return to equilibrium material scans first.

### A. Deterministic dimensionless phase diagram

Use `full_dynamic_rfsquid.py` to map

```text
pulse rise time
x
pulse energy / wavelength
x
scalar damping
-> final basin.
```

Test whether different material points collapse when expressed through

```text
quench-energy margin M_q
rho = tau_rise/tau_phi
zeta = damping ratio
chi = cooling time/tau_phi.
```

### B. Spatial thermal model

Replace instantaneously uniform `T_e(t)` by at least a minimal heat equation and couple the phase to the weak-link-weighted local electronic state. Compare on-junction and far-from-junction absorption.

### C. Causal electromagnetic environment

Replace scalar `R` with

```math
Y(\omega,T_e)
```

and use the same environmental spectral density for classical damping, fluctuation-dissipation noise and dissipative MQT.

### D. Stochastic capture

Compute

```text
P_capture
P_wrong
P_return
capture-time distribution
```

before restoring detailed optical absorptance/readout/reset.

## 16. Verdict

**GO for continued theory. NO-GO for manuscript.**

The architecture remains theoretically alive. The dominant uncertainty has moved from photon energy and fold existence to **nonadiabatic energy delivery, spatial thermalization, damping/admittance and stochastic metastable capture**.
