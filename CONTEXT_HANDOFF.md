# CONTEXT_HANDOFF.md — Live Agent Continuity Pointer

**Repository:** `Kajin-0/gedanken`  
**Active experiment:** `experiments/03-superconducting-photon-flux-transduction/`  
**Updated:** 2026-08-15  
**Mode:** exploratory theory / falsification-first

> **LIVE `main` ALWAYS WINS.** Fetch current HEAD before every write. Conversation history is non-authoritative when it conflicts with the repository.

## Recovery order

1. root `AGENTS.md`;
2. Experiment-03 `AGENTS.md`;
3. Experiment-03 `CURRENT_STATE.md`;
4. `INITIAL_WIGNER_CAPTURE_CHECKPOINT_2026-08-15.md`;
5. `QUANTUM_CAPTURE_MARGIN_CLOSURE_2026-08-15.md`;
6. `QUANTUM_SPEED_SIGNAL_CLOSURE_2026-08-15.md`;
7. `CAUSAL_ENVIRONMENT_REQUIREMENTS_2026-08-15.md`;
8. `FULL_DYNAMIC_RCSJ_CHECKPOINT_2026-08-15.md`;
9. `SUDDEN_QUENCH_BOUND_2026-08-15.md`;
10. `PARAMETRIC_PHASE_WORK_2026-08-15.md`;
11. `DERIVATION_LOG_DYNAMIC_2026-08-15.md`;
12. `CLAIM_LEDGER_DYNAMIC_2026-08-15.md`;
13. `LITERATURE_LEDGER_DYNAMIC_2026-08-15.md`;
14. `NOVELTY_GATES.md`.

## One-sentence live state

Experiment 03 is now a **probabilistic nonadiabatic superconducting flux-latch problem**: one absorbed LWIR photon rapidly reshapes a proximity-Josephson/rf-SQUID potential, and useful detection requires a large fraction of the physical cold phase-state distribution to land in the favored persistent-flux basin while the same causal environment keeps dark switching acceptably low.

Generation A uses external flux tilt and is **not photovoltaic**.

## Deterministic mechanism retained underneath the probability problem

Current diagnostic dynamics:

```math
LC\ddot x+\frac{L}{R}\dot x+F[x,T_e(t)]=0.
```

Static fold remains the quasistatic limit, but `T_peak>=T_f` is neither necessary nor sufficient for fast switching.

Current absorbed-14-um finite-rise scales:

```text
rDelta=.8 -> deterministic capture survives roughly through 9 ps rise
rDelta=.6 -> deterministic capture survives roughly through 30 ps rise.
```

Sudden-quench organization:

```text
rDelta=.8: lambda_fold~14.7 um; lambda_quench~18.8 um
rDelta=.6: lambda_fold~20.1 um; lambda_quench~25.6 um
```

with current model hierarchy

```math
lambda_fold < lambda_dynamic < lambda_quench.
```

The exact scalar-R phase-work identity is

```math
\boxed{
\frac{d}{dt}\left[\frac12LC\dot x^2+U(x,T)\right]
=U_T\dot T-\frac{L}{R}\dot x^2.
}
```

Damping hurts launch but helps final capture/retrapping, producing folded finite-time basin geometry.

## Current detector criterion — target-basin probability

Let `Omega_R^0` be the target basin pulled back through the finite pulse map to the initial phase plane and define

```math
u=\dot x/\omega_c.
```

Current probability object:

```math
\boxed{
P_{cap}^{init}=\iint_{\Omega_R^0}\rho_W(x,u)\,dx\,du.
}
```

The pulled-back basin contains multiple alternating strips. Deterministic center-state success therefore does not imply high capture probability.

## Cold quantum width

For the harmonic cold well,

```math
\sigma_x^2
=\frac{\hbar}{2C\bar\Phi^2\omega_c}
\coth\!\left(\frac{\hbar\omega_c}{2k_BT_0}\right),
\qquad
\sigma_u=\sigma_x.
```

Current values at `T0=20 mK`:

```text
rDelta=.8: sigma_x~0.11559 rad; hbar omega_c/(kBT0)~76.9
rDelta=.6: sigma_x~0.11499 rad; hbar omega_c/(kBT0)~65.4.
```

The initial width is overwhelmingly zero-point.

## Validated geometry-aware initial-Wigner probabilities

Raw tensor Gauss-Hermite on the discontinuous basin indicator is rejected as numerically poor.

Current methods:

```text
quantum_basin_integral.py -> resolve all velocity basin strips and integrate Gaussian u mass analytically
quantum_basin_xgrid.py    -> nested normal-coordinate x grid + explicit Gaussian-tail bound
```

Workflow:

```text
experiment03-quantum-xgrid.yml
run 31908931322 -> PASS.
```

Current one-photon 14-um results:

```text
rDelta=.6, rise=20 ps, R=75 ohm:
  Pcap(init)=0.813771–0.813778

rDelta=.6, rise=20 ps, R=120 ohm:
  nx=33 Pcap(init)=0.966397; tail upper 0.966404
  one further x refinement desirable because nx17->33 shifted ~0.0034

rDelta=.8, rise=5 ps, R=300 ohm:
  Pcap(init)=0.767736–0.767743

rDelta=.8, rise=5 ps, R=185 ohm:
  not yet x-converged; nx=9,17,33 ->0.634,0.669,0.684.
```

Thus the `rDelta=.6` family is presently substantially more robust to initial zero-point spread than `.8` at representative interior points.

A coarse probability-vs-R scan also finds the `.8` family is non-monotonic: scouting probability rises from ~0.59 at 170 ohm to ~0.875 near 400 ohm, then falls by 900 ohm. The probability optimum is therefore not the deterministic onset and not the weakest damping.

## Important quantum caveat

The initial harmonic Wigner state is exact for the assumed cold quadratic well, but current basin calculations propagate samples with the classical nonlinear RCSJ map. They are a **truncated-Wigner / semiclassical initial-state approximation**, not exact nonlinear quantum evolution.

The cold action scale is only `DeltaU/(hbar omega_c)~5.3`, so percent-level quantum corrections cannot be assumed negligible.

A closed-system fixed-hot exact quantum benchmark now exists:

```text
calculations/quantum_quench_benchmark.py
.github/workflows/experiment03-quantum-quench.yml
```

First quick-grid result: exact Schrodinger vs classical-Wigner right-of-saddle probability differs by as much as ~4.1 percentage points for `rDelta=.8` and ~2.0 points for `.6` over 5–40 ps. A finer run is in progress / must be checked on live `main` before treating these numbers as final.

## Exact harmonic closures

Define

```math
\Delta U_c=(\bar\Phi^2/L)u_b,
\qquad
S=\Delta U_c/(\hbar\omega_c).
```

Then

```math
\boxed{
\sigma_x^2S
=\frac{u_b}{2\kappa_c}
\coth\!\left(\frac{\hbar\omega_c}{2k_BT_0}\right).
}
```

At low temperature,

```math
\sigma_x^2S=u_b/(2\kappa_c).
```

For a locally planar pulled-back basin boundary at normal distance `d_n`,

```math
\boxed{P_{cap}^{local}=\Phi(d_n/\sigma_x).}
```

Therefore the deterministic boundary is locally a 50% quantum-capture contour.

With persistent-state flux separation `DeltaPhi=zeta Phi0`, circulating-current separation `DeltaI=zeta Phi0/L`, and `tau0=1/omega_c`,

```math
\boxed{
\sigma_x^2\tau_0\Delta I
=\frac{2\pi e\zeta}{\kappa_c}
\coth\!\left(\frac{\hbar\omega_c}{2k_BT_0}\right).
}
```

At low T, quantum localization, intrinsic phase speed and circulating-current state scale cannot all be independently improved by changing `L` and `C`.

If target local probability `p` requires `d_n>=z_p sigma_x` and `t_avail>=g tau0`, then

```math
\boxed{
\Delta I\,t_{avail}
\ge
\frac{2\pi e\zeta g z_p^2}{\kappa_c d_n^2}
\coth\!\left(\frac{\hbar\omega_c}{2k_BT_0}\right).
}
```

This is local/harmonic, not a global result for folded basins.

## Causal environment — mandatory next physical correction

A physical damping environment must generate the associated fluctuations and modify quantum escape.

For `q=barPhi x`:

```math
C\ddot q(t)
+\int_{-\infty}^{t}y(t-t')\dot q(t')dt'
+\partial_qU
=I_N(t).
```

Using a two-sided symmetrized convention,

```math
\boxed{
S_I^{sym}(\omega)
=\hbar|\omega|
\coth\!\left(\frac{\hbar|\omega|}{2k_BT_b}\right)
\operatorname{Re}Y(\omega).
}
```

Current phase frequencies `~27–32 GHz` correspond to `hf/k_B~1.3–1.5 K`, comparable with the `~0.6–0.8 K` transient/fold temperatures. A classical white-Johnson bath is not controlled over the phase band.

The same `Y(omega)` must ultimately govern

```text
real-time damping/memory,
pulse-time fluctuations,
reactive loading,
and dissipative quantum escape.
```

Do not optimize noiseless scalar `R` and independently assign MQT.

## Two-gap material rule retained

Do not identify

```text
Delta_ind -> weak-link ABS/CPR/Ic(T)/thermal sensitivity
Delta_s   -> parent-electrode hot-carrier escape/confinement.
```

Representative retuned static family remains

```text
rDelta .8: Tf~0.813 K, L~96.8 pH, barrier~8.12 K, provisional Cmin~181 fF
rDelta .6: Tf~0.695 K, L~111.5 pH, barrier~6.87 K, provisional Cmin~215 fF.
```

The provisional capacitances come from the old cubic-MQT screening model and must eventually be replaced by dissipative escape using the same causal environment.

## Novelty boundary

Do not claim novelty for generic

```text
superconducting MIR/LWIR single-photon detection
photon-heated graphene Josephson switching
single-photon persistent flux memory
rf-SQUID tipping by Ic suppression
phase-battery/vorticity switching
rate-induced tipping
quantum/classical probability of Josephson basin capture
noisy graphene-JJ switching
frequency-dependent retrapping
dissipation-modified MQT.
```

The only plausible paper route is a detector-specific **single absorbed LWIR photon -> nonadiabatic proximity-JJ dynamics -> persistent superconducting flux** feasibility/optimality/impossibility closure with simultaneous capture, dark, thermal-rise and causal-environment constraints.

## Immediate next work

1. Finish focused probability-vs-R scouting for `rDelta=.6`; refine the best `.6/.8` scalar-R points with nested x-grid integration.
2. Check the finer exact-quantum quench benchmark and quantify the truncation-Wigner error.
3. Add one fluctuation-dissipation-consistent Ohmic bath and quantify the change in capture probability relative to initial-state-only results.
4. Replace scalar Ohmic damping by a low-order causal `Y(omega)` and use the same bath in dissipative MQT.
5. Add spatial electronic heat stochasticity / weak-link-weighted local state.
6. Determine whether

```math
\mathcal O(p_*,D_*)
=\{\theta:P_{cap}(\theta)\ge p_*,\Gamma_{dark}(\theta)\le D_*\}
```

remains nonempty.
7. Only then restore detailed optical coupling/readout/reset and perform the narrow paper/patent audit.

## Publication state

**GO for continued theory. NO-GO for manuscript.**

Experiments 01 and 02 remain frozen/submission tracks.
