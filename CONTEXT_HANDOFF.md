# CONTEXT_HANDOFF.md — Live Agent Continuity Pointer

**Repository:** `Kajin-0/gedanken`  
**Active research experiment:** `experiments/03-superconducting-photon-flux-transduction/`  
**Updated:** 2026-08-15  
**Mode:** exploratory theory / falsification-first

> **LIVE `main` ALWAYS WINS.** Fetch current HEAD before every write. Conversation history is non-authoritative when it conflicts with the repository.

## Recovery order

1. root `AGENTS.md`;
2. Experiment-03 `AGENTS.md`;
3. Experiment-03 `CURRENT_STATE.md`;
4. `FULL_DYNAMIC_RCSJ_CHECKPOINT_2026-08-15.md`;
5. `SUDDEN_QUENCH_BOUND_2026-08-15.md`;
6. `PARAMETRIC_PHASE_WORK_2026-08-15.md`;
7. `THERMAL_RISE_GEOMETRY_CLOSURE_2026-08-15.md`;
8. `RATE_INDUCED_TIPPING_COLLISION_2026-08-15.md`;
9. `DERIVATION_LOG_DYNAMIC_2026-08-15.md`;
10. `CLAIM_LEDGER_DYNAMIC_2026-08-15.md`;
11. older closure/ledger files linked from Experiment-03 `AGENTS.md`.

## One-sentence live state

Experiment 03 is now a **photon-triggered nonadiabatic metastable superconducting flux-latch problem**: a single absorbed LWIR photon rapidly reshapes a proximity-Josephson/rf-SQUID potential, the phase acquires a finite trajectory through the changing landscape, and successful detection means capture in the favored persistent-flux basin after recovery.

Generation A uses external flux tilt and is **not photovoltaic**.

## Most important mechanism correction

The quasistatic fold

```math
\mathcal I(x_f,T_f)=x_f-\delta,
\qquad
\partial_x\mathcal I(x_f,T_f)=1
```

remains the slow-drive organizing limit, but

```math
\boxed{T_{peak}\ge T_f}
```

is **neither necessary nor sufficient** for fast switching.

The full nonlinear solver shows successful sub-fold trajectories because rapid potential reshaping displaces/accelerates the phase before the barrier fully disappears.

Canonical solver:

```text
calculations/full_dynamic_rfsquid.py
```

At `A=100 um^2`, one absorbed `14 um` photon:

```text
instantaneous deposition:
  rDelta=0.8 -> lower scalar-R capture boundary ~111 ohm
  rDelta=0.6 -> lower boundary ~32.7 ohm; upper retrapping/oscillatory edge ~1.13 kOhm in current finite-time classification.

finite rise:
  rDelta=0.8 -> capture survives to roughly 9 ps; becomes weak-damping/settling sensitive near 9.5–10 ps
  rDelta=0.6 -> capture survives to roughly 30 ps; broadly absent near ~32 ps.
```

These are conditional model results, not device specifications.

## Three spectral scales

Define the sudden fixed-hot conservative quench barrier

```math
\mathcal B_q(T)
=U[x_s(T),T]-U(x_c,T).
```

The quench threshold satisfies

```math
\boxed{\mathcal B_q(T_q)=0.}
```

Current values:

```text
rDelta=0.8:
  Tq~0.718 K < Tf~0.812 K
  lambda_fold~14.7 um
  lambda_quench~18.8 um.

rDelta=0.6:
  Tq~0.615 K < Tf~0.694 K
  lambda_fold~20.1 um
  lambda_quench~25.6 um.
```

Current organization:

```math
\boxed{\lambda_{fold}<\lambda_{dynamic}<\lambda_{quench}}
```

for the retained model families.

`lambda_fold` is quasistatic well disappearance; `lambda_quench` is the ideal held-hot sudden-quench phase-energy scale; the real finite-rate boundary lies between. Do not report any as a universal detector cutoff.

## Exact phase-work accounting

For scalar-R RCSJ dynamics,

```math
\boxed{
\frac{d}{dt}
\left[\frac12LC\dot x^2+U(x,T)\right]
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

Use this as the preferred dynamic accounting language.

Damping has opposite roles:

```text
before crossing: excessive dissipation destroys launch energy;
after crossing: damping helps trap the target basin.
```

Therefore the correct next environment is a causal `Y(omega,T)` rather than a freely adjustable noiseless scalar resistor. The same environment must enter fluctuation-dissipation noise and dissipative MQT.

## Thermal-rise / geometry constraint

Primary graphene literature contains sub-ps to few-ps electronic redistribution regimes, so the current `~9–30 ps` rise windows are not obviously impossible. However, spatial delivery is geometry dependent.

Using only the Huang characteristic scale

```math
D_{char}\sim0.705\;m^2/s,
```

a simple `d^2/D` screen gives

```text
0.6 um ->~0.5 ps
1.7 um ->~4 ps
4 um   ->~23 ps
25 um  ->~0.9 ns.
```

Current conditional geometry scales:

```text
rDelta~0.8 -> useful absorption within ~2.5 um of JJ
rDelta~0.6 -> within ~4.6 um of JJ.
```

Treat these only as design/falsification scales. Optical collection area and thermally active distance can be decoupled by antenna/cavity design.

## Static two-gap family retained

Do not identify

```text
Delta_ind -> weak-link ABS/CPR/Ic(T)/thermal sensitivity
Delta_s   -> parent-electrode hot-carrier escape/confinement.
```

Retuned `A=100 um^2` static family:

```text
rDelta  Tf[K]  barrier/kB[K]  Cmin,Q[fF]  lambda_fold
1.0     0.905      9.10          161         11.8 um
0.8     0.813      8.12          181         14.7 um
0.6     0.695      6.87          215         20.1 um
0.5     0.623      6.10          244         25.0 um
0.4     0.540      5.22          287         33.3 um.
```

## Novelty boundary

Do not claim novelty for

```text
superconducting MIR/LWIR single-photon detection
photon-heated graphene Josephson switching
thermal Ic suppression -> SQUID detection
single photon -> persistent superconducting flux memory
optically written flux/vortices
transient Ic suppression -> rf-SQUID tipping/freeze
field-free Josephson directionality
illumination-driven phase batteries/vorticity
engineered proximity ABS / induced-gap sensitivity
graphene thermal-transport optimization
generic dark-count/timing tradeoffs
generic rate-induced tipping / fast loss of attractor tracking.
```

The only plausible paper route is a **detector-specific nonadiabatic persistent-flux feasibility/optimality/impossibility closure** that survives causal damping, dissipative MQT, stochastic capture, spatial heat transport and a narrow paper/patent audit.

## Current immediate work

1. Add phase-work diagnostics to full trajectories: `W_T`, `Q_R`, separatrix-energy margin and first crossing.
2. Build a dimensionless capture map versus pulse energy, rise time and damping; test collapse across `rDelta` families.
3. Add a minimal spatial electronic heat equation and compare on-JJ vs remote absorption.
4. Replace scalar `R` with causal `Y(omega,T)`.
5. Use the same spectral density for FDT noise and dissipative MQT.
6. Compute stochastic `P_capture`, `P_wrong`, `P_return` and timing distributions.
7. Restore detailed optical absorptance/readout/reset only after the dynamic core survives.

## CI note

Experiment-03 dynamic CI exists at

```text
.github/workflows/experiment03-dynamic-rfsquid.yml
```

The first smoke design incorrectly required a coarse CPR grid to reproduce fine capture boundaries. It has been revised to test numerical invariants. **Check the latest workflow status on live `main` before calling the dynamic stack validated.**

## Publication state

**GO for continued theory. NO-GO for manuscript.**

Experiments 01 and 02 remain frozen/submission tracks.
