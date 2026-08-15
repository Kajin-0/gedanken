# AGENTS.md — Experiment 03 Recovery Protocol

**Experiment:** `03-superconducting-photon-flux-transduction`  
**Mode:** active exploratory theory / falsification-first  
**Manuscript status:** none; do not create one until `NOVELTY_GATES.md` is passed.

> Conversation history is non-authoritative when it conflicts with live repository state. Fetch `main` before every write.

## Recovery order — read this first

1. `CURRENT_STATE.md`
2. `FULL_DYNAMIC_RCSJ_CHECKPOINT_2026-08-15.md`
3. `SUDDEN_QUENCH_BOUND_2026-08-15.md`
4. `PARAMETRIC_PHASE_WORK_2026-08-15.md`
5. `THERMAL_RISE_GEOMETRY_CLOSURE_2026-08-15.md`
6. `RATE_INDUCED_TIPPING_COLLISION_2026-08-15.md`
7. `DARK_CAPTURE_ELIMINATION_2026-08-15.md`
8. `RCSJ_DAMPING_WINDOW_2026-08-15.md`
9. `HUANG_THERMAL_DWELL_CALIBRATION_2026-08-15.md`
10. `SPECTRAL_STABILITY_PARETO_2026-08-15.md`
11. `THERMAL_CONFINEMENT_GAP_CLOSURE_2026-08-15.md`
12. `DERIVATION_LOG_DYNAMIC_2026-08-15.md`
13. `CLAIM_LEDGER_DYNAMIC_2026-08-15.md`
14. `DERIVATION_LOG_CONTINUATION_2026-08-15.md`
15. `CLAIM_LEDGER_CONTINUATION_2026-08-15.md`
16. `LITERATURE_LEDGER_CONTINUATION_2026-08-15.md`
17. `DERIVATION_LOG.md`, `CLAIM_LEDGER.md`, `LITERATURE_LEDGER.md`
18. `ASSUMPTIONS.md`
19. `NOVELTY_GATES.md`
20. `calculations/`.

Earlier static/short-junction checkpoints are regression/provenance records, not the current preferred model.

## Current physical objective

Determine whether a **single absorbed LWIR photon** can rapidly reshape a proximity-Josephson/rf-SQUID metastable potential so that the phase is transferred into a directionally favored basin and retained as persistent superconducting flux, while cold false switching remains extremely low.

Current internal description:

```text
photon-triggered nonadiabatic metastable superconducting flux latch
```

Generation A uses external flux tilt and is **not photovoltaic**. Generation B remains reserved for later zero-external-flux directionality.

## Mechanism — current

```text
LWIR photon
 -> electronic thermalization + spatial delivery near weak link
 -> temperature-dependent full CPR changes rapidly
 -> phase coordinate is displaced / accelerated
 -> trajectory may cross a finite barrier OR a vanished fold
 -> potential recovers during cooling
 -> phase is captured in favored basin
 -> persistent superconducting flux remains.
```

The rf-SQUID saddle-node/fold is the quasistatic organizing limit. **Static fold disappearance is neither necessary nor sufficient for the fast-pulse regime.**

## Static fold regression

```math
I_* = \Phi_0/(2\pi L),
\qquad
\mathcal I=I_s/I_*,
\qquad
F=x-\delta-\mathcal I,
```

```math
\boxed{\mathcal I(x_f,T_f)=x_f-\delta,}
\qquad
\boxed{\partial_x\mathcal I(x_f,T_f)=1.}
```

Near a smooth fold:

```math
\Delta U\propto|p-p_f|^{3/2},
\qquad
\omega_m\propto|p-p_f|^{1/4}.
```

## Two-gap rule — mandatory

Never collapse

```text
Delta_ind  induced/minigap controlling ABS/CPR/Ic(T)/thermal sensitivity
Delta_s    parent-electrode gap controlling hot-carrier escape/confinement.
```

Current plausible direction:

```text
moderately reduced Delta_ind
+ high parent Delta_s
+ retuned L/C
+ localized optical energy delivery within a few micrometres of the JJ
+ causal dynamical admittance compatible with capture and cold stability.
```

## Retained static family

Realistic-skewness, retuned `beta~0.8`, `A=100 um^2`:

```text
rDelta  Tf[K]  L[pH]  barrier/kB[K]  Cmin,Q[fF]  lambda_fold
1.0     0.905   87.8      9.10          161         11.8 um
0.8     0.813   96.8      8.12          181         14.7 um
0.6     0.695  111.5      6.87          215         20.1 um
0.5     0.623  123.1      6.10          244         25.0 um
0.4     0.540  140.3      5.22          287         33.3 um.
```

`lambda_fold` is only the quasistatic well-disappearance scale.

## Full deterministic dynamics — strongest current calculation

Canonical solver:

```text
calculations/full_dynamic_rfsquid.py
```

It integrates

```math
\boxed{LC\ddot x+\frac{L}{R}\dot x+F[x,T_e(t)]=0}
```

with full interpolated arbitrary-length CPR, current interface-skewness envelope, inertia, finite energy-deposition rise, cooling, barrier reformation and basin classification.

At `A=100 um^2`, one absorbed `14 um` photon:

```text
instantaneous deposition:
  rDelta=0.8 -> lower scalar-R capture boundary ~111 ohm
  rDelta=0.6 -> lower boundary ~32.7 ohm; upper oscillatory/retrapping boundary ~1.13 kOhm in current classification.

finite rise:
  rDelta=0.8 -> ordinary capture survives through ~9 ps; becomes weak-damping/settling sensitive by ~9.5–10 ps
  rDelta=0.6 -> capture survives through ~30 ps; broadly absent around ~32 ps.
```

Successful trajectories can have `T_peak<T_f`. Do not use `T_peak>=T_f` as a detection criterion.

## Sudden-quench energy scale

Let `x_c` be the cold metastable coordinate and `x_s(T)` the hot saddle. Define

```math
\boxed{
\mathcal B_q(T)
=U[x_s(T),T]-U(x_c,T)
=\int_{x_c}^{x_s(T)}F(x,T)dx.
}
```

The fixed-hot conservative quench threshold is

```math
\boxed{\mathcal B_q(T_q)=0.}
```

Current values:

```text
rDelta=0.8: Tq~0.718 K, Tf~0.812 K, lambda_fold~14.7 um, lambda_quench~18.8 um
rDelta=0.6: Tq~0.615 K, Tf~0.694 K, lambda_fold~20.1 um, lambda_quench~25.6 um.
```

Current model hierarchy:

```math
\boxed{\lambda_{fold}<\lambda_{dynamic}<\lambda_{quench}.}
```

This is a model organization, not a universal theorem.

## Exact parametric phase-work identity

For scalar-R dynamics,

```math
\boxed{
\frac{d}{dt}\left[\frac12LC\dot x^2+U(x,T)\right]
=U_T(x,T)\dot T-\frac{L}{R}\dot x^2.
}
```

While a saddle exists,

```math
\mathcal E_s
=\frac12LC\dot x^2+U(x,T)-U[x_s(T),T],
```

```math
\boxed{
\dot{\mathcal E}_s
=[U_T(x,T)-U_T(x_s,T)]\dot T
-\frac{L}{R}\dot x^2.
}
```

This is the preferred accounting language for the next dynamic reduction.

Damping has two conflicting roles:

```text
launch/crossing -> excessive dissipation suppresses useful phase energy
capture/retrapping -> sufficient dissipation helps trap the target basin.
```

Hence a single broadband scalar `R` is unlikely to be the physical optimum; any causal `Y(omega,T)` must be used consistently in FDT noise and dissipative MQT.

## Provisional dark-stability reduction

Inside the **non-dissipative/cubic diagnostic only**:

```math
\boxed{
\tau_Q(D)
=\frac{\hbar\sqrt{\kappa_c}}
{\alpha_Q\Delta U_c}
W\!\left(\frac{\alpha_Q\Delta U_c}{2\pi\hbar D}\right),
}
```

```math
\boxed{LC_{min,Q}=\tau_Q^2.}
```

Do not treat `alpha_Q~7.2` as exact dissipative rf-SQUID MQT.

## Thermal-rise / geometry requirement

Primary graphene literature contains sub-ps to few-ps electronic response regimes, but a cryogenic GJJ calibration is missing.

Using Huang's characteristic `l_D~230 um`, `tau~75 ns` gives only the cross-device scale

```math
D_{char}\sim0.705\;m^2/s.
```

Simple `d^2/D` gives approximately

```text
0.6 um ->0.5 ps
1.7 um ->4 ps
4 um   ->23 ps
25 um  ->0.9 ns.
```

Current conditional rise windows therefore correspond roughly to energy delivery within

```text
rDelta~0.8 -> few-micrometre scale (~2.5 um)
rDelta~0.6 -> few-micrometre scale (~4.6 um).
```

Large optical aperture is acceptable only if optical coupling localizes the useful electronic heating near the Josephson-sensitive region.

## Novelty discipline

Broad novelty is closed for:

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
generic dark-count vs timing/dead-time tradeoffs
generic rate-induced tipping / loss of attractor tracking under fast parameter change.
```

The only plausible publication route is a **detector-specific nonadiabatic persistent-flux feasibility/optimality/impossibility closure** that survives the remaining dynamics and a narrow paper/patent audit.

## Numerical regression state

Workflow:

```text
.github/workflows/experiment03-dynamic-rfsquid.yml
```

Pinned environment:

```text
Python 3.12.13
NumPy 2.5.1
SciPy 1.18.0.
```

The initial dynamic CI failed because a deliberately coarse smoke grid was asked to reproduce fine-grid capture brackets. This was a test-design error, not a scientific contradiction. `full_dynamic_smoke.py` now tests numerical invariants; **recheck the latest workflow before declaring the dynamic stack validated.**

## Immediate work queue

Do not return to static parameter scanning first.

1. Extend full trajectories with exact phase-work diagnostics: `W_T`, `Q_R`, separatrix-energy margin, first crossing and final basin.
2. Build a dimensionless deterministic map in pulse energy/rise time/damping and test collapse across material points.
3. Build a minimal spatial electronic heat equation and compare on-junction vs far-from-junction absorption.
4. Replace scalar `R` with causal `Y(omega,T_e)` / memory kernel.
5. Use that same environmental spectral density for FDT noise and dissipative MQT.
6. Compute stochastic `P_capture`, `P_wrong`, `P_return` and timing distributions.
7. Only then restore detailed 8–14-um absorptance, readout and reset.
8. If a compact result survives, perform the narrow paper + patent collision audit.

## Stop / reformulate conditions

Stop or reformulate if robust work shows any of:

- physically credible energy-delivery rise is too slow for the desired LWIR range;
- no causal environment permits launch + capture without unacceptable cold noise/MQT;
- spatial thermal transport removes the local heating advantage;
- stochastic wrong-basin/retrapping probabilities are unacceptable;
- reset/readout erases the operating distinction;
- narrow prior art already contains the same mechanism and no independent closure survives.

A negative bound is a valid result. Do not force the architecture to survive.

**Current verdict: GO for continued theory. NO-GO for manuscript.**
