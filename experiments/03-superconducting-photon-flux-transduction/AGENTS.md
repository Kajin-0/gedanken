# AGENTS.md — Experiment 03 Recovery Protocol

**Experiment:** `03-superconducting-photon-flux-transduction`  
**Mode:** active exploratory theory / falsification-first  
**Manuscript status:** none; do not create one until `NOVELTY_GATES.md` is passed.

> Conversation history is non-authoritative when it conflicts with live repository state. Fetch `main` before every write.

## Recovery order — current frontier

1. `CURRENT_STATE.md`
2. `INITIAL_WIGNER_CAPTURE_CHECKPOINT_2026-08-15.md`
3. `QUANTUM_CAPTURE_MARGIN_CLOSURE_2026-08-15.md`
4. `QUANTUM_SPEED_SIGNAL_CLOSURE_2026-08-15.md`
5. `CAUSAL_ENVIRONMENT_REQUIREMENTS_2026-08-15.md`
6. `FULL_DYNAMIC_RCSJ_CHECKPOINT_2026-08-15.md`
7. `SUDDEN_QUENCH_BOUND_2026-08-15.md`
8. `PARAMETRIC_PHASE_WORK_2026-08-15.md`
9. `THERMAL_RISE_GEOMETRY_CLOSURE_2026-08-15.md`
10. `DERIVATION_LOG_DYNAMIC_2026-08-15.md`
11. `CLAIM_LEDGER_DYNAMIC_2026-08-15.md`
12. `LITERATURE_LEDGER_DYNAMIC_2026-08-15.md`
13. `RATE_INDUCED_TIPPING_COLLISION_2026-08-15.md`
14. older closure/ledger files linked from `CURRENT_STATE.md`
15. `NOVELTY_GATES.md`
16. `calculations/`.

Earlier static/short-junction checkpoints remain provenance/regression records, not the current preferred model.

## Current physical objective

Determine whether one absorbed LWIR photon can rapidly reshape a proximity-Josephson/rf-SQUID metastable potential and produce a **high-probability** transfer into a directionally favored persistent-flux basin while the same physical environment keeps cold false switching acceptably low.

Current internal description:

```text
photon-triggered nonadiabatic metastable superconducting flux latch
```

Generation A uses external flux tilt and is **not photovoltaic**. Generation B remains reserved for later zero-external-flux directionality.

## Current design criterion — probability, not one trajectory

The deterministic center trajectory is no longer the detector criterion. Let `Omega_R^0` be the target final basin pulled back to the initial phase plane and `rho_W` the cold initial phase-state distribution. The present probability object is

```math
\boxed{
P_{cap}^{init}
=\iint_{\Omega_R^0}\rho_W(x,u)\,dx\,du,
\qquad u=\dot x/\omega_c.
}
```

A physically meaningful future operating set must combine capture and dark stability:

```math
\boxed{
\mathcal O(p_*,D_*)
=\{\theta:P_{cap}(\theta)\ge p_*,\ \Gamma_{dark}(\theta)\le D_*\}.
}
```

`theta` includes photon energy/rise/spatial delivery, CPR/material parameters, `L`, `C`, flux tilt and the causal electromagnetic environment.

## Initial-state quantum checkpoint

The cold harmonic Wigner distribution has

```math
\sigma_x^2
=\frac{\hbar}{2C\bar\Phi^2\omega_c}
\coth\!\left(\frac{\hbar\omega_c}{2k_BT_0}\right),
\qquad
\sigma_{u}=\sigma_x,
```

with current values near

```text
rDelta=.8: sigma_x~0.11559 rad, hbar omega_c/(kBT0)~76.9
rDelta=.6: sigma_x~0.11499 rad, hbar omega_c/(kBT0)~65.4.
```

Thus the cold phase width is predominantly zero-point.

The finite-time basin is folded into multiple alternating strips. Raw tensor Gauss-Hermite on the discontinuous basin indicator is rejected as numerically poor. Current preferred integration:

```text
calculations/quantum_basin_integral.py   resolve all velocity strips and integrate Gaussian u mass analytically
calculations/quantum_basin_xgrid.py      nested standard-normal x grid with explicit Gaussian-tail bound
```

Validated x-grid workflow:

```text
.github/workflows/experiment03-quantum-xgrid.yml
run 31908931322
```

Current results for one absorbed `14 um` photon:

```text
rDelta=.6, rise=20 ps, R=75 ohm:
  Pcap(init)=0.813771–0.813778

rDelta=.6, rise=20 ps, R=120 ohm:
  current nx=33 value 0.966397, Gaussian-tail upper 0.966404;
  one further x refinement desired because nx17->33 moved ~0.0034

rDelta=.8, rise=5 ps, R=300 ohm:
  Pcap(init)=0.767736–0.767743

rDelta=.8, rise=5 ps, R=185 ohm:
  x-grid not yet converged; nx=9,17,33 -> 0.634,0.669,0.684.
```

The `rDelta=.6` family is currently much more robust to initial zero-point spread than the `.8` family at representative interior points.

**Critical quantum caveat:** this calculation uses the exact harmonic Wigner distribution at `t=0` but propagates each sample by the classical nonlinear RCSJ flow. It is a truncated-Wigner / semiclassical initial-state treatment, not exact nonlinear open-system quantum evolution.

## Quantum localization / action closure

Let

```math
\Delta U_c=(\bar\Phi^2/L)u_b,
\qquad
S=\Delta U_c/(\hbar\omega_c).
```

Then exactly inside the harmonic cold-well approximation,

```math
\boxed{
\sigma_x^2S
=\frac{u_b}{2\kappa_c}
\coth\!\left(\frac{\hbar\omega_c}{2k_BT_0}\right).
}
```

At low T:

```math
\boxed{\sigma_x^2S=u_b/(2\kappa_c).}
```

For a locally planar pulled-back basin boundary at signed normal distance `d_n`,

```math
\boxed{P_{cap}^{local}=\Phi(d_n/\sigma_x).}
```

Thus a deterministic boundary is locally a 50% probability contour, not a high-efficiency boundary.

## Quantum localization / speed / current identity

For intrinsic harmonic timescale `tau_0=1/omega_c` and persistent-state flux separation `DeltaPhi=zeta Phi0`, `DeltaI=zeta Phi0/L`,

```math
\boxed{
\sigma_x^2\tau_0\Delta I
=\frac{2\pi e\zeta}{\kappa_c}
\coth\!\left(\frac{\hbar\omega_c}{2k_BT_0}\right).
}
```

At low T the `coth` factor is one.

For local target probability `p`, basin distance `d_n`, and available time `t_avail>=g tau_0`, a necessary local condition is

```math
\boxed{
\Delta I\,t_{avail}
\ge
\frac{2\pi e\zeta g z_p^2}{\kappa_c d_n^2}
\coth\!\left(\frac{\hbar\omega_c}{2k_BT_0}\right),
\qquad z_p=\Phi^{-1}(p).
}
```

This identity does not use the provisional MQT ansatz. Do not claim novelty before collision audit.

## Full deterministic mechanism retained underneath probability map

Canonical solver:

```text
calculations/full_dynamic_rfsquid.py
```

It integrates

```math
LC\ddot x+\frac{L}{R}\dot x+F[x,T_e(t)]=0.
```

At 14 um the current deterministic finite-rise scales are roughly

```text
rDelta=.8: capture survives through ~9 ps; becomes weak-damping/settling sensitive near 9.5–10 ps
rDelta=.6: capture survives through ~30 ps; broadly absent near ~32 ps.
```

Successful trajectories can have `T_peak<T_f`; static fold disappearance is neither necessary nor sufficient.

The exact scalar-R phase-work identity is

```math
\boxed{
\frac{d}{dt}\left[\frac12LC\dot x^2+U(x,T)\right]
=U_T\dot T-\frac{L}{R}\dot x^2.
}
```

Damping hurts launch but helps final trapping, producing folded basin geometry rather than a monotonic capture threshold.

## Causal environment — mandatory next physical correction

A scalar resistor may remain a diagnostic, but the final environment must be one causal admittance `Y(omega)` used consistently in real-time damping, fluctuations and cold dissipative quantum escape.

For coordinate `q=barPhi x`, the linear open-system equation is

```math
C\ddot q(t)
+\int_{-\infty}^{t}y(t-t')\dot q(t')dt'
+\partial_qU
=I_N(t).
```

Using a two-sided symmetrized PSD convention,

```math
\boxed{
S_I^{sym}(\omega)
=\hbar|\omega|
\coth\!\left(\frac{\hbar|\omega|}{2k_BT_b}\right)
\operatorname{Re}Y(\omega).
}
```

The current phase frequencies are about `27–32 GHz`, so `h f/k_B~1.3–1.5 K`, comparable with the `~0.6–0.8 K` transient/fold temperatures. A purely classical white-Johnson bath is not a controlled approximation over the phase-mode band.

Caldeira–Leggett / AES physics also means dissipation modifies quantum escape itself. Do not optimize `R` for capture and then assign an independent MQT rate as if the knobs were unrelated.

## Static two-gap/material baseline retained

Never collapse

```text
Delta_ind -> weak-link ABS/CPR/Ic(T)/thermal sensitivity
Delta_s   -> parent-electrode hot-carrier escape/confinement.
```

Representative retuned `A=100 um^2`, realistic-skewness family:

```text
rDelta  Tf[K]  L[pH]  barrier/kB[K]  Cmin,Q[fF]  lambda_fold
1.0     0.905   87.8      9.10          161         11.8 um
0.8     0.813   96.8      8.12          181         14.7 um
0.6     0.695  111.5      6.87          215         20.1 um
0.5     0.623  123.1      6.10          244         25.0 um
0.4     0.540  140.3      5.22          287         33.3 um.
```

`lambda_fold` is only the quasistatic well-disappearance scale. The full dynamic spectral boundary can lie above it but below the ideal sudden-quench scale.

## Novelty discipline

Do not claim novelty for any of:

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
generic rate-induced tipping
quantum/classical probability of Josephson basin capture
noisy graphene-JJ metastable switching
frequency-dependent environment affecting Josephson retrapping
dissipation modifying macroscopic quantum tunneling.
```

The only plausible publication route is a detector-specific **single-LWIR-photon -> nonadiabatic proximity-JJ dynamics -> persistent flux** feasibility/optimality/impossibility closure with simultaneous capture/dark/environment constraints, if it survives the full open-system treatment and narrow paper/patent audit.

## Immediate work queue

1. Finish the probability-optimal scalar-R scouting scan and refine only the best points with nested x-grid integration.
2. Benchmark the semiclassical/truncated-Wigner propagation against an explicitly quantum nonlinear phase calculation.
3. Add a fluctuation-dissipation-consistent Ohmic bath to quantify the incremental effect of pulse-time bath fluctuations at fixed `R,L,C`.
4. Replace Ohmic `R` with a low-order causal `Y(omega)` and use the same spectral density for real-time noise and dissipative MQT.
5. Add spatial electronic heat stochasticity / weak-link-weighted local state.
6. Only after a nonempty `O(p_*,D_*)` survives, restore detailed optical absorptance, readout and reset.
7. Then perform the narrow paper + patent collision audit.

## Stop / reformulate conditions

Stop or reformulate if robust work shows any of:

- physically credible energy delivery is too slow for useful LWIR operation;
- no causal environment yields high target-basin probability while satisfying cold dark constraints;
- exact/open-system quantum evolution closes the apparent semiclassical capture corridor;
- spatial thermal transport removes the local heating advantage;
- reset/readout erases the operating distinction;
- narrow prior art already contains the same detector-specific mechanism/closure.

A negative bound is a valid result. Do not force the architecture to survive.

**Current verdict: GO for continued theory. NO-GO for manuscript.**
