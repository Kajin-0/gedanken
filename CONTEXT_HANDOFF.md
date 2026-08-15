# CONTEXT_HANDOFF.md — Live Agent Continuity Pointer

**Repository:** `Kajin-0/gedanken`  
**Active research experiment:** `experiments/03-superconducting-photon-flux-transduction/`  
**Updated:** 2026-08-15  
**Mode:** exploratory theory / falsification-first

> **LIVE `main` ALWAYS WINS.** Before every write, fetch current HEAD, inspect intervening commits, fetch the exact target blob, and never overwrite a stale SHA.

## Recovery order

1. root `AGENTS.md`;
2. Experiment 03 `AGENTS.md`;
3. Experiment 03 `CURRENT_STATE.md`;
4. `DYNAMIC_FOLD_GHOST_2026-08-15.md`;
5. `RCSJ_DAMPING_WINDOW_2026-08-15.md`;
6. `DARK_CAPTURE_ELIMINATION_2026-08-15.md`;
7. `HUANG_THERMAL_DWELL_CALIBRATION_2026-08-15.md`;
8. `SPECTRAL_STABILITY_PARETO_2026-08-15.md`;
9. `THERMAL_CONFINEMENT_GAP_CLOSURE_2026-08-15.md`;
10. `DERIVATION_LOG_CONTINUATION_2026-08-15.md`;
11. `CLAIM_LEDGER_CONTINUATION_2026-08-15.md`;
12. `LITERATURE_LEDGER_CONTINUATION_2026-08-15.md`;
13. legacy ledgers/checkpoints as linked from Experiment-03 `AGENTS.md`.

## One-sentence state

Experiment 03 is now a **dynamic photon-triggered persistent-flux problem**: a single absorbed LWIR photon must push a full proximity-JJ CPR beyond an rf-SQUID saddle-node **and keep it there long enough for the phase to traverse the critical-slowing bottleneck and enter the favored basin before cooling restores the original metastable well**.

Generation A uses external flux tilt and is not photovoltaic.

## Critical correction — static fold reach is not the detector cutoff

The static fold remains

```math
\mathcal I(x_f,T_f)=x_f-\delta,
\qquad
\partial_x\mathcal I(x_f,T_f)=1.
```

But near the fold

```math
\omega_m\propto|T-T_f|^{1/4},
```

so for any finite Ohmic damping

```math
\boxed{\zeta\propto|T-T_f|^{-1/4}\to\infty.}
```

The phase therefore experiences saddle-node critical slowing. A photon that only barely satisfies `T_pk>T_f` can be dynamically useless.

Local full-ghost scale:

```math
\boxed{
 t_{ghost}^{full}
\simeq
\frac{2\pi L}{R\kappa_c}
\sqrt{\frac{T_f-T_0}{T_{pk}-T_f}}.
}
```

After balancing this against recovered-basin underdamped relaxation and setting `C=C_min,Q`, the current optimistic diagnostic is

```math
\boxed{
 t_{dyn,min}
=2\sqrt{\frac{\pi}{\kappa_c}}\tau_Q
\left(
\frac{T_f-T_0}{T_{pk}-T_f}
\right)^{1/4}.
}
```

The current dynamic feasibility metric is therefore roughly

```math
\mathcal M_{fold}
=\frac{t_>(T_{pk},T_f)}{t_{dyn,min}}.
```

`M_fold>1` is only a diagnostic pass, not sufficient capture proof.

## Capacitance elimination

Inside the provisional cubic-MQT diagnostic,

```math
\boxed{
\tau_Q(D)
=\frac{\hbar\sqrt{\kappa_c}}
{\alpha_Q\Delta U_c}
W\!\left(
\frac{\alpha_Q\Delta U_c}{2\pi\hbar D}
\right),
}
```

with

```math
\boxed{LC_{min,Q}=\tau_Q^2.}
```

A phase-limited provisional spectral/dark/capture scaling near a smooth graphene fold is

```math
\boxed{
\lambda_{max}
\propto
\left[
\frac{t_c}{\ln(1/Dt_c)}
\right]^{4/3}.
}
```

Novelty is unknown; do not claim it.

## Exact scalar-R damping correction

Recovered-basin linearized RCSJ:

```math
LC\ddot y+\frac{L}{R}\dot y+\kappa y=0.
```

Critical resistance and fastest scalar-Ohmic e-fold time:

```math
\boxed{R_*=\frac12\sqrt{\frac{L}{C\kappa}},}
\qquad
\boxed{\tau_{min}=\sqrt{\frac{LC}{\kappa}}.}
```

For `a=omega0 t_avail>=1` the allowed scalar resistance is

```math
\boxed{
\frac{2a}{a^2+1}
\le\frac{R}{R_*}\le a.
}
```

Thus the old `R<t/(2C)` expression was only the high-R edge. Too little resistance is also slow because of overdamping.

Under the conditional Huang dwell mapping, the retuned family gives roughly

```text
R_* ~13–14 ohm
R_- ~1–2 ohm
R_+ ~0.23–0.36 kOhm.
```

Actual design must use a causal frequency-dependent admittance, not these as literal shunt values.

## Two-gap static family retained

Do not identify

```text
Delta_ind -> ABS/CPR/Ic(T)/fold
Delta_s   -> parent-electrode heat-escape/confinement scale.
```

Realistic-skewness, retuned `beta~0.8`, `A=100 um^2` family:

```text
rDelta  Tf[K]  L[pH]  barrier/kB[K]  Cmin[fF]  static absorbed-photon reach
1.0     0.905   87.8      9.10         161           11.8 um
0.8     0.813   96.8      8.12         181           14.7 um
0.6     0.695  111.5      6.87         215           20.1 um
0.5     0.623  123.1      6.10         244           25.0 um
0.4     0.540  140.3      5.22         287           33.3 um.
```

These wavelengths are static upper envelopes only.

## Conditional 14-um dynamic stress

Huang et al.'s `tau_ep~75 ns` fit at `T0=20 mK` is **not** treated as a measured temperature-independent hot-state lifetime. Mapping it to the local clean `T^4` cooling coefficient is explicitly conditional.

Under that conditional mapping, `A=100 um^2`, one absorbed `14 um` photon gives `T_pk~0.832 K`:

```text
rDelta=1.0: no static crossing
rDelta=0.8: overshoot ~0.019 K; t_>~4.1 ps; dynamic diagnostic~44.7 ps -> strongly fails stress
rDelta=0.6: overshoot ~0.137 K; t_>~37.6 ps; diagnostic~30.9 ps -> marginal pass
rDelta=0.5: larger pass margin.
```

Do **not** report `rDelta=0.6` as the actual 14-um design. The result only shows that finite-rate fold passage can move the boundary substantially relative to static energy accounting.

## Prior-art boundary

Broad novelty is closed for

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
generic dark-count vs jitter/dead-time tradeoffs.
```

The only plausible paper route is a **specific dynamic fold/calorimetric feasibility, optimality or impossibility closure** that survives exact dynamics, dissipative MQT and a narrow paper/patent audit.

## Immediate next task

Stop doing static material tables first.

Build the full deterministic time-dependent phase trajectory

```math
LC\ddot x
+\int K(t-t';T_e)\dot x(t')dt'
+F[x,T_e(t)]
=\xi(t),
```

in stages:

1. full CPR + realistic `T_e(t)` + scalar `R`, deterministic;
2. exact dynamic overshoot / basin entry / return threshold;
3. causal `Y(omega,T_e)` instead of scalar `R`;
4. same environmental spectral density in fluctuation-dissipation noise and dissipative MQT;
5. stochastic `P_capture`, `P_wrong`, `P_return` and timing distribution;
6. only then restore detailed 8–14-um absorptance and readout/reset.

## Publication state

**GO for continued theory. NO-GO for manuscript.**

Experiments 01 and 02 remain frozen/submission tracks.
